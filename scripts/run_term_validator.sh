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
# This wrapper is always a per-file path: cli.py's `ai-gene-review validate
# --terms` and `just validate-terms-all` call it once per file in a sequential
# loop. A retry there is paid per file and can't short-circuit across processes,
# so on a large gene PR during a sustained outage it adds N×(timeouts + sleep)
# serially -- enough to trip the merge queue's response timeout. The skip here
# is advisory (97), so a retry buys only coverage, never pass/fail; default to
# none (the helper's own header prescribes 0 for per-file loops). An explicit
# TERM_VALIDATE_RETRIES still wins.
export TERM_VALIDATE_RETRIES="${TERM_VALIDATE_RETRIES:-0}"
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
# captured output is the outage banner, so the WARN grep below is not reached.
# The ::warning:: (stderr) is for direct terminal / Actions use. The stdout WARN
# line is the one that matters for the dominant path: `ai-gene-review validate
# --terms` runs this wrapper under subprocess.run(capture_output=True), and
# cli.py's _warning_lines matches a "⚠"/"WARN" line, so without it an outage
# would be recorded as no issue at all and the gene PR would go green with no
# trace the terms were skipped. It is emitted after the $output capture, so the
# wrapper's own WARN grep is unaffected; it does not match the NCBITaxon
# label-mismatch pattern, so cli.py keeps it advisory (non-blocking).
if [[ $exit_code -eq 97 ]]; then
    echo "::warning::Ontology service unavailable; term validation skipped (not a data error)." >&2
    echo "⚠️  WARN: ontology service unavailable; term validation skipped (not a data error)"
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

