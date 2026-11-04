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
