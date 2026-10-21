#!/usr/bin/env bash
# Download the GO ontology and the GO Consortium GAFs used by the ligand gap check.
# Usage: projects/LIGANDS_IN_SIGNALING/scripts/fetch_data.sh [DATA_DIR]
# Default DATA_DIR is .cache/ligands_in_signaling (git-ignored).
set -euo pipefail
DATA_DIR="${1:-.cache/ligands_in_signaling}"
mkdir -p "$DATA_DIR"
for f in goa_human mgi rgd zfin fb sgd pombase; do
  curl -sSfL -o "$DATA_DIR/$f.gaf.gz" "https://current.geneontology.org/annotations/$f.gaf.gz"
  echo "fetched $f.gaf.gz ($(zcat "$DATA_DIR/$f.gaf.gz" | head -40 | grep -m1 'date-generated' || true))"
done
curl -sSfL -o "$DATA_DIR/go-basic.obo" https://purl.obolibrary.org/obo/go/go-basic.obo
echo "fetched go-basic.obo ($(grep -m1 '^data-version' "$DATA_DIR/go-basic.obo"))"
