# E. coli leuC (P0A6A6) curation notes

Provider deep research was not run for this gene. These notes record the
literature read for the review (cached abstracts under `publications/`).

- The isomerase is a LeuC-LeuD complex [PMID:374346 "isomerase, a complex of the leuC and leuD gene product."]; in Salmonella both subunits copurify and leuC and leuD extracts complement in vitro [PMID:7026530 "in vitro complementation of cell-free extracts of leuC and leuD mutant strains was demonstrated"].
- Co-expressed E. coli leuC and leuD complement yeast leu1 [PMID:23636690].
- [4Fe-4S] enzyme inactivated by micromolar H2O2 [PMID:17102132 "The oxidized cluster then degraded to a catalytically inactive [3Fe-4S] form."].
- Qualifier decision: GO:0003861 is the activity of the heterodimer, so the
  LeuC rows are reviewed as `contributes_to` (core_functions uses
  `contributes_to_molecular_function`) and the UniProt `enables` IEA row
  carries a CONFIRMED WRONG_QUALIFIER source defect. Same treatment as
  PSEPK leuC and all LeuD reviews (ECOLI, SALTY, PSEPK).
- The module function-conformance check therefore reports CONTRIBUTES_ONLY
  for this representative; it becomes CONTRIBUTES_IN_COMPLEX if the module
  models LeuC and LeuD as active units of a protein complex.
