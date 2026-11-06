#!/usr/bin/env bash
# Fetch KEGG records for the MG1363 genes flanking sufB (llmg_1969) to show operon context.
# Usage: bash fetch_neighborhood.sh > neighborhood_output.txt
set -euo pipefail
for i in $(seq 1968 1975); do
  curl -sS -m 30 "https://rest.kegg.jp/get/llm:llmg_$i" \
    | grep -E "^(ENTRY|SYMBOL|NAME|ORTHOLOGY|POSITION)" | tr -s ' ' | paste -sd'|'
done
