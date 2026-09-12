---
title: "PSEPK Pst phosphate uptake batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_5329, PP_5328, PP_5327, pstB2, pstS, pstC, pstA, pstB1]
autolink_gene_symbols: false
---

# PSEPK Pst phosphate uptake

- KEGG context: `ppu02010` (ABC transporters)
- Reusable module: `modules/bacterial_pst_phosphate_uptake.yaml`
- Curated genes: 8
- Boundary: PstS phosphate capture, PstA/PstC membrane translocation, and PstB ATP-dependent energy coupling

## Workflow

- [x] Define a species-neutral module with three substantive parts.
- [x] Curate every GOA row for the four PP_5326-PP_5329 genes and the four PP_2656-PP_2659 genes.
- [x] Perform an annotation-reviewer pass over all 43 GOA rows in all eight selected reviews.
- [x] Correct collective transporter functions to `contributes_to` in the curated core functions.
- [x] Verify UniProt accessions, PANTHER families, GO identifiers, and supporting-text fragments.
- [x] Assign PP_5327 and PP_5328 as the predicted PstB2 membrane partners without presenting the inferred KT2440 assembly as experimental fact.
- [x] Reconcile the completed module-plus-`ppu02010`-plus-PSEPK OpenScientist report.
- [x] Document the distinct PP_2656-PP_2659 and Pho-linked PP_5326-PP_5329 loci.
- [x] Add per-gene evidence notes and same-species primary-literature context.
- [x] Validate and render the gene reviews, module, and batch page.
- [ ] Shepherd the draft PR through review and CI.

## Curated Genes

| Gene | Locus | UniProt | Core role | Audit decision |
|---|---|---|---|---|
| `PP_5329` | PP_5329 | Q88C54 | Canonical-locus periplasmic PstS | Add phosphate-uptake process and inferred complex membership |
| `PP_5328` | PP_5328 | Q88C55 | Canonical-locus PstC-like permease | Refine generic transport and add collective phosphate-transporter contribution |
| `PP_5327` | PP_5327 | Q88C56 | Canonical-locus PstA permease | Treat GO:0005315 as a collective contribution |
| `pstB2` | PP_5326 | Q88C57 | Canonical-locus PstB ATPase | Link conservatively to adjacent predicted permeases and document the PANTHER conflict |
| `pstS` | PP_2656 | Q88JJ3 | Candidate second-locus periplasmic PstS | Refine location and add inferred complex membership |
| `pstC` | PP_2657 | Q88JJ2 | Candidate second-locus permease | Treat GO:0005315 as a collective contribution |
| `pstA` | PP_2658 | Q88JJ1 | Candidate second-locus permease | Confirm corrected `pstA` symbol and collective qualifier |
| `pstB1` | PP_2659 | Q88JJ0 | Candidate second-locus ATPase | Model ATP hydrolysis and inferred complex membership |

## Module Structure

1. **Phosphate capture.** Periplasmic PstS binds inorganic phosphate and presents it to the transporter.
2. **Collective PstSACB transport.** One PstS, one PstA, one PstC, and two PstB subunits form the substrate-binding ABC importer that moves phosphate into the cytoplasm.
3. **Energy coupling.** A PstB-family ATPase hydrolyzes ATP to drive the collective transport step.

The reusable module does not encode either KT2440 locus as its exemplar. Its
family selectors use reviewed *Escherichia coli* K-12 representatives whose
exact PANTHER subfamilies and local family containment were verified. The
PP_5326-PP_5329 locus is the high-confidence Pho-linked KT2440 realization;
PP_2656-PP_2659 remains a second candidate Pst-like realization with weaker
taxon-specific support.

`scope: CONCRETE` is retained because the module specifies one physical
PstSACB importer architecture and its required activities, while remaining
species-neutral. It is not a broad thematic collection of phosphate-homeostasis
genes. PhoU/PhoR/PhoB regulation is therefore outside the module boundary.

The module excludes PhoU/PhoR/PhoB phosphate-homeostasis regulation, low-affinity
phosphate transporters, phosphonate transport, and downstream phosphate
assimilation. Molecular functions occur only on leaf annotons.

## Evidence Boundary

The completed module-plus-`ppu02010`-plus-PSEPK OpenScientist report identifies
PP_5326-PP_5329 as the complete Pho-linked locus and PP_2656-PP_2659 as a second
Pst-like candidate operon without the same regulatory context. The primary PRS2000 study
(PMID:16232467) establishes PstSCAB-dependent phosphate uptake in the same
species but does not directly test either KT2440 locus. The gene reviews retain
that distinction. The generic-module OpenScientist run completed in 1,542
seconds and independently supports the PstS/PstA/PstC/PstB transport boundary,
the PstB dimer, and exclusion of PhoU/PhoR/PhoB regulation. Its broader
moonlighting and lineage-variation discussion is retrieval context rather than
additional required module structure.

## Wave 125 annotation-reviewer audit

Every selected GOA row was checked against the fetched UniProt record, qualifier
semantics, locus context, and the available pathway evidence. The audit covered
43 source GOA rows: 6 each for PP_5327, pstA, and pstC; 4 for PP_5328; 3 for
PP_5329; 4 for pstS; and 7 each for pstB1 and pstB2. Five conservative `NEW`
rows record inferred complex membership or a missing phosphate-specific
contribution. No row remains `PENDING`; no experimental annotation was removed.
