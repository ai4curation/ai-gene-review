---
title: "Upstream Tickets: Origins of Animal Multicellularity"
autolink_gene_symbols: false
---
# Upstream tickets

[← back to Origins of Animal Multicellularity](../../ORIGINS_OF_MULTICELLULARITY.md)

These are ready-to-file reports for the source databases. Each comes from the
reviews in this project, and its facts were re-checked on 2026-10-01 against
live QuickGO, UniProt REST, NCBI E-utilities and the cached PAINT slices.
**None has been filed yet.** The trackers are outside this repository, so a
curator needs to submit them. Record the issue URL here once a ticket is
filed.

| # | Destination | Subject | Rows affected (2026-10-01) | Filed |
|---|---|---|---|---|
| 1 | PAINT (PTHR24356) | [Organ growth and apoptosis IBDs on the LATS node reach choanoflagellates](01-paint-lats-node.md) | 2 IBA + 2 TreeGrafter (one per Warts protein) | no |
| 2 | PANTHER / TreeGrafter (PTHR24027) | [Choanoflagellate cadherins graft onto a node PAINT restricts to Bilateria](02-panther-cadherin-graft.md) | 30 TreeGrafter + 5 IBA | no |
| 3 | PANTHER (PTHR22988 / PTHR24356) | [Warts/LATS kinases split across two families; *Capsaspora* Warts grafted with citron/ROCK](03-panther-warts-family.md) | coWts: 2 TreeGrafter rows; one Capsaspora protein misses the LATS-node IBDs | no |
| 4 | PANTHER (PTHR10316 / PTHR17616) | [*S. rosetta* Yorkie candidate in the MAGI-related family](04-panther-yorkie-family.md) | 2 TreeGrafter | no |
| 5 | PAINT (PTHR31646) | [Mannan biosynthesis IBD seeded only by *Candida* reaches algae, oomycetes and choanoflagellates](05-paint-mannan-node.md) | 56 IBA; 129 rows in all | no |
| 6 | UniProt | [ITGB1–FLNB IPI pair cites the wrong PMID (digit transposition)](06-uniprot-itgb1-flnb-pmid.md) | 2 IPI | no |
| 7 | UniProt | [F2U5Y1 named "Lung surfactant protein A"; it is Rosetteless](07-uniprot-rosetteless-name.md) | name only | no |
| 8 | UniProt / GO annotation | [NOT actin binding (IDA) on vinculin contradicts its cited paper](08-uniprot-vcl-not-actin.md) | 1 NOT IDA | no |
| 9 | GO ontology | [Taxon constraints for organ-level growth terms; NTR rosette colony development](09-go-ontology.md) | ontology | no |
| 10 | TreeGrafter (tool) | [QC rule: suppress graft-node terms whose PAINT taxon excludes the query](10-treegrafter-qc-rule.md) | method | no |
| 11 | PANTHER / TreeGrafter (PTHR10082) | [Unicellular integrin betas grafted onto the vertebrate ITGBL1 node](11-panther-integrin-itgbl1-graft.md) | 54 + 9 TreeGrafter | no |
| 12 | PANTHER / TreeGrafter (PTHR11267) | [*Capsaspora* Brachyury in a Tbx2-class subfamily; cell fate specification from an all-animal node](12-panther-tbox-cobra.md) | 5 + 3 TreeGrafter (one term) | no |

The background for each ticket is in the
[propagation audit](../propagation-audit.md), the
[TreeGrafter case study](../../TREEGRAFTER/holozoan-hippo-case-study.md) and
the [MISCITATIONS project](../../MISCITATIONS.md).
