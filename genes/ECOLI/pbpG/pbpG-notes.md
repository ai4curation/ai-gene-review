# pbpG (ECOLI, UniProt P0AFI5) curation notes

## 2026-11-04 (Claude, AI-assisted)

- Review written for the module `low_molecular_mass_pbp_peptidoglycan_hydrolysis`
  (PBP7 representative member).
- Provider deep research was not run: no deep-research API keys are configured in
  this session. The review is based on the UniProt record, the GOA rows and the
  cached publications for every GOA reference (abstracts, plus full text where
  `full_text_available: true`).
- GO term definitions used in reasons (GO:0006508, GO:0061785, GO:0004252,
  GO:0004185, GO:0009002, GO:0042597/GO:0030288) were checked against QuickGO.
- Cross-gene consistency: GO:0006508 proteolysis is REMOVEd and generic
  peptidase/carboxypeptidase/periplasm rows are MODIFYed to GO:0061785,
  GO:0009002 and GO:0030288 in the same way across the PBP4 (E. coli, P.
  aeruginosa, P. putida) and PBP7 (E. coli, P. putida) reviews.

## 2026-11-04, PR #5959 review follow-up

- Recorded the GO:0006508 InterPro2GO removal (IPR001967, IPR018044) as a source_defect.
