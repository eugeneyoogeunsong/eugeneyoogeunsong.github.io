---
layout: about
title: About
permalink: /
subtitle: >
  PhD student in <a href='https://www.imperial.ac.uk/physics/'>Physics at Imperial College London</a> ·
  Neutrinos (<a href='https://www.dunescience.org/'>DUNE</a> · <a href='https://novaexperiment.fnal.gov/'>NOvA</a>) ·
  Machine Learning (ML) · Quantum Computing · Quantitative (Finance) Research

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p>Blackett Laboratory</p>
    <p>Imperial College London</p>
    <p>South Kensington, London SW7 2AZ</p>

selected_papers: true
social: true

announcements:
  enabled: true
  scrollable: true
  limit: 5

latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

<style>
  .profile figure { position: relative; margin: 0; }
  #headshot-slideshow {
    position: relative;
    width: 100%;
    aspect-ratio: 3 / 4;
    overflow: hidden;
    border-radius: 6px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.16), 0 2px 10px rgba(0, 0, 0, 0.12);
    background: var(--global-card-bg-color);
  }
  #headshot-slideshow img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: 50% 22%;
    opacity: 0;
    transition: opacity 1.1s ease-in-out;
  }
  #headshot-slideshow img.is-active { opacity: 1; }
  #headshot-dots {
    display: flex;
    justify-content: center;
    gap: 6px;
    margin-top: 10px;
  }
  #headshot-dots button {
    width: 7px; height: 7px;
    padding: 0; border: 0; border-radius: 50%;
    background: var(--global-divider-color);
    cursor: pointer;
    transition: background 0.3s ease;
  }
  #headshot-dots button.is-active { background: var(--global-theme-color); }
  @media (prefers-reduced-motion: reduce) {
    #headshot-slideshow img { transition: none; }
  }
</style>

<script>
  (function () {
    var mount = document.querySelector(".profile figure") || document.querySelector(".profile");
    if (!mount) return;

    var sources = ["01", "02", "03", "04", "05"].map(function (n) {
      return "{{ '/assets/img/profile/' | relative_url }}" + n + ".jpg";
    });

    var stage = document.createElement("div");
    stage.id = "headshot-slideshow";
    sources.forEach(function (src, i) {
      var img = document.createElement("img");
      img.src = src;
      img.alt = "Yoogeun Song";
      img.loading = i === 0 ? "eager" : "lazy";
      if (i === 0) img.className = "is-active";
      stage.appendChild(img);
    });

    var dots = document.createElement("div");
    dots.id = "headshot-dots";
    sources.forEach(function (_, i) {
      var b = document.createElement("button");
      b.type = "button";
      b.setAttribute("aria-label", "Show photo " + (i + 1));
      if (i === 0) b.className = "is-active";
      b.addEventListener("click", function () { show(i); });
      dots.appendChild(b);
    });

    mount.innerHTML = "";
    mount.appendChild(stage);
    mount.appendChild(dots);

    var slides = stage.querySelectorAll("img");
    var pips = dots.querySelectorAll("button");
    var current = 0;
    var timer = null;

    function show(i) {
      slides[current].classList.remove("is-active");
      pips[current].classList.remove("is-active");
      current = (i + slides.length) % slides.length;
      slides[current].classList.add("is-active");
      pips[current].classList.add("is-active");
      restart();
    }

    function restart() {
      if (timer) clearInterval(timer);
      timer = setInterval(function () { show(current + 1); }, 4500);
    }

    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) restart();
  })();
</script>

