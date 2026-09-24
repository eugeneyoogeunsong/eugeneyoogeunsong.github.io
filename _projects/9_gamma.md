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

**It does, and frame dragging is why.** A rotating magnetosphere needs a particular charge density, the Goldreich–Julian density, in order to screen its own electric field; wherever the plasma cannot supply it, an unscreened field remains. Near a rapidly rotating black hole, frame dragging (spacetime itself being swept around with the hole) reverses the sign of that required density close to the horizon. That reversal leaves an unscreened magnetic-field-aligned electric field, which accelerates electrons and positrons in opposite directions and drives a pair cascade. The result is a **lepton accelerator in the immediate vicinity of the event horizon** {% cite song2017gamma %}.

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

**The particle accelerator (also known as the "gap"), written down.** The background is the Kerr metric for a hole of mass $$M$$ and spin $$a$$ (in units with $$c = G = 1$$, so that $$a = M$$ is maximal spin), with the horizon at $$r_H = M + \sqrt{M^{2} - a^{2}}$$. Frame dragging enters through a single number, the angular frequency at which spacetime is swept around,

$$\omega \equiv -\frac{g_{t\varphi}}{g_{\varphi\varphi}} = \frac{2Mar}{A}, \qquad A \equiv (r^{2}+a^{2})^{2} - (r^{2} - 2Mr + a^{2})\,a^{2}\sin^{2}\theta$$

Far from the hole $$A \to r^{4}$$, so $$\omega$$ falls off as $$2Ma/r^{3}$$; it is only close in that it is large. Under a stationary approximation (nothing depends on $$t$$ and $$\varphi$$ except through $$\varphi - \Omega_F t$$, with $$\Omega_F$$ the angular frequency at which the field lines rotate), Gauss's law gives a Poisson equation for the non-corotational potential $$\Psi$$ (the part of the electric potential that a co-rotating observer would still see) in the three-dimensional magnetosphere,

$$-\frac{1}{\sqrt{-g}}\,\partial_\mu\!\left[\frac{\sqrt{-g}}{\rho_w^{2}}\,g^{\mu\nu}g_{\varphi\varphi}\,\partial_\nu\Psi\right] = 4\pi\left(\rho - \rho_{\mathrm{GJ}}\right)$$

where $$\rho_w^{2} \equiv g_{t\varphi}^{2} - g_{tt}g_{\varphi\varphi}$$ is a metric factor, and the general-relativistic Goldreich–Julian charge density carries $$\omega$$ explicitly:

$$\rho_{\mathrm{GJ}} \equiv \frac{1}{4\pi\sqrt{-g}}\,\partial_\mu\!\left[\frac{\sqrt{-g}}{\rho_w^{2}}\,g^{\mu\nu}g_{\varphi\varphi}\left(\Omega_F - \omega\right)F_{\varphi\nu}\right]$$

Wherever the real charge density $$\rho$$ departs from $$\rho_{\mathrm{GJ}}$$, an accelerating field $$E_\parallel = -\partial\Psi/\partial s$$ appears along the field line. The gap is the region where $$E_\parallel \neq 0$$; it forms around the null-charge surface, where $$\rho_{\mathrm{GJ}}$$ changes sign because $$\Omega_F - \omega$$ does, and that surface exists only because of frame dragging. The gap is then solved as a free-boundary problem: the Poisson equation, the equations of motion of the created pairs, and the radiative transfer of the emitted photons, closed by the condition that the pair cascade sustains itself (the gap closure condition), with the created current inside the gap, $$j_{\mathrm{cr}} \equiv J_{\mathrm{cr}}/J_{\mathrm{GJ}}$$, given externally.

**What sets the scale.** The cascade needs a supply of soft photons for the gamma rays to collide with, and those come from the accretion flow. At the accretion rates of interest (well below 1% of the Eddington rate, the rate at which radiation pressure would halt the infall) the flow is an advection-dominated one (an ADAF): hot, tenuous and radiatively inefficient, so its radio-to-MeV photons are too sparse to screen the gap, which can therefore stretch out spatially and build a large potential drop. The magnetic field is normalised so that its energy density matches that of the infalling gas (equipartition) at $$r = 2M$$,

$$B_H = 4 \times 10^{8}\sqrt{\frac{\dot m}{M_1}}\ \mathrm{G}, \qquad B_r \simeq f_B(\theta;\,a)\,B_H\!\left(\frac{2M}{r}\right)^{2}$$

with $$\dot m$$ the accretion rate in Eddington units and $$M_1 \equiv M/(10\,M_\odot)$$. Earlier work set $$f_B = 1$$, i.e., a horizon field uniform in colatitude $$\theta$$. The new ingredient in the MNRAS letter is $$f_B(\theta;\,a)$$ itself: general-relativistic magnetohydrodynamic (GRMHD) simulations of accreting holes show that as $$a \to M$$ the magnetic flux bunches up towards the rotation axis, and we took that concentration from the simulations instead of assuming the field uniform.

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

