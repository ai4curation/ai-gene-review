# PANTHER Family Review: PTHR22974

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR22974 |
| **Family Name** | Serine/Threonine and Dual Specificity Protein Kinases |
| **InterPro Entry** | (none integrated in metadata) |
| **Total Proteins** | 12,711 |
| **Taxonomic Breadth** | 9,745 taxa |
| **Subfamilies** | 10 |
| **Representative Structure** | 4js8 (Crystal structure of TTK kinase domain with an inhibitor) |
| **Anchor Gene** | S. pombe mph1 / Mps1 (O94235) |

## Executive Summary

PTHR22974 groups **Ser/Thr and dual-specificity protein kinases** built on the canonical eukaryotic protein-kinase fold, dominated by two functionally distinct clades: the **Mps1/TTK** dual-specificity checkpoint kinases and the **Tousled-like kinases (TLK)**. The shared conserved core is **protein kinase activity** (ATP-dependent phosphotransfer onto Ser/Thr, with Tyr autophosphorylation in the Mps1/TTK members).

Functionally the family is **neofunctionalized**: the **Mps1/TTK** clade is the apical kinase of the **spindle assembly checkpoint (SAC)**, phosphorylating the outer-kinetochore KNL1/Spc7 MELT repeats to recruit Bub1-Bub3 and build the "wait-anaphase" signal; the **Tousled-like kinase** clade acts in **chromatin assembly / DNA replication and repair**, phosphorylating the histone chaperone ASF1. The two clades share catalysis but not biological process. The fission-yeast anchor **mph1** is the Mps1/TTK checkpoint kinase.

## Subfamily Analysis

Based on the family entry table (20 members with PANTHER subfamily IDs):

### PTHR22974:SF21 — DUAL SPECIFICITY PROTEIN KINASE TTK (Mps1/TTK)  *(ANCHOR SUBFAMILY)*
**Members**: 9 (largest sampled subfamily)

**Key Members**:
- **S. pombe mph1 (O94235)** — the anchor (a.k.a. Mps1)
- Human TTK/Mps1 (P33981), mouse Ttk (P35761)
- S. cerevisiae MPS1 (P54199)
- Arabidopsis MPS1 (Q84VX4), Dictyostelium mps1 (Q54UL8)
- Zebrafish ttk (Q8AYG3), *Encephalitozoon cuniculi* MPS1 (Q8SSH4)

**Function**: Apical **spindle assembly checkpoint** kinase; dual-specificity (Ser/Thr with Tyr autophosphorylation). Phosphorylates KNL1/Spc7 MELT motifs to recruit Bub1-Bub3, gating the metaphase-to-anaphase transition. This is the anchor gene's subfamily, populated by bona fide Mps1/TTK orthologs across eukaryotes.

### PTHR22974:SF20 / SF22 / SF23 / SF32 — TOUSLED-LIKE KINASES (TLK1/TLK2)
**Members**: SF23 (4), SF20 (4), SF22 (2), SF32 (1).

**Key Members**:
- Serine/threonine-protein kinase Tousled-like 1 and 2 (TLK1/TLK2) orthologs

**Function**: Cell-cycle-regulated Ser/Thr kinases acting in **chromatin assembly, DNA replication and repair** (e.g., ASF1 phosphorylation). Distinct biological role from the Mps1/TTK checkpoint clade despite shared kinase chemistry.

## IBA Annotation Assessment

IBAs (GO_REF:0000033) propagated to mph1, with the PANTHER seed node and our recorded action:

| GO ID | GO label | Aspect | Node | Our action | Assessment |
|-------|----------|--------|------|------------|------------|
| GO:0004712 | protein serine/threonine/tyrosine kinase activity | MF | PTN001122082 | ACCEPT | **CORRECT.** Mps1/TTK kinases are dual-specificity (Ser/Thr + Tyr autophosphorylation); the term is well supported for mph1 and conserved across SF21. |
| GO:0007094 | mitotic spindle assembly checkpoint signaling | BP | PTN001122082 | ACCEPT | **CORRECT.** This is mph1's experimentally established core function (Spc7/KNL1 MELT phosphorylation → Bub1-Bub3 recruitment). Node is the Mps1/TTK clade node. |
| GO:0000776 | kinetochore | CC | PTN001122082 | ACCEPT | **CORRECT (localization flag).** mph1 localizes to (and is enriched at unattached) kinetochores; the CC matches experimental localization. No conflict. |
| GO:0034501 | protein localization to kinetochore | BP | PTN001122082 | ACCEPT | **CORRECT.** Consistent with mph1's role in building the kinetochore-based checkpoint signal. |
| GO:0033316 | meiotic spindle assembly checkpoint signaling | BP | PTN001122082 | KEEP_AS_NON_CORE | **REASONABLE.** mph1 acts in meiosis I (prevents homolog non-disjunction), but the meiotic SAC is a context-specific extension of its core mitotic role; non-core is appropriate. |
| GO:0007059 | chromosome segregation | BP | PTN000540737 | KEEP_AS_NON_CORE | **REASONABLE.** A broad downstream-outcome term seeded from a more inclusive node (PTN000540737) spanning SF20/SF23 (Tousled-like) as well. Demoting to non-core (versus the precise SAC term) is well calibrated; the precise term GO:0007094 carries the core signal. |

**Triage flags.** GO:0007059 (chromosome segregation) carries `CROSS_SUBFAMILY` (other_sf includes PTHR22974:SF20 and SF23, the Tousled-like clade). This is **triage, not a verdict**. Here it is informative rather than alarming: chromosome segregation is a generic outcome term that both the Mps1/TTK and TLK clades can touch, but mph1's *specific* mechanistic contribution is the SAC term GO:0007094 (same-subfamily node), which we accept as core. The cross-subfamily, less-specific term is correctly kept as non-core. The remaining IBAs are all anchored on the Mps1/TTK clade node PTN001122082 and require no change.

**No REMOVE warranted.** Every propagated term is biologically consistent with a fission-yeast Mps1/TTK checkpoint kinase; none transfers a Tousled-like-specific molecular function (e.g., ASF1/chromatin-assembly catalysis) onto mph1.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata, family entry table, S. pombe mph1 UniProt/GOA/AI-review, iba_propagation.tsv
