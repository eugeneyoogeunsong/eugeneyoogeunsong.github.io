---
layout: page
title: Contact
permalink: /contact/
description: The best ways to reach me.
nav: true
nav_order: 8
---

## Email

**Personal** — [ygsong1004@gmail.com](mailto:ygsong1004@gmail.com) · the fastest route, and the one I check.

**Academic** — [yoogeun.song24@imperial.ac.uk](mailto:yoogeun.song24@imperial.ac.uk) · for anything Imperial or DUNE related.

## Elsewhere

- **LinkedIn** — [linkedin.com/in/yoogeunsong](https://www.linkedin.com/in/yoogeunsong) · where I am most active
- **X** — [@YoogeunSong](https://x.com/YoogeunSong)
- **Bluesky** — [@eugeneyoogeunsong.bsky.social](https://bsky.app/profile/eugeneyoogeunsong.bsky.social)
- **GitHub** — [eugeneyoogeunsong](https://github.com/eugeneyoogeunsong)

## Research profiles

- **ORCID** — [0000-0003-3206-1556](https://orcid.org/0000-0003-3206-1556)
- **Google Scholar** — [profile](https://scholar.google.com/citations?user=6pWw3eYAAAAJ)
- **InspireHEP** — [author page](https://inspirehep.net/authors/1790652)
- **ResearchGate** — [profile](https://www.researchgate.net/profile/Yoogeun-Song)

## Where I am

Blackett Laboratory, Department of Physics
Imperial College London
South Kensington Campus, London SW7 2AZ, United Kingdom

---

I am open to conversations about neutrino and BSM physics, machine learning for physics, quantitative research roles and collaborations, speaking, and mentoring. If you are a researcher, founder, investor or quant practitioner and there is an interesting problem involved — write to me.

---

## Latest from Bluesky

<style>
  .bsky-feed { margin: 1.5rem 0 0.5rem; }
  .bsky-post {
    border: 1px solid var(--global-divider-color);
    border-radius: 8px;
    padding: 1rem 1.15rem;
    margin-bottom: 0.9rem;
    background: var(--global-card-bg-color);
    transition: border-color 0.15s ease;
  }
  .bsky-post:hover { border-color: var(--global-theme-color); }
  .bsky-head {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    margin-bottom: 0.6rem;
    font-size: 0.8rem;
    color: var(--global-text-color-light);
  }
  .bsky-head img { width: 26px; height: 26px; border-radius: 50%; }
  .bsky-head b { color: var(--global-text-color); font-weight: 600; }
  .bsky-text {
    white-space: pre-wrap;
    line-height: 1.55;
    font-size: 0.95rem;
    margin: 0 0 0.6rem;
  }
  .bsky-text a { color: var(--global-theme-color); text-decoration: none; }
  .bsky-text a:hover { text-decoration: underline; }
  .bsky-media {
    display: block;
    margin: 0.6rem 0;
    border-radius: 6px;
    overflow: hidden;
    max-height: 260px;
  }
  .bsky-media img { width: 100%; object-fit: cover; display: block; }
  .bsky-meta {
    display: flex;
    gap: 1rem;
    font-size: 0.78rem;
    color: var(--global-text-color-light);
  }
  .bsky-meta a { color: inherit; text-decoration: none; }
  .bsky-meta a:hover { color: var(--global-theme-color); }
  .bsky-note { font-size: 0.88rem; color: var(--global-text-color-light); }
</style>

<div class="bsky-feed" id="bsky-feed">
  <p class="bsky-note">Loading recent posts…</p>
</div>

{% raw %}
<script>
  (function () {
    var HANDLE = "eugeneyoogeunsong.bsky.social";
    var LIMIT = 4;
    var mount = document.getElementById("bsky-feed");
    if (!mount) return;

    var API =
      "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed" +
      "?actor=" + encodeURIComponent(HANDLE) +
      "&limit=" + (LIMIT * 3) +
      "&filter=posts_no_replies";

    function esc(s) {
      return String(s).replace(/[&<>"']/g, function (c) {
        return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
      });
    }

    // Linkify bare URLs and @handle mentions after escaping.
    function rich(text) {
      var out = esc(text);
      out = out.replace(/(https?:\/\/[^\s<]+)/g, function (u) {
        return '<a href="' + u + '" target="_blank" rel="noopener">' + u + "</a>";
      });
      out = out.replace(/@([a-z0-9.-]+\.[a-z]{2,})/gi, function (m, h) {
        return '<a href="https://bsky.app/profile/' + h + '" target="_blank" rel="noopener">' + m + "</a>";
      });
      return out;
    }

    function when(iso) {
      var d = new Date(iso);
      return d.toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });
    }

    function postUrl(uri) {
      var rkey = uri.split("/").pop();
      return "https://bsky.app/profile/" + HANDLE + "/post/" + rkey;
    }

    fetch(API)
      .then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.json();
      })
      .then(function (data) {
        var items = (data.feed || [])
          .filter(function (i) { return i.post && i.post.record && !i.reason; })
          .slice(0, LIMIT);

        if (!items.length) throw new Error("empty");

        mount.innerHTML = items
          .map(function (i) {
            var p = i.post;
            var a = p.author || {};
            var img =
              p.embed && p.embed.images && p.embed.images[0]
                ? '<a class="bsky-media" href="' + postUrl(p.uri) + '" target="_blank" rel="noopener">' +
                  '<img src="' + p.embed.images[0].thumb + '" alt="' + esc(p.embed.images[0].alt || "") + '" loading="lazy"></a>'
                : "";
            return (
              '<div class="bsky-post">' +
              '<div class="bsky-head">' +
              (a.avatar ? '<img src="' + a.avatar + '" alt="">' : "") +
              "<b>" + esc(a.displayName || HANDLE) + "</b>" +
              "<span>@" + esc(a.handle || HANDLE) + "</span>" +
              "<span>·</span><span>" + when(p.record.createdAt) + "</span>" +
              "</div>" +
              '<p class="bsky-text">' + rich(p.record.text || "") + "</p>" +
              img +
              '<div class="bsky-meta">' +
              "<span>♥ " + (p.likeCount || 0) + "</span>" +
              "<span>↻ " + (p.repostCount || 0) + "</span>" +
              "<span>💬 " + (p.replyCount || 0) + "</span>" +
              '<a href="' + postUrl(p.uri) + '" target="_blank" rel="noopener">Open →</a>' +
              "</div></div>"
            );
          })
          .join("");

        mount.insertAdjacentHTML(
          "beforeend",
          '<p class="bsky-note"><a href="https://bsky.app/profile/' + HANDLE +
            '" target="_blank" rel="noopener">See everything on Bluesky →</a></p>'
        );
      })
      .catch(function () {
        mount.innerHTML =
          '<p class="bsky-note">Posts could not be loaded just now — ' +
          '<a href="https://bsky.app/profile/' + HANDLE + '" target="_blank" rel="noopener">read them on Bluesky</a>.</p>';
      });
  })();
</script>
{% endraw %}