- $$\lvert E_\parallel \rvert$$ peaks on the axis and reaches $$7.9 \times 10^{4}$$ statvolt cm$$^{-1}$$ (about $$2.4 \times 10^{9}$$ V m$$^{-1}$$) at $$a = 0.9999M$$, against $$1.4 \times 10^{4}$$ at $$a = 0.90M$$: a factor of five, tracking $$f_B$$ at the pole (0.60 to 2.87).
- The spectrum has two peaks, made by two different processes. The high-energy one, between 0.05 and 10 GeV, is curvature radiation (the light an ultra-relativistic particle sheds as it follows a bent field line) and is brightest and hardest on the axis; the very-high-energy one, between 0.05 and 1 TeV, is inverse Compton scattering (the accelerated electrons kicking the accretion flow's soft photons up to TeV energies) and is brightest at middle latitudes. For a stellar-mass hole the curvature process dominates, so the total flux is beamed towards the axis.
- The gap brightens as the accretion rate _falls_, because the potential drop grows as the soft-photon field thins. Stationary solutions exist for $$5.6 \times 10^{-5} \le \dot m \le 10^{-3}$$: above that the gap is too thin to resolve; below it, the gap is no longer stationary.
- In the window $$5.6 \times 10^{-5} \le \dot m \le 10^{-4}$$ the GeV flux sits a factor of ten above the Fermi-LAT ten-year limit. Therefore, an almost maximally rotating $$10\,M_\odot$$ hole within 3 kpc, viewed nearly along its axis, is detectable by the LAT if a flare lasts 1.2 months, or if the hole spends 10% of its time flaring; the TeV flux is marginally detectable by CTA in a single night at a viewing angle of about $$45^\circ$$.
- Dropping the spin to $$a = 0.90M$$ costs more than an order of magnitude in flux, and the control test says why: with $$B_r$$ held uniform on the horizon, as in all the earlier work, the two spins barely differ, so the poleward concentration is not a correction to the effect but the effect itself.

**Why the outer-gap model, and not the polar cap.** The choice of pulsar model to transplant is not arbitrary; it is forced by data. Fermi-LAT has detected pulsed gamma rays from more than 200 rotation-powered pulsars, and over 99% of them show phase-averaged spectra with an exponential or sub-exponential cutoff at a few GeV. A polar-cap accelerator, sitting in the strong field just above the neutron star's surface, would produce a much sharper (super-exponential) cutoff, because the field there converts high-energy photons into pairs before they escape; the observed shape rules it out and places the emission in the outer magnetosphere, near the light cylinder (the radius at which co-rotation with the star would reach the speed of light). That is the outer gap, and it is the outer gap's electrodynamics that we carry over. The one structural difference is where the gap comes from: in a pulsar, from the convex geometry of the dipole field far from the star; in a black hole, from frame dragging next to the horizon. Far from the hole ($$r \gg M$$) the general-relativistic charge density above reduces to the textbook flat-space form,

$$\rho_{\mathrm{GJ}} = -\frac{\boldsymbol{\Omega}\cdot\mathbf{B}}{2\pi c} + \frac{(\boldsymbol{\Omega}\times\mathbf{r})\cdot(\nabla\times\mathbf{B})}{4\pi c}$$

so the relativistic expression already carries the current corrections that the second term supplies. Close in, $$\rho_{\mathrm{GJ}}$$ vanishes where $$\Omega_F$$ matches $$\omega(r,\theta)$$; since $$\omega \propto r^{-3}$$ outward, that match is only possible near the horizon, which is why the gap sits within one or two gravitational radii of it whatever the mass of the hole.

**Where the accretion comes from** {% cite hirotani2018stellar %}**.** The MNRAS letter left a question open: where does a stellar-mass hole find an accretion rate of $$10^{-4}$$ Eddington? The ApJ paper answers it with a giant molecular cloud. Massive stars form in groups (OB associations) inside such clouds and end as black holes there, typically kicked to tens of km s$$^{-1}$$ by the supernova that makes them; sooner or later, such a hole crosses a dense part of the cloud; the cloud's sound speed is under 630 m s$$^{-1}$$, so the hole moves supersonically, a bow shock forms behind it, and gas inside the Bondi radius $$r_B \sim GM/V^{2}$$ falls in at the Bondi–Hoyle rate,

$$\dot M_B = 4\pi\lambda\,\frac{(GM)^{2}}{V^{3}}\,\rho, \qquad \dot m_B = 5.39 \times 10^{-9}\,\lambda\,n_{\mathrm{H_2}}\,M_1\left(\frac{\eta}{0.1}\right)^{-1}\left(\frac{V}{10^{2}\ \mathrm{km\,s^{-1}}}\right)^{-3}$$

with $$\lambda = 1.12$$ for isothermal gas, $$\eta \sim 0.1$$ the radiative efficiency, and $$n_{\mathrm{H_2}}$$ in cm$$^{-3}$$. The captured gas carries little angular momentum, so it forms a disc only far inside $$r_B$$ and the rate near the hole is simply $$\dot m_B$$. The gap is brightest for $$6 \times 10^{-5} < \dot m < 2 \times 10^{-4}$$, which a cloud core of $$n_{\mathrm{H_2}} \gtrsim 10^{4}$$ cm$$^{-3}$$ supplies at 100 km s$$^{-1}$$, and $$\gtrsim 1.2 \times 10^{3}$$ cm$$^{-3}$$ at 50 km s$$^{-1}$$; both are ordinary densities for a dense core, which is the point: the scenario requires nothing exotic of the cloud.

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

**What the cascade looks like, and what it emits.** With $$M = 10\,M_\odot$$ and $$a = 0.99M$$, and keeping every term of the Poisson equation rather than the $$\Delta \ll M^{2}$$ approximation used before, the electrons' Lorentz factors saturate around $$3 \times 10^{6}$$ (energies of about 1.5 TeV), the point at which curvature-radiation losses balance the acceleration, with a broad plateau between $$6 \times 10^{4}$$ and $$2 \times 10^{6}$$ held down by inverse-Compton losses; at these energies the scattering is in the Klein–Nishina regime, where the cross-section falls with electron energy, so it is the _lower_-energy electrons of the plateau that scatter most efficiently and do most of the TeV emission. The resulting spectrum is bimodal: a broad curvature peak at 0.01–1 GeV and a sharp inverse-Compton peak near 0.1 TeV, with the primary inverse-Compton component absorbed above about 0.1 TeV. The gap is brightest face-on ($$\theta < 15^\circ$$) and detectable with CTA if $$a > 0.90M$$ and the distance is under 1 kpc; at $$a = 0.50M$$ the hole would need to be within 0.3 kpc.

Two robustness results matter more than any single number, because the electric current flowing through the gap is the one input nobody can measure. Firstly, the spectrum changes little as the current created inside the gap, $$j_{\mathrm{cr}}$$, runs from 0.3 to 0.9 of the Goldreich–Julian value, and little again as the current fed in from outside runs from 0 to 0.8 of it, even though $$E_\parallel(s)$$ itself moves substantially (the gap shifts inward and deepens, but gravitational redshift takes back most of what that gains before the photons reach us). Secondly, there is no stationary solution at all once $$j_{\mathrm{cr}} > 1$$, which sets a hard ceiling rather than a soft preference. Therefore, the prediction does not depend on tuning the parameter we are least able to constrain, and that is worth more than any one number in it.

**Why it is testable, and against what.** The Galactic plane holds 76 very-high-energy sources, of which 36 were unidentified at the time; of 18 unidentified sources with radio molecular-line data, 12 sit on dense gas, and several of those are compact. The standard explanation is hadronic, i.e., protons rather than electrons: cosmic rays from a supernova remnant strike the cloud's gas, the collisions make neutral pions, and the pions decay into gamma rays with a single power-law spectrum from GeV to 100 TeV, spread over the whole cloud core ($$10^{18}$$ to $$10^{19}$$ cm). The gap model predicts something distinguishable on three counts: a **point-like** image, since the emission region is at most $$10\,r_g \sim 10^{7}$$ cm, eleven orders of magnitude smaller; a **bimodal** spectrum with peaks near 0.1 GeV and 0.1 TeV rather than a power law; and **no synchrotron counterpart**, i.e., no power-law component in radio or X-rays of the kind that an extended population of cosmic-ray electrons always produces. CTA's angular resolution is about five times better than the instruments that found these sources, which is what makes the first test possible. A source such as HESS J1800–2400C, point-like and in a cloud, is the kind of object the model is for.

**The honest caveats.** There are three, and we state them in the papers themselves rather than in a footnote. The spin $$a = 0.9999M$$ is adopted to show the extreme; a hole that preferentially swallows negative-angular-momentum photons from its own accretion flow settles at the canonical $$a = 0.998M$$, and the moderate cases interpolate between the two we solved. Stationarity is an assumption: particle-in-cell simulations of black hole gaps (which follow the individual charges in time rather than solving for a steady state) show rapid oscillations of $$E_\parallel$$ and the current, and if the injected current is a sizeable fraction of the Goldreich–Julian current the stationary picture breaks down. What we could argue is that an outer-gap-type accelerator carries a negative feedback (extra pair creation redistributes charge so as to reduce $$E_\parallel$$), unlike the polar-cap type whose positive feedback is known to be unstable, and that the closure condition is met across a wide range of currents; a proper stability analysis is a separate piece of work. In addition, the ApJ study found that when pairs are created by MeV–MeV collisions they return to the horizon and pile charge at the outer boundary, so the solution is, strictly, slowly time-dependent.

This work ran across the Korea Astronomy and Space Science Institute and the University of Science and Technology, and a visiting studentship at the Academia Sinica Institute of Astronomy and Astrophysics in Taipei. The 2017 MNRAS letter was my first peer-reviewed first-author publication, at **age 19**; the 2018 ApJ paper, on which I am a co-author, is where the same accelerator was set loose in a molecular cloud.

{% include author_self_link.liquid %}

{% include linkedin_card.liquid after_heading="references" %}
