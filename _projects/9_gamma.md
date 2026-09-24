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

Pulsars have a well-developed theory of particle acceleration in vacuum gaps: regions where the plasma fails to screen the electric field along the magnetic field lines, so charged particles are accelerated to enormous energies and radiate. The question we asked is whether the same machinery operates around a black hole, which has no surface, no crust and no rotating magnet; only spacetime.

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

**The particle accelerator (also known as the "gap"), written down.** The background is the Kerr metric in Boyer–Lindquist coordinates, with $$c = G = 1$$: $$\Delta \equiv r^{2} - 2Mr + a^{2}$$, $$\Sigma \equiv r^{2} + a^{2}\cos^{2}\theta$$, $$A \equiv (r^{2}+a^{2})^{2} - \Delta a^{2}\sin^{2}\theta$$, and the horizon at $$r_H = M + \sqrt{M^{2} - a^{2}}$$. Frame dragging enters through one number, the angular frequency at which spacetime itself is swept around,

$$\omega \equiv -\frac{g_{t\varphi}}{g_{\varphi\varphi}} = \frac{2Mar}{A}$$

Under a stationary approximation (nothing depends on $$t$$ and $$\varphi$$ except through $$\varphi - \Omega_F t$$, with $$\Omega_F$$ the angular frequency of the field lines), Gauss's law gives a Poisson equation for the non-corotational potential $$\Psi$$ in the three-dimensional magnetosphere,

$$-\frac{1}{\sqrt{-g}}\,\partial_\mu\!\left[\frac{\sqrt{-g}}{\rho_w^{2}}\,g^{\mu\nu}g_{\varphi\varphi}\,\partial_\nu\Psi\right] = 4\pi\left(\rho - \rho_{\mathrm{GJ}}\right)$$

where the general-relativistic Goldreich–Julian charge density carries $$\omega$$ explicitly:

$$\rho_{\mathrm{GJ}} \equiv \frac{1}{4\pi\sqrt{-g}}\,\partial_\mu\!\left[\frac{\sqrt{-g}}{\rho_w^{2}}\,g^{\mu\nu}g_{\varphi\varphi}\left(\Omega_F - \omega\right)F_{\varphi\nu}\right]$$

Wherever the real charge density $$\rho$$ departs from $$\rho_{\mathrm{GJ}}$$, an accelerating field $$E_\parallel = -\partial\Psi/\partial s$$ appears along the field line. The gap is the region where $$E_\parallel \neq 0$$; it forms around the null-charge surface, where $$\rho_{\mathrm{GJ}}$$ changes sign because $$\Omega_F - \omega$$ does, and that surface exists only because of frame dragging. The gap is then solved as a free-boundary problem: the Poisson equation, the equations of motion of the created pairs, and the radiative transfer of the emitted photons, closed by the condition that the pair cascade sustains itself (the gap closure condition), with the created current inside the gap, $$j_{\mathrm{cr}} \equiv J_{\mathrm{cr}}/J_{\mathrm{GJ}}$$, given externally.

**What sets the scale.** The soft photons that feed the cascade come from the accretion flow. At the accretion rates of interest (well below 1% of Eddington) that flow is radiatively inefficient (an ADAF), so its radio-to-MeV photons do not screen the gap; the gap can therefore be spatially extended, with a large potential drop. The magnetic field is normalised to equipartition at $$r = 2M$$,

$$B_H = 4 \times 10^{8}\sqrt{\frac{\dot m}{M_1}}\ \mathrm{G}, \qquad B_r \simeq f_B(\theta;\,a)\,B_H\!\left(\frac{2M}{r}\right)^{2}$$

with $$\dot m$$ the accretion rate in Eddington units and $$M_1 \equiv M/(10\,M_\odot)$$. Earlier work set $$f_B = 1$$, i.e., a horizon field uniform in $$\theta$$. The new ingredient in the MNRAS letter is $$f_B(\theta;\,a)$$ itself: GRMHD simulations show that as $$a \to M$$ the flux bunches up towards the rotation axis, and we took that concentration from the simulations rather than assuming it away.

<div class="only-light">
<figure style="margin: 1.5rem 0; text-align: center;">
  <img src="{{ '/assets/img/projects/gamma-poleward-light.png' | relative_url }}"
       alt="Radial magnetic field at the horizon relative to the equipartition value, against colatitude, for spins 0.5, 0.9 and 0.9999; the field concentrates sharply on the axis at the highest spin"
       style="max-width:min(100%, 620px); height:auto; border-radius:6px;" loading="lazy">
</figure>
</div>
<div class="only-dark">
<figure style="margin: 1.5rem 0; text-align: center;">
  <img src="{{ '/assets/img/projects/gamma-poleward-dark.png' | relative_url }}"
       alt="Radial magnetic field at the horizon relative to the equipartition value, against colatitude, for spins 0.5, 0.9 and 0.9999; the field concentrates sharply on the axis at the highest spin"
       style="max-width:min(100%, 620px); height:auto; border-radius:6px;" loading="lazy">
</figure>
</div>

