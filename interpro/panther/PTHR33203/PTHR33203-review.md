# PANTHER Family Review: PTHR33203

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR33203 |
| **Family Name** | OLEOSIN |
| **InterPro Entry** | IPR000136 (integrated) |
| **Total Proteins** | 3,508 |
| **Taxonomic Breadth** | 1,132 taxa; 376 proteomes (Viridiplantae — gymnosperms and angiosperms) |
| **Subfamilies** | 31 |
| **Module role** | Oil-body **packaging/biogenesis** (not a Kennedy-pathway enzyme) — structural surface protein of seed lipid droplets (oleosomes). Exemplar: `UniProtKB:Q39165 (OLEO2_ARATH)` at **PTHR33203:SF32**; no catalytic MF — related process `GO:0010344 seed oilbody biogenesis` |

## Executive Summary

PTHR33203 is the **oleosin family**, small, plant-specific **structural proteins** that coat the surface of seed oil bodies (oleosomes / lipid droplets). An oleosin has a long central hydrophobic hairpin (with a conserved proline knot) that inserts into the triacylglycerol core and two amphipathic arms that lie on the phospholipid monolayer surface. Oleosins do **not** catalyze any reaction; instead they stabilize oil bodies, control their size, prevent coalescence, and are required for normal oil-body biogenesis and for lipid mobilization during germination.

Relative to the Kennedy-pathway enzymes (GPAT9 → LPAAT → PAP → DGAT/PDAT) that *synthesize* seed triacylglycerol, oleosins act **downstream in packaging**: the TAG produced by those enzymes is deposited into oil bodies whose surface is stabilized by oleosins. The appropriate GO characterization is therefore a **cellular-component / biological-process** one (oil-body surface; `GO:0010344 seed oilbody biogenesis` and lipid-storage processes), not a molecular-function catalytic term. Assigning any enzymatic MF to this family would be an over-annotation.

## Subfamily Analysis

- **Exemplar subfamily**: Arabidopsis oleosin OLEO2 (21.2 kDa, Q39165) is **PTHR33203:SF32** ("OLEOSIN 21.2 KDA"). Other Arabidopsis seed oleosins map to SF25 (18.5 kDa), SF35 (14.9 kDa), SF44 (20.3 kDa) and SF61 (oleosin 5); tapetal/glycine-rich oleosin relatives fall in SF26/SF49/SF52.
- **Broad parent**: 31 subfamilies but a **narrow, homogeneous taxonomic range — entirely Viridiplantae** (gymnosperms such as *Pinus*, and angiosperms: Arabidopsis, Brassica, maize, rice, soybean, peanut, sesame, cotton, sunflower, hazel, almond). Only **376 proteomes / 1,132 taxa**, by far the most lineage-restricted of the seed-TAG-module families. The subfamily structure reflects seed vs. tapetal/pollen oleosin classes and size variants rather than different biochemical activities (all are structural oil-body/lipid-droplet proteins).

## IBA / PAINT Assessment

No local PAINT IBD data available for this family (`PTHR33203-paint.tsv` is not present). PANTHER PTN node identifiers and propagated terms are therefore not determined here.

## InterPro2GO / parent-family mapping verdict

**No molecular-function (catalytic) GO term should be mapped to this family at any level — oleosins are non-enzymatic structural proteins.** Because the family is taxonomically homogeneous (Viridiplantae oil-body/lipid-droplet proteins), **structural-role and localization/process terms are safe at or near the family (and IPR000136) level**: e.g. lipid-droplet / monolayer-surrounded lipid-storage-body cellular-component terms and lipid-storage / oil-body processes, with `GO:0010344 seed oilbody biogenesis` appropriate for the seed-oleosin subfamilies. Care is only needed to distinguish the **seed oleosins** (seed oil-body biogenesis) from the **tapetal/pollen "glycine-rich" oleosin** subfamilies (SF26/SF49/SF52), whose process context is pollen-coat rather than seed oil storage; a seed-specific process term should stay at the seed-oleosin subfamily level.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, plant bioenergy module curation (no local PAINT available)
