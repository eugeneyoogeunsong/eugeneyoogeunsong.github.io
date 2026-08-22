---
layout: page
title: DUNE - Near Detector reconstruction
description: Systematics-aware ML reconstruction and MCMC inference for precision neutrino oscillation measurements.
img: assets/img/projects/dune.jpg
importance: 1
category: Particle Physics
---

**[Imperial College London](https://www.imperial.ac.uk/) · 2026 – present · with [Dr Linda Cremonesi](https://profiles.imperial.ac.uk/l.cremonesi), [Dr Patrick Dunne](https://profiles.imperial.ac.uk/p.dunne12), [Prof. Alexander Tapper](https://profiles.imperial.ac.uk/a.tapper) and [Dr Alex Booth](https://profiles.imperial.ac.uk/a.booth)**

<figure style="margin: 0 0 1.5rem;">
  <img src="{{ '/assets/img/projects/dune-beamline.jpg' | relative_url }}"
       alt="The DUNE beamline: protons accelerated at Fermilab produce neutrinos that travel 1,300 km through the Earth to detectors at the Sanford Underground Research Facility in South Dakota"
       style="width:100%; height:auto; border-radius:6px;" loading="eager">
  <figcaption style="font-size:0.8rem; color:var(--global-text-color-light); margin-top:0.5rem;">
    The 1,300 km baseline, from the proton accelerator at Fermilab to the far detector a mile
    underground in South Dakota. Image: <a href="https://www.fnal.gov/">Fermilab</a>.
  </figcaption>
</figure>

The [Deep Underground Neutrino Experiment](https://www.dunescience.org/) will fire a neutrino beam 1,300 km from [Fermilab](https://www.fnal.gov/) to the [Sanford Underground Research Facility](https://sanfordlab.org/) in South Dakota, into liquid-argon time projection chambers a mile below ground. The goals are charge–parity (CP) violation in the lepton sector, the neutrino mass ordering, and physics beyond the Standard Model. The physics reach is not limited by statistics; it is limited by how well the flux and cross-section systematics can be controlled.

**What I work on.** Systematics-aware machine learning reconstruction in liquid argon time projection chambers (TPCs), coupled to MCMC (Markov chain Monte Carlo) inference, and the propagation of Near-Detector constraints into the Far-Detector oscillation fit.

**[Where Imperial sits](https://www.imperial.ac.uk/high-energy-physics/research/experiments/dune/).** The group's contribution runs from hardware to inference. On the detector side it designs the data acquisition systems for both the near and far detectors, builds anode plane assemblies for one of the far-detector modules, and leads the technology for **DUNE Phase II**, in particular the high-pressure gaseous argon TPC destined for the more capable Phase-II near detector. A gas TPC sees low-momentum protons and pions that a liquid-argon detector loses below threshold, which is precisely where the nuclear-effect modelling driving the cross-section systematic is least constrained.

**Where my own work plugs in.** On the analysis side, Imperial leads **MaCh3**, the Bayesian oscillation-analysis framework used by the long-baseline group, with [Dr Patrick Dunne](https://profiles.imperial.ac.uk/p.dunne12) and others. That is the natural home for what I do: MaCh3 is where a reconstruction's uncertainty stops being a plot and becomes a term in the likelihood, and it is the point at which a systematics-aware network either earns its place or does not.

**Where the uncertainty actually enters.** The fit is Bayesian: the posterior over oscillation and nuisance parameters $$\vec{\theta}$$ given data $$D$$ is

$$P(\vec{\theta} \mid D) \;\propto\; P(D \mid \vec{\theta})\,P(\vec{\theta})$$

and in practice one minimises the negative log-likelihood, a Poisson term over reconstructed-energy bins plus a Gaussian penalty carrying the prior covariance $$V$$ of the systematic parameters:

$$-\log \mathcal{L} \;=\; \sum_{\mathrm{bins}}\left[\lambda(\vec{\theta}) - n + n\log\frac{n}{\lambda(\vec{\theta})}\right] \;+\; \frac{1}{2}\sum_{i,j}(\theta_i-\mu_i)\,V^{-1}_{ij}\,(\theta_j-\mu_j)$$

That second sum is the whole argument for systematics-aware reconstruction: a network's uncertainty is only worth anything if it can be written into $$V$$, and the Near Detector is what shrinks it.

**The framing.** The Near Detector is not merely a control detector. Rather, it is the constraint engine: it pins down the nuisance parameters that would otherwise dominate the measurement. The interesting problem is therefore not "how accurate is the reconstruction," but "how faithfully does the uncertainty on the reconstruction propagate through to the posterior on $$\delta_{CP}$$."

**The principle I work under.** Machine learning should augment physical interpretation, never replace it. A network that improves resolution while hiding its own failure modes is a worse instrument than a slower method whose biases you can enumerate.

_Work in progress; outputs will appear here and on [Publications](/publications/)._

{% include linkedin_badge.liquid %}
