---
title: "FUNG-GROWTH carbon-source phenotypes as a check on fungal GO annotations"
description: >-
  Harvests the FUNG-GROWTH plate-growth matrix (398 fungal strains x 35 carbon
  sources) and extracts decisive no-growth ("killer") phenotypes that can
  corroborate or contradict GO annotations to carbohydrate catabolism and
  uptake in reviewed fungal species.
autolink_gene_symbols: false
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [SCHPO, yeast, CANAL, NEUCR, EMENI, ASPNG, ASPOR, HYPJE, MYCMD, PENCH, PYROR]
manifest:
  artifacts:
    - href: https://claude.ai/artifact/GsyMpPX1wW2DxpyurEA5Ka
      title: Project brief
---

# FUNG-GROWTH carbon-source phenotypes

**Bottom line:** [FUNG-GROWTH](https://www.fung-growth.org/) (Westerdijk
Institute; de Vries et al. 2025, PMID:40767478) records plate growth of 398
fungal strains on 35 carbon sources, from monosaccharides to crude plant
biomass, each scored 0–10 next to a no-carbon control plate. We downloaded the
whole matrix through the site's public JSON service and called "killer"
phenotypes: a strain grows no better than on its no-carbon plate, on a
substrate that comparable fungi use. A killer phenotype is a sharp,
falsifiable organism-level claim. It says the strain has no working route to
use that carbon source, which bears directly on GO annotations to
carbohydrate catabolic processes, CAZyme activities and sugar transporters.
The first pass finds 299 killer calls across 153 strains, 5 of them in species
with gene reviews here. One already agrees with a curation decision:
*S. pombe* barely grows on starch, consistent with removing
`carbohydrate catabolic process` from the alpha-amylase homologue aah1. Status:
SCOPING. The data and scripts are in place, but no annotation has yet been
changed on the strength of these phenotypes.

## Data

| Item | Value |
|---|---|
| Source | https://www.fung-growth.org/ (BioloMICS site 87, table `14682616000000025`) |
| Citation | de Vries RP *et al.* 2025. The FUNG-GROWTH database: linking fungal phenotype to genome. *Microbiol Resour Announc* 14:9. PMID:40767478 |
| Strains | 398 (277 species), 393 with a no-carbon control; includes 2 *A. niger* deletion mutants (ΔnoxR, ΔracA) |
| Carbon sources | 35 plus no-carbon control. Arabinogalactan is never scored; oat spelt xylan, lignin and sugar beet pulp are scored for only 82–152 strains |
| Per cell | growth rating (0–10), colony growth curve (day:measurement), plate photo, sporulation (almost never filled) |
| Per strain | JGI MycoCosm genome link, CAZy genome link, genome publication, incubation temperature |

Files (regenerate with `python projects/FUNG_GROWTH/fetch_fung_growth.py`):

- `FUNG_GROWTH/data/fung_growth_matrix.tsv`: strain × carbon source growth rating
- `FUNG_GROWTH/data/fung_growth_ratings.tsv`: long format with growth curves
- `FUNG_GROWTH/data/fung_growth_strains.tsv`: strain metadata (genome, CAZy, PMID, temperature)
- `FUNG_GROWTH/data/fung_growth_fields.tsv`: source field dictionary

## Calling killer phenotypes

`python projects/FUNG_GROWTH/killer_phenotypes.py` makes every call relative
to the strain's own no-carbon plate, because many fungi form thin colonies on
agar alone (*S. cerevisiae* S288C scores 2 and *U. maydis* 4 without any
added carbon):

- `delta = rating − no-carbon rating`; NO_GROWTH ≤ 0, WEAK 1–2, GROWTH ≥ 3.
- A NO_GROWTH cell is a **killer** if comparable fungi do grow:
  - *database* basis: ≥ 75% of all rated strains GROW (13 carbon sources qualify);
  - *genus* basis: ≥ 50% of at least 3 other strains of the same genus GROW.

Outputs: `FUNG_GROWTH/data/killer_phenotypes.tsv` (299 calls: 112 database,
145 genus, 42 both) and `FUNG_GROWTH/data/carbon_source_summary.tsv`. The
substrates with the most killer calls are casein (35), cellobiose (30), apple
pectin (23), soluble starch (17) and D-mannose (16).

The carbon-source summary also shows which plates carry little information.
Crystalline cellulose (7% of strains GROW), D-glucuronic acid (13%) and
D-galacturonic acid (22%) are poor plate substrates for most fungi. A
no-growth call on them says little about the gene content, so these
substrates are excluded from the database basis.

## Species with gene reviews in this repository

