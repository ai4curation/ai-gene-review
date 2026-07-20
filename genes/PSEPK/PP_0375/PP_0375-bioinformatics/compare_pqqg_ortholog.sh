#!/usr/bin/env bash
set -euo pipefail

output_dir="${1:-results}"
mkdir -p "$output_dir"

tmp_dir="$(mktemp -d "${TMPDIR:-/tmp}/pqqg-ortholog.XXXXXX")"
trap 'rm -rf "$tmp_dir"' EXIT

curl -fsSL 'https://rest.uniprot.org/uniprotkb/Q88QV9.fasta' \
  -o "$tmp_dir/Q88QV9.fasta"
curl -fsSL \
  'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AAX10035.1&rettype=fasta&retmode=text' \
  -o "$tmp_dir/AAX10035.fasta"
curl -fsSL 'https://rest.uniprot.org/uniprotkb/Q9I2B9.fasta' \
  -o "$tmp_dir/Q9I2B9.fasta"
curl -fsSL \
  'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AAX10035.1&rettype=gb&retmode=text' \
  -o "$output_dir/AAX10035.1.gb"

mmseqs easy-search \
  "$tmp_dir/Q88QV9.fasta" \
  "$tmp_dir/AAX10035.fasta" \
  "$output_dir/PP_0375_vs_AAX10035.tsv" \
  "$tmp_dir/mmseqs" \
  --format-output 'query,target,pident,alnlen,qcov,tcov,evalue,bits' \
  -v 1

mmseqs easy-search \
  "$tmp_dir/Q88QV9.fasta" \
  "$tmp_dir/Q9I2B9.fasta" \
  "$output_dir/PP_0375_vs_Q9I2B9.tsv" \
  "$tmp_dir/mmseqs-pa1990" \
  --format-output 'query,target,pident,alnlen,qcov,tcov,evalue,bits' \
  -v 1
