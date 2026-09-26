---
title: "Yeast Metabolic Engineering & Bioproduction"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [yeast]
genes: [PDC1, ADH1, ADH2, GPD1, GPD2, HXK1, PFK1, PYC1, TDH1, ZWF1]
---

# Yeast Metabolic Engineering & Bioproduction

**Bottom line:** scoped, not yet started. Industrial *S. cerevisiae*
strains are engineered by redirecting flux through glycolysis and ethanol
fermentation, cutting the glycerol byproduct and balancing NADH and NADPH.
This project picked 10 central-carbon genes that engineers commonly target
(PDC1, ADH1, ADH2, GPD1, GPD2, HXK1, PFK1, PYC1, TDH1, ZWF1) to check that
their GO annotations are accurate and complete enough to support pathway
design. None of the 10 has a review folder under `genes/yeast/` yet, and the
repo glycolysis and pentose phosphate modules do not cite these yeast
proteins. Before starting,
the list is worth one check: on glucose, HXK2 rather than HXK1 is the main
hexokinase and TDH3 the main GAPDH isoform, so the paralog pairs may be
better reviewed together.

## Overview

This project reviews *Saccharomyces cerevisiae* genes central to metabolic engineering for bioproduction. Recent computational studies (ecFactory, 2024) have identified key genetic targets for optimizing production of bioethanol, specialty chemicals, and renewable fuels. The focus is on:

1. **Primary alcohol production pathway** - ethanol fermentation (PDC1, ADH1, ADH2)
2. **Byproduct suppression** - reducing glycerol accumulation (GPD1, GPD2)
3. **Redox metabolism** - NAD+/NADH balance for efficient fermentation
4. **Central carbon metabolism** - glucose catabolism and cofactor recycling
5. **Stress tolerance genes** - enabling production under harsh conditions

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

Last updated: 2025-12-30

## Genes to Review

- [ ] PDC1 - Pyruvate decarboxylase 1 (primary ethanol pathway)
- [ ] ADH1 - Alcohol dehydrogenase 1 (primary ethanol pathway)
- [ ] ADH2 - Alcohol dehydrogenase 2 (secondary/stress responder)
- [ ] GPD1 - Glycerol-3-phosphate dehydrogenase 1 (byproduct suppression)
- [ ] GPD2 - Glycerol-3-phosphate dehydrogenase 2 (byproduct suppression)
- [ ] HXK1 - Hexokinase 1 (glucose phosphorylation)
- [ ] PFK1 - Phosphofructokinase 1 (glycolytic rate-limiting step)
- [ ] PYC1 - Pyruvate carboxylase (gluconeogenesis/anaplerosis)
- [ ] TDH1 - GAPDH (core glycolytic enzyme)
- [ ] ZWF1 - Glucose-6-phosphate dehydrogenase (pentose phosphate pathway)

## Progress

- Total genes: 10
- Reviewed: 0
- In progress: 0
- Completed: 0

---

# NOTES

## 2025-12-30

- Project initialized
- Selected metabolic engineering & bioproduction as focus area
- Identified 10 candidate genes spanning primary alcohol production, byproduct suppression, and central carbon metabolism
- Ready to begin gene review workflow
