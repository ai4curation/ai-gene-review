# PANTHER Family Review: PTHR12317

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR12317 |
| **Family Name** | Diacylglycerol O-acyltransferase / Retinol O-fatty-acyltransferase (DGAT2/MGAT/ARAT; DGAT/ARAT) |
| **InterPro Entry** | none (no integrated InterPro entry) |
| **Total Proteins** | 10,739 |
| **Taxonomic Breadth** | 8,790 taxa; 3,299 proteomes (fungi, amoebozoa, plants, metazoa) |
| **Subfamilies** | 24 |
| **Module role** | Kennedy pathway **step 4 (acyl-CoA–dependent, DGAT2 route)** — acyl-CoA:diacylglycerol acyltransferase forming triacylglycerol. Exemplar: `UniProtKB:Q9ASU1 (DGAT2_ARATH)` at **PTHR12317:SF63**; module function `GO:0004144 diacylglycerol O-acyltransferase activity` |

## Executive Summary

PTHR12317 is the **DGAT2/MGAT superfamily**, a set of membrane-bound acyltransferases structurally unrelated to the MBOAT DGAT1 family (PTHR10408) but catalyzing the same net reaction. The family groups several acyl-CoA–dependent acyltransferases that differ in acceptor: **DGAT2** (diacylglycerol → triacylglycerol), **MOGAT1/2/3** (monoacylglycerol → diacylglycerol; intestinal fat re-absorption), and the **acyl-CoA wax alcohol acyltransferases AWAT1/2** (fatty alcohol → wax esters), plus retinol O-fatty-acyltransferase activity in some members.

In seed oil biosynthesis the relevant member is **DGAT2** (Arabidopsis DGAT2, Q9ASU1), a second, biochemically independent route to triacylglycerol that in many oilseeds channels unusual/modified fatty acids into TAG and works alongside DGAT1. DGAT2's TAG-forming activity is `GO:0004144`, the same MF as DGAT1, reached by convergent chemistry. Because the family also contains the diacylglycerol-*forming* MGATs and the wax-ester AWATs, the specific DGAT2 (TAG-forming) activity is a subfamily property; the parent groups multiple distinct acyl-acceptor specificities under one fold.

## Subfamily Analysis

- **Exemplar subfamily**: plant DGAT2 is **PTHR12317:SF63** ("DIACYLGLYCEROL O-ACYLTRANSFERASE 2"), shared with castor DGAT2 (A1A442) and soybean DGAT2D (K7K424). Animal DGAT2 clusters in SF14; fungal DGA1 (S. cerevisiae, S. pombe, Umbelopsis) sits in the generic SF0 ("ACYLTRANSFERASE").
- **Broad parent**: 24 subfamilies across **8,790 taxa** (fungi → amoebozoa → plants → metazoa). Distinct activities occupy their own subfamilies: **SF26 MOGAT1, SF74 MOGAT2, SF36 MOGAT3** (monoacylglycerol acyltransferases), **SF16 AWAT1, SF12 AWAT2** (wax alcohol acyltransferases), **SF19 DGAT2L6**. The family is eukaryote-wide and **functionally split across TAG, DAG (MGAT) and wax-ester synthesis**.

## IBA / PAINT Assessment

No local PAINT IBD data available for this family (`PTHR12317-paint.tsv` is not present). PANTHER PTN node identifiers and propagated terms are therefore not determined here.

## InterPro2GO / parent-family mapping verdict

**Do NOT map `GO:0004144 diacylglycerol O-acyltransferase activity` at the parent-family level.** PTHR12317 mixes DGAT2 (TAG synthesis) with MOGAT1/2/3 (DAG synthesis) and AWAT1/2 (wax-ester synthesis) across 24 subfamilies; a whole-protein DGAT term would over-annotate the MGAT and wax acyltransferase members (which have different acceptors and physiological roles — e.g. intestinal dietary-fat absorption, sebaceous wax synthesis). The DGAT2 module function is safe only at the **SF63 / SF14 DGAT2-clade subfamily (or PAINT-node) level**; family-wide, only a generic acyl-CoA–dependent diacylglycerol/monoacylglycerol O-acyltransferase activity plus ER-membrane localization is defensible. Note also that DGAT1 (PTHR10408) and DGAT2 (this family) share the `GO:0004144` MF but are non-homologous, so this term legitimately arises in two unrelated PANTHER families and neither is the sole "owner" for InterPro2GO purposes.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, plant bioenergy module curation (no local PAINT available)
