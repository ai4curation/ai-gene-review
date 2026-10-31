# E1BL04 (bovine XIRP2): comparison with characterized Xin-family proteins

Script: `compare_xin_family.py` (run with `uv run python compare_xin_family.py`;
raw output in `compare_xin_family.out`). Sequences are fetched live from UniProt
REST; global pairwise alignment, BLOSUM62, gap open -10, extend -0.5.

## Results (2026-10-20 run)

| Reference | PANTHER subfamily | Length | Identity over aligned | Reference coverage | Ref C-term 300 aa covered |
|---|---|---|---|---|---|
| A4UGR9 human XIRP2 | PTHR22591:SF1 | 3374 | 0.805 | 0.992 | 0.993 |
| Q4U4S6 mouse Xirp2 (isoform 1) | PTHR22591:SF1 | 3784 | 0.707 | 0.860 | 0.047 |
| Q702N8 human XIRP1 | PTHR22591:SF2 | 1843 | 0.378 | 0.916 | 0.833 |
| O70373 mouse Xirp1 | PTHR22591:SF2 | 1813 | 0.359 | 0.949 | 0.957 |

LIM check: a local alignment of the mouse Xirp2 isoform-1 LIM zinc-binding
domain (Q4U4S6 residues 3255-3315) against E1BL04 gave only a 13-residue
alignment with 5 identities (score 33), i.e. no LIM domain is present in E1BL04.

## Interpretation

- E1BL04 is a full-length XIRP2 long (Xin-repeat) product: it covers 99% of
  human XIRP2 (A4UGR9) including both termini, with 80.5% identity, and is far
  less similar to XIRP1 (36-38%), consistent with its PANTHER SF1 placement.
- E1BL04 lacks the C-terminal LIM domain / C-terminal domain (CTD) carried by
  mouse Xirp2 isoform 1 and by the short stereocilia isoform (XEPLIN, isoform 3).
  It therefore corresponds to the LIM-less long isoform class (like human
  A4UGR9 canonical and mouse isoform 2), not to the isoform whose LIM/CTD
  mediates force-dependent recruitment and monomeric gamma-actin enrichment
  at stereocilia gaps (PMID:37294664).
- It is not a fragment. A UniProt search (gene:XIRP2, organism 9913, 2026-10-20)
  returns three unreviewed entries: E1BL04 (3561 aa) and two short products,
  A0AAA9SWG7 (936 aa) and A0AAA9SUE1 (957 aa), which were not analysed here and
  may represent short-isoform gene models. No reviewed (Swiss-Prot) bovine XIRP2
  entry exists, so E1BL04 is the de facto canonical long product.
