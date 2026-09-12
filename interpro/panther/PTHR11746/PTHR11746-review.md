# PANTHER Family Review: PTHR11746

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR11746 |
| **Family Name** | O-METHYLTRANSFERASE |
| **InterPro Entry** | IPR016461 |
| **Total Proteins** | 19,450 |
| **Taxonomic Breadth** | 3,340 taxa |
| **Subfamilies** | 123 |
| **Representative Structure** | 5ice ((S)-norcoclaurine 6-O-methyltransferase with SAH and norlaudanosoline) |
| **Module role** | Provides **COMT (caffeic acid / 5-hydroxyconiferaldehyde O-methyltransferase)**, the methylation step feeding syringyl monolignols. Exemplar: `UniProtKB:Q9FK25 (OMT1_ARATH, AtCOMT)`, PANTHER `PTHR11746` (no SF assigned to the exemplar in the reviewed entries); function `GO:0047763 caffeate O-methyltransferase activity`. |

## Executive Summary

PTHR11746 is a large family of **class I SAM-dependent plant O-methyltransferases** (the caffeic-acid-OMT-like fold). Members transfer a methyl group from S-adenosyl-L-methionine to hydroxyl groups of a broad range of phenylpropanoid, flavonoid, and alkaloid substrates.

The lignin-module enzyme is **COMT (caffeic acid 3-O-methyltransferase / 5-hydroxyconiferaldehyde O-methyltransferase, EC 2.1.1.68)**. Despite the "caffeate" name, the physiologically dominant role of COMT in lignification is 5-O-methylation of 5-hydroxyconiferaldehyde (and 5-hydroxyconiferyl alcohol) to sinapaldehyde/sinapyl alcohol — the final methylation required for **syringyl (S) lignin**, complementing F5H. COMT is one specialized subfamily among ~123 in a functionally diverse plant OMT family.

## Subfamily Analysis

The exemplar AtCOMT (Q9FK25) sits in the COMT clade of PTHR11746; the reviewed-entries table does not assign it a distinct `:SF` id (the family resolves 2 broad subfamily groupings in the reviewed set). The family name — **O-METHYLTRANSFERASE** — reflects generic SAM-dependent O-methyl-transfer chemistry, not COMT specifically. With 123 subfamilies acting on many phenolic/alkaloid acceptors, caffeate/5-hydroxyconiferaldehyde specificity is a subfamily-level trait.

## IBA / PAINT Assessment

Local PAINT (`PTHR11746-paint.tsv`) has a single IBD node carrying only generic terms:

| Node (PTN) | GO term(s) | Aspect | Interpretation |
|------------|-----------|--------|----------------|
| PTN000202149 | `GO:0008171 O-methyltransferase activity`; `GO:0008757 S-adenosylmethionine-dependent methyltransferase activity`; `GO:0009058 biosynthetic process`; `GO:0032259 methylation` | F/F/P/P | Broad family node; seeds span plants, animals (rat, mouse), and *Dictyostelium*. |

The specific `GO:0047763 caffeate O-methyltransferase activity` is **not** propagated. Only generic methyltransferase MF and generic biosynthetic/methylation process terms are assigned, consistent with the family's substrate breadth and mixed taxonomy.

## InterPro2GO / parent-family mapping verdict

Whole-protein mapping of `GO:0047763 caffeate O-methyltransferase activity` at the **parent level is unsafe**. PTHR11746 / IPR016461 is a broad plant OMT family (123 subfamilies, ~3,340 taxa, including non-plant seeds) whose members methylate many different phenolic and alkaloid substrates; only the generic `GO:0008171 O-methyltransferase activity` / `GO:0008757 SAM-dependent methyltransferase activity` is defensible family-wide (as PAINT assigns). The COMT-specific activity must be restricted to the **COMT subfamily / a dedicated PAINT node**; no such specific node exists in the local data, so the specific function should be curated from experimental evidence at the subfamily level.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
