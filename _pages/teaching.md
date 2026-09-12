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
  /* Lift shadow, split by theme: a black shadow is invisible against a
     near-black page, and dark is now the default on desktop. */
  :root {
    --tn-lift-shadow: rgba(0, 0, 0, 0.12);
  }
  html[data-theme="dark"] {
    --tn-lift-shadow: rgba(0, 0, 0, 0.55);
  }

  /* The whole card is the link. It is an <a> in the markup rather than a <div>
     with an <a> inside it: an anchor may wrap headings, paragraphs and lists
     (they are flow content), but it may NOT contain another anchor, so the old
     <h4><a> had to go rather than being nested inside this one.

     cursor: pointer is right here, unlike the Media stat tiles: this card really
     does navigate, so the promise the pointer makes is one it keeps. */
  .tn-card {
    border: 1px solid var(--global-divider-color);
    border-radius: 8px;
    background: var(--global-card-bg-color);
    padding: 1rem 1.15rem 1.05rem;
    display: flex;
    flex-direction: column;
    color: inherit;
    text-decoration: none;
    cursor: pointer;
    transition:
      transform 0.18s ease,
      box-shadow 0.18s ease,
      border-color 0.18s ease;
  }
  .tn-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 18px var(--tn-lift-shadow);
    border-color: var(--global-theme-color);
    text-decoration: none;
  }
  .tn-card h4 {
    font-size: 1rem;
    font-weight: 700;
    margin: 0 0 0.15rem;
    line-height: 1.3;
  }
  /* Underline on hover only. A permanent underline would need a colour literal
     that works in both themes, and with the whole card clickable the lift and
     the border already say "this goes somewhere"; the underline just confirms
     where. */
  .tn-card:hover h4 {
    color: var(--global-theme-color);
    text-decoration: underline;
  }
  .tn-pages {
    font-size: 0.75rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    /* Same eyebrow colour as .affil-label; see --local-accent-deep in
       _sass/_themes.scss. Two different kicker colours on one site would read
       as an accident. */
    color: var(--local-accent-deep, #312e81);
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

As of 2026, I am going all in on my <a href="/research/" class="plain-link">research projects</a> at <a href="https://www.imperial.ac.uk/physics/" class="plain-link">Imperial</a>, so I am yet to take on teaching duties here or elsewhere. My official teaching for physics classes at <a href="https://www.imperial.ac.uk/physics/">Imperial</a> may begin from 2027 onwards, and I will list it here if it does. For now this page holds the summaries I have made public, and tutoring. **I teach in English**, which is my preference for teaching, though I can also teach in **Korean** or, with some limitations, even in **French** where the circumstances call for it. I welcome any opportunities for teaching - <a href="/contact/" class="plain-link">reach out</a>!

I have also given talks many times in schools, at science museums and at expos, alongside the broadcast work collected under <a href="/media/" class="plain-link">Media & Outreach</a>. I welcome those opportunities too.

## Study materials

My handwritten summaries from the <a href="/cv/#education" class="plain-link">Master's in Physics</a> at <a href="https://www.imperial.ac.uk/physics/" class="plain-link">Imperial</a> (2024–2025), one folder per module, released under the MIT Licence in [imperial-physics-notes](https://github.com/eugeneyoogeunsong/imperial-physics-notes). Corrections by issue or pull request are welcome.

{% include affiliations.liquid logos="imperial" label="" %}

<div class="tn-grid">
  <a class="tn-card" href="https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/advanced-quantum-field-theory">
    <h4>Advanced Quantum Field Theory</h4>
    <p class="tn-pages">227 pages</p>
    <ul>
      <li>Functional methods and the generating functional</li>
      <li>Renormalisation and the renormalisation group</li>
      <li>Non-abelian gauge theories, Faddeev–Popov ghosts</li>
      <li>Spontaneous symmetry breaking and the Higgs mechanism</li>
      <li>Anomalies</li>
    </ul>
  </a>
  <a class="tn-card" href="https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/quantum-field-theory">
    <h4>Quantum Field Theory</h4>
    <p class="tn-pages">138 pages</p>
    <ul>
      <li>Canonical quantisation of scalar, spinor and vector fields</li>
      <li>The S-matrix, Wick's theorem, Feynman rules</li>
      <li>Tree-level cross sections and decay rates</li>
      <li>Loop corrections and regularisation</li>
    </ul>
  </a>
  <a class="tn-card" href="https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/advanced-particle-physics">
    <h4>Advanced Particle Physics</h4>
    <p class="tn-pages">94 pages</p>
    <ul>
      <li>Electroweak unification and precision tests</li>
      <li>QCD, asymptotic freedom, parton distributions</li>
      <li>Flavour physics and CP violation</li>
      <li>Neutrino masses and oscillations</li>
      <li>Beyond the Standard Model: the Higgs sector and dark matter</li>
    </ul>
  </a>
</div>

Alongside those sits my <a href="https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/comp-phys-mini-project" class="plain-link">computational physics mini-project</a>, a finite-difference time-domain solver for the time-dependent Schrödinger equation written in Mathematica, with animations of wave-packet dispersion, reflection and tunnelling across four potentials. This was five weeks of work rather than a full research project, and it was awarded the highest grade by [Dr Jaroslaw Pasternak](https://profiles.imperial.ac.uk/j.pasternak) in 2025.

The three modules above were run by <a href="https://profiles.imperial.ac.uk/a.tolley">Prof. Andrew Tolley</a> (Advanced Quantum Field Theory), <a href="https://profiles.imperial.ac.uk/t.wiseman">Prof. Toby Wiseman</a> (Quantum Field Theory) and <a href="https://profiles.imperial.ac.uk/m.mccann">Dr Michael McCann</a> (Advanced Particle Physics). Incidentally, Dr McCann is also part of the <a href="https://www.imperial.ac.uk/high-energy-physics/">Imperial High Energy Physics group</a>, my own group, and works on flavour physics and b-quark decays on <a href="https://lhcb.web.cern.ch/">LHCb</a> at CERN.

I took several others that have no folder here: Mathematical Methods for Physicists with <a href="https://profiles.imperial.ac.uk/f.dowker">Prof. Fay Dowker</a>; General Relativity with <a href="https://profiles.imperial.ac.uk/c.de-rham">Prof. Claudia de Rham</a>; and Advanced Classical Physics, again with <a href="https://profiles.imperial.ac.uk/a.tolley">Prof. Andrew Tolley</a>.

I know all of these subjects mentioned here well, inside out, so I can supply study materials for any of them, and I am able to teach all of them.
The advanced subjects I can teach, and supply materials for:

<ul class="tn-topics">
  <li><a href="https://ocw.mit.edu/courses/8-323-relativistic-quantum-field-theory-i-spring-2023/pages/syllabus/">Quantum Field Theory</a></li>
  <li><a href="https://ocw.mit.edu/courses/8-701-introduction-to-nuclear-and-particle-physics-fall-2020/pages/syllabus/">Particle Physics</a></li>
  <li><a href="https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/pages/syllabus/">Quantum Mechanics</a></li>
  <li><a href="https://ocw.mit.edu/courses/18-435j-quantum-computation-fall-2003/pages/syllabus/">Quantum Information</a></li>
  <li><a href="https://ocw.mit.edu/courses/8-962-general-relativity-spring-2020/pages/syllabus/">General Relativity</a></li>
  <li><a href="https://ocw.mit.edu/courses/8-286-the-early-universe-fall-2013/pages/syllabus/">Cosmology</a></li>
  <li><a href="https://ocw.mit.edu/courses/8-311-electromagnetic-theory-spring-2004/pages/syllabus/">Electrodynamics</a></li>
  <li><a href="https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/pages/syllabus/">Fluid Mechanics</a></li>
  <li><a href="https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/syllabus/">Mathematical Methods for Physicists</a></li>
  <li><a href="https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2012/pages/syllabus/">Computational Physics</a></li>
  <li><a href="https://ocw.mit.edu/courses/6-036-introduction-to-machine-learning-fall-2020/pages/syllabus/">Machine Learning</a></li>
</ul>

Each subject above links to the <a href="https://ocw.mit.edu/" class="plain-link">MIT OpenCourseWare</a> syllabus for the nearest equivalent course, as a neutral reference for the level and scope I mean.

One thing the repository deliberately does not contain: lecture notes, slides, problem sheets or past papers produced by Imperial or anyone else. Those belong to their authors and are not mine to redistribute. Everything published there is my own handwriting and my own code.

## Tutoring

For tutoring specifically: private or in groups, online or in person in London. Undergraduate and Master's students who study physics and mathematics are the natural fit - quantum mechanics, quantum field theory, particle physics, general relativity, mathematical methods - along with scientific Python and machine learning for people coming to it from a physics background.

The foundational subjects I tutor:

<ul class="tn-topics">
  <li>GCSE Physics</li>
  <li>A-level Physics</li>
  <li>A-level Mathematics</li>
  <li><a href="https://ocw.mit.edu/courses/18-701-algebra-i-fall-2010/pages/syllabus/">Algebra</a></li>
  <li><a href="https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/pages/syllabus/">Geometry</a></li>
  <li><a href="https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/syllabus/">Calculus</a></li>
  <li><a href="https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/">Linear Algebra</a></li>
  <li><a href="https://ocw.mit.edu/courses/18-085-computational-science-and-engineering-i-fall-2008/pages/syllabus/">Engineering Mathematics</a></li>
  <li><a href="https://ocw.mit.edu/courses/8-223-classical-mechanics-ii-january-iap-2017/pages/syllabus/">Classical Mechanics</a></li>
  <li><a href="https://ocw.mit.edu/courses/8-20-introduction-to-special-relativity-january-iap-2021/pages/syllabus/">Special Relativity</a></li>
</ul>

GCSE and A-level have no MIT counterpart, so those are left unlinked. The material I teach follows the UK specifications and the Imperial modules above, not MIT's.

On format, level and everything else I am flexible. For opportunities, <a href="/contact/" class="plain-link">reach out</a>!

{% include linkedin_card.liquid %}

{% include goatcounter.liquid %}
