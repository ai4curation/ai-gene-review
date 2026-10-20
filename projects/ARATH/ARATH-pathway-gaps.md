---
title: Arabidopsis pathways not yet curated
species:
- ARATH
---

# Arabidopsis pathways not yet curated

Back to [the Arabidopsis corpus project](../ARATH.md).

**Bottom line:** of 107 Arabidopsis pathways checked, 34 have a module that
contains a reviewed Arabidopsis gene. These are mostly hormone signaling,
flowering, development and immunity. The other 73 are not curated for
Arabidopsis. 35 have no module at all. 21 have only a cross-kingdom module that
never mentions Arabidopsis. 17 have a module that mentions Arabidopsis but holds
none of our reviewed genes. Plant-specific metabolism is the largest gap: seven
of the nine hormone biosynthesis pathways, starch and sucrose,
flavonoids and anthocyanins, cuticle lipids, plastid lipids,
phytosterols, and nitrate and ammonium assimilation.

## Method

- Pathway list: [`ARATH-pathway-map.yaml`](ARATH-pathway-map.yaml) is a
  hand-curated map from 107 pathways to the modules that cover them. The list
  draws on KEGG's 162 *A. thaliana* maps
  ([rest.kegg.jp/list/pathway/ath](https://rest.kegg.jp/list/pathway/ath),
  retrieved 2026-10-19) and adds well-known plant processes that KEGG has no
  map for (cold acclimation, karrikin, UV-B, small-RNA pathways and others).
  Modules were found by searching module titles and then reading each
  module's scope. A module that covers only one step, or another lineage's
  version of the chemistry (for example the bacterial nitrate reductase
  module), is recorded as `related_modules` and does not count as coverage.
- Script: [`scripts/arath_pathway_gaps.py`](scripts/arath_pathway_gaps.py)
  (`uv run python projects/ARATH/scripts/arath_pathway_gaps.py`). It fails if
  a module id, gene folder or KEGG map in the map file does not exist. It
  counts module members with the same rule as `arath_corpus_stats.py`.
- Output: [`ARATH-pathway-gaps.yaml`](ARATH-pathway-gaps.yaml) gives the
  coverage call for each pathway, with module status, Arabidopsis members and
  named genes that sit in no module.

Coverage calls:

| Call | Meaning | Pathways |
|---|---|---|
| `NO_MODULE` | No module covers the pathway | 35 |
| `MODULE_WITHOUT_ARABIDOPSIS` | Module exists but never mentions Arabidopsis | 21 |
| `MODULE_WITHOUT_ARATH_GENES` | Module mentions Arabidopsis, has no reviewed ARATH gene | 17 |
| `MODULE_WITH_ARATH_GENES` | At least one reviewed ARATH gene is a module member | 34 |

Limits. The pathway list is not exhaustive and has not been compared with
AraCyc/PMN. Of the 162 KEGG maps, 69 are assigned to a pathway and 32 are set
aside as overviews or animal/pathogen biology. The other 61 are not assessed;
they are general eukaryotic machinery (ribosome, spliceosome, proteasome, DNA
repair, N-glycosylation) or minor metabolic maps, and the output file lists
them. A `MODULE_WITH_ARATH_GENES` call does not mean the pathway is finished:
every module is still `DRAFT`, and some hold only one or two Arabidopsis genes.

## 1. No module (35)

| Area | Pathways | Reviewed ARATH genes waiting for a module |
|---|---|---|
| Photosynthesis and carbon | Starch synthesis and degradation; sucrose synthesis and degradation | |
| Hormone biosynthesis | Abscisic acid; auxin (TAA/YUCCA); cytokinin; brassinosteroid; jasmonate (oxylipin); ethylene; strigolactone | NCED3 |
| Lipids | Plastid type II fatty acid synthesis; fatty acid desaturation; cutin, suberin and wax; galactolipids; phytosterols (cycloartenol route) | FAD2, CER1 |
| Specialised metabolism | Flavonoids, flavonols and anthocyanins; indolic glucosinolates and their MYB regulation; mono-, sesqui- and triterpenoids | TT8, MYB34, MYB51, MYB122 |
| Nitrogen | Nitrate assimilation; ammonium assimilation (GS/GOGAT) | CHL1 |
| Cofactors and vitamins | Ascorbate (Smirnoff-Wheeler); tocopherol, plastoquinone and phylloquinone; molybdenum cofactor (eukaryotic) | |
| Cell wall and sugars | Pectin, xyloglucan and callose; nucleotide sugar interconversion | |
| Light and hormone signaling | Blue light (cryptochromes, phototropins); UV-B (UVR8); karrikin (KAI2) | UVR8 |
| Abiotic stress | Cold acclimation (ICE1-CBF); drought (DREB2); phosphate starvation; iron deficiency; hypoxia (ERF-VII N-degron) | CBF1 |
| Small RNA | siRNA, tasiRNA and RNA-directed DNA methylation | |
| Organelles | Chloroplast protein import (TOC/TIC); autophagy | |

The last column lists named genes the script found in no module. Other
reviewed genes for these pathways sit in modules built for something else:
CRY1 and CRY2 (photomorphogenesis and photoperiod), RDR6 (miRNA biogenesis),
ICE1 (stomatal lineage) and DREB2A (heat stress).

## 2. Module exists but never mentions Arabidopsis (21)

These modules are generic or cross-kingdom. Arabidopsis representatives could
be added without writing new modules.

- Central metabolism: glycolysis and gluconeogenesis, TCA cycle, pentose
  phosphate pathway, oxidative phosphorylation, inositol phosphates,
  trehalose 6-phosphate
- Amino acids: branched-chain amino acids, histidine, polyamines, glutathione
- Cofactors: MEP/mevalonate isoprenoid precursors, biotin, coenzyme A, NAD,
  riboflavin, vitamin B6
- Lipids: peroxisomal beta-oxidation, phospholipids (CDP-DAG), sphingolipids
- Sulfate assimilation (APS reduction and PAPS activation)
- Peroxisome biogenesis and matrix protein import

## 3. Module mentions Arabidopsis but holds no reviewed ARATH gene (17)

- Photosynthesis: light reactions and antenna, Calvin-Benson-Bassham cycle,
  chlorophyll biosynthesis (all parts of one `photosynthesis` module)
- Cell wall: cellulose, xylan
- Amino acids: shikimate and aromatic amino acids, aspartate family (Thr,
  Met), proline and arginine catabolism, GABA shunt
- Cofactors: thiamine, folate and one-carbon metabolism, siroheme
- Other: glyoxylate cycle, Leloir galactose pathway, alcoholic fermentation,
  ureide catabolism, ER unfolded protein response

## 4. Curated: module with reviewed ARATH genes (34)

These are hormone signaling (auxin, cytokinin, gibberellin, ABA, ethylene,
brassinosteroid, jasmonate, strigolactone, SA/NPR1), light and clock
(phytochrome, circadian), flowering and development (photoperiod,
vernalization, autonomous pathway, floral meristem and organ identity,
CLV-WUS, SHR-SCR, stomata, trichomes), immunity (FLS2/EFR, chitin, NLR), heat
and salt stress, and some metabolism (aliphatic glucosinolates, camalexin,
carotenes, gibberellin biosynthesis, fatty acid elongation, seed oil, lignin),
plus miRNA biogenesis, the LINC complex and photorespiration (the
`photorespiration_c2_cycle` module, with 18 reviewed Arabidopsis members as of
2026-10-20).

The thinnest are lignin (PAL1 only), seed oil (DGAT1 only), NLR immunity (EDS1
and PAD4; RPM1 and RPS2 are reviewed but are not members), the SOS pathway
(two members; HKT1 is reviewed but is not a member) and the carotene module,
which leaves out xanthophylls.

## Suggested order

1. Plant-specific pathways in section 1. No other organism's curation fills
   them, and several already have reviewed genes waiting: ABA biosynthesis
   (NCED3), flavonoids/anthocyanins (TT8), cuticle (CER1), indolic
   glucosinolates (MYB34/51/122), UV-B (UVR8), cold (CBF1).
2. Hormone biosynthesis as a set, so that every signaling module has its
   matching biosynthesis module.
3. Starch and sucrose, together with Arabidopsis reviews for the
   `photosynthesis` module (section 3).
4. Add Arabidopsis representatives to the section 2 modules.
