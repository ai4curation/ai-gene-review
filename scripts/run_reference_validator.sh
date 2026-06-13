#!/usr/bin/env bash
# Wrapper for linkml-reference-validator that strips supporting_text
# from entries marked full_text_unavailable: true before validation.
#
# The full_text_unavailable flag lets curators declare "I don't have full text
# so this quote may be from an abstract or is absent entirely" without failing
# validation. The reference validator CLI doesn't know about this convention,
# so we pre-process the YAML to remove supporting_text from those entries.
#
# Usage: scripts/run_reference_validator.sh [args...]
#   e.g.: scripts/run_reference_validator.sh validate data file.yaml --schema schema.yaml --target-class GeneReview --config conf/reference_validator_config.yaml

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

# If the first two args are "validate data", pre-process the data file
if [[ $# -ge 3 && "$1" == "validate" && "$2" == "data" ]]; then
    data_file="$3"
    shift 3  # remaining args: --schema ... --target-class ... --config ...

    # Create a temp copy with supporting_text stripped where full_text_unavailable
    tmp_file="$(mktemp "${data_file}.lrv.XXXXXX")"
    trap 'rm -f "$tmp_file"' EXIT

    uv run python -c "
import sys, yaml, copy

with open(sys.argv[1]) as f:
    data = yaml.safe_load(f)

def strip(obj):
    if isinstance(obj, dict):
        if 'supported_by' in obj and isinstance(obj['supported_by'], list):
            for sb in obj['supported_by']:
                if isinstance(sb, dict) and sb.get('full_text_unavailable'):
                    sb.pop('supporting_text', None)
        for v in obj.values():
            strip(v)
    elif isinstance(obj, list):
        for item in obj:
            strip(item)

strip(data)

with open(sys.argv[2], 'w') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
" "$data_file" "$tmp_file"

    run_lrv validate data "$tmp_file" "$@"
else
    run_lrv "$@"
fi
