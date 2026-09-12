# PANTHER Family Review: PTHR32285

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR32285 |
| **Family Name** | PROTEIN TRICHOME BIREFRINGENCE-LIKE 9-RELATED |
| **InterPro Entry** | IPR029962 |
| **Total Proteins** | 29,799 |
| **Taxonomic Breadth** | 1,848 taxa |
| **Subfamilies** | 175 |
| **Representative Structure** | 6cci (Crystal structure of XOAT1) |
| **Module role** | Xylan backbone acetylation (secondary cell wall glucuronoxylan/GAX). 2-O / 3-O acetylation of xylose residues in the xylan backbone. Exemplar: `UniProtKB:Q9LY46 (TBL29_ARATH)` (ESK1 / XOAT1) at PTHR32285:SF10. Associated function `GO:1990538 xylan O-acetyltransferase activity`. |

## Executive Summary

PTHR32285 is the **TBL (TRICHOME BIREFRINGENCE-LIKE) / DUF231** family, a large plant-specific group of Golgi-membrane **polysaccharide O-acetyltransferases** carrying the GDSL-like/DUF231 (PC-CBM/TBL) architecture. Members transfer acetyl groups from an acetyl donor onto the hydroxyls of diverse cell-wall polysaccharides, with each subfamily tuned to a different acceptor: **xylan (ESK1/TBL29 and the XOAT series), xyloglucan (AXY4/AXY4L and poplar XGOATs), pectin, and mannan**, plus TBR/PMR5 members affecting wall acetylation and disease resistance.

In glucuronoxylan/GAX biosynthesis, **ESK1/TBL29 (XOAT1)** is the principal **xylan O-acetyltransferase**, adding 2-O- and 3-O-acetyl esters to backbone xylosyl residues; the *eskimo1* mutant shows collapsed xylem and reduced xylan acetylation. Xylan acetylation is a major backbone modification (alongside GlcA branching by GUX and its methylation by GXM), and its extent strongly influences biomass recalcitrance to enzymatic saccharification, making the xylan-acetylating members of this family key bioenergy targets. Because the family also acetylates non-xylan polymers, the specific "xylan O-acetyltransferase" role is a property of particular subfamilies (notably SF10), not of the family as a whole.

## Subfamily Analysis

The exemplar **ESK1/TBL29 (Q9LY46) is in PTHR32285:SF10** ("XYLAN O-ACETYLTRANSFERASE 1"), which also contains rice XOAT1 (Q8S237) and XOAT2 (B9FKP6) — a coherent xylan-acetyltransferase subfamily. Other subfamilies encode acetyltransferases for **different substrates**: xyloglucan O-acetyltransferases (AXY4/O04523 and AXY4L/Q9LRS2 in SF57/SF28; poplar XGOATs), and the many TBL1-TBL46 members (SF8, SF11, SF12, SF14=PMR5, SF22=TBR, etc.) associated with pectin/other wall acetylation. Rice XOAT members are distributed across several subfamilies (SF10, SF37, SF67, SF276, SF285, SF327, SF370, etc.).

This is the **largest and most subfamily-rich parent** in the xylan-module set (175 subfamilies), but taxonomically **restricted to land plants/green lineage** (1,848 taxa) — it does not span kingdoms. The breadth here is in *substrate diversity across paralogous subfamilies within plants*, not phylogenetic span.

## IBA / PAINT Assessment

Local PAINT IBD data are available (`PTHR32285-paint.tsv`), with **two IBD propagations from a single node, PTN000792257** (all `IBD`, not negated, dated 2022-09-25, `taxon:` blank):

| Family | Node | GO ID | GO Label | Aspect | Negated | Seeds (n) |
|--------|------|-------|----------|--------|---------|-----------|
| PTHR32285 | PTN000792257 | GO:0016413 | O-acetyltransferase activity | F | false | ~24 (e.g. UniProtKB:Q8S237 XOAT1, B9FKP6 XOAT2, Q2QYU2/Q2RBL8 XOAT12/13, A0A2K1X4I9 XGOAT4, plus many AGI loci) |
| PTHR32285 | PTN000792257 | GO:0005794 | Golgi apparatus | C | false | ~10 AGI loci + UniProtKB:Q2QYU2 |

The propagated molecular function is the **general parent term `GO:0016413 O-acetyltransferase activity`, NOT the specific `GO:1990538 xylan O-acetyltransferase activity`.** This is appropriate and cautious: the seed set for the MF node mixes xylan-acetylating (XOAT) and xyloglucan-acetylating (XGOAT) members, so PAINT correctly generalizes to the shared O-acetyltransferase activity rather than asserting the xylan-specific reaction across the node. The Golgi CC term is consistent with the known Golgi localization of these wall-polysaccharide acetyltransferases. PTN node id: **PTN000792257** (single node for both terms).

## InterPro2GO / parent-family mapping verdict

A **whole-protein GO mapping of the xylan-specific activity at the PARENT level is NOT safe**, and the local PAINT data already reflect the correct practice. `GO:1990538 xylan O-acetyltransferase activity` applies only to the xylan-acetylating subfamilies (notably SF10 / ESK1-XOAT1, and other XOAT subfamilies), whereas sibling subfamilies acetylate xyloglucan (AXY4/XGOAT), pectin, or mannan. The safe parent/PAINT-level term is the **general `GO:0016413 O-acetyltransferase activity`** (exactly what PTN000792257 propagates), optionally with the Golgi CC. The **xylan-specific function must be assigned at the SF/subclade or curated-member level** (e.g. SF10 for ESK1/XOAT1, other XOAT subfamilies), never as a whole-protein parent mapping. **Verdict: general O-acetyltransferase at parent/PAINT level (already done); xylan O-acetyltransferase only at SF level.**

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT (PTHR32285-paint.tsv), UniProt, plant bioenergy xylan-module curation
