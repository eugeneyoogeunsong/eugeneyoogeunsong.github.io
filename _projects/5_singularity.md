---
layout: page
title: Quantum-accelerated CFD — Singularity Quantum
description: Augmenting the computational fluid dynamics model behind non-invasive cardiovascular diagnostics.
img: assets/img/projects/quantum.jpg
importance: 1
category: quantum computing
---

**[Singularity Quantum](https://singularityquantum.com/) · part-time · 2026 – present**

[Singularity Quantum](https://singularityquantum.com/) is building quantum-enhanced biomechanical modelling for precision treatment decisions. The flagship application is **CT-FFR** — deriving fractional flow reserve, the pressure ratio a cardiologist uses to decide whether a coronary stenosis needs intervention, from a CT scan rather than from a catheter. Done well, it replaces an invasive procedure with a simulation.

**My role.** I work part-time with their CFD engineers on augmenting and enhancing the CFD model — the classical solver that the quantum work is built around.

**Why the classical layer is the interesting part.** In a CT-FFR pipeline the accuracy is not dominated by solver speed. It is dominated by three things around the solver: the segmentation of the coronary tree from the CT, the outlet boundary conditions where a whole downstream vasculature you cannot see is compressed into a lumped-parameter model, and the rheological choices — Newtonian or shear-thinning blood, rigid or compliant walls. Get those wrong and a solver a thousand times faster converges beautifully to the wrong number, sooner.

That is the same problem I have been working on elsewhere. In [AtriPINN](/projects/) the governing equation was never the hard part; the hard part was a sparse, noisy observation operator. Physics-informed methods are well suited to exactly that class of problem, because they let unknown boundary conditions and material parameters be *learned* while the PDE is still enforced.

**How it connects to my other work.** My fluid-dynamics background is [GRMHD](/projects/) — conservative finite-volume schemes on curvilinear grids, approximate Riemann solvers, CFL conditions, grid-convergence studies. The numerical craft transfers directly. What does not transfer is pressure–velocity coupling: general-relativistic MHD is compressible and hyperbolic, so there is no incompressibility constraint, no pressure–Poisson equation, and none of the machinery that incompressible coronary flow makes central. That gap is the part I am actively closing.

**And a coincidence.** One of Singularity Quantum's co-founders is Professor **Doyeol (David) Ahn**, in whose physics classes at the University of Seoul I sat for about a year in 2007, aged nine. Nearly twenty years of doing physics later, the thread loops back.
