# PANTHER Family Review: PTHR11440

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR11440 |
| **Family Name** | AB hydrolase superfamily Lipase (LCAT-like; AB_hydrolase_Lipase) |
| **InterPro Entry** | none (no integrated InterPro entry) |
| **Total Proteins** | 13,618 |
| **Taxonomic Breadth** | 10,891 taxa; 4,367 proteomes (spans apicomplexa, fungi, plants, metazoa) |
| **Subfamilies** | 26 |
| **Module role** | Acyl-CoA-**independent** TAG route — phospholipid:diacylglycerol acyltransferase (PDAT) transferring an sn-2 acyl group from phospholipid onto DAG to form triacylglycerol. Exemplar: `UniProtKB:Q9FNA9 (PDAT1_ARATH)` (PANTHER subfamily not assigned in local entries); module function `GO:0046027 phospholipid:diacylglycerol acyltransferase activity` |

## Executive Summary

PTHR11440 is an **α/β-hydrolase-fold (LCAT-like) acyltransferase/lipase family** built around a Ser-Asp-His catalytic triad. Its best-characterized members are the plasma/extracellular **lecithin:cholesterol acyltransferases (LCAT)**, which esterify cholesterol on lipoproteins, plus the lysosomal phospholipase A2/acyltransferase **PLA2G15**. The family also contains the plant/fungal **phospholipid:diacylglycerol acyltransferases (PDAT)**.

In seed oil biosynthesis the relevant member is **PDAT1** (Arabidopsis PDAT1, Q9FNA9). PDAT provides the **acyl-CoA-independent route to triacylglycerol**: rather than using acyl-CoA (as DGAT1/DGAT2 do), it transfers an acyl group from the sn-2 position of a phospholipid (e.g. phosphatidylcholine) directly onto diacylglycerol, yielding TAG and a lysophospholipid (`GO:0046027`). This route is important for channeling PC-modified/unusual fatty acids into seed oil and is partially redundant with DGAT1 in Arabidopsis. PDAT sits within a family whose ancestral/dominant activity is sterol esterification (LCAT) — so, like the DGAT1/MBOAT case, the family name and the bulk of members describe a different activity from the seed-TAG module enzyme.

## Subfamily Analysis

- **Exemplar subfamily**: In the local entries table the PANTHER subfamily column is **blank for all members**, so the PDAT1 subfamily assignment is **not determined here** (anchor records it as "PTHR11440, SF n/a"). PDAT relatives present include Arabidopsis PDAT1 (Q9FNA9), PDAT2 (Q9FYC7), yeast LRO1 (P40345), and S. pombe plh1 (O94680).
- **Broad parent**: 26 subfamilies across **10,891 taxa** spanning **apicomplexa (Plasmodium surface phospholipase), fungi, plants and metazoa** — cross-lineage. The family mixes **LCAT cholesterol esterification** (mammalian LCAT, e.g. human P04180), **lysosomal PLA2/acyltransferase PLA2G15**, plant LCAT-like proteins (LCAT1/3/4, PSAT), and the **PDAT/LRO1 TAG-forming acyltransferases** — i.e. genuinely distinct physiological activities on one α/β-hydrolase scaffold.

## IBA / PAINT Assessment

No local PAINT IBD data available for this family (`PTHR11440-paint.tsv` is not present). PANTHER PTN node identifiers and propagated terms are therefore not determined here.

## InterPro2GO / parent-family mapping verdict

**Do NOT map `GO:0046027 phospholipid:diacylglycerol acyltransferase activity` at the parent-family level.** PTHR11440 is a broad, cross-lineage α/β-hydrolase LCAT-like family whose dominant/ancestral activity is **cholesterol esterification (LCAT)**, with additional lysosomal phospholipase (PLA2G15) and plant LCAT-like members. A whole-protein PDAT mapping would over-annotate the LCAT/PLA2G15/PSAT members. The PDAT module function is safe only at the **PDAT/LRO1 subfamily (or PAINT-node) level** — and since the local entries do not assign the PDAT1 subfamily id, that grouping should be confirmed against the current PANTHER subfamily tree before any specific-MF propagation. Family-wide, only a generic lecithin/phospholipid acyltransferase (α/β-hydrolase LCAT-like) activity is defensible.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, plant bioenergy module curation (no local PAINT available)
