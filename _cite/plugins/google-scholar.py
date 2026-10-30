import re
import time
import html
import json
import urllib.parse
import urllib.request
from util import *

# scrapes the public profile directly (no API key needed)
# shortcut: Scholar may serve a captcha to CI runners; if so, run `python _cite/cite.py` locally and commit
BASE = "https://scholar.google.ca/citations"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept-Language": "en",
}


def fetch(url, headers=HEADERS):
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        page = response.read().decode("utf8")
    if "gs_captcha" in page or "unusual traffic" in page:
        raise Exception("Google Scholar served a captcha, try again later")
    return page


def text(fragment):
    return html.unescape(re.sub(r"<.*?>", "", fragment)).strip()


def is_author(name, last, initial):
    """does a Scholar-style name ("CJ Gauthier", "Claudine J Gauthier") match"""
    parts = name.replace(".", " ").split()
    return len(parts) > 1 and parts[-1].lower() == last and parts[0][0].lower() == initial


@log_cache
@cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
def list_works(_id):
    works = []
    start = 0
    while True:
        page = fetch(f"{BASE}?hl=en&user={_id}&view_op=list_works&sortby=pubdate&cstart={start}&pagesize=100")
        rows = re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page, re.S)
        for row in rows:
            link = re.search(r'href="[^"]*citation_for_view=([^"&]+)"', row)
            gray = re.findall(r'<div class="gs_gray">(.*?)</div>', row, re.S)
            year = re.search(r'gsc_a_h gsc_a_hc gs_ibl">(\d*)<', row)
            works.append({
                "citation_id": html.unescape(link.group(1)) if link else "",
                "title": text(re.search(r'class="gsc_a_at">(.*?)</a>', row, re.S).group(1)),
                "authors": text(gray[0]) if gray else "",
                "publication": re.sub(r",\s*\d{4}$", "", text(gray[1])) if len(gray) > 1 else "",
                "year": year.group(1) if year else "",
            })
        if len(rows) < 100:
            return works
        start += 100
        time.sleep(2)


def simplify(title):
    return re.sub(r"[^a-z0-9]", "", title.lower())


@cache.memoize(name=__file__ + "crossref", expire=90 * (60 * 60 * 24))
def crossref_detail(title):
    """full author list from Crossref, if it has a work with exactly this title"""
    query = urllib.parse.urlencode({"query.bibliographic": title, "rows": 3})
    response = json.loads(fetch(f"https://api.crossref.org/works?{query}", {"User-Agent": "qpilab-website (mailto:claudine.gauthier@umontreal.ca)"}))
    for item in get_safe(response, "message.items", []):
        if simplify(get_safe(item, "title.0", "")) == simplify(title):
            authors = [" ".join(filter(None, [a.get("given", ""), a.get("family", "")])) for a in item.get("author", [])]
            if authors:
                return {"authors": ", ".join(authors), "link": item.get("URL", "")}
    return None


@cache.memoize(name=__file__ + "detail", expire=90 * (60 * 60 * 24))
def scholar_detail(_id, citation_id):
    """full author list and publisher link from the work's Scholar page"""
    time.sleep(5)
    page = fetch(f"{BASE}?view_op=view_citation&hl=en&user={_id}&citation_for_view={citation_id}")
    fields = dict(
        (text(k), text(v))
        for k, v in re.findall(r'<div class="gsc_oci_field">(.*?)</div><div class="gsc_oci_value">(.*?)</div>', page, re.S)
    )
    link = re.search(r'class="gsc_oci_title_link" href="([^"]+)"', page)
    return {
        "authors": fields.get("Authors", ""),
        "link": html.unescape(link.group(1)) if link else "",
    }


def main(entry):
    """
    receives single list entry from google-scholar data file
    returns list of sources to cite (only works with the author first or last, if "author" is set)
    """

    _id = get_safe(entry, "gsid", "")
    if not _id:
        raise Exception('No "gsid" key')

    # e.g. "C Gauthier" -> match last name "gauthier" with first initial "c"
    author = get_safe(entry, "author", "").split()
    last, initial = (author[-1].lower(), author[0][0].lower()) if author else ("", "")

    sources = []
    for work in list_works(_id):
        authors = [a.strip() for a in work["authors"].split(",") if a.strip()]
        link = ""

        # list view truncates long author lists with "..."
        if authors and authors[-1] == "...":
            if last and is_author(authors[0], last, initial):
                authors = authors[:-1]
            else:
                try:
                    detail = crossref_detail(work["title"]) or scholar_detail(_id, work["citation_id"])
                except Exception as e:
                    # can't tell who the last author is, so leave it out this run
                    log(f"Skipping \"{work['title']}\": {e}", indent=3, level="WARNING")
                    continue
                authors = [a.strip() for a in detail["authors"].split(",") if a.strip()] or authors[:-1]
                link = detail["link"]

        if last and not (
            authors and (is_author(authors[0], last, initial) or is_author(authors[-1], last, initial))
        ):
            continue

        sources.append({
            # no "id": Scholar ids aren't Manubot-citeable, so keep these details as the citation
            "title": work["title"],
            "authors": authors,
            "publisher": work["publication"],
            "date": (work["year"] + "-01-01") if work["year"] else "",
            "link": link or f"{BASE}?view_op=view_citation&hl=en&user={_id}&citation_for_view={work['citation_id']}",
            **{k: v for k, v in entry.items() if k not in ("gsid", "author")},
        })

    return sources


if __name__ == "__main__":
    assert is_author("CJ Gauthier", "gauthier", "c")
    assert is_author("Claudine J. Gauthier", "gauthier", "c")
    assert not is_author("L Gauthier", "gauthier", "c")
    assert not is_author("...", "gauthier", "c")
    print("ok")
