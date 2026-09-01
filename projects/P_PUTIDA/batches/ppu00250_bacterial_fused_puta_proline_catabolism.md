---
title: "PSEPK fused PutA proline catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [putP, putA]
autolink_gene_symbols: false
---

# PSEPK proline uptake and fused PutA catabolism

## Workflow

- [x] Fetch the PutP and PutA gene-review inputs.
- [x] Complete available OpenScientist gene research.
- [x] Complete the module and PSEPK pathway research attempts.
- [x] Curate every GOA row and consult the annotation reviewer.
- [x] Validate and render all artifacts.
- [ ] Open one draft PR.

## Boundary

- PutP imports L-proline by sodium symport.
- One full-length PutA performs two distinct reactions, represented as separate parts.
- PutA transcriptional regulation and proline biosynthesis are outside the reaction chain.

## Curated Artifacts

- [Reusable fused-PutA module](../../../modules/bacterial_fused_puta_proline_catabolism.yaml)
- [putP review](../../../genes/PSEPK/putP/putP-ai-review.yaml)
- [putA review](../../../genes/PSEPK/putA/putA-ai-review.yaml)
- [Batch membership TSV](ppu00250_bacterial_fused_puta_proline_catabolism.tsv)

## Evidence Summary

The exact KT2440 members are PutP Q88D81 (PP_4946) and PutA Q88D80
(PP_4947). PMID:10613867 directly identifies PutP as an integral inner-membrane
proline-uptake protein and genetically links PutA to proline utilization; its
domain analysis suggests that one PutA polypeptide carries both
proline-to-glutamate catalytic steps. PMID:11097893 separately establishes
PutA-dependent repression of the divergent promoters; that regulatory role is
retained in the gene review but excluded from the metabolic module. UniProt
maps the three modeled reactions to RHEA:28967, RHEA:23784, and RHEA:30235.
The exact putA GOA rows cite PANTHER:PTN001709052 for GO:0003842 and
GO:0009898. That PTN is recorded as evidence provenance but is not used as the
module selector: the fetched PTHR42862:SF1 family contains many stand-alone
P5C dehydrogenases and does not safely identify the fused two-domain PutA
architecture.
The refreshed putP rows cite PANTHER:PTN005155986, and the exact UniProt record
assigns Q88D81 to PTHR48086:SF3; the fetched PTHR48086 family data corroborate
the broader sodium:solute-symporter family context.

QuickGO returned 14 source rows for putA. A forced putP refresh corrected the
initial header-only artifact and returned 11 source rows covering five distinct
UniProt-displayed terms plus six additional current inference rows. All 25
source rows now have explicit decisions; no putP term is misrepresented as NEW.

## Notes

2026-08-13: Started as module 17 of the current 20-module batch. The selector
requires orthology to full-length PSEPK PutA to avoid conflating fused PutA with
stand-alone P5C dehydrogenases in PTHR42862:SF1. OpenScientist produced the
putA report and artifact bundle. The putP research run exited without an output file.
The generic-module and module+pathway+taxon wrappers exited, and their detached
provider clients later exited naturally without publishing report artifacts.
They were not restarted or terminated. The curation therefore uses the
completed PutA report as retrieval support and grounds decisions in the exact
UniProt/QuickGO records and cached primary literature.
