---
layout: page
title: Quantum-accelerated CFD - Singularity Quantum
description: Augmenting the computational fluid dynamics model behind non-invasive cardiovascular diagnostics.
img: assets/img/projects/quantum.jpg
importance: 1
category: Quantum Computing
---

**[Singularity Quantum](https://singularityquantum.com/) · part-time · 2026 – present · with [Dr Victoria Rolandi](https://www.linkedin.com/in/victoria-rolandi-b0bb25160/), [Dr Austin Tapp](https://www.linkedin.com/in/austintapp/) and [Prof Doyeol (David) Ahn](https://www.linkedin.com/in/doyeol-david-ahn-06165558/)**

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
    first three steps, before the solver runs at all. Illustrative only: this is a generic
    example of such a pipeline, not output from our own work.
  </figcaption>
</figure>

**My role.** I work part-time with their computational fluid dynamics (CFD) engineers - among them [Victoria Rolandi](https://www.linkedin.com/in/victoria-rolandi-b0bb25160/) - on augmenting and enhancing the CFD model, the classical solver that the quantum work is built around. My contribution is technical and methodological throughout: fluid-dynamics modelling, numerics, the underlying physics, the quantum computing side, and ML engineering. Cardiology is not my interest, and I make no claim to it: that expertise sits entirely with my collaborators. I have learned only what the modelling demands, enough coronary anatomy and haemodynamics to know what the geometry and the pressure ratio actually mean, and no further.

**The governing equations.** Coronary blood flow is modelled as an incompressible fluid, so the solver is working on the incompressible Navier–Stokes equations:

$$\rho\left(\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u}\cdot\nabla)\,\mathbf{u}\right) = -\nabla p + \mu\,\nabla^{2}\mathbf{u}$$

$$\nabla\cdot\mathbf{u} = 0$$

with $$\mathbf{u}$$ the velocity field, $$p$$ the pressure, $$\rho$$ the density and $$\mu$$ the dynamic viscosity. Term by term in the momentum equation: $$\rho\,\partial\mathbf{u}/\partial t$$ is unsteady inertia, which matters because coronary flow is pulsatile rather than steady; $$\rho(\mathbf{u}\cdot\nabla)\mathbf{u}$$ is convective inertia, the nonlinear term, and the source of most of the difficulty; $$-\nabla p$$ is the pressure gradient; $$\mu\nabla^{2}\mathbf{u}$$ is viscous diffusion. The second equation is mass conservation for an incompressible fluid.

Two consequences follow, and they shape everything below. The clinical quantity is a **pressure ratio** across a stenosis, so the entire pipeline reduces to resolving $$\nabla p$$ faithfully. And because the convective term is nonlinear, Navier–Stokes is not a linear system that a quantum linear solver can be pointed at directly: the linear algebra only appears once the equations have been discretised and linearised. That is a large part of why the classical layer, rather than the quantum kernel, is where the accuracy is won or lost.

**Why the classical layer is the interesting part.** In a CT-FFR pipeline the accuracy is not dominated by solver speed. It is dominated by three things around the solver: the segmentation of the coronary tree from the CT, the outlet boundary conditions where a whole downstream vasculature you cannot see is compressed into a lumped-parameter model, and the rheological choices - Newtonian or shear-thinning blood, rigid or compliant walls. Get those wrong and a solver a thousand times faster converges beautifully to the wrong number, sooner.

That is the same problem I have been working on elsewhere. In [AtriPINN](/projects/3_atripinn/) the governing equation was never the hard part; the hard part was a sparse, noisy observation operator. Physics-informed methods are well suited to exactly that class of problem, because they let unknown boundary conditions and material parameters be _learned_ while the partial differential equation (PDE) is still enforced.

**How it connects to my other work.** My fluid-dynamics background is general-relativistic magnetohydrodynamics ([GRMHD](/projects/6_sgra/)): conservative finite-volume schemes on curvilinear grids, approximate Riemann solvers, Courant–Friedrichs–Lewy (CFL) conditions, grid-convergence studies. The numerical craft transfers directly. What does not transfer is pressure–velocity coupling: general-relativistic magnetohydrodynamics is compressible and hyperbolic, so there is no incompressibility constraint, no pressure–Poisson equation, and none of the machinery that incompressible coronary flow makes central. That gap is the part I am actively closing.

**Where this is heading.** I have put a research proposal to the company for a single physics-informed framework carrying two clinical tracks, both of which I think are equally doable here. One extends the [AtriPINN](/projects/3_atripinn/) work in cardiac electrophysiology towards real-time arrhythmia characterisation. The other is the CFD side: physics-informed surrogates and reconstruction models built on top of the existing solver stack, so the pipeline runs faster and extracts more from the imaging without giving up the physics that makes the number trustworthy. The point of one framework rather than two is that they share a network core, a set of switchable physics residuals and a common uncertainty layer, which is exactly what let AtriPINN carry three physics back-ends behind one pipeline. The same machinery points at further directions beyond the first year, tumour microcirculation and myocardial perfusion among them. Specifics will follow the results rather than precede them.

**Where the interest started.** Around 2007 and 2008 I became obsessed with quantum information and quantum computing, and it has stayed with me ever since, running underneath everything I have done in academia. That is not incidental to this project; it is why it appealed to me in the first place.

**And a coincidence.** One of Singularity Quantum's co-founders is Professor **[Doyeol (David) Ahn](https://www.linkedin.com/in/doyeol-david-ahn-06165558/)**, in whose physics classes at the University of Seoul I sat for about a year in 2007, aged nine. It was through him, over 2007 and 2008, that I first learned quantum computing and quantum information. Nearly twenty years of doing physics later, the thread loops back.

_Work in progress; outputs will appear here and on [Publications](/publications/)._

{% include linkedin_badge.liquid %}
