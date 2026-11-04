---
title: Tools
alt: /fr/outils/
nav:
  order: 1.5
  tooltip: Open-source software
---

# {% include icon.html icon="fa-solid fa-code" %}Tools

We believe methods should be as open as results. The software we build to measure brain physiology is released openly on [GitHub](https://github.com/QuantitativePhysiologyImagingLab), so other labs can reproduce our work and use it in their own studies.

{% include section.html %}

{% capture text %}
Veins carry deoxygenated blood, so mapping them precisely is the first step to measuring how much oxygen the brain extracts (OEF). **VeinSeg** is a 3D deep-learning tool that segments cerebral veins from a QSM or R2\* map.

- Trained on multi-site data at **3T and 7T**, across five QSM reconstruction methods (TGV, MEDI, L1, STAR, iLSQR) and R2\*
- **Physics-informed**: training combines Dice and cross-entropy with a dipole field-consistency loss and a Frangi vesselness shape loss
- Needs only a single image as input, and outputs a binary vein mask and a probability map

```bash
pip install veinseg-qsm
veinseg -i qsm.nii.gz -r tgv -f 7t -o mask.nii.gz -p prob.nii.gz
```

{% include button.html type="github" text="VeinSeg on GitHub" link="https://github.com/QuantitativePhysiologyImagingLab/VeinSeg" %}
{% include button.html icon="fa-solid fa-cube" text="Model on Hugging Face" link="https://huggingface.co/YousifKhoury/VeinSeg" %}
{% endcapture %}

{% include feature.html image="images/maps/veins.jpg" title="VeinSeg: cerebral vein segmentation" text=text %}

{% include figure.html image="images/projects/veinseg.jpg" caption="VeinSeg architecture: physics-based priors guide the network during training" width="700px" %}

{% include section.html %}

## Coming soon

We are preparing more of our pipelines for release, including tools for mapping oxygen extraction (OEF) and oxygen metabolism (CMRO2), and for separating the magnetic signatures of veins, iron and myelin. [Follow us on GitHub](https://github.com/QuantitativePhysiologyImagingLab) to hear when they are out.
