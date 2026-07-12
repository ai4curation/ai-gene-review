# PANTHER Family Review: PTHR47948

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR47948 |
| **Family Name** | Cytochrome P450 CYP73A |
| **InterPro Entry** | none (not integrated) |
| **Total Proteins** | 1,867 |
| **Taxonomic Breadth** | 1,453 taxa |
| **Subfamilies** | 9 |
| **Representative Structure** | 6vby (cinnamate 4-hydroxylase C4H1 from *Sorghum bicolor*) |
| **Module role** | Provides **C4H (cinnamate 4-hydroxylase, CYP73A)**, the second step of the general phenylpropanoid pathway. Exemplar: `UniProtKB:P92994 (TCMO_ARATH, CYP73A5/REF3)`, PANTHER `PTHR47948:SF4`; function `GO:0016710 trans-cinnamate 4-monooxygenase activity`. |

## Executive Summary

PTHR47948 is the **CYP73A** family of plant cytochrome P450 heme-thiolate monooxygenases. Its defining activity is **cinnamate 4-hydroxylase (C4H, EC 1.14.14.91)**, which hydroxylates *trans*-cinnamate at the para (4-) position to give *p*-coumarate. This is the first oxidative step of the phenylpropanoid pathway, sitting between PAL and 4CL, and it channels carbon toward *p*-coumaroyl-CoA and hence the monolignols that polymerize into lignin (as well as flavonoids and other phenolics).

Unlike the broad ancestral superfamilies seen in other lignin-module families, PTHR47948 is a **narrow, dedicated, plant-restricted CYP73A family** (1,867 proteins, 9 subfamilies, ~1,453 taxa). The family circumscription (CYP73A) is essentially coextensive with C4H. Some divergence exists — e.g. the reviewed entries include a `PTHR47948:SF3` member annotated as taxane 2'-alpha-hydroxylase — indicating a small degree of neofunctionalization within the CYP73A scaffold.

## Subfamily Analysis

The C4H exemplar CYP73A5/REF3 (P92994) belongs to `PTHR47948:SF4` (TRANS-CINNAMATE 4-MONOOXYGENASE), the canonical C4H subfamily; most reviewed members labelled "C4H"/"C4H1"/"C4H2" fall here. The family has 9 subfamilies total; at least one (`PTHR47948:SF3`) captures a divergent hydroxylase activity (taxane 2'-alpha-hydroxylase), so the family is nearly — but not perfectly — homogeneous for C4H. The parent name (Cytochrome P450 CYP73A) reflects the same C4H-type activity rather than a different ancestral function, which distinguishes this family from the broad-superfamily lignin modules.

## IBA / PAINT Assessment

Local PAINT (`PTHR47948-paint.tsv`) has a single IBD node:

| Node (PTN) | GO term | Aspect | Interpretation |
|------------|---------|--------|----------------|
| PTN001548296 | `GO:0016710 trans-cinnamate 4-monooxygenase activity`; `GO:0009808 lignin metabolic process` | F/P | Angiosperm (taxon:3398) C4H clade; seeds = Q94IP1 and Arabidopsis AT2G30490. |

The propagation is exactly on target: it assigns the specific C4H molecular function and the lignin-metabolic process to the plant C4H node, consistent with the family's module role. No mis-propagation onto divergent siblings is present in the local data.

## InterPro2GO / parent-family mapping verdict

This is the closest of the lignin-module families to a **parent-level-safe** whole-protein mapping: the family is small, plant-restricted, and its CYP73A circumscription is nearly synonymous with C4H, and PAINT propagates the specific `GO:0016710` at the C4H node. However, because at least one subfamily (`:SF3`) has a divergent hydroxylase activity, strict best practice is to keep `GO:0016710 trans-cinnamate 4-monooxygenase activity` at the **C4H subfamily / PAINT node (SF4 / PTN001548296)** rather than blanket-mapping every family member. Parent-level mapping is defensible as a low-risk approximation, but SF/PAINT-level restriction avoids over-annotating the neofunctionalized minority.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
