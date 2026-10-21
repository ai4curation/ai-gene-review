#!/usr/bin/env bash
# Re-run every SURFACEOME analysis from the repo root; writes projects/SURFACEOME/results/.
set -euo pipefail
cd "$(dirname "$0")/../../.."
S=projects/SURFACEOME/scripts R=projects/SURFACEOME/results
[ -f projects/SURFACEOME/data/goa_human.gaf.gz ] || $S/fetch_inputs.sh
PYTHONPATH=$S uv run python $S/overlap.py       | tee $R/overlap.txt
PYTHONPATH=$S uv run python $S/score_gaf.py     | tee $R/gaf_scores.txt
PYTHONPATH=$S uv run python $S/score_reviews.py | tee $R/review_scores.txt
