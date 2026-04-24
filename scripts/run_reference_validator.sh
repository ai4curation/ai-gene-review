#!/usr/bin/env bash
# Wrapper for linkml-reference-validator.
# Usage: scripts/run_reference_validator.sh [args...]
#   e.g.: scripts/run_reference_validator.sh validate data file.yaml --schema schema.yaml --target-class GeneReview --config conf/reference_validator_config.yaml

set -euo pipefail

exec uv run linkml-reference-validator "$@"
