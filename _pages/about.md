---
layout: about
title: About
permalink: /
subtitle: >
  PhD Researcher in <a href='https://www.imperial.ac.uk/physics/'>Physics at Imperial College London</a> ·
  Neutrinos (<a href='https://www.dunescience.org/'>DUNE</a> · <a href='https://novaexperiment.fnal.gov/'>NOvA</a>) ·
  Machine Learning (ML) · Quantum Computing · Quantitative (Finance) Research · Computational Fluid Dynamics (CFD)

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p>Imperial College London,</p>
    <p>South Kensington, London SW7 2AZ, United Kingdom</p>

selected_papers: true
social: true

announcements:
  enabled: true
  scrollable: true
  limit: 6

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
  a#headshot-slideshow { display: block; cursor: pointer; }
  a#headshot-slideshow::after {
    content: "See more →";
    position: absolute;
    left: 0; right: 0; bottom: 0;
    padding: 0.5rem 0.7rem;
    font-size: 0.75rem;
    color: #fff;
    background: linear-gradient(transparent, rgba(0, 0, 0, 0.65));
    opacity: 0;
    transition: opacity 0.2s ease;
    z-index: 2;
  }
  a#headshot-slideshow:hover::after { opacity: 1; }
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

    var stage = document.createElement("a");
    stage.id = "headshot-slideshow";
    stage.href = "{{ '/pictures/' | relative_url }}";
    stage.title = "See more photos";
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

    restart(); // the CSS already drops the fade under prefers-reduced-motion
  })();
</script>

