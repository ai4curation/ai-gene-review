# AP1 (APETALA1, At1g69120; UniProt P35631) curation notes

## 2026-10-05 — finishing review (floral_meristem_identity module)

- Resolved the last UNDECIDED row: protein binding IPI with ABS/TT16 (Q8RYD9) from PMID:16080001 (abstract-only).
  The interaction is MADS-MADS and the curator saw the full text, so it is now MODIFY -> GO:0046982
  protein heterodimerization activity, consistent with AP1's other MADS partner rows
  [PMID:16080001 "These data suggest that the formation of multimeric transcription factor complexes might be a general phenomenon among MIKC-type MADS-domain proteins in angiosperms."]
- Three protein binding rows previously MARK_AS_OVER_ANNOTATED (SAP54 phytoplasma effector PMID:24714165;
  CrY2H-seq PMID:28650476; phytoplasma effector screen PMID:37965720) changed to REMOVE per the protein-binding
  policy (no informative AP1-enabled MF follows; removal does not mean the interactions are false).
- AP1 role in the floral_meristem_identity module: floral-fate MADS factor that directly represses SOC1/AGL24/SVP
  [PMID:17428825] and is directly induced by LFY [PMID:10417387] and FT-FD [PMID:16099979].
