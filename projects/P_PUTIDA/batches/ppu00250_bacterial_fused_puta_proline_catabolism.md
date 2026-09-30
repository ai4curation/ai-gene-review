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
- [x] Complete the module and PSEPK pathway research.
- [x] Curate every GOA row and consult the annotation reviewer.
- [x] Validate and render all artifacts.
- [x] Open one draft PR: [PR #2829](https://github.com/ai4curation/ai-gene-review/pull/2829).

## Boundary

- PutP imports L-proline by sodium symport.
- One full-length PutA performs two distinct reactions, represented as separate parts.
- PutA transcriptional regulation and proline biosynthesis are outside the reaction chain.

## Curated Artifacts

- [Reusable fused-PutA module](../../../modules/bacterial_fused_puta_proline_catabolism.yaml)
- [putP review](../../../genes/PSEPK/putP/putP-ai-review.yaml)
- [putA review](../../../genes/PSEPK/putA/putA-ai-review.yaml)
- [Batch membership TSV](ppu00250_bacterial_fused_puta_proline_catabolism.tsv)
- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial_fused_puta_proline_catabolism__ppu00250-deep-research-openscientist.md)
- [OpenScientist generic-module report](../../../modules/bacterial_fused_puta_proline_catabolism-deep-research-openscientist.md)

## Evidence Summary

The exact KT2440 members are PutP Q88D81 (PP_4946) and PutA Q88D80
(PP_4947). PMID:10613867 assigns PutP as an integral inner-membrane
proline-uptake protein by homology and genetically links PutA to proline
utilization; its domain analysis suggests that one PutA polypeptide carries
both proline-to-glutamate catalytic steps. PMID:11097893 separately establishes
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

The completed taxon-aware report confirms that the module is satisfiable with
these two adjacent genes but clarifies that `ppu00250` was only the screening
bucket. Proline uptake and oxidation belong biologically with arginine/proline
metabolism (`ppu00330`); PutA-derived glutamate then feeds the broader
alanine/aspartate/glutamate network represented by `ppu00250`. PutP is absent
from that KEGG candidate list because it is a transporter. The report also
supports excluding the osmoprotectant ProP and betaine/proline ABC systems from
this catabolic module, and treats the PP_3331 sodium:proline-symporter label as
uncertain because its recorded domain architecture lacks the PutP/SSS-family
signature.

The generic-module report independently recovers the same three-event
transport/oxidation architecture and the conserved PutA fusion model. Its claim
that PSEPK PutA is only bifunctional was not imported: the direct P. putida
operator-DNA structure and regulation literature already establish the
additional DNA-binding autorepressor activity. That activity remains in the
gene review and outside this connected metabolic module.

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

2026-08-31: Opened focused draft PR #2829 after correcting the distinction
between direct pathway evidence and homology-supported catalytic assignments,
adding direct P. putida PutA-DNA structural evidence, and fixing broad-term and
supporting-text decisions. The PutP, PSEPK module/pathway/taxon, and
generic-module retries all completed and were integrated conservatively.
