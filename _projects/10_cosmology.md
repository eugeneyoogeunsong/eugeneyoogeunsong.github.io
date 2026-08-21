---
layout: page
title: Early-universe cosmology
description: Geodesic congruences and anisotropic shear in a Bianchi type I universe.
img: assets/img/projects/cosmology.jpg
importance: 4
category: Astrophysics
related_publications: true
---

**[KASI](https://www.kasi.re.kr/eng/index) & [UST](https://ust.ac.kr/eng/) · 2013 – 2015 · with Prof Seok Jae Park, and with [Prof Yong Seung Cho](https://myr.ewha.ac.kr/matheng/people/professors-emeritus.do?mode=view&articleNo=609449&title=Yong+Seung+Cho) of Ewha Womans University**

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/projects/cosmology.jpg' | relative_url }}"
    alt="Timeline of the universe from quantum fluctuations and inflation through the afterglow light pattern at 400,000 years, the dark ages, the first stars, and galaxy formation, to dark-energy-driven accelerated expansion over 13.7 billion years"
    style="max-width: 100%; height: auto; border-radius: 6px"
    loading="eager"
  />
  <figcaption style="font-size: 0.8rem; color: var(--global-text-color-light); margin-top: 0.5rem">
    13.7 billion years of expansion. This work concerns the far left of that diagram: the interval
    where anisotropy, if the universe had any, still mattered. Image: NASA / WMAP Science Team.
  </figcaption>
</figure>

Cosmology assumes the universe is homogeneous and isotropic, and the assumption works extremely well. But it is a statement about the universe we observe now, not about the one that began: nothing in general relativity requires the initial state to have been isotropic, and inflation is credited with erasing the anisotropy rather than with its never having existed. The question I worked on as a _teenage_ graduate researcher - the first PhD course that I did - is what that erasure looks like written down, and whether anything survives it.

**The setting.** The simplest homogeneous but anisotropic model is Bianchi type I, which expands at a different rate along each axis:

$$ds^{2} = -dt^{2} + X^{2}(t)\,dx^{2} + Y^{2}(t)\,dy^{2} + Z^{2}(t)\,dz^{2}, \qquad l^{3} \equiv XYZ$$

Setting $$X = Y = Z$$ recovers Friedmann–Robertson–Walker, so the anisotropy is a genuine generalisation rather than a different theory. The vacuum case is the Kasner universe.

**The kinematics.** For a timelike geodesic congruence with tangent $$\xi^{a}$$, the gradient $$B_{ab} = \nabla_{b}\xi_{a}$$ decomposes into an expansion, a shear and a rotation:

$$B_{ab} = \tfrac{1}{3}\theta\, h_{ab} + \sigma_{ab} + \omega_{ab}, \qquad h_{ab} = g_{ab} + \xi_{a}\xi_{b}$$

Bianchi I initial conditions make the rotation negligible, so $$\omega_{ab} = 0$$ and the dynamics live entirely in $$\theta$$ and $$\sigma_{ab}$$.

**The evolution equations.** Contracting the Riemann identity for $$B_{ab}$$ gives a Raychaudhuri-type equation for the expansion, which in this geometry can be written purely in terms of the mean scale factor $$l$$ and the shear amplitude $$\Sigma$$:

$$\dot{\theta} = -\tfrac{1}{3}\theta^{2} - \sigma_{ab}\sigma^{ab} - R_{ab}\xi^{a}\xi^{b} = -\frac{3\dot{l}^{2}}{l^{2}} - \frac{2\Sigma^{2}}{l^{6}} - R_{ab}\xi^{a}\xi^{b}$$

with $$\theta = 3\dot{l}/l$$, $$\sigma_{ab} = \Sigma_{ab}/l^{3}$$ and $$\sigma^{2} \equiv \tfrac{1}{2}\sigma_{ab}\sigma^{ab} = \Sigma^{2}/l^{6}$$; the field equations reduce to $$3\ddot{l}/l + 2\sigma^{2} = 0$$ and $$\left(l^{6}\sigma^{2}\right)^{\cdot} = 0$$. Retaining only the dominant $$l^{-6}$$ terms in the earliest epoch leaves an evolution equation for the shear itself:

$$\frac{d\sigma_{ab}}{dt} \;\approx\; -\frac{1}{l^{6}}\,\Sigma_{ac}\Sigma^{c}_{\;b} \;+\; \frac{2\Sigma^{2}}{3\,l^{6}}\,h_{ab}$$

We derived the same pair of results for null congruences, where the $$\tfrac{1}{3}$$ becomes $$\tfrac{1}{2}$$ and the affine parameter replaces proper time {% cite song2016shear %}.

**What falls out of it.** Two things. The $$l^{-6}$$ scaling is the whole story of isotropisation: shear dilutes faster than any ordinary fluid, so a modest expansion is enough to render it invisible, and the anisotropy does not need to be forbidden, only outrun. And the shear term makes the Raychaudhuri inequality _stronger_, not weaker, which means anisotropy brings the singularity closer rather than helping to avoid it, sharpening the Hawking–Penrose result rather than evading it.

**Why it might be observable.** Shear that has become negligible today was not negligible when the primordial gravitational-wave background was imprinted. If a future low-frequency observatory such as LISA ever resolves an anisotropy in that background, an evolution equation for $$\sigma_{ab}$$ is what converts the measurement into a statement about initial conditions. That connection is an outlook rather than a result: this work supplies the kinematics, not a predicted spectrum.

This was my earliest first-author preprint, written at eighteen.

{% include author_self_link.liquid %}

{% include linkedin_badge.liquid %}
