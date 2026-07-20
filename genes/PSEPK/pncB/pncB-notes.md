# pncB curation notes

## 2026-07-20

- Target identity: PP_4868 / reviewed UniProtKB Q88DF7, NAPRTase-family PncB
  [UniProtKB:Q88DF7, "Belongs to the NAPRTase family."].
- Reaction: ATP-coupled phosphoribosylation of nicotinate and PRPP yields NaMN,
  ADP, phosphate, and diphosphate [UniProtKB:Q88DF7,
  "Reaction=5-phospho-alpha-D-ribose 1-diphosphate + nicotinate + ATP + H2O = nicotinate beta-D-ribonucleotide + ADP + phosphate + diphosphate"]
  [RHEA:36163, nicotinate phosphoribosyltransferase reaction].
- Family grounding: the target has a PTHR11098:SF1 nicotinate
  phosphoribosyltransferase cross-reference, and E. coli PncB P18133 is retained
  as a representative exemplar; no ancestral PTN is asserted
  [UniProtKB:Q88DF7, "PANTHER; PTHR11098; NICOTINATE
  PHOSPHORIBOSYLTRANSFERASE; 1."].
- Curation: all four seeded annotations are consistent with direct nicotinate
  salvage through the Preiss-Handler route.
- OpenScientist independently recovered the ATP-coupled RHEA:36163 chemistry
  and conserved NAPRTase architecture. Its generic PncA/NiaP nicotinamide-entry
  diagram and rate-limiting claim are not established for KT2440: the proteome
  search found no canonical PncA, and Q88DF7 itself only establishes direct
  nicotinate entry. Those extensions were not added to the review
  [file:PSEPK/pncB/pncB-deep-research-openscientist.md,
  "No direct assay of the P. putida KT2440 enzyme."].
