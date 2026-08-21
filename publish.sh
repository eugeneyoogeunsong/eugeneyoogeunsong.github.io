#!/usr/bin/env bash
#
# Format, commit and push in one step.
#
#   bash publish.sh "About: fixed a typo"
#   bash publish.sh                        # uses a generic message
#
# Why the Prettier step matters: the repo runs `prettier . --check` in CI, so an
# unformatted file turns the Actions tab red even though the site builds fine.
# Running it here means that never happens.

set -euo pipefail
cd "$(dirname "$0")"

MSG="${1:-Content update}"

echo "==> Formatting with Prettier"
if [ ! -d node_modules/prettier ]; then
  echo "    (first run: installing prettier locally, ~20s)"
  npm install --silent
fi
npx prettier . --write --log-level warn

echo "==> Changes"
if git diff --quiet && git diff --cached --quiet && [ -z "$(git status --porcelain)" ]; then
  echo "    nothing to commit"
else
  git status --short
fi

echo "==> Committing"
git add -A
git commit -m "$MSG" || echo "    nothing new to commit"

echo "==> Syncing with remote"
# The update-citations workflow commits Google Scholar counts straight to main on
# a schedule, so the remote is regularly one bot commit ahead of you. Without this
# step the push below is rejected as non-fast-forward through no fault of yours.
# --autostash covers anything Prettier left behind after the commit above.
git fetch origin main
if ! git rebase --autostash origin/main; then
  echo
  echo "    Rebase stopped on a conflict. Nothing is lost and nothing has been pushed."
  echo "    Fix the files listed above, then:"
  echo "      git add <files> && git rebase --continue && git push origin main"
  echo "    Or back out entirely with:"
  echo "      git rebase --abort"
  exit 1
fi

echo "==> Pushing"
git push origin main

echo
echo "Done. Watch the build here:"
echo "  https://github.com/eugeneyoogeunsong/eugeneyoogeunsong.github.io/actions"
echo "Live in a few minutes at https://yoogeunsong.com"
