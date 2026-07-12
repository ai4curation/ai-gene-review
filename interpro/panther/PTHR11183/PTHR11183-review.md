# PANTHER Family Review: PTHR11183

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR11183 |
| **Family Name** | GNT1/Glycosyltransferase 8 |
| **InterPro Entry** | IPR050587 |
| **Total Proteins** | 18,986 |
| **Taxonomic Breadth** | 10,164 taxa |
| **Subfamilies** | 54 |
| **Representative Structure** | 3u2u (human Glycogenin-1 / GYG1 with Mn, UDP, maltotetraose) |
| **Module role** | Xylan sidechain decoration (secondary cell wall glucuronoxylan/GAX). Adds alpha-1,2-linked (methyl)glucuronic acid branches to the xylan backbone. Exemplar: `UniProtKB:Q9LSB1 (GUX1_ARATH)`; PANTHER SF not assigned (family-level). Associated function `GO:0080116 glucuronoxylan glucuronosyltransferase activity`. |

## Executive Summary

PTHR11183 is the **glycosyltransferase family 8 (GT8)** clade, a retaining GT-A superfamily. Its members carry out a **broad range of unrelated glucosyl/galactosyl/glucuronosyl transfers** onto diverse acceptors: fungal glycogenins (GLG1/GLG2) and animal glycogenins (GYG1/GYG2) that self-glucosylate to prime glycogen synthesis; plant galactinol synthases (GOLS1-10) that make galactinol for raffinose-family oligosaccharide (osmoprotectant) synthesis; fungal N-acetylglucosaminyltransferases (GNT1); plant inositol-phosphorylceramide glucuronosyltransferase (IPUT1); and the **plant xylan alpha-glucuronosyltransferases GUX** (and the related PGSIP proteins).

In glucuronoxylan/GAX biosynthesis, the **GUX** subfamily (GlucUronic acid substitution of Xylan; GUX1/GUX2/GUX3, plus putative GUX4/GUX5 and PGSIP7/PGSIP8) transfers alpha-1,2-linked D-glucuronic acid from UDP-GlcA onto the xylan backbone, generating the GlcA branches that GXM (PTHR31444) subsequently 4-O-methylates. GUX1 and GUX2 together account for most GlcA/MeGlcA decoration of stem glucuronoxylan and are required for normal wall integrity and recalcitrance. The GUX activity is thus one specialized branch of a functionally heterogeneous GT8 parent that otherwise centers on glycogenin/galactinol-synthase chemistry unrelated to cell-wall xylan.

## Subfamily Analysis

In the local entries table the plant GUX members (`Q9LSB1 GUX1`, `Q8GWW4 GUX2`, `Q8W4A7 GUX3`, `Q9FZ37 GUX4`, `F4HZC3 GUX5`) and the PGSIP paralogs carry **no PANTHER subfamily assignment** (SF column blank), consistent with the anchor listing GUX at family level (SF n/a). The exemplar GUX1 (Q9LSB1) is therefore best cited at the **PTHR11183 family level**, not a specific SF, in the local data.

The parent is large and **spans kingdoms** (54 subfamilies, 10,164 taxa) — fungi (GLG, GNT1), metazoa (glycogenins), plants (galactinol synthases, GUX/PGSIP, IPUT1), and even a mimivirus entry (Q5UNW1). The GT8 fold is shared, but the acceptor substrates (glycogen primer vs. inositol vs. xylan vs. myo-inositol/galactinol) are entirely different, making this one of the more functionally diverse parents in the xylan module set.

## IBA / PAINT Assessment

No local PAINT IBD data available for this family (`PTHR11183-paint.tsv` is absent). PTN node id(s) not determined here.

## InterPro2GO / parent-family mapping verdict

A **whole-protein GO mapping of the xylan glucuronosyltransferase activity at the PARENT level is NOT safe.** GT8 (PTHR11183) is explicitly a multi-activity family (glycogenin self-glucosylation, galactinol synthesis, GlcNAc transfer, IPC glucuronylation, xylan glucuronylation). Propagating `GO:0080116 glucuronoxylan glucuronosyltransferase activity` to all members would grossly over-annotate glycogenins and galactinol synthases, which never touch xylan. The specific function must be scoped to the **GUX/PGSIP subclade** (via PAINT-node or curated-member annotation, since these lack a distinct SF id in the local data). At parent level only a generic retaining-GT8 glycosyltransferase framing is defensible. **Verdict: keep GUX xylan glucuronosyltransferase at subclade/PAINT level, not parent level.**

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT (none for this family), UniProt, plant bioenergy xylan-module curation
