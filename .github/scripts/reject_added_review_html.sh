#!/usr/bin/env bash
# Fail if HEAD adds rendered gene review HTML relative to its first parent.
#
# The HTML is gitignored and built by the Pages workflow (#6221). In CI, HEAD
# is the PR merge commit, the merge-queue commit or the pushed commit, so its
# first parent is the base. Edits and deletions of still-tracked copies pass.
set -euo pipefail

# Explicit glob magic: a bare `genes/*` pathspec also crosses `/`, but adding
# `:(glob)` to it later would silently match nothing.
pathspec=':(glob)genes/**/*-ai-review.html'

# Read the parent from the commit object: in a depth-1 clone `git log --pretty=%P`
# reports no parents, which would turn this check into a silent pass. awk reads
# all of its input rather than exiting early, so git never gets SIGPIPE.
base=$(git cat-file -p HEAD | awk '/^parent / && !p {p = $2} END {print p}')
if [ -z "$base" ]; then
  echo "HEAD has no parent; nothing to compare."
  exit 0
fi
if [[ ! "$base" =~ ^[0-9a-f]{40}$ ]]; then
  echo "Unexpected parent id: $base" >&2
  exit 1
fi
# A depth-1 checkout lacks the parent; persist-credentials is off, so this
# uses public read access.
if ! git cat-file -e "$base^{commit}" 2>/dev/null; then
  git fetch --quiet --no-tags --depth=1 origin "$base"
fi

added=$(git diff --no-renames --name-only --diff-filter=A "$base" HEAD -- "$pathspec")
if [ -n "$added" ]; then
  echo "::error title=Rendered HTML added::Gene review HTML is a build product. Untrack it with git rm --cached (for a renamed gene folder, untrack the HTML at the new path):"
  echo "$added"
  exit 1
fi
echo "No gene review HTML added."
