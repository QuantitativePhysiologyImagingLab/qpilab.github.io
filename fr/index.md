---
logos-top: true
alt: /
---

# IRM quantitative de l'axe cœur-cerveau

<img src="{{ "images/heart-brain-fr.svg" | relative_url }}" alt="Le cœur et le cerveau reliés par une artère, avec les mesures que nous imageons : CBF, CVR, pulsatilité, OEF et CMRO2" style="width: 100%; margin: 20px 0 40px;">

Le cœur nourrit le cerveau. Quand le système cardiovasculaire vieillit ou devient malade, l'apport sanguin et le métabolisme énergétique du cerveau changent aussi, souvent des années avant que la mémoire ou la pensée soient touchées.

Le **Laboratoire d'imagerie physiologique quantitative** développe et applique l'IRM quantitative pour mesurer directement ces changements : la quantité de sang qui atteint le cerveau, la réponse de ses vaisseaux, et la quantité d'oxygène qu'il extrait et consomme. Ces mesures nous permettent de relier la santé du cœur à celle du cerveau, et de repérer qui est sur une mauvaise trajectoire de vieillissement pendant qu'il est encore temps d'intervenir.

Dirigé par la [Pre Claudine Gauthier](../members/claudine-gauthier) à l'[Université de Montréal](https://www.umontreal.ca), le laboratoire est affilié au Centre de recherche de l'[Institut de Cardiologie de Montréal](https://www.icm-mhi.org) et au [Centre EPIC](https://www.centreepic.org).

{% include logos.html %}

{% capture content %}
**Nous recrutons!** Stagiaires de premier cycle et étudiants à la maîtrise et au doctorat en physique, génie, informatique, neurosciences, kinésiologie ou médecine : [voyez comment vous joindre au labo](joindre).
{% endcapture %}
{% include alert.html type="tip" content=content %}

{% include section.html %}

## Ce que nous mesurons

- **CBF**, le débit sanguin cérébral, par marquage de spins artériels (ASL)
- **CVR**, la réactivité cérébrovasculaire : la capacité des vaisseaux à se dilater lors d'un défi respiratoire
- **Pulsatilité** : la part du pouls cardiaque qui atteint les petits vaisseaux fragiles du cerveau
- **OEF**, la fraction d'extraction d'oxygène, à partir de la susceptibilité magnétique des veines (QSM) ou de l'IRMf calibrée
- **CMRO2**, le taux métabolique cérébral d'oxygène : selon le principe de Fick, CMRO2 = CBF × OEF × contenu artériel en oxygène
- **Myéline, fer et microstructure de la matière blanche**, par MTsat, R2\*, QSM et IRM de diffusion

{% capture content %}
{% include figure.html image="images/maps/cbf.jpg" caption="Débit sanguin cérébral (ASL)" %}
{% include figure.html image="images/maps/qsm.jpg" caption="Susceptibilité magnétique (QSM)" %}
{% include figure.html image="images/maps/cvr.jpg" caption="Réactivité cérébrovasculaire (CVR)" %}
{% include figure.html image="images/maps/mtsat.jpg" caption="Myéline (MTsat)" %}
{% include figure.html image="images/maps/r2star.jpg" caption="R2\*, sensible au fer" %}
{% include figure.html image="images/maps/lesions.jpg" caption="Lésions de la matière blanche" %}
{% endcapture %}

{% include grid.html content=content %}

{% include section.html %}

## Notre approche

{% capture col1 %}
### Des marqueurs précoces
Des changements vasculaires et métaboliques, comme un CBF plus faible, une réactivité réduite ou une OEF altérée, peuvent apparaître avant les atteintes visibles en IRM classique. Dans la maladie coronarienne, nous les avons observés chez des personnes considérées comme cognitivement normales.
{% endcapture %}

{% capture col2 %}
### Des différences aux trajectoires
À l'aide de modèles informatiques et de l'intelligence artificielle, nous combinons ces mesures en profils de vulnérabilité pour comprendre quelles différences annoncent un déclin cognitif.
{% endcapture %}

{% capture col3 %}
### Intervenir avant le déclin
Avec des essais comme NeuroDance, nous vérifions si l'exercice, la danse et la stimulation cognitive peuvent modifier la trajectoire du vieillissement cérébral.
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}

{% include section.html %}

## Travaux récents

{% assign recent = site.data.citations | sort: "date" | reverse %}
{% for c in recent limit: 3 %}
  {% include citation.html title=c.title authors=c.authors publisher=c.publisher date=c.date link=c.link %}
{% endfor %}

{% include button.html link="fr/publications" text="Toutes les publications" icon="fa-solid fa-arrow-right" flip=true style="bare" %}

{% include section.html %}

{% include button.html link="fr/projets" text="Nos projets" icon="fa-solid fa-arrow-right" flip=true %}
{% include button.html link="fr/publications" text="Publications" icon="fa-solid fa-arrow-right" flip=true %}
{% include button.html link="fr/joindre" text="Se joindre au labo" icon="fa-solid fa-arrow-right" flip=true %}
{% include button.html link="https://github.com/QuantitativePhysiologyImagingLab" text="Notre code sur GitHub" icon="fa-brands fa-github" %}
