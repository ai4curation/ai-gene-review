# PANTHER Family Review: PTHR48012

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR48012 |
| **Family Name** | STE20/SPS1-related Proline-Alanine-rich Kinase (STE20/SPS1-PAK) |
| **InterPro Entry** | IPR050629 |
| **Total Proteins** | 32,396 |
| **Taxonomic Breadth** | 10,099 taxa |
| **Subfamilies** | 28 |
| **Representative Structure** | 7l25 (HPK1 in complex with compound 18) |
| **Anchor gene** | *S. pombe* cdc7 (P41892), subfamily PTHR48012:SF26 |

## Executive Summary

PTHR48012 is the **STE20/SPS1-related (GCK/germinal-center-kinase and STE20-like) serine/threonine protein kinase** family. The conserved core function is **protein serine/threonine kinase activity** (GO:0004674). Members participate in a wide range of signaling contexts, including the WNK–SPAK/OSR1 ion-transport cascade, Hippo (MST1/2–STK3/4) growth control, stress-activated MAP4K (MAP kinase kinase kinase kinase) signaling upstream of JNK/p38, and — in fungi — the GTPase-regulated kinase relays that control cytokinesis (the *S. cerevisiae* Mitotic Exit Network and the *S. pombe* Septation Initiation Network).

The fission yeast anchor gene **cdc7** (P41892) is in subfamily **PTHR48012:SF26 (SERINE/THREONINE-PROTEIN KINASE DDB_G0283821-RELATED)**, which also contains *S. cerevisiae* **CDC15** (P27636) — the apical MEN kinase. Cdc7 is the apical kinase of the *S. pombe* **Septation Initiation Network (SIN)**: it is recruited to the spindle pole body by the GTP-bound Spg1 GTPase and initiates the SIN kinase cascade (Cdc7 → Sid1–Cdc14 → Sid2–Mob1) that triggers cytokinesis and septum formation (P41892 review; PMID:12546793; PMID:8039497).

**Key IBA finding (TRUE POSITIVE over-annotation):** cdc7 carries an IBA to **GO:0000165 (MAPK cascade)**. This is biologically incorrect for cdc7 and we **MARK_AS_OVER_ANNOTATED**. The SIN is a GTPase-regulated (Spg1) kinase relay, NOT a MAPK cascade; cdc7 is not a MAP kinase kinase kinase and does not feed a MAPK module. See IBA assessment below.

## Subfamily Analysis

Subfamily assignments below are drawn from the curated representative members in `PTHR48012-entries.csv`.

### PTHR48012:SF26 - SERINE/THREONINE-PROTEIN KINASE DDB_G0283821-RELATED (anchor subfamily)
**Representative members**:
- *S. pombe* cdc7 (P41892)
- *S. cerevisiae* CDC15 (P27636) - apical Mitotic Exit Network kinase
- *Dictyostelium* sepA (Q8T2I8), DDB_G0293184 (Q54C77), DDB_G0284251 (Q54PX0), DDB_G0270146 (Q55CA6)

**Function**: Fungal/amoebal GTPase-regulated cytokinesis-initiating kinases. The two best-characterized members — *S. pombe* cdc7 (SIN) and *S. cerevisiae* Cdc15 (MEN) — are the apical kinases of the homologous septation/mitotic-exit relays, recruited to the spindle pole body by a Ras-family GTPase (Spg1/Tem1). This is the anchor subfamily for cdc7.

### PTHR48012:SF2 - STERILE20-LIKE KINASE, ISOFORM B
**Representative members** (largest curated subfamily):
- Human STK4/MST1 (Q13043), STK3/MST2 (Q13188)
- Mouse Stk3 (Q9JI10), Stk4 (Q9JI11)
- *Drosophila* hippo/hpo (Q8T0S6)
- *C. elegans* cst-1 (A8XJW8)
- *S. pombe* ppk2 (Q10447)

**Function**: STE20/MST (Hippo-pathway) kinases controlling growth, apoptosis, and organ size. Distinct signaling context from the anchor.

### PTHR48012:SF10 - FI20177P1 (GCK/SPS1-like)
**Representative members**:
- *S. cerevisiae* SPS1 (P08458) - sporulation-specific kinase, KIC1 (P38692)
- *S. pombe* ppk11 (O14047)
- *Dictyostelium* svkA (O61122), and others

**Function**: SPS1/GCK-type kinases including sporulation and cell-integrity roles.

### PTHR48012:SF14 - STE20/SPS1-RELATED PROLINE-ALANINE-RICH PROTEIN KINASE (SPAK/OSR1-related)
**Representative members**:
- Human STK39/SPAK (Q9UEW8), rat Stk39 (O88506), mouse Stk39 (Q9Z1W9)

**Function**: SPAK kinases of the WNK–SPAK/OSR1 ion-cotransporter cascade.

### PTHR48012:SF1 - SERINE/THREONINE-PROTEIN KINASE OSR1
**Representative members**:
- Human OXSR1/OSR1 (O95747), mouse Oxsr1 (Q6P9R2), rat Oxsr1 (A0A8I5ZNK2)

