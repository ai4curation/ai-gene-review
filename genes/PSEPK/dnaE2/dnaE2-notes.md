# dnaE2 / ImuC curation notes

- DnaE2 is the polymerase-active component of the cassette; catalytic-residue substitution phenocopies deletion in the orthologous system. [PMID:20615954, "replacement of DnaE2 catalytic residues reproduces the dnaE2 gene"]
- P. putida DnaE2 has context-dependent mutation effects and can act as an anti-mutator for stationary-phase base substitutions. [PMID:17331811, "it acted as an anti-mutator in accumulation of base substitution"]
- P. putida ImuC/DnaE2 contributes to methylation-damage tolerance. [PMID:28118378, "polymerases ImuC and DinB ensured a protective role against N- and O-methylation"]

## Completion pass (ImuABC module curation)

- Status set to COMPLETE. Every row now carries a vetted quote.
- GO:0008408 (3'-5' exonuclease activity) was UNDECIDED; resolved to
  MARK_AS_OVER_ANNOTATED on the published PHP-residue comparison, which shows DnaE1 retains
  the exonuclease residues while they are absent in DnaE2.
  [PMID:20615954, "The corresponding domain of Mtb DnaE1 retains all amino acids associated with exonuclease activity ( 34 – 36 ), whereas key residues are absent in DnaE2."]
  No DnaE2 exonuclease assay exists, so the row is flagged rather than removed.
- GO:0006260 (DNA replication) over-annotation is argued from the HAMAP function statement
  plus the missing C-terminal clamp-loader-binding region of DnaE2 proteins.
- KT2440 retains GO:0019985; the mutagenic child GO:0042276 is used only in the Caulobacter
  and mycobacterial reviews. See the PP_3117 notes for the reasoning.
