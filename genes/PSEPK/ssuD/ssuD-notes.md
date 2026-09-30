# ssuD curation notes

## Molecular function and PAINT provenance

- The exact substrate-specific term is GO:0008726 alkanesulfonate
  monooxygenase activity. The broad GO:0016705 oxygenase parent is therefore
  `MODIFY` to GO:0008726, which already exists as a separate accepted GOA row;
  downstream curation should not create a duplicate annotation.
- The GOA row carries PANTHER:PTN002450490 as TreeGrafter provenance. The local
  canonical PTHR42847 PAINT table instead identifies ancestral node
  PTN000768559, seeded by E. coli SsuD P80645, for GO:0008726 and GO:0046306.
  These identifiers describe different provenance objects and are not
  interchangeable.

## Localization restraint

The Falcon report calls a cytosolic site "most consistent" with the reaction
context [file:PSEPK/ssuD/ssuD-deep-research-falcon.md, "most consistent with a
**cytosolic** site of reaction"], but the exact Q88R95 UniProt record has no
subcellular-location assertion and no target-specific localization experiment
was identified. No cellular-component annotation is proposed from this indirect
context alone.