**What follows from it** {% cite song2017gamma %}**.** Everything downstream is set by that concentration. Specifically, for a $$10\,M_\odot$$ hole:

- $$\lvert E_\parallel \rvert$$ peaks on the axis and reaches $$7.9 \times 10^{4}$$ statvolt cm$$^{-1}$$ at $$a = 0.9999M$$, against $$1.4 \times 10^{4}$$ at $$a = 0.90M$$: a factor of five, tracking $$f_B$$ at the pole (0.60 to 2.87).
- The spectrum has two peaks. The high-energy one, between 0.05 and 10 GeV, is curvature radiation and is brightest and hardest on the axis; the very-high-energy one, between 0.05 and 1 TeV, is inverse Compton scattering of the ADAF photons and is brightest at middle latitudes. For a stellar-mass hole the curvature process dominates, so the total flux is beamed towards the axis.
- The gap brightens as the accretion rate _falls_, because the potential drop grows as the soft-photon field thins. Stationary solutions exist for $$5.6 \times 10^{-5} \le \dot m \le 10^{-3}$$: above that the gap is too thin to resolve; below it, the gap is no longer stationary.
- In the window $$5.6 \times 10^{-5} \le \dot m \le 10^{-4}$$ the GeV flux sits a factor of ten above the Fermi-LAT ten-year limit. Therefore, an almost maximally rotating $$10\,M_\odot$$ hole within 3 kpc, viewed nearly along its axis, is detectable by the LAT if a flare lasts 1.2 months, or if the hole spends 10% of its time flaring; the TeV flux is marginally detectable by CTA in a single night at a viewing angle of about $$45^\circ$$.
- Dropping the spin to $$a = 0.90M$$ costs more than an order of magnitude in flux. The control test is the important part: with $$B_r$$ held uniform on the horizon, as in all the earlier work, the two spins barely differ. The poleward concentration is the whole effect, not a correction to it.

**Why the outer-gap model, and not the polar cap.** The choice of pulsar model to transplant is not arbitrary; it is forced by data. Fermi-LAT has detected pulsed gamma rays from more than 200 rotation-powered pulsars, and over 99% of them show phase-averaged spectra with an exponential or sub-exponential cutoff at a few GeV. A polar-cap accelerator, sitting in the strong field near the stellar surface, would produce a super-exponential cutoff from magnetic pair attenuation; the observed shape rules it out and places the emission in the outer magnetosphere, near or beyond the light cylinder. That is the outer gap, and it is the outer gap's electrodynamics we carry over. The one structural difference is where the gap comes from: in a pulsar, from the convex geometry of the dipole field far from the star; in a black hole, from frame dragging next to the horizon. Far from the hole ($$r \gg M$$) the general-relativistic charge density above reduces to the textbook flat-space form,

$$\rho_{\mathrm{GJ}} = -\frac{\boldsymbol{\Omega}\cdot\mathbf{B}}{2\pi c} + \frac{(\boldsymbol{\Omega}\times\mathbf{r})\cdot(\nabla\times\mathbf{B})}{4\pi c}$$

so the relativistic expression already carries the current corrections that the second term supplies. Close in, $$\rho_{\mathrm{GJ}}$$ vanishes where $$\Omega_F$$ matches $$\omega(r,\theta)$$; since $$\omega \propto r^{-3}$$ outward, that match is only possible near the horizon, which is why the gap sits within one or two gravitational radii of it whatever the mass of the hole.

**Then put the black hole somewhere it can eat** {% cite hirotani2018stellar %}**.** The MNRAS letter left a question open: where does a stellar-mass hole find an accretion rate of $$10^{-4}$$ Eddington? The ApJ paper answers it with a giant molecular cloud. A black hole formed in an OB association and kicked at tens of km s$$^{-1}$$ will, sooner or later, cross a dense cloud; the cloud's sound speed is under 630 m s$$^{-1}$$, so the hole moves supersonically, a bow shock forms behind it, and gas inside the Bondi radius $$r_B \sim GM/V^{2}$$ falls in at the Bondi–Hoyle rate,

$$\dot M_B = 4\pi\lambda\,\frac{(GM)^{2}}{V^{3}}\,\rho, \qquad \dot m_B = 5.39 \times 10^{-9}\,\lambda\,n_{\mathrm{H_2}}\,M_1\left(\frac{\eta}{0.1}\right)^{-1}\left(\frac{V}{10^{2}\ \mathrm{km\,s^{-1}}}\right)^{-3}$$

with $$\lambda = 1.12$$ for isothermal gas, $$\eta \sim 0.1$$ the radiative efficiency, and $$n_{\mathrm{H_2}}$$ in cm$$^{-3}$$. The captured gas carries little angular momentum, so it forms a disc only far inside $$r_B$$ and the rate near the hole is simply $$\dot m_B$$. The gap is brightest for $$6 \times 10^{-5} < \dot m < 2 \times 10^{-4}$$, which a cloud core of $$n_{\mathrm{H_2}} \gtrsim 10^{4}$$ cm$$^{-3}$$ supplies at 100 km s$$^{-1}$$, and $$\gtrsim 1.2 \times 10^{3}$$ cm$$^{-3}$$ at 50 km s$$^{-1}$$. Those are ordinary numbers for a dense core.

