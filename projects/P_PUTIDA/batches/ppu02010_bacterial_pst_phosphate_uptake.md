---
title: "PSEPK Pst phosphate uptake batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [pstS, pstA, pstC, pstB1, pstB2]
autolink_gene_symbols: false
---

# PSEPK Pst phosphate uptake

- KEGG context: `ppu02010` (ABC transporters)
- Reusable module: `modules/bacterial_pst_phosphate_uptake.yaml`
- Curated genes: 5
- Boundary: PstS phosphate capture, PstA/PstC membrane translocation, and PstB ATP-dependent energy coupling

## Workflow

- [x] Define a species-neutral module with three substantive parts.
- [x] Curate every GOA row for pstS, pstA, pstC, pstB1, and pstB2.
- [x] Perform an independent annotation-reviewer audit of all five reviews.
- [x] Correct collective transporter functions to `contributes_to` in the curated core functions.
- [x] Verify UniProt accessions, PANTHER families, GO identifiers, and supporting-text fragments.
- [x] Keep the PstB2 membrane partner unresolved rather than assigning it to PstSACB1.
- [x] Reconcile the completed module-plus-`ppu02010`-plus-PSEPK OpenScientist report.
- [x] Document the distinct PP_2656-PP_2659 and Pho-linked PP_5326-PP_5329 loci.
- [x] Add per-gene evidence notes and same-species primary-literature context.
- [x] Validate and render the gene reviews, module, and batch page.
- [ ] Shepherd the draft PR through review and CI.

## Curated Genes

| Gene | Locus | UniProt | Core role | Audit decision |
|---|---|---|---|---|
| `pstS` | PP_2656 | Q88JJ3 | Periplasmic phosphate capture | Refine location and add complex membership |
| `pstC` | PP_2657 | Q88JJ2 | Membrane permease subunit | Treat GO:0005315 as a collective contribution |
| `pstA` | PP_2658 | Q88JJ1 | Membrane permease subunit | Confirm corrected `pstA` symbol and collective qualifier |
| `pstB1` | PP_2659 | Q88JJ0 | PP_2656 operon transport ATPase | Model ATP hydrolysis and inferred complex membership |
| `pstB2` | PP_5326 | Q88C57 | Pho-linked operon transport ATPase | Keep separate from the PP_2656 complex and document the PANTHER conflict |

## Module Structure

1. **Phosphate capture.** Periplasmic PstS binds inorganic phosphate and presents it to the transporter.
2. **Membrane translocation.** PstA and PstC form the phosphate-selective inner-membrane pathway and collectively contribute transporter activity.
3. **Energy coupling.** A PstB-family ATPase hydrolyzes ATP to drive import.
   PstB1 is encoded beside the represented `pstSAC` genes. PstB2 is an
   alternative exact family exemplar encoded in the distinct PP_5326-PP_5329
   Pho-linked locus and is not modeled as part of the PP_2656 complex.

The module excludes PhoU/PhoR/PhoB phosphate-homeostasis regulation, low-affinity
phosphate transporters, phosphonate transport, and downstream phosphate
assimilation. Molecular functions occur only on leaf annotons.

## Evidence Boundary

The completed module-plus-`ppu02010`-plus-PSEPK OpenScientist report identifies
PP_5326-PP_5329 as the Pho-linked locus and PP_2656-PP_2659 as a second complete
Pst-like operon without the same regulatory context. The primary PRS2000 study
(PMID:16232467) establishes PstSCAB-dependent phosphate uptake in the same
species but does not directly test either KT2440 locus. The gene reviews retain
that distinction. Gene-level and generic-module provider jobs remain active and
were not stopped; their incomplete outputs are not included.
