# PANTHER Family Review: PTHR10408

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10408 |
| **Family Name** | STEROL O-ACYLTRANSFERASE (MBOAT superfamily; ACAT/SOAT + DGAT1) |
| **InterPro Entry** | IPR014371 (integrated) |
| **Total Proteins** | 9,242 |
| **Taxonomic Breadth** | 8,841 taxa; 3,320 proteomes (fungi, amoebozoa, plants, metazoa) |
| **Subfamilies** | 12 |
| **Module role** | Kennedy pathway **step 4 (acyl-CoA–dependent)** — acyl-CoA:diacylglycerol acyltransferase forming triacylglycerol. Exemplar: `UniProtKB:Q9SLD2 (DGAT1_ARATH, TAG1)` at **PTHR10408:SF7**; module function `GO:0004144 diacylglycerol O-acyltransferase activity` |

## Executive Summary

PTHR10408 is a **membrane-bound O-acyltransferase (MBOAT) superfamily** whose parent name — **STEROL O-ACYLTRANSFERASE** — reflects the ACAT/SOAT cholesterol-esterifying activity, not DGAT1. The family groups two mechanistically related but biologically distinct activities: (i) **sterol O-acyltransferases** (animal SOAT1/SOAT2 esterifying cholesterol; fungal ARE1/ARE2 esterifying ergosterol) and (ii) **acyl-CoA:diacylglycerol acyltransferase 1 (DGAT1)**, the acyl-CoA–dependent enzyme that completes triacylglycerol assembly.

In seed oil biosynthesis the relevant member is **DGAT1** (Arabidopsis DGAT1/TAG1, Q9SLD2), which catalyzes the final, acyl-CoA–dependent acylation of sn-1,2-diacylglycerol to triacylglycerol (`GO:0004144`) and is the major determinant of seed oil content in many crops (human O75907 and soybean I1MSF2 are the mammalian and oilseed orthologs). Crucially, **DGAT1 is only one subfamily (SF7) within this MBOAT family**; the family also contains the cholesterol/ergosterol acyltransferases whose physiological role is sterol esterification and storage, entirely separate from TAG. This makes the parent name potentially misleading for the DGAT1 module: parent-level "DGAT" mapping would wrongly annotate the ACAT/SOAT sterol acyltransferases, and parent-level "sterol O-acyltransferase" mapping would wrongly annotate DGAT1.

## Subfamily Analysis

- **Exemplar subfamily**: DGAT1 is **PTHR10408:SF7** ("DIACYLGLYCEROL O-ACYLTRANSFERASE 1") — the pan-eukaryotic DGAT1 clade (Arabidopsis Q9SLD2, human O75907, rat/mouse/bovine DGAT1, Dictyostelium, rice DGAT1-2). Soybean DGAT1A/1B split into SF22; rice DGAT1-1 into SF12.
- **Broad parent**: 12 subfamilies across **8,841 taxa** (fungi → metazoa → plants → amoebozoa). Distinct, non-DGAT activities occupy their own subfamilies: **SF6 SOAT1** and **SF10 SOAT2** (cholesterol esterification, human/rodent/primate), **SF23 fungal ARE1/ARE2** (ergosterol esterification), **SF9 SOAT2-related**. The family spans a single eukaryotic superfamily but is **functionally split between sterol-ester and TAG synthesis**.

## IBA / PAINT Assessment

Local PAINT (IBD) data (`PTHR10408-paint.tsv`) cleanly separates the two activities by node:

| Node | GO ID | Aspect | Negated | Notes |
|------|-------|--------|---------|-------|
| PTN000045225 | GO:0005789 endoplasmic reticulum membrane | C | false | ER-membrane localization at the family root node (broad seed set incl. SOAT1 P35610, SOAT2 O75908, yeast ARE). |
| PTN000045225 | GO:0016747 acyltransferase activity, transferring groups other than amino-acyl groups | F | false | Only a **generic** acyltransferase MF is propagated at the root — not DGAT and not sterol acyltransferase. |
| PTN000045226 | GO:0004144 diacylglycerol O-acyltransferase activity | F | false | **DGAT activity restricted to the DGAT1 sub-node** (taxon:2759; seeds incl. Arabidopsis AT2G19450, human O75907, soybean I1MSF2). |
| PTN000045226 | GO:0019432 triglyceride biosynthetic process | P | false | TAG-synthesis process on the same DGAT1 node. |
| PTN000045308 | GO:0000062 fatty-acyl-CoA binding | F | false | SOAT node (human SOAT1 P35610, SOAT2 O75908). |
| PTN000045308 | GO:0015485 cholesterol binding | F | false | SOAT node. |
| PTN000045308 | GO:0034736 cholesterol O-acyltransferase activity | F | false | **Cholesterol acyltransferase restricted to the SOAT sub-node**, separate from the DGAT1 node. |
| PTN000045308 | GO:0033344 cholesterol efflux | P | false | SOAT node process. |
| PTN000823393 | GO:0034737 ergosterol O-acyltransferase activity | F | false | **Fungal (taxon:4751) ARE node** (yeast SGD seeds). |
| PTN000823393 | GO:0008204 ergosterol metabolic process | P | false | Fungal ARE process. |
| PTN000823449 | GO:0009941 chloroplast envelope | C | false | Plant (taxon:3193) DGAT1 localization (Arabidopsis AT2G19450). |
| PTN000823452 | GO:0008203 cholesterol metabolic process | P | false | Sterol-metabolism process at a mammalian node. |

This is a textbook case: the ancestral/generic acyltransferase term sits at the root, while **DGAT activity (GO:0004144) and sterol/cholesterol acyltransferase activity (GO:0034736, GO:0034737) are held at separate, mutually exclusive sub-nodes** matching the SF7 (DGAT1) vs SF6/SF10/SF23 (SOAT/ARE) split.

## InterPro2GO / parent-family mapping verdict

**`GO:0004144 diacylglycerol O-acyltransferase activity` must NOT be mapped at the parent-family (or IPR014371 whole-family) level.** The parent is the MBOAT sterol-O-acyltransferase superfamily; a parent-level DGAT term would over-annotate the ACAT/SOAT cholesterol acyltransferases and the fungal ergosterol acyltransferases, and vice versa a parent-level sterol-acyltransferase term would over-annotate DGAT1. The PAINT graph already enforces the correct resolution — DGAT at PTN000045226 (SF7 clade) and sterol/ergosterol acyltransferase at PTN000045308/PTN000823393 — so **the DGAT1 module function is safe only at the SF7 subfamily / DGAT1 PAINT-node level**. Family-wide, only the generic `GO:0016747` acyltransferase MF plus ER-membrane localization is defensible.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT (PTHR10408-paint.tsv), UniProt, plant bioenergy module curation
