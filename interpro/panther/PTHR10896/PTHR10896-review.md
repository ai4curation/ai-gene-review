# PANTHER Family Review: PTHR10896

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10896 |
| **Family Name** | GALACTOSYLGALACTOSYLXYLOSYLPROTEIN 3-BETA-GLUCURONOSYLTRANSFERASE / BETA-1,3-GLUCURONYLTRANSFERASE |
| **InterPro Entry** | IPR005027 |
| **Total Proteins** | 8,268 |
| **Taxonomic Breadth** | 5,376 taxa |
| **Subfamilies** | 22 |
| **Representative Structure** | 1v84 (human GlcAT-P with N-acetyllactosamine, UDP, Mn2+) |
| **Module role** | Xylan backbone elongation (secondary cell wall glucuronoxylan/GAX). GT43 xylan-synthase components IRX9 and IRX14. Exemplars: `UniProtKB:Q9ZQC6 (IRX9_ARATH)` at PTHR10896:SF59 and `UniProtKB:Q8L707 (IRX14_ARATH)` at PTHR10896:SF63. Associated function `GO:0047517 1,4-beta-D-xylan synthase activity`. |

## Executive Summary

PTHR10896 is the **glycosyltransferase family 43 (GT43)** clade. The PANTHER parent name reflects the animal-type activity **beta-1,3-glucuronyltransferase (GlcAT-I / GlcAT-P / GlcAT-S; B3GAT1/2/3)** — the enzyme that adds the terminal glucuronic acid completing the GAG-protein linkage tetrasaccharide (GlcA-Gal-Gal-Xyl-Ser) in proteoglycan biosynthesis. Within this same GT43 fold, plants evolved the **secondary-wall xylan synthase components IRX9 and IRX14**, which are required in the Golgi-localized xylan-synthase complex that elongates the beta-1,4-linked D-xylose backbone of glucuronoxylan (GX) and glucuronoarabinoxylan (GAX). IRX9 and IRX14 (and their partial-redundant paralogs IRX9L/IRX14L) are non-redundantly required for xylan backbone synthesis; loss produces the irregular-xylem (collapsed vessel) phenotype.

In glucuronoxylan/GAX biosynthesis, the IRX9/IRX14 GT43 pair provides the backbone-elongation activity onto which the downstream module enzymes act: GUX (GT8, PTHR11183) adds alpha-1,2-GlcA branches, GXM (DUF579, PTHR31444) 4-O-methylates those GlcA residues, and ESK1/TBL29 (TBL/DUF231, PTHR32285) 2-O/3-O-acetylates the backbone. Thus the plant GT43 members are the entry point of the xylan module, and are mechanistically distinct in substrate (xylan backbone) from the animal GT43 members (GAG linker glucuronylation), even though both are inverting UDP-sugar glucuronyl/xylosyl-transferases sharing the GT-A fold.

## Subfamily Analysis

The exemplars sit in **distinct plant subfamilies**: IRX9 in **PTHR10896:SF59** ("BETA-1,4-XYLOSYLTRANSFERASE IRX9"; also contains rice GT43A Q75L84) and IRX14 in **PTHR10896:SF63** ("BETA-1,4-XYLOSYLTRANSFERASE IRX14"). Additional plant GT43 members populate several further subfamilies (e.g. IRX9L-related SF20, IRX14H-related SF17, IRX9-related SF26, GT43E-related SF31, and other rice "glucuronosyltransferase"-named subfamilies SF24/25/32/33). The **animal beta-1,3-glucuronyltransferases** occupy separate subfamilies — B3GAT1 in SF21, B3GAT2 in SF8, B3GAT3 / GlcAT-I / sqv-8 in SF65, and *Drosophila* GlcAT-P (SF50) and GlcAT-S (SF51).

The parent family therefore **spans kingdoms** (22 subfamilies across 5,376 taxa, including metazoa, plants, and other eukaryotes) and mixes two mechanistically different reactions: GAG-linker glucuronylation (animal) and xylan-backbone xylosyltransfer (plant). The plant xylan-synthase members are confined to their own subfamily set (notably SF59 and SF63 for the two exemplars).

## IBA / PAINT Assessment

No local PAINT IBD data available for this family (`PTHR10896-paint.tsv` is absent). PTN node id(s) not determined here.

## InterPro2GO / parent-family mapping verdict

A **whole-protein GO mapping of the specialized xylan activity at the PARENT level is NOT safe.** The parent GT43 family is a mixed, cross-kingdom clade whose name and largest metazoan contingent correspond to a **different reaction** (`GO:0015020` glucuronosyltransferase / beta-1,3-glucuronyltransferase acting on the proteoglycan linker), not xylan synthesis. Mapping `GO:0047517 1,4-beta-D-xylan synthase activity` (or a xylan-backbone xylosyltransferase term) onto every PTHR10896 member would over-annotate all animal B3GAT1/2/3 and insect GlcAT proteins, which do not make xylan. Additionally, IRX9/IRX14 act only as components of a multi-subunit xylan-synthase complex and IRX9 in particular may be catalytically supportive rather than the sole catalytic subunit, so even the plant assignment is best expressed as a subfamily/complex-scoped annotation. **Verdict: restrict the xylan-synthase function to the plant subfamilies (e.g. SF59/IRX9, SF63/IRX14) via SF-level or PAINT-node annotation; keep only the general GT-A glucuronyl/xylosyltransferase framing at parent level.**

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT (none for this family), UniProt, plant bioenergy xylan-module curation
