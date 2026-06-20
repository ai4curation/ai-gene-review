#!/usr/bin/env bash
# Run falcon deep research for a list of human genes (one per line in $1).
# Skips genes that already have a falcon deep-research file. Bounded concurrency.
set -uo pipefail
cd "$(dirname "$0")/.."

LIST="${1:?usage: run_falcon_batch.sh GENE_LIST_FILE [CONCURRENCY]}"
CONC="${2:-4}"
LOGDIR="/tmp/falcon_batch_logs"
mkdir -p "$LOGDIR"

run_one() {
  g="$1"
  out="genes/human/$g/$g-deep-research-falcon.md"
  if [ -s "$out" ]; then
    echo "SKIP $g (exists)"; return 0
  fi
  log="$LOGDIR/$g.log"
  # Edison/falcon jobs run ~600-700s; give the wrapper a 1200s internal timeout
  # and a slightly larger outer guard. The file is the source of truth: Edison
  # sometimes writes the report even when the wrapper races its own timeout.
  timeout 1300 uv run python scripts/deep_research_wrapper.py human "$g" falcon --timeout 1200 >"$log" 2>&1
  rc=$?
  if [ -s "$out" ]; then echo "OK   $g (rc=$rc)"; else echo "FAIL $g (rc=$rc, no file)"; fi
}
export -f run_one
export LOGDIR

grep -v '^[[:space:]]*$' "$LIST" | xargs -P "$CONC" -I{} bash -c 'run_one "$@"' _ {}
echo "=== BATCH DONE ==="
