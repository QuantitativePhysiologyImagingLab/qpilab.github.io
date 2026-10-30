---
title: Équipe
alt: /team/
nav:
  order: 2
  tooltip: Notre équipe
---

# {% include icon.html icon="fa-solid fa-users" %}Équipe

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}
{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)^(?!alumni$)" %}

