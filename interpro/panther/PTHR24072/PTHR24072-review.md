# PANTHER Family Review: PTHR24072

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR24072 |
| **Family Name** | RHO FAMILY GTPASE |
| **InterPro Entry** | IPR003578 (Small GTPase Rho domain) |
| **Total Proteins** | 51,615 |
| **Taxonomic Breadth** | 9,604 taxa |
| **Subfamilies** | 98 |
| **Representative Structure** | 5o33 (GEF Kalirin DH1 domain in complex with the small GTPase Rac1) |
| **Anchor gene (S. pombe)** | cdc42 (Q01112), no subfamily assignment in UniProt/entries |

## Executive Summary

PTHR24072 is the **Rho-family of small (monomeric) GTPases**, molecular switches that cycle between an inactive GDP-bound and an active GTP-bound state. Activation is catalyzed by guanine-nucleotide exchange factors (GEFs) and inactivation is accelerated by GTPase-activating proteins (GAPs); a C-terminal CAAX prenylation motif anchors most members to the cytoplasmic face of membranes. In the GTP-bound state they bind CRIB/effector domains to control actin cytoskeleton dynamics, cell polarity, membrane trafficking and signaling.

The family contains the canonical Rho subfamilies - **CDC42**, **RAC** (RAC1/2/3), **RHO** (RHOA/B/C), the atypical **RND** (RND1/2/3, constitutively GTP-bound), **RHOU/RHOV/RHOH/RHOF/RHOG/RHOQ**, fungal **RHO1-RHO4**, and the mitochondrial Rho **MIRO/GEM1**. The shared **GTPase molecular function is deeply conserved across the whole family**, which (per the calibration guidance) means cross-subfamily IBA transfer of the core GTPase/binding functions is normally correct; the real review risk is paralog-specific downstream processes and localization.

## Subfamily Analysis

Note: the PTHR24072 entries table in this repository does not carry per-member PANTHER subfamily (SFn) suffixes, so subfamilies are described here by gene-name clade (member counts from `PTHR24072-entries.csv`).

### CDC42 clade (ANCHOR clade)
**Members**: e.g. S. pombe cdc42 (Q01112, anchor), human CDC42 (P60953), mouse Cdc42 (P60766), rat Cdc42 (Q8CFN2), Drosophila Cdc42 (P40793), S. cerevisiae CDC42 (P19073), Candida CDC42 (P0CY33), Eremothecium CDC42 (Q9HF56). CDC42-named proteins are the most numerous in the sampled members.

**Function**: Master regulator of **cell polarity and polarized (tip) growth**. In S. pombe, Cdc42 is activated by GEFs Scd1/Gef1 and inactivated by GAP Rga4, binds CRIB-domain effectors (PAK kinases Shk1/Pak1, Shk2/Pak2; scaffold Scd2; formin For3) to organize the actin cytoskeleton and polarized exocytosis, forms oscillating GTP-Cdc42 zones that set cell width and drive bipolar growth, and acts at the division site and during mating/fusion. Geranylgeranylated at its CAAX cysteine for plasma-membrane anchoring.

### RAC clade (RAC1/RAC2/RAC3)
**Members**: human RAC1 (P63000), RAC2 (P15153), mouse/rat orthologs. Multiple RAC1 and RAC2 entries are present.

**Function**: Lamellipodium formation, NADPH-oxidase regulation (RAC2 in immune cells), membrane ruffling.

### RHO clade (RHOA/RHOB/RHOC)
**Members**: human RHOA (P61586), RHOC (P08134/RHOC entries), RHOB; multiple orthologs across mammals.

**Function**: Stress-fiber and focal-adhesion formation, actomyosin contractility, cytokinesis (animal cells). Fungal RHO1-RHO4 (e.g. S. cerevisiae RHO1) regulate cell-wall integrity and glucan synthase.

### RND clade (RND1/RND2/RND3) and atypical Rho
**Members**: human RND3/RhoE, RND1, and Rhov/RhoV, RhoU, RhoQ, etc.

**Function**: Atypical, often constitutively GTP-bound Rho GTPases that antagonize RhoA signaling; distinct regulation (no classic GTPase cycle).

### MIRO/GEM1 clade
**Members**: Mitochondrial Rho GTPase 1 (GEM1) entries.

**Function**: Mitochondrial Rho (MIRO) - calcium-binding, mitochondrial dynamics/transport; structurally divergent (two GTPase domains plus EF-hands).

## Functional Diversity Assessment

