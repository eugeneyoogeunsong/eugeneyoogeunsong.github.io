---
layout: cv
permalink: /cv/
title: CV
nav: true
nav_order: 5
cv_pdf: /assets/pdf/Yoogeun_Song_CV.pdf # the authored Overleaf CV — replace this file to update the download
cv_format: rendercv # options: rendercv, jsonresume
description: Education, research experience, awards and skills. A PDF version is available above.
toc:
  sidebar: left
---

{% include cv_contact_extra.liquid %}

{% include affiliations.liquid %}

{%- comment -%}
No append_to here any more. That argument dated from when the gem's cv
layout discarded {{ content }} entirely and the badge had to be JS-moved
into the page. \_layouts/cv.liquid now renders content, so both blocks sit
in normal flow and keep their source order: logos, then the card. Leaving
append_to in would append the card to .post and put it ABOVE the logos.
{%- endcomment -%}
{% include linkedin_card.liquid %}

{% include goatcounter.liquid %}
