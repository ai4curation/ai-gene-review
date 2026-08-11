---
title: "PSEPK Pst phosphate uptake batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [pstS, pstA, pstC, pstB1, pstB2]
autolink_gene_symbols: false
---

# PSEPK Pst high-affinity phosphate uptake

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
- [ ] Reconcile active OpenScientist reports when they complete.
- [x] Validate and render the gene reviews, module, and batch page.
- [ ] Shepherd the draft PR through review and CI.

## Curated Genes

| Gene | Locus | UniProt | Core role | Audit decision |
|---|---|---|---|---|
| `pstS` | PP_2656 | Q88JJ3 | Periplasmic phosphate capture | Replace broad extracellular region with periplasmic space |
| `pstC` | PP_2657 | Q88JJ2 | Membrane permease subunit | Treat GO:0005315 as a collective contribution |
| `pstA` | PP_2658 | Q88JJ1 | Membrane permease subunit | Confirm corrected `pstA` symbol and collective qualifier |
| `pstB1` | PP_2659 | Q88JJ0 | Cluster-linked transport ATPase | Model ATP hydrolysis as its direct leaf activity |
| `pstB2` | PP_5326 | Q88C57 | Second phosphate-transport ATPase | Preserve phosphate assignment but leave partner unresolved |

## Module Structure

1. **Phosphate capture.** Periplasmic PstS binds inorganic phosphate and presents it to the transporter.
2. **Membrane translocation.** PstA and PstC form the phosphate-selective inner-membrane pathway and collectively contribute transporter activity.
3. **Energy coupling.** A PstB-family ATPase hydrolyzes ATP to drive import. PstB1 is encoded beside `pstSAC`; PstB2 is an alternative exact exemplar whose cognate membrane assembly is not known.

The module excludes PhoU/PhoR/PhoB phosphate-homeostasis regulation, low-affinity
phosphate transporters, phosphonate transport, and downstream phosphate
assimilation. Molecular functions occur only on leaf annotons.

## Research Status

The five gene-level OpenScientist jobs and both generic module and
module-plus-`ppu02010`-plus-PSEPK jobs were active at publication time. They
were allowed to continue with the required full provider timeout and did not
block the mandatory manual audit or draft PR.
