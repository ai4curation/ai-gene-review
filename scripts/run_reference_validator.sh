#!/usr/bin/env bash
# Wrapper for linkml-reference-validator that strips supporting_text
# from entries marked full_text_unavailable: true before validation.
#
# The full_text_unavailable flag lets curators declare "I don't have full text
# so this quote may be from an abstract or is absent entirely" without failing
# validation. The reference validator CLI doesn't know about this convention,
# so we pre-process the YAML to remove supporting_text from those entries.
#
# Accepts one OR many data files. With many files it strips them in a single
# pass and makes a single `linkml-reference-validator validate data F1 F2 ...`
# call (the validator builds/parses the schema once), which is dramatically
# faster than one process per file. Requires linkml-reference-validator >= 0.2.1
# (multi-file `validate data`).
#
# Usage: scripts/run_reference_validator.sh validate data F1 [F2 ...] --schema S --target-class C --config CFG

set -euo pipefail

run_lrv() {
    set +e
    output="$(uv run linkml-reference-validator "$@" 2>&1)"
    exit_code=$?
    set -e

    printf '%s\n' "$output"

    if [[ $exit_code -eq 0 ]]; then
        return 0
    fi

    # linkml-reference-validator currently exits nonzero when it emits warning
    # results. Keep warning-only results advisory so unknown/unfetchable
    # references do not block validation.
    if grep -Eq '^[[:space:]]*\[WARN(ING)?\]' <<<"$output" \
        && ! grep -Eq '^[[:space:]]*\[ERROR\]|Traceback|^Error:' <<<"$output"; then
        return 0
    fi

    return "$exit_code"
}

# If the first two args are "validate data", pre-process the data file(s).
if [[ $# -ge 3 && "$1" == "validate" && "$2" == "data" ]]; then
    shift 2  # drop "validate data"; remaining = data files then options

    # Collect leading data-file arguments (everything up to the first option).
    data_files=()
    while [[ $# -gt 0 && "$1" != -* ]]; do
        data_files+=("$1")
        shift
    done
    # Remaining "$@" = options: --schema ... --target-class ... --config ...

    # The validator reads the data files directly. The only preprocessing is the
    # project's full_text_unavailable convention: for entries flagged
    # full_text_unavailable we drop supporting_text (the quote may be from an
    # abstract or unavailable, so it cannot be verified). Only files that actually
    # contain such an entry get a stripped temp copy written ALONGSIDE the original
    # (so relative `file:` references still resolve); every other file is passed to
    # the validator unchanged. A single Python pass writes, per input, the path to
    # validate (original or temp) to $resolved_list and any temp paths to
    # $cleanup_list. The corpus is kept strict-YAML-valid by tests/test_gene_yaml_strict.py.
    cleanup_list="$(mktemp)"
    resolved_list="$(mktemp)"
    trap 'while IFS= read -r t; do rm -f "$t"; done < "$cleanup_list"; rm -f "$cleanup_list" "$resolved_list"' EXIT

    uv run python -c "
import sys, os, tempfile, yaml

def strip(obj):
    changed = False
    if isinstance(obj, dict):
        sb = obj.get('supported_by')
        if isinstance(sb, list):
            for entry in sb:
                if isinstance(entry, dict) and entry.get('full_text_unavailable') and 'supporting_text' in entry:
                    entry.pop('supporting_text', None)
                    changed = True
        for v in obj.values():
            changed = strip(v) or changed
    elif isinstance(obj, list):
        for item in obj:
            changed = strip(item) or changed
    return changed

with open(sys.argv[1], 'w') as cleanup, open(sys.argv[2], 'w') as resolved:
    for src in sys.argv[3:]:
        with open(src) as f:
            data = yaml.safe_load(f)
        if strip(data):
            d = os.path.dirname(src) or '.'
            fd, tmp = tempfile.mkstemp(prefix=os.path.basename(src) + '.lrv.', dir=d)
            with os.fdopen(fd, 'w') as g:
                yaml.dump(data, g, default_flow_style=False, allow_unicode=True, sort_keys=False)
            cleanup.write(tmp + '\n')
            resolved.write(tmp + '\n')
        else:
            resolved.write(src + '\n')
" "$cleanup_list" "$resolved_list" "${data_files[@]}"

    # Read the resolved (original-or-stripped-temp) paths to validate.
    validate_files=()
    while IFS= read -r p; do
        validate_files+=("$p")
    done < "$resolved_list"

    run_lrv validate data "${validate_files[@]}" "$@"
else
    run_lrv "$@"
fi