<div class="only-light">
<figure style="margin: 1.5rem 0; text-align: center;">
  <img src="{{ '/assets/img/projects/gamma-bondi-light.png' | relative_url }}"
       alt="Bondi accretion rate in Eddington units against molecular-cloud density for three black-hole velocities, with the accretion-rate window in which the gap is brightest shaded"
       style="max-width:min(100%, 620px); height:auto; border-radius:6px;" loading="lazy">
</figure>
</div>
<div class="only-dark">
<figure style="margin: 1.5rem 0; text-align: center;">
  <img src="{{ '/assets/img/projects/gamma-bondi-dark.png' | relative_url }}"
       alt="Bondi accretion rate in Eddington units against molecular-cloud density for three black-hole velocities, with the accretion-rate window in which the gap is brightest shaded"
       style="max-width:min(100%, 620px); height:auto; border-radius:6px;" loading="lazy">
</figure>
</div>

**What the cascade looks like, and what it emits.** With $$M = 10\,M_\odot$$ and $$a = 0.99M$$, and keeping every term of the Poisson equation rather than the $$\Delta \ll M^{2}$$ approximation used before, the electrons' Lorentz factors saturate around $$3 \times 10^{6}$$ under curvature-radiation drag, with a broad plateau between $$6 \times 10^{4}$$ and $$2 \times 10^{6}$$ held down by inverse-Compton drag deep in the Klein–Nishina regime; it is those lower-energy electrons that do most of the TeV emission. The resulting spectrum is bimodal: a broad curvature peak at 0.01–1 GeV and a sharp inverse-Compton peak near 0.1 TeV, with the primary inverse-Compton component absorbed above about 0.1 TeV. The gap is brightest face-on ($$\theta < 15^\circ$$) and detectable with CTA if $$a > 0.90M$$ and the distance is under 1 kpc; at $$a = 0.50M$$ the hole would need to be within 0.3 kpc.

Two robustness results matter more than any single number. Firstly, the spectrum changes little as the created current $$j_{\mathrm{cr}}$$ runs from 0.3 to 0.9 of the Goldreich–Julian value, and little again as the positronic current injected across the outer boundary runs from 0 to 0.8 of it, even though $$E_\parallel(s)$$ itself moves substantially (the gap shifts inward and deepens, but gravitational redshift takes back most of what that gains). Secondly, there is no stationary solution at all once $$j_{\mathrm{cr}} > 1$$. A prediction that survives a wide range of the one parameter nobody can measure is worth more than one tuned to a point.

**Why it is testable, and against what.** The Galactic plane holds 76 very-high-energy sources, of which 36 were unidentified at the time; of 18 unidentified sources with radio molecular-line data, 12 sit on dense gas, and several of those are compact. The standard explanation is hadronic: cosmic rays from a supernova remnant striking a cloud, producing $$\pi^{0}$$ decays and a single power law from GeV to 100 TeV, spread over the cloud core ($$10^{18}$$ to $$10^{19}$$ cm). The gap model predicts something distinguishable on three counts: a **point-like** image, since the emission region is at most $$10\,r_g \sim 10^{7}$$ cm; a **bimodal** spectrum with peaks near 0.1 GeV and 0.1 TeV rather than a power law; and **no synchrotron counterpart** in radio or X-rays. CTA's angular resolution is about five times better than the instruments that found these sources, which is what makes the first test possible. A source such as HESS J1800–2400C, point-like and in a cloud, is the kind of object the model is for.

**The honest caveats.** Three, and we put them in the papers rather than in a footnote. The spin $$a = 0.9999M$$ is adopted to show the extreme; a hole that preferentially swallows negative-angular-momentum photons from its own accretion flow settles at the canonical $$a = 0.998M$$, and the moderate cases interpolate between the two we solved. Stationarity is an assumption: particle-in-cell simulations of black hole gaps show rapid oscillations of $$E_\parallel$$ and the current, and if the injected current is a sizeable fraction of the Goldreich–Julian current the stationary picture breaks down. What we could argue is that an outer-gap-type accelerator carries a negative feedback (extra pair creation redistributes charge so as to reduce $$E_\parallel$$), unlike the polar-cap type whose positive feedback is known to be unstable, and that the closure condition is met across a wide range of currents; a proper stability analysis is a separate piece of work. In addition, the ApJ study found that when pairs are created by MeV–MeV collisions they return to the horizon and pile charge at the outer boundary, so the solution is, strictly, slowly time-dependent.

This work ran across the Korea Astronomy and Space Science Institute and the University of Science and Technology, and a visiting studentship at the Academia Sinica Institute of Astronomy and Astrophysics in Taipei. The 2017 MNRAS letter was my first peer-reviewed first-author publication, at **age 19**; the 2018 ApJ paper, on which I am a co-author, is where the same accelerator was set loose in a molecular cloud.

{% include author_self_link.liquid %}

{% include linkedin_card.liquid after_heading="references" %}
