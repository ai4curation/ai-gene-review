#!/usr/bin/env bash
# Local replacement for `just validate <org> <gene>` (just not installed here)
set -e
org="$1"; gene="$2"
schema="src/ai_gene_review/schema/gene_review.yaml"
file="genes/${org}/${gene}/${gene}-ai-review.yaml"
echo "== schema =="
uv run linkml-validate --schema "$schema" --target-class GeneReview "$file"
echo "== terms =="
scripts/run_term_validator.sh validate-data "$file" -s "$schema" -t GeneReview --labels -c conf/oak_config.yaml
echo "== references =="
scripts/run_reference_validator.sh validate data "$file" --schema "$schema" --target-class GeneReview --config conf/reference_validator_config.yaml
echo "== best practices =="
uv run ai-gene-review validate --verbose "$file"
echo "✓ ${org}/${gene} OK"
