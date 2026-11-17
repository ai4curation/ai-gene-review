# epd review notes (P. putida KT2440, Q88D63, PP_4964)

## Provenance

- Sources: the UniProt record (unreviewed, PE 3), the OpenScientist deep
  research file (`epd-deep-research-openscientist.md`), and the cached E. coli
  ortholog papers PMID:7751290, PMID:9182530, PMID:9696782 (abstract-only).
- The deep-research report records that no direct study of PP_4964 exists.
  [file:PSEPK/epd/epd-deep-research-openscientist.md "There is no published
  biochemical, structural, or genetic characterization of the *P. putida*
  KT2440 Epd protein itself."]

## Decisions (2026-11 completion of the draft)

- GO:0048001 accepted as core, from the Epd-specific family models and the
  E. coli ortholog. [PMID:7751290 "We found that the gapB-encoded enzyme is
  indeed an E4PDH and not a second GA3PDH"]
- GO:0016620 changed from MARK_AS_OVER_ANNOTATED to MODIFY -> GO:0048001
  (correct but general), matching the E. coli review.
- GO:0042823 changed from KEEP_AS_NON_CORE to MODIFY -> GO:0036001, matching
  the E. coli review; GO:0036001 kept as the NEW core process.
- GO:0008615 accepted (GO's term for the UniPathway PNP branch).
- Cytoplasm KEEP_AS_NON_CORE (no cytosol row on this protein).
- This protein carries no GAPDH (GO:0004365) or glucose metabolism rows; the
  E. coli review removes those as noise-level/over-propagated, so the two
  orthologs are consistent.
- The draft's reference to the GOA tsv was removed (a GOA file is never support).
