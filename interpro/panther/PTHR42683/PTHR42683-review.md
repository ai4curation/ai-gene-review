# PANTHER Family Review: PTHR42683

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR42683 |
| **Family Name** | ALDEHYDE REDUCTASE |
| **InterPro Entry** | IPR047109 |
| **Total Proteins** | 31,617 |
| **Taxonomic Breadth** | 16,871 taxa |
| **Subfamilies** | 41 |
| **Representative Structure** | 7bu3 (alcohol dehydrogenase YjgB with NADP from *Escherichia coli*) |
| **Module role** | Provides **CAD (cinnamyl alcohol dehydrogenase)**, the final reductive step producing monolignols. Exemplars: `UniProtKB:O49482 (CADH5_ARATH, AtCAD5)` and `UniProtKB:O24562 (CADH_MAIZE, BM1)`, PANTHER `PTHR42683` (no SF assigned to the exemplar in the reviewed entries); function `GO:0045551 cinnamyl-alcohol dehydrogenase activity`. |

## Executive Summary

PTHR42683 is a broad **NAD(P)-dependent medium-chain dehydrogenase/reductase (MDR) / aldehyde-reductase** family (zinc-containing alcohol-dehydrogenase-like fold). Members reduce aldehydes to alcohols (or oxidize the reverse) across bacteria, fungi, plants, and animals — the family name reflects this generic aldehyde-reductase/ADH activity.

The lignin-module enzyme is **cinnamyl alcohol dehydrogenase (CAD, EC 1.1.1.195)**, which catalyzes the last committed step of monolignol biosynthesis: NADPH-dependent reduction of the hydroxycinnamaldehydes (*p*-coumaraldehyde, coniferaldehyde, sinapaldehyde) produced by CCR to the corresponding monolignols (*p*-coumaryl, coniferyl, sinapyl alcohol). These monolignols are then exported and oxidatively polymerized (by laccases/peroxidases) into lignin. CAD is a plant-specific subfamily within a large ADH/MDR family that also contains bacterial and fungal alcohol dehydrogenases.

## Subfamily Analysis

The exemplars AtCAD5 (O49482) and maize BM1 (O24562) fall in the plant CAD clade of PTHR42683; the reviewed-entries table does not assign the exemplar a distinct `:SF` id (2 broad subfamily groupings resolve in the reviewed set). The family name — **ALDEHYDE REDUCTASE** — reflects the ancestral ADH/aldehyde-reductase activity, not CAD. The plant CAD clade is one specialized offshoot; other clades are fungal NADP-dependent ADHs and broad bacterial/eukaryotic MDR oxidoreductases.

## IBA / PAINT Assessment

Local PAINT (`PTHR42683-paint.tsv`) cleanly separates the plant CAD clade from ancestral ADH clades:

| Node (PTN) | GO term(s) | Aspect | Interpretation |
|------------|-----------|--------|----------------|
| PTN000915374 | `GO:0045551 cinnamyl-alcohol dehydrogenase activity`; `GO:0009809 lignin biosynthetic process` | F/P | **Land-plant (taxon:3193) CAD clade** — seeds include maize BM1 (O24562) and Arabidopsis CAD loci. This is the lignin-module node. |
| PTN001290610 | `GO:0008106 alcohol dehydrogenase (NADP+) activity` | F | Fungal (Opisthokonta, taxon:33154) ADH clade (yeast SGD seeds). |
| PTN001708008 | `GO:0016616 oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor` | F | Broad node including bacterial ADHs (*E. coli* P27250, etc.). |

This is a model example of correct PAINT structuring: the specific CAD activity (`GO:0045551`) and lignin biosynthesis are propagated **only** to the plant CAD node PTN000915374, while fungal ADH and generic CH-OH oxidoreductase terms sit on their own clades.

## InterPro2GO / parent-family mapping verdict

Whole-protein mapping of `GO:0045551 cinnamyl-alcohol dehydrogenase activity` at the **parent level is unsafe**. PTHR42683 / IPR047109 is a broad ADH/aldehyde-reductase family (41 subfamilies, ~16,871 taxa, bacteria to animals; representative structure is *E. coli* YjgB); only the generic `GO:0016616 oxidoreductase activity (CH-OH donors, NAD(P) acceptor)` is defensible family-wide. The CAD-specific activity must be restricted to the **plant CAD PAINT node (PTN000915374)** / CAD subfamily — which is precisely how the current PAINT annotation confines it.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
