---
title: "Glycobiology pathway modules"
species: [human]
---

# Glycobiology pathway modules

Index of the `modules/` entries that belong to the
[Glycobiology project](../GLYCOBIOLOGY.md). The **17 core modules** below, plus
`lysosomal_glycogen_degradation`, were curated independently of the project's
[seven exemplar gene reviews](../GLYCOBIOLOGY.md#exemplar-reviews-calibration-set)
and were linked from **no** project page at all; this page wires them in.
`galactose_leloir_pathway` and the non-animal modules in the last section already
belong to other projects and are listed only as cross-references.

The modules supply the axis the exemplar set lacks. The exemplars are
*single-gene* reviews chosen to probe annotation **altitude and pleiotropy**; the
modules are *pathway-level* `ModuleReview` documents that place glycogenes in
ordered biosynthetic and catabolic sequences. Together they reach glycoconjugate classes the exemplars never touch —
GPI anchors, glycosphingolipids, and the lysosomal catabolism of glycolipids and
glycosaminoglycans — rather than only the glycosyltransferase/lectin axes.
**O-glycosylation remains a genuine hole**: no module covers mucin-type
GALNT-initiated O-glycan biosynthesis, and the exemplars reach O-linked biology
only through single genes (POFUT1, B3GALNT2).

**Scope note.** A `ModuleReview` is not a GO-CAM. The decision to **PUNT**
GO-CAM/causal modelling in
[GLYCOBIOLOGY-resource-reuse.md](GLYCOBIOLOGY-resource-reuse.md) is unchanged by
this page; these modules are the repo's own pathway-decomposition format.

## Core animal glycoconjugate modules

All are `status: DRAFT`. "Genes" counts the distinct gene reviews cited as
`file:` evidence by the module.

### N-linked glycosylation

| Module | Genes | What it covers |
|--------|------:|----------------|
| [n_glycan_llo_assembly_cytoplasmic](../../modules/n_glycan_llo_assembly_cytoplasmic.html) | 6 | LLO assembly on the cytoplasmic ER face to Man5GlcNAc2-PP-dolichol (DPAGT1, ALG13/14, ALG1/2/11) |
| [n_glycan_llo_assembly_lumenal](../../modules/n_glycan_llo_assembly_lumenal.html) | 6 | LLO completion on the lumenal face + glucosylation to Glc3Man9GlcNAc2-PP-dolichol (ALG3/9/12, ALG6/8/10) |
| [oligosaccharyltransferase_complex](../../modules/oligosaccharyltransferase_complex.html) | 9 | En-bloc transfer of the glycan to Asn; STT3A/STT3B catalytic subunits + accessory subunits (RPN1/2, DDOST, DAD1, OSTC, MAGT1, TUSC3) |

### Donor and precursor supply

| Module | Genes | What it covers |
|--------|------:|----------------|
| [dolichyl_phosphate_biosynthesis](../../modules/dolichyl_phosphate_biosynthesis.html) | 5 | The Dol-P lipid carrier itself (cis-PT/DHDDS-NUS1 → DOLPP1 → SRD5A3 → DOLK) |
| [dolichol_phosphate_sugar_donor_supply](../../modules/dolichol_phosphate_sugar_donor_supply.html) | 7 | Dol-P-Man / Dol-P-Glc donor formation and flipping (DPM1/2/3, ALG5, MPDU1) |
| [hexosamine_biosynthesis](../../modules/hexosamine_biosynthesis.html) | 6 | Fru-6-P → UDP-GlcNAc, plus the GlcNAc salvage branch (GFPT1/2, GNPNAT1, PGM3, UAP1, NAGK) |
| [sialic_acid_metabolism](../../modules/sialic_acid_metabolism.html) | 7 | Neu5Ac biosynthesis, CMP activation, Golgi import and catabolism (GNE, NANS, NANP, CMAS, SLC35A1, NEU1, NPL) |
| [paps_sulfate_activation](../../modules/paps_sulfate_activation.html) | 4 | PAPS synthesis and Golgi import — the donor for all glycosaminoglycan/glycolipid sulfation (PAPSS1/2, SLC35B2/3) |

### GPI anchors

The five modules decompose `GO:0006505/0006506` into its ordered stages, and
between them cover the PIG/PGAP gene family the project overview names.

| Module | Genes | Stage |
|--------|------:|-------|
| [gpi_anchor_glcnac_transferase](../../modules/gpi_anchor_glcnac_transferase.html) | 6 | I — GPI-GnT complex (PIGA/C/H/P/Q/Y) |
| [gpi_anchor_core_glycan_assembly](../../modules/gpi_anchor_core_glycan_assembly.html) | 6 | II — de-N-acetylation, inositol acylation, mannosylation (PIGL/W/M/X/V/B) |
| [gpi_anchor_ethanolamine_phosphate](../../modules/gpi_anchor_ethanolamine_phosphate.html) | 4 | III — EtNP additions (PIGN/G/F/O) |
| [gpi_anchor_transamidase](../../modules/gpi_anchor_transamidase.html) | 5 | IV — transamidase complex, attachment to protein (PIGK/S/T/U, GPAA1) |
| [gpi_anchor_remodeling](../../modules/gpi_anchor_remodeling.html) | 3 | V — post-attachment lipid remodelling (PGAP1/2/3), i.e. `GO:0120574` |

### Glycolipids and glycan catabolism

| Module | Genes | What it covers |
|--------|------:|----------------|
| [glycosphingolipid_biosynthesis](../../modules/glycosphingolipid_biosynthesis.html) | 10 | Ceramide → GlcCer/GalCer → LacCer → ganglio/globo/lacto series (UGCG, UGT8, B4GALT5/6, ST3GAL5, ST8SIA1, B4GALNT1, B3GALNT1, B3GNT5, A4GALT) |
| [glycosphingolipid_lysosomal_degradation](../../modules/glycosphingolipid_lysosomal_degradation.html) | 7 | The sphingolipidoses (ARSA, GALC, GBA, SMPD1, ASAH1 + the GM2A/PSAP activators) |
| [heparan_sulfate_lysosomal_degradation](../../modules/heparan_sulfate_lysosomal_degradation.html) | 7 | The mucopolysaccharidoses (IDS, IDUA, SGSH, HGSNAT, NAGLU, GNS, GUSB) |
| [keratan_chondroitin_sulfate_lysosomal_degradation](../../modules/keratan_chondroitin_sulfate_lysosomal_degradation.html) | 4 | Morquio / GM2 exolytic cascade (GALNS, GLB1, HEXA, HEXB) |

### Adjacent

Glycan-metabolism modules at the project boundary — included for completeness,
not counted in the core cohort below.

| Module | Genes | Why adjacent |
|--------|------:|--------------|
| [lysosomal_glycogen_degradation](../../modules/lysosomal_glycogen_degradation.html) | 1 | Glycan catabolism, but of a storage polysaccharide rather than a glycoconjugate (GAA; Pompe) |
| [galactose_leloir_pathway](../../modules/galactose_leloir_pathway.html) | 4 | Central carbon metabolism, but regenerates the UDP-galactose that galactosyltransferases spend (GALM, GALK1, GALT, GALE). Already curated under [P_PUTIDA](../P_PUTIDA.md) (`ppu00052`) |

## Non-animal glycan modules (cross-reference)

These are **already owned by other projects** — listed here as cross-references
because they share the project's term landscape, not as glycobiology deliverables.
Bacterial and plant cell-surface glycan synthesis is where CAZy family coverage is
densest, so they are the natural test set for `cazy2go` even though they sit
outside the animal GO-usage audit.

| Module | Owning project | What it covers |
|--------|----------------|----------------|
| [adp_heptose_biosynthesis](../../modules/adp_heptose_biosynthesis.html) | [P_PUTIDA](../P_PUTIDA.md) (`ppu00541`) | ADP-heptose for the LPS inner core (GmhA, HldE, GmhB, HldD) |
| [dtdp_l_rhamnose_biosynthesis](../../modules/dtdp_l_rhamnose_biosynthesis.html) | [P_PUTIDA](../P_PUTIDA.md) (`ppu00523/525`) | dTDP-L-rhamnose, an O-antigen/cell-wall sugar donor (rfbA/C/D, rffG) |
| [peptidoglycan_precursor_biosynthesis](../../modules/peptidoglycan_precursor_biosynthesis.html) | [P_PUTIDA](../P_PUTIDA.md) (`ppu00550`) | Lipid II synthesis and export |
| [peptidoglycan_recycling](../../modules/peptidoglycan_recycling.html) | [P_PUTIDA](../P_PUTIDA.md) (`ppu00520`) | Pseudomonas-type anabolic recycling |
| [glycogen_synthesis_and_mobilization](../../modules/glycogen_synthesis_and_mobilization.html) | [P_PUTIDA](../P_PUTIDA.md) (`ppu00500`) | Bacterial glycogen / α-glucan metabolism (glgA/B/P/X, galU) |
| [cellulose_biosynthesis](../../modules/cellulose_biosynthesis.html) | [PLANT_BIOENERGY](../PLANT_BIOENERGY.md) | Plant cellulose synthase rosette; UDP-glucose → (1→4)-β-D-glucan |

## The module gene cohort — a second, independent verdict baseline

The 17 core modules cite **100 distinct human gene reviews**, all present in
`genes/human/`, with **no overlap at all** with the seven exemplars. That is a
substantially larger reviewed glycogene corpus than the project page previously
claimed, and it gives a second verdict distribution to compare against the
calibration set.

Counts below are computed from the `existing_annotations[].review.action` fields
of the 100 YAMLs (not transcribed from prose), over **2,735 annotations** — every
one adjudicated, none left `PENDING`.

| Cohort | N | ACCEPT | NON_CORE | OVER | MODIFY | REMOVE | NEW |
|--------|--:|-------:|---------:|-----:|-------:|-------:|----:|
| Module genes (100) | 2735 | 1729 (63.2%) | 486 (17.8%) | 422 (15.4%) | 73 (2.7%) | 13 (0.5%) | 12 (0.4%) |
| Exemplars (7) | 303 | 137 (45.2%) | 100 (33.0%) | 42 (13.9%) | 22 (7.3%) | 1 (0.3%) | 1 (0.3%) |

Three things the comparison shows:

- **The project's central claim holds, and holds harder on the larger cohort.**
  REMOVE is 0.5% and 0.3% respectively; ~99.5% of annotations are retained in
  some form. Mis-annotation really is altitude/specificity and pleiotropy rather
  than wrong function, and that is now supported by 3,038 annotations rather
  than 303.
- **The exemplar set is NON_CORE- and MODIFY-skewed by design, and the skew is
  mostly one gene.** LGALS3 alone contributes 62 of the exemplars' 100 NON_CORE.
  The module cohort is dominated by narrow biosynthetic enzymes with little
  pleiotropy, so it lands 18 points higher on ACCEPT. Neither distribution is
  "the" glycogene baseline — the difference between them is a gene-class effect,
  which is worth stating explicitly before the GOA closure query produces a third
  number.
- **The module cohort is under-proposing new terms.** 100 genes yielded **1**
  top-level `proposed_new_terms` entry between them; the 7 exemplars yielded 8.
  (This is a different field from the `NEW` column above, which counts
  annotations proposed against existing GO terms.) A 1-vs-8 split is unlikely to
  be a real difference in GO coverage, and more likely reflects that the
  module-driven reviews were not run with new-term proposal in view. It is a
  concrete re-review target.

**Caveat on `status`.** 97 of the 100 carry `status: INITIALIZED` despite being
fully adjudicated (2 `COMPLETE`, 1 `IN_PROGRESS`). The status field is stale
rather than the reviews being incomplete, but it means the cohort cannot be
selected by status; it is selected here by module citation.
