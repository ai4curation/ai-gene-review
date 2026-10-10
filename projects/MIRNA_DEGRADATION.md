---
title: "MicroRNA Degradation / TDMD Project"
maturity: MATURE
last_reviewed: "2026-10-04"
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
genes: [ZSWIM8, CUL3, ARIH1, ELOB, ELOC, AGO2, AGO1, AGO3, AGO4]
species: [human]
sidecars:
  genes: MIRNA_DEGRADATION/genes.csv
  fetch_queue: MIRNA_DEGRADATION/fetch_queue.csv
  sources: MIRNA_DEGRADATION/sources.md
  slide_figures:
    - MIRNA_DEGRADATION/slides/actions-per-gene.svg
    - MIRNA_DEGRADATION/slides/tdmd-ligase.svg
    - MIRNA_DEGRADATION/slides/zswim8-review-table.jpg
manifest:
  slides:
    - href: MIRNA_DEGRADATION/slides/MIRNA_DEGRADATION-slides.html
      description: AI generated
---
# MicroRNA Degradation / TDMD Project

**Bottom line:** target-directed microRNA degradation (TDMD) removes selected mature miRNAs by
using highly complementary trigger RNAs to expose an AGO-miRNA state that is recognized by a
ZSWIM8-CUL3 Cullin-RING ligase and handed to the ubiquitin-proteasome system. Anchored on Farnung
et al. 2026 (Nature), this project reviews the dedicated protein layer - ZSWIM8, CUL3, ARIH1,
ELOB, ELOC and the AGO1-4 substrate layer - without folding in miRNA biogenesis, generic CRLs,
proteasome subunits or every transcript that can carry a TDMD trigger. As of 2026-10-04, all
nine human phase-1 reviews exist and all 1,106 GOA rows are actioned: 686 ACCEPT, 126
KEEP_AS_NON_CORE, 111 MARK_AS_OVER_ANNOTATED, 143 REMOVE, 18 MODIFY and 22 UNDECIDED. The most
TDMD-specific corrections are in ZSWIM8, where broad `positive regulation of miRNA catabolic
process` rows point to `GO:0140958` target-directed miRNA degradation and an inherited
Cul2-RING complex row is replaced by Cul3-RING; across the cohort, 139 of 143 removals are bare
`protein binding` rows.

## Overview

This phase-1 pass reviews dedicated gene products in metazoan microRNA degradation. It is
intentionally centered on target-directed microRNA degradation (TDMD), not on every
process that can influence miRNA abundance.

