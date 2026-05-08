---
species: [human, mouse, DROME, worm]
sidecars:
  genes: MIRNA_DEGRADATION/genes.csv
  fetch_queue: MIRNA_DEGRADATION/fetch_queue.csv
  sources: MIRNA_DEGRADATION/sources.md
---
# MicroRNA Degradation / TDMD Project

## Overview

This is the phase-1 scaffold for reviewing dedicated gene products in metazoan microRNA degradation.
The first pass is intentionally centered on target-directed microRNA degradation (TDMD), not on every
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
- **ATP6V1G1, LPAR4, PLAGL1, LRRC58**: mouse trigger-bearing transcripts from Lin et al. 2026; biologically important, but not dedicated TDMD machinery genes.

## Deferred Expansion Modules

- The TUT4/TUT7-DIS3L2 branch and other miRNA tailing or trimming factors.
- Comparative species modules for fly and worm TDMD machinery once the human core queue is underway.
- Viral TDMD modules as a separate subproject if those examples become important for ontology work.

## Review Launch Workflow

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
- [ ] Per-gene folders fetched
- [ ] Per-gene reviews underway

## Notes

### 2026-04-04

- Chris seed source integrated: Farnung et al. 2026 sharpened the decision to treat TDMD as the phase-1 scope.
- Trigger RNAs and trigger-bearing transcripts are explicitly tracked, but are not automatically phase-1 review jobs because the ai-gene-review pipeline is protein and GO centric.
- The first pass stays human-centered for review jobs. Comparative fly, mouse, and worm layers can be added after the core machinery reviews exist.
