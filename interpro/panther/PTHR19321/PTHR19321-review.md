# PANTHER Family Review: PTHR19321

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR19321 |
| **Family Name** | PROTEIN REGULATOR OF CYTOKINESIS 1 PRC1-RELATED |
| **InterPro Entry** | IPR007145 (MAP65/ASE1/PRC1 family) |
| **Total Proteins** | 11,236 |
| **Taxonomic Breadth** | 8,422 taxa |
| **Subfamilies** | 35 |
| **Representative Structure** | 3nrx (PRC1 antiparallel microtubule crosslinking) |

## Executive Summary

PTHR19321 is the **Ase1 / PRC1 / MAP65 family of microtubule-associated proteins (MAPs)**. Members are **homodimeric, non-motor microtubule-bundling proteins** that specifically crosslink **antiparallel** microtubules, defining and stabilizing the zone of antiparallel microtubule overlap - the spindle midzone in dividing animal/fungal cells, and the phragmoplast/cortical arrays in plants. The shared architecture combines a dimerization/spectrin-like rod with a C-terminal microtubule-binding region (the IPR007145 MAP65/ASE1/PRC1 domain).

The **conserved core function across the family is antiparallel microtubule crosslinking/bundling**, organizing the spindle midzone (or its plant equivalent) and serving as a scaffold that recruits midzone effectors (kinesins, CLASP, etc.). Neofunctionalization is minimal at the biochemical level; diversification is mainly **lineage-specific paralog expansion** (notably the Arabidopsis MAP65-1...MAP65-9 family) and regulatory specialization (e.g. PRC1 in mammalian cytokinesis).

The fission yeast anchor **ase1 (Q9HDY1)** crosslinks antiparallel microtubules to build and stabilize the anaphase spindle midzone; *ase1Δ* spindles collapse during anaphase B. Ase1 also organizes interphase, post-anaphase and quiescence microtubule bundles and recruits Klp9, Cls1/Peg1 and other partners.

## Subfamily Analysis

### PTHR19321:SF41 - FASCETTO-RELATED  *(ANCHOR SUBFAMILY)*
**Members**: 4 of the 14 curated reference proteins (largest subfamily)

**Taxonomy**: Cross-kingdom - fungal Ase1-type and a plant MAP65-1, grouped by orthology to *Drosophila* Fascetto (the fly PRC1/Ase1 ortholog).

**Key Members**:
- ***S. pombe* ase1 (Q9HDY1) - the anchor gene**
- *S. pombe* mcp1 (O94452, meiotic coiled-coil protein 1)
- *S. cerevisiae* ASE1 (P50275, anaphase spindle elongation protein)
- *Arabidopsis* MAP65-1 (Q9FLP0)

**Function**: Antiparallel microtubule crosslinking/bundling; spindle midzone (or phragmoplast) organization.

**Notes**: This is **ase1's subfamily**, confirmed from the UniProt record (`DR PANTHER; PTHR19321:SF41; FASCETTO-RELATED`). The grouping of the budding-yeast ASE1, fission-yeast ase1, and a plant MAP65 under one subfamily reflects the deep conservation of the midzone-bundling function.

### PTHR19321:SF1 - PROTEIN REGULATOR OF CYTOKINESIS 1
**Members**: 2 proteins

**Key Members**: Human PRC1 (O43663), Mouse Prc1 (Q99K43)

**Function**: Mammalian PRC1 - antiparallel microtubule crosslinker of the central spindle/midbody, essential for cytokinesis; phosphoregulated by Cdk1 and a docking site for KIF4 and other midzone factors (cf. representative structure 3nrx).

### Arabidopsis MAP65 paralog subfamilies
**Members**: One reference protein each in SF0, SF3, SF4, SF7, SF21, SF23, SF24, SF52

**Key Members**: MAP65-2 (Q8LEG3, SF21), MAP65-3 (Q9FHM4, SF7), MAP65-4 (Q9LZY0, SF52), MAP65-5 (Q9ZVJ3, SF4), MAP65-6 (Q9SIS3, SF0), MAP65-7 (Q8L836, SF23), MAP65-8 (Q9C7G0, SF3), MAP65-9 (Q4PSA3, SF24)

**Function**: Plant 65-kDa microtubule-associated proteins; antiparallel MT bundlers acting in cortical arrays, the preprophase band, spindle and phragmoplast. The expanded paralog set reflects the elaborate plant microtubule cytoskeleton; MAP65-1 itself groups with the conserved SF41/Fascetto subfamily.

## Functional Diversity Assessment

### Neo-functionalization: MINIMAL (biochemically conserved; paralog expansion)
The antiparallel microtubule-bundling biochemistry is conserved across all members. Variation is in **cellular context** (mitotic midzone in fungi/animals vs phragmoplast/cortical arrays in plants), **regulatory wiring** (Cdk1 phosphoregulation of PRC1/Ase1), and **paralog number** (large plant MAP65 family). None of these alter the core MAP function.

## IBA Annotation Assessment

IBA annotations (GO_REF:0000033, node PTN000448590) propagated to ase1 (Q9HDY1).

| GO ID | Label | Aspect | Flags | Assessment |
|-------|-------|--------|-------|------------|
| GO:0051256 | mitotic spindle midzone assembly | BP | NO_UNIPROT_SEEDS | **APPROPRIATE.** This is precisely ase1's curated core role - it assembles/stabilizes the antiparallel overlap of the spindle midzone. The conserved family function. (Propagated without UniProt seeds but biologically well supported for ase1.) |
| GO:1990023 | mitotic spindle midzone | CC | LOCALIZATION; NO_UNIPROT_SEEDS | **APPROPRIATE.** ase1 accumulates robustly at the anaphase spindle midzone; this localization is experimentally established and is the location term used in the curated core_functions. No localization conflict. |

**Summary**: Both propagations are clean and match ase1's curated function and localization exactly. The `NO_UNIPROT_SEEDS` flag reflects how the IBA seeds were drawn (PomBase/WB/dictyBase/SGD ids rather than UniProt accessions), not a quality problem. No paralog-specific or contradictory transfers. (The IBA set is conservatively narrow and does not transfer ase1's additional, less broadly conserved roles such as nuclear-envelope remodeling or meiotic functions, which is appropriate.)

## Key Literature

| PMID | Key Finding |
|------|-------------|
| PMID:15689489 | Fission yeast ase1p (ASE1/PRC1/MAP65 family) organizes the spindle midzone in mitosis. |
| PMID:15647375 | ase1Δ elongating spindles collapse mid-anaphase B. |
| PMID:17254972 | Ase1p localizes along antiparallel MTs (bundler) vs Klp2 at plus ends. |
| PMID:21892183 | Ase1 enables stable antiparallel microtubule overlaps. |

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER PTHR19321 metadata/entries, UniProt (Q9HDY1), ase1 ai-review, GOA IBA annotations, iba_propagation.tsv
