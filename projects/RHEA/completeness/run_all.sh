#!/usr/bin/env bash
# Usage: run_all.sh GO_EDIT_OBO [DATA_DIR]   (run fetch_data.sh first)
# GO_EDIT_OBO: src/ontology/go-edit.obo from a go-ontology checkout (mappings are read from its RHEA xrefs).
set -euo pipefail
OBO=$1; DATA=${2:-.cache/rhea-completeness}; HERE=$(cd "$(dirname "$0")" && pwd)
python3 "$HERE/coverage.py" "$DATA" "$OBO" | tee "$HERE/coverage_summary.txt"
python3 "$HERE/candidates.py" "$DATA" "$OBO"
python3 "$HERE/defmatch.py" "$DATA" "$OBO"
python3 "$HERE/native_consensus.py" "$DATA" 0.6
python3 "$HERE/consistency.py" "$DATA" "$OBO"
cp "$DATA/candidates3.tsv" "$HERE/unmapped_candidates.tsv"
cp "$DATA/consistency.tsv" "$HERE/consistency.tsv"
python3 "$HERE/subunit_projection.py" "$DATA" "$OBO" | tee "$HERE/subunit_projection_summary.txt"; cp "$DATA/subunit_projection.tsv" "$HERE/subunit_projection.tsv"
python3 "$HERE/subunit_consistency.py" "$DATA" "$OBO" | tee "$HERE/subunit_consistency_summary.txt"; cp "$DATA/subunit_consistency.tsv" "$HERE/subunit_consistency.tsv"
python3 "$HERE/subunit_flag_eval.py" "$DATA" "$OBO" | tee "$HERE/subunit_flag_eval_summary.txt"; cp "$DATA/subunit_flag_spotcheck.tsv" "$HERE/subunit_flag_spotcheck.tsv"
