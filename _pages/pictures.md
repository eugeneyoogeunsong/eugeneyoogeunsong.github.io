---
layout: page
title: Pictures
permalink: /pictures/
description: Headshots, at full resolution. Free to use for talks, panels, articles and profiles.
nav: false
---

<style>
  .gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.1rem;
    margin: 1.75rem 0 1rem;
  }
  .gallery a {
    display: block;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--global-divider-color);
    background: var(--global-card-bg-color);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
  }
  .gallery a:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.16);
  }
  .gallery img {
    display: block;
    width: 100%;
    height: auto;
  }
  .gallery figcaption {
    font-size: 0.75rem;
    color: var(--global-text-color-light);
    padding: 0.5rem 0.7rem 0.6rem;
  }
  .gallery figure { margin: 0; }
</style>

Click any photo to open it at full resolution. You are welcome to use these for conference
programmes, seminar announcements, panel listings or press — no need to ask, though I would
always like to know where it ends up.

<div class="gallery">
  <a href="{{ '/assets/img/profile/full/01.jpg' | relative_url }}" target="_blank" rel="noopener">
    <figure>
      <img src="{{ '/assets/img/profile/01.jpg' | relative_url }}" alt="Yoogeun Song, denim shirt" loading="lazy">
      <figcaption>1024 × 1535 · JPG</figcaption>
    </figure>
  </a>
  <a href="{{ '/assets/img/profile/full/02.jpg' | relative_url }}" target="_blank" rel="noopener">
    <figure>
      <img src="{{ '/assets/img/profile/02.jpg' | relative_url }}" alt="Yoogeun Song, striped cardigan" loading="lazy">
      <figcaption>1024 × 1535 · JPG</figcaption>
    </figure>
  </a>
  <a href="{{ '/assets/img/profile/full/03.jpg' | relative_url }}" target="_blank" rel="noopener">
    <figure>
      <img src="{{ '/assets/img/profile/03.jpg' | relative_url }}" alt="Yoogeun Song, maroon turtleneck" loading="lazy">
      <figcaption>1024 × 683 · JPG</figcaption>
    </figure>
  </a>
  <a href="{{ '/assets/img/profile/full/04.jpg' | relative_url }}" target="_blank" rel="noopener">
    <figure>
      <img src="{{ '/assets/img/profile/04.jpg' | relative_url }}" alt="Yoogeun Song, three-piece suit" loading="lazy">
      <figcaption>1024 × 1535 · JPG</figcaption>
    </figure>
  </a>
  <a href="{{ '/assets/img/profile/full/05.jpg' | relative_url }}" target="_blank" rel="noopener">
    <figure>
      <img src="{{ '/assets/img/profile/05.jpg' | relative_url }}" alt="Yoogeun Song, black suit" loading="lazy">
      <figcaption>1024 × 683 · JPG</figcaption>
    </figure>
  </a>
</div>

Back to [About](/).

{% include goatcounter.liquid %}
