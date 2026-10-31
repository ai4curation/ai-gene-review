#!/usr/bin/env bash
# Download the model files, HAMAP rule and sequences used by model_scores.py
# into a directory given as $1 (keep it outside any interpreter working
# directory). Prints sha256 sums so a later run can confirm identical inputs.
set -euo pipefail
D="${1:?usage: fetch_inputs.sh <download-dir>}"
mkdir -p "$D"
NCBI=https://ftp.ncbi.nlm.nih.gov/hmm/current
curl -sS -o "$D/TIGR02666.1.HMM" "$NCBI/hmm_PGAP.HMM/TIGR02666.1.HMM"
curl -sS -o "$D/TIGR02668.1.HMM" "$NCBI/hmm_PGAP.HMM/TIGR02668.1.HMM"
curl -sS -o "$D/RELEASE_NOTES.txt" "$NCBI/RELEASE_NOTES.txt"
curl -sS -L -o "$D/MF_01225_B.prf" https://hamap.expasy.org/profile/MF_01225_B.txt
curl -sS -o "$D/MF_01225.rule.txt" https://hamap.expasy.org/rule/MF_01225.txt
# Q88E69 canonical KT2440 MoaA; Q88LG4 PP_1969; Q88K11 PP_2482; reviewed MoaA from
# E. coli (P30745), S. aureus (P69848, HAMAP template), P. aeruginosa moaA1/moaA2
# (Q9HXD6, Q9I3K7); human MOCS1 (Q9NZB8, MOCS1A-MOCS1B fusion); KT2440 PqqE
# (Q88QV8) as a non-MoaA radical-SAM control.
curl -sS -o "$D/seqs.fasta" \
  "https://rest.uniprot.org/uniprotkb/accessions?accessions=Q88E69,Q88LG4,Q88K11,P30745,P69848,Q9HXD6,Q9I3K7,Q9NZB8,Q88QV8&format=fasta"
sha256sum "$D"/*.HMM "$D"/*.prf "$D"/*.rule.txt "$D"/seqs.fasta
