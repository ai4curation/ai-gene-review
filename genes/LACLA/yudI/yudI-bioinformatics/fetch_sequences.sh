#!/usr/bin/env bash
# Fetch reference Dus sequences from UniProt and check the number of Dus
# family proteins in the IL1403 (UP000002196) and MG1363 (UP000000364) proteomes.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p data
for acc in Q9CE84 P0ABT5 P32695 P33371 P37567 O31546 Q2SR34 A2RN88; do
  curl -s "https://rest.uniprot.org/uniprotkb/${acc}.fasta" > "data/${acc}.fasta"
done
for proteome in UP000002196 UP000000364; do
  curl -s "https://rest.uniprot.org/uniprotkb/search?query=(xref:interpro-IPR001269+OR+xref:interpro-IPR035587+OR+xref:pfam-PF01207)+AND+proteome:${proteome}&fields=accession,gene_names,gene_oln,length&format=tsv" \
    > "data/dus_family_${proteome}.tsv"
done
