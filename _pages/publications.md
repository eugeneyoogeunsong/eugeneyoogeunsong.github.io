---
layout: page
permalink: /publications/
title: Publications
description: Peer-reviewed papers, preprints and work in progress, generated automatically from BibTeX.
nav: true
nav_order: 3
# Pinned to dark, like /pictures/, and not changeable on the page: the toggle is
# hidden below because it could not do anything here. Individual posts and
# project pages are NOT pinned - this applies to the index only.
force_theme: dark
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

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>

{% include author_self_link.liquid %}

{% include affiliations.liquid %}

{% include linkedin_card.liquid %}

{% include goatcounter.liquid %}
