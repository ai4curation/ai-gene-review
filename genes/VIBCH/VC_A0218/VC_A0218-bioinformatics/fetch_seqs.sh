#!/usr/bin/env bash
# Fetch the protein sequences compared in RESULTS.md.
# Reproducible: all sequences come from public UniProt / NCBI REST endpoints.
set -euo pipefail
cd "$(dirname "$0")/data"

# UniProt accessions
for acc in Q9KMV0 Q68CM4 O33407 Q9HUP2 P10480 Q9LU14; do
  curl -sS "https://rest.uniprot.org/uniprotkb/${acc}.fasta" -o "${acc}.fasta"
done

# NCBI protein: Fiore et al. 1997 V. cholerae lecithinase (lec) from strain E7946
curl -sS "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AAA92960.1&rettype=fasta&retmode=text" -o AAA92960.fasta
