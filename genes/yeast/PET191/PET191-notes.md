# PET191 curation notes

## IBA / PAINT

- The pinned GOA snapshot has two `GO_REF:0000033` rows, both with
  `PANTHER:PTN002007797` in `WITH/FROM`.
- Current local PAINT for `PTHR28627` still places those same IBD assertions on
  `PTN002007797`: `GO:0005739` mitochondrion, seeded by yeast Pet191 and human
  COA5, and `GO:0033617` mitochondrial respiratory chain complex IV assembly,
  seeded by yeast Pet191 itself.
- The broad mitochondrion IBA is a valid non-core localization; the more
  specific mitochondrial intermembrane space and inner-membrane association rows
  carry the precise sites.
- The complex IV assembly IBA is a core no-failure transfer. The target's own
  `SGD:S000003795` source is expected because direct yeast Pet191 evidence was
  used to place the ancestral PAINT assertion.

## Cached Literature

- PMID:8381337 is the founding genetic paper: PET191 is required to assemble
  active cytochrome c oxidase, but its product is not a subunit of the final
  enzyme.
- PMID:18503002 establishes Pet191 as a twin-CX9C complex IV assembly factor
  whose motif cysteines support function and disulfide-linked incorporation into
  a large inner-membrane-associated oligomeric complex. Its abstract also
  reported Mia40-independent import, but that import model is now disputed:
  [PMID:22984289 "We tested the protein levels of Cox12 and Pet191 in wild-type
  and mia40–3 mitochondria by immunoblotting and found a significant reduction
  of both proteins in the mutant mitochondria relative to the wild-type (Fig.
  5A). The levels of other mitochondrial proteins that are MIA-independent
  remained unchanged (Fig. 5A)."]
- PMID:22984289 supports the mitochondrial intermembrane-space localization by
  Bax-release IMS proteomics and Pet191-specific protease protection.
- PMID:16823961 and PMID:24769239 are high-throughput mitochondrial proteome
  rows and do not add Pet191-specific mechanistic evidence in the cached text.

## 2024-2026 Literature Check

- The only recent PubMed hit for PET191/COA5 in the cytochrome c oxidase
  literature is the 2025 human COA5 complexome study, PMID:39779219. It supports
  an early complex IV assembly role for human COA5, especially around MTCO2
  biogenesis and incorporation: [PMID:39779219 "Mitochondrial complexome
  profiling pinpointed a role of COA5 in early CIV assembly, more specifically,
  its involvement in the stage between MTCO1 maturation and the incorporation of
  MTCO2"]. This is consistent with, rather than corrective of, the yeast PAINT
  transfer.

## 2026-10-01 current-GOA sweep

- Refreshed UniProt/GOA and found the same ten live GOA rows: two PTHR28627
  IBA rows, one SubCell intermembrane-space IEA, two direct complex-IV assembly
  IMP rows, one direct intermembrane-space IDA, one direct inner-membrane IDA,
  two high-throughput mitochondrial HDA rows, and the SGD molecular-function ND
  placeholder.
- Refetched the `PTHR28627` PAINT slice. `PTN002007797` still has both node
  assertions: `GO:0005739` mitochondrion, seeded by yeast Pet191 and human
  COA5, and `GO:0033617` mitochondrial respiratory chain complex IV assembly,
  seeded by yeast Pet191 itself. The row-level
  `propagation_review.source_entities` now name only this PTN node; the extant
  `WITH/FROM` descendants remain as deterministic `supporting_entities`.
- Searched for newer PET191/COA5 papers in 2025-2026 and found no newer
  yeast-specific primary paper beyond the already-cached 2025 human COA5
  complexome study.
