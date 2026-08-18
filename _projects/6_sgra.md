---
layout: page
title: Sagittarius A* variability
description: GRMHD and radiative transfer modelling of the Galactic Centre black hole.
img: assets/img/projects/sgra.jpg
importance: 1
category: Astrophysics
related_publications: true
---

**[UCL / Mullard Space Science Laboratory](https://www.ucl.ac.uk/mathematical-physical-sciences/mssl) · 2023 – 2024 · with [Dr Ziri Younsi](https://profiles.ucl.ac.uk/26858-ziri-younsi) and [Prof Kinwah Wu](https://profiles.ucl.ac.uk/10719-kinwah-wu)**

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/projects/sgra-eht.jpg' | relative_url }}"
    alt="Sagittarius A* imaged by the Event Horizon Telescope, alongside progressively wider views of the Galactic Centre and the South Pole Telescope"
    style="max-width: 100%; height: auto; border-radius: 6px"
    loading="eager"
  />
  <figcaption style="font-size: 0.8rem; color: var(--global-text-color-light); margin-top: 0.5rem">
    Sgr A* at four scales, from three light-minutes to 500 light-years. Image: Event Horizon Telescope Collaboration and others.
  </figcaption>
</figure>

Sagittarius (Sgr) A\* varies across the electromagnetic spectrum on timescales from minutes to hours. What that variability tells us about the accretion flow depends entirely on how the electrons are heated, and that is precisely the part of the physics that general-relativistic magnetohydrodynamics (GRMHD) does not determine on its own.

**Method.** GRMHD simulations run in **[BHAC](https://bhac.science/)**, post-processed through general-relativistic radiative transfer in **[BHOSS](https://arxiv.org/abs/1907.09196)**, in Fortran and Python.

**Parameter space.** Magnetically arrested disc states across black hole spins $$a = -0.94$$ to $$+0.94$$, with three competing electron-heating prescriptions: R–$$\beta$$, turbulent heating, and magnetic reconnection.

**Status.** Manuscript in preparation, targeting _MNRAS_, with co-authors including Dr Yosuke Mizuno and Dr Christian M. Fromm. Discussions with researchers from the [EHT (Event Horizon Telescope)](https://eventhorizontelescope.org/) collaboration informed the radiative-transfer setup {% cite song2026sgra %}.

_Work in progress; outputs will appear here and on [Publications](/publications/)._
