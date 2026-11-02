# grim apoptosis curation notes

## 2026-09-30

- Reviewed all 23 seeded FlyBase GOA rows for `grim` using the local UniProt record and cached publications.
- Treated Grim as an RHG/IAP antagonist with two separable pro-apoptotic regions:
  an N-terminal IAP-binding motif that binds IAP BIR domains and a GH3 amphipathic
  helix that supports mitochondrial apoptotic changes.
- Downcasted generic `GO:0006915 apoptotic process` and `GO:0012501 programmed
  cell death` rows to `GO:0097190 apoptotic signaling pathway` where the source
  assayed Grim as the upstream pro-death trigger.
- Replaced the generic DIAP2 `GO:0005515 protein binding` row with
  `GO:1990525 BIR domain binding`; Ribeiro et al. directly state that Rpr and
  Grim preferentially bind the BIR2 domain of DIAP2 [PMID:18166655].
- Broadened the `GO:0005759 mitochondrial matrix` row to
  `GO:0005739 mitochondrion`; Claveria et al. used a matrix marker to show that
  Grim-positive rings are mitochondria associated, not that Grim enters the
  matrix [PMID:12093734].
- Broadened `positive regulation of release of cytochrome c from mitochondria`
  to `GO:0008637 apoptotic mitochondrial changes` because the same paper reports
  no substantial free cytochrome-c release into the cytosol in Grim-expressing
  Drosophila cells, only cytochrome-c redistribution into Grim-positive puncta
  [PMID:12093734].
- Kept Malpighian tubule nuclear localization and neuronal/glial developmental
  death rows as non-core or context-specific: they are real deployments or
  restraint contexts of the Grim program rather than separate molecular
  activities.
- Left rows from abstract-only papers `UNDECIDED` when the visible cache did not
  expose Grim-specific evidence, notably lifespan, melanization, larval CNS
  remodeling, plasma membrane, and one Sickle-paper top-level apoptosis row.
