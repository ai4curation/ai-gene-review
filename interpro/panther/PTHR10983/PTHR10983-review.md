# PANTHER Family Review: PTHR10983

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10983 |
| **Family Name** | 1-acyl-sn-glycerol-3-phosphate acyltransferase (LPAAT / 1-AGP_acyltransferase) |
| **InterPro Entry** | none (no integrated InterPro entry) |
| **Total Proteins** | 15,449 |
| **Taxonomic Breadth** | 12,019 taxa; 5,707 proteomes (spans bacteria, fungi, plants, metazoa) |
| **Subfamilies** | 25 |
| **Module role** | Kennedy pathway **step 2** — sn-2 acylation of lysophosphatidic acid (LPA) to phosphatidic acid (PA). Exemplar: `UniProtKB:Q8LG50 (LPAT2_ARATH)` at **PTHR10983:SF24**; module function `GO:0003841 1-acylglycerol-3-phosphate O-acyltransferase activity` |

## Executive Summary

PTHR10983 is the **1-acyl-sn-glycerol-3-phosphate acyltransferase (LPAAT / AGPAT) family**, membrane-integral HXXXXD-motif acyltransferases that transfer an acyl group onto the sn-2 position of lysophosphatidic acid to form phosphatidic acid (PA). PA is the branch-point intermediate feeding both phospholipid synthesis and, via phosphatidate phosphatase (PAP/lipin) and DGAT, triacylglycerol assembly. The family also contains related lysophospholipid acyltransferases that remodel other lyso-glycerophospholipids (LPGAT, LCLAT/lysocardiolipin acyltransferase, LPIAT).

In seed TAG assembly the key member is **LPAT2** (Arabidopsis LPAT2, Q8LG50), the ER-localized LPAAT that performs Kennedy-pathway step 2 (`GO:0003841`). It is one of several plant LPAT isoforms (the plastidial LPAAT/ATS2 for chloroplast lipids is a separate lineage). The broader family relates the plant enzyme to animal AGPAT3/4/5 (SF9/SF8/SF73), bacterial YihG (SF15), and cardiolipin-remodeling LCLAT1 (SF16) — sibling activities that share the acyltransferase fold but differ in acceptor lipid, so the specific de novo LPAAT (PA-forming) activity is a subfamily property rather than a family-wide one.

## Subfamily Analysis

- **Exemplar subfamily**: LPAT2 is **PTHR10983:SF24** ("1-ACYLGLYCEROL-3-PHOSPHATE O-ACYLTRANSFERASE 3, ISOFORM E-RELATED"); Brassica LPAT2 orthologs (Q6IWY1, Q9XFW4) co-cluster in SF24.
- **Broad parent**: 25 subfamilies across **12,019 taxa spanning bacteria (E. coli YihG, SF15), fungi (S. cerevisiae CST26; S. pombe SPBC428.14), plants and metazoa** — clearly **cross-kingdom**. Other subfamilies carry distinct remodeling activities: SF16 lysocardiolipin acyltransferase (LCLAT1), SF2 LPGAT1, SF8/SF9/SF73 the animal AGPAT delta/gamma/epsilon isoforms. Plant LPAT3/4/5 fall in SF55/SF16/SF74.

## IBA / PAINT Assessment

No local PAINT IBD data available for this family (`PTHR10983-paint.tsv` is not present). PANTHER PTN node identifiers and propagated terms are therefore not determined here.

## InterPro2GO / parent-family mapping verdict

**Do NOT map `GO:0003841 1-acylglycerol-3-phosphate O-acyltransferase activity` at the parent-family level.** PTHR10983 is a cross-kingdom, 25-subfamily family that mixes de novo LPAAT (PA synthesis) with a range of lysophospholipid-remodeling activities (cardiolipin, PG, PI acyltransferases). A whole-protein assignment of the PA-forming LPAAT activity would over-annotate the remodeling members. The module function is safe only at the **SF24 (and sibling AGPAT SF8/SF9/SF73) subfamily / PAINT-node level**; family-wide, only a generic acyl-CoA–dependent lysophospholipid acyltransferase activity plus ER-membrane localization is defensible.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, plant bioenergy module curation (no local PAINT available)
