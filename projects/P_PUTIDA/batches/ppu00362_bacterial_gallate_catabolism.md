---
title: "PSEPK bacterial gallate catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK bacterial gallate catabolism

This batch assembles the curated KT2440 Gal proteins into a reusable multi-part
gallate catabolism module. The complete OpenScientist GalC report was integrated
with the existing Falcon reports, reviewed UniProt records, QuickGO rows, and
the two direct KT2440 publications.

## Boundary

- GalA, GalD, GalB, and GalC form the required sequential catalytic route from
  gallate to pyruvate and oxaloacetate.
- GalP is optional uptake context because porin activity is supported but its
  transported substrate is not directly established.
- GalT and GalR remain adjacent transport/regulatory context until their roles
  can be represented without overclaiming.
- The current GO term for GalC names HMG aldolase activity; its use for the
  physiological CHA cleavage is documented as an ontology limitation.

## Workflow

- [x] Select a distinct reusable pathway with more than one substantive part.
- [x] Add exact PSEPK UniProt exemplars at each annoton.
- [x] Preserve uncertainty around GalP specificity and the GalC GO label.
- [x] Wait for all requested OpenScientist calls to finish without terminating them.
- [x] Record the four gene and two module calls that exited without artifacts.
- [x] Reconcile the completed GalC report and existing evidence with every gene review.
- [x] Audit all 26 downloaded GOA rows (25 distinct assertions) and remove all pending actions.
- [x] Validate and render all changed artifacts.
- [ ] Open one focused draft PR.

## Selected genes

| Done | Gene | Locus | UniProt | Module role |
|---|---|---|---|---|
| [x] | `galP` | PP_2517 | Q88JX6 | optional outer-membrane porin |
| [x] | `galA` | PP_2518 | Q88JX5 | gallate ring-cleavage dioxygenase |
| [x] | `galD` | PP_2513 | Q88JY0 | 4-oxalomesaconate tautomerase |
| [x] | `galB` | PP_2515 | Q88JX8 | 4-oxalomesaconate hydratase |
| [x] | `galC` | PP_2514 | Q88JX9 | terminal CHA aldolase |

## Notes

2026-08-13: Added as the replacement for a newly detected duplicate
nitrogen-regulatory PTS allocation. The nitrogen PTS is already covered by PR
#2525 and therefore does not count toward this 20-module batch.

2026-08-13: The galP, galA, galD, and galB gene-level OpenScientist calls and
both the generic-module and module + ppu00362 + PSEPK calls exited after the
requested wait without writing report artifacts. They were not restarted. The
pre-existing completed GalC OpenScientist report and artifacts were integrated;
the other genes retain their existing Falcon reports and direct local evidence.

2026-08-13: All 26 downloaded QuickGO rows were reviewed. GalC contains one
exact duplicate experimental row, yielding 25 distinct source assertions. The reusable module keeps
GalP optional, models the four experimentally established catalytic reactions,
and records exact PSEPK UniProt exemplars and Rhea reactions. The principal
residual gaps are GalP substrate specificity/inner-membrane uptake and the lack
of a CHA-specific GO molecular-function term for GalC.
