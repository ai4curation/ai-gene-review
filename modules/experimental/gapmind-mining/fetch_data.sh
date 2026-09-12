#!/usr/bin/env bash
# Re-fetch the mining inputs for the GapMind feasibility spike.
# GapMind .steps files are small and committed; the ModelSEED reactions table
# (~37 MB) is gitignored and fetched here.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"

aa="$here/cache/gapmind/aa"
mkdir -p "$aa"
base="https://raw.githubusercontent.com/morgannprice/PaperBLAST/master/gaps/aa"
for f in arg asn chorismate cys gln gly his ile leu lys met phe pro ser thr trp tyr val; do
  curl -sSL --max-time 60 -o "$aa/$f.steps" "$base/$f.steps"
done

ms="$here/cache/modelseed"
mkdir -p "$ms"
curl -sSL --max-time 300 -o "$ms/reactions.tsv" \
  https://raw.githubusercontent.com/ModelSEED/ModelSEEDDatabase/master/Biochemistry/reactions.tsv

echo "Fetched $(ls "$aa"/*.steps | wc -l) GapMind aa pathways + ModelSEED reactions.tsv"
