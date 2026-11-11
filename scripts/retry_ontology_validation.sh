#!/usr/bin/env bash
# Retry complete ontology validation only for an explicitly unavailable service.
# This helper sets no warning policy: strict and corpus callers retain theirs.
set -euo pipefail
if [[ $# -eq 0 ]]; then
    echo "Usage: scripts/retry_ontology_validation.sh command [args...]" >&2
    exit 2
fi
for attempt_count in 1 2 3; do
    set +e
    output="$("$@" 2>&1)"
    exit_code=$?
    set -e
    unavailable=false
    if grep -Eq 'Terms could not be checked; this is not a data error\.|Unable to validate at this time: ontology service unavailable' <<<"$output"; then
        unavailable=true
    fi
    if ! $unavailable || [[ $attempt_count -eq 3 ]]; then
        break
    fi
    printf 'Ontology lookup temporarily unavailable; retrying complete term validation (%s/3).\n' "$((attempt_count + 1))" >&2
    sleep "$attempt_count"
done
printf '%s\n' "$output"
# A skipped check cannot become success just because the upstream tool exits 0.
if $unavailable; then
    printf '%s\n' 'Unable to validate at this time: ontology service unavailable after 3 attempts.' >&2
    if [[ $exit_code -eq 0 ]]; then
        exit_code=1
    fi
fi
exit "$exit_code"
