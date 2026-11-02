# SPAC25B8.09 (Q9UTA9) re-review: PTHR44942:SF4 members in the two yeasts

Script: `compare_sf4_yeast_members.py` (PEP 723; run with `uv run --script`).
Raw output: `results_sf4_pairwise.json`.

## Membership (UniProt PANTHER cross-references, queried 2026-10-21)

PTHR44942:SF4 has two members in each yeast:
S. pombe Q9UTA9 (SPAC25B8.09, 251 aa) and its tandem neighbour Q9UTA8 (SPAC25B8.10, 256 aa);
S. cerevisiae P32643 (TMT1, 299 aa) and P38892 (CRG1, 291 aa).
The official PANTHER 19.0 per-organism file places Q9UTA9 in PTHR42912:SF95 instead
(see interpro/panther/panther-members-overrides.tsv).

## Pairwise global identity (BLOSUM62, gap -10/-0.5)

| Pair | % identity (aligned columns) | score |
|---|---|---|
| Q9UTA9 vs Q9UTA8 | 68.1 | 884.5 |
| P32643 TMT1 vs P38892 CRG1 | 36.2 | 384.5 |
| Q9UTA9 vs TMT1 | 25.6 | 112.5 |
| Q9UTA9 vs CRG1 | 29.1 | 104.0 |
| Q9UTA8 vs TMT1 | 25.5 | 104.0 |
| Q9UTA8 vs CRG1 | 28.3 | 126.5 |

## Interpretation

- The two fission-yeast genes are a recent, lineage-specific tandem duplication (68% identity).
- Each fission-yeast gene is about equally distant (25-29% identity) from TMT1 and from CRG1.
  Pairwise similarity does not single out TMT1 as a one-to-one ortholog of SPAC25B8.09.
  The relationship is at best a 2:2 co-orthology group within SF4.
- SF4 also contains fungal natural-product O-methyltransferases (e.g. ptaH, nsrG, cfoB,
  pgmE in interpro/panther/PTHR44942/PTHR44942-entries.csv), so SF4 membership by itself does
  not imply a particular acceptor such as trans-aconitate.
- This is a pairwise analysis, not a tree; it cannot resolve whether the TMT1/CRG1 duplication
  predates the Saccharomyces/Schizosaccharomyces split. The result is inconclusive on acceptor
  specificity and supports only the shared SAM-dependent methyltransferase fold.
