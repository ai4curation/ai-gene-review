# PANTHER Family Review: PTHR10509

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10509 |
| **Family Name** | Cation-dependent O-methyltransferase |
| **InterPro Entry** | IPR050362 |
| **Total Proteins** | 26,935 |
| **Taxonomic Breadth** | 22,254 taxa |
| **Subfamilies** | 33 |
| **Representative Structure** | 8gxn (CsFAOMT2 in complex with SAH) |
| **Module role** | Provides **CCoAOMT (caffeoyl-CoA O-methyltransferase)**, which methylates caffeoyl-CoA to feruloyl-CoA in the monolignol pathway. Exemplar: `UniProtKB:O49499 (CCoAOMT1, AtCCoAOMT1)`, PANTHER `PTHR10509:SF84`; function `GO:0042409 caffeoyl-CoA O-methyltransferase activity`. |

## Executive Summary

PTHR10509 is the **cation (Mg2+/metal)-dependent, SAM-dependent O-methyltransferase** family (class I plant OMT / CCoAOMT-like fold). Members transfer a methyl group from S-adenosyl-L-methionine to a hydroxyl acceptor, and the family spans a very wide taxonomic range (~22,254 taxa) with diverse small-molecule substrates.

The lignin-module enzyme is **caffeoyl-CoA O-methyltransferase (CCoAOMT, EC 2.1.1.104)**, which 3-O-methylates caffeoyl-CoA to feruloyl-CoA (and 5-hydroxyferuloyl-CoA to sinapoyl-CoA in some contexts). This CoA-ester methylation branch is a major route to guaiacyl (and, with F5H/COMT, syringyl) lignin monomers, working alongside CCR and CAD downstream. CCoAOMT is one specialized subfamily within a broad cation-dependent methyltransferase family whose other members methylate flavonoids, alkaloids, and diverse phenolics.

## Subfamily Analysis

The exemplar AtCCoAOMT1 (O49499) belongs to `PTHR10509:SF84` (CAFFEOYL-COA O-METHYLTRANSFERASE 1). The reviewed entries cover 15 of the family's 33 subfamilies, and the family name — **Cation-dependent O-methyltransferase** — reflects the shared SAM/metal-dependent methyl-transfer chemistry rather than CCoAOMT specifically. Substrate specificity diverges widely across subfamilies, so caffeoyl-CoA specificity is a subfamily-level trait.

## IBA / PAINT Assessment

Local PAINT (`PTHR10509-paint.tsv`) propagates only generic methyltransferase activities:

| Node (PTN) | GO term | Aspect | Interpretation |
|------------|---------|--------|----------------|
| PTN000053484 | `GO:0008757 S-adenosylmethionine-dependent methyltransferase activity` | F | Broad SAM-MT node (plant + other seeds). |
| PTN001629970 | `GO:0008171 O-methyltransferase activity` | F | Broad OMT node; seeds span animals, fish, fungi (*S. pombe*), plants. |

The specific `GO:0042409 caffeoyl-CoA O-methyltransferase activity` is **not** propagated by any local PAINT node. Only the generic SAM-dependent and O-methyltransferase activities are assigned family-wide — appropriate given the family's breadth.

## InterPro2GO / parent-family mapping verdict

Whole-protein mapping of `GO:0042409 caffeoyl-CoA O-methyltransferase activity` at the **parent level is unsafe**. PTHR10509 / IPR050362 is a broad, deeply conserved cation-dependent OMT family (33 subfamilies, ~22k taxa from bacteria to animals to plants); the only family-wide-defensible MF terms are the generic `GO:0008757 SAM-dependent methyltransferase activity` and `GO:0008171 O-methyltransferase activity` (which PAINT already assigns). The CCoAOMT-specific activity must be restricted to the **CCoAOMT subfamily (`PTHR10509:SF84`) / a dedicated PAINT node**; no such specific node exists in the local data, so the specific function should be curated at the subfamily/experimental level.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
