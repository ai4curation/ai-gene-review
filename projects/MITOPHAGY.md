---
title: "PINK1-Parkin Mitophagy Project"
maturity: SCOPING
last_reviewed: "2026-10-04"
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
genes: [OPTN, CALCOCO2, SQSTM1, TAX1BP1, NBR1, TBK1, BNIP3L, VCP]   # reviewed genes only; full candidate list is in the table below
manifest:
  slides:
    - href: MITOPHAGY/slides/MITOPHAGY-slides.html
      description: AI generated
---

# PINK1-Parkin Mitophagy Project

**Bottom line:** scoped around the human PINK1-Parkin and receptor-mediated
mitophagy network, but still missing the kinase/E3 center. PINK1 stabilizes on
damaged mitochondria and activates the Parkin (PRKN) E3 ligase through
phospho-ubiquitin; in the reviewed set, OPTN and CALCOCO2 are the primary
ubiquitin-binding receptors that recruit LC3/GABARAP-family autophagy
machinery. SQSTM1, TAX1BP1 and NBR1 are selective-autophagy adaptors that can
appear at damaged mitochondria, but the current reviews treat their direct
mitophagy roles as non-core or not yet represented by direct mitophagy rows.
Eight of the 14 candidates already have reviews made for Proteostasis and other
projects (OPTN, CALCOCO2, SQSTM1, TAX1BP1, NBR1, TBK1, BNIP3L and VCP), but
there is no mitophagy module and PINK1 and PRKN themselves have not been
reviewed. The existing reviews already make mitophagy a core function of OPTN
(`type 2 mitophagy`, GO:0061734), CALCOCO2, BNIP3L and VCP, and a real but
non-core role of SQSTM1. BNIP3, FUNDC1, PHB2 and MFN2 are also unreviewed. The
worm counterpart, [CAEEL_MITOPHAGY](CAEEL_MITOPHAGY.md), is much further along.

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

### 5. Receptor-mediated and noncanonical mitophagy

- **BNIP3/BNIP3L** (NIX) - Outer-membrane LIR receptors
- **FUNDC1** - Hypoxia-induced outer-membrane LIR receptor
- **PHB2** - Inner-membrane receptor exposed after outer-membrane rupture

## Candidate genes (14)

| Gene | UniProt | Function | Review status |
|------|---------|----------|---------------|
| PINK1 | Q9BXM7 | Damage-stabilized kinase | Missing; tracked in [#3956](https://github.com/ai4curation/ai-gene-review/issues/3956) |
| PRKN | O60260 | Parkin E3 ubiquitin ligase | Missing; tracked in [#3956](https://github.com/ai4curation/ai-gene-review/issues/3956) |
| OPTN | Q96CV9 | Ubiquitin-binding receptor | Reviewed; core GO:0061734 `type 2 mitophagy` |
| CALCOCO2 | Q13137 | NDP52 ubiquitin-binding receptor | Reviewed; core GO:0000423 `mitophagy` |
| SQSTM1 | Q13501 | p62 ubiquitin-binding receptor | Reviewed; GO:0000423 retained as non-core |
| TAX1BP1 | Q86VP1 | Selective-autophagy receptor | Reviewed; xenophagy/macroautophagy core, no direct mitophagy row |
| NBR1 | Q14596 | Selective-autophagy receptor | Reviewed; aggrephagy/macroautophagy core, no direct mitophagy row |
| TBK1 | Q9UHD2 | Receptor kinase | Reviewed; selective-autophagy kinase, no direct mitophagy row |
| BNIP3 | Q12983 | LIR mitophagy receptor | Missing; tracked in [#3956](https://github.com/ai4curation/ai-gene-review/issues/3956) |
| BNIP3L | O60238 | NIX LIR mitophagy receptor | Reviewed; core GO:0140580 `mitochondrion autophagosome adaptor activity` |
| FUNDC1 | Q8IVP5 | LIR mitophagy receptor | Missing; tracked in [#3956](https://github.com/ai4curation/ai-gene-review/issues/3956) |
| PHB2 | Q99623 | Inner-membrane receptor | Missing; tracked in [#3956](https://github.com/ai4curation/ai-gene-review/issues/3956) |
| VCP | P55072 | OMM protein extraction | Reviewed; core GO:0000423 `mitophagy` |
| MFN2 | O95140 | Parkin substrate/adaptor | Missing; tracked in [#3956](https://github.com/ai4curation/ai-gene-review/issues/3956) |

## Existing review results

| Gene | Current mitophagy outcome |
|------|---------------------------|
| OPTN | `ACCEPT` IMP row on GO:0061734 `type 2 mitophagy`; core PINK1/Parkin mitophagy receptor |
| CALCOCO2 | `NEW` IMP row on GO:0000423 `mitophagy`; core NDP52 receptor/adaptor |
| SQSTM1 | IBA/IGI/NAS mitophagy rows kept as `KEEP_AS_NON_CORE`; p62 clusters damaged mitochondria but is dispensable for the clearance step |
| TAX1BP1 | reviewed as a ubiquitin-binding autophagy cargo adaptor for macroautophagy/xenophagy; mitochondrial rows are context-dependent `KEEP_AS_NON_CORE` localizations |
| NBR1 | reviewed as a selective autophagy receptor; Parkin-mitophagy mitochondrial colocalization kept as non-core and a predicted intermembrane-space row removed |
| TBK1 | reviewed as a kinase for innate immunity and selective autophagy; mitophagy is represented through OPTN/CALCOCO2 receptor phosphorylation rather than a direct BP row |
| BNIP3L | `ACCEPT` GO:1901524 `regulation of mitophagy` and `NEW` GO:0140580 `mitochondrion autophagosome adaptor activity`; core NIX outer-membrane receptor |
| VCP | `ACCEPT` IDA row on GO:0000423 `mitophagy`; core AAA-ATPase for extraction of ubiquitinated outer-membrane proteins |

## Disease Relevance

- Parkinson's disease (PINK1, PRKN mutations)
- Amyotrophic lateral sclerosis (OPTN, TBK1 mutations)
- VCP-linked multisystem proteinopathy, through defective clearance of damaged mitochondria

## Project Status

- [x] Cross-project reviews checked for OPTN, CALCOCO2, SQSTM1, TAX1BP1,
  NBR1, TBK1, BNIP3L and VCP
- [ ] Fetch and review PINK1, PRKN, BNIP3, FUNDC1, PHB2 and MFN2
  ([#3956](https://github.com/ai4curation/ai-gene-review/issues/3956))
- [ ] Build a PINK1-Parkin mitophagy module after the E3 ligase, kinase and
  alternative mitochondrial receptors are reviewed
