---
layout: page
title: DUNE — Near Detector reconstruction
description: Systematics-aware ML reconstruction and MCMC inference for precision neutrino oscillation measurements.
img: assets/img/projects/dune.jpg
importance: 1
category: physics
---

**[Imperial College London](https://www.imperial.ac.uk/) · 2026 – present · with [Dr Linda Cremonesi](https://profiles.imperial.ac.uk/l.cremonesi)**

The [Deep Underground Neutrino Experiment](https://www.dunescience.org/) will fire a neutrino beam 1,300 km from [Fermilab](https://www.fnal.gov/) to the [Sanford Underground Research Facility](https://sanfordlab.org/) in South Dakota, into liquid-argon time projection chambers a mile below ground. The goals are charge–parity (CP) violation in the lepton sector, the neutrino mass ordering, and physics beyond the Standard Model. The physics reach is not limited by statistics — it is limited by how well the flux and cross-section systematics can be controlled.

**What I work on.** Systematics-aware machine learning reconstruction in liquid argon time projection chambers (TPCs), coupled to MCMC (Markov chain Monte Carlo) inference, and the propagation of Near-Detector constraints into the Far-Detector oscillation fit.

**Where Imperial sits.** The group is heavily involved in the technology for [DUNE Phase II](https://www.imperial.ac.uk/high-energy-physics/research/experiments/dune/), in particular the design and construction of the high-pressure gaseous argon TPC that will form part of the more capable Phase-II near detector. A gas TPC sees low-momentum protons and pions that a liquid-argon detector loses below threshold — which is precisely where the nuclear-effect modelling that drives the cross-section systematic is least constrained.

**The framing.** The Near Detector is not merely a control detector. Rather, it is the constraint engine: it pins down the nuisance parameters that would otherwise dominate the measurement. The interesting problem is therefore not "how accurate is the reconstruction," but "how faithfully does the uncertainty on the reconstruction propagate through to the posterior on $$\delta_{CP}$$."

**The principle I work under.** Machine learning should augment physical interpretation, never replace it. A network that improves resolution while hiding its own failure modes is a worse instrument than a slower method whose biases you can enumerate.

*Work in progress; outputs will appear here and on [Publications](/publications/).*
