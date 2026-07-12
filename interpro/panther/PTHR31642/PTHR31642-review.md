# PANTHER Family Review: PTHR31642

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR31642 |
| **Family Name** | Plant and Fungal Acyltransferase |
| **InterPro Entry** | none (not integrated) |
| **Total Proteins** | 18,493 |
| **Taxonomic Breadth** | 3,829 taxa |
| **Subfamilies** | 142 |
| **Representative Structure** | 5kjv (HCT from *Coleus blumei*) |
| **Module role** | Provides **HCT (hydroxycinnamoyl-CoA:shikimate/quinate hydroxycinnamoyltransferase)**, a BAHD acyltransferase that routes *p*-coumaroyl-CoA into the 3-hydroxylation (C3'H) branch of monolignol biosynthesis. Exemplar: `UniProtKB:Q9FI78 (HST_ARATH, AtHCT)`, PANTHER `PTHR31642:SF11`; function `GO:0047172 shikimate O-hydroxycinnamoyltransferase activity`. |

## Executive Summary

PTHR31642 is a large **BAHD-type acyltransferase** family (the "Plant and Fungal Acyltransferase" superfamily). BAHD enzymes use a conserved His-x-x-x-Asp catalytic motif to transfer an acyl group from an acyl-CoA donor to a hydroxyl (or amine) acceptor, and they underlie an enormous range of plant/fungal specialized metabolism (phytoalexins, volatiles, alkaloids, mycotoxins, and cell-wall-directed acyl esters).

Within this family the lignin-module enzyme is **HCT (hydroxycinnamoyl-CoA:shikimate/quinate hydroxycinnamoyltransferase, EC 2.3.1.133)**. HCT esterifies *p*-coumaroyl-CoA to shikimate (or quinate), producing *p*-coumaroyl-shikimate, the substrate that C3'H (CYP98A) hydroxylates at the 3-position; a second HCT-catalyzed transesterification then returns the 3-hydroxylated acyl group to CoA as caffeoyl-CoA. HCT therefore forms, with C3'H, the meta-hydroxylation shunt that is essential for guaiacyl/syringyl lignin. HCT is one of ~142 BAHD subfamilies, most of which act on entirely different acyl acceptors.

## Subfamily Analysis

The exemplar AtHCT (Q9FI78) belongs to `PTHR31642:SF11` (SHIKIMATE O-HYDROXYCINNAMOYLTRANSFERASE). The reviewed entries cover 22 distinct subfamilies of the 142 in the family, and the family name — **Plant and Fungal Acyltransferase** — reflects the generic BAHD acyl-transfer chemistry, not HCT specifically. Substrate/acceptor specificity is the principal axis of diversification across BAHD subfamilies, so the specific shikimate-hydroxycinnamoyltransferase activity is a property of the HCT subfamily, not the family as a whole.

## IBA / PAINT Assessment

Local PAINT (`PTHR31642-paint.tsv`) is deliberately conservative:

| Node (PTN) | GO term | Aspect | Interpretation |
|------------|---------|--------|----------------|
| PTN001270227 | `GO:0016747 acyltransferase activity, transferring groups other than amino-acyl groups` | F | Broad eukaryote (taxon:2759) BAHD acyltransferase node. |
| PTN002420108 | `GO:0044550 secondary metabolite biosynthetic process` | P | Fungal (Pezizomycotina, taxon:147538) secondary-metabolism clade. |

Notably, the specific HCT term `GO:0047172` is **not** propagated by PAINT; only the generic acyltransferase MF and a fungal secondary-metabolism process are assigned. This reflects appropriate caution given the acceptor-specificity diversity of BAHD enzymes.

## InterPro2GO / parent-family mapping verdict

Whole-protein mapping of `GO:0047172 shikimate O-hydroxycinnamoyltransferase activity` at the **parent level is unsafe**. PTHR31642 is a 142-subfamily BAHD acyltransferase family spanning plants and fungi with highly divergent acyl-acceptor specificities; the only family-wide-defensible MF is the generic `GO:0016747 acyltransferase activity, transferring groups other than amino-acyl groups` (as PAINT already assigns). The HCT-specific activity must be restricted to the **HCT subfamily (`PTHR31642:SF11`) / a dedicated PAINT node**. Because no HCT-specific PAINT node currently exists in the local data, the specific function should be curated at the subfamily/experimental level rather than propagated.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
