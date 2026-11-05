#!/usr/bin/env bash
# Fetch UniProt flat files for the E. coli experimental seeds of PAINT nodes
# PTN001252273 and PTN002019137 (AmpD P13016, AmiD P75820), used to check
# where the node members are located. Re-run to refresh.
set -euo pipefail
cd "$(dirname "$0")"
for acc in P13016 P75820; do
  curl -sf "https://rest.uniprot.org/uniprotkb/${acc}.txt" -o "${acc}.txt"
  grep -A1 "SUBCELLULAR LOCATION" "${acc}.txt" || true
done
