# PANTHER Family Review: PTHR12181

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR12181 |
| **Family Name** | LIPIN |
| **InterPro Entry** | IPR026058 (integrated) |
| **Total Proteins** | 10,024 |
| **Taxonomic Breadth** | 8,951 taxa; 3,400 proteomes (eukaryote-wide: fungi, plants, metazoa) |
| **Subfamilies** | 14 |
| **Module role** | Kennedy pathway **step 3** — Mg²⁺-dependent phosphatidate phosphatase (PAP) converting phosphatidic acid (PA) to diacylglycerol (DAG). Exemplar: `UniProtKB:Q9SF47 (PAH1_ARATH)` at **PTHR12181:SF59**; module function `GO:0008195 phosphatidate phosphatase activity` |

## Executive Summary

PTHR12181 is the **lipin family** of Mg²⁺-dependent (HAD-like DXDXT motif) phosphatidate phosphatases (PAP1-type). Lipins dephosphorylate phosphatidic acid to diacylglycerol, the committed penultimate step of the Kennedy pathway that supplies DAG both for phospholipid synthesis and for the final DGAT/PDAT acylation to triacylglycerol. Beyond catalysis, lipins have a nuclear/transcriptional-coactivator role in some lineages, but the conserved enzymatic core is the PAP activity captured by `GO:0008195`.

In seed TAG assembly the relevant member is plant **PAH1** (Arabidopsis PAH1, Q9SF47), one of the two Arabidopsis lipins (PAH1/PAH2) that provide the DAG pool feeding oil biosynthesis. The family is unusual among the seed-TAG modules in being **taxonomically homogeneous for its activity**: essentially all members are eukaryotic lipins/PAH enzymes with the same PAP function — yeast PAH1 and Ned1 (S. pombe), plant PAH1/PAH2, and animal LPIN1/LPIN2/LPIN3. There is no unrelated ancestral activity masquerading under the family name, in contrast to the broad superfamilies that house DGAT1, GPAT9, or PDAT.

## Subfamily Analysis

- **Exemplar subfamily**: plant PAH1 is **PTHR12181:SF59** ("PHOSPHATIDATE PHOSPHATASE PAH1"). Arabidopsis PAH2 and yeast PAH1/Ned1 cluster in the generic SF12 ("PHOSPHATIDATE PHOSPHATASE"); animal lipins occupy SF10 (LPIN1), SF11 (LPIN2) and SF62 (LPIN3).
- **Broad parent**: 14 subfamilies across **8,951 taxa**, all **eukaryotic lipins**. The family does not span kingdoms into bacteria/archaea and does not mix in unrelated enzymes; the subfamily structure reflects paralog/ortholog groups (fungal PAH, plant PAH, animal LPIN1/2/3) all sharing the PAP activity.

## IBA / PAINT Assessment

No local PAINT IBD data available for this family (`PTHR12181-paint.tsv` is not present). PANTHER PTN node identifiers and propagated terms are therefore not determined here.

## InterPro2GO / parent-family mapping verdict

**A whole-protein `GO:0008195 phosphatidate phosphatase activity` mapping is largely defensible at (or near) the family level here.** Unlike the other seed-TAG families, PTHR12181 is homogeneous — its members are eukaryotic lipin/PAH phosphatidate phosphatases sharing the catalytic PAP core, so parent-level annotation of PAP activity does not obviously over-annotate a paralogous non-PAP clade. Caveats: (i) family-level PAP is a molecular-function statement only — the additional nuclear/transcriptional-regulatory roles of animal lipins are lineage-specific and must stay at subfamily level; (ii) the plant-oil-specific *process* context (seed TAG) is not a family-wide property and should remain at the PAH1/PAH2 subfamily/PAINT level. The specific `GO:0008195` MF is best emitted at least at the InterPro entry IPR026058 (lipin) level and can reasonably propagate across the PANTHER family.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, plant bioenergy module curation (no local PAINT available)
