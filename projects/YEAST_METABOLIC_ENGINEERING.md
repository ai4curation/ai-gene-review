---
title: "Yeast Metabolic Engineering & Bioproduction"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [yeast]
last_reviewed: '2026-10-05'
autolink_gene_symbols: false
manifest:
  slides:
    - href: YEAST_METABOLIC_ENGINEERING/slides/YEAST_METABOLIC_ENGINEERING-slides.html
      description: Yeast metabolic engineering slides
---

# Yeast Metabolic Engineering & Bioproduction

**Bottom line:** scoped, not yet started. Industrial *S. cerevisiae*
strains are engineered by redirecting flux through glycolysis and ethanol
fermentation, cutting the glycerol byproduct and balancing NADH and NADPH.
This project picked 10 central-carbon genes that engineers commonly target
(PDC1, ADH1, ADH2, GPD1, GPD2, HXK1, PFK1, PYC1, TDH1, ZWF1) to check that
their GO annotations are accurate and complete enough to support pathway
design. None of the 10 has a review folder under `genes/yeast/` yet, and the
repo does not have a custom module YAML for this fermentation and glycerol
branch yet; cached SGD YeastPathways GO-CAMs already cover the core glucose
fermentation, glycolysis, and pentose phosphate entries for much of the set.
Before starting,
the list is worth one check: on glucose, HXK2 rather than HXK1 is the main
hexokinase and TDH3 the main GAPDH isoform, so the paralog pairs may be
better reviewed together.

## Overview

This project reviews *Saccharomyces cerevisiae* genes central to metabolic engineering for bioproduction. Recent computational studies (ecFactory, 2024) have identified key genetic targets for optimizing production of bioethanol, specialty chemicals, and renewable fuels. The focus is on:

1. **Primary alcohol production pathway** - ethanol fermentation (PDC1, ADH1, ADH2)
2. **Byproduct suppression** - reducing glycerol accumulation (GPD1, GPD2)
3. **Redox metabolism** - NAD+/NADH balance for efficient fermentation
4. **Central carbon metabolism** - glucose catabolism and cofactor recycling
5. **PPP and anaplerotic support** - NADPH supply and pyruvate carboxylation (ZWF1, PYC1)

## Biological Significance

These genes represent foundational metabolic functions that can be rationally engineered to:

- Increase ethanol/chemical yields per glucose
- Reduce undesired byproducts
- Improve strain robustness under industrial conditions
- Enable new synthetic pathways for novel chemical production

## Project Goals

- Synthesize current knowledge of metabolic engineering targets in yeast
- Review existing GO annotations for accuracy and completeness
- Identify gaps in functional annotation
- Propose improved terms reflecting engineering-relevant functions
- Create a reference resource for metabolic engineering research

---

# STATUS

Last updated: 2026-10-05

## Genes to Review

- Todo: PDC1 - Pyruvate decarboxylase 1 (primary ethanol pathway)
- Todo: ADH1 - Alcohol dehydrogenase 1 (primary ethanol pathway)
- Todo: ADH2 - Alcohol dehydrogenase 2 (secondary/stress responder)
- Todo: GPD1 - Glycerol-3-phosphate dehydrogenase 1 (byproduct suppression)
- Todo: GPD2 - Glycerol-3-phosphate dehydrogenase 2 (byproduct suppression)
- Todo: HXK1 - Hexokinase 1 (glucose phosphorylation)
- Todo: PFK1 - Phosphofructokinase 1 (glycolytic rate-limiting step)
- Todo: PYC1 - Pyruvate carboxylase (gluconeogenesis/anaplerosis)
- Todo: TDH1 - GAPDH (core glycolytic enzyme)
- Todo: ZWF1 - Glucose-6-phosphate dehydrogenase (pentose phosphate pathway)

## Progress

- Total genes: 10
- Reviewed: 0
- In progress: 0
- Remaining work: [#3961](https://github.com/ai4curation/ai-gene-review/issues/3961)

---

# NOTES

## 2025-12-30

- Project initialized
- Selected metabolic engineering & bioproduction as focus area
- Identified 10 candidate genes spanning primary alcohol production, byproduct suppression, and central carbon metabolism
- Ready to begin gene review workflow
