# PANTHER Family Review: PTHR47944

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR47944 |
| **Family Name** | Plant Cytochrome P450 Monooxygenases |
| **InterPro Entry** | none (not integrated) |
| **Total Proteins** | 11,722 |
| **Taxonomic Breadth** | 1,928 taxa |
| **Subfamilies** | 17 |
| **Representative Structure** | 8e83 (2-hydroxyisoflavanone synthase from *Medicago truncatula*) |
| **Module role** | Provides **C3'H (p-coumaroyl-shikimate 3'-hydroxylase, CYP98A)**, the meta-hydroxylase of the monolignol pathway. Exemplar: `UniProtKB:O22203 (C98A3_ARATH, REF8)`, PANTHER `PTHR47944:SF10`; function `GO:0046409 p-coumarate 3-hydroxylase activity`. |

## Executive Summary

PTHR47944 is a family of **plant cytochrome P450 heme-thiolate monooxygenases** encompassing several CYP clans (the metadata groups CYP98A with other plant-specialized P450s such as isoflavone/flavonoid hydroxylases and terpene-oxidizing P450s). The unifying chemistry is NAD(P)H- and O2-dependent monooxygenation/hydroxylation of specialized-metabolite substrates.

The lignin-module member is **C3'H (CYP98A, EC 1.14.14.96)**, which 3-hydroxylates the shikimate (or quinate) ester of *p*-coumarate produced by HCT, yielding caffeoyl-shikimate. This meta-hydroxylation is indispensable for guaiacyl (G) and syringyl (S) lignin; loss of C3'H (e.g. Arabidopsis *ref8*) collapses the pathway toward *p*-hydroxyphenyl units. C3'H is one CYP98A clade among many divergent plant P450 activities in this family.

## Subfamily Analysis

The C3'H exemplar REF8/CYP98A3 (O22203) is in `PTHR47944:SF10` (CYTOCHROME P450 98A9). The reviewed entries span 15 of the family's 17 subfamilies, and the family name — **Plant Cytochrome P450 Monooxygenases** — describes only the shared monooxygenase chemistry, not C3'H specifically. Sibling clades in this family perform substantially different reactions (glucosinolate biosynthesis, terpene/terpenoid oxidation, coumarin/flavonoid hydroxylation, spermidine-conjugate meta-hydroxylation), so C3'H activity is subfamily-specific.

## IBA / PAINT Assessment

Local PAINT (`PTHR47944-paint.tsv`) is highly heterogeneous, confirming strong neofunctionalization across the family:

| Node (PTN) | GO term(s) | Aspect | Interpretation |
|------------|-----------|--------|----------------|
| PTN001210282 | `GO:0016709 oxidoreductase activity … NAD(P)H as one donor, one O incorporated`; `GO:0005783 endoplasmic reticulum`; `GO:0016020 membrane` | F/C | Generic ER-membrane P450 monooxygenase clade (seeds include CYP98-related loci). |
| PTN000670267 / PTN005381430 | `GO:0019761 glucosinolate biosynthetic process` | P | Glucosinolate-biosynthesis P450 clades. |
| PTN001960545 | `GO:0033511 luteolin biosynthetic process` | P | Flavone-hydroxylase clade. |
| PTN005379571 | `GO:0010333 terpene synthase activity`; `GO:0016114 terpenoid biosynthetic process` | F/P | Terpene/terpenoid clade. |
| PTN005381483 | `GO:0009805 coumarin`; `GO:0009813 flavonoid biosynthetic process` | P | Coumarin/flavonoid clade. |
| PTN005383291 | `GO:0052722 fatty acid in-chain hydroxylase activity`; `GO:0002933 lipid hydroxylation`; `GO:0010584 pollen exine formation` | F/P | In-chain fatty-acid hydroxylase clade. |
| PTN008722774 | `GO:0072547/0072548/0072549` (coumaroyl-/caffeoyl-spermidine meta-hydroxylase activities); `GO:0008216 spermidine metabolic process` | F/P | **CYP98A8/A9 clade** — spermidine-conjugate meta-hydroxylases (sister to C3'H). |
| PTN008612649 | `GO:0009682 induced systemic resistance` | P | Defense clade. |
| PTN009216876 / PTN009217258 | `GO:0016491 oxidoreductase activity` | F | Broad oxidoreductase nodes. |

Crucially, the specific C3'H term `GO:0046409 p-coumarate 3-hydroxylase activity` is **not** propagated by any local PAINT node. The nearest CYP98 activity captured is the divergent spermidine-conjugate meta-hydroxylase clade (PTN008722774), not C3'H itself.

## InterPro2GO / parent-family mapping verdict

Whole-protein mapping of the C3'H activity at the **parent level is strongly unsafe**. The family is a taxonomically broad, functionally divergent set of plant P450s (17 subfamilies performing glucosinolate, terpene, flavonoid, coumarin, spermidine, and fatty-acid oxidations); only a generic monooxygenase term (`GO:0016709` / `GO:0016491`) is defensible family-wide. The specific `GO:0046409 p-coumarate 3-hydroxylase activity` must be restricted to the **C3'H subfamily (`PTHR47944:SF10`)** and, ideally, curated from experimental evidence — the local PAINT does not even carry a C3'H node, so no family- or superfamily-level propagation of C3'H is warranted.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
