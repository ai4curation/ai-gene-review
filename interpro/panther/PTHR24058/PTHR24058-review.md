# PANTHER Family Review: PTHR24058

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR24058 |
| **Family Name** | Serine/threonine and dual-specificity kinase (DUAL SPECIFICITY PROTEIN KINASE) |
| **InterPro Entry** | IPR050494 |
| **Total Proteins** | 33,682 |
| **Taxonomic Breadth** | 9,510 taxa |
| **Subfamilies** | 29 |
| **Representative Structure** | 6s14 (Crystal structure of DYRK1A with small molecule inhibitor) |
| **Anchor gene (S. pombe)** | pom1 (Q09690), subfamily PTHR24058:SF132 |

## Executive Summary

PTHR24058 is a large family of **CMGC-group serine/threonine and dual-specificity protein kinases** that includes the **DYRK** (dual-specificity tyrosine-phosphorylation-regulated kinases), **HIPK** (homeodomain-interacting protein kinases), **PRP4/PRPF4B** pre-mRNA splicing kinases, and the fungal cell-polarity kinase **Pom1**. The defining biochemical feature of the DYRK branch is dual specificity: members autophosphorylate on a tyrosine in their activation loop during translation and then act as proline-directed serine/threonine kinases on exogenous substrates.

Despite a shared catalytic core, the family is strongly **neo/subfunctionalized**: subfamilies act in distinct compartments and processes (nuclear splicing regulation for PRP4; transcriptional co-regulation for HIPK; cell-cycle, stress-granule and developmental signaling for DYRK; cortical cell-polarity/cell-size control for Pom1). Functional annotations are therefore appropriate only when restricted to the correct subfamily; the catalytic and ATP-binding molecular-function terms are conserved family-wide, but compartment/process terms are not.

## Subfamily Analysis

### PTHR24058:SF132 - DYRK-FAMILY KINASE POM1 (ANCHOR SUBFAMILY)
**Members**: Pom1 and close fungal orthologs (the S. pombe anchor, Q09690, is the representative).

**Function**: Pom1 is a DYRK-family dual-specificity kinase that acts as a **cortical cell-end marker** in fission yeast. It forms a plasma-membrane concentration gradient highest at cell tips, couples cell geometry to mitotic timing (via inhibition of Cdr2/Cdr1 -> Wee1) and to division-plane positioning (via Mid1 and the F-BAR protein Cdc15), and promotes bipolar growth (NETO) through control of the Cdc42 GAP Rga4.

**Notes**: This is a fungal-specific branch. Critically, **Pom1 is a peripheral plasma-membrane/cell-cortex kinase, not a cytoskeletal or nuclear protein** - this distinguishes it from the metazoan DYRK and PRP4 subfamilies and is central to the IBA assessment below.

### PTHR24058:SF103 - SERINE/THREONINE-PROTEIN KINASE PRP4 HOMOLOG
**Members**: ~7 proteins (largest annotated subfamily in this sample), e.g. human PRP4K/PRPF4B (Q13523), mouse Prp4k (Q61136), rat Prp4k (Q5RKH1), Bos taurus PRP4K (Q08DZ2), Dictyostelium prp4k (Q54WE5), and S. pombe prp4 (Q07538).

**Function**: Nuclear pre-mRNA splicing kinases that phosphorylate spliceosomal substrates (e.g. Prp6/Prp31) and contribute to spliceosome assembly and kinetochore function.

**Notes**: Predominantly **nuclear**; localization terms from this subfamily should not be transferred to cortical members such as Pom1.

### PTHR24058:SF121 - DUAL SPECIFICITY TYROSINE-PHOSPHORYLATION-REGULATED KINASE 1A (DYRK1A)
**Members**: ~5 proteins, e.g. human DYRK1A (Q13627), mouse Dyrk1a (Q61214), rat Dyrk1a (Q63470), Xenopus dyrk1a (Q0IJ08, Q2TAE3).

**Function**: Proline-directed dual-specificity kinase central to neuronal development; the human gene is dosage-sensitive (Down syndrome critical region). Acts on many substrates including transcription factors and splicing factors.

### PTHR24058:SF35 - DUAL SPECIFICITY TYROSINE-PHOSPHORYLATION-REGULATED KINASE 3 (DYRK3)
**Members**: ~4 proteins, e.g. human DYRK3 (O43781), mouse Dyrk3 (Q922Y0), rat Dyrk3 (Q4V8A3), Macaca DYRK3 (Q4R6S5).

