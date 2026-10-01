# ORC1 IBA and literature re-review notes

## 2026-09-28 IBA/new-literature re-review

- Current ORC1 GOA has four `GO_REF:0000033` IBA rows in PANTHER family `PTHR10763`.
- `PANTHER:PTN000080056` is the ORC1-family node carrying both `GO:0003688 DNA
  replication origin binding` and `GO:0006270 DNA replication initiation`. Both transfer
  correctly to budding-yeast Orc1 and are supported by direct yeast origin-recognition and
  pre-RC-assembly evidence.
- `PANTHER:PTN000080057` carries `GO:0005664 nuclear origin of replication recognition
  complex`; this is also a correct core transfer because yeast Orc1 is an established
  structural subunit of the nuclear ORC.
- The `GO:0033314 mitotic DNA replication checkpoint signaling` IBA should not be kept:
  PMID:16716188 supports failed replication initiation and downstream DNA-damage/spindle
  checkpoint arrest after ORC inactivation, not a direct checkpoint-signaling role for Orc1.
  The local `PTHR10763` PAINT cache also has no `GO:0033314` IBD row at any node, so the
  GOA row appears stale or absent relative to the cached PAINT source. This is a
  role-conflation/term-scoping problem in the annotation itself, but the source status is
  `SOURCE_STALE_OR_MISSING` for the cached node.
- New 2024 primary paper PMID:38597680 is now cached with PMC full text. It refined the
  Orc1 origin-binding model by mapping 38 designed ORC mutants in vivo and showing that
  Orc1-BP4/BP3 basic patches and Orc4-IH differentially support classes of origin motifs,
  while the Orc1 BAH domain explains ORC binding at motif-lacking silencing-associated
  sites.
- The nine `GO:0005515 protein binding` IPI rows were changed from `KEEP_AS_NON_CORE` to
  `REMOVE` or `MODIFY`. The reported physical associations are not being disputed, but a bare
  protein-binding term does not describe ORC1's function when ORC-complex membership, origin
  binding, pre-RC assembly and silent-locus heterochromatin formation are already curated. The
  exception is the PMID:8622770 Orc1-Sir1 row, where the interaction supports a more informative
  chromatin-protein adaptor activity.

## 2026-10-01 current GOA refresh

- `just fetch-gene yeast ORC1 --force` refreshed ORC1 from 48 historical GOA-derived rows
  to 43 current GOA rows, with five newly seeded rows retained for review and ten historical
  rows kept as `retired: true`.
- Current PTHR10763 PAINT is stable relative to the 2026-09-28 check: PTN000080056 carries
  `GO:0003688` and `GO:0006270`, PTN000080057 carries `GO:0005664`, PTN000080129 carries
  `GO:0005634`, and no current PAINT node carries the stale checkpoint-signaling IBA.
- The three new `GO:0005515` rows are IntAct exact-source splits for Orc4 interactions from
  PMID:16429126, PMID:22405012, and PMID:37968396. Like the older Orc6 rows from the same
  papers, they were removed as generic protein-binding annotations rather than disputed as
  physical interactions.
- The new InterPro2GO `GO:0005524 ATP binding` row from `IPR003959` was accepted as a direct
  AAA+ ATPase-core mapping that matches direct yeast ATP-binding evidence, and the new
  ComplexPortal `GO:0005664` row from PMID:27148210 was accepted as redundant direct support
  for Orc1's membership in the yeast ORC heterohexamer.
- New full-text PMID:42100701 was cached from PMC. Kawakami et al. 2026 mapped an Orc1
  ISM-related region that restrains ORC-ssDNA binding and helps maintain origin specificity;
  this refines the core `GO:0003688 DNA replication origin binding` model but does not justify
  adding a separate ssDNA-binding function.
