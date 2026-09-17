---
layout: page
title: Projects
permalink: /projects/
description: Research programmes and code across particle physics, astrophysics, machine learning, quantum computing, and markets.
nav: true
nav_order: 4
# Pinned to dark, like /pictures/, and not changeable on the page: the toggle is
# hidden below because it could not do anything here. Individual posts and
# project pages are NOT pinned - this applies to the index only.
force_theme: dark
display_categories: [Particle Physics, Machine Learning, Quantum Computing, Quant, Astrophysics]
horizontal: false
---

<style>
  /* This page is pinned to dark (force_theme in the front matter above), so the
     theme toggle cannot change anything here. Hidden rather than removed: it is
     hidden the same way on /pictures/, and theme.js attaches a click listener to
     the element on load, so deleting it would throw. */
  #light-toggle {
    display: none;
  }
</style>

<!-- pages/projects.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>

{% include affiliations.liquid %}

{% include linkedin_card.liquid %}

{% include goatcounter.liquid %}
