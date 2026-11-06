# PP_3117 / ImuA curation notes

- PP_3117 is the ImuA component of the LexA2-regulated damage-inducible cassette. [PMID:15458417, "these genes constitute a DNA damage-inducible operon"]
- Ortholog genetics establishes ImuA, ImuB, and DnaE2 as one functional unit. [PMID:15886391, "all three genes that compose this expression unit are involved"]
- No catalytic activity is assigned to ImuA; its direct interaction mechanism remains unresolved.

## Completion pass (ImuABC module curation)

- Status set to COMPLETE. Every row now carries a vetted quote.
- The GO:0051782 (negative regulation of cell division) row is REMOVEd and recorded as a
  source defect. Its GOA WITH/FROM is `InterPro:IPR004596` (Cell division suppressor
  protein, SulA), but the protein's current InterPro signatures are IPR047610
  (ImuA_translesion) plus IPR017166, and NCBIfam NF033429 ImuA_translesion. InterPro's own
  IPR047610 description records that this protein "was previously misnamed SulA in
  Pseudomonas putida", which is the legacy the annotation preserves.
- The DNA repair row's route is TreeGrafter (GO_REF:0000118, grafting node
  PANTHER:PTN009155960), not a PAINT IBA.
- GO:0019985 (not the mutagenic child GO:0042276) is used for KT2440, because in this
  organism DnaE2 is an anti-mutator for stationary-phase base substitutions.
  [PMID:17331811, "it acted as an anti-mutator in accumulation of base substitution"]
  The Caulobacter and M. tuberculosis reviews use GO:0042276, where induced mutagenesis is
  demonstrated for the whole cassette.
- No provider deep research exists for this gene (no -deep-research-*.md file).
