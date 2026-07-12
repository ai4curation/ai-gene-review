---
title: "Plant Bioenergy Modules"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [ARATH, POPTR, SORBI]
autolink_gene_symbols: false
---

# Plant Bioenergy Modules

## Overview

Plant biomass is the largest renewable feedstock for liquid fuels and
bioproducts. Two broad routes dominate: **lignocellulosic** conversion of
structural cell walls (cellulose + hemicellulose + lignin) to fermentable sugars,
and **oleochemical** use of seed storage oil (triacylglycerol) for biodiesel and
oleochemicals. The central technical barrier for lignocellulose is
**recalcitrance** — the resistance of the wall to enzymatic saccharification —
which is set largely by lignin content/composition, hemicellulose substitution
(especially acetylation), and cellulose crystallinity. For oilseeds the levers are
total oil flux and oil-body packaging capacity.

This project collects the reusable, taxon-neutral biological **modules** that
underlie these use cases. Each module is a recursively decomposable
`ModuleReview` document (see [`modules/README.md`](../modules/README.html)) whose
GO and UniProt identifiers are grounded only where verified; concrete members are
Arabidopsis exemplars for orientation, not species-restricting claims.

## Modules

### Lignocellulosic cell wall (recalcitrance targets)

- [**Cellulose biosynthesis**](../modules/cellulose_biosynthesis.html)
  — UDP-glucose supply, glucan polymerization by the primary/secondary cellulose
  synthase complexes (CESA rosettes), microtubule guidance, and accessory factors
  (KORRIGAN, COBRA). Cellulose crystallinity and the secondary-wall CESA set are
  primary digestibility determinants.
  Source: [`modules/cellulose_biosynthesis.yaml`](../modules/cellulose_biosynthesis.yaml).

- [**Lignin (monolignol) biosynthesis**](../modules/lignin_monolignol_biosynthesis.html)
  — the general phenylpropanoid entry (PAL/C4H/4CL), the monolignol-specific
  grid (HCT, C3'H, CCoAOMT, CCR, F5H, COMT, CAD), monolignol export, and
  laccase/peroxidase radical coupling into H/G/S lignin. Monolignol flux and the
  **S/G ratio** are the dominant recalcitrance-engineering levers.
  Source: [`modules/lignin_monolignol_biosynthesis.yaml`](../modules/lignin_monolignol_biosynthesis.yaml).

- [**Xylan (glucuronoxylan) biosynthesis**](../modules/xylan_biosynthesis.html)
  — Golgi backbone elongation (IRX9/IRX10/IRX14), the eudicot reducing-end
  sequence, glucuronosyl substitution (GUX), 4-O-methylation (GXM), and
  O-acetylation (ESK1/TBL29 + RWA). Xylan acetylation and quantity drive both
  recalcitrance and acetate-mediated fermentation inhibition.
  Source: [`modules/xylan_biosynthesis.yaml`](../modules/xylan_biosynthesis.yaml).

### Storage oil (biodiesel / oleochemical feedstock)

- [**Seed triacylglycerol (oil) biosynthesis**](../modules/seed_triacylglycerol_biosynthesis.html)
  — the ER glycerol-phosphate (Kennedy) pathway (GPAT → LPAAT → PAP → DGAT),
  the acyl-CoA-independent PDAT route, and oleosin-mediated oil-body packaging.
  DGAT/PDAT capacity, the acyl-CoA pool, and oleosin dosage set seed-oil yield.
  Source: [`modules/seed_triacylglycerol_biosynthesis.yaml`](../modules/seed_triacylglycerol_biosynthesis.yaml).

### Upstream carbon supply

- [**Photosynthesis**](../modules/photosynthesis.html) — the light reactions and
  Calvin–Benson–Bassham carbon fixation that ultimately supply the carbon
  skeletons feeding all of the above.
  Source: [`modules/photosynthesis.yaml`](../modules/photosynthesis.yaml).

## Why these modules for bioenergy

| Use case | Module(s) | Principal engineering lever |
|----------|-----------|-----------------------------|
| Lignocellulosic ethanol / sugars | lignin, xylan, cellulose | lower lignin, raise S/G, reduce xylan acetylation, alter crystallinity |
| Fermentation inhibitor reduction | xylan | reduce backbone O-acetylation (acetate) |
| Biodiesel / oleochemicals | seed TAG | increase DGAT/PDAT flux and oil-body capacity |
| Feedstock productivity | photosynthesis | carbon assimilation upstream of wall and oil |

## Relevant bioenergy species in this repo

The modules are written taxon-neutrally with Arabidopsis exemplars, but the repo
also contains relevant feedstock species directories, including poplar
(**POPTR**), sorghum (**SORBI**), maize (**MAIZE**), *Brachypodium* (**BRADI**),
rice (**ORYSJ**/**ORYSI**), soybean (**SOYBN**), and *Chlamydomonas* (**CHLRE**).
Grass-specific wall features (mixed-linkage glucan, glucuronoarabinoxylan
arabinosylation, wall-bound ferulate/coumarate esters) are noted in the module
documents and are candidates for future dedicated modules.

## Status / next steps

- [x] Structured modules curated and validated against `ModuleReview`
      (lignin, xylan, seed TAG; cellulose and photosynthesis pre-existing).
- [ ] Grass-specific modules: mixed-linkage glucan (CSLF/CSLH) and
      glucuronoarabinoxylan arabinosylation/feruloylation.
- [ ] Suberin and cutin biosynthesis (barrier polyesters relevant to some
      feedstocks and to pretreatment).
- [ ] Per-gene reviews for feedstock-species orthologs (poplar/sorghum) of the
      exemplar enzymes above.
