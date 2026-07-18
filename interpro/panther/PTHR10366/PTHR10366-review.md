# PANTHER Family Review: PTHR10366

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10366 |
| **Family Name** | NAD(P)-dependent epimerase/dehydratase-related protein |
| **InterPro Entry** | IPR050425 |
| **Total Proteins** | 35,886 |
| **Taxonomic Breadth** | 11,757 taxa |
| **Subfamilies** | 153 |
| **Representative Structure** | 4pvc (yeast methylglyoxal/isovaleraldehyde reductase Gre2) |
| **Module role** | Provides **CCR (cinnamoyl-CoA reductase)**, the first committed enzyme of the monolignol-specific branch. Exemplar: `UniProtKB:Q9S9N9 (CCR1_ARATH, IRX4)`, PANTHER `PTHR10366:SF404`; function `GO:0016621 cinnamoyl-CoA reductase activity`. |

## Executive Summary

PTHR10366 is a large **NAD(P)-dependent Rossmann-fold oxidoreductase** family related to the extended SDR / epimerase-dehydratase-reductase superfamily. Members reduce/interconvert a wide variety of carbonyl and sugar-nucleotide substrates using NAD(P)H, and the family is functionally sprawling (153 subfamilies; flavonoid, lignin, and other specialized-metabolism reductases as well as general aldo-keto reductases).

The lignin-module enzyme is **cinnamoyl-CoA reductase (CCR, EC 1.2.1.44)**, which reduces hydroxycinnamoyl-CoA thioesters (feruloyl-CoA, *p*-coumaroyl-CoA, sinapoyl-CoA) to the corresponding cinnamaldehydes. CCR is the entry point of the monolignol-specific pathway (its product aldehydes are then reduced by CAD to monolignols), and it exerts strong flux control over lignin deposition. CCR is one specialized subfamily within a very broad reductase family that also contains dihydroflavonol 4-reductase (DFR) and anthocyanidin reductase (ANR) — flavonoid enzymes that share the fold but act on different substrates.

## Subfamily Analysis

The exemplar CCR1/IRX4 (Q9S9N9) belongs to `PTHR10366:SF404` (CINNAMOYL-COA REDUCTASE 1). The reviewed entries cover 19 of the family's 153 subfamilies, and the family name — **NAD(P)-dependent epimerase/dehydratase-related protein** — reflects the ancestral NAD(P)-dependent oxidoreductase chemistry, not CCR. Close siblings in the same family (DFR, ANR) demonstrate that substrate specificity, and hence pathway role, is a subfamily-level property.

## IBA / PAINT Assessment

Local PAINT (`PTHR10366-paint.tsv`):

| Node (PTN) | GO term | Aspect | Interpretation |
|------------|---------|--------|----------------|
| PTN000041225 | `GO:0016616 oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor` | F | Broad root-level oxidoreductase node (large mixed-taxon seed set: plants, animals, fungi, bacteria). |
| PTN001622455 | `GO:0009809 lignin biosynthetic process` | P | Plant lignin-biosynthesis clade. |
| PTN001622618 | `GO:0033729 anthocyanidin reductase activity` | F | ANR (flavonoid) sibling clade. |
| PTN001622637 | `GO:0045552 dihydroflavanol 4-reductase activity`; `GO:0009718 anthocyanin-containing compound biosynthetic process` | F/P | DFR (flavonoid) sibling clade. |

The specific CCR term `GO:0016621 cinnamoyl-CoA reductase activity` is **not** propagated as a molecular function in the local PAINT; the plant lignin node PTN001622455 carries only the process term `GO:0009809 lignin biosynthetic process`. Meanwhile the sibling nodes carry distinctly different flavonoid MFs (DFR, ANR), directly illustrating why family-wide MF propagation would be wrong.

## InterPro2GO / parent-family mapping verdict

Whole-protein mapping of `GO:0016621 cinnamoyl-CoA reductase activity` at the **parent level is clearly unsafe**. PTHR10366 / IPR050425 is a 153-subfamily NAD(P)-dependent reductase family in which even neighboring plant subfamilies perform flavonoid reductions (DFR, ANR) rather than CCR; only the generic `GO:0016616 oxidoreductase activity (CH-OH donors, NAD(P) acceptor)` is defensible family-wide. The CCR-specific activity must be restricted to the **CCR subfamily (`PTHR10366:SF404`)**, and even the plant PAINT node keeps only the lignin *process* term rather than the CCR MF — a correctly conservative structure.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
