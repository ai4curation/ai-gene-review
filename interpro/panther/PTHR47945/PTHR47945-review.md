# PANTHER Family Review: PTHR47945

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR47945 |
| **Family Name** | Cytochrome P450 84A |
| **InterPro Entry** | IPR053062 |
| **Total Proteins** | 1,463 |
| **Taxonomic Breadth** | 1,044 taxa |
| **Subfamilies** | 5 |
| **Representative Structure** | none |
| **Module role** | Provides **F5H (ferulate/coniferaldehyde 5-hydroxylase, CYP84A)**, the syringyl-lignin branch hydroxylase. Exemplar: `UniProtKB:Q42600 (C84A1_ARATH, FAH1)`, PANTHER `PTHR47945:SF5`; function `GO:0046424 ferulate 5-hydroxylase activity`. |

## Executive Summary

PTHR47945 is the **CYP84A** family of plant cytochrome P450 heme-thiolate monooxygenases. Its lignin-module activity is **ferulate 5-hydroxylase / coniferaldehyde 5-hydroxylase (F5H, EC 1.14.-.-)**, which 5-hydroxylates coniferaldehyde/coniferyl alcohol (and ferulate) en route to sinapyl monolignols. F5H is the gateway to **syringyl (S) lignin**: its activity level largely determines the S/G ratio of lignin, making it a central target for altering lignin composition in bioenergy crops.

This is a **small, dedicated, plant-restricted family** (1,463 proteins, 5 subfamilies, ~1,044 taxa) whose CYP84A circumscription is essentially the F5H clade. The metadata notes at least one divergent activity in the family (a *p*-coumaraldehyde→caffealdehyde step associated with arabidopyrone biosynthesis), indicating minor neofunctionalization within CYP84A.

## Subfamily Analysis

The exemplar FAH1/CYP84A1 (Q42600) belongs to `PTHR47945:SF5` (CYTOCHROME P450 84A1-RELATED). The reviewed entries resolve essentially a single subfamily (the CYP84A/F5H clade); the family has only 5 subfamilies total. Unlike the broad-superfamily lignin modules, the parent name (Cytochrome P450 84A) reflects the same F5H-associated CYP84A activity rather than a different ancestral function — so the family is close to homogeneous, though not exclusively F5H (e.g. CYP84A4-type members with the arabidopyrone-related activity).

## IBA / PAINT Assessment

Local PAINT (`PTHR47945-paint.tsv`) has a single IBD node:

| Node (PTN) | GO term | Aspect | Interpretation |
|------------|---------|--------|----------------|
| PTN001548160 | `GO:0004497 monooxygenase activity` | F | Angiosperm (taxon:3398) CYP84A node; seeds AT4G36220 (FAH1/CYP84A1) and AT5G04330 (CYP84A4). |

The PAINT node propagates only the generic `GO:0004497 monooxygenase activity`, not the specific `GO:0046424 ferulate 5-hydroxylase activity`. Because the seed set mixes the canonical F5H (CYP84A1) with a divergent CYP84A4 member, the conservative generic MF is appropriate.

## InterPro2GO / parent-family mapping verdict

This family is narrow and nearly homogeneous, so a family-level **monooxygenase** MF (`GO:0004497`, as PAINT assigns) is broadly safe. However, whole-protein mapping of the **specific** `GO:0046424 ferulate 5-hydroxylase activity` at the parent level is **not** fully safe, because at least one CYP84A subfamily member (CYP84A4) carries a divergent hydroxylase activity. Best practice is to keep the specific F5H function at the **F5H subfamily / PAINT node (`PTHR47945:SF5` / PTN001548160)** and let the family-level term remain the generic monooxygenase activity. The narrow taxonomic and structural scope makes parent-level F5H a low-risk approximation, but SF-level restriction is the defensible choice.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
