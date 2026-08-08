---
layout: page
title: AtriPINN
description: Physics-informed neural networks for real-time atrial fibrillation mapping from grid electrograms.
img: assets/img/projects/atripinn.jpg
importance: 1
category: Machine Learning
---

**[Imperial College London](https://www.imperial.ac.uk/) · 2025 – present · with [Prof David Colling](https://profiles.imperial.ac.uk/d.colling) and [Dr Nick Linton](https://profiles.imperial.ac.uk/nick.linton) · clinical data from [Hammersmith Hospital](https://www.imperial.nhs.uk/our-locations/hammersmith-hospital)**

Catheter ablation for atrial fibrillation depends on knowing where the arrhythmia originates, and knowing it fast enough to act during the procedure. Conventional mapping either interpolates naively across a sparse electrode grid or solves the underlying wave problem too slowly to be useful in theatre.

**Approach.** ATRIPINN, built in PyTorch, combines three things:

- **Local plane-fit conduction velocity** to get a fast first estimate of wavefront direction and speed;
- **Time-shifted kNN blending** to fuse neighbouring channels without smearing the wavefront;
- **Physics-informed neural network (PINN) residuals** enforcing wave, eikonal and monodomain (Aliev–Panfilov) dynamics as soft constraints, so the network cannot produce a physically impossible activation map.

The architecture is coordinate-agnostic with switchable physics back-ends, shipped through v1–v11.2 with CLI tooling.

<figure style="margin: 1.75rem 0; text-align: center;">
  <video controls preload="none" playsinline
         poster="{{ '/assets/img/projects/atripinn-video-poster.jpg' | relative_url }}"
         style="width:100%; max-width:760px; border-radius:6px;">
    <source src="{{ '/assets/video/atripinn-nsr-wave.mp4' | relative_url }}" type="video/mp4">
    Your browser does not support embedded video —
    <a href="{{ '/assets/video/atripinn-nsr-wave.mp4' | relative_url }}">download the clip</a> instead.
  </video>
  <figcaption style="font-size:0.8rem; color:var(--global-text-color-light); margin-top:0.5rem;">
    Reconstructed activation wavefront propagating across the 4×4 grid in normal sinus rhythm.
    Click to play.
  </figcaption>
</figure>

<figure style="margin: 1.75rem 0; text-align: center;">
  <img src="{{ '/assets/img/projects/atripinn-timeshift.png' | relative_url }}"
       alt="Three panels comparing measured electrograms at E_11, E_12 and E_33 against the estimate for E_22, each offset by the travel time implied by the local conduction velocity"
       style="max-width:100%; height:auto; border-radius:6px;" loading="lazy">
  <figcaption style="font-size:0.8rem; color:var(--global-text-color-light); margin-top:0.5rem;">
    Time-shifted blending in practice: neighbouring electrodes are offset by the travel time implied
    by the local velocity field before they are combined. Shifts of ±31–83 ms recover the waveform at
    a withheld electrode.
  </figcaption>
</figure>

**Results on sinus-rhythm data.**

| Metric | Value |
| :--- | :--- |
| RMS localisation error | ~1.6 mm |
| End-to-end latency | ~78 ms |
| Channel cross-correlation | ≥ 0.99 |

**Why it generalises.** The transferable result is not the error bar — it is that imposing the governing equation as a soft constraint buys data efficiency and physical plausibility at the same time. That is exactly the trade you want in detector reconstruction, where labelled events are expensive and unphysical predictions are worse than imprecise ones.

This work formed my MSc thesis, which was awarded the highest grade.