**Function**: OSR1 kinases; with SPAK, effectors of the WNK cascade.

### MAP4K subfamilies (SF15, SF6, SF17, SF19)
**Representative members**: human MAP4K1/HPK1 (Q92918), MAP4K2 (Q12851), MAP4K3 (Q8IVH8), MAP4K5 (Q9Y4K4) and orthologs.

**Function**: MAP kinase kinase kinase kinases (germinal-center kinases) that act *upstream* of MAP3K–MAP2K–MAPK (JNK/p38) modules. NOTE: these members are MAP4Ks (feeding a MAPK cascade), which is the likely seed origin of the MAPK-cascade term that mis-propagates to cdc7 (see below).

### Other fission-yeast members
- *S. pombe* sid1 (O14305, SF27) - SIN kinase downstream of cdc7; nak1 (O75011, SF29); ppk11 (O14047, SF10); ppk2 (Q10447, SF2).

## Functional Diversity Assessment

This is a large, functionally **heterogeneous** kinase family. The single conserved property is Ser/Thr kinase activity (GO:0004674); the *signaling context* differs sharply among subfamilies: Hippo/MST (SF2), WNK–SPAK/OSR1 ion transport (SF1, SF14), MAP4K stress signaling upstream of MAPK modules (SF6/SF15/SF17/SF19), GCK/SPS1 (SF10), and the fungal GTPase-regulated cytokinesis-initiation kinases (SF26, the anchor). Because several subfamilies genuinely operate upstream of MAPK cascades while others (including SF26) do not, process-level BP terms are at high risk of inappropriate cross-subfamily transfer.

## IBA Annotation Assessment

IBA (`GO_REF:0000033`) annotations propagated to cdc7 (P41892, subfamily PTHR48012:SF26). Flags and actions from `iba_propagation.tsv`.

| GO ID | Label | Aspect | Flags | Our action |
|-------|-------|--------|-------|------------|
| GO:0004674 | protein serine/threonine kinase activity | MF | (3 seeds) | ACCEPT |
| GO:0000165 | MAPK cascade | BP | NO_UNIPROT_SEEDS | **MARK_AS_OVER_ANNOTATED** |

**Assessment**:

- **GO:0004674 (protein serine/threonine kinase activity)** — ACCEPT. This is the conserved core molecular function of the entire family and is directly supported for cdc7, whose kinase activity drives mitotic hyperphosphorylation of the SIN scaffold Cdc11 (PMID:12546793). Correct family-level transfer (3 seeds at node PTN004700021).

- **GO:0000165 (MAPK cascade)** — **MARK_AS_OVER_ANNOTATED (KNOWN TRUE POSITIVE).** This BP term is propagated to cdc7 (node PTN001969282, NO_UNIPROT_SEEDS) but is biologically wrong for this protein. The positive biological argument:
  - Cdc7 is the **apical kinase of the Septation Initiation Network (SIN)**, a spindle-pole-body-associated, **GTPase (Spg1)-regulated** kinase relay (Cdc7 → Sid1–Cdc14 → Sid2–Mob1) that triggers cytokinesis and septum formation (P41892 review; PMID:8039497: cdc7 plays a key role in initiation of septum formation and cytokinesis).
  - A **MAPK cascade** (GO:0000165) is the specific MAP3K → MAP2K → MAPK three-tier phosphorylation relay. The SIN is **not** such a module: cdc7 is not a MAP3K, it does not phosphorylate a MAP2K, and the SIN does not terminate in a MAP kinase.
  - The most plausible source of this transfer is the **MAP4K members of other subfamilies** in this family (SF6/SF15/SF17/SF19, the HPK1/MAP4K1–5 germinal-center kinases), which genuinely act upstream of MAPK cascades. This is a classic case of a process term that is correct for some paralogs in the family being mis-transferred across subfamilies to a kinase with a different signaling role.

**Contrast with wis1 (PTHR48013):** the *same* GO:0000165 IBA is **CORRECT** for wis1 and we ACCEPTed it, because wis1 is the genuine MAP2K of the Sty1/Spc1 SAPK cascade. The divergent outcomes for the same GO term in two related kinase families illustrate why MAPK-cascade transfers must be evaluated against the specific protein's signaling role rather than accepted family-wide. See `PTHR48013-review.md`.

**Summary**: The kinase-activity MF transfers correctly to cdc7. The MAPK-cascade BP is a genuine cross-subfamily over-annotation (MARK_AS_OVER_ANNOTATED): cdc7 drives the GTPase-regulated SIN, not a MAPK module, and the term likely originates from the MAP4K members elsewhere in this large heterogeneous kinase family.

## Key Literature

| PMID | Key Finding |
|------|-------------|
| PMID:12546793 | Mitotic hyperphosphorylation of Cdc11 requires Cdc7 kinase activity; dephosphorylation requires PP2A-Par1 |
| PMID:8039497 | p120cdc7 kinase plays a key role in initiation of septum formation and cytokinesis in fission yeast |

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, cdc7 ai-review.yaml, GOA IBA rows, iba_propagation.tsv
