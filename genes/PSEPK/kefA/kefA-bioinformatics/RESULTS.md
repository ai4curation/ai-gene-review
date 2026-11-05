# kefA (PP_5067) bioinformatics: homology to E. coli MscK and topology

Run: BERIL `runs/20261030T211325Z-kefa-homology-topology` (`just all`; numbers below are from `results.json`).
Inputs: dashboard sequence NZ_LGRH01000055.1_2 (`data/query.fasta`), UniProt Q88CW3, P77338 (E. coli MscK) and P0C0S1 (E. coli MscS) (`data/references.fasta`, `data/P77338.json`), and the DeepTMHMM path frozen in the dashboard call (`data/dashboard_call.json`).
Method: Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5; global for full-length pairs, local for MscS.

## Identity

| Subject | Mode | Identical / aligned | % identity | Query range | Subject range |
|---|---|---|---|---|---|
| Q88CW3 (KT2440 PP_5067) | global | 1089 / 1102 | 98.8 | 1-1102 | 1-1102 |
| P77338 (E. coli MscK, 1120 aa) | global | 464 / 1077 | 43.1 | 1-1102 | 1-1120 |
| P0C0S1 (E. coli MscS, 286 aa) | local | 74 / 254 | 29.1 | 828-1085 | 30-284 |

The query is a full-length MscK homologue (43.1% identical to E. coli MscK across its whole length), not an MscS-length protein. The MscS-like part is the C-terminal pore helix plus cytoplasmic domain (query 828-1085).

## Topology

DeepTMHMM on the query predicts a 1-24 signal peptide, a 25-490 extracytoplasmic region and 11 TM helices, with the C-terminus (919-1102) cytoplasmic.
All 11 predicted query TM segments map, via the global alignment, onto the 11 UniProt TM helices of E. coli MscK in order (TM1 500-520 ... TM11 922-942). The query signal peptide maps onto the MscK UniProt signal region 1-33.
This is the MscK architecture of a ~500-residue N-terminal periplasmic domain, an 11-helix TM domain and a C-terminal MscS-like cytoplasmic domain, as in the cryo-EM structure (PMID:36371466).
DeepTMHMM calls the N-terminal segment a cleavable signal peptide. Whether it is cleaved or acts as an anchor has not been tested for either protein.

## Conserved key residues

- The E. coli MscK W914 periplasmic tryptophan gate ring (PMID:36371466) aligns to query W897, which is conserved.
- The E. coli MscK G922 (kefA2 mutagenesis site in UniProt) aligns to query G905, which is conserved.
- The E. coli MscS pore-lining L105/L109 align to query V904/F908, which are hydrophobic.

## Genomic context (from dashboard evidence, not re-run)

In KT2440 and several P. fluorescens strains, the gene is flanked upstream by an NhaP2-type K+/H+ antiporter and downstream by SelO. This is conserved neighbourhood, not functional evidence.

## Limits

- No KT2440 fitness data could be retrieved: the Fitness Browser returned HTTP 403.
- The only fitness phenotypes in the dashboard evidence come from homologs (P. simiae WCS417 76%, polymyxin B; P. stutzeri RCH2 61.6%, nickel; Klebsiella 44%, D-alanine).
- K+-dependent gating has been shown only for E. coli MscK. Nothing here tests ion selectivity or K+ dependence in P. putida.
