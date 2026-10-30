#!/usr/bin/env bash
# Reciprocal phmmer between S. pombe crt10 (O42996) and the S. cerevisiae proteome,
# and between S. cerevisiae Crt10 (Q08226) and the S. pombe proteome.
# Requires HMMER (phmmer) on PATH. Downloads reference proteomes from UniProt.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
work="${WORK:-$(mktemp -d)}"
mkdir -p "$work"
fetch() { curl -s "https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=$1" -o "$2"; }
[ -s "$work/scer.fasta" ] || fetch "proteome:UP000002311" "$work/scer.fasta"
[ -s "$work/spom.fasta" ] || fetch "proteome:UP000002485" "$work/spom.fasta"
fetch "accession:O42996" "$work/O42996.fasta"
fetch "accession:Q08226" "$work/Q08226.fasta"
echo "S. cerevisiae proteome size: $(grep -c '>' "$work/scer.fasta")"
echo "S. pombe proteome size: $(grep -c '>' "$work/spom.fasta")"
echo "== O42996 (S. pombe crt10) vs S. cerevisiae proteome: top 5 =="
phmmer --noali --tblout "$work/O42996_vs_scer.tbl" "$work/O42996.fasta" "$work/scer.fasta" > /dev/null
grep -v '^#' "$work/O42996_vs_scer.tbl" | head -5 | awk '{print $1, "E="$5, "score="$6}'
echo "== Q08226 (S. cerevisiae Crt10) vs S. pombe proteome: top 5 =="
phmmer --noali --tblout "$work/Q08226_vs_spom.tbl" "$work/Q08226.fasta" "$work/spom.fasta" > /dev/null
grep -v '^#' "$work/Q08226_vs_spom.tbl" | head -5 | awk '{print $1, "E="$5, "score="$6}'
echo "== O42996 vs Q08226 domain-level alignment =="
phmmer "$work/O42996.fasta" "$work/Q08226.fasta" | sed -n '/Domain annotation/,/Internal pipeline/p' | head -40
echo "== O42996 non-WD40 C-terminal region (residues 260-482) vs S. cerevisiae proteome: top 5 =="
python3 -c "
import sys
lines=open('$work/O42996.fasta').read().split(chr(10))
seq=''.join(l for l in lines[1:] if l)
print('>O42996_260-482'); print(seq[259:482])" > "$work/O42996_Cterm.fasta"
phmmer --noali --tblout "$work/O42996_Cterm_vs_scer.tbl" "$work/O42996_Cterm.fasta" "$work/scer.fasta" > /dev/null
grep -v '^#' "$work/O42996_Cterm_vs_scer.tbl" | head -5 | awk '{print $1, "E="$5, "score="$6}'
echo "Rank of Q08226 (CRT10_YEAST) in full-length O42996 search:"
grep -v '^#' "$work/O42996_vs_scer.tbl" | awk '{print NR, $1, "E="$5}' | grep CRT10 || echo "not found"
echo "Total hits in full-length search: $(grep -vc '^#' "$work/O42996_vs_scer.tbl")"
