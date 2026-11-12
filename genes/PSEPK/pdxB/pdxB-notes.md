# pdxB review notes (P. putida KT2440, Q88L20, PP_2117)

## Provenance

- Sources: reviewed UniProt record (HAMAP MF_01825), the OpenScientist report
  (`pdxB-deep-research-openscientist.md`), and the E. coli ortholog paper
  PMID:20831184 (full text cached). No direct study of PP_2117 exists.

## Decisions (2026-11 completion of the draft)

- GO:0005829 cytosol (TreeGrafter IEA) kept KEEP_AS_NON_CORE, as fixed by the
  TreeGrafter rereview of 2026-09-24; only vetted support was added.
- GO:0005737 cytoplasm changed from KEEP_AS_NON_CORE to MODIFY -> cytosol
  (correct but general; cytosol is on the gene), matching E. coli PdxB. This row
  is not among those listed in the rereview.
- GO:0016491 and GO:0016616 changed from MARK_AS_OVER_ANNOTATED to MODIFY ->
  GO:0033711; GO:0046983 to MODIFY -> GO:0042803 (HAMAP homodimer; P. aeruginosa
  structure). [file:PSEPK/pdxB/pdxB-uniprot.txt "SUBUNIT: Homodimer."]
- GO:0033711 and GO:0036001 core; GO:0008615 accepted.
- The two strings quoted by `interpro/panther/PTHR42938/PTHR42938-review.yaml`
  (description first sentence; GO:0033711 summary) were preserved.
- Removed the GOA-file reference.
