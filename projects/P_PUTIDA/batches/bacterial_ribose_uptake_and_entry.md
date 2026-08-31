---
title: "PSEPK bacterial D-ribose uptake and entry batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [rbsB, rbsA-I, rbsC, rbsR, rbsK, rbsD]
autolink_gene_symbols: false
---

# PSEPK bacterial D-ribose uptake and entry

- Reusable module: `modules/bacterial_ribose_uptake_and_entry.yaml`
- KT2440 locus: `PP_2454`-`PP_2459`
- Core route: RbsABC import, RbsD ring-form interconversion, and RbsK phosphorylation
- Boundary review: RbsR regulation and the separate PP_2759/PP_2760 transporter-like pair

## Workflow

- [x] Recover the complete route from UniProt metadata and locus organization.
- [x] Define a species-neutral module with three substantive operations.
- [x] Fetch current UniProt and GOA records for all six locus genes.
- [x] Start OpenScientist research for all six genes with full provider allowances.
- [x] Complete module-plus-taxon OpenScientist research.
- [x] Complete generic module OpenScientist research.
- [x] Curate every GOA row with no `PENDING` actions.
- [x] Complete the independent annotation-reviewer audit.
- [x] Reconcile the module and reviews against completed research.
- [x] Validate and render all affected artifacts.
- [ ] Open one focused draft PR and shepherd it through review and CI.

## Pathway Shape

| Order | Operation | KT2440 implementation | Decision |
|---|---|---|---|
| 1 | ATP-dependent D-ribose import | `rbsB`, `rbsC`, `rbsA-I` | Covered by the contiguous ABC-importer locus; collective transporter activity belongs to the assembled complex |
| 2 | beta-D-ribopyranose to beta-D-ribofuranose | `rbsD` | Covered by a specific HAMAP/EC/Rhea assignment |
| 3 | beta-D-ribofuranose to D-ribose 5-phosphate | `rbsK` | Covered by a specific HAMAP/EC/Rhea assignment |

The output D-ribose 5-phosphate feeds the pentose-phosphate and biosynthetic
networks, but those downstream reactions are outside this module.

## Boundary Decisions

`rbsR` is part of the locus and is curated in this batch, but transcriptional
regulation is not a transport or metabolic operation. The second ATPase/permease
pair `rbsA`/PP_2759 and PP_2760 lacks an assigned substrate-binding component
and substrate-specific evidence, so it does not satisfy the ribose-import step.

The current PANTHER selectors for RbsB and RbsA-I carry D-allose-related labels.
Those terms are omitted from the module rather than relabeled or guessed. Exact
KT2440 UniProt proteins remain as exemplars, while the specific RbsC, RbsD, and
RbsK subfamilies are retained where their official labels match the represented
roles.

The [taxon-aware OpenScientist report](../deep-research/PSEPK__bacterial_ribose_uptake_and_entry__rbs-locus-deep-research-openscientist.md)
independently recovered the same `PP_2454`-`PP_2459` boundary and found no direct
KT2440 transport, enzyme, or growth-on-ribose experiment. Its assignments are
therefore used as retrieval support for locus and orthology evidence, not as
direct experimental evidence. It also flagged the `PP_2757`-`PP_2761` cluster
as substrate-ambiguous rather than a second satisfied ribose-import route.

The [generic module report](../../../modules/bacterial_ribose_uptake_and_entry-deep-research-openscientist.md)
supports the same three operations from cross-bacterial structural and
biochemical literature. It also establishes that RbsD accelerates a spontaneous
ring-form equilibrium. The module therefore includes RbsD as a substantive
catalytic operation without claiming it is the sole source of
beta-D-ribofuranose or universally essential.

## Metadata Follow-up

The Q88K36 UniProt record still carries legacy transporter EC `3.6.3.17` and an
embedded `GO:0016787` hydrolase mapping. The latter is not present in the
current fetched GOA table, so it is documented here rather than fabricated as
an `existing_annotations` row. The same legacy EC occurs on Q88K37. These are
UniProt metadata follow-ups and do not alter the current GOA-row decisions.

## Partition Lesson

The first-pass KEGG partition did not recover this route as a coherent pathway:
the `rbs` locus genes sit in transport/orphan metadata buckets rather than a
KT2440-specific KEGG pathway. Locus-aware module recovery is therefore required
in addition to KEGG bucket traversal for whole-genome coverage.
