#!/usr/bin/env bash
# Download inputs for the RHEA->GO completeness pipeline into DATA_DIR (default .cache/rhea-completeness).
# Inputs are large and are not committed.
set -euo pipefail
DATA=${1:-.cache/rhea-completeness}; HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$DATA"
for f in rhea2uniprot_sprot.tsv rhea-directions.tsv rhea2ec.tsv rhea-relationships.tsv; do
  curl -sSf -o "$DATA/$f" "https://ftp.expasy.org/databases/rhea/tsv/$f"
done
curl -sSf -o "$DATA/rhea_all.tsv" 'https://www.rhea-db.org/rhea?query=&columns=rhea-id,equation,ec,chebi-id,uniprot&format=tsv&limit=50000'
curl -sSfL -o "$DATA/go-basic.obo" http://purl.obolibrary.org/obo/go/go-basic.obo
# MF GO annotations (with evidence/source) for every Swiss-Prot entry carrying a RHEA reaction.
cut -f4 "$DATA/rhea2uniprot_sprot.tsv" | tail -n +2 | sort -u > "$DATA/sp_accessions.txt"
rm -f "$DATA"/sp_mf.*.jsonl
uv run -q --with requests python "$HERE/fetch_by_acc.py" "$DATA/sp_accessions.txt" "$DATA/sp_mf.all.jsonl"
# Inputs for subunit_projection.py: native contributes_to MF rows, and complex-membership fields of Swiss-Prot Rhea entries.
curl -sSf -H 'Accept: text/tsv' -o "$DATA/goa_contributes_to_mf.tsv" 'https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?qualifier=contributes_to&aspect=molecular_function&geneProductType=protein&downloadLimit=200000&selectedFields=geneProductId,qualifier,goId,evidenceCode,reference,assignedBy'
curl -sSf -o "$DATA/sp_rhea_complex.tsv" 'https://rest.uniprot.org/uniprotkb/stream?query=reviewed:true+AND+cc_catalytic_activity:RHEA&fields=accession,organism_id,xref_complexportal,go_c,cc_subunit&format=tsv'
# Premise check for subunit_projection.py: qualifiers on UniProt's Rhea2GO projection (GO_REF:0000116).
# On 2026-11-26: enables 528129, contributes_to 0.
for q in enables contributes_to; do
  printf 'GO_REF:0000116 %s: ' "$q"
  curl -sSf -H 'Accept: application/json' "https://www.ebi.ac.uk/QuickGO/services/annotation/search?reference=GO_REF:0000116&qualifier=$q&limit=1" | python3 -c 'import sys,json; print(json.load(sys.stdin)["numberOfHits"])'
done | tee "$DATA/rhea2go_projection_qualifiers.txt"
