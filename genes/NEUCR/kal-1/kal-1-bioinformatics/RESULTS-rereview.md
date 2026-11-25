# kal-1 (Q7S7W0) relative placement, re-review 2026-10-21

Script: `compare_relatives_rereview.py` (PEP 723; `uv run --script compare_relatives_rereview.py > RESULTS-rereview.txt`).
Raw output: `RESULTS-rereview.txt`. Sequences and cross-references are fetched live from UniProt REST.

## Method

Global pairwise alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5) of the full
KAL-1 sequence and of its UniProt homeodomain DNA_BIND window (residues 77-136) against PANTHER
PTHR24324 members with experimental literature, plus the Aspergillus nidulans PF24818 protein.
Identity is reported as identical aligned positions divided by the shorter sequence length, so the
full-length value is inflated for short proteins (yox1, HHEX); the homeodomain value is the fairer
comparison for distant members. Shared HOGENOM / OrthoDB clusters are taken from the UniProt records.

## Results

| Accession | Gene | Species | Length | Full-length id % | Homeodomain id % | Shares KAL-1 HOGENOM cluster | Has PF24818 (PH_TRF2_HOY1) | PANTHER subfamily |
|---|---|---|---|---|---|---|---|---|
| G4N2B2 | TRF2 | Pyricularia oryzae | 625 | 67.3 | 93.3 | yes | yes | SF5 |
| C8VLD7 | ANIA_02009 | Aspergillus nidulans | 604 | 51.2 | 88.3 | yes | yes | SF5 |
| Q99160 | HOY1 | Yarrowia lipolytica | 509 | 28.5 | 55.0 | no | yes | SF5 |
| Q10328 | phx1 | Schizosaccharomyces pombe | 942 | 31.4 | 53.3 | no | no | SF5 |
| P07269 | PHO2 | Saccharomyces cerevisiae | 559 | 24.5 | 43.3 | no | no | SF5 |
| P40923 | yox1 | Schizosaccharomyces pombe | 201 | 37.3 | 35.0 | no | no | SF5 |
| Q03014 | HHEX | Homo sapiens | 270 | 27.8 | 35.0 | no | no | SF5 |
| Q04116 | YHP1 | Saccharomyces cerevisiae | 353 | 27.5 | 40.0 | no | no | SF9 |
| P34161 | YOX1 | Saccharomyces cerevisiae | 385 | 27.8 | 41.7 | no | no | SF9 |

## Interpretation

- KAL-1 is a full-length, single-homeodomain protein (615 aa, homeodomain 77-136, C-terminal PF24818
  PH-like domain); nothing suggests a fragment or alternative gene model.
- Pyricularia oryzae TRF2 (MGG_04853) is the KAL-1 ortholog: same PANTHER subfamily (SF5), same
  HOGENOM cluster (CLU_023524_1_0_1) and OrthoDB group (6159439at2759), same two-domain architecture
  (homeodomain + PF24818), near-identical length, 67% full-length and 93% homeodomain identity. Separate UniProt REST queries
  (`xref:pfam-PF24818 AND organism_id:242507` and `... organism_id:367110`, run 2026-10-21) return only TRF2
  in P. oryzae 70-15 and only KAL-1 in N. crassa OR74A, so each proteome has a single PF24818 homeobox
  protein and the pair is 1:1.
- Yarrowia HOY1 shares the domain architecture and subfamily but not the HOGENOM cluster, and has much
  lower identity; it is a more distant member of the same lineage.
- The yeast and animal IBA donors (PHO2, yox1, phx1, HHEX) share only the homeodomain (35-55% identity
  over the homeodomain) and lack the PF24818 domain, so only the shared homeodomain activity
  (sequence-specific DNA binding / RNA polymerase II-specific transcription factor activity) is a safe transfer.
  Their specific physiological roles (phosphate regulation, MBF repression, lysine biosynthesis
  regulation, vertebrate development) are not transferred.