**Function**: DYRK3 is a "dissolvase" kinase that regulates the assembly/disassembly of membraneless organelles (stress granules, the pericentriolar material) and mTORC1 signaling. **This subfamily is the source of the cytoskeleton-related localization IBA discussed below.**

### Other subfamilies (HIPK branch)
HIPK subfamilies (SF17, SF43-SF53, SF45, SF46) encode homeodomain-interacting protein kinases acting as nuclear transcriptional co-regulators and DNA-damage-response kinases; SF22/SF51/SF112 are additional DYRK paralogs; SF28 (minibrain/MNB) is the insect DYRK1A ortholog.

## Functional Diversity Assessment

- **Conserved family-wide (safe to propagate):** ATP binding and protein kinase / protein serine/threonine kinase / dual-specificity kinase catalytic activity (the catalytic core is shared by all members).
- **Subfamily-specific (do NOT propagate broadly):** subcellular localization (nucleus for PRP4/HIPK; stress granules/centrosome for DYRK3; cell cortex/plasma membrane for Pom1) and downstream biological processes (splicing, transcription, neuronal development, cell-size control).

## IBA Annotation Assessment

Two IBA (GO_REF:0000033) annotations were propagated to the anchor gene **pom1 (Q09690, subfamily SF132)** via PANTHER node PTN008603465. Both are **cross-subfamily localization transfers**, and the seed evidence comes from non-cortical DYRK paralogs.

| GO ID | Label | Aspect | Seed subfamilies (other_sf) | Our action |
|-------|-------|--------|-----------------------------|------------|
| GO:0005737 | cytoplasm | CC | PTHR24058:SF35; PTHR24058:SF51 (2 seeds, 0 same-SF) | **KEEP_AS_NON_CORE** |
| GO:0005856 | cytoskeleton | CC | PTHR24058:SF35 (1 seed, 0 same-SF) | **REMOVE** |

**GO:0005856 (cytoskeleton) - REMOVE (KNOWN TRUE POSITIVE error).**
This is a genuine cross-subfamily over-propagation. The single seed for this term lies in **SF35 (DYRK3)**, none in Pom1's own SF132. DYRK3 associates with the pericentriolar material/centrosome and cytoskeleton-linked condensates, so a cytoskeleton location is reasonable *for DYRK3*. **Pom1, by contrast, is a peripheral plasma-membrane/cell-cortex kinase** whose gradient emanates from cell tips; its delivery depends on the Tea1-Tea4 microtubule landmark system but Pom1 is not itself a structural component of the cytoskeleton. The IBA is therefore an over-annotation propagated across an inappropriate functional boundary and is removed in the pom1 review. (See `genes/SCHPO/pom1/pom1-ai-review.yaml`, GO:0005856, action REMOVE.)

**GO:0005737 (cytoplasm) - KEEP_AS_NON_CORE.**
The two seeds lie in SF35 and SF51 (DYRK paralogs), again outside SF132. The term is not wrong - Pom1 is a cytoplasmic-face cortical protein - but it is far less specific and informative than the experimentally supported cell-cortex-of-cell-tip / plasma-membrane / site-of-polarized-growth locations. It is retained as non-core rather than removed because a cytoplasmic assignment is biologically defensible.

**Calibration note.** This family illustrates the difference between the conserved-catalysis case and the localization-transfer risk. We do not challenge the conserved kinase molecular-function terms, but localization IBAs propagated from metazoan DYRK paralogs to the cortical fungal Pom1 require subfamily-aware review, and one (cytoskeleton) is a clear positive error.

## Key Considerations for Curators

1. Family-wide propagation is appropriate only for the catalytic/ATP-binding molecular-function terms.
2. Localization and process terms must be gated by subfamily; nuclear (PRP4/HIPK), stress-granule/centrosomal (DYRK3) and cortical (Pom1) compartments are mutually exclusive.
3. The Pom1 cytoskeleton IBA (GO:0005856) is a documented false transfer from the DYRK3 subfamily and should not be propagated to cortical fungal members.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, S. pombe pom1 curated review, GOA IBA annotations, PANTHER_IBA_REVIEW propagation table
