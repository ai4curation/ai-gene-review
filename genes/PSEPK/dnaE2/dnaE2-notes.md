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


## 2026-11-07 — comparative ImuABC annotation audit

MMS-induced mutagenesis in PaW85 and stationary-phase antimutator effects are separate contexts. Replaced blanket nonmutagenic/nonreplicative claims with conditional physiology; current GO places TLS under DNA replication and DNA biosynthesis. Broad true claims refine to supported chemistry/processes. PHP exonuclease is UNDECIDED because the cited loss-of-residues comparison is mycobacterial, not a Q88I82 assay or target alignment. Historical TLS NEW is unchanged.

The genuine existing provider research was read and preserved unchanged; primary sources control conclusions where reports are stale. PAINT-loss checking completed sequentially, but the target is not a leaf in the available cached family tree: loss status is unavailable, not demonstrated absent. Original ordered annotation payloads and historical NEW actions are preserved; no new row is added. Existing notes above are historical and superseded only where this dated audit explains a correction. All original raw, provider and publication bytes remain unchanged.