| Strain | Repo dir | No-carbon | Killer phenotypes |
|---|---|---|---|
| *Schizosaccharomyces pombe* 972h- | SCHPO | 0 | alfalfa meal, apple pectin, cellobiose |
| *Saccharomyces cerevisiae* S288C | yeast | 2 | apple pectin, cellobiose |
| *Candida albicans* SC5314 | CANAL | 1 | cellobiose |
| *Ustilago maydis* | MYCMD | 4 | cellobiose, citrus pectin, soluble starch, sugar beet pulp |
| *Penicillium rubens* Wisconsin 54-1255 | PENCH | 0 | birchwood xylan |
| *Neurospora crassa* OR74A, *Aspergillus nidulans* FGSC A4, *A. niger* CBS 513.88, *A. oryzae* RIB40, *Trichoderma reesei*, *Pyricularia oryzae* Guy11 | NEUCR, EMENI, ASPNG, ASPOR, HYPJE, PYROR | 0 | none |

Other informative cells that do not meet either killer rule:

- *S. pombe* scores 0 on D-galactose, D-xylose, L-arabinose and lactose, but
  sucrose 4, raffinose 3 and maltose 3. This is the expected profile of a
  fission yeast with invertase and maltase but no Leloir or pentose pathway
  in use. Soluble starch scores 1 (WEAK), consistent with
  `genes/SCHPO/aah1` where `GO:0016052 carbohydrate catabolic process` (IEA)
  is marked REMOVE: Aah1 is a cell-wall transglycosylase and no
  starch-degrading activity is detected.
- *A. niger* scores 0 on D-galactose in all nine strains. This matches the
  reported failure of *A. niger* conidia to germinate on galactose (to be
  cited before use). It is a
  germination and uptake phenotype, not proof that Leloir enzymes are absent,
  so it should not be used to argue against galactokinase or epimerase
  annotations.
- *T. reesei*, the source of `genes/HYPJE/cbh1`, scores only 2 on
  crystalline cellulose. The plate assay does not resolve cellulolytic
  capacity, so it cannot be used to check the cbh1 cellulose annotations.
- The *A. niger* ΔnoxR and ΔracA mutants score 0 on oat spelt xylan while the
  N402 parent scores 5; beechwood and birchwood xylan are unaffected. This is
  the only mutant phenotype in the database. It is a single plate and has not
  been checked against the source publication.

## How to use this in reviews

- Treat a killer phenotype as organism-level evidence: it supports a
  REMOVE or MARK_AS_OVER_ANNOTATED only for an annotation that implies the
  organism *uses* that carbon source (catabolic process, uptake). It says
  nothing about an enzyme that has another role (aah1 is the model case).
- Do not use plate growth to propose `NEW` process annotations. Growth on a
  substrate shows that some gene product does the work, not which one.
- Check the growth curve and photo (in `fung_growth_ratings.tsv` and on the
  site) before citing a single 0–10 rating. The colour-coded rating is
  semi-quantitative, and yeast and filamentous ratings are not on comparable
  colony scales.

## GOA join

Full write-up: [killer calls joined to GOA](FUNG_GROWTH/GOA_JOIN.md).

- `FUNG_GROWTH/build_go_map.py` maps 25 plates to 16 GO catabolic-process
  terms and 13 substrate-specific activity terms. It writes only labels;
  every id is resolved in OLS4 by exact label and checked to be current and
  in the right namespace (`data/carbon_source_go_map.tsv`,
  `data/carbon_source_go_activity_map.tsv`).
- `FUNG_GROWTH/goa_join.py` pulls 1,865 QuickGO annotations to those terms
  for the 11 species and flags 60 rows (29 gene products, 40 IEA) where the
  plate is a killer call (`data/goa_killer_flags.tsv`).
- `cellobiose catabolic process` is unused in all 11 species, and
  `starch catabolic process` is unused in *U. maydis*, so the target pairs
  meet GO through hydrolase activities instead.
- *S. cerevisiae* has no cellobiose-implying annotation, which agrees with
  its plate. The clearest review candidate is two *C. albicans* GH3
  β-glucosidases (BGL22, CAALFM_C301820WA) with IEA `cellulose catabolic
  process` from a UniPathway mapping.
- Three flag sets (*P. rubens* birchwood xylan, *U. maydis* citrus pectin,
  *S. cerevisiae* apple pectin) rest on plates contradicted by a sister plate
  of the same polymer and should be discounted.

## Next steps

- Review the *C. albicans* BGL22 and CAALFM_C301820WA cellulose-catabolism
  rows as gene reviews, after checking the literature on cellobiose
  assimilation.
- Require agreement across sister plates (pectin ×2, xylan ×3) before
  calling a killer phenotype.
- Read the *U. maydis* growth curves before using its calls: its no-carbon
  score of 4 leaves little room on the 0–10 scale.
- Ask the FUNG-GROWTH curators whether ratings of 0 on a 0-baseline plate
  are true zero growth or unscored cells, and source the ΔnoxR/ΔracA plates.
