---
layout: page
title: AtriPINN
description: Physics-informed neural networks for real-time atrial fibrillation mapping from grid electrograms.
img: assets/img/projects/atripinn.jpg
importance: 1
category: machine learning
---

**[Imperial College London](https://www.imperial.ac.uk/) · 2025 – present · with [Prof David Colling](https://profiles.imperial.ac.uk/d.colling) and [Dr Nick Linton](https://profiles.imperial.ac.uk/nick.linton) · clinical data from [Hammersmith Hospital](https://www.imperial.nhs.uk/our-locations/hammersmith-hospital)**

Catheter ablation for atrial fibrillation depends on knowing where the arrhythmia originates, and knowing it fast enough to act during the procedure. Conventional mapping either interpolates naively across a sparse electrode grid or solves the underlying wave problem too slowly to be useful in theatre.

**Approach.** ATRIPINN, built in PyTorch, combines three things:

- **Local plane-fit conduction velocity** to get a fast first estimate of wavefront direction and speed;
- **Time-shifted kNN blending** to fuse neighbouring channels without smearing the wavefront;
- **Physics-informed neural network (PINN) residuals** enforcing wave, eikonal and monodomain (Aliev–Panfilov) dynamics as soft constraints, so the network cannot produce a physically impossible activation map.

The architecture is coordinate-agnostic with switchable physics back-ends, shipped through v1–v11.2 with CLI tooling.

**Results on sinus-rhythm data.**

| Metric | Value |
| :--- | :--- |
| RMS localisation error | ~1.6 mm |
| End-to-end latency | ~78 ms |
| Channel cross-correlation | ≥ 0.99 |

**Why it generalises.** The transferable result is not the error bar — it is that imposing the governing equation as a soft constraint buys data efficiency and physical plausibility at the same time. That is exactly the trade you want in detector reconstruction, where labelled events are expensive and unphysical predictions are worse than imprecise ones.

This work formed my MSc thesis, which was awarded the highest grade.
