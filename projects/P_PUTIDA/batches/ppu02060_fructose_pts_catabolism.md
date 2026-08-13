---
title: "PSEPK fructose PTS catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [fruB, fruK, fruA]
autolink_gene_symbols: false
---

# PSEPK ppu02060: fructose PTS catabolism

- Module seed: `bacterial_fructose_pts_catabolism`
- Selected genes: 3
- Reused curated reviews: `fruB`, `fruA`, `fruK`

## Curated Boundary

- FruB supplies the fused soluble EI-HPr-EIIA phosphorelay.
- FruA couples fructose import to fructose 1-phosphate formation.
- FruK converts fructose 1-phosphate to fructose 1,6-bisphosphate.
- PtsP/PtsO/PtsN nitrogen-related signaling is a separate module despite
  documented cross-talk with FruB.

## Required Workflow

- [x] Define a reusable multi-part module.
- [x] Confirm all selected gene reviews are already curated.
- [x] Confirm existing OpenScientist research for `fruK`.
- [x] Record unsuccessful OpenScientist runs for `fruA` and `fruB`.
- [x] Complete module-level OpenScientist research.
- [x] Complete module + pathway + PSEPK OpenScientist research.
- [x] Consult the annotation reviewer and address its five blockers.
- [x] Validate the revised module and selected gene reviews.
- [x] Render module and selected gene reviews.
- [ ] Open one draft PR for this module.

## Selected Genes

| Done | Gene | Locus | UniProt | Role | Research |
|---|---|---|---|---|---|
| [x] | `fruB` | PP_0793 | Q88PQ5 | fused EI-HPr-EIIA phosphorelay | no artifact returned |
| [x] | `fruK` | PP_0794 | Q88PQ4 | 1-phosphofructokinase | OpenScientist complete |
| [x] | `fruA` | PP_0795 | Q88PQ3 | fructose-specific EIIB-EIIC transporter | no artifact returned |

## Notes

2026-08-13: Split the KEGG PTS bucket into a coherent fructose-catabolism
module and a later nitrogen-PTS signaling module. The boundary ends at fructose
1,6-bisphosphate, before shared central-carbon reactions.

2026-08-13: Annotation review restricted the reusable scope to fused-relay
systems, replaced selector-incompatible exemplars, separated PEP entry from the
internal FruB EI-HPr-EIIA relay, completed FruK reaction chemistry, and corrected
the broad FruK process annotation from over-annotation to MODIFY. The generic
OpenScientist wrapper reached its outer timeout after writing a complete report
and final artifacts; the report was retained and assessed normally.

2026-08-13: The `fruA` and `fruB` provider jobs were launched and retried but
exited without reports. Their curated reviews are retained on the strength of
the completed generic and PSEPK pathway syntheses, direct UniProt/GOA evidence,
primary literature, and the independent annotation-review pass; no missing
gene-level report is claimed.
