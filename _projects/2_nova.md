---
layout: page
title: NOvA - oscillations with data on the ground
description: Electron-neutrino appearance and muon-neutrino disappearance on Fermilab's running long-baseline experiment.
img: assets/img/projects/nova.jpg
importance: 2
category: Particle Physics
---

**[Imperial College London](https://www.imperial.ac.uk/) · 2026 – present · with [Dr Linda Cremonesi](https://profiles.imperial.ac.uk/l.cremonesi) and [Dr Alex Booth](https://profiles.imperial.ac.uk/a.booth)**

Where [DUNE](https://www.dunescience.org/) is still being built, [NOvA](https://novaexperiment.fnal.gov/) (NuMI Off-axis $$\nu_e$$ Appearance) has been running since 2014. So, NOvA is the experiment that gives me data _now_. The analysis problems NOvA poses are the ones that will still be there when DUNE turns on.

My role on NOvA is **a variety of physics analysis**.

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img src="{{ '/assets/img/projects/nova-baseline-schematic.jpg' | relative_url }}"
       alt="Schematic of the NOvA beamline: muon neutrinos leave Fermilab and travel 810 km to the far detector at Ash River, Minnesota, oscillating into electron and tau neutrinos along the way"
       style="max-width:100%; height:auto; border-radius:6px;" loading="eager">
  <figcaption style="font-size:0.8rem; color:var(--global-text-color-light); margin-top:0.5rem;">
    The NOvA baseline. A beam that starts as muon neutrinos develops electron- and tau-neutrino
    components over 810 km; the near detector measures what was produced, the far detector what
    arrives. Credit: Jeremy Wolcott (Tufts University), via the
    <a href="https://www.imperial.ac.uk/high-energy-physics/research/experiments/nova/">Imperial NOvA group</a>.
  </figcaption>
</figure>

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img src="{{ '/assets/img/projects/nova-full.jpg' | relative_url }}"
       alt="The NOvA experiment: a neutrino beam from Fermilab travels 810 km to the far detector at Ash River, Minnesota, with the muon-neutrino beam partially oscillating into electron neutrinos"
       style="max-width:100%; height:auto; border-radius:6px;" loading="eager">
  <figcaption style="font-size:0.8rem; color:var(--global-text-color-light); margin-top:0.5rem;">
    The 810 km baseline. A beam that leaves Fermilab almost entirely muon neutrinos arrives at Ash
    River with a measurable electron-neutrino component: that appearance is the measurement.
  </figcaption>
</figure>

**The apparatus.** Two functionally identical liquid-scintillator tracking calorimeters sit in [Fermilab](https://www.fnal.gov/)'s NuMI beam: a near detector at Fermilab, and a 14 kt far detector 810 km away at Ash River, Minnesota. Both sit **14.6 mrad off the beam axis**, which is the design choice that makes the experiment work: going off-axis narrows the flux into a band around 2 GeV, close to the $$\nu_\mu \rightarrow \nu_e$$ oscillation maximum, and strips out the high-energy tail that would otherwise dominate the neutral-current background.

**The underlying relation.** Flavour eigenstates are superpositions of mass eigenstates, $$\lvert\nu_\alpha\rangle = \sum_i U^{*}_{\alpha i}\lvert\nu_i\rangle$$, and propagating them gives the transition probability in full three-flavour form:

$$P(\nu_\alpha \to \nu_\beta) = \delta_{\alpha\beta} - 4\sum_{j>i}\mathrm{Re}\!\left[W^{ij}_{\alpha\beta}\right]\sin^{2}\!\left(\frac{\Delta m^{2}_{ji}L}{4E_\nu}\right) \pm 2\sum_{j>i}\mathrm{Im}\!\left[W^{ij}_{\alpha\beta}\right]\sin\!\left(\frac{\Delta m^{2}_{ji}L}{2E_\nu}\right)$$

with $$W^{ij}_{\alpha\beta} = U_{\alpha i}U^{*}_{\beta i}U^{*}_{\alpha j}U_{\beta j}$$ and $$\Delta m^{2}_{ij} = m_i^{2}-m_j^{2}$$. The last term is the one that matters most here: it changes sign between neutrinos and antineutrinos, so it vanishes unless the mixing matrix is complex. **That term is CP violation**, and measuring it is why the experiment runs in both beam modes.

**The measurements.** Electron-neutrino appearance and muon-neutrino disappearance, in both neutrino and antineutrino beam modes. Together these constrain the mass ordering, the octant of $$\theta_{23}$$, and $$\delta_{CP}$$.

**[NOvA at Imperial](https://www.imperial.ac.uk/high-energy-physics/research/experiments/nova/).** The group works on both sides of the problem, interactions and oscillations, which are not separable: because neutrinos cannot be observed directly, an oscillation measurement is only as good as the interaction model underneath it. Imperial leads the near-detector interaction programme, is heavily involved in the extrapolation technique that uses the near detector to predict the far-detector spectra, and leads the development of reconstruction algorithms, both traditional and machine-learned, with a particular focus on attention mechanisms and on the interpretability of those methods. My supervisor [Dr Linda Cremonesi](https://profiles.imperial.ac.uk/l.cremonesi) was elected [co-spokesperson of NOvA](https://news.fnal.gov/2026/06/linda-cremonesi-elected-as-co-spokesperson-for-nova-neutrino-experiment/) in April 2026, having served as the experiment's analysis coordinator since 2022; she now co-leads the collaboration with Fermilab's Alex Himmel. I work with her and [Dr Alex Booth](https://profiles.imperial.ac.uk/a.booth).

**Why it matters to my work.** That last strand is the one I came for. An interpretable, systematics-aware reconstruction network is exactly the instrument I argue for: one whose failure modes you can audit, rather than one that merely scores well. Working across several physics analyses is also the fastest way to learn where an experiment's systematics actually live, because you watch the same nuisance parameters surface in different measurements, which a single channel never shows you. The group treats NOvA and DUNE as one programme rather than two. Practically, that means the reconstruction and inference methods I develop get tested against real, systematics-limited data on NOvA before they are asked to carry a DUNE measurement. That is the right order to do it in. A method that has never met a real detector is a hypothesis, not a tool.

_Work in progress; outputs will appear here and on [Publications](/publications/)._

{% include linkedin_badge.liquid %}
