# CASP7 notes

## 2026-09-30

- Seeded and completed the human CASP7 review from cached PubMed records,
  Reactome, UniProt, GOA, GO-CAM models, and the PTHR10454 PAINT context.
- Accepted CASP7's core activity as an Asp-directed cysteine endopeptidase in
  apoptotic execution and kept the broad `GO:0006915 apoptotic process` PAINT
  and TAS rows as `MODIFY` to `GO:0097194 execution phase of apoptosis`.
- Captured the CASP7-specific N-terminal exosite/RNA mechanism from
  PMID:31586028: CASP7 binds RNA and other nucleic acids through lysines in its
  N terminus, and RNA bridges CASP7 to PARP1 and other RNA-binding substrates
  to enhance proteolysis.
- Kept the TNF receptosome and membrane-pore repair branch as a distinct CASP7
  core role: CASP7 proteolytically matures pro-acid sphingomyelinase/SMPD1 in
  support of extracellular ceramide production and membrane repair, represented
  in the local SMPD1 pore-repair GO-CAMs.
- Removed uninformative high-throughput `GO:0005515 protein binding` rows from
  BioPlex and binary interactome screens, while leaving the PMID:11084335 IAP
  row `UNDECIDED` because the cached ML-IAP/BIRC7 abstract does not verify the
  GOA BIRC2-CASP7 edge.
- Removed the CAFA-derived DFF40/CAD catalytic rows that used CASP7 as a
  staurosporine readout in PMID:22253444 rather than establishing CASP7
  nuclease or endopeptidase activity.
- Treated abstract-only or ambiguous papers cautiously: ATP11C cleavage
  (PMID:24904167), p23/telomerase regulation (PMID:19740745), the 2023 GSDMD
  paper (PMID:37327784), and PAK2-dependent CASP7 localization rows
  (PMID:21555521) are `UNDECIDED` where the abstract does not prove a
  CASP7-specific assertion.
- Marked the broad electronic `GO:0009617 response to bacterium` row as
  over-annotated for CASP7 because the supported biology is the more direct
  SMPD1 protein-maturation step downstream of membrane damage.