I am a high-energy physicist at **Imperial College London**, working on neutrino physics with the [Imperial High Energy Physics group](https://www.imperial.ac.uk/high-energy-physics/) on the [NOvA](https://novaexperiment.fnal.gov/) (NuMI Off-axis $$\nu_e$$ Appearance) and [DUNE](https://www.dunescience.org/) (Deep Underground Neutrino Experiment) collaborations, under [Dr Linda Cremonesi](https://profiles.imperial.ac.uk/l.cremonesi). On NOvA my role is a variety of physics analysis. My work sits at the point where physical modelling, machine learning and statistical inference stop being separate disciplines and start being one problem: **inference under uncertainty**.

That framing is also my history. I began university physics at **age seven**, finished a BSc at **age 11**, and published my first first-author paper in [*MNRAS Letters*](https://academic.oup.com/mnrasl) at **age 19**. Since then I have worked across general relativity and early-universe cosmology, black hole magnetospheres and Blandford–Znajek energy extraction, GRMHD modelling of Sgr A\*, physics-informed neural networks for clinical electrophysiology, and — now — neutrinos and beyond-Standard-Model physics. The range looks scattered from the outside. From the inside it is one method applied to different data.

Four things occupy me at the moment. **First**, systematics-aware ML reconstruction for the DUNE Near Detector — the ND is not merely a control detector; it is the constraint engine that makes precision oscillation measurements possible. **Second**, [AtriPINN](/projects/): physics-informed neural networks that map atrial fibrillation from grid electrograms in real time, at ~78 ms end-to-end latency and ~1.6 mm RMS localisation error. **Third**, a part-time quantum computing collaboration with [Singularity Quantum](https://singularityquantum.com/) — quantum-accelerated computational fluid dynamics for non-invasive cardiovascular diagnostics, where I work with their CFD engineers on augmenting and enhancing the CFD model, and on the hybrid layer around it: the physics-informed machinery that infers the boundary conditions, conditions what gets handed to the quantum kernel, and puts a calibrated uncertainty on the number a cardiologist actually acts on. **Fourth**, quantitative research — from October 2025 to August 2026 I ran an independent practice on alpha under non-stationary market dynamics, treated as a physics problem in signal and noise rather than a curve-fitting exercise. That work is now folded back into the same question the rest of my research asks.

I care about building things that are reproducible, scalable, and principled, and I would rather re-examine a premise than optimise inside someone else's. If you are working on hard problems in neutrinos, in machine learning for physics, in quantum computing, or in markets, I would like to hear from you.

---

## More about me

From being celebrated as a prodigy for my academic achievements in my teens to conducting cutting-edge research in Physics at [Imperial College London](https://www.imperial.ac.uk/), my journey presents a relentless drive to push the boundaries of science and technology.

Early recognition positioned me to inspire others. Today, as a Physics graduate researcher at Imperial, I am leveraging my multidisciplinary expertise in particle physics and machine learning to drive impactful global scientific advancements. In 2026 I work at the intersection of physics, ML and bioengineering; from October, for my PhD, I move to neutrino oscillations and interactions. For now I want to continue living in Europe and to make it home here.

Outside physics I have built end-to-end quant capability: time-series and stochastic control (HJB), with a focus on production constraints — Monte Carlo, high-performance optimisation, and robust monitoring. I build long-horizon, robust, durable systems: reproducible, scalable, and principled. My strength is first-principles mastery across physics, mathematics, and quantitative finance. I am also open to the possibility of leading global STEM innovation in industry, where science evolves into real-world applications.

**The early record.** In October 2005, at the age of 7, I set a national record by enrolling in the Physics BSc programme at [Inha University](https://eng.inha.ac.kr/eng/index.do), with coursework commencing in February 2006. Soon after, I transitioned to a Computer Science programme at the National Institute for Lifelong Education (NILE). In 2009, at the age of 11, I earned my Bachelor's through NILE's Academic Credit Bank System — a record that remains unmatched.

**Graduate work in Korea.** In 2009 I joined the integrative (Master's + PhD) programme at the Korea University of Science and Technology (UST). Whilst there I authored four papers in cosmology and high-energy astrophysics, two of them published in [*Monthly Notices of the Royal Astronomical Society*](https://academic.oup.com/mnras) and [*The Astrophysical Journal*](https://iopscience.iop.org/journal/0004-637X). I finished with All-But-Dissertation status and left UST in August 2018.

**Since then.** From December 2018 to August 2020 I completed my mandatory national service, which was essential for my personal growth. Since 2023 I have been living in the UK — 2023–2024 at [UCL](https://www.ucl.ac.uk/mssl/), and from 2024 studying and working as a graduate researcher in the Department of Physics at Imperial, ranked **#2 globally** in the [QS World University Rankings](https://www.topuniversities.com/universities/imperial-college-london) for three years in a row, from 2025 to 2027.

**Where to find me.** [LinkedIn](https://www.linkedin.com/in/yoogeunsong) is where I am most active, with [Bluesky](https://bsky.app/profile/eugeneyoogeunsong.bsky.social) next.

{% include author_self_link.liquid %}