- **Conserved family-wide (safe to propagate):** GTPase/GTP binding activity and the core switch mechanism (calibration: cdc42 GTPase = expected correct across fine subfamilies).
- **Paralog/clade-specific (review carefully):** downstream biological processes (lamellipodia vs. stress fibers vs. polarized tip growth), specific effector bindings, and atypical members (RND constitutively active; MIRO mitochondrial).

## IBA Annotation Assessment

Four IBA (GO_REF:0000033) annotations were propagated to **cdc42 (Q01112)**. Because cdc42 has **no PANTHER subfamily assignment** here, all carry the `GENE_NO_SUBFAMILY` flag - the propagation operates at family level rather than within a fine subfamily.

| GO ID | Label | Aspect | Node | Seeds | Our action |
|-------|-------|--------|------|-------|------------|
| GO:0007015 | actin filament organization | BP | PTN000632671 | 7 (6 in family) | **ACCEPT** |
| GO:0030010 | establishment of cell polarity | BP | PTN008604842 | 1 | **ACCEPT** |
| GO:0006897 | endocytosis | BP | PTN008604842 | 1 | **KEEP_AS_NON_CORE** |
| GO:0019901 | protein kinase binding | MF | PTN008604840 | 1 | **MARK_AS_OVER_ANNOTATED** |

**GO:0007015 (actin filament organization) - ACCEPT.** Strongly supported (7 seeds, including CDC42 and RAC orthologs across FB/MGI/RGD/WB/dictyBase and UniProt P60953). Organizing the actin cytoskeleton is a defining, conserved Rho-family/Cdc42 function and matches the S. pombe curated function (Cdc42 -> For3/PAK -> actin). Correct propagation.

**GO:0030010 (establishment of cell polarity) - ACCEPT.** The single seed (node PTN008604842) is consistent with the central role of Cdc42 in cell polarity - the most strongly documented Cdc42 function in fission yeast (polarized tip growth, oscillating GTP-Cdc42 zones). A conserved, paralog-appropriate process for the CDC42 clade.

**GO:0006897 (endocytosis) - KEEP_AS_NON_CORE.** Endocytosis is a real but peripheral/secondary aspect of Cdc42 biology (actin-dependent endocytic patch dynamics); it is not the core polarity-establishment function, so it is retained as non-core rather than treated as a primary annotation.

**GO:0019901 (protein kinase binding) - MARK_AS_OVER_ANNOTATED.** This is an uninformative generic-binding transfer. Cdc42 does functionally engage kinases (PAK/Shk1, Shk2), but "protein kinase binding" is a low-content MF term that obscures the specific effector mechanism (GTP-dependent CRIB-domain effector binding). Per project guidance to avoid generic protein-binding terms, this is marked as over-annotated in favor of more specific effector-binding descriptions.

**Calibration note.** Consistent with the guidance that cdc42 GTPase function is expected correct across fine subfamilies, no IBA here was removed as a paralog error. The conserved cytoskeletal and polarity processes are accepted; only the generic kinase-binding MF term is flagged, and endocytosis is down-weighted to non-core.

## Key Considerations for Curators

1. Core GTPase activity and actin/polarity processes are conserved across the CDC42/RAC/RHO clades - safe to propagate within the canonical Rho subfamilies.
2. Atypical members (RND clade, MIRO/GEM1) violate the standard GTPase-cycle assumption and should not inherit cycle-dependent or canonical-effector annotations.
3. Generic "protein kinase binding" should be replaced by specific GTP-dependent effector-binding terms.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, S. pombe cdc42 curated review, GOA IBA annotations, PANTHER_IBA_REVIEW propagation table

## Falcon Deep Research Integration (2026-06-28)

**Source:** [PTHR24072-deep-research-falcon.md](PTHR24072-deep-research-falcon.md)

**Falcon verdict:** Falcon treats the current empty parent-family InterPro2GO mapping as appropriate for the broad Rho-family entry, despite conserved GTPase-switch biology, because downstream processes, effector bindings, localization, and atypical members are strongly clade-specific.

**Family-level synthesis:** PTHR24072 covers the Rho-family small GTPases, including CDC42, RAC, RHO, atypical RND/RHOU/RHOV/RHOH/RHOF/RHOG/RHOQ members, fungal RHO clades, and mitochondrial MIRO/GEM1-like proteins. Core GTPase/GTP-binding biology is conserved, while pathway outputs and localization should be reviewed by clade.

**Curation use:** Use this Falcon report as support for conservative parent-family handling: keep broad parent mappings empty or minimal, and place specific GO functions on child entries, PAINT/PTN anchors, or representative members after manual review.