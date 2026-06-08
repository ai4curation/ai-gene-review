# PANTHER Family Review: PTHR47102

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR47102 |
| **Family Name** | Actin filament dynamics regulator (formin / BNI1-related) |
| **InterPro Entry** | IPR051661 |
| **Total Proteins** | 2,751 |
| **Taxonomic Breadth** | 3,532 taxa |
| **Subfamilies** | 4 |
| **Anchor Gene** | S. pombe cdc12 (Q10059), subfamily PTHR47102:SF5 |

## Executive Summary

PTHR47102 encodes **formins** of the BNI1/diaphanous lineage — multidomain actin-filament nucleators and processive elongators. The defining functional unit is the formin homology region: a proline-rich **FH1** domain that recruits profilin–actin and a dimeric **FH2** domain that encircles, caps and processively elongates the barbed end of unbranched actin filaments. Family members govern actin-dependent processes including cytokinesis, cell polarity, mating projection growth and cable assembly.

The S. pombe anchor **cdc12** is the single essential cytokinesis formin of fission yeast. Through its FH1/FH2 module it nucleates and elongates the unbranched actin filaments of the cytokinetic actomyosin contractile ring (CAR), with FH1 binding the profilin Cdc3 to deliver profilin–actin (profilin-gated capping). It is recruited early to the medial division site (Mid1 nodes, then the condensing ring, via the F-BAR scaffold Cdc15) and is cell-cycle regulated by Cdk1 and SIN (Sid2) phosphorylation.

The core actin-nucleation/elongation function (FH2-driven) is broadly conserved across the family. The principal axes of variation are **which actin structure** each formin builds (contractile ring vs. interphase cables vs. mating projection) and **where/when** it localizes — these are subfamily- and species-specific and are the main source of over-propagation risk for localization terms.

## Subfamily Analysis

### PTHR47102:SF2 - PROTEIN BNI1
**Members**: 8 proteins (largest subfamily)

**Taxonomy**: Fungi (S. cerevisiae, S. pombe, C. albicans, A. nidulans) plus the *Rickettsia* RickA actin-nucleation effector.

**Key Members**:
- S. cerevisiae BNI1 (P41832)
- S. pombe fus1 (Q10719), rid1 (O74737)
- C. albicans BNI1 (Q5AL52), BNR1 (Q5AAF4)
- A. nidulans sepA (P78621)
- *Rickettsia* RickA (Q9AKJ0, Q92H62) — bacterial actin-nucleating virulence effector

**Function**: Actin filament nucleation/elongation; in budding yeast Bni1 builds polarized actin cables, and S. pombe Fus1 is the mating-specific formin. This subfamily is functionally heterogeneous (polarity, mating, virulence mimicry).

### PTHR47102:SF5 - CELL DIVISION CONTROL PROTEIN 12 (ANCHOR SUBFAMILY)
**Members**: 1 proteins (contains the S. pombe anchor)

**Anchor**: **S. pombe cdc12 (Q10059)** — the essential cytokinesis formin.

**Function**: FH1/FH2-mediated nucleation and processive barbed-end elongation of the unbranched actin filaments of the mitotic actomyosin contractile ring (CAR); cytokinesis and septum formation. This is the contractile-ring-dedicated formin, functionally distinct from the polarity/cable formin (For3, SF3) and the mating formin (Fus1, SF2) of the same organism.

### PTHR47102:SF3 - FORMIN-3
**Members**: 1 proteins

**Key Members**:
- S. pombe for3 (O94532)

**Function**: Interphase formin that nucleates the actin cables required for cell polarity and polarized growth — a distinct cellular role from the cytokinesis formin Cdc12, despite sharing the conserved FH2 elongation mechanism.

### PTHR47102:SF1 - BNI1-RELATED PROTEIN 1
**Members**: 1 proteins

**Function**: BNI1-related formin (Bnr1-type), the second budding-yeast-lineage formin paralog. Same core FH2 nucleation/elongation chemistry, distinct cellular deployment.

## IBA Annotation Assessment

The following IBAs (GO_REF:0000033) are propagated to the anchor **cdc12 (Q10059, PTHR47102:SF5)**. None of these IBAs had UniProt experimental seeds within the family node in the propagation table (`NO_UNIPROT_SEEDS`), so each was judged on biological grounds.

| GO ID | Label | Aspect | Flags | Our action | Assessment |
|-------|-------|--------|-------|-----------|------------|
| GO:0051015 | actin filament binding | MF | NO_UNIPROT_SEEDS | **ACCEPT** | Core, conserved formin property (FH2 binds F-actin). Correct for all members. |
| GO:0051017 | actin filament bundle assembly | BP | NO_UNIPROT_SEEDS | **KEEP_AS_NON_CORE** | Cdc12 nucleates/elongates ring filaments; bundling is a secondary, context-dependent activity (its multimerization/F-actin-bundling domain), so retained but non-core. |
| GO:1903475 | mitotic actomyosin contractile ring assembly | BP | NO_UNIPROT_SEEDS | **ACCEPT** | The defining biological role of the anchor subfamily; well supported for Cdc12. |
| GO:0110085 | mitotic actomyosin contractile ring | CC | LOCALIZATION;NO_UNIPROT_SEEDS | **ACCEPT** | Localization term, but it is exactly where the cytokinesis formin acts; correct for Cdc12 despite the LOCALIZATION triage flag. |
| GO:0043332 | mating projection tip | CC | LOCALIZATION;NO_UNIPROT_SEEDS | **MARK_AS_OVER_ANNOTATED** | This localization belongs to the **mating formin (Fus1/Bni1-type, SF2)**, not to the cytokinesis formin Cdc12. A paralog-specific localization mis-transferred across the family — the genuine localization-transfer risk in this family. |

**Key finding:** The actin-nucleation/elongation **molecular function** and the contractile-ring assembly **process** transfer correctly to the anchor — these are conserved family functions. The one demonstrable over-propagation is the **localization** term *mating projection tip* (GO:0043332): mating-projection growth is the job of the Fus1/Bni1-type formins (SF2), and Cdc12 is the dedicated cytokinesis formin. This matches the calibration rule that localization transfers and paralog-specific functions are the real IBA risks, while conserved catalytic/process terms are normally correct.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER (PTHR47102) metadata and member list, InterPro IPR051661, S. pombe cdc12 UniProt (Q10059), cdc12 GOA IBA rows, cdc12 ai-review.yaml, and the PANTHER_IBA_REVIEW propagation table.
