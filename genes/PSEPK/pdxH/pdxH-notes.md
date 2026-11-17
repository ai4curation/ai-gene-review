# pdxH review notes (P. putida KT2440, Q88NS5, PP_1129)

## Provenance

- Sources: reviewed UniProt record (HAMAP MF_01629-derived, PE 3), the
  OpenScientist deep-research file, the GO:0042823 hypothesis run in
  `pdxH-hypotheses/`, and E. coli ortholog literature (PMID:11786019).
- No direct study of PP_1129 exists; no IBA rows (PAINT IBAs are shown only on
  PANTHER reference proteomes; E. coli P0AFI7 carries them).
- Orthology: [file:PSEPK/pdxH/pdxH-hypotheses/function-hypothesis-go-0042823/openscientist.md
  "41.5% id to *E. coli* PdxH (and 49.3% to human PNPO)"] (provider alignment).

## Curation decisions (2026-11 completion)

Aligned term by term with genes/ECOLI/pdxH:
- GO:0008615 REMOVE -> MODIFY to GO:0042823 (same claim, wrong process).
- FMN binding KEEP_AS_NON_CORE -> ACCEPT (family consistency: PDX3, PNPO, E. coli).
- GO:0016638 MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0004733 (draft argued redundancy).
- GO:0042816 KEEP_AS_NON_CORE -> TOO_GENERAL (draft argued more specific terms exist).
- GO:0042823 (TreeGrafter IEA) ACCEPT; NEW GO:0036001 and GO:0009443 kept.
- Removed the GOA-file reference.
