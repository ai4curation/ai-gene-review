# TRF2 (G4N2B2, MGG_04853) relative placement, 2026-10-21

Script: `compare_relatives.py` (PEP 723; `uv run --script compare_relatives.py > RESULTS.txt`).
Raw output: `RESULTS.txt`. Sequences and cross-references are fetched live from UniProt REST.

## Method

Global pairwise alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5) of the full
TRF2 sequence and of its UniProt homeodomain DNA_BIND window (residues 73-132) against PANTHER
PTHR24324 members that have experimental literature, plus the Aspergillus nidulans PF24818 protein.
Identity is identical aligned positions divided by the shorter sequence length (inflated for short
proteins such as yox1 and HHEX; the homeodomain value is the fairer comparison). HOGENOM/OrthoDB sharing
is read from the UniProt records. A UniProt REST query counts PF24818 proteins in P. oryzae 70-15.

## Results

| Accession | Gene | Species | Full-length id % | Homeodomain id % | Shares TRF2 HOGENOM cluster | Has PF24818 | PANTHER subfamily |
|---|---|---|---|---|---|---|---|
| Q7S7W0 | kal-1 | Neurospora crassa | 67.3 | 93.3 | yes | yes | SF5 |
| C8VLD7 | ANIA_02009 | Aspergillus nidulans | 50.3 | 81.7 | yes | yes | SF5 |
| Q99160 | HOY1 | Yarrowia lipolytica | 32.0 | 55.0 | no | yes | SF5 |
| Q10328 | phx1 | Schizosaccharomyces pombe | 33.3 | 51.7 | no | no | SF5 |
| P07269 | PHO2 | Saccharomyces cerevisiae | 24.9 | 43.3 | no | no | SF5 |
| P40923 | yox1 | Schizosaccharomyces pombe | 32.8 | 36.7 | no | no | SF5 |
| Q03014 | HHEX | Homo sapiens | 27.8 | 33.3 | no | no | SF5 |
| Q04116 | YHP1 | Saccharomyces cerevisiae | 23.5 | 40.0 | no | no | SF9 |
| P34161 | YOX1 | Saccharomyces cerevisiae | 26.2 | 41.7 | no | no | SF9 |

The TRF2 homeodomain (residues 73-132) carries the helix-3 recognition motif WFQNRR (residues 120-125),
with I47, Q50, N51 and R53 (canonical homeodomain numbering) at residues 119, 122, 123 and 125.
TRF2 is the only PF24818 protein returned for P. oryzae 70-15.

## Interpretation

- TRF2 has an intact, typical homeodomain whose DNA-contacting helix-3 residues (I47/Q50/N51/R53) are those
  of canonical TAAT-core-binding homeodomains, so sequence-specific DNA binding is well supported by sequence.
- N. crassa KAL-1 is the TRF2 ortholog (same PANTHER subfamily SF5, same HOGENOM cluster CLU_023524_1_0_1,
  same homeodomain + PF24818 architecture, 67% full-length / 93% homeodomain identity, a single PF24818
  protein in each proteome). The OrthoDB group 6159439at2759 is a eukaryote-level group that also contains
  PHO2 and HHEX, so it is not by itself evidence of 1:1 orthology; the HOGENOM cluster and PF24818
  architecture are the discriminating features.
- HOY1 (Yarrowia) shares architecture and subfamily but is distant (55% homeodomain identity).
- The yeast and animal SF5 members with experimental data (PHO2, phx1, yox1, HHEX) share only the
  homeodomain (33-52% identity) and lack PF24818. Only the shared homeodomain activity
  (sequence-specific DNA binding, RNA polymerase II-specific transcription factor activity) is a safe
  transfer; their physiological roles (phosphate regulation, cell-cycle repression, vertebrate development)
  are not.
