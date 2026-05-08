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

    exec uv run linkml-reference-validator validate data "$tmp_file" "$@"
else
    exec uv run linkml-reference-validator "$@"
fi
