#!/usr/bin/env bash
# Download the inputs of the cell-cell communication resource audit.
# Usage: projects/SPATIAL_CELL_COMMUNICATION/scripts/fetch_data.sh [DATA_DIR]
# Default DATA_DIR is .cache/spatial_ccc (git-ignored). Nothing here is committed.
set -euo pipefail
DATA_DIR="${1:-.cache/spatial_ccc}"
CPDB_TAG="${CPDB_TAG:-v5.0.0}"
mkdir -p "$DATA_DIR/cellphonedb"
for f in interaction_input complex_input protein_input gene_input; do
  curl -sSfL -o "$DATA_DIR/cellphonedb/$f.csv" \
    "https://raw.githubusercontent.com/ventolab/cellphonedb-data/$CPDB_TAG/data/$f.csv"
done
echo "$CPDB_TAG" > "$DATA_DIR/cellphonedb/VERSION"
echo "fetched CellPhoneDB data $CPDB_TAG"
# OmniPath: directed interactions from the omnipath and ligrecextra datasets, and
# generic composite ligand / receptor roles from the intercell database.
curl -sSfL -o "$DATA_DIR/omnipath_interactions.tsv" \
  "https://omnipathdb.org/interactions?datasets=omnipath,ligrecextra&genesymbols=yes&fields=sources,references,curation_effort,datasets&license=academic"
curl -sSfL -o "$DATA_DIR/omnipath_intercell.tsv" \
  "https://omnipathdb.org/intercell?categories=ligand,receptor&scope=generic&aspect=functional&source=composite"
date -u +%Y-%m-%d > "$DATA_DIR/OMNIPATH_RETRIEVED"
echo "fetched OmniPath interactions and intercell roles"
curl -sSfL -o "$DATA_DIR/HOM_MouseHumanSequence.rpt" https://www.informatics.jax.org/downloads/reports/HOM_MouseHumanSequence.rpt
echo "fetched MGI human-mouse homology report"
curl -sSfL -o "$DATA_DIR/goa_human.gaf.gz" https://current.geneontology.org/annotations/goa_human.gaf.gz
curl -sSfL -o "$DATA_DIR/go-basic.obo" https://purl.obolibrary.org/obo/go/go-basic.obo
echo "fetched goa_human.gaf.gz and go-basic.obo ($(grep -m1 '^data-version' "$DATA_DIR/go-basic.obo"))"