The anchor paper from Chris, Farnung et al. 2026 in Nature,
["The E3 ubiquitin ligase mechanism specifying targeted microRNA degradation"](https://www.nature.com/articles/s41586-026-10232-0),
makes the initial scope sharper: the strongest direct mechanistic evidence currently converges on the
ZSWIM8-CUL3-ARIH1 axis acting on AGO-miRNA complexes bound by specialized trigger RNAs. That is the
right place to start a review project without accidentally absorbing half of RNA biology.

## Phase-1 Question

Which dedicated proteins directly execute or specify TDMD in metazoans, and how should their GO
annotations distinguish core TDMD function from generic RNA silencing, ubiquitin ligase, or RNA
decay biology?

## 2026-10-04 Review Results

| Gene | Status | Existing rows | Main curation result |
|------|--------|---------------|----------------------|
| ZSWIM8 | COMPLETE | 14 | TDMD is represented with `GO:0140958` target-directed miRNA degradation and Cul3-RING, not the broader miRNA catabolic-process parent or an inherited Cul2-RING complex |
| CUL3 | INITIALIZED | 228 | Every row is actioned; CUL3 is treated as a ubiquitin ligase complex scaffold, with 78 mostly generic protein-binding, broad pathway or stray localization/proximity rows marked over-annotated; ubiquitin-ligase and transferase proxy rows are modified to `GO:0160072` |
| ARIH1 | COMPLETE | 75 | HHARI is retained as a catalytic RBR E3 and ubiquitin-conjugating-enzyme-binding CRL partner rather than annotated specifically to TDMD |
| ELOB | COMPLETE | 111 | Elongin B is kept as a reusable Elongin BC adaptor module; 23 bare `protein binding` rows and one RNA polymerase II initiation row are removed |
| ELOC | COMPLETE | 120 | Elongin C is kept as the SKP1-like Elongin BC adaptor; 35 bare `protein binding` rows and one RNA polymerase II initiation row are removed |
| AGO1 | DRAFT | 113 | The non-slicing Argonaute core is kept; 20 bare `protein binding` rows are removed and eight poorly supported rows remain undecided |
| AGO2 | DRAFT | 267 | AGO2 remains the catalytic human slicer; 57 bare `protein binding` rows are removed and 11 rows remain undecided |
| AGO3 | COMPLETE | 95 | AGO3 is kept as a miRNA-binding RISC component with conditional guide-dependent slicer activity; broad or processing-adjacent rows are mostly over-annotated |
| AGO4 | COMPLETE | 83 | AGO4 is kept as a non-slicing miRNA-binding RISC component; the propagated RNA endonuclease row is removed |

## Selection Criteria

- Include genes with direct genetic, biochemical, or structural evidence for participation in TDMD or immediate AGO-trigger recognition.
- Prefer genes whose own protein function is meaningfully reviewable in a GO-centric gene review.
- Keep AGO paralogs if there is evidence they are direct TDMD substrates or part of the immediate mechanistic target layer.
- Track trigger RNAs and trigger-bearing transcripts as source/context regulators, but do not automatically turn them into phase-1 review jobs.
- Defer generic RNA turnover, proteasome, or ubiquitin housekeeping factors unless a TDMD-specific role becomes part of the actual review question.

## Scope Guardrails

In scope for phase 1:

- The ZSWIM8 ligase axis and the immediate AGO substrate layer.
- Endogenous trigger RNAs and trigger-bearing transcripts as contextual regulators in project notes.

Out of scope for phase 1:

- General miRNA biogenesis genes such as DROSHA, DGCR8, DICER1, TARBP2, and XPO5.
- Canonical effector-side repression genes such as TNRC6A, TNRC6B, TNRC6C, or CCR4-NOT components.
- Generic CRL or proteasome housekeeping components such as RBX1, UBE2D2, UBE2L3, and proteasome subunits unless a TDMD-specific review need emerges.
- Broad RNA decay enzymes such as DIS3L2, TUT4, TUT7, XRN factors, and Nibbler-like trimming factors. These remain phase-2 expansion candidates unless the evidence shows they are part of the core dedicated machinery for the review target in question.
- Protein-coding genes whose only current relevance is a TDMD trigger site in the 3' UTR. These are biologically important but should not dominate gene-function review jobs.

## Initial Core Review Queue

This queue is intentionally narrow. It is the reviewable protein layer that the current evidence most
strongly supports.

| Gene | UniProt | Priority | Why it is in the initial queue |
|------|---------|----------|--------------------------------|
| ZSWIM8 | A7E2V4 | Tier 1 | Dedicated TDMD substrate receptor and central project anchor |
| CUL3 | Q13618 | Tier 1 | Core cullin scaffold of the TDMD ligase |
| ARIH1 | Q9Y4X5 | Tier 1 | Partner E3 required for AGO polyubiquitylation |
| ELOB | Q15370 | Tier 1 | Obligatory ZSWIM8 ligase partner |
| ELOC | Q15369 | Tier 1 | Obligatory ZSWIM8 ligase partner |
| AGO2 | Q9UKV8 | Tier 1 | Direct mechanistic substrate in reconstitution and structural work |
| AGO1 | Q9UL18 | Tier 2 | AGO family TDMD substrate layer |
| AGO3 | Q9H9G7 | Tier 2 | AGO family TDMD substrate layer |
| AGO4 | Q9HCK5 | Tier 2 | AGO family TDMD substrate layer |

## Context Regulators Tracked But Not Queued As Initial Gene Reviews

These are part of the pathway framing, but they should stay out of the phase-1 review queue unless a
later subproject explicitly decides to review trigger-bearing transcripts or ncRNA regulators.

- **CYRANO / OIP5-AS1**: lncRNA trigger for miR-7 and a canonical endogenous TDMD example.
- **NREP**: conserved trigger-bearing transcript for miR-29b with in vivo behavioral phenotypes.
- **SERPINE1**: endogenous TDMD trigger for miR-30b and miR-30c during cell-cycle re-entry.
- **HSUR1**: viral prototype trigger for miR-27; important conceptually but better handled as context or a viral subproject.
- **Drosophila AGO1 mRNA**: validated endogenous trigger for miR-999 and a useful comparative example.
- **`Atp6v1g1`, `Lpar4`, `Plagl1`, `Lrrc58`**: mouse trigger-bearing transcripts from Lin et al. 2026; biologically important, but not dedicated TDMD machinery genes.

## Deferred Expansion Modules

- The TUT4/TUT7-DIS3L2 branch and other miRNA tailing or trimming factors.
- Comparative species modules for fly and worm TDMD machinery once the human core queue is underway.
- Viral TDMD modules as a separate subproject if those examples become important for ontology work.

[#4224](https://github.com/ai4curation/ai-gene-review/issues/4224) tracks those phase-2 decisions
plus the remaining status cleanup for the fully actioned human reviews.

## Fetch Workflow

`projects/MIRNA_DEGRADATION/genes.csv` is the human-readable queue with rationale.
`projects/MIRNA_DEGRADATION/fetch_queue.csv` is the headerless machine-oriented input for the CLI.

```bash
# Fetch the phase-1 queue
uv run ai-gene-review batch-fetch projects/MIRNA_DEGRADATION/fetch_queue.csv

# Launch one review
just fetch-gene human ZSWIM8
just deep-research human ZSWIM8 --provider perplexity
just validate human ZSWIM8
```

## Seed Sources

The source intake file lives at [projects/MIRNA_DEGRADATION/sources.md](MIRNA_DEGRADATION/sources.md).
That file is the place to append new papers from Chris before the project expands the queue.

## Status

- [x] Project scaffold created
- [x] Chris seed Nature 2026 paper integrated
- [x] Initial TDMD core queue defined
- [x] Batch-fetch queue prepared for review launch
- [x] Per-gene folders fetched
- [x] Every fetched phase-1 GOA row assigned an action
- [ ] Promote CUL3, AGO1 and AGO2 out of provisional review statuses after final QA
- [ ] Decide whether to open comparative fly, worm and mouse TDMD modules
- [ ] Decide whether to open a TUT4/TUT7-DIS3L2 tailing-and-decay expansion module

## Notes

### 2026-04-04

- Chris seed source integrated: Farnung et al. 2026 sharpened the decision to treat TDMD as the phase-1 scope.
- Trigger RNAs and trigger-bearing transcripts are explicitly tracked, but are not automatically phase-1 review jobs because the ai-gene-review pipeline is protein and GO centric.
- The first pass stays human-centered for review jobs. Comparative fly, mouse, and worm layers can be added after the core machinery reviews exist.
