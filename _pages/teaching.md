---
layout: page
title: Teaching
permalink: /teaching/
description: How I teach, the summaries I have made public, and how to reach me about tutoring.
nav: true
nav_order: 6
---

<style>
  /* Scoped to this page. al-folio v1.x ships with Bootstrap compat disabled,
     so .row and col-* are undefined; everything here is self-contained CSS on
     the theme's own custom properties, so dark mode follows along.
     Classes and tags only: PurgeCSS strips attribute selectors from the build. */

  .tn-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1rem;
    margin: 1.4rem 0 2rem;
  }
  .tn-card {
    border: 1px solid var(--global-divider-color);
    border-radius: 8px;
    background: var(--global-card-bg-color);
    padding: 1rem 1.15rem 1.05rem;
    display: flex;
    flex-direction: column;
  }
  .tn-card h4 {
    font-size: 1rem;
    font-weight: 700;
    margin: 0 0 0.15rem;
    line-height: 1.3;
  }
  .tn-card h4 a {
    color: inherit;
    text-decoration: underline;
    text-decoration-color: rgba(20, 20, 26, 0.25);
  }
  .tn-card h4 a:hover {
    color: var(--global-theme-color);
    text-decoration-color: currentColor;
  }
  .tn-pages {
    font-size: 0.75rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--global-theme-color);
    font-weight: 700;
    margin: 0 0 0.6rem;
  }
  .tn-card ul {
    margin: 0;
    padding-left: 1.1rem;
    font-size: 0.87rem;
    color: var(--global-text-color-light);
    line-height: 1.5;
  }

  /* Subject pills, same visual language as .mo-outlets on the Media page.
     Static text, so no link or hover-navigation affordance. */
  .tn-topics {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 1.25rem 0 1.75rem;
    padding: 0;
    list-style: none;
  }
  .tn-topics li {
    font-size: 0.82rem;
    padding: 0.3rem 0.75rem;
    color: var(--global-text-color-light);
    border: 1px solid var(--global-divider-color);
    border-radius: 999px;
    transition: border-color 0.15s ease, color 0.15s ease;
  }
  .tn-topics li:hover {
    border-color: var(--global-theme-color);
    color: var(--global-theme-color);
  }
</style>

From 2026 onwards, I'm seeking any teaching opportunities in London or elsewhere.

I learn best by teaching. That is not a slogan about generosity: explaining something is the only reliable way I have found to see how deeply I understand it, the so-called Feynman technique. So I teach a fair amount, and the summaries below exist because writing them was how I learned the material in the first place.

The way I teach follows from the same thing. I start from the premise rather than the procedure, because a student who can only reproduce a method is stuck the moment the problem is phrased differently. That takes longer at the start and is much faster afterwards. I would happily talk for hours about <a href="https://yoogeunsong.com/projects/#Particle%20Physics" class="plain-link">fundamental physics</a>, <a href="https://yoogeunsong.com/projects/#Machine%20Learning" class="plain-link">machine learning</a>, <a href="https://yoogeunsong.com/projects/#Quantum%20Computing" class="plain-link">quantum computing</a>, first principles, psychology, neuroscience, philosophy, music, or films.

As of 2026, I currently have no teaching duties at <a href="https://www.imperial.ac.uk/physics/" class="plain-link">Imperial</a> or elsewhere, because I am going all in on my <a href="/research/" class="plain-link">research projects</a>. My official teaching for physics classes at <a href="https://www.imperial.ac.uk/physics/">Imperial</a> may begin from 2027 onwards, and I will list it here if it does. For now this page holds the summaries I have made public, and tutoring. **I teach in English**, which is my preference for teaching, though I can also teach in **Korean** or, with some limitations, even in **French** where the circumstances call for it. I welcome any opportunities for teaching - <a href="/contact/" class="plain-link">reach out</a>!

I have also given talks many times in schools, at science museums and at expos, alongside the broadcast work collected under <a href="/media/" class="plain-link">Media & Outreach</a>. I welcome those opportunities too.

