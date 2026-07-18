# PANTHER Family Review: PTHR10362

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10362 |
| **Family Name** | HISTIDINE AMMONIA-LYASE |
| **InterPro Entry** | IPR001106 |
| **Total Proteins** | 31,750 |
| **Taxonomic Breadth** | 23,042 taxa |
| **Subfamilies** | 27 |
| **Representative Structure** | 1w27 (phenylalanine ammonia-lyase from *Petroselinum crispum*) |
| **Module role** | Provides **PAL (phenylalanine ammonia-lyase)**, the entry step of the phenylpropanoid pathway that feeds monolignol/lignin biosynthesis. Exemplar: `UniProtKB:P35510 (PAL1_ARATH)`, PANTHER `PTHR10362` (no SF assigned to the exemplar in the reviewed entries); function `GO:0045548 phenylalanine ammonia-lyase activity`. |

## Executive Summary

PTHR10362 is the **aromatic amino-acid ammonia-lyase / MIO-dependent lyase** superfamily. Its members share a 4-methylideneimidazole-5-one (MIO) cofactor, formed autocatalytically from an internal Ala-Ser-Gly tripeptide, and catalyze the non-oxidative elimination of ammonia from an aromatic amino acid. The family name reflects the ancestral/canonical activity, **histidine ammonia-lyase (histidase, EC 4.3.1.3)**, which converts L-histidine to urocanate in the histidine catabolic pathway of bacteria and animals.

In plants a specialized clade of this superfamily performs **phenylalanine ammonia-lyase (PAL, EC 4.3.1.24/4.3.1.25)**, deaminating L-phenylalanine to *trans*-cinnamate. This is the committed, rate-influencing first step of the phenylpropanoid pathway, upstream of C4H and 4CL, and the ultimate source of the hydroxycinnamate/monolignol precursors of lignin. PAL therefore represents a plant-lineage neofunctionalization of an ancient ammonia-lyase fold: same MIO chemistry and reaction type (aromatic C–N elimination), different amino-acid substrate.

## Subfamily Analysis

The exemplar PAL1 (P35510) sits in the plant PAL clade of PTHR10362; the reviewed-entries table does not assign it a distinct `:SF` id, but the PAINT data resolve a dedicated plant-PAL node (below). The parent family is **broad and enzymatically heterogeneous** (27 subfamilies, 23,042 taxa spanning bacteria, fungi, animals and plants) and is named for **histidine ammonia-lyase**, not PAL. It also contains tyrosine/phenylalanine ammonia-lyase and aminomutase relatives. PAL is thus one specialized activity within an ancestral histidase superfamily — the classic case where the family name reflects a different ancestral function from the lignin-module activity.

## IBA / PAINT Assessment

Local PAINT (`PTHR10362-paint.tsv`) contains IBD nodes that cleanly separate the ancestral and plant-specialized activities:

| Node (PTN) | GO term | Aspect | Interpretation |
|------------|---------|--------|----------------|
| PTN000796617 | `GO:0016841 ammonia-lyase activity` | F | Broad root-level activity for the whole superfamily. |
| PTN000796665 | `GO:0004397 histidine ammonia-lyase activity`; `GO:0006548 L-histidine catabolic process` | F/P | Bacterial (taxon:2) histidase clade. |
| PTN000820875 | `GO:0004397 histidine ammonia-lyase activity`; `GO:0006548 L-histidine catabolic process` | F/P | Animal (taxon:6072, Eumetazoa) histidase clade. |
| PTN001621754 | `GO:0045548 phenylalanine ammonia-lyase activity` | F | **Plant PAL clade** (seeds = Arabidopsis PAL AGI loci; taxon:71275). This is the lignin-module node. |

The propagation is biologically correct: PAL activity (`GO:0045548`) is confined to the plant PAL node PTN001621754, histidase activity to the bacterial and animal nodes, and only the generic `GO:0016841 ammonia-lyase activity` sits at the superfamily root. No spurious cross-propagation of PAL onto histidase clades is seen.

## InterPro2GO / parent-family mapping verdict

A whole-protein mapping of `GO:0045548 phenylalanine ammonia-lyase activity` at the **parent (PTHR10362 / IPR001106) level is NOT safe**: the parent is the histidine-ammonia-lyase superfamily, and the great majority of its members are histidases and other non-PAL ammonia-lyases across bacteria and animals. Only the generic `GO:0016841 ammonia-lyase activity` is defensible family-wide. The specific PAL activity must be restricted to the **plant PAL PAINT node (PTN001621754)** / plant PAL subfamily, which is exactly how the current PAINT annotation is structured.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
