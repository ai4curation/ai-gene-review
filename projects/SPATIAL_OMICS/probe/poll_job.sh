#!/usr/bin/env bash
# Poll an OpenScientist job to completion and save its markdown report.
#
# Usage: ./poll_job.sh <job_id> <output.md> [max_seconds]
#
# Submitted jobs are polled via the public API using OPENSCIENTIST_API_KEY.
# Note: the OpenScientist edge (Cloudflare) rejects request bodies that contain
# literal shell commands or code snippets, so hypothesis prompts for this project
# must be written in prose. See environment-probe-prompt.md.
set -uo pipefail

JOB_ID="${1:?job id required}"
OUT="${2:?output path required}"
MAX="${3:-3900}"
API="https://www.openscientist.io/api/v1"
AUTH="Authorization: Bearer ${OPENSCIENTIST_API_KEY:?OPENSCIENTIST_API_KEY not set}"

elapsed=0
while [ "$elapsed" -lt "$MAX" ]; do
  status_json=$(curl -sS -H "$AUTH" "$API/jobs/$JOB_ID/status")
  status=$(printf '%s' "$status_json" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("status","unknown"))' 2>/dev/null || echo parse_error)
  iter=$(printf '%s' "$status_json" | python3 -c 'import json,sys; d=json.load(sys.stdin); print(f"{d.get(\"current_iteration\")}/{d.get(\"max_iterations\")}")' 2>/dev/null || echo '?')
  echo "[${elapsed}s] status=$status iteration=$iter"

  case "$status" in
    completed|failed|cancelled|error)
      echo "Terminal status: $status"
      if [ "$status" = "completed" ]; then
        curl -sS -H "$AUTH" -H "Accept: text/markdown" "$API/jobs/$JOB_ID/report" -o "$OUT"
        echo "Report written to $OUT ($(wc -c < "$OUT") bytes)"
      else
        echo "Job did not complete successfully; no report downloaded."
        printf '%s\n' "$status_json"
      fi
      exit 0
      ;;
  esac

  sleep 30
  elapsed=$((elapsed + 30))
done

echo "Timed out after ${MAX}s; job still not terminal."
exit 1
