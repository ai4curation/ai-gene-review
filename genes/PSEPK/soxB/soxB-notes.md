# soxB curation notes

- Q88R11 is the FAD-bearing beta subunit and its UniProt reaction is tetrahydrofolate coupled. [file:PSEPK/soxB/soxB-uniprot.txt, "Rhea:RHEA:70455"]
- KT2440 literature identifies SoxBDAG as the tetrameric enzyme converting sarcosine to glycine. [PMID:35266867, "sarcosine is then converted to glycine and formaldehyde by the tetrameric sarcosine oxidase (SoxBDAG)"]
- SoxB contains the sarcosine-binding FAD site and oxygen-reducing FMN site, so its oxidase annotation remains `enables`; accessory subunits use `contributes_to` [PMID:15946648, "The beta subunit contains dimethylglycine, FAD, and FMN, and these flavins are approximately 10A apart."].
- Recombinant heterotetrameric sarcosine oxidase contains a stable FMN-sulfide
  adduct implicated in electron transfer and oxidase function [PMID:16934831,
  "The results provide definitive evidence for sulfide as the endogenous TSOX ligand"].

## 2026-11-04 review completion

- Provider deep research was not generated in this session (no API keys); cached literature only.
- Aligned with the CORS9 Sox reviews and the module (orchestrator decision): GO:0008115 (defined by the
  formaldehyde-forming reaction, EC 1.5.3.1/RHEA:13313) is KEEP_AS_NON_CORE, a real conditional folate-free
  activity [PMID:16934831, "In the absence of H 4 folate, turnover occurs at a somewhat slower rate and the sarcosine imine is hydrolyzed to glycine and formaldehyde."].
  enables kept (SoxB carries the FAD substrate site); no qualifier defect.
- Core function uses proposed_molecular_function "sarcosine oxidase (5,10-methylenetetrahydrofolate-forming) activity"
  (EC 1.5.3.24, RHEA:70455; proposed parent GO:0016647), in_complex GO:0032921, location cytoplasm.
- Earlier draft NEW contributes_to GO:0008115 rows were dropped (the qualifier issue is a source defect).
