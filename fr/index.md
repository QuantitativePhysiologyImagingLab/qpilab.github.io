---
logos-top: true
alt: /
---

# À propos du laboratoire

Le **Laboratoire d'imagerie physiologique quantitative**, dirigé par la [Pre Claudine Gauthier](../members/claudine-gauthier), vise à approfondir notre compréhension de l'axe cœur-cerveau en étudiant comment la santé cardiovasculaire influence la fonction vasculaire, le métabolisme et la microstructure du cerveau au cours du vieillissement. Établi à l'[Université de Montréal](https://www.umontreal.ca) et au Centre de recherche de l'[Institut de Cardiologie de Montréal](https://www.icm-mhi.org), et affilié au [Centre ÉPIC](https://www.centreepic.org), le laboratoire utilise l'imagerie par résonance magnétique (IRM) quantitative avancée pour étudier les liens entre la santé cardiovasculaire, la santé cérébrale et la fonction cognitive.

Nos recherches portent sur la mesure de marqueurs physiologiques clés de la santé cérébrale, dont le débit sanguin cérébral (CBF), la réactivité cérébrovasculaire (CVR), la fraction d'extraction d'oxygène (OEF), le taux métabolique cérébral d'oxygène (CMRO₂), le contenu en myéline (MTsat) et le fer tissulaire (QSM et R2\*). Ensemble, ces mesures éclairent les changements vasculaires, métaboliques et structuraux qui peuvent précéder le déclin cognitif et la neurodégénérescence.

En parallèle de nos recherches physiologiques, nous développons et optimisons des outils d'analyse computationnelle pour améliorer la précision, la fiabilité et l'accessibilité de l'imagerie cérébrale quantitative. Nos travaux couvrent l'IRM sensible à l'oxygénation, des chaînes avancées de traitement d'images et des outils d'apprentissage profond en libre accès.

En intégrant la physique de l'IRM, l'imagerie computationnelle et la recherche clinique, notre laboratoire cherche à mieux comprendre les trajectoires des changements cérébraux vasculaires, métaboliques et structuraux associés au vieillissement et aux maladies cardiovasculaires, à identifier des biomarqueurs précoces de la dysfonction cérébrovasculaire, et à étudier comment des interventions, en particulier l'exercice et l'activité physique, peuvent aider à préserver la santé cérébrale et à atténuer le déclin cognitif.

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
