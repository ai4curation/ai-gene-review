# C6T1A2 re-review bioinformatics (2026-10-20)

Independent of any ProtNLM2 output. Two reproducible scripts in this folder:

- `compare_sequences_rereview.py` (output `results-rereview.tsv`): fetches sequences from
  UniProt, global Needleman-Wunsch identity to C6T1A2 (BLOSUM62, gap -10/-0.5, identity
  normalised by the shorter sequence), and regex positions of the QALGGH motif and of
  LxLxL / DLNxxP EAR-like motifs.
- `panther_tree_placement_rereview.py` (output `panther_tree_placement_rereview.txt`):
  parses the PANTHER 19 trees (treeinfo API; cached as `panther19_tree_*.json`) for
  PTHR47593 and PTHR45730.

## Sequence features of C6T1A2

- 210 aa, single C2H2 zinc finger (UniProt PROSITE PS50157 feature 79-106).
- The QALGGH motif of plant Q-type C2H2 zinc fingers is present at residues 92-97.
- C-terminal LDLRL at residues 206-210 matches the LxLxL EAR-like repression motif
  pattern; a second LxLxL match (LSLGL, 49-53) lies in the N-terminal region.
- The sequence is identical to soybean A0A2K7G974 (gene name ZFP1) and 99.5% identical
  to Q1H8M0 (zfp1); these are redundant entries for the same or a homeologous locus.

## Pairwise identity to C6T1A2 (global)

| accession | note | identity (%) |
|---|---|---|
| I1K296, A0A0K2CT86 | soybean PTHR47593:SF9 | 85.9 |
| K7KN68 | soybean PTHR47593:SF9 | 64.3 |
| C6SYT9 / K7N376 | soybean PTHR47593:SF8 | 50.0 / 48.2 |
| Q39266 | Arabidopsis ZFP7 | 36.4 |
| Q39263 | Arabidopsis ZFP4 | 37.1 |
| Q39262 | Arabidopsis ZFP3 | 33.8 |
| Q39261 | Arabidopsis ZFP2 | 36.0 |

All the Arabidopsis ZFPs share the QALGGH finger; outside the finger they are divergent
(about 34-37% overall identity), so none is a close sequence relative of C6T1A2.

## PANTHER 19 tree placement

- C6T1A2 (GLYMA_17G165600) is a leaf of the PTHR47593 tree, in subfamily SF9. Its path
  is Magnoliophyta root (PTN005350917, SF8) > Pentapetalae (PTN002402887) > duplication
  PTN002935045 > rosids PTN002521841 (start of SF9) > fabids > Fabales-Rosales >
  duplication PTN002402900 > C6T1A2. SF8 soybean members (C6SYT9, K7N376) descend from
  the other daughter of duplication PTN002935045, so SF8 and SF9 are paralogous lineages
  produced by a Pentapetalae-level duplication.
- The PTHR47593 tree has 75 leaves and contains no Arabidopsis (or other Brassicaceae)
  leaf, and no PAINT node: PTN008158895 and PTN009184003 are absent from it.
- Arabidopsis ZFP7 (Q39266) and ZFP4 (Q39263) are leaves of the PTHR45730 tree, and both
  PAINT nodes listed in `interpro/panther/PTHR47593/PTHR47593-paint.tsv` (PTN008158895,
  GO:0009788; PTN009184003, GO:0005634 and GO:0000976) are nodes of the PTHR45730 tree.
  C6T1A2 is not a leaf of the PTHR45730 tree, so it does not descend from either PAINT node.
- UniProt's PANTHER cross-reference places ZFP7 in PTHR47593:SF8 (HMM scoring), while the
  PANTHER 19 gene-info service and tree place it in PTHR45730 (SF104). The two sources
  disagree on ZFP7's family.

## Conclusion

C6T1A2 has the domain signature of a plant single-finger Q-type C2H2 zinc-finger
transcription factor, which supports DNA-binding transcription factor activity and a
nuclear location at the level of domain inference. It sits in a Pentapetalae-duplicated
PTHR47593:SF9 lineage that has no experimentally characterised member and no PAINT
annotation. The ABA-signalling annotation that PAINT curators placed on the Arabidopsis
ZFP4/ZFP7 node cannot be inherited by C6T1A2, because that node is in a different tree.
