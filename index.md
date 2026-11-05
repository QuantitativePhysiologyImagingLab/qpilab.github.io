---
logos-top: true
alt: /fr/
---

# Quantitative MRI of the heart–brain axis

<img src="{{ "images/heart-brain.svg" | relative_url }}" alt="The heart and brain connected by an artery, with the measures we image: CBF, CVR, pulsatility, OEF and CMRO2" style="width: 100%; margin: 20px 0 40px;">

The heart feeds the brain. When the cardiovascular system ages or becomes diseased, the brain's blood supply and energy metabolism change too, often years before memory or thinking are affected.

The **Quantitative Physiological Imaging Lab** develops and applies quantitative MRI to measure these changes directly: how much blood reaches the brain, how well its vessels respond, and how much oxygen it extracts and consumes. We use these measures to link heart and brain health, and to find out who is on an unfavourable aging trajectory while there is still time to intervene.

Led by [Dr. Claudine Gauthier](members/claudine-gauthier) at the [Université de Montréal](https://www.umontreal.ca), the lab is affiliated with the [Montreal Heart Institute](https://www.icm-mhi.org) Research Centre and the [EPIC Centre](https://www.centreepic.org).

{% include logos.html %}

{% capture content %}
**We're recruiting!** Undergraduate interns and MSc and PhD students with backgrounds in physics, engineering, computer science, neuroscience, kinesiology or medicine: [see how to join the lab](join).
{% endcapture %}
{% include alert.html type="tip" content=content %}

{% include section.html %}

## What we measure

- **CBF**, cerebral blood flow, with arterial spin labelling (ASL)
- **CVR**, cerebrovascular reactivity: how much vessels dilate in response to a breathing challenge
- **Pulsatility**: how much of the heart's pulse reaches small, fragile brain vessels
- **OEF**, oxygen extraction fraction, from the magnetic susceptibility of veins (QSM) or calibrated fMRI
- **CMRO2**, the cerebral metabolic rate of oxygen: by the Fick principle, CMRO2 = CBF × OEF × arterial oxygen content
- **Myelin, iron and white-matter microstructure**, with MTsat, R2\*, QSM and diffusion MRI

{% capture content %}
{% include figure.html image="images/maps/cbf.jpg" caption="Cerebral blood flow (ASL)" %}
{% include figure.html image="images/maps/qsm.jpg" caption="Magnetic susceptibility (QSM)" %}
{% include figure.html image="images/maps/cvr.jpg" caption="Cerebrovascular reactivity (CVR)" %}
{% include figure.html image="images/maps/mtsat.jpg" caption="Myelin (MTsat)" %}
{% include figure.html image="images/maps/r2star.jpg" caption="Iron-sensitive R2\*" %}
{% include figure.html image="images/maps/lesions.jpg" caption="White-matter lesions" %}
{% endcapture %}

{% include grid.html content=content %}

{% include section.html %}

## Our approach

{% capture col1 %}
### Early markers
Vascular and metabolic changes such as lower CBF, impaired reactivity or altered OEF can appear before the damage seen on conventional MRI. In coronary artery disease, we have found them in people considered cognitively normal.
{% endcapture %}

{% capture col2 %}
### From differences to trajectories
With computational models and AI, we combine these measures into vulnerability profiles that show which differences predict future cognitive decline.
{% endcapture %}

{% capture col3 %}
### Intervening before decline
Through trials such as NeuroDance, we test whether exercise, dance and cognitive training can change the trajectory of brain aging.
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}

{% include section.html %}

## Recent work

{% assign recent = site.data.citations | sort: "date" | reverse %}
{% for c in recent limit: 3 %}
  {% include citation.html title=c.title authors=c.authors publisher=c.publisher date=c.date link=c.link %}
{% endfor %}

{% include button.html link="publications" text="All publications" icon="fa-solid fa-arrow-right" flip=true style="bare" %}

{% include section.html %}

{% include button.html link="projects" text="Our projects" icon="fa-solid fa-arrow-right" flip=true %}
{% include button.html link="publications" text="Publications" icon="fa-solid fa-arrow-right" flip=true %}
{% include button.html link="join" text="Join the lab" icon="fa-solid fa-arrow-right" flip=true %}
{% include button.html link="https://github.com/QuantitativePhysiologyImagingLab" text="Our code on GitHub" icon="fa-brands fa-github" %}
