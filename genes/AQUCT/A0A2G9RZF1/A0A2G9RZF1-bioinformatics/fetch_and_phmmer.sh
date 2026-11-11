#!/usr/bin/env bash
# Re-review analysis: compare the 156-aa A0A2G9RZF1 CUB ORF against full-length
# characterised CUB proteins (tolloids, PCOLCE, MFRP, cubilin, NETO) and the two
# neighbouring ORFs on scaffold KV928989. Uses UniProt REST + local phmmer (HMMER3).
set -euo pipefail
cd "$(dirname "$0")"
QUERY=A0A2G9RZF1
PANEL="A0A2G9RZH1 A0A2G9RZI6 P13497 O43897 Q9Y6L7 Q15113 Q9UKZ9 Q9BY79 O60494 Q8TDF5 Q8NC67 P98070 Q20176 Q8JI28 O57382 Q62381 P98063"
curl -s "https://rest.uniprot.org/uniprotkb/${QUERY}.fasta" > query.fasta
: > panel.fasta
for a in $PANEL; do curl -s "https://rest.uniprot.org/uniprotkb/${a}.fasta" >> panel.fasta; done
phmmer --domtblout phmmer_panel.domtbl -E 10 --domE 10 query.fasta panel.fasta > phmmer_panel.out
grep -v '^#' phmmer_panel.domtbl | awk '{printf "%s\t%s\tlen=%s\tfullE=%s\tbits=%s\tdom=%s/%s\tdomE=%s\tdomBits=%s\ttarget=%s-%s\tquery=%s-%s\n",$1,$23" "$24" "$25" "$26,$3,$7,$8,$10,$11,$13,$14,$18,$19,$16,$17}' > phmmer_panel_summary.tsv
cat phmmer_panel_summary.tsv
