#!/usr/bin/env bash
# Wrapper for linkml-term-validator that fails on warnings.
# Uses upstream --strict or --fail-on-warnings flags when available;
# otherwise treats WARN output as fatal.
#
# Usage: scripts/run_term_validator.sh <subcommand> [args...]
#   e.g.: scripts/run_term_validator.sh validate-data file.yaml -s schema.yaml -t GeneReview --labels -c conf/oak_config.yaml

set -euo pipefail

if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <linkml-term-validator subcommand> [args...]" >&2
    exit 2
fi

subcommand=$1
shift

if [[ "$subcommand" != "validate-data" ]]; then
    exec uv run linkml-term-validator "$subcommand" "$@"
fi

help_output="$(uv run linkml-term-validator validate-data --help 2>&1)"
strict_args=()

if grep -q -- "--strict" <<<"$help_output"; then
    strict_args+=(--strict)
elif grep -q -- "--fail-on-warnings" <<<"$help_output"; then
    strict_args+=(--fail-on-warnings)
fi

cmd=(uv run linkml-term-validator validate-data "$@")
if [[ ${#strict_args[@]} -gt 0 ]]; then
    cmd+=("${strict_args[@]}")
fi

# The validator exits 2 with "ontology service unavailable" when a lookup times
# out. That is an outage, not a data error, and one slow response from the
# service has failed a whole validate-all run. Retry those, and only those.
attempts=${TERM_VALIDATOR_ATTEMPTS:-3}
delay=${TERM_VALIDATOR_RETRY_DELAY:-10}
attempt=1
while true; do
    set +e
    output="$("${cmd[@]}" 2>&1)"
    exit_code=$?
    set -e
    if [[ $exit_code -eq 2 && $attempt -lt $attempts ]] \
        && grep -q "ontology service unavailable" <<<"$output"; then
        echo "Ontology service unavailable (attempt $attempt of $attempts); retrying in ${delay}s." >&2
        sleep "$delay"
        attempt=$((attempt + 1))
        delay=$((delay * 2))
        continue
    fi
    break
done

printf '%s\n' "$output"

if [[ $exit_code -ne 0 ]]; then
    exit "$exit_code"
fi

if grep -Eq '(^|[^[:alnum:]_])(WARN|WARNING)([^[:alnum:]_]|$)' <<<"$output"; then
    echo "Strict term validation failed: validator emitted warnings." >&2
    exit 1
fi

