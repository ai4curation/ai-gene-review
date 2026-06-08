# PANTHER Family Review: PTHR48013

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR48013 |
| **Family Name** | Mitogen-activated protein kinase kinase (MAP_kinase_kinase) |
| **InterPro Entry** | (none integrated) |
| **Total Proteins** | 16,190 |
| **Taxonomic Breadth** | 10,162 taxa |
| **Subfamilies** | 24 |
| **Representative Structure** | 8pm3 (MAP2K6 with covalent compound GCL94) |
| **Anchor gene** | *S. pombe* wis1 (P33886), subfamily PTHR48013:SF25 |

## Executive Summary

PTHR48013 is the **MAP kinase kinase (MAP2K / MAPKK / MEK)** family of **dual-specificity protein kinases** that phosphorylate and activate MAP kinases on the activation-loop Thr and Tyr residues, forming the middle tier of the canonical MAP3K → MAP2K → MAPK signaling cascade. The conserved core function is **MAP kinase kinase activity** acting within the **MAPK cascade** (GO:0000165). Members cover the ERK (STE7/MEK1/2), JNK (MKK4/7), and p38 (MKK3/6, PBS2/Wis1) branches across fungi, animals, plants, and protists.

The fission yeast anchor gene **wis1** (P33886) is in subfamily **PTHR48013:SF25 (MAP KINASE KINASE PBS2)**, together with its budding-yeast ortholog *S. cerevisiae* **PBS2** (P08018). Wis1 is the sole MAP2K of the *S. pombe* **stress-activated (SAPK) pathway**: it phosphorylates and activates the p38/Hog1-related MAP kinase Spc1/Sty1 on Thr-171/Tyr-173 in response to osmotic, oxidative, heat, and nutritional stress, and is itself activated by the Wis4/Win1 MAPKKKs (P33886 review; PMID:12181336; PMID:10749922; PMID:9321395; PMID:7859738).

**Key IBA finding (TRUE POSITIVE, correct transfer):** wis1 carries an IBA to **GO:0000165 (MAPK cascade)** flagged CROSS_SUBFAMILY. This transfer is **CORRECT** and we **ACCEPTed** it — wis1 is a bona fide MAP2K and the MAPK cascade is its defining process. This contrasts with cdc7 (PTHR48012), where the same term is an over-annotation. See IBA assessment.

## Subfamily Analysis

Subfamily assignments below are drawn from the curated representative members in `PTHR48013-entries.csv`.

### PTHR48013:SF25 - MAP KINASE KINASE PBS2 (anchor subfamily)
**Representative members**:
- *S. pombe* wis1 (P33886)
- *S. cerevisiae* PBS2 (P08018)

**Function**: The fungal stress/osmotic-pathway MAP2K (Pbs2/Wis1 type). Wis1 activates the Spc1/Sty1 p38-class SAPK; Pbs2 activates Hog1 in the budding-yeast HOG osmoregulatory pathway. This is the anchor subfamily for wis1, and notably the wis1 description records that Wis1 is most closely related to *S. cerevisiae* Pbs2 (PMID:7859738). This is the homologous stress-MAPKK clade.

### PTHR48013:SF9 - DUAL SPECIFICITY MAP KINASE KINASE 5 (STE7/MEK-related)
**Representative members** (large curated subfamily):
- *S. cerevisiae* STE7 (P06784) - mating-pathway MEK
- *Arabidopsis* MKK3 (O80396), MKK7 (Q9LPQ3), MKK9 (Q9FX43)
- *Dictyostelium* mekA (Q55CL6)
- *Leishmania* MKK5 (Q0PKV7), MKK4 (Q9GRT1)

**Function**: ERK/STE7-branch and plant MAP2Ks.

### PTHR48013:SF32 - MITOGEN-ACTIVATED PROTEIN KINASE KINASE 2-LIKE (plant MKK)
**Representative members**:
- *Arabidopsis* MKK1 (Q94A06), MKK2 (Q9S7U9), MKK6 (Q9FJV0)
- rice MKK1 (Q5QN75), moss MKK1a/b/c (A9RWC9, A9SR33, A9S5R3)
- tobacco SIPKK (A0A1S4CGX4)

**Function**: Plant-lineage MAP2Ks for biotic/abiotic stress signaling.

### PTHR48013:SF15 - DUAL SPECIFICITY MAP KINASE KINASE 4 (MKK4/JNK branch)
**Representative members**:
- Human MAP2K4 (P45985), mouse Map2k4 (P47809)
- *C. elegans* mkk-4 (Q20347)

**Function**: JNK-branch MAP2K (MKK4/SEK1).

### PTHR48013:SF12 / SF21 - DUAL SPECIFICITY MAP KINASE KINASE 6 / 3 (p38 branch)
**Representative members**:
- MAP2K6: human (P52564), mouse (P70236), bovine (Q5E9X2), zebrafish (Q9DGE0)
- MAP2K3: human (P46734), mouse (O09110)

