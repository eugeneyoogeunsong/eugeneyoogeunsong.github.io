---
layout: page
title: Higgs portal to dark matter
description: Invisible Higgs decays as a probe of a hidden sector.
img: assets/img/projects/higgs.jpg
importance: 3
category: Physics
---

**[Imperial College London](https://www.imperial.ac.uk/) · 2025 · under [Prof. Alexander Tapper](https://profiles.imperial.ac.uk/a.tapper)**

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/projects/higgs-event.jpg' | relative_url }}"
    alt="An ATLAS event display showing two forward jets and large missing transverse momentum, the vector-boson-fusion signature used to search for invisible Higgs decays"
    style="max-width: 100%; height: auto; border-radius: 6px"
    loading="eager"
  />
  <figcaption style="font-size: 0.8rem; color: var(--global-text-color-light); margin-top: 0.5rem">
    The experimental signature: two forward jets, and a large momentum imbalance (red) where nothing was detected. If the Higgs decays to dark matter, this is what it looks like. Image: ATLAS Experiment &copy; CERN.
  </figcaption>
</figure>

If dark matter couples to the Standard Model at all, the Higgs boson is one of the few renormalisable doors available to it. That makes the invisible branching fraction of the Higgs a direct experimental handle on a sector we otherwise cannot see.

**The portal, written down.** That the door is the Higgs is really an accident of dimensional analysis: $$\lvert\Phi\rvert^{2}$$ is the lowest-dimension gauge-singlet operator the Standard Model possesses, so it is the one thing a hidden sector can couple to without paying a price in powers of some high scale. For a real scalar dark matter candidate $$S$$,

$$\mathcal{L}_{\mathrm{portal}} = -\frac{\lambda_{hS}}{2}\,S^{2}\,\lvert\Phi\rvert^{2}$$

After electroweak symmetry breaking, $$\Phi \to (v+h)/\sqrt{2}$$, and the Lagrangian operator expands into a trilinear and a quartic term:

$$\mathcal{L} \supset -\frac{\lambda_{hS}\,v}{2}\,h\,S^{2}\;-\;\frac{\lambda_{hS}}{4}\,h^{2}S^{2}$$

The first is a direct $$h \to SS$$ vertex. If $$2m_{S} < m_{h}$$ that channel is open, and it is entirely invisible to the detector, with width

$$\Gamma(h \to SS) \;=\; \frac{\lambda_{hS}^{2}\,v^{2}}{32\pi\,m_{h}}\sqrt{1-\frac{4m_{S}^{2}}{m_{h}^{2}}}$$

which is what makes a bound on $$\mathrm{BR}(h \to \mathrm{inv})$$ translate directly into a bound on $$\lambda_{hS}$$.

**And the production side.** Vector-boson fusion is driven by the gauge–Higgs coupling sitting inside the Higgs kinetic term $$\lvert D_{\mu}\Phi\rvert^{2}$$, which after symmetry breaking contains

$$\mathcal{L} \supset \frac{2m_{W}^{2}}{v}\,h\,W^{+}_{\mu}W^{-\mu}\;+\;\frac{m_{Z}^{2}}{v}\,h\,Z_{\mu}Z^{\mu}$$

That vertex is what allows $$qq \to qqh$$ to proceed by $$t$$-channel $$W/Z$$ exchange, and it is why the two spectator quarks emerge forward with large $$\Delta\eta_{jj}$$ and large $$m_{jj}$$: precisely the topology in the event display above, and the reason the channel remains searchable even when the Higgs itself decays to nothing.

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/projects/higgs-vbf.png' | relative_url }}"
    alt="Feynman diagram of vector boson fusion: two incoming quarks each radiate a vector boson, which fuse to produce a Higgs boson, leaving two outgoing quarks"
    style="max-width: 100%; height: auto; border-radius: 6px"
    loading="lazy"
  />
  <figcaption style="font-size: 0.8rem; color: var(--global-text-color-light); margin-top: 0.5rem">
    Vector-boson fusion. The two quarks carry on and become the forward jets; the Higgs is produced centrally between them. That topology is what makes the channel searchable even when the Higgs itself decays invisibly.
  </figcaption>
</figure>

**Scope of the study.** Higgs-portal dark matter models; existing constraints on invisible decays from [ATLAS](https://atlas.cern/) and [CMS](https://cms.cern/), principally through the vector-boson-fusion signature; and projected sensitivity at the High-Luminosity LHC (HL-LHC).

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/projects/higgs-limits.png' | relative_url }}"
    alt="Left: constraints in the plane of fermion coupling against invisible Higgs width, with 68 and 95 percent contours and the direct limit. Right: ATLAS and CMS Run 1 likelihood scan against the beyond-Standard-Model branching fraction"
    style="max-width: 100%; height: auto; border-radius: 6px"
    loading="lazy"
  />
  <figcaption style="font-size: 0.8rem; color: var(--global-text-color-light); margin-top: 0.5rem">
    Where the constraints stood. Left: the invisible width against the fermion coupling, with the direct limit overlaid. Right: the ATLAS and CMS Run 1 combined scan on the BSM branching fraction: the observed curve sits above the expectation, which is the sort of small excess that only more luminosity resolves.
  </figcaption>
</figure>

**What I took from it.** The exclusion reach in this channel is set almost entirely by the control of the $$Z \to \nu\nu$$ and $$W \to \ell\nu$$ backgrounds, which is to say, by systematics rather than luminosity. The same lesson that governs neutrino oscillation measurements governs this search, and it is the reason I moved towards systematics-aware methods.

{% include linkedin_badge.liquid %}
