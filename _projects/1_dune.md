---
layout: page
title: DUNE - Near Detector reconstruction
description: Systematics-aware ML reconstruction and MCMC inference for precision neutrino oscillation measurements.
img: assets/img/projects/dune.jpg
importance: 1
category: Particle Physics
---

**[Imperial College London](https://www.imperial.ac.uk/) · 2026 – present · London · with [Dr Linda Cremonesi](https://profiles.imperial.ac.uk/l.cremonesi), [Dr Patrick Dunne](https://profiles.imperial.ac.uk/p.dunne12), [Prof. Alexander Tapper](https://profiles.imperial.ac.uk/a.tapper), [Dr Alex Booth](https://profiles.imperial.ac.uk/a.booth), [Prof. Stefan Soldner-Rembold](https://profiles.imperial.ac.uk/s.soldner-rembold) and [Dr Abigail Waldron](https://www.seresearch.qmul.ac.uk/ceap/people/awaldron/) (QMUL)**

{% include affiliations.liquid logos="imperial,dune" label="" %}

<figure style="margin: 0 0 1.5rem;">
  <img src="{{ '/assets/img/projects/dune-beamline.jpg' | relative_url }}"
       alt="The DUNE beamline: protons accelerated at Fermilab produce neutrinos that travel 1,300 km through the Earth to detectors at the Sanford Underground Research Facility in South Dakota"
       style="width:100%; height:auto; border-radius:6px;" loading="eager">
  <figcaption style="font-size:0.8rem; color:var(--global-text-color-light); margin-top:0.5rem;">
    The 1,300 km baseline, from the proton accelerator at Fermilab to the far detector a mile
    underground in South Dakota. Image: <a href="https://www.fnal.gov/">Fermilab</a>.
  </figcaption>
</figure>

The [Deep Underground Neutrino Experiment](https://www.dunescience.org/) (DUNE) will fire a neutrino beam 1,300 km (1,285 km, precisely) from [Fermilab](https://www.fnal.gov/) to the [Sanford Underground Research Facility](https://sanfordlab.org/) in South Dakota, into liquid-argon time projection chambers a mile below ground. The goals are charge–parity (CP) violation in the lepton sector, the neutrino mass ordering, and physics beyond the Standard Model. The physics reach is not limited by statistics; it is limited by how well the flux and cross-section systematics can be controlled.

**What I work on.** Systematics-aware machine learning reconstruction in liquid argon time projection chambers (TPCs), coupled to MCMC (Markov chain Monte Carlo) inference, and the propagation of Near-Detector constraints into the Far-Detector oscillation fit.

**Where I actually am.** I am based in London, not Illinois or South Dakota, although I will visit the US sites occasionally. The beamline and the caverns are in the United States; the analysis is not tied to them. Simulation, fits, framework development and review all run on shared computing, so the work I do (statistical modelling, inference, reconstruction) happens from Imperial's South Kensington campus.

**[Where Imperial sits](https://www.imperial.ac.uk/high-energy-physics/research/experiments/dune/).** The group's contribution runs from hardware to inference. On the detector side it designs the data acquisition systems for both the near and far detectors, builds anode plane assemblies for one of the far-detector modules, and leads the technology for **DUNE Phase II**, in particular the high-pressure gaseous argon TPC destined for the more capable Phase-II near detector. A gas TPC sees low-momentum protons and pions that a liquid-argon detector loses below threshold, which is precisely where the nuclear-effect modelling driving the cross-section systematic is least constrained.

**Who leads it here.** My supervisor, [Dr Linda Cremonesi](https://profiles.imperial.ac.uk/l.cremonesi), leads the Imperial HEP group's work on the physics and reconstruction of the DUNE Near Detector. That is the effort my own project sits inside.

**Where my own work plugs in.** On the analysis side, Imperial leads **MaCh3**, the Bayesian oscillation-analysis framework used by the long-baseline group, with [Dr Patrick Dunne](https://profiles.imperial.ac.uk/p.dunne12) and others. That is the natural home for what I do: MaCh3 is where a reconstruction's uncertainty stops being a plot and becomes a term in the likelihood, and it is the point at which a systematics-aware network either earns its place or does not.

**Where the uncertainty actually enters.** The fit is Bayesian: the posterior over oscillation and nuisance parameters $$\vec{\theta}$$ given data $$D$$ is

$$P(\vec{\theta} \mid D) \;\propto\; P(D \mid \vec{\theta})\,P(\vec{\theta})$$

and in practice one minimises the negative log-likelihood, a Poisson term over reconstructed-energy bins plus a Gaussian penalty carrying the prior covariance $$V$$ of the systematic parameters:

$$-\log \mathcal{L} \;=\; \sum_{\mathrm{bins}}\left[\lambda(\vec{\theta}) - n + n\log\frac{n}{\lambda(\vec{\theta})}\right] \;+\; \frac{1}{2}\sum_{i,j}(\theta_i-\mu_i)\,V^{-1}_{ij}\,(\theta_j-\mu_j)$$

That second sum is the whole argument for systematics-aware reconstruction: a network's uncertainty is only worth anything if it can be written into $$V$$, and the Near Detector is what shrinks it.

**How the inference is actually done.** The posterior is never written down in closed form; it is sampled. The sampler is Metropolis-Hastings: from the current point $$\vec\theta_n$$ a candidate $$\vec y$$ is drawn from a proposal function $$q$$ (a Gaussian, in these analyses) and accepted with probability

$$\alpha(\vec\theta_n \to \vec y) \;=\; \min\!\left[1,\; \frac{P(\vec y \mid D)\;q(\vec\theta_n \mid \vec y)}{P(\vec\theta_n \mid D)\;q(\vec y \mid \vec\theta_n)}\right]$$

For a symmetric proposal the $$q$$ factors cancel and the acceptance reduces to a ratio of posteriors. Two practical consequences follow. Firstly, the step size is very nearly the whole game: too small, and the chain crawls, with successive steps so correlated that the effective sample size collapses; too large, and almost nothing is accepted. Secondly, the diagnostics are not optional: trace plots, autocorrelation, and a properly discarded burn-in are what separate a converged chain from one that is merely stuck.

What the Bayesian approach then buys, and the reason Imperial runs it alongside the frequentist fit rather than instead of it, is that nuisance parameters are _integrated out_ rather than profiled:

$$P(\theta_i \mid D) \;=\; \int P(\vec\theta \mid D)\;\prod_{j \neq i} d\theta_j$$

Marginalising over several hundred systematic parameters is essentially free once the chain exists, and so is the posterior of any derived quantity. Furthermore, a finished chain can be re-analysed under a different prior simply by reweighting each step,

$$w(\vec\theta) \;=\; \frac{\pi'(\vec\theta)}{\pi(\vec\theta)}$$

so a reactor short-baseline constraint on $$\theta_{13}$$, or a change from a flat prior in $$\delta_{CP}$$ to a flat prior in $$\sin\delta_{CP}$$, can be applied _post hoc_ without re-running the fit. That flexibility is not merely a convenience; rather, it is what makes the prior dependence of a result auditable at all.

Where the compute actually goes is worth knowing too, since it decides what is feasible to iterate on. The MCMC step time is dominated by the likelihood evaluation, which splits into two expensive pieces: the oscillation probabilities and the systematic weights. Parallelising the oscillation calculator across roughly five CPU threads already brings the step time to something comparable with a GPU configuration, because at that point the systematic weights dominate. Moving only half of the calculation onto a GPU therefore buys much less than it appears to.

**What the first Bayesian DUNE sensitivities already show.** Imperial produced the first Bayesian oscillation sensitivity study of DUNE (L. Warsame, _First Bayesian Neutrino Oscillation Sensitivities of DUNE_, PhD thesis, Imperial College London, 2025, supervised by Dunne and Tapper; now a collaboration paper, [arXiv:2608.04059](https://arxiv.org/abs/2608.04059)). Three results from that work frame my own:

- The posterior is broadly correlated across the four-dimensional oscillation parameter space, most sharply between $$\sin^{2}\theta_{23}$$ and $$\sin^{2}\theta_{13}$$. Applying the reactor $$\theta_{13}$$ constraint suppresses the wrong-octant peak and substantially improves octant sensitivity: a good illustration of prior reweighting earning its keep.
- It contains the first study of DUNE's sensitivity to the Jarlskog invariant $$J$$, the parameterisation-independent measure of leptonic CP violation. At the Asimov point used, a 336 kt-MW-yr exposure and the reactor constraint applied, $$J = 0$$ (i.e., CP conservation) is excluded at $$3\sigma$$; $$\delta_{CP} = 0$$ is likewise excluded at $$3\sigma$$. These are sensitivity projections at an assumed true point, not measurements.
- Adding near-detector samples tightens the credible intervals on $$\sin^{2}\theta_{23}$$, $$\sin^{2}\theta_{13}$$ and $$\Delta m^{2}_{32}$$ considerably, whilst $$\delta_{CP}$$ improves much less: at this exposure $$\delta_{CP}$$ remains statistically limited, and the others do not.

**The over-constraint problem, and why it is mine.** The most useful result in that study is a negative one. DUNE's near detector will record of order $$10^{8}$$ neutrino interactions at 336 kt-MW-yr; for comparison, [T2K](https://t2k-experiment.org/) has collected roughly $$2 \times 10^{5}$$ across all of its near-detector samples in about a decade of running. Once statistical uncertainty is effectively gone, the fit will constrain whatever the systematic model permits it to constrain, whether or not that constraint is physical. In the joint near-and-far fit, the quasi-elastic axial mass $$M_A^{QE}$$ came back with a posterior $$1\sigma$$ of $$8.6 \times 10^{-5}$$ against a prior uncertainty of 1: four orders of magnitude, which nobody believes.

The diagnosis was degeneracy, or rather its absence from the model. Introducing a deliberately duplicated, perfectly degenerate copy of $$M_A^{QE}$$ (constructed so that only one of the pair affects the far detector) widened the posterior by a factor of roughly 100, to $$6.2 \times 10^{-3}$$: better, and still not credible. The lesson generalises. When a systematic model omits degeneracies that exist in the real experiment, a high-statistics near detector does not expose the omission; rather, it converts it into a confidently wrong number. Tellingly, the symptom showed up in the sampler itself, as poor mixing and a visibly jagged posterior.

That is precisely why I work on the propagation of uncertainty rather than on resolution. In this regime, a reconstruction that is not honest about its own degeneracies does not make the fit less accurate in any obvious way; it makes the fit more confident, which is worse.

**Where I sit here.** Mostly on these equations. My main work is the statistical modelling: Bayesian inference and MCMC for the oscillation sensitivities, together with the phenomenology and the underlying physics that fix what those parameters mean before anything is fitted. ML reconstruction comes last in that order, and deliberately so: it is an input whose uncertainty has to survive the likelihood, not the point of the exercise.

**The framing.** The Near Detector is not merely a control detector. Rather, it is the constraint engine: it pins down the nuisance parameters that would otherwise dominate the measurement. The interesting problem is therefore not "how accurate is the reconstruction," but "how faithfully does the uncertainty on the reconstruction propagate through to the posterior on $$\delta_{CP}$$."

**The principle I work under.** Machine learning should augment physical interpretation, never replace it. A network that improves resolution whilst hiding its own failure modes is a worse instrument than a slower method whose biases you can enumerate.

_Work in progress; outputs will appear here and on [Publications](/publications/)._

{% include linkedin_card.liquid %}