**Function**: p38-branch MAP2Ks (MKK6, MKK3). These are the vertebrate counterparts of the stress/p38 pathway and are part of the seed set for the MAPK-cascade transfer to wis1.

### PTHR48013:SF6 - MAP KINASE KINASE MKK1/SSP32-related
**Representative members**:
- *S. cerevisiae* MKK1 (P32490), MKK2 (P32491)

**Function**: Budding-yeast cell-wall-integrity (PKC pathway) MAP2Ks.

### Invertebrate stress-pathway members
- *C. elegans* sek-1 (G5EDF7, SF28), jkk-1 (G5EDT6, SF14).

## Functional Diversity Assessment

PTHR48013 is functionally **coherent** at the molecular level: essentially all members are MAP2Ks that activate a MAPK within a MAPK cascade. Divergence is by **pathway branch** (ERK/STE7, JNK/MKK4-7, p38/MKK3-6 and the fungal stress Pbs2/Wis1, cell-wall MKK1/2) rather than by changed core biochemistry. Because the MAPK-cascade role is conserved family-wide, the BP term GO:0000165 transfers correctly even across subfamilies — the opposite situation from the heterogeneous STE20 family PTHR48012.

## IBA Annotation Assessment

IBA (`GO_REF:0000033`) annotations propagated to wis1 (P33886, subfamily PTHR48013:SF25). Flags and actions from `iba_propagation.tsv`.

| GO ID | Label | Aspect | Flags | Our action |
|-------|-------|--------|-------|------------|
| GO:0000165 | MAPK cascade | BP | CROSS_SUBFAMILY (seeds in SF12, SF21) | **ACCEPT** |
| GO:0071474 | cellular hyperosmotic response | BP | (seed at node PTN001220544) | ACCEPT |

**Assessment**:

- **GO:0000165 (MAPK cascade)** — **ACCEPT (CORRECT cross-subfamily transfer).** The term is flagged `CROSS_SUBFAMILY` because the seeds lie partly in other subfamilies (SF12/MAP2K6 and SF21/MAP2K3, the vertebrate p38-branch MAP2Ks), with additional seeds within wis1's own node (n_seed_in_fam = 2). CROSS_SUBFAMILY is triage, not a verdict: here the transfer is correct because the **entire family consists of MAP2Ks whose defining job is to operate within a MAPK cascade**, and wis1 is the genuine MAP2K of the Sty1/Spc1 SAPK cascade (PMID:10749922: Spc1 is activated by phosphorylation of Thr-171/Tyr-173 carried out by the MEK homologue Wis1; PMID:12181336: Wis1 is the only MAPKK that activates Spc1). The cross-subfamily seeds (p38-branch MAP2Ks) share exactly this conserved process with the p38-class stress pathway that wis1 heads, so the transfer is biologically sound.

  **Contrast with cdc7 (PTHR48012):** the identical GO:0000165 IBA is an over-annotation for cdc7 and we MARK_AS_OVER_ANNOTATED it, because cdc7 is the apical kinase of the GTPase-regulated Septation Initiation Network — not a MAP2K and not part of a MAPK module. The decisive difference is the protein's actual signaling role, not the GO term or the triage flag: in PTHR48013 the MAPK-cascade role is family-wide and conserved, whereas in the heterogeneous STE20 family PTHR48012 it belongs only to the MAP4K members. See `PTHR48012-review.md`.

- **GO:0071474 (cellular hyperosmotic response)** — ACCEPT. Directly consistent with wis1's role: it transduces osmotic stress to Spc1, and the Pbs2/Wis1 stress-MAPKK clade is defined by osmoregulation (PMID:7859738: Wis1 is most closely related to Pbs2, required for osmoregulation; PMID:9321395: integrity of the Wis1-Spc1 pathway is required for survival under extreme osmolarity). Correct subfamily-appropriate transfer.

**Summary**: Both IBA terms transfer correctly to wis1. The MAPK-cascade term is a CORRECT cross-subfamily transfer (ACCEPT) because the MAP2K/MAPK-cascade role is conserved across the whole family — the key contrast with the cdc7 case in PTHR48012, where the same term is an over-annotation.

## Key Literature

| PMID | Key Finding |
|------|-------------|
| PMID:10749922 | Spc1 is activated by phosphorylation of Thr-171/Tyr-173 by the MEK homologue Wis1 |
| PMID:12181336 | Wis1 is the only MAPKK that phosphorylates and activates Spc1 under various stresses; cytoplasmic NES important for stress signaling |
| PMID:9321395 | Integrity of the Wis1-Spc1 pathway is required for survival under heat, osmolarity, oxidation, and nutrient limitation |
| PMID:7859738 | Wis1 is most closely related to *S. cerevisiae* Pbs2, required for osmoregulation |

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, wis1 ai-review.yaml, GOA IBA rows, iba_propagation.tsv
