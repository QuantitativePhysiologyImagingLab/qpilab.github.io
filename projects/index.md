---
title: Projects
alt: /fr/projets/
nav:
  order: 1
  tooltip: Current research projects
---

# {% include icon.html icon="fa-solid fa-brain" %}Projects

A common thread runs through our projects, from dance to menopause: finding biomarkers that tell us who is on an unfavourable aging trajectory, and what we can do to help.

Each project is a cohort we scan with our quantitative MRI protocol. The software we build along the way is on our [Tools](../tools) page.

{% include section.html %}

{% assign projects = site.data.projects | where: "lang", "en" %}
{% for p in projects %}
{% capture text %}
_{{ p.subtitle }}_

{{ p.description }}

{% include tags.html tags=p.tags %}
{% endcapture %}
{% assign odd = forloop.index | modulo: 2 %}
{% if odd == 0 %}
{% include feature.html image=p.image title=p.title text=text flip=true %}
{% else %}
{% include feature.html image=p.image title=p.title text=text %}
{% endif %}
{% endfor %}
