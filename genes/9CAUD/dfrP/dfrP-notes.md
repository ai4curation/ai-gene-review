# dfrP (D0VXF2) notes: Bacillus phage phiNIT1 dihydrofolate reductase

## 2026-10-01: GOA refresh (PR #3503)

- **Gene symbol.** As of the 2026-07-27 GOA release (and UniProt `GN Name=orf168`),
  this protein's symbol is `orf168`. The review keeps `gene_symbol: dfrP` because
  that is the gene-directory name and the name used in the deep research. This
  differs from 9CAUD/g022, whose symbol *was* synced to GOA: there the old value
  was the UniProt accession, a placeholder rather than a gene name. Revisit if
  the directory is ever renamed.
- **TreeGrafter rows retired.** GO:0046452 (dihydrofolate metabolic process,
  previously ACCEPT) and GO:0046655 (folic acid metabolic process, previously
  KEEP_AS_NON_CORE) no longer come from TreeGrafter (GO_REF:0000118) for this
  viral protein. See the 2026-09-29 note in projects/TREEGRAFTER.md.
- **GO:0046452 re-asserted as NEW (ISS).** Its replacement in GOA,
  GO:0046654 tetrahydrofolate biosynthetic process, is a *sibling* under
  GO:0006760 folic acid-containing compound metabolic process, not an
  ancestor, so the dihydrofolate-side statement would otherwise be lost. The
  comparator check supports it. The PAINT IBD for GO:0046452 sits on the family
  root node PTN000167322 in PTHR48069, seeded by rat Dhfr (RGD:2500), yeast DFR1
  (SGD:S000005762) and human DHFR (P00374). *E. coli* folA (P0ABQ4) carries it
  by IBA as a descendant (folA seeds GO:0046654, not this term). dfrP is in the
  same subfamily as folA (PTHR48069:SF3).
  GO:0046655 was allowed to lapse as a broad parent.
