#!/usr/bin/env bash
# Run `linkml-term-validator` (the caller passes the full subcommand, e.g.
# `validate-data <files> -s ... -t ... --labels -c ...`) while treating a
# transient ontology-service outage as a skip rather than a hard failure.
#
# linkml-term-validator (>=0.4.5) exits with EXIT_SERVICE_UNAVAILABLE (2) and
# prints "ontology service unavailable" when it cannot reach the ontology
# service (e.g. an EBI read timeout). Nothing was checked -- that is not a data
# error. Keying a blocking decision on it (via the "Unable to validate" text in
# a grep, or a bare `|| rc=1`) turns an upstream blip into a hard failure, which
# in the merge queue fails the check for every PR at the front and jams the
# whole queue (observed with #6261-#6263 and many unrelated PRs). Exit code 2 is
# also typer/click/uv's usage-error code, so the outage is matched on code 2 AND
# the banner text, never on the code alone.
#
# This wrapper normalizes only that one case and passes everything else through
# unchanged, so each caller's own output grep (which classifies ❌ ERROR vs
# advisory ⚠️ WARN -- validate-data exits 1 for both) keeps working:
#   exit 0      -> validated, no issues
#   exit 1      -> validate-data reported issues (caller greps to classify)
#   exit 2      -> ontology-service outage, STRICT: treat as fatal (block)
#   exit 3      -> ontology-service outage, skipped (non-strict)
#   other       -> passed through unchanged
# The caller decides what a skip (3) means for it and emits the GitHub Actions
# ::warning:: itself (so it survives the caller capturing this script's stdout).
# linkml-term-validator's own stdout/stderr is always reprinted here.
#
# Env:
#   TERM_VALIDATION_STRICT  non-empty -> an outage exits 2 (block) instead of 3.
#                           Set on the weekly/manual full pass so an unverified
#                           term is still caught once the service is reachable.
#   TERM_VALIDATE_RETRIES   extra attempts on an outage (default 2), 8s apart,
#                           to ride out a brief blip. Set 0 in per-file loops.
set -uo pipefail

banner_re='ontology service unavailable|could not reach ontology service'
retries="${TERM_VALIDATE_RETRIES:-2}"
attempt=0
while :; do
    out="$(uv run linkml-term-validator "$@" 2>&1)"
    rc=$?
    if [ "$rc" -eq 2 ] && printf '%s\n' "$out" | grep -qE "$banner_re"; then
        if [ "$attempt" -lt "$retries" ]; then
            attempt=$((attempt + 1))
            sleep 8
            continue
        fi
        printf '%s\n' "$out"
        if [ -n "${TERM_VALIDATION_STRICT:-}" ]; then
            exit 2
        fi
        exit 3
    fi
    printf '%s\n' "$out"
    exit "$rc"
done
