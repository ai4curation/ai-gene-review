# PANTHER Family Review: PTHR31444

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR31444 |
| **Family Name** | OS11G0490100 PROTEIN (DUF579) |
| **InterPro Entry** | IPR006514 |
| **Total Proteins** | 3,901 |
| **Taxonomic Breadth** | 1,212 taxa |
| **Subfamilies** | 25 |
| **Representative Structure** | none |
| **Module role** | Xylan sidechain decoration (secondary cell wall glucuronoxylan/GAX). 4-O-methylation of the glucuronic acid branches on xylan, producing 4-O-methyl-glucuronic acid (MeGlcA). Exemplar: `UniProtKB:Q9LQ32 (GXM3_ARATH)`; PANTHER SF not assigned (family-level). Associated function `GO:0030775 glucuronoxylan 4-O-methyltransferase activity`. |

## Executive Summary

PTHR31444 is a **DUF579 (domain of unknown function 579; IPR006514)** family with an uninformative PANTHER parent name inherited from a rice gene model (OS11G0490100). Despite the "unknown function" label, several plant members have been characterized as **S-adenosylmethionine–dependent methyltransferases acting on cell-wall polysaccharides**. The best-defined members are the **glucuronoxylan 4-O-methyltransferases GXM1/GXM2/GXM3**, which transfer a methyl group to the O-4 position of the alpha-glucuronic acid branches that GUX (PTHR11183) installs on the xylan backbone, converting GlcA to 4-O-methyl-GlcA (MeGlcA) — a dominant natural substitution of dicot glucuronoxylan.

The family also includes the DUF579 members **IRX15 and IRX15-L**, implicated in xylan backbone synthesis/deposition (irregular-xylem phenotype), and **AGM1/AGM2 arabinogalactan O-methyltransferases**, which methylate a different wall polymer (arabinogalactan-protein glycan) rather than xylan. Thus, even within this small plant-centric family, the enzymatic outputs diverge by substrate: GXM (xylan GlcA), AGM (arabinogalactan), and IRX15/IRX15-L (xylan-related but mechanistically less resolved). In the xylan module, the GXM subclade specifically performs the methyl-decoration step downstream of GUX branch addition.

## Subfamily Analysis

In the local entries table all members are Arabidopsis and **none carries a PANTHER subfamily assignment** (SF column blank), consistent with the anchor listing GXM at family level (SF n/a). The exemplar GXM3 (Q9LQ32) is therefore cited at the **PTHR31444 family level** in the local data. Characterized functional groups within the family include GXM1/2/3 (glucuronoxylan 4-O-MT), AGM1/2 (arabinogalactan O-MT), and IRX15 / IRX15-L (xylan deposition).

The parent is comparatively **small and plant-enriched** (25 subfamilies, 3,901 proteins across only 1,212 taxa — narrow relative to the other xylan-module parents), reflecting the largely plant/land-plant distribution of DUF579. However, "plant-enriched" is not "functionally homogeneous": the presence of the AGM arabinogalactan methyltransferases inside the same family shows the acceptor specificity is not uniform.

## IBA / PAINT Assessment

No local PAINT IBD data available for this family (`PTHR31444-paint.tsv` is absent). PTN node id(s) not determined here.

## InterPro2GO / parent-family mapping verdict

A **whole-protein GO mapping of glucuronoxylan 4-O-methyltransferase at the PARENT level is NOT safe**, despite the family being smaller and more plant-restricted than the others. DUF579/PTHR31444 mixes at least two substrate specificities — xylan-GlcA methylation (GXM1/2/3) and arabinogalactan methylation (AGM1/2) — plus the mechanistically distinct IRX15/IRX15-L. Propagating `GO:0030775 glucuronoxylan 4-O-methyltransferase activity` to the whole family would mis-annotate the AGM arabinogalactan methyltransferases and the IRX15 members. The most defensible parent-level term is a **general S-adenosyl-L-methionine–dependent methyltransferase activity acting on a carbohydrate/polysaccharide acceptor**; the specific glucuronoxylan 4-O-methyltransferase activity should be restricted to the **GXM subclade** via curated-member or PAINT-node annotation. **Verdict: GXM-specific function stays at subclade level, not parent level.**

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT (none for this family), UniProt, plant bioenergy xylan-module curation
