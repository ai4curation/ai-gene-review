# MTFMT notes

Literature review was done manually from cached PubMed records; the falcon deep-research report (MTFMT-deep-research-falcon.md) completed afterwards and was skimmed for consistency with the review decisions; no conflicts were found.

- MTFMT formylates part of the mitochondrial Met-tRNA(Met) pool to fMet-tRNA(Met) for initiation [PMID:21907147 "A portion of the Met-tRNA(Met) pool is formylated by mitochondrial methionyl-tRNA formyltransferase (MTFMT) to generate N-formylmethionine-tRNA(Met) (fMet-tRNA(met)), which is used for translation initiation"].
- Patient fibroblasts lose fMet-tRNA(Met) and have a mitochondrial translation defect rescued by MTFMT [PMID:21907147 "Patient fibroblasts exhibit severe defects in mitochondrial translation that can be rescued by exogenous expression of MTFMT."].
- Purified enzyme assays of disease variants [PMID:25288793 "The S125L mutant has 653-fold lower activity, whereas the S209L mutant has 36-fold lower activity."].
- Disease: COXPD15 / Leigh syndrome; recurrent hypomorphic c.626C>T (see dismech entry Combined_Oxidative_Phosphorylation_Defect_Type_15).
- Review decisions: core MF GO:0004479, BP GO:0071951; GO:0006413 modified to GO:0070124 mitochondrial translational initiation.

## Reviewed-row count, and the organelle-level rows

`MTFMT-ai-review.yaml` carries 12 `action:` entries against 13 data rows in `MTFMT-goa.tsv`. The
difference is a genuine GOA duplicate, not an omission: two `located_in GO:0005739` ISS rows share
`GO_REF:0000024`, `WITH/FROM UniProtKB:O77480` and `ASSIGNED BY UniProt`, and differ only in `DATE`
(20240916 and 20211006). They are reviewed as one row.

The four `GO:0005739` mitochondrion rows are `ACCEPT`, and that was examined rather than defaulted.
MTFMT is a matrix protein, `GO:0005759` is this review's core location, and the review carries no
`GO:0005759` annotation row — so refining `GO:0005739` to `GO:0005759` was tried, and it does clear
the standing `core_functions.locations` traceability warning, because `proposed_replacement_terms`
counts toward that check. It was reverted for a different reason: one of the four rows is an IBA, and
a `MODIFY` on a propagated row draws a `propagation_review` requirement that has to rest on inspected
PAINT evidence for this family, which has not been inspected. Refining three of the four and leaving
the IBA would put one term under two actions in one file, which is the inconsistency this review set
has been removing. The rows therefore stay `ACCEPT`, their reasons do not argue that the term is too
general, and whether organelle-level rows should be refined wherever a compartment term is
established is left as the systemic question.
