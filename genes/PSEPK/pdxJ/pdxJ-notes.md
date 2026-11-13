# PdxJ curation notes

## 2026-07-17 OpenScientist retrieval

The gene-level OpenScientist request for PSEPK PdxJ (Q88MY2/PP_1436) reached
the provider's 3600-second service ceiling and was cancelled without producing
a report. No provider-named deep-research file was created. This first-pass
review therefore remains grounded in the exact UniProt reaction and family
record plus the successful module/pathway/taxon OpenScientist report for the
complete DXP-dependent PLP pathway.

## 2026-11 completion

- The OpenScientist file `pdxJ-deep-research-openscientist.md` is present
  (a later run succeeded) and is now cited; it reports no direct study of
  PP_1436 [file:PSEPK/pdxJ/pdxJ-deep-research-openscientist.md "No experimental
  study directly characterizes the *P. putida* KT2440 protein itself"].
- `GO:0016769` changed MARK_AS_OVER_ANNOTATED -> MODIFY to `GO:0033856`
  (the draft argued redundancy with the specific activity).
- `GO:0005737` cytoplasm changed KEEP_AS_NON_CORE -> MODIFY to `GO:0005829`
  cytosol, which the entry carries. The cytosol row itself keeps the
  KEEP_AS_NON_CORE set by projects/TREEGRAFTER/rereview-2026-09-24 (support
  added only).
- NEW `GO:0036001` kept; it matches E. coli PdxJ (NEW, IDA PMID:10225425) and
  the PdxA reviews (GO:0042823 -> GO:0036001).
- GOA-file reference removed. No IBA rows: PAINT IBAs are only shown on
  PANTHER reference proteomes (E. coli P0A794 carries PTN000765245).
