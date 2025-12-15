---
title: News
nav:
  order: 0
  tooltip: Lab news
---

# {% include icon.html icon="fa-solid fa-feather-pointed" %}News

<p style="text-align: center;">News and updates from the QPI lab.</p>

{% include section.html %}

{% include search-box.html %}

{% include tags.html tags=site.tags %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}
