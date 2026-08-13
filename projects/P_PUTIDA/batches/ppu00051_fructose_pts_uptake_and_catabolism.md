---
title: "PSEPK fructose PTS uptake and catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [fruB, fruK, fruA]
autolink_gene_symbols: false
---

# PSEPK fructose PTS uptake and catabolism

- KEGG context: `ppu00051` (fructose and mannose metabolism) and `ppu02060` (PTS)
- Reusable module: `modules/fructose_pts_uptake_and_catabolism.yaml`
- Curated genes: 3
- Boundary: FruB/FruA PTS import to fructose 1-phosphate, followed by FruK to fructose 1,6-bisphosphate

## Workflow

- [x] Define a species-neutral module with at least two substantive parts.
- [x] Fetch FruB, FruA, and FruK UniProt/GOA records.
- [x] Fetch and inspect primary KT2440 literature.
- [x] Curate all selected gene reviews.
- [x] Add exact UniProt exemplars and checked PANTHER family identifiers.
- [x] Record exact TreeGrafter PTNs without promoting them to PAINT ancestral nodes.
- [x] Attempt gene-level OpenScientist research; the FruK report completed,
  while the corrected FruB and FruA requests each exhausted the 7,200-second
  provider timeout without a report.
- [x] Attempt generic module-level OpenScientist research; the corrected
  request exhausted its 7,200-second provider timeout without a report.
- [x] Run module + pathway + PSEPK OpenScientist research.
- [x] Reconcile generated reports with the manual curation.
- [x] Validate gene and module YAML.
- [x] Render the module and project page.
- [x] Open one non-draft PR for this module:
  [#2235](https://github.com/ai4curation/ai-gene-review/pull/2235).
- [ ] Shepherd the PR through review and CI.

## Curated Genes

| Done | Gene | Locus | UniProt | Core role | Key decision |
|---|---|---|---|---|---|
| [x] | `fruB` | PP_0793 | Q88PQ5 | EI-HPr-EIIA(Fru) phosphorelay | Accept GO:0008965; broad kinase/transferase parents are over-annotated |
| [x] | `fruA` | PP_0795 | Q88PQ3 | EIIB-EIIC fructose transport-phosphorylation | Remove proton symport and proton transport; accept GO:0022877 and GO:0090563 |
| [x] | `fruK` | PP_0794 | Q88PQ4 | 1-phosphofructokinase | Accept GO:0008662; generic phosphofructokinase and kinase parents are over-annotated |

## Module Structure

1. **Fructose PTS import and phosphorylation.** FruB introduces phosphate from
   PEP into the soluble relay; FruA receives phosphate through its EIIB domain
   and couples EIIC-mediated import to formation of intracellular fructose
   1-phosphate.
2. **FruK phosphorylation.** FruK uses ATP to convert fructose 1-phosphate to
   fructose 1,6-bisphosphate.

The first part exposes FruB and FruA as separate leaf annotons so each
molecular function remains attached to the protein that executes it. No
molecular-function term is placed at the process-module level.

## Evidence and Scope

Primary KT2440 studies identify FruA and FruB as the complete fructose-intake
PTS and describe the `fruBKA` locus, FruB EI-HPr-EIIA(Fru) architecture, FruA
EIIBC architecture, and FruK 1-phosphofructokinase role (PMID:18296519,
PMID:22708906, PMID:27933319). Exact reactions are RHEA:23880 for FruB,
RHEA:49252 for FruA, and RHEA:14213 for FruK.

Cra/FruR regulation, PP_3443-dependent PEP support, and PTS(Ntr) cross-talk are
documented context but are outside the catalytic module. Other `ppu00051`
members belong to alginate, mannose, fucose, or downstream central-carbon
modules and were not pulled into this focused batch.

The generic OpenScientist request was allowed to run for the full configured
7,200 seconds with three iterations but timed out in the provider queue. No
generic report is cited or represented as evidence. The completed
module-plus-`ppu00051`-plus-PSEPK report was checked against the primary
KT2440 evidence above. The completed FruK report independently recovered the
exact 1-phosphofructokinase reaction, the `fruBKA` context, and the distinction
from fructose 6-phosphate kinases; it did not require a change to the manually
curated review. FruB and FruA were each allowed the same full provider timeout,
so their missing reports are recorded as retrieval failures rather than
unfinished curation.
