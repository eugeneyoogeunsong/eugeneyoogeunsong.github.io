---
layout: page
title: News
permalink: /news/
description: Every news item on this site, newest first.
nav: false
---

**Follow me on [LinkedIn](https://www.linkedin.com/in/yoogeunsong) or [Bluesky](https://bsky.app/profile/eugeneyoogeunsong.bsky.social).** I strongly encourage it: the most up-to-date information is on my LinkedIn, and this page only holds the most recent events. A great many other interesting news and events are not here at all; they are all on my [LinkedIn](https://www.linkedin.com/in/yoogeunsong) page, so follow me there!

Below is everything on this site, from the very beginning to the most recent. Like the rest of this website, it is written in English throughout, deliberately: I am aiming for a global audience, principally in Europe and the USA.

{% include affiliations.liquid %}

<style>
  .news-all { margin: 1.5rem 0 2rem; padding: 0; list-style: none; }
  .news-all li {
    display: grid;
    grid-template-columns: 7.5rem 1fr;
    gap: 0.25rem 1rem;
    padding: 0.85rem 0;
    border-bottom: 1px solid var(--global-divider-color);
  }
  .news-all li:last-child { border-bottom: 0; }
  .news-all .news-date {
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--global-text-color-light);
    white-space: nowrap;
  }
  .news-all .news-body p { margin: 0; }
  .news-all .news-body p + p { margin-top: 0.5rem; }
  @media (max-width: 576px) {
    .news-all li { grid-template-columns: 1fr; gap: 0.2rem; }
  }
</style>

<ul class="news-all">
{%- assign items = site.news | sort: "date" | reverse -%}
{%- for item in items %}
  <li>
    <span class="news-date">{{ item.date | date: "%b %d, %Y" }}</span>
    <div class="news-body">{{ item.content }}</div>
  </li>
{%- endfor %}
</ul>

{% include linkedin_card.liquid %}
