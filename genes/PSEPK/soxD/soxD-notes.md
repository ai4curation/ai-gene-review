# soxD curation notes

- Q88R10 is the small delta subunit of tetrameric sarcosine oxidase. [file:PSEPK/soxD/soxD-uniprot.txt, "DR   InterPro; IPR006279; SoxD."]
- KT2440 literature identifies SoxBDAG as the tetrameric enzyme converting sarcosine to glycine. [PMID:35266867, "sarcosine is then converted to glycine and formaldehyde by the tetrameric sarcosine oxidase (SoxBDAG)"]
- SoxD contributes to complex activity rather than independently enabling it.
- The characterized delta subunit coordinates structural zinc through a Cys3His motif [PMID:15946648, "The delta subunit contains a single atom of zinc and has a Cys(3)His zinc finger structure."].

## 2026-11-04 review completion

- Provider deep research was not generated in this session (no API keys); cached literature only.
- Aligned with the CORS9 Sox reviews and the module (orchestrator decision): GO:0008115 (defined by the
  formaldehyde-forming reaction, EC 1.5.3.1/RHEA:13313) is KEEP_AS_NON_CORE, a real conditional folate-free
  activity [PMID:16934831, "In the absence of H 4 folate, turnover occurs at a somewhat slower rate and the sarcosine imine is hydrolyzed to glycine and formaldehyde."].
  WRONG_QUALIFIER source defect (enables -> contributes_to) recorded on the UniProt row.
- Core function uses proposed_molecular_function "sarcosine oxidase (5,10-methylenetetrahydrofolate-forming) activity"
  (EC 1.5.3.24, RHEA:70455; proposed parent GO:0016647), in_complex GO:0032921, location cytoplasm.
- Earlier draft NEW contributes_to GO:0008115 rows were dropped (the qualifier issue is a source defect).
