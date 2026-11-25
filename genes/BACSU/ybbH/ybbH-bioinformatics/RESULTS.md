# ybbH/murR (Q45581): sequence comparison with RpiR-family regulators and SubtiWiki record

Script: `compare_rpir_homologs.py` (run with `uv run python genes/BACSU/ybbH/ybbH-bioinformatics/compare_rpir_homologs.py`).
Outputs: `data/pairwise_identity_vs_Q45581.tsv`, `data/subtiwiki_murR_BSU_01690.json`, and the UniProt FASTA files in `data/`.

## 1. Pairwise identity of Q45581 with characterized RpiR-family regulators

Global alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5); identity is over aligned columns.

| Subject | Description | Length | % identity |
|---|---|---|---|
| P77245 | E. coli MurR (YfeT), characterized MurNAc-6P repressor | 285 | 27.0 |
| P46118 | E. coli HexR (YebK) | 289 | 33.0 |
| Q8EE97 | S. oneidensis HexR (SO_2490) | 284 | 30.6 |
| P0ACS7 | E. coli RpiR (AlsR) | 296 | 24.4 |
| Q2G1G4 | S. aureus SAOUHSC_00160 (MurR-like, in the murQ cluster) | 291 | 28.1 |
| NZ_CP017763.1_2226 | KBase dashboard query (B. subtilis strain) | 291 | 98.2 |

Interpretation:

- YbbH is about as similar to E. coli HexR (33.0%) as to E. coli MurR (27.0%); by
  pairwise identity alone it is slightly closer to HexR. Sequence identity therefore
  cannot assign YbbH to the MurR rather than the HexR subfamily. The MurR assignment rests
  on gene context (ybbH lies inside the murQ-murP MurNAc-recycling operon) and on the
  B. subtilis reporter data of Morabbi Heravi and Altenbuchner 2018 (PMID:30038046), not
  on sequence similarity.
- The value for E. coli MurR (27.0%) agrees with the 26-27% reported by Litzinger et al.
  2010 and Borisova et al. 2016.
- The dashboard sequence is 98.2% identical to Q45581 over 283 aligned columns. It
  differs at one internal residue and at the C-terminus: Q45581 ends ...TRAAIQSMRIK
  (283 aa), whereas the dashboard sequence ends ...TRAAIQYENKIRHLEGEGF (291 aa). Both
  sequences keep the full HTH (3-79) and SIS (123-264) domains, so the difference does not
  affect domain architecture.

## 2. SubtiWiki record for murR (BSU_01690)

Fetched from the SubtiWiki v5 API (gene id 174) on 2026-10-30. Fields saved in
`data/subtiwiki_murR_BSU_01690.json`.

- SubtiWiki names the gene murR, with synonym ybbH, linked to UniProt Q45581.
- SubtiWiki describes MurR as the transcriptional repressor of genes required for the
  utilization of N-acetylmuramic acid.
- SubtiWiki operon: murQ-murR-murP-amiE-nagZ-namZ (namZ is the former ybbC). The operon
  is listed as negatively regulated by murR (transcription repression), citing
  PMID:30038046.
- SubtiWiki lists no effector for MurR.

Gene order (old names): ybbI (murQ) - ybbH (murR) - ybbF (murP) - ybbE (amiE) - ybbD
(nagZ) - ybbC (namZ), all on the minus strand; there is no ybbG in the operon.

## Limitations

- Pairwise identity is not a phylogeny. A tree of COG1737 proteins with known
  regulons would be needed to place YbbH firmly in the MurR rather than the HexR clade.
- The SubtiWiki API record is a curated database entry; the experimental basis for the
  repression call is PMID:30038046, which is cited directly in the review.
