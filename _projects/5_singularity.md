---
layout: page
title: Quantum-accelerated CFD - Singularity Quantum
description: Augmenting the computational fluid dynamics model behind non-invasive cardiovascular diagnostics.
img: assets/img/projects/quantum.jpg
importance: 1
category: Quantum Computing
---

**[Singularity Quantum](https://singularityquantum.com/) · part-time · 2026 – present**

[Singularity Quantum](https://singularityquantum.com/) is building quantum-enhanced biomechanical modelling for precision treatment decisions. The flagship application is **CT-FFR**: fractional flow reserve (FFR) derived from a CT scan. FFR is the pressure ratio a cardiologist uses to decide whether a coronary stenosis needs intervention, from a CT scan rather than from a catheter. Done well, it replaces an invasive procedure with a simulation.

<figure style="margin: 0 0 1.5rem; text-align: center;">
  <img
    src="{{ '/assets/img/projects/quantum-pipeline.jpg' | relative_url }}"
    alt="Model generation pipeline: functional CT imaging, segmentation, registration against a template, producing a 4D CFD-ready model of an infarcted ventricle"
    style="max-width: 100%; height: auto; border-radius: 6px"
    loading="eager"
  />
  <figcaption style="font-size: 0.8rem; color: var(--global-text-color-light); margin-top: 0.5rem">
    From scan to solver: functional CT imaging, segmentation, registration against a template,
    and out the other end a 4D CFD-ready mesh. Almost all the accuracy is won or lost in the
    first three steps, before the solver runs at all.
  </figcaption>
</figure>

**My role.** I work part-time with their computational fluid dynamics (CFD) engineers - among them [Victoria Rolandi](https://www.linkedin.com/in/victoria-rolandi-b0bb25160/) - on augmenting and enhancing the CFD model, the classical solver that the quantum work is built around. My contribution is technical and methodological throughout: fluid-dynamics modelling, numerics, the quantum computing side, and ML engineering. I am not a clinician and make no claim to the cardiology; that expertise belongs to my collaborators, and cardiology itself is not where my own interest lies.

**Why the classical layer is the interesting part.** In a CT-FFR pipeline the accuracy is not dominated by solver speed. It is dominated by three things around the solver: the segmentation of the coronary tree from the CT, the outlet boundary conditions where a whole downstream vasculature you cannot see is compressed into a lumped-parameter model, and the rheological choices (Newtonian or shear-thinning blood, rigid or compliant walls). Get those wrong and a solver a thousand times faster converges beautifully to the wrong number, sooner.

That is the same problem I have been working on elsewhere. In [AtriPINN](/projects/3_atripinn/) the governing equation was never the hard part; the hard part was a sparse, noisy observation operator. Physics-informed methods are well suited to exactly that class of problem, because they let unknown boundary conditions and material parameters be _learned_ while the partial differential equation (PDE) is still enforced.

**How it connects to my other work.** My fluid-dynamics background is general-relativistic magnetohydrodynamics ([GRMHD](/projects/6_sgra/)): conservative finite-volume schemes on curvilinear grids, approximate Riemann solvers, Courant–Friedrichs–Lewy (CFL) conditions, grid-convergence studies. The numerical craft transfers directly. What does not transfer is pressure–velocity coupling: general-relativistic magnetohydrodynamics is compressible and hyperbolic, so there is no incompressibility constraint, no pressure–Poisson equation, and none of the machinery that incompressible coronary flow makes central. That gap is the part I am actively closing.

**And a coincidence.** One of Singularity Quantum's co-founders is Professor **[Doyeol (David) Ahn](https://www.linkedin.com/in/doyeol-david-ahn-06165558/)**, in whose physics classes at the University of Seoul I sat for about a year in 2007, aged nine. Nearly twenty years of doing physics later, the thread loops back.
