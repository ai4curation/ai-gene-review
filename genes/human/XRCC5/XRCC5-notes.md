# XRCC5 notes

## 2026-11-21

Deep-research providers were not available in this checkout. `just deep-research-falcon
human XRCC5 --fallback perplexity-lite` reported that only `claude_code` was available,
and `just deep-research human XRCC5 claude-code --timeout 300` failed because the
Claude Code provider was not logged in. This review therefore uses the fetched GOA rows,
UniProt, cached publications, PANTHER/PAINT files, and the existing
`modules/nonhomologous_end_joining.yaml` review.

PTHR12604 is a compact Ku family. In human reviewed Swiss-Prot it contains XRCC5
(Ku80, PTHR12604:SF4) and XRCC6 (Ku70, PTHR12604:SF5). Both contribute to the
Ku70:Ku80 ring that binds broken double-stranded DNA ends, recruits DNA-PKcs,
and starts classical non-homologous end joining. The existing
`modules/nonhomologous_end_joining.yaml` ModuleReview already models this as the
`ku_end_binding` step, with XRCC5 and XRCC6 as active units of the Ku heterodimer,
so no module edit is needed in this family PR.

PAINT places five positive PTHR12604 assertions at PTN000288287: Ku70:Ku80
complex, double-stranded DNA binding, telomeric repeat DNA binding, telomere
maintenance, and NHEJ. A Drosophila node, PTN000288402, carries IRDs for the same
terms. `just paint-losses human XRCC5` reported no IRD/IKR loss on the human XRCC5
lineage, so the human IBA rows are retained.

Review calls:

- Retain the Ku heterodimer, DNA end-binding, telomeric-repeat binding, NHEJ, and
  nuclear/site-of-damage rows as the central DNA-repair and telomere-protection
  biology of XRCC5.
- Keep direct ATPase, AP lyase, and DNA helicase rows as non-core biochemical
  activities. They are experimentally observed for Ku preparations or individual
  subunits but are subordinate to the heterodimer's evolved DNA-end recognition
  role.
- Keep the rRNA/U3 snoRNA/small-subunit processome rows from PMID:32103174 as
  non-core. They report a Ku-dependent, c-NHEJ-independent DNA-PKcs function in
  rRNA processing, but the Ku family review should not move that side context
  into the family-wide PAINT scope.
- Treat cytosolic DNA sensing and promoter/transcription rows as peripheral or
  over-annotated. The Reactome cytosolic DNA-PK event itself says it is unclear
  whether all DNA-PK subunits are critical for exogenous DNA recognition or act
  as a holoenzyme, and no production GO-CAM in the cache covers Ku in core
  c-NHEJ.
- Remove the IntAct and ComplexPortal `GO:0005515` rows under the generic
  protein-binding policy; no specific replacement is proposed for these
  high-volume physical-interaction imports.
