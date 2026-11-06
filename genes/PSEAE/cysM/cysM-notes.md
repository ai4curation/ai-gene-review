# cysM (P. aeruginosa PAO1, PA0932, Q9I526) curation notes

## 2026-11-03 review (cysteine biosynthesis module promotion)

Deep research: no provider deep-research run was possible in this session (no
provider API keys). The review rests on two full-text papers on this protein,
the UniProt entry (PE 3, homology-inferred), and the local PTHR10314 PAINT table.

- Substrates: [PMID:41541697 "PA2709 is reactive only with the OAS+bisulfide
  substrate couple, while PA0932 is reactive with both OAS+bisulfide and
  OAS+thiosulfate couples."] and classification as EC 2.5.1.144
  [PMID:41541697 "while PA0932 is also a S-sulfocysteine synthase
  (O-acetyl-L-serine-dependent) (EC 2.5.1.144)"].
- Independent confirmation of thiosulfate specialization [PMID:41676964
  "Growth phenotypes further indicated that PaCysK primarily supports
  sulfide‐dependent cysteine biosynthesis, whereas PaCysM is specialized for
  thiosulfate utilization, consistent with their distinct catalytic
  properties."].
- Redundancy: [PMID:41541697 "Deletion of either one of the two genes does not
  lead to cysteine auxotrophy, which is reached only with the double deletion
  mutant."].
- PLP stoichiometry measured on the purified enzyme (PMID:41676964); added as a
  NEW non-core PLP binding row, matching the E. coli CysM review.
- GO has no MF term for the thiosulfate reaction (label search for
  "sulfocysteine"/"sulfo-L-cysteine"/"thiosulfonate" found only obsolete
  GO:0019345), so it is a proposed new term and a core function via
  proposed_molecular_function.
- Generic catalytic activity (ARBA) is TOO_GENERAL; cytoplasm IBA refined to
  cytosol, consistent with the module siblings.
- PANTHER: PTHR10314:SF162 (CYSTEINE SYNTHASE B), same subfamily as E. coli
  CysM; IBA from PTN008497439. No PAINT loss on its lineage
  (`just paint-losses PSEAE cysM`).

## 2026-11-03 PR #5929 review round

- Cytoplasm -> cytosol MODIFY reason now states that the refinement is an inference from solubility plus the PAINT node, not a localization measurement.
- The NEW PLP-binding row now leads with the one-PLP-per-monomer measurement.
