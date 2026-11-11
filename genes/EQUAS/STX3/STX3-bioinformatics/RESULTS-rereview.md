# STX3 (donkey A0A9L0J901): splice-form identity of the benchmark gene model

Re-review analysis, 2026-10-21. Script: `compare_isoforms_rereview.py` (run with
`uv run --script compare_isoforms_rereview.py`); sequences fetched from the UniProt REST API
are saved in `isoforms_rereview.fasta`, per-segment results in `results_rereview.json`.
This analysis does not replace `RESULTS.md` (the earlier donkey-human pairwise comparison).

## Question

Syntaxin 3A and 3B share exons 1-8 and differ in the C-terminal half of the SNARE motif and in
the transmembrane anchor, which are encoded by alternatively spliced exons (PMID:18683220,
PMID:39408994). Which splice form does the benchmark model A0A9L0J901 encode?

## Method

Each sequence was globally aligned (Biopython PairwiseAligner; match 2, mismatch -1, gap open
-10, gap extend -0.5) to mouse syntaxin 3A (Q64704-1) and to mouse syntaxin 3B (Q64704-2).
Identity was computed over three segments of the reference: N (1-225, shared region), SNc
(226-262, C-terminal half of the SNARE motif) and TM (263-end, juxtamembrane region and
transmembrane anchor).

## Results (percent identity to mouse 3A / 3B)

| accession | length | N | SNc | TM | interpretation |
|---|---|---|---|---|---|
| A0A9L0J901 (benchmark) | 289 | 99.1 / 99.1 | 48.6 / 100.0 | 92.6 / 36.0 | 3B SNARE half + 3A anchor |
| A0A8C4LHZ8 (UniProt gene-centric canonical) | 289 | 99.1 / 99.1 | 91.9 / 48.6 | 92.6 / 36.0 | syntaxin 3A |
| A0A8C4PQW9 | 287 | 99.1 / 99.1 | 48.6 / 100.0 | 37.0 / 96.0 | syntaxin 3B |
| Q13277-1 (human isoform A) | 289 | 99.6 / 99.6 | 91.9 / 56.8 | 92.6 / 36.0 | syntaxin 3A |
| Q08849 (rat) | 289 | 100.0 / 100.0 | 100.0 / 48.6 | 96.3 / 36.0 | syntaxin 3A |

## Conclusion

The benchmark model A0A9L0J901 (Ensembl ENSEAST00005047497, non-canonical transcript of
ENSEASG00005007989) combines the syntaxin 3B exon for the C-terminal half of the SNARE motif
(identical to mouse 3B over residues 226-262) with the syntaxin 3A transmembrane-anchor exon.
This exon combination is not one of the four described rodent forms (3A, 3B, 3C, 3D;
PMID:7598732), so it is an alternative gene model of uncertain biological reality. It is full
length and keeps an intact Habc region, a complete SNARE motif and a C-terminal tail anchor.
The earlier statement that the benchmark is "a full-length counterpart of human isoform A" is
therefore not correct: its 92% identity to human isoform A is the average of near identity
outside the alternative exon and about 49% identity inside it.

The donkey syntaxin 3A product is A0A8C4LHZ8, which UniProt treats as the gene-centric
canonical protein of donkey STX3; the donkey 3B product is A0A8C4PQW9.
