---
title: "PINK1-Parkin Mitophagy Project"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [PINK1, PRKN, OPTN, CALCOCO2, SQSTM1, TAX1BP1, NBR1, TBK1, BNIP3, BNIP3L, FUNDC1, PHB2, VCP, MFN2]   # all 14 candidates now reviewed; see the table below
manifest:
  slides:
    - href: MITOPHAGY/slides/MITOPHAGY-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/6cKsT95CWm1eYy7upcA6HU
      title: Project brief
index_group: MAMMAL
---

# PINK1-Parkin Mitophagy Project

**Bottom line:** the seed review work is done. In PINK1-Parkin mitophagy, the
PINK1 kinase accumulates on damaged mitochondria and makes phospho-ubiquitin,
which activates the Parkin (PRKN) E3 ligase; ubiquitin-binding receptors (OPTN,
CALCOCO2, SQSTM1, TAX1BP1, NBR1) then link the organelle to the autophagosome.
All 14 candidates in the table below now have completed reviews, and
`modules/mitophagy.yaml` models the pathway across human and *C. elegans*.
Mitophagy is a core function in the reviews of PINK1, PRKN, OPTN (`type 2
mitophagy`, GO:0061734), CALCOCO2, BNIP3, BNIP3L, FUNDC1, PHB2 and VCP, and
non-core for SQSTM1 and MFN2; TAX1BP1, NBR1 and TBK1 carry no mitophagy process
row at all and are placed in the pathway through their adaptor and kinase
functions rather than a mitophagy term. The clearest molecular-function result
is that the four integral outer- and inner-membrane receptors converge on one
term, `mitochondrion autophagosome adaptor activity` (GO:0140580): BNIP3,
BNIP3L, FUNDC1 and PHB2 all take it as a core function, which is also the core
molecular function of the worm receptors dct-1 and fndc-1 in
[CAEEL_MITOPHAGY](CAEEL_MITOPHAGY.md). Eight of the 14 reviews were made
earlier for Proteostasis and other projects (OPTN, CALCOCO2, SQSTM1, TAX1BP1,
NBR1, TBK1, BNIP3L, VCP), and several candidates are also listed by other
project pages — VCP by
[RIBOSOME_QUALITY_CONTROL](RIBOSOME_QUALITY_CONTROL.md) and
[STRESS_GRANULES](STRESS_GRANULES.md), SQSTM1 by
[CONDENSATES](CONDENSATES.md) — so do not sum row totals across project
pages. What is left is module refinement rather than gene fetching: see
[Project Status](#project-status).

## Overview

Mitophagy is the selective autophagy of damaged mitochondria. The PINK1-Parkin pathway is the best-characterized mitophagy pathway, where mitochondrial damage stabilizes PINK1 kinase, which recruits and activates the Parkin E3 ubiquitin ligase.

## Model Species

**Primary: Homo sapiens (human)**
- Parkinson's disease relevance
- Well-characterized pathway

## Core Pathway Architecture

### 1. Damage Sensing
- **PINK1** - Kinase, stabilized on damaged mitochondria
- **TOMM complex** - PINK1 import/stabilization

### 2. Ubiquitin Ligase
- **PRKN** (Parkin) - E3 ubiquitin ligase
- **Phospho-ubiquitin** - PINK1 product, Parkin activator

### 3. Mitophagy Receptors
Ubiquitin-binding autophagy receptors:
- **OPTN** - Optineurin
- **CALCOCO2** (NDP52) - Autophagy receptor
- **SQSTM1** (p62) - Autophagy receptor
- **TAX1BP1** - Autophagy receptor
- **NBR1** - Autophagy receptor

### 4. Autophagy Machinery
- **ULK1 complex** - Initiation
- **LC3/GABARAP** - Autophagosome proteins
- **TBK1** - Phosphorylates receptors

### 5. Alternative Mitophagy
PINK1/Parkin-independent:
- **BNIP3/BNIP3L** (NIX) - Receptor-mediated
- **FUNDC1** - Hypoxia-induced
- **PHB2** - Inner membrane receptor

## Candidate Genes (14)

All 14 have completed reviews. "Core MF" is the molecular function the review
takes as core for the mitophagy role (several reviews have more than one core
function; only the mitophagy-relevant one is listed). "Mitophagy process" is
how the review treats mitophagy process terms.

| Gene | UniProt | Role | Review | Core MF for the role | Mitophagy process |
|------|---------|------|--------|----------------------|-------------------|
| PINK1 | Q9BXM7 | Kinase | done | protein serine/threonine kinase activity | core |
| PRKN | O60260 | E3 ligase | done | ubiquitin protein ligase activity | core |
| OPTN | Q96CV9 | Ubiquitin-reading receptor | done | protein-macromolecule adaptor activity (GO:0030674) | core (`type 2 mitophagy`) |
| CALCOCO2 | Q13137 | NDP52 receptor | done | autophagy cargo adaptor activity | core (proposed as a NEW row) |
| SQSTM1 | Q13501 | p62 receptor | done | ubiquitin-modified protein reader activity | non-core |
| TAX1BP1 | Q86VP1 | Minor receptor | done | autophagy cargo adaptor activity | no mitophagy row |
| NBR1 | Q14596 | Minor receptor | done | autophagy cargo adaptor activity | no mitophagy row |
| TBK1 | Q9UHD2 | Receptor kinase | done | protein serine/threonine kinase activity | no mitophagy row |
| BNIP3 | Q12983 | Outer-membrane receptor | done | mitochondrion autophagosome adaptor activity (GO:0140580) | core |
| BNIP3L | O60238 | NIX receptor | done | mitochondrion autophagosome adaptor activity (GO:0140580) | core (`regulation of mitophagy`) |
| FUNDC1 | Q8IVP5 | Hypoxia receptor | done | mitochondrion autophagosome adaptor activity (GO:0140580) | core |
| PHB2 | Q99623 | Inner-membrane receptor | done | mitochondrion autophagosome adaptor activity (GO:0140580) | core |
| VCP | P55072 | Outer-membrane extraction | done | ATP hydrolysis activity | core |
| MFN2 | O95140 | Parkin substrate | done | GTPase activity | non-core |

## Module

[mitophagy](../modules/mitophagy.html) (`modules/mitophagy.yaml`, `MODULE:mitophagy`,
status `DRAFT`, scope `CONCRETE`) models the pathway for Eumetazoa with human
and *C. elegans* representatives, in five parts:

1. PINK1/Parkin ubiquitin signalling on damaged mitochondria (`type 2
   mitophagy`, GO:0061734)
2. Mitophagy receptor recognition, as a `ONE_OR_MORE` variant set over the
   ubiquitin-reading receptors (OPTN, CALCOCO2), the BNIP3/NIX family, the
   FUNDC1 family and the nematode-specific ALLO-1 allophagy receptor
3. Receptor capture by Atg8-family proteins on the phagophore (MAP1LC3B,
   GABARAP, worm LGG-1)
4. The nematode FIS-1/FIS-2 step that completes disposal of fission-derived
   fragments
5. Basal restraint of receptor-mediated mitophagy by SCF-FBXL4, which degrades
   BNIP3 and NIX

Autophagosome biogenesis (ULK1, ATG9A and the lipidation cascade) is out of
boundary and lives in `MODULE:metazoan_autophagosome_biogenesis`; the module's
`notes` record why SQSTM1, TAX1BP1, NBR1 and TBK1 are deliberately left out as
members.

## Disease Relevance

- Parkinson's disease (PINK1, PRKN mutations)
- ALS (OPTN, TBK1 mutations)
- Mitochondrial diseases

## Project Status

Seed reviews and the module are delivered:

- [x] Gene folders and reviews for all 14 candidates
- [x] PINK1 and PRKN reviews (the kinase/E3 pair)
- [x] Alternative-receptor reviews: BNIP3, FUNDC1, PHB2, plus the MFN2 Parkin
      substrate
- [x] A mitophagy module spanning ubiquitin-dependent marking, receptor
      recognition and Atg8-family docking

Remaining work, none of it blocking:

- [ ] Fold PHB2 into the module: the inner-membrane route was reviewed after
      the module was written, and part 2's variant set still covers only
      outer-membrane and ubiquitin-reading receptors
- [ ] Decide whether VCP (outer-membrane substrate extraction) and MFN2 (Parkin
      substrate) belong as module parts or stay as context, and record the
      decision in the module `notes` either way
- [ ] Cross-check the production GO-CAMs that model parts of this pathway
      against the curated reviews
- [ ] Move the module from `DRAFT` once the above are settled
