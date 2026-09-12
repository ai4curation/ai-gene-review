# PANTHER Family Review: PTHR11709

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR11709 |
| **Family Name** | MULTI-COPPER OXIDASE |
| **InterPro Entry** | IPR045087 |
| **Total Proteins** | 83,061 |
| **Taxonomic Breadth** | 26,412 taxa |
| **Subfamilies** | 176 |
| **Representative Structure** | 6kli (*Zea mays* laccase 3 in complex with sinapyl alcohol) |
| **Module role** | Provides **cell-wall laccase**, which oxidatively polymerizes monolignols into lignin. Exemplar: `UniProtKB:Q9FJD5 (LAC17_ARATH, AtLAC17)`, PANTHER `PTHR11709:SF417`; function `GO:0016682 oxidoreductase activity, acting on diphenols and related substances as donors, oxygen as acceptor` (laccase, EC 1.10.3.2). |

## Executive Summary

PTHR11709 is the **multicopper oxidase (MCO) superfamily** — a very large, ancient group (83,061 proteins, 176 subfamilies, ~26,412 taxa) of enzymes that couple one-electron oxidation of a substrate to the four-electron reduction of O2 to water at a trinuclear copper cluster. The superfamily is enzymatically heterogeneous: it contains laccases/diphenol oxidases, **ferroxidases** (fungal Fet3, animal ceruloplasmin and hephaestin), and ascorbate oxidases, among others.

The lignin-module members are the **plant cell-wall laccases** (EC 1.10.3.2), which oxidize monolignols (coniferyl, sinapyl, *p*-coumaryl alcohol) to phenoxy radicals that couple non-enzymatically into the lignin polymer. Together with class III peroxidases (see PTHR31388), laccases perform the final, extracellular polymerization step of lignification. Plant laccase is one subfamily-level activity within the broad MCO superfamily whose name and ancestral function are simply "multicopper oxidase," not laccase.

## Subfamily Analysis

The exemplar AtLAC17 (Q9FJD5) belongs to `PTHR11709:SF417` (LACCASE-17). The reviewed entries span 49 distinct subfamilies of the 176 in the family; the family name — **MULTI-COPPER OXIDASE** — reflects the shared copper-oxidase chemistry, not laccase specifically. The reviewed members explicitly include non-laccase MCOs such as human ceruloplasmin (P00450) and fungal/animal ferroxidases, underscoring that laccase activity is a subfamily property, not a family-wide one.

## IBA / PAINT Assessment

Local PAINT (`PTHR11709-paint.tsv`) is strongly heterogeneous and includes an explicit negation:

| Node (PTN) | GO term(s) | Aspect | Interpretation |
|------------|-----------|--------|----------------|
| PTN000194698 | `GO:0016491 oxidoreductase activity` | F | Broad root-level MCO node; seeds include ceruloplasmin (P00450), plant laccases, fungal and insect MCOs. |
| PTN000194708 | `GO:0005886 plasma membrane` | C | Membrane-associated clade. |
| PTN000194745 | `GO:0000329 fungal-type vacuole membrane`; `GO:0033573 high-affinity iron permease complex` (**IRD, negated=true**) | C | Fungal clade; the iron-permease-complex term is explicitly retracted (IRD) from this subclade. |
| PTN000917581 | `GO:0033573 high-affinity iron permease complex`; `GO:0004322 ferroxidase activity`; `GO:0010106 cellular response to iron ion starvation`; `GO:0033215 reductive iron assimilation` | C/F/P | **Fungal Fet3-type ferroxidase clade.** |
| PTN002619510 | `GO:0004322 ferroxidase activity` | F | Animal ferroxidase clade (ceruloplasmin/hephaestin-type; Q9BQS7, MGI seeds). |
| PTN004294009 | `GO:0005886 plasma membrane` | C | Plant laccase clade (Arabidopsis AT4G25240, AT4G12420). |

Notably, the laccase MF term `GO:0016682` is **not** propagated anywhere in the local PAINT; only the generic `GO:0016491 oxidoreductase activity` sits at the root, while the ferroxidase clades carry `GO:0004322`. The negated (IRD) iron-permease term shows PAINT actively removing a mis-fitting annotation from a subclade.

## InterPro2GO / parent-family mapping verdict

Whole-protein mapping of `GO:0016682 … (laccase)` at the **parent level is strongly unsafe**. PTHR11709 / IPR045087 is the multicopper-oxidase superfamily, and large clades are ferroxidases (ceruloplasmin, hephaestin, Fet3) and other MCOs — mapping laccase family-wide would falsely annotate these iron-oxidizing enzymes as laccases. Only the generic `GO:0016491 oxidoreductase activity` is defensible family-wide (as PAINT assigns at the root). Plant cell-wall laccase activity must be restricted to the **laccase subfamily (`PTHR11709:SF417`) / plant laccase PAINT node**; the local PAINT correctly keeps only generic oxidoreductase at the root and assigns ferroxidase (not laccase) to the iron-metabolism clades.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