I am a high-energy physicist at **[Imperial College London](https://www.imperial.ac.uk/)**, working on neutrino physics with the [Imperial High Energy Physics group](https://www.imperial.ac.uk/high-energy-physics/) on the [DUNE](https://www.dunescience.org/) (Deep Underground Neutrino Experiment) and [NOvA](https://novaexperiment.fnal.gov/) (NuMI Off-axis $$\nu_e$$ Appearance) collaborations, under [Dr Linda Cremonesi](https://profiles.imperial.ac.uk/l.cremonesi). Both are [Fermilab](https://www.fnal.gov/)'s flagship American neutrino experiments; Fermilab is the United States' national laboratory for particle physics, supported principally by the [Department of Energy](https://www.energy.gov/science/office-science). On NOvA my role is a variety of physics analysis. My work sits at the point where physical modelling, machine learning and statistical inference stop being separate disciplines and start being one problem: **inference under uncertainty**.

That framing is also my history. I began [university physics](/cv/) at **age 7**, finished a [Bachelor's degree](https://yoogeunsong.com/cv/#awards) at **age 11**, and published my first first-author paper in [_MNRAS Letters_](https://academic.oup.com/mnrasl) at **age 19**. Since then I have worked across general relativity and early-universe cosmology, <a href="/projects/9_gamma/" class="plain-link">black hole magnetospheres</a> and <a href="/projects/7_kerr/" class="plain-link">Blandford–Znajek energy extraction</a>, <a href="/projects/6_sgra/" class="plain-link">general-relativistic magnetohydrodynamic (GRMHD) modelling of Sgr A\*</a>, <a href="/projects/3_atripinn/" class="plain-link">physics-informed neural networks for clinical electrophysiology</a>, and, at present, <a href="/projects/1_dune/" class="plain-link">neutrinos</a> and <a href="/projects/8_higgs/" class="plain-link">beyond-Standard-Model physics (or "new" physics)</a>. The range looks scattered from the outside. From the inside it is one method applied to different data.

From early 2023 to mid 2024, I was a visiting researcher at [UCL's Mullard Space Science Laboratory](https://www.ucl.ac.uk/mssl/), working on <a href="/projects/6_sgra/" class="plain-link">general-relativistic magnetohydrodynamic (GRMHD) modelling of Sgr A\*</a>.

From 2024 to 2025, at [Imperial](https://www.imperial.ac.uk/), I did projects on the <a href="/projects/8_higgs/" class="plain-link">Higgs boson as a portal to dark matter</a> and [AtriPINN](/projects/3_atripinn/). Alongside both I have been a member of Imperial's [Algorithmic Trading](https://algosoc.com/) and [Investment](https://investmentsoc.com/) societies, which is where the <a href="/projects/4_quant/" class="plain-link">independent quant practice</a> came from. [Imperial College London](https://www.imperial.ac.uk/) is ranked [**#2 globally**](https://www.imperial.ac.uk/about/introducing-imperial/league-tables/) in the [QS World University Rankings](https://www.topuniversities.com/universities/imperial-college-london) for three years in a row, from 2024-25 to 2026-27.

In 2026, four things occupy me. **First**, the <a href="/projects/" class="plain-link">neutrino physics</a>: a variety of physics analyses on [NOvA](https://yoogeunsong.com/projects/2_nova/), and systematics-aware machine learning (ML) reconstruction for the [DUNE](https://yoogeunsong.com/projects/1_dune/) <a href="https://atwork.dunescience.org/near-detector/" class="plain-link">Near Detector</a> (ND): the ND is not merely a control detector; it is the constraint engine that makes precision oscillation measurements possible. **Second**, [AtriPINN](/projects/3_atripinn/): physics-informed neural networks that map atrial fibrillation from grid electrograms in real time, at ~78 ms end-to-end latency and ~1.6 mm RMS localisation error. **Third**, a part-time <a href="/projects/5_singularity/" class="plain-link">quantum computing collaboration</a> with <a href="https://singularityquantum.com/" class="plain-link">Singularity Quantum</a>: quantum-accelerated computational fluid dynamics (CFD) for non-invasive cardiovascular diagnostics, where I work with their CFD engineers on augmenting and enhancing the CFD model, and on the hybrid layer around it: the physics-informed machinery that infers the boundary conditions and prepares what gets handed to the quantum kernel. **Fourth**, [quantitative research](/projects/4_quant/). From October 2025 to August 2026 I ran an independent practice on alpha under non-stationary market dynamics, treated as a physics problem in signal and noise rather than a curve-fitting exercise. That work is now folded back into the same question the rest of my research asks.

I have been based in the **London** area in the UK since **2023**, and before that I spent time in Spain and the Netherlands for various collaborations. For now I want to continue living in Europe and to make it home here.
I care about building things that are reproducible, scalable, and principled, and I would rather re-examine a premise than optimise inside someone else's.
I always _trust the process_, and that habit carries directly into my research and all the other aspects of my life. If you are working on hard problems in neutrinos, in machine learning for physics, in quantum computing, or in markets, I would like to hear from you. Feel free to [reach out](/contact/)!

**Where to find me.** For the most up-to-date: **[LinkedIn](https://www.linkedin.com/in/yoogeunsong)** is where I am most active - **8,000+ followers** - with **[Bluesky](https://bsky.app/profile/eugeneyoogeunsong.bsky.social)** next. Location-wise, I am physically in **London, UK** most of the year, or occasionally in **LA, California** or **Chicago, Illinois**; [get in touch](/contact/) when you are in town!

---

## More about me

My name in Korean is **송유근**, and my pronouns are **he/him/his** (cisgender male; straight). I was born in **Seoul, Korea**, on **27 November 1997**. I hold citizenship of the <a href="https://www.henleyglobal.com/passport-index/ranking" class="plain-link">**Republic of Korea**</a>, and only that one, at least for now - this may change.

From being celebrated in Korea as a prodigy for my [academic achievements](/media/) in my teens, to conducting cutting-edge research in Physics at [Imperial College London](https://www.imperial.ac.uk/), my journey presents a relentless drive to push the boundaries of science and technology, and to make an impact.

Early recognition positioned me to inspire others, and to highlight the importance of science education, or rather the absence of a complete system able to support the _hyper-gifted_ children it identifies. Today, as a Physics graduate researcher at [Imperial](https://www.imperial.ac.uk/), I am leveraging my multidisciplinary expertise in particle physics and machine learning to drive impactful global scientific advancements. In 2026 I work at the intersection of physics, ML and bioengineering. Also, for my PhD, I started working on <a href="/projects/1_dune/" class="plain-link">neutrino oscillations and interactions</a> this year.

Outside physics I have built end-to-end <a href="/projects/4_quant/" class="plain-link">quantitative research</a> capability across futures, derivatives and equities: stochastic calculus and stochastic differential equation (SDE) modelling, alpha generation under non-stationary regimes, regime-shift detection that does not simply overfit the last regime, physics-inspired signal-and-noise separation, Bayesian inference and Monte Carlo for path-dependent problems, and the market-microstructure constraints (impact, inventory, liquidity, latency) that decide whether a signal survives contact with a book.

As you can see, I build long-horizon, robust, durable systems: reproducible, scalable, and principled. My strength is **first-principles mastery** across the _**physics**_ (elementary particle physics, quantum field theory, general relativity, astrophysics, fluid dynamics, quantum information), the _**mathematics**_ underneath it (differential geometry, topology, stochastic calculus), and the _**computational & applied**_ side (deep learning, statistical modelling, alpha research, algorithmic trading).

I have been based in Europe (now in London, UK) since 2023, and I plan to continue living here for a while. As of 2026, my current focus in on the academic research side, but I am also considering, and very open to the possibility of leading global STEM innovation in industry, where science evolves into real-world applications.

In 2026 I am working part-time with [Singularity Quantum](https://singularityquantum.com/) on CFD applications, and over the last few years I have met and talked with a great many founders and CEOs across robotics, machine learning, quantum computing, advanced biotechnology & neurotech, AI applications and quantitative finance: in London, in Paris, and in Seoul at [ICML 2026](https://icml.cc/). I also spend a good deal of time talking to, and befriended people from [Imperial Business School](https://www.imperial.ac.uk/business-school/) and [Dyson School of Design Engineering](https://www.imperial.ac.uk/design-engineering/) too. For instance, in the summer of 2025, I participated in a discussion with [Lucy Jung](https://www.linkedin.com/in/lucyjung/) (Imperial alum, founder at LYEONS) as part of the Imperial [Neurotech](https://iclneurotech.co.uk/) society event; we also talked about possible future collaborations.

In fact most of my friends and connections in the UK are from Imperial society activities, business-related people, sports buddies, and language exchange buddies. My connections come from every sort of background, nationality, ethnicity and culture, which is a large part of why I love London so much, and all of them are welcome. I'm always open to collaborations with brilliant, like-minded people!

<p style="margin-top: 3.25rem;"><strong>What follows is how I got here, chapter by chapter.</strong></p>

**The early record: 2004–2009.** In October 2005, at the age of 7, I set a [national record](/media/) in South Korea by enrolling in the [Physics BSc programme](/cv/) at [Inha University](https://eng.inha.ac.kr/eng/index.do), with coursework commencing in February 2006. Soon after, I transitioned to a Computer Science programme at the National Institute for Lifelong Education ([NILE](https://www.nile.or.kr/index.do?lang=en)). In 2009, at the age of 11, I earned my [Bachelor's](/cv/) through NILE's [Academic Credit Bank System](https://www.nile.or.kr/usr/wap/detail.do?app=13309&seq=623&lang=en), a record that remains unmatched. For the full record, see my [CV](/cv/).

**Graduate work in Korea: 2009–2018.** In 2009, I joined the [integrative (Master's + PhD) programme](/cv/) at the Korea University of Science and Technology ([UST](https://ust.ac.kr/eng/)) and the Korea Astronomy and Space Science Institute ([KASI](https://www.kasi.re.kr/eng/index)). Whilst there I authored four papers in cosmology and <a href="/projects/9_gamma/" class="plain-link">high-energy astrophysics</a>, two of them published in [_Monthly Notices of the Royal Astronomical Society_](https://academic.oup.com/mnras) and [_The Astrophysical Journal_](https://iopscience.iop.org/journal/0004-637X). I <a href="/cv/#education" class="plain-link"><strong>completed the PhD coursework</strong></a> there, finished with All-But-Dissertation status, and left UST in August 2018.
During 2017–2018 I was invited by [Dr Kouichi Hirotani](https://www.asiaa.sinica.edu.tw/people/cv.php?i=hirotani) as a visiting PhD student at the [Academia Sinica Institute of Astronomy and Astrophysics](https://www.asiaa.sinica.edu.tw/) in Taiwan, where I published two papers with him and [Dr Satoki Matsushita](https://www.asiaa.sinica.edu.tw/people/cv.php?i=satoki): <a href="/projects/9_gamma/" class="plain-link">Song et al. (2017)</a> and <a href="/projects/9_gamma/" class="plain-link">Hirotani et al. (2018)</a>.
In 2018, for 4 months, I was invited by [Dr Isao Okamoto](https://www.researchgate.net/profile/Isao-Okamoto) as a visiting researcher at the [National Astronomical Observatory of Japan](https://www.nao.ac.jp/en/) to work on the <a href="/projects/7_kerr/" class="plain-link">modified Blandford–Znajek mechanism</a> ([arXiv:1904.11978](https://arxiv.org/abs/1904.11978)), and I carried on collaborating with him until the end of 2022, before I moved to Europe. From that period there is also an [SBS Special](/media/) documentary about my journey.

**National service: 2018–2020.** From December 2018 to August 2020 I completed my mandatory [national service](/cv/#experience) in the Republic of Korea Army, as a driver and driving instructor with the 7th Engineer Brigade, VII Corps. I finished as a Sergeant. Being away from research and academic side, it mattered more than the dates suggest. Being responsible for other people's safety in an environment where everything is checked, and checked time and time again, is where I learned _responsibility_ and _reliability_ as habits rather than intentions, and ultimately it is where the _discipline_ behind everything since came from. Whilst there, I was good in every key area: that's why I was awarded the _“Special Grade Warrior”_ (특급전사) distinction by the brigade in 2020 for my outstanding performance across all key military competencies, including marksmanship, regular brigade training, tactical expertise, and weapon proficiency. My specialty in the army was driving various vehicles, maintaining and repairing them, and teaching driving to juniors. I was honored with the brigade’s _"Exemplary Army Driver"_ (모범 운전병) distinction in 2020 in recognition of my outstanding performance in driving and teaching, and commitment to safety. I also represented my company in the brigade-level bodyweight fitness competition in 2020 - this is another thing started here - I was obssessed with physical fitness training: mid-distance running, calisthenics, weight-lifting and so on, which later became my strong [passion](https://yoogeunsong.com/interests/). My honorable discharge was in August 2020 -- 6 years ago (time really flies)! I was a civilian again then.

**Independent research, and building a global network: 2020–2022.** The worldwide pandemic happened earlier that year. After my honorable discharge in August 2020, through the pandemic, as a civilian I kept my research going remotely, working with Dr Isao Okamoto, in collaboration with the National Astronomical Observatory of Japan on <a href="/projects/7_kerr/" class="plain-link">modified Blandford–Znajek energy extraction</a> from Kerr black holes. I also spent this pandemic period reaching out to researchers across the US, the UK and Europe - at [Montana State](https://www.montana.edu/), [Purdue](https://www.purdue.edu/), [Columbia](https://www.columbia.edu/), the [Observatoire de Paris](https://www.obspm.fr/), [UCL](https://www.ucl.ac.uk/) and elsewhere - which is how much of my later [network](https://www.linkedin.com/in/yoogeunsong) began. Two other things started in this period and changed my direction: Being an avid language learner I went deep into European languages, adding Spanish and Italian to French and German, and decided that Europe was where I wanted to be; and I also began seriously exploring quantitative finance. For a few years back then I had been contemplating moving to the _USA_ or _Europe_, initially for my career in academia or possibly industry. Voilà, Europe it is. And I never looked back ever since.

**Moving to Europe, and working at UCL: 2022–2024.** In 2022, I visited Europe - Spain, the Netherlands, and eventually the UK - collaborating with European researchers and attending in-person European conferences including the European Astronomical Society (EAS) and the Heidelberg International Symposium. I discussed with various researchers during this period in Europe, including [Ciska Kemper](https://www.icrea.cat/community/icreas/16694/francisca-kemper/), [Frank M. Rieger](https://www.mpi-hd.mpg.de/~frieger), [Oliver Porth](https://www.uva.nl/en/profile/p/o/o.j.g.porth/o.j.g.porth.html), [Benoît Cerutti](https://www.cnrs.fr/fr/personne/benoit-cerutti), [Ziri Younsi](https://profiles.ucl.ac.uk/26858-ziri-younsi), and others. From 2023 I moved to the UK, and I was a visiting researcher at [UCL's Mullard Space Science Laboratory](https://www.ucl.ac.uk/mssl/), working with [Dr Ziri Younsi](https://profiles.ucl.ac.uk/26858-ziri-younsi) and [Prof Kinwah Wu](https://profiles.ucl.ac.uk/10719-kinwah-wu) on the <a href="/projects/6_sgra/" class="plain-link"><em>multi-wavelength variability of Sagittarius A\*</em></a>, coupling GRMHD simulations to general-relativistic radiative transfer. That is where large-scale computational physics stopped being something I read about and became a part of my arsenal.

**Imperial: 2024–present.** In 2024, I moved to [Imperial College London](https://www.imperial.ac.uk/physics/) for a Masters in Physics. The taught side ran through Advanced Quantum Field Theory ([AQFT](https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/advanced-quantum-field-theory)), Advanced Particle Physics ([APP](https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/advanced-particle-physics)), Quantum Field Theory, General Relativity, Advanced Classical Physics, Mathematical Methods for Physicists, and Research Computing Skills for Physicists (Mathematica and MATLAB). Alongside those I completed a self-study project on <a href="/projects/8_higgs/" class="plain-link">the Higgs boson as a portal to dark matter</a> with [Prof. Alexander Tapper](https://profiles.imperial.ac.uk/a.tapper) of the Imperial HEP group, graded A. I also built an interactive Mathematica simulator, <a href="https://github.com/eugeneyoogeunsong/imperial-physics-notes/tree/main/research-computing-skills" class="plain-link"><em>Quantum Waves in Motion: numerical modelling of the time-dependent Schrödinger equation</em></a>, with wave-packet visualisations and tunnelling, also graded A, assessed by [Dr Jaroslaw Pasternak](https://profiles.imperial.ac.uk/j.pasternak). My thesis, <a href="/projects/3_atripinn/" class="plain-link"><em>Physics-Informed Machine Learning for Real-Time Afib Mapping on Grid Electrograms</em></a>, was supervised by [Prof David Colling](https://profiles.imperial.ac.uk/d.colling) of the HEP group and [Dr Nick Linton](https://profiles.imperial.ac.uk/nick.linton) of Bioengineering, and was awarded the highest grade; I stayed on as a research assistant on that project for a further year. Since then the work has widened: [AtriPINN](/projects/3_atripinn/) with Hammersmith Hospital, and an independent quantitative research practice through 2025–26. In 2026, I also started my PhD - technically my second one - in neutrino physics with [DUNE](https://yoogeunsong.com/projects/1_dune) and [NOvA](https://yoogeunsong.com/projects/2_nova) under [Dr Linda Cremonesi](https://profiles.imperial.ac.uk/l.cremonesi). I have also recently started working part-time with [Singularity Quantum](https://www.linkedin.com/company/singularity-quantum) on [quantum-enhanced CFD](/projects/5_singularity/) projects. Imperial has held [**#2 globally**](https://www.imperial.ac.uk/about/introducing-imperial/league-tables/) in the QS rankings for three years running.

For the full record, see my [CV](/cv/).

Follow me on [LinkedIn](https://www.linkedin.com/in/yoogeunsong) for the most recent updates on my journey!
My connections, built over the past five years, come from every sort of background, nationality and culture, which is a large part of why I like Europe and London, and you are welcome to join them!

{% include author_self_link.liquid %}

{% include goatcounter.liquid %}

{% include news_heading_link.liquid %}

{% include linkedin_badge.liquid before_heading="selected publications" %}