## Study materials

My handwritten summaries from the <a href="/cv/#education" class="plain-link">Master's in Physics</a> at <a href="https://www.imperial.ac.uk/physics/" class="plain-link">Imperial</a> (2024–2025), one folder per module, released under the MIT Licence in [imperial-physics-notes](https://github.com/eugeneyoogeunsong/imperial-physics-notes). Corrections by issue or pull request are welcome.

<div class="tn-grid">
  <div class="tn-card">
    <h4><a href="https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/advanced-quantum-field-theory">Advanced Quantum Field Theory</a></h4>
    <p class="tn-pages">227 pages</p>
    <ul>
      <li>Functional methods and the generating functional</li>
      <li>Renormalisation and the renormalisation group</li>
      <li>Non-abelian gauge theories, Faddeev–Popov ghosts</li>
      <li>Spontaneous symmetry breaking and the Higgs mechanism</li>
      <li>Anomalies</li>
    </ul>
  </div>
  <div class="tn-card">
    <h4><a href="https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/quantum-field-theory">Quantum Field Theory</a></h4>
    <p class="tn-pages">138 pages</p>
    <ul>
      <li>Canonical quantisation of scalar, spinor and vector fields</li>
      <li>The S-matrix, Wick's theorem, Feynman rules</li>
      <li>Tree-level cross sections and decay rates</li>
      <li>Loop corrections and regularisation</li>
    </ul>
  </div>
  <div class="tn-card">
    <h4><a href="https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/advanced-particle-physics">Advanced Particle Physics</a></h4>
    <p class="tn-pages">94 pages</p>
    <ul>
      <li>Electroweak unification and precision tests</li>
      <li>QCD, asymptotic freedom, parton distributions</li>
      <li>Flavour physics and CP violation</li>
      <li>Neutrino masses and oscillations</li>
      <li>Beyond the Standard Model: the Higgs sector and dark matter</li>
    </ul>
  </div>
</div>

Alongside those sits my <a href="https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/comp-phys-mini-project" class="plain-link">computational physics mini-project</a>, a finite-difference time-domain solver for the time-dependent Schrödinger equation written in Mathematica, with animations of wave-packet dispersion, reflection and tunnelling across four potentials. Five weeks of work rather than a full research project, and awarded the highest grade by [Dr Jaroslaw Pasternak](https://profiles.imperial.ac.uk/j.pasternak).

One thing the repository deliberately does not contain: lecture notes, slides, problem sheets or past papers produced by Imperial or anyone else. Those belong to their authors and are not mine to redistribute. Everything published there is my own handwriting and my own code.

## Tutoring

For tutoring specifically: private or in groups, online or in person in London. Undergraduate and Master's students who study physics and mathematics are the natural fit - quantum mechanics, quantum field theory, particle physics, general relativity, mathematical methods - along with scientific Python and machine learning for people coming to it from a physics background.

The subjects I cover:

<ul class="tn-topics">
  <li>GCSE Physics</li>
  <li>A-level Physics</li>
  <li>A-level Mathematics</li>
  <li>Algebra</li>
  <li>Geometry</li>
  <li>Calculus</li>
  <li>Linear Algebra</li>
  <li>Mathematical Methods for Physicists</li>
  <li>Engineering Mathematics</li>
  <li>Classical Mechanics</li>
  <li>Electrodynamics</li>
  <li>Special Relativity</li>
  <li>General Relativity</li>
  <li>Fluid Mechanics</li>
  <li>Quantum Mechanics</li>
  <li>Quantum Field Theory</li>
  <li>Particle Physics</li>
  <li>Quantum Information</li>
  <li>Cosmology</li>
  <li>Computational Physics</li>
  <li>Machine Learning</li>
</ul>

On format, level and everything else I am flexible. For opportunities, <a href="/contact/" class="plain-link">reach out</a>!

{% include linkedin_badge.liquid %}

{% include goatcounter.liquid %}
