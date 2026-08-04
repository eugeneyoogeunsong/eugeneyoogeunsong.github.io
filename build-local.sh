#!/usr/bin/env bash
# Local build check for yoogeunsong.com
#
# Usage:   cd into this folder, then:   bash build-local.sh
#
# Writes everything to build.log as well as the screen, so you can paste
# the log back to Claude if something fails.

set -o pipefail
cd "$(dirname "$0")" || exit 1

LOG="build.log"
: > "$LOG"

say() { printf '\n\033[1;35m==> %s\033[0m\n' "$*" | tee -a "$LOG"; }
run() { echo "\$ $*" | tee -a "$LOG"; "$@" 2>&1 | tee -a "$LOG"; return "${PIPESTATUS[0]}"; }

say "Environment"
run ruby -v
run bundle -v
run node -v
command -v magick >/dev/null 2>&1 || command -v convert >/dev/null 2>&1 \
  && echo "imagemagick: found" | tee -a "$LOG" \
  || echo "imagemagick: NOT FOUND -> brew install imagemagick (or set imagemagick.enabled: false in _config.yml)" | tee -a "$LOG"

say "Installing Ruby gems (first run takes a few minutes)"
run bundle config set --local path vendor/bundle
run bundle install || { say "bundle install FAILED — stop here and send me build.log"; exit 1; }

say "Installing Node deps"
if [ -f package-lock.json ]; then
  run npm ci || run npm install
fi

say "Building the site"
JEKYLL_ENV=production run bundle exec jekyll build --trace
STATUS=$?

if [ $STATUS -ne 0 ]; then
  say "BUILD FAILED (exit $STATUS) — send me build.log"
  exit $STATUS
fi

say "Build succeeded. Pages generated:"
find _site -name '*.html' -maxdepth 2 | sort | tee -a "$LOG"

say "Sanity checks"
for p in _site/index.html _site/research/index.html _site/publications/index.html \
         _site/projects/index.html _site/cv/index.html _site/interests/index.html \
         _site/contact/index.html; do
  if [ -f "$p" ]; then echo "  ok   $p" | tee -a "$LOG"; else echo "  MISS $p" | tee -a "$LOG"; fi
done

grep -q "Song" _site/publications/index.html 2>/dev/null \
  && echo "  ok   publications page rendered your name" | tee -a "$LOG" \
  || echo "  WARN publications page may not have rendered the bibliography" | tee -a "$LOG"

say "Now serving at http://localhost:4000  (Ctrl-C to stop)"
bundle exec jekyll serve --livereload --skip-initial-build
