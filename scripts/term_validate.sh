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
# advisory ⚠️ WARN -- validate-data exits 1 for both) keeps working. It reports
# an outage with exit codes linkml-term-validator itself never returns (it exits
# 0/1/2), so a real LTV status can never be mistaken for the outage sentinel:
#   exit 0      -> validated, no issues
#   exit 1      -> validate-data reported issues (caller greps to classify)
#   exit 96     -> ontology-service outage, STRICT: caller must block
#   exit 97     -> ontology-service outage, skipped (non-strict)
#   other       -> linkml-term-validator's own status, passed through unchanged
# The caller decides what a skip (97) means for it and emits the GitHub Actions
# ::warning:: itself (so it survives the caller capturing this script's stdout).
# linkml-term-validator's own stdout/stderr is always reprinted here.
#
# Env:
#   TERM_VALIDATION_STRICT  non-empty -> an outage exits 96 (block) instead of 97.
#                           Set on the weekly/manual full pass so an unverified
#                           term is still caught once the service is reachable.
#   TERM_VALIDATE_RETRIES   extra attempts on an outage (default 1, non-numeric
#                           treated as 1), 8s apart, to ride out a brief blip.
#                           Set 0 in per-file loops.
set -uo pipefail

EXIT_OUTAGE_STRICT=96   # outage under TERM_VALIDATION_STRICT: caller blocks
EXIT_OUTAGE_SKIP=97     # outage, non-strict: caller skips with a ::warning::

banner_re='ontology service unavailable|could not reach ontology service'
case "${TERM_VALIDATE_RETRIES:-}" in
    '' | *[!0-9]*) retries=1 ;;   # default / non-numeric -> one retry
    *) retries="${TERM_VALIDATE_RETRIES}" ;;
esac
attempt=0
while :; do
    out="$(uv run linkml-term-validator "$@" 2>&1)"
    rc=$?
    if [ "$rc" -eq 2 ] && printf '%s\n' "$out" | grep -qE "$banner_re"; then
        if [ "$attempt" -lt "$retries" ]; then
            attempt=$((attempt + 1))
            echo "::notice::ontology service unavailable; retrying term validation ($attempt/$retries)" >&2
            sleep 8
            continue
        fi
        printf '%s\n' "$out"
        # Record the outage on the run's step summary too, so it is visible even
        # when a caller captures both stdout and stderr (e.g. cli.py's multi-file
        # validate-changed prints issue detail only for invalid files, so the
        # stdout WARN line is counted but not shown). Best-effort: never fail here.
        if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
            if [ -n "${TERM_VALIDATION_STRICT:-}" ]; then
                echo "⚠️ Ontology service unavailable; term validation blocked (strict full pass)." >> "$GITHUB_STEP_SUMMARY" 2>/dev/null || true
            else
                echo "⚠️ Ontology service unavailable; term validation skipped (not a data error)." >> "$GITHUB_STEP_SUMMARY" 2>/dev/null || true
            fi
        fi
        if [ -n "${TERM_VALIDATION_STRICT:-}" ]; then
            exit "$EXIT_OUTAGE_STRICT"
        fi
        exit "$EXIT_OUTAGE_SKIP"
    fi
    printf '%s\n' "$out"
    exit "$rc"
done
