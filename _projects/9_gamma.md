---
layout: page
title: Gamma radiation from black hole magnetospheres
description: Lepton accelerators near the event horizon, and the very-high-energy emission they produce.
img: assets/img/projects/gamma.jpg
importance: 3
category: Astrophysics
related_publications: true
---

**[KASI](https://www.kasi.re.kr/eng/index) & [UST](https://ust.ac.kr/eng/), and [Academia Sinica](https://www.asiaa.sinica.edu.tw/) · 2015 – 2018 · with [Dr Kouichi Hirotani](https://www.asiaa.sinica.edu.tw/people/cv.php?i=hirotani), [Dr Satoki Matsushita](https://www.asiaa.sinica.edu.tw/people/cv.php?i=satoki), [Dr Hung-Yi Pu](https://scholar.lib.ntnu.edu.tw/en/persons/hung-yi-pu/) and [Prof Albert Kong](https://astr.site.nthu.edu.tw/p/406-1336-35225,r2556.php?Lang=en)**

Pulsars have a well-developed theory of particle acceleration in vacuum gaps: regions where the plasma fails to screen the electric field along the magnetic field lines, so charged particles are accelerated to enormous energies and radiate. The question we asked is whether the same machinery operates around a black hole, which has no surface, no crust, and no rotating magnet, only spacetime.

**It does, and frame dragging is why.** Near a rapidly rotating black hole, frame dragging reverses the sign of the Goldreich–Julian charge density. That reversal leaves an unscreened magnetic-field-aligned electric field, which accelerates electrons and positrons in opposite directions and drives a pair cascade. The result is a **lepton accelerator in the immediate vicinity of the event horizon** {% cite song2017gamma %}.

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/projects/gamma-spectrum.jpg' | relative_url }}"
    alt="Predicted photon energy flux against photon energy for a 10 solar-mass black hole with maximal spin at 3 kpc, against Fermi-LAT ten-year and CTA fifty-hour sensitivity curves"
    style="max-width: 100%; height: auto; border-radius: 6px"
    loading="lazy"
  />
  <figcaption style="font-size: 0.8rem; color: var(--global-text-color-light); margin-top: 0.5rem">
    Predicted spectrum for a 10 M<sub>&#9737;</sub> extremally rotating black hole at 3 kpc. The GeV–TeV emission rises above the Fermi-LAT and CTA sensitivity curves, which is what makes the prediction testable rather than merely interesting.
  </figcaption>
</figure>

**The particle accelerator (also known as the "gap"), written down.** Under a stationary approximation, Gauss's law gives a Poisson equation for the non-corotational potential $$\Psi$$ in the three-dimensional magnetosphere,

$$-\frac{1}{\sqrt{-g}}\,\partial_\mu\!\left[\frac{\sqrt{-g}}{\rho_w^{2}}\,g^{\mu\nu}g_{\varphi\varphi}\,\partial_\nu\Psi\right] = 4\pi\left(\rho - \rho_{\mathrm{GJ}}\right)$$

where the general-relativistic Goldreich–Julian charge density carries the frame-dragging frequency $$\omega \equiv -g_{t\varphi}/g_{\varphi\varphi}$$ explicitly:

$$\rho_{\mathrm{GJ}} \equiv \frac{1}{4\pi\sqrt{-g}}\,\partial_\mu\!\left[\frac{\sqrt{-g}}{\rho_w^{2}}\,g^{\mu\nu}g_{\varphi\varphi}\left(\Omega_F - \omega\right)F_{\varphi\nu}\right]$$

Wherever the real charge density $$\rho$$ departs from $$\rho_{\mathrm{GJ}}$$, an accelerating field $$E_\parallel = -\partial\Psi/\partial s$$ appears along the field line. The gap is the region where $$E_\parallel \neq 0$$, and it forms around the null-charge surface where $$\rho_{\mathrm{GJ}}$$ changes sign, a surface that exists only because of frame dragging.

**The observational prediction.** The resulting gamma-ray flux is beamed towards the rotation axis, and it is strongly spin-dependent: it rises by more than an order of magnitude as the spin increases from $$a = 0.90M$$ to $$a = 0.9999M$$. That makes it a testable statement for Fermi-LAT and CTA, not merely a theoretical curiosity; a detection would constrain the spin of the emitting object.

**Stellar-mass black holes too.** Extending the same framework to a stellar-mass black hole traversing a dense gas cloud, we found that the pair cascade produces detectable very-high-energy emission if the hole is extremally rotating and within roughly 1 kpc {% cite hirotani2018stellar %}.

This work ran across the Korea Astronomy and Space Science Institute and the University of Science and Technology, and a visiting studentship at the Academia Sinica Institute of Astronomy and Astrophysics in Taipei. The 2017 paper was my first peer-reviewed first-author publication, at nineteen.

{% include author_self_link.liquid %}
