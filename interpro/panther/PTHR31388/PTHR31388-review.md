# PANTHER Family Review: PTHR31388

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR31388 |
| **Family Name** | PEROXIDASE 72-RELATED |
| **InterPro Entry** | IPR000823 |
| **Total Proteins** | 16,500 |
| **Taxonomic Breadth** | 1,248 taxa |
| **Subfamilies** | 132 |
| **Representative Structure** | 1hch (horseradish peroxidase C1A compound I) |
| **Module role** | Provides **class III secretory (plant) peroxidase**, which oxidatively polymerizes monolignols into lignin in the cell wall. Exemplar: `UniProtKB:Q9FJZ9 (PER72_ARATH, AtPRX72)`, PANTHER `PTHR31388:SF3`; function `GO:0004601 peroxidase activity`. |

## Executive Summary

PTHR31388 is a family of **plant class III secretory peroxidases** (the IPR000823 plant-peroxidase clade; heme-containing, EC 1.11.1.7). These enzymes reduce H2O2 while oxidizing a wide range of phenolic and other substrates via one-electron radical chemistry. The family is taxonomically confined to land plants (~1,248 taxa) but is very large in gene number (16,500 proteins, 132 subfamilies), reflecting the well-known massive expansion of class III peroxidases in plant genomes.

In lignification, class III peroxidases (with laccases; see PTHR11709) catalyze the final oxidative coupling of monolignols into the lignin polymer, using apoplastic H2O2. The same enzyme family, however, participates in many other processes — auxin catabolism, cross-linking of cell-wall structural components, suberization, reactive-oxygen signaling, wound/pathogen defense, seed-coat mucilage, and stress responses. Thus the **molecular function (peroxidase activity) is essentially homogeneous across the family, but the biological role/substrate is subfamily- and context-specific.**

## Subfamily Analysis

The exemplar AtPRX72 (Q9FJZ9) belongs to `PTHR31388:SF3` (PEROXIDASE 72). The reviewed entries span 31 distinct subfamilies of the 132 in the family. Unlike the broad-superfamily lignin modules, the family name — **PEROXIDASE 72-RELATED** — and its InterPro integration (IPR000823 plant peroxidase) reflect the same class III peroxidase activity throughout; diversification is chiefly in physiological role (lignin vs. defense vs. mucilage vs. hypoxia) rather than in core catalytic chemistry.

## IBA / PAINT Assessment

Local PAINT (`PTHR31388-paint.tsv`) shows a homogeneous MF (peroxidase) distributed over role-specific process/component nodes:

| Node (PTN) | GO term(s) | Aspect | Interpretation |
|------------|-----------|--------|----------------|
| PTN001261499 | `GO:0004601 peroxidase activity`; `GO:0009505 plant-type cell wall`; `GO:0006950 response to stress` | F/C/P | Core cell-wall peroxidase clade. |
| PTN007876793 | `GO:0004601 peroxidase activity`; `GO:0009505 plant-type cell wall` | F/C | Second cell-wall peroxidase clade (land plants, taxon:3193). |
| PTN001584130 / PTN004818249 | `GO:0009809 lignin biosynthetic process` | P | Lignin-associated clades. |
| PTN000775420 | `GO:0048658 anther wall tapetum development` | P | Anther-development clade. |
| PTN002047285 | `GO:0080001 mucilage extrusion from seed coat` | P | Seed-coat mucilage clade. |
| PTN007876857 | `GO:0071456 cellular response to hypoxia` | P | Hypoxia-response clade. |
| PTN009119955 | `GO:0002215 defense response to nematode` | P | Defense clade. |

The MF term `GO:0004601 peroxidase activity` is propagated on the two cell-wall peroxidase nodes, while the many process terms (lignin biosynthesis, mucilage, hypoxia, nematode defense, tapetum development) are distributed to distinct role-specific nodes. This correctly reflects one shared catalytic activity with divergent biological contexts.

## InterPro2GO / parent-family mapping verdict

For **molecular function**, `GO:0004601 peroxidase activity` is a **safe family/parent-level mapping**: PTHR31388 / IPR000823 is a homogeneous, plant-restricted class III peroxidase family, and every member is expected to be a heme peroxidase. This is the one lignin-module family where a whole-protein MF term is defensible at the parent level. **However, the specific lignin-polymerization role must not be generalized:** `GO:0009809 lignin biosynthetic process` and the other role terms (mucilage, hypoxia, defense, tapetum) are subfamily/context-specific and are correctly kept at individual PAINT nodes. In short — MF (peroxidase) OK at family level; the lignin-biosynthesis process assignment should remain restricted to the relevant lignin-peroxidase subfamilies/nodes.

## Review Status

- **Date**: 2026-07-11
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, local PAINT, UniProt, plant bioenergy module curation
