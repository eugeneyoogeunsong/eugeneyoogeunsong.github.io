---
layout: page
permalink: /publications/
title: Publications
description: Peer-reviewed papers, preprints and work in progress, generated automatically from BibTeX.
nav: true
nav_order: 3
# Pinned to dark, like /pictures/. Releasable: a deliberate change on the page
# (the toggle, or the Cmd/Ctrl-K palette) takes over. Individual posts and
# project pages are NOT pinned - this applies to the index only.
force_theme: dark
---

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
