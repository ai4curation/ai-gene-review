# EMENI sec11 notes

## Deep Research

No provider deep-research file was present in the seeded sparse worktree. I
searched manually for `Aspergillus nidulans` / `Emericella nidulans` `sec11`,
`AN10354`, `ANIA_10354`, and signal peptidase literature instead of creating a
fake `sec11-deep-research-{provider}.md` file.

The manual search found one organism-specific paper. Schalen et al. 2016
constructed an A. nidulans strain overexpressing `AN10354`, which they describe
as the S. cerevisiae SEC11 ortholog, as part of a 14-gene secretory-pathway
overexpression panel. That supports the locus correspondence and shows that
sec11 dosage has been manipulated in A. nidulans, but it does not directly assay
Sec11 catalytic activity, complex membership, or ER localization. The direct
catalytic model is therefore still a homology/PAINT inference from the conserved
Sec11 family rather than an A. nidulans biochemical result.

Chung et al. 2026 assayed the S. cerevisiae signal peptidase complex and
confirmed that Sec11 is the catalytic subunit of the SPC, has a C-terminal short
helix spanning the ER membrane, and helps productively engage a subset of
internal signal sequences. This is useful mechanistic support for the conserved
Sec11 architecture described in the Q5B8K4 UniProt record.

## PAINT Summary

`PTHR10806-paint.tsv` has three IBD placements:

- `PTN000086749`, root of PTHR10806: `GO:0008233 peptidase activity`. This is
  intentionally broad because the family spans type I signal peptidases outside
  the eukaryotic ER signal peptidase complex. It is true for Q5B8K4 but
  redundant with exact `GO:0009003 signal peptidase activity`, so I marked both
  peptidase-activity rows `TOO_GENERAL`.
- `PTN000086750`, taxon 2759/Eukaryota: `GO:0005787 signal peptidase complex`.
  This is the correct complex call for eukaryotic Sec11; Q5B8K4 is in the
  fungal `PTHR10806:SF6` SEC11 subfamily and has no evidence of loss.
- `PTN000086750`, taxon 2759/Eukaryota: `GO:0051604 protein maturation`. This
  is broader than "signal peptide cleavage" but directly describes the maturation
  of signal-bearing protein precursors by the ER SPC, so I accepted it.

## Annotation Decisions

- Accepted the exact conserved calls for `GO:0009003 signal peptidase activity`,
  `GO:0005787 signal peptidase complex`, `GO:0005789 endoplasmic reticulum
  membrane`, the broader but still correct `GO:0005783 endoplasmic reticulum`,
  and `GO:0051604 protein maturation`.
- Modified `GO:0004252 serine-type endopeptidase activity` to
  `GO:0009003 signal peptidase activity`, and marked `GO:0008233 peptidase
  activity` and `GO:0016020 membrane` as `TOO_GENERAL` because each is entailed
  by a more specific accepted Sec11 term already present in the review.
- Removed the EnsemblFungi transfer to `GO:0045047 protein targeting to ER`.
  Sec11 cleaves signal peptides in the ER membrane after targeting to the
  Sec61/Sec62/Sec63 translocation machinery; it is not known to direct nascent
  chains to the ER.

No new GO annotations or new GO terms are warranted from the available evidence.
