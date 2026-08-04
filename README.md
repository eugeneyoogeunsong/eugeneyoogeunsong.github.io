# yoogeunsong.com

Personal research site for **Yoogeun (Eugene) Song** — physicist, ML, quant.
Built on [al-folio](https://github.com/alshedivat/al-folio) (v1.x), served by GitHub Pages
from `eugeneyoogeunsong.github.io` at the custom domain **yoogeunsong.com**.

---

## First-time setup

### 1. Push to GitHub

```bash
cd eugeneyoogeunsong.github.io
git init -b main
git add -A
git commit -m "Initial site"
git remote add origin https://github.com/eugeneyoogeunsong/eugeneyoogeunsong.github.io.git
git push -u origin main
```

### 2. Turn on Pages

Repo → **Settings → Pages** → Source: **Deploy from a branch** → Branch: **`gh-pages`** / root.

The `gh-pages` branch is created for you the first time `.github/workflows/deploy.yml`
runs. Give the first run a couple of minutes.

Also: **Settings → Actions → General → Workflow permissions → Read and write permissions.**
Without this the deploy action cannot push to `gh-pages`.

### 3. Point the domain

At your registrar for `yoogeunsong.com`:

| Type  | Host | Value |
| :---- | :--- | :---- |
| A     | @    | 185.199.108.153 |
| A     | @    | 185.199.109.153 |
| A     | @    | 185.199.110.153 |
| A     | @    | 185.199.111.153 |
| CNAME | www  | eugeneyoogeunsong.github.io |

Optional IPv6 (AAAA on `@`): `2606:50c0:8000::153`, `...8001::153`, `...8002::153`, `...8003::153`.

The `CNAME` file in this repo already contains `yoogeunsong.com`. Once DNS propagates,
tick **Enforce HTTPS** in Settings → Pages.

---

## Where everything lives

| What | File |
| :--- | :--- |
| Site settings, nav, SEO | `_config.yml` |
| Home / bio | `_pages/about.md` |
| Research narrative | `_pages/research.md` |
| Publications (auto-rendered) | `_bibliography/papers.bib` |
| Project cards | `_projects/*.md` |
| CV content | `_data/cv.yml` |
| Social + scholarly links | `_data/socials.yml` |
| Coauthor homepage links | `_data/coauthors.yml` |
| "News" items on the home page | `_news/*.md` |
| Blog posts | `_posts/*.md` |
| Theme colours | `_sass/_themes.scss` |

## Things to do next

- [ ] **Replace `assets/img/prof_pic.jpg`** with a real headshot (square, ≥800×800).
- [ ] Replace the six placeholder cards in `assets/img/projects/` with real figures —
      a DUNE event display, an AtriPINN activation map, a GRMHD snapshot.
- [ ] Verify `arxiv_id: song_y_1` in `_data/socials.yml` resolves at
      <https://arxiv.org/a/song_y_1> — delete the line if it 404s.
- [ ] Turn the blog on when you want it: `nav: false` → `nav: true` in `_pages/blog.md`.
- [ ] Optional: add a Google Analytics ID under `analytics.google` in `_config.yml`,
      and verify the domain in Google Search Console via `google_site_verification`.

## Automation already wired up

- **`deploy.yml`** — builds and publishes on every push to `main`.
- **`render-cv.yml`** — regenerates the CV PDF from `_data/cv.yml` whenever you edit it,
  and commits it to `assets/rendercv/rendercv_output/Yoogeun_Song_CV.pdf`.
- **`update-citations.yml`** — refreshes Google Scholar citation counts three times a week.
- **`upgrade-check.yml`** — flags new al-folio releases.
- **`broken-links.yml`** — link rot check.

## Running it locally (optional)

Requires Ruby 3.3+ and Node 20+.

```bash
bundle install
npm ci
bundle exec jekyll serve --livereload
```

Or skip it entirely — GitHub Actions builds the site on every push.
