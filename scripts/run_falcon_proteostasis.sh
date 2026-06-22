#!/usr/bin/env bash
# Run falcon deep research in series for PROTEOSTASIS genes lacking deep research.
# Resumable: skips any gene that already has a *-deep-research-falcon.md file.
# Does NOT commit; integration + git handled separately.
set -u
cd "$(dirname "$0")/.."

WORKLIST="${1:-/tmp/worklist.txt}"
PROGRESS="/tmp/falcon_progress.log"
LOGDIR="/tmp/falcon_logs"
mkdir -p "$LOGDIR"

echo "=== driver start $(date) ===" >> "$PROGRESS"
while read -r g; do
  [ -z "$g" ] && continue
  dir="genes/human/$g"
  if [ ! -d "$dir" ]; then
    echo "$(date +%H:%M:%S) SKIP $g (no dir)" >> "$PROGRESS"
    continue
  fi
  if ls "$dir"/*-deep-research-falcon.md >/dev/null 2>&1; then
    echo "$(date +%H:%M:%S) SKIP $g (already has falcon)" >> "$PROGRESS"
    continue
  fi
  echo "$(date +%H:%M:%S) START $g" >> "$PROGRESS"
  uv run python -m ai_gene_review.tools.deep_research_unified human "$g" \
      --provider falcon > "$LOGDIR/$g.log" 2>&1
  rc=$?
  if ls "$dir"/*-deep-research-falcon.md >/dev/null 2>&1; then
    echo "$(date +%H:%M:%S) DONE  $g (rc=$rc)" >> "$PROGRESS"
  else
    echo "$(date +%H:%M:%S) FAIL  $g (rc=$rc)" >> "$PROGRESS"
  fi
done < "$WORKLIST"
echo "=== driver end $(date) ===" >> "$PROGRESS"
