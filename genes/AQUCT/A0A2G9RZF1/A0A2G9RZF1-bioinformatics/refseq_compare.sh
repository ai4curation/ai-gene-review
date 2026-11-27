#!/usr/bin/env bash
# Compare A0A2G9RZF1 with the complete bullfrog TLL1 and BMP1 gene models from the
# chromosome-level RefSeq annotation (XP_073462190.1 TLL1; XP_073478370.1 BMP1).
set -euo pipefail
cd "$(dirname "$0")"
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=XP_073462190.1,XP_073478370.1&rettype=fasta&retmode=text" > refseq_tolloids.fasta
phmmer --domtblout phmmer_refseq.domtbl query.fasta refseq_tolloids.fasta > phmmer_refseq.out
grep -v '^#' phmmer_refseq.domtbl | awk '{printf "%s\tlen=%s\tdom=%s/%s\tdomBits=%s\ttarget=%s-%s\tquery=%s-%s\n",$1,$3,$10,$11,$14,$18,$19,$16,$17}' | tee phmmer_refseq_summary.tsv
