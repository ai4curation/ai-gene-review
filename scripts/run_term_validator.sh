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

# Route through term_validate.sh (resolved next to this script, so cwd does not
# matter) so a transient ontology-service outage is a skip (exit 97) rather than
# a hard failure. This path -- `ai-gene-review validate --terms`, i.e.
# `just validate-changed` and `just validate <org> <gene>` -- is how most gene
# PRs get their terms checked, so without this an EBI blip reddens every gene
# PR's own validation check (and a red PR can't enter the merge queue either).
here="$(cd "$(dirname "$0")" && pwd)"
set +e
cmd=("$here/term_validate.sh" validate-data "$@")
if [[ ${#strict_args[@]} -gt 0 ]]; then
    cmd+=("${strict_args[@]}")
fi
output="$("${cmd[@]}" 2>&1)"
exit_code=$?
set -e

printf '%s\n' "$output"

# 97 = outage, non-strict: the term check was skipped, not passed. The only
# output is the outage banner, so do not run the WARN grep below.
if [[ $exit_code -eq 97 ]]; then
    echo "::warning::Ontology service unavailable; strict term validation skipped (not a data error)." >&2
    exit 0
fi

# 96 = outage under TERM_VALIDATION_STRICT (weekly/manual full pass): block, so
# the unverified terms are caught once the service is back.
if [[ $exit_code -eq 96 ]]; then
    echo "Ontology service unavailable during strict term validation." >&2
    exit 1
fi

if [[ $exit_code -ne 0 ]]; then
    exit "$exit_code"
fi

if grep -Eq '(^|[^[:alnum:]_])(WARN|WARNING)([^[:alnum:]_]|$)' <<<"$output"; then
    echo "Strict term validation failed: validator emitted warnings." >&2
    exit 1
fi

