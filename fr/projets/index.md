---
title: Projets
alt: /projects/
nav:
  order: 1
  tooltip: Projets de recherche en cours
---

# {% include icon.html icon="fa-solid fa-brain" %}Projets

Un même fil relie nos projets, de la danse à la ménopause : trouver des biomarqueurs qui indiquent qui est sur une mauvaise trajectoire de vieillissement, et ce qu'on peut faire pour aider.

Chaque projet est une cohorte que nous imageons avec notre protocole d'IRM quantitative. Les logiciels que nous développons en chemin sont sur notre page [Outils](../outils).

{% include section.html %}

{% assign projects = site.data.projects | where: "lang", "fr" %}
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
