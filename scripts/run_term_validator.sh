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

# A failed lookup is not a data verdict. Re-run the complete validation, which
# reuses labels already fetched into its cache, rather than skipping any term.
# Only the final attempt's report goes to the caller: the gene validator also
# parses error-like text, so a recovered transport error must not masquerade as
# a remaining data error. An exhausted outage retains its nonzero status/report.
for attempt_count in 1 2 3; do
    set +e
    output="$("${cmd[@]}" 2>&1)"
    exit_code=$?
    set -e
    if [[ $exit_code -eq 0 || $attempt_count -eq 3 ]] ||
        ! grep -Fq 'Terms could not be checked; this is not a data error.' <<<"$output"; then
        break
    fi
    printf 'Ontology lookup temporarily unavailable; retrying complete term validation (%s/3).\n' "$((attempt_count + 1))" >&2
    sleep "$attempt_count"
done

printf '%s\n' "$output"

if [[ $exit_code -ne 0 ]]; then
    exit "$exit_code"
fi

if grep -Eq '(^|[^[:alnum:]_])(WARN|WARNING)([^[:alnum:]_]|$)' <<<"$output"; then
    echo "Strict term validation failed: validator emitted warnings." >&2
    exit 1
fi

