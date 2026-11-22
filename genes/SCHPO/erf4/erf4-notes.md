# erf4 notes

## PTHR13254 fungal Erf4/GOLGA7 review, 2026-11-22

- Reviewed fission-yeast erf4 against the current PTHR13254 PAINT slice and
  the 2023 S. pombe palmitoyltransferase paper [PMID:36650056].
- Removed the PomBase root molecular-function ND row as stale because the same
  record now carries conserved Erf4/GOLGA7 PAINT assertions and the 2023 paper
  directly showed that Erf2-Erf4 is required for Ras1 palmitoylation and mating
  localization.
- Accepted `GO:0006612 protein targeting to membrane` from the PTHR13254 root
  IBD: the S. pombe complex keeps Ras1 at the cell periphery and conjugation
  site.
- Modified the `GO:0031211 endoplasmic reticulum palmitoyltransferase complex`
  IBA to generic `GO:0002178 palmitoyltransferase complex`. The IBD is seeded
  by ER-localized S. cerevisiae Shr5; the 2006 ORFeome also reported direct
  S. pombe ER signal, but a later focused fission-yeast study imaged
  nmt1-driven Erf2-Erf4 at Golgi and cell-periphery sites.
- Added the curated primary fission-yeast references PMID:16303567 and
  PMID:23843742, using the 2013 work to ground protein-palmitoylation evidence
  and the S. pombe functional-orthology bridge to S. cerevisiae Erf4.
