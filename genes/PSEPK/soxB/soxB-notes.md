# soxB curation notes

- Q88R11 is the FAD-bearing beta subunit and its UniProt reaction is tetrahydrofolate coupled. [file:PSEPK/soxB/soxB-uniprot.txt, "Rhea:RHEA:70455"]
- KT2440 literature identifies SoxBDAG as the tetrameric enzyme converting sarcosine to glycine. [PMID:35266867, "sarcosine is then converted to glycine and formaldehyde by the tetrameric sarcosine oxidase (SoxBDAG)"]
- SoxB contains the sarcosine-binding FAD site and oxygen-reducing FMN site, so its oxidase annotation remains `enables`; accessory subunits use `contributes_to` [PMID:15946648, "The beta subunit contains dimethylglycine, FAD, and FMN, and these flavins are approximately 10A apart."].
- Recombinant heterotetrameric sarcosine oxidase contains a stable FMN-sulfide
  adduct implicated in electron transfer and oxidase function [PMID:16934831,
  "The results provide definitive evidence for sulfide as the endogenous TSOX ligand"].

## 2026-11-04 review completion

- Provider deep research was not generated in this session (no API keys); cached literature only.
- GO:0008115 is defined by the formaldehyde-forming reaction (EC 1.5.3.1, RHEA:13313). Heterotetrameric
  sarcosine oxidases transfer the oxidised methyl group to tetrahydrofolate and form formaldehyde only
  without folate [PMID:16934831, "In the absence of H 4 folate, turnover occurs at a somewhat slower rate and the sarcosine imine is hydrolyzed to glycine and formaldehyde."].
  The GO:0008115 IEA row was therefore changed from REMOVE/ACCEPT to MODIFY -> NTR
  "sarcosine oxidase (5,10-methylenetetrahydrofolate-forming) activity" (EC 1.5.3.24, RHEA:70455), the
  proposed term shared by soxA/soxB/soxD/soxG (parent GO:0016647, oxygen as acceptor).
- The redundant NEW contributes_to GO:0008115 rows were dropped; the qualifier problem is recorded
  as a WRONG_QUALIFIER source defect on the UniProt row instead (SUSPECTED/CHECK for soxB, which carries
  the flavin sites; PROBABLE for the accessory subunits).
- core_functions use contributes_to GO:0016647 (parent of the proposed term) because the schema's
  proposed_molecular_function implies enables, and no single subunit performs the folate-coupled reaction.
