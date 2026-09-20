#!/usr/bin/env python3
"""Turn one al-folio project/page Markdown file into a standalone reading PDF.

Why this exists: the site pages are Jekyll + Liquid + MathJax, which is fine in a
browser and useless offline. This strips the site machinery, hands the physics to
real LaTeX (so the equations are typeset rather than rasterised), and compiles
with XeLaTeX.

What it has to fix on the way:

1. YAML front matter - not pandoc metadata, so it is parsed out and used to build
   a title block instead.
2. Liquid tags - {% include ... %} dropped; {{ '/assets/x' | relative_url }}
   resolved to the file on disk so graphicx can find it.
3. Raw <figure> blocks - pandoc drops raw HTML when targeting LaTeX, so each one
   is rewritten as a Markdown image with its <figcaption> as the caption.
4. Theme-swapped images - the page ships .only-light and .only-dark variants of
   the same plot. Print keeps the light one and discards the dark block entirely.
5. INLINE math written as $$...$$ - this is the one that silently ruins the
   document. Kramdown treats $$...$$ as inline when it sits inside a sentence,
   but pandoc always reads it as display math, so every "$$\\nu_e$$" would break
   its paragraph onto its own centred line. Any $$...$$ that is not alone on its
   line is demoted to $...$.

Usage:  python3 assets/scripts/page_to_pdf.py _projects/2_nova.md [output.pdf]
"""

import os
import re
import subprocess
import sys
import tempfile

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def split_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip("\"'")
    return meta, text[m.end() :]


def tex_escape(s):
    """Pandoc --variable values are injected into the template as raw LaTeX.

    So a bare underscore in a value - and the source filenames all have one,
    '2_nova' - reaches TeX in text mode and fails with 'Missing $ inserted'.
    That is a confusing error to chase, because it points at a line in the
    generated document rather than at the variable.
    """
    for ch in "_&%#":
        s = s.replace(ch, "\\" + ch)
    return s


def page_url(md_path):
    """_projects/2_nova.md -> yoogeunsong.com/projects/2_nova/"""
    stem = os.path.splitext(os.path.basename(md_path))[0]
    section = os.path.basename(os.path.dirname(md_path)).lstrip("_")
    return f"yoogeunsong.com/{section}/{stem}/"


def resolve_asset(path):
    """'/assets/img/x.png' -> absolute path on disk, for graphicx."""
    return os.path.join(REPO, path.lstrip("/"))


def figure_to_markdown(block):
    """Rewrite one raw <figure> element as a Markdown image + caption."""
    src = re.search(r"src=\"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}\"", block)
    if not src:
        src = re.search(r"src=\"([^\"]+)\"", block)
        if not src:
            return ""
    path = resolve_asset(src.group(1))

    cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", block, re.S)
    caption = ""
    if cap:
        caption = re.sub(r"<a [^>]*>(.*?)</a>", r"\1", cap.group(1), flags=re.S)
        caption = re.sub(r"<[^>]+>", "", caption)
        caption = " ".join(caption.split())
    return f"\n![{caption}]({path})\n"


def preprocess(md):
    # 2. Liquid includes - site furniture with no print equivalent.
    md = re.sub(r"\{%\s*include .*?%\}", "", md)

    # 4. Theme-swapped figures: drop the dark block, unwrap the light one.
    md = re.sub(r'<div class="only-dark">.*?</div>', "", md, flags=re.S)
    md = re.sub(r'<div class="only-light">(.*?)</div>', r"\1", md, flags=re.S)

    # 3. Remaining raw <figure> elements -> Markdown images.
    md = re.sub(r"<figure[^>]*>.*?</figure>", lambda m: figure_to_markdown(m.group(0)), md, flags=re.S)

    # Any leftover standalone <p> note (the figure credit line).
    md = re.sub(
        r"<p [^>]*>(.*?)</p>",
        lambda m: "\n_" + " ".join(re.sub(r"<[^>]+>", "", m.group(1)).split()) + "_\n",
        md,
        flags=re.S,
    )

    # 2b. Any surviving {{ ... }} output tags.
    md = re.sub(r"\{\{.*?\}\}", "", md)

    # 5. Inline $$...$$ -> $...$ (leave display blocks, which own their line).
    def demote(line):
        stripped = line.strip()
        if stripped.startswith("$$") and stripped.endswith("$$") and stripped.count("$$") == 2:
            return line  # a true display equation
        # $...$ rather than \(...\): pandoc only reads \( \) as math with the
        # tex_math_single_backslash extension, so without it the body lands as
        # literal text and the first _ or ^ throws "Missing $ inserted".
        return re.sub(r"\$\$(.+?)\$\$", r"$\1$", line)

    md = "\n".join(demote(l) for l in md.split("\n"))
    return md


PREAMBLE = r"""
\usepackage{amsmath,amssymb}
\usepackage{microtype}
\setlength{\emergencystretch}{3em}
\usepackage{float}
\makeatletter
\def\fps@figure{H}
\makeatother
\renewcommand{\familydefault}{\sfdefault}
\usepackage[font=small,labelformat=empty,skip=6pt]{caption}
\setlength{\parskip}{0.6em}
\setlength{\parindent}{0pt}
% Define the link colour rather than naming NavyBlue: pandoc's template loads
% xcolor without the dvipsnames option, so the named colours are not available.
\definecolor{linkindigo}{HTML}{312E81}
\hypersetup{colorlinks=true,linkcolor=linkindigo,urlcolor=linkindigo,citecolor=linkindigo}
"""


def build(md_path, pdf_path):
    with open(md_path, encoding="utf-8") as fh:
        meta, body = split_front_matter(fh.read())

    body = preprocess(body)

    header = os.path.join(tempfile.mkdtemp(), "header.tex")
    with open(header, "w", encoding="utf-8") as fh:
        fh.write(PREAMBLE)

    tmp_md = os.path.join(os.path.dirname(header), "body.md")
    with open(tmp_md, "w", encoding="utf-8") as fh:
        fh.write(body)

    cmd = [
        "pandoc", tmp_md,
        "--from=markdown+tex_math_dollars+raw_tex",
        "--pdf-engine=xelatex",
        "--include-in-header", header,
        "--variable", "documentclass=article",
        "--variable", "geometry:a4paper,margin=2.4cm",
        "--variable", "fontsize=11pt",
        "--variable", f"title={tex_escape(meta.get('title', os.path.basename(md_path)))}",
        "--variable", f"subtitle={tex_escape(meta.get('description', ''))}",
        "--variable", "author=Yoogeun (Eugene) Song",
        "--variable", f"date={tex_escape(page_url(md_path))}",
        # No --toc: these pages structure themselves with bold lead-ins rather
        # than headings, so a table of contents renders as an empty "Contents".
        "--resource-path", REPO,
        "-o", pdf_path,
    ]
    subprocess.run(cmd, check=True)
    return pdf_path


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "_projects/2_nova.md"
    out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/page.pdf"
    print(build(os.path.join(REPO, src) if not os.path.isabs(src) else src, out))
