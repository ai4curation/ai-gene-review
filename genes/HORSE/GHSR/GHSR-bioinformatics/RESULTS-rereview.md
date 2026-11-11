# GHSR horse F6QF00: motif and curated-site check (2026-10-20 re-review)

Script: `motif_check_rereview.py` (standard-library Python; reads the cached UniProt records). Raw output: `motif_check_rereview.out`.

## Findings

- Human Q92847 and horse F6QF00 are both 366 aa and differ at 18 positions (gapless, consistent with `alignment.txt`). Most substitutions lie in the N-terminal extracellular segment (positions 12-36) and the C-terminal tail (336, 341). Two fall in extracellular loop 2 (W193Q, P200A), adjacent to but not at the C116-C198 disulfide.
- The class A GPCR motifs are at identical positions in both: the E/DRY motif at 140 (GHSR has ERY, not DRY, in both species), CWxP at 275 (TM6), and NPxxY at 319 (TM7).
- Every curated human site in the record is conserved in horse: the C116-C198 disulfide, the ligand-contact BINDING residues 178, 181, 213, 214 and 286, and the N-glycosylation sites N13 and N27.

## Interpretation and limits

F6QF00 is a complete GHSR type 1a product, not a fragment or alternative model. The ERY motif probably explains the PROSITE-ProRule PRU00521 "lacks conserved residue(s)" caution on the unreviewed horse record. It is shared with the experimentally characterised human receptor, so it does not suggest loss of function. This is a positional sequence comparison. It does not assay equine ligand binding, and the ECL2 substitutions have not been tested.
