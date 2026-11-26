#!/bin/sh
# Residue checker for agent-review sandboxes: runs the repository's
# `ai-gene-review sequence-read residues` against this sandbox's genes/ folder.
#   sh tools/residues.sh human GENE D58 K72 --note "..." --write
set -e
unset CDPATH
SANDBOX=$(cd "$(dirname "$0")/.." && pwd)
UV_NO_SYNC=1 UV_FROZEN=1 UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1 \
  uv run --project "$AIGR_REPO" --directory "$SANDBOX" \
  ai-gene-review sequence-read residues "$@" --genes-root "$SANDBOX/genes"
