#!/usr/bin/env bash
# Fetch the dusA gene models and upstream context used in RESULTS.md.
#   S. meliloti 1021 (AL591688.1 / NC_003047.1): SMc04235, UniProt Q92P85
#   E. meliloti USDA1810 (NZ_RPHN01000062.1): source contig of the KBase item
# Run from this directory: bash fetch_gene_models.sh
set -euo pipefail
E=https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi
# 1021: dusA CDS (EMBL) is complement(2061682..2062761); take 300 nt upstream
sleep 1; curl -s "$E?db=nuccore&id=AL591688.1&seq_start=2061682&seq_stop=2063061&strand=2&rettype=fasta&retmode=text" > sm1021_dusA_region_AL591688.1.fasta
sleep 1; curl -s "$E?db=nuccore&id=NC_003047.1&seq_start=2061500&seq_stop=2063200&rettype=ft&retmode=text" > sm1021_refseq_features.txt
sleep 1; curl -s "$E?db=protein&id=WP_015241224.1&rettype=fasta&retmode=text" > refseq_WP_015241224.1.fasta
# USDA1810: dusA CDS is 39436..40515 (+); take 300 nt upstream
sleep 1; curl -s "$E?db=nuccore&id=NZ_RPHN01000062.1&seq_start=39136&seq_stop=40518&rettype=fasta&retmode=text" > usda1810_dusA_region_NZ_RPHN01000062.1.fasta
sleep 1; curl -s "$E?db=nuccore&id=NZ_RPHN01000062.1&rettype=ft&retmode=text" > usda1810_contig62_features.txt
