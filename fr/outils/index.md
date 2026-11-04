---
title: Outils
alt: /tools/
nav:
  order: 1.5
  tooltip: Logiciels libres
---

# {% include icon.html icon="fa-solid fa-code" %}Outils

Les logiciels que nous développons pour mesurer la physiologie du cerveau sont publiés librement sur [GitHub](https://github.com/QuantitativePhysiologyImagingLab), afin que d'autres laboratoires puissent reproduire nos travaux et les utiliser dans leurs propres études.

{% include section.html %}

{% capture text %}
Les veines transportent le sang désoxygéné : les cartographier avec précision est la première étape pour mesurer la quantité d'oxygène extraite par le cerveau (OEF). **VeinSeg** est un outil d'apprentissage profond 3D qui segmente les veines cérébrales à partir d'une carte QSM ou R2\*.

- Entraîné sur des données multicentriques à **3T et 7T**, avec cinq méthodes de reconstruction QSM (TGV, MEDI, L1, STAR, iLSQR) et le R2\*
- **Fondé sur la physique** : l'entraînement combine Dice et entropie croisée avec une perte de cohérence du champ dipolaire et une perte de vascularité de Frangi
- Une seule image en entrée; en sortie, un masque binaire des veines et une carte de probabilité

```bash
pip install veinseg-qsm
veinseg -i qsm.nii.gz -r tgv -f 7t -o mask.nii.gz -p prob.nii.gz
```

{% include button.html type="github" text="VeinSeg sur GitHub" link="https://github.com/QuantitativePhysiologyImagingLab/VeinSeg" %}
{% include button.html icon="fa-solid fa-cube" text="Modèle sur Hugging Face" link="https://huggingface.co/YousifKhoury/VeinSeg" %}
{% endcapture %}

{% include feature.html image="images/maps/veins.jpg" title="VeinSeg : segmentation des veines cérébrales" text=text %}

{% include figure.html image="images/projects/veinseg.jpg" caption="Architecture de VeinSeg : des a priori physiques guident le réseau pendant l'entraînement" width="700px" %}

{% include section.html %}

## À venir

Nous préparons la publication d'autres chaînes de traitement, dont des outils pour cartographier l'extraction (OEF) et le métabolisme (CMRO2) de l'oxygène, et pour séparer les signatures magnétiques des veines, du fer et de la myéline. [Suivez-nous sur GitHub](https://github.com/QuantitativePhysiologyImagingLab) pour être informés de leur sortie.
