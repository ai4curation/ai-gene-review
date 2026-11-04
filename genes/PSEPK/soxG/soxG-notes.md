# soxG curation notes

- Q88R08 is the gamma subunit of tetrameric sarcosine oxidase. [file:PSEPK/soxG/soxG-uniprot.txt, "DR   InterPro; IPR006280; SoxG_het."]
- KT2440 literature identifies SoxBDAG as the tetrameric enzyme converting sarcosine to glycine. [PMID:35266867, "sarcosine is then converted to glycine and formaldehyde by the tetrameric sarcosine oxidase (SoxBDAG)"]
- SoxG contributes to complex activity rather than independently enabling it.

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
