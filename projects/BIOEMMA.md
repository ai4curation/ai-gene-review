---
title: "BioEMMA Evaluation"
maturity: SCOPING
tags: [PIPELINE, EVALUATION]
species: [PSEPK, ECOLI]
autolink_gene_symbols: false
sidecars:
  eval_script: BIOEMMA/bioemma_eval.py
  recall_script: BIOEMMA/subsystem_recall.py
  ppu_map_summary: BIOEMMA/results/iJN1463_map_summary.tsv
  ppu_retained_reactions: BIOEMMA/results/iJN1463_retained_reactions.tsv
  ppu_gpr_review_coverage: BIOEMMA/results/iJN1463_gpr_review_coverage.tsv
  ppu_subsystem_recall: BIOEMMA/results/iJN1463_subsystem_recall.tsv
  ecoli_core_map_summary: BIOEMMA/results/e_coli_core_map_summary.tsv
  example_escher_map: BIOEMMA/results/iJN1463_rn00220_escher_map.json
---

# BioEMMA Evaluation

Hands-on assessment of **BioEMMA** (BioUML Escher Metabolic Maps Assistant), a
Python tool that turns a KEGG pathway map (KGML) plus a genome-scale metabolic
model (SBML) into a model-specific, editable Escher map with an optional flux
balance analysis (FBA) overlay.

- Paper: Kachnov VA, Esembaeva MA, Melikhova EV, Kulyashov MA. *BioEMMA:
  Automated Generation of Model-Specific Escher-Compatible Maps from KEGG
  Pathways.* Biology 2026, 15, 1493.
  [DOI:10.3390/biology15171493](https://doi.org/10.3390/biology15171493)
  (published 2026-09-02; no PubMed id yet as of 2026-09-07).
- Code: [KAVladD/BioEMMA](https://github.com/KAVladD/BioEMMA) (MIT), PyPI
  `bioemma`; results repo
  [mishakula-group/BioEMMA_article](https://github.com/mishakula-group/BioEMMA_article).
- Version tested here: **0.4.3** (git checkout, same version as the paper's Table 1).

## Bottom line

- **It works, offline, in seconds, and it is honest.** The bundled reference
  case (e_coli_core on KEGG map00010) runs without network access; a full
  genome-scale model (*P. putida* KT2440 iJN1463, 2927 reactions) is projected
  onto 17 KEGG maps in well under a minute. Across 15 (map, model-subsystem)
  pairs on the two models we found **no case where BioEMMA dropped a model reaction whose KEGG
  cross-reference is actually drawn on the map**, other than duplicated model
  reactions (`_copy1`/`_copy2`) of which it keeps exactly one.
- **The dominant failure mode is KEGG granularity, not the tool.** Reactions
  missing from a generated map are overwhelmingly ones whose KEGG id in the
  model is *not on that map*: KEGG draws the pyruvate and 2-oxoglutarate
  dehydrogenase complexes as lipoamide half-reactions (R02569, R07618, R08549)
  while models carry the lumped reaction (R00209); KEGG's stereo-split
  glucose-6-phosphate isomerase (R13199) does not match the model's PGI; and
  model subsystems are broader than any one KEGG map. A blank spot on a
  BioEMMA map therefore means "no identifier bridge", not "absent from the
  model" (the paper says this too, Section 4).
- **Organism-specific KGML maps are useless as input.** Our modules cite KEGG
  maps as `KEGG:ppu00220` etc. Those organism maps contain gene entries, not
  reaction entries; fed to BioEMMA they yield 0 reactions. Use the reference
  `rnNNNNN` map of the same number, which has the identical layout.
- **Two implementation issues worth reporting upstream.** (1) When a model
  duplicates a reaction (`PRAMPC_copy1`, `PRAMPC_copy2`), BioEMMA labels the
  Escher reaction with the BiGG annotation (`PRAMPC`) but keys `fluxes.json`
  by the model id, so the flux overlay silently misses those reactions (10 of
  295 retained reactions in our P. putida run, 3 of 15 on the histidine map).
  (2) Retention on the paper's own reference case differs from the paper (12
  reactions here vs 16 reported) because the shipped MetaNetX table has
  changed; the paper's headline "GAPD unmapped" limitation is already fixed
  in 0.4.3 (GAPD is retained), which shows how version-dependent these maps are.
- **Fit for this repo: a pathway-level "what does the model say" lens, not a
  GO evidence source.** BioEMMA produces no gene-level assertion of its own.
  Its value here is the gene-protein-reaction (GPR) bridge: every retained
  reaction carries the model's genes, and joining those on UniProt
  ordered-locus names finds that 186 of the 292 iJN1463 genes on the 17 maps
  already have reviews under `genes/PSEPK/`. That gives a cheap, pathway-shaped
  worklist and a way to colour an Escher map by review status.

## What BioEMMA does (from the paper and the code)

1. Parse a KEGG KGML file: compound entries become primary metabolite nodes with
   their KEGG coordinates; reaction entries keep substrates, products,
   reversibility and position.
2. Translate KEGG compound/reaction ids to BiGG or ModelSEED through bundled
   MetaNetX (MNXref 4.5) cross-reference tables. An EC-number fallback exists
   but is off by default and the authors recommend manual review if it is on.
3. Build Escher nodes (metabolite, midmarker, two multimarkers per reaction) and
   segments from the KGML geometry; non-primary metabolites (ATP, H2O, cofactors)
   are pulled from the model and placed heuristically.
4. Filter to the reactions and metabolites present in the input SBML model by
   BiGG id, then KEGG id, then SEED id (scores 100/90/80); with fallback on,
   MetaCyc, Rhea, EC-derived ids and bare EC numbers are tried (70 down to 10).
   If several KEGG entries hit the same model reaction only the best is kept.
5. Optionally run FBA with COBRApy and export `fluxes.json`; with the `escher`
   package installed, write an interactive HTML map.
6. Merge several maps into a grid; wrap the whole thing in a BioUML/WDL pipeline
   (fastp, SPAdes, Prokka, gapseq/ModelSEEDpy/Reconstructor/Bactabolize, MEMOTE,
   BioEMMA) for reconstruct-and-compare workflows.

The paper's evaluation compares three automated *E. coli* reconstructions on
three central-carbon maps (Table 2 there: gapseq retained 60 to 81% of mappable
reactions, ModelSEEDpy 38 to 52%), 87 prokaryotic BiGG models, a methanogen
(iAF692, map00680) and three eukaryotic models with compartment filtering.

## Our evaluation

Everything below is regenerated by two scripts in [`BIOEMMA/`](BIOEMMA/):
[`bioemma_eval.py`](BIOEMMA/bioemma_eval.py) (fetch KGML + model, run BioEMMA
with FBA, write per-map and per-reaction tables, join genes to reviews) and
[`subsystem_recall.py`](BIOEMMA/subsystem_recall.py) (recall against the BiGG
model's own subsystem assignment). Outputs live in
[`BIOEMMA/results/`](BIOEMMA/results/). Nothing is hard-coded; the first run
needs the KEGG REST API and BiGG.

### 1. Reference case: e_coli_core on glycolysis, TCA, pentose phosphate

| map | KEGG reactions | mapped to BiGG | retained | non-zero FBA flux | model subsystem recall |
|---|---|---|---|---|---|
| rn00010 glycolysis/gluconeogenesis | 56 | 46 | 12 | 8 | 10/12 (83%) |
| rn00020 citrate cycle | 29 | 28 | 7 | 6 | 6/8 (75%) |
| rn00030 pentose phosphate | 58 | 44 | 7 | 6 | 4/8 (50%) |

Every model reaction not retained falls into one of two classes
([`e_coli_core_subsystem_dropped.tsv`](BIOEMMA/results/e_coli_core_subsystem_dropped.tsv)):

- **KEGG xref not drawn on the map** (6): PDH (model R00209; the map draws the
  E1/E2/E3 half-reactions R00014/R03270/R02569), AKGDH (model R08549; map
  draws R00621/R02570), ICDHyr (model R00267, the lumped NADP reaction; the
  map draws the NAD form R00709 and the oxalosuccinate two-step
  R01899/R00268), TALA (R01827 absent), TKT2 (model R01830; map draws R01641)
  and G6PDH2r (model R00835; map draws the lactone form R02736).
- **No `kegg.reaction` annotation in the model** (2): PGI and TKT1. For PGI the
  map's isomerase is the stereo-specific R13199, whose MetaNetX BiGG partner is
  `PGI1`, not `PGI`, so neither identifier route fires.

None is a wrong retention. The paper reports 16 retained reactions for this
case and flags GAPD as an unmapped element; with the mapping table shipped in
0.4.3 GAPD is retained and 12 reactions survive, i.e. the shipped
cross-reference table, not the algorithm, decides the map.

### 2. *P. putida* KT2440 iJN1463 on the 17 reference maps cited by our modules

Our `modules/*.yaml` documents cite KEGG maps as sources for 30 modules, mostly
`ppu` maps from the [P. putida module program](P_PUTIDA/P_PUTIDA_MODULE_PLAN.md).
We projected iJN1463 (BiGG; 2927 reactions, 1462 genes; KEGG xrefs on 702
reactions, BiGG ids on all) onto the reference versions of those maps
([`iJN1463_map_summary.tsv`](BIOEMMA/results/iJN1463_map_summary.tsv)).

| map | module(s) citing it | KEGG rxns | retained | % | flux ≠ 0 |
|---|---|---|---|---|---|
| rn00010 | (glycolysis, background) | 56 | 15 | 27 | 7 |
| rn00020 | (TCA, background) | 29 | 8 | 28 | 6 |
| rn00030 | pentose_phosphate_pathway | 58 | 18 | 31 | 9 |
| rn00220 | arginine_biosynthesis | 33 | 17 | 52 | 11 |
| rn00250 | (Ala/Asp/Glu, background) | 47 | 23 | 49 | 11 |
| rn00260 | (Gly/Ser/Thr, background) | 76 | 31 | 41 | 14 |
| rn00270 | methionine_biosynthesis, bacterial_methionine_cycle | 101 | 27 | 27 | 11 |
| rn00290 | branched_chain_amino_acid_biosynthesis | 25 | 15 | 60 | 12 |
| rn00300 | lysine_biosynthesis | 37 | 11 | 30 | 10 |
| rn00340 | histidine_biosynthesis | 45 | 15 | 33 | 6 |
| rn00361 | catechol_ortho_cleavage | 74 | 0 | 0 | 0 |
| rn00362 | catechol_ortho_cleavage | 96 | 19 | 20 | 1 |
| rn00620 | (pyruvate, background) | 85 | 23 | 27 | 8 |
| rn00630 | glycolate_glyoxylate_assimilation | 89 | 28 | 31 | 12 |
| rn00670 | folate_one_carbon_interconversion | 51 | 21 | 41 | 11 |
| rn00770 | coenzyme_a_biosynthesis | 34 | 15 | 44 | 13 |
| rn00780 | biotin_biosynthesis | 27 | 9 | 33 | 9 |

Readings:

- **Retention fractions of 20 to 60% are normal and mostly reflect KEGG's
  breadth**, not model holes: a KEGG reference map draws every organism's
  variant. Recall against the model's *own* subsystem assignment is the fairer
  number ([`iJN1463_subsystem_recall.tsv`](BIOEMMA/results/iJN1463_subsystem_recall.tsv)):
  91% for glyoxylate metabolism, 90% for pantothenate/CoA, 79% methionine, 73%
  Gly/Ser/Thr, 65% histidine, 60% biotin, but only 14% for the arginine *and
  proline* subsystem (proline lives on map00330, which we did not project) and
  35 to 40% for glycolysis and TCA (model subsystems include gluconeogenic,
  anaplerotic and duplicated reactions that KEGG draws elsewhere).
- **rn00361 is a true zero and a useful one.** The `catechol_ortho_cleavage`
  module cites `ppu00361` (chlorocyclohexane/chlorobenzene degradation). None
  of that map's reactions has a KEGG xref in iJN1463 and only 11 of 74 have any
  BiGG partner. The unsubstituted catechol branch (CATDOX R00817, MUCCY, MUCLI,
  OXOAEL, 3OADPCOAT) is drawn on **map00362** and is retained there. The module
  source citation should point at map00362 (or a KEGG module such as M00568)
  rather than 00361; rn00361 adds nothing for KT2440.
- **The flux overlay tells a growth-condition story, not a function story.**
  On the benzoate map only ACALD carries flux because glucose, not benzoate, is
  the carbon source in the default medium; on the arginine map the acetylated
  ornithine route (ACGS argA → ACGK argB → AGPR argC1/argC2 → ACOTA argD →
  ACODA argE/argJ → OCBT → ARGSS argG → ARGSL argH) carries 0.23 mmol/gDW/h of
  biosynthetic flux while the catabolic ARGDr/ARGDI are at zero. That is
  exactly the variant structure the
  [`arginine_biosynthesis`](../modules/arginine_biosynthesis.html) module
  encodes (dedicated ArgA vs bifunctional ArgJ initiation), and the model's
  `ACODA: argE or argJ` GPR agrees with it.

### 3. The GPR bridge to gene reviews

For each retained reaction `bioemma_eval.py` records the model's GPR and joins
its genes on the `OrderedLocusNames` in `genes/PSEPK/*/*-uniprot.txt`
([`iJN1463_gpr_review_coverage.tsv`](BIOEMMA/results/iJN1463_gpr_review_coverage.tsv)):

| map | genes on retained reactions | with a review | |
|---|---|---|---|
| rn00020 TCA | 12 | 11 | 92% |
| rn00340 histidine | 15 | 13 | 87% |
| rn00770 CoA | 20 | 17 | 85% |
| rn00030 PPP | 19 | 16 | 84% |
| rn00780 biotin | 6 | 5 | 83% |
| rn00010 glycolysis | 23 | 18 | 78% |
| rn00620 pyruvate | 35 | 26 | 74% |
| rn00300 lysine | 14 | 10 | 71% |
| rn00290 BCAA | 15 | 10 | 67% |
| rn00670 folate C1 | 29 | 19 | 66% |
| rn00362 benzoate | 33 | 19 | 58% |
| rn00630 glyoxylate | 48 | 26 | 54% |
| rn00220 arginine | 21 | 11 | 52% |
| rn00270 Cys/Met | 31 | 15 | 48% |
| rn00250 Ala/Asp/Glu | 31 | 12 | 39% |
| rn00260 Gly/Ser/Thr | 38 | 12 | 32% |
| **all 17 maps** | **292** | **186** | **64%** |

On the arginine map every enzyme of the biosynthetic route proper is reviewed
(argA, argB, argC1, argC2, argD, argE, argJ, argG, argH, gdhA, tyrB); the
unreviewed genes are the carbamoyl-phosphate, transaminase, glutaminase and
catabolic edges (PP_0999, PP_1000, PP_1001, PP_4723/4724, PP_2453, PP_2080,
PP_3721, PP_0817/1872). That is a sensible next batch for the P. putida module
program, and the same table gives one for every other map.

## Assessment

**Strengths.**

- Deterministic, reproducible, scriptable; no web UI required; KGML and SBML
  in, JSON out. Runs on a bundled test model with no network.
- Preserves the curated KEGG layout, so several models (or one model under
  several media) can be compared *in place*. This is the paper's central claim
  and it holds.
- Conservative identifier matching by default (direct MNXref links only), with
  fallback layers clearly marked in the output tables.
- Output is standard Escher JSON that a curator can open, edit and re-export.

**Limitations relevant to us.**

- No gene-level inference: the map inherits the model's GPRs and nothing else.
  It cannot tell us whether an annotation is right, only whether a
  reconstruction contains a reaction and whether FBA uses it under one medium.
- Everything hinges on MNXref cross-reference coverage and KEGG's reaction
  granularity (half-reactions, stereo-split isomerases, lumped complexes).
  Absence on the map is not absence from the model; the paper says so, and our
  drop classification quantifies it.
- Organism KGML maps (the ones our modules cite) are silently non-functional
  input; only reference `rn`/`map` KGML has reaction entries.
- Flux overlay keys can miss duplicated model reactions (bug noted above).
- HTML export needs the `escher` Python package (not tested here).
- Layout quality is "KEGG-shaped": non-primary metabolites are placed by
  heuristic and dense regions need hand editing, as the paper acknowledges.

**Verdict.** Useful, narrow, and trustworthy for what it claims. For this
project it is best used as (a) a visual QC lens on a module's KEGG scope
versus a model's content, (b) a GPR-derived worklist generator, and (c) a
comparison surface when we hold several reconstructions of the same organism
(the METABOLIC_MODEL_ANALYSIS iRP911 work would be a natural second target).
It is not an evidence source for GO annotations and should not be cited as one.

## Possible follow-ups

- [ ] Render the BioEMMA maps with review status: colour each retained
      reaction by whether all of its GPR genes have a complete review
      (Escher `reaction_data` accepts any numeric layer).
- [ ] Fix the `catechol_ortho_cleavage` module source to cite map00362 /
      M00568 instead of ppu00361.
- [ ] Project the *M. extorquens* iRP911 model used in
      [METABOLIC_MODEL_ANALYSIS](METABOLIC_MODEL_ANALYSIS.md) onto map00680 (C1
      metabolism) and map00630 to see the serine cycle in place.
- [ ] Report the duplicate-reaction flux-key issue and the ppu-map behaviour
      to the BioEMMA authors.
- [ ] Batch the unreviewed GPR genes from `iJN1463_gpr_review_coverage.tsv`
      into the P. putida module worklists.

---

# STATUS

- [x] Read the paper (DOI:10.3390/biology15171493) and the 0.4.3 source
- [x] Reproduce the bundled e_coli_core reference case offline
- [x] Project iJN1463 onto the 17 reference maps cited by our modules, with FBA
- [x] Classify dropped reactions against BiGG subsystems
- [x] Join retained-reaction GPRs to `genes/PSEPK` reviews
- [ ] Follow-ups listed above

# NOTES

## 2026-09-07

Initial evaluation. BioEMMA 0.4.3 installed from a git checkout with
`cobra 0.32.1`; the KGML maps were fetched from `rest.kegg.jp` and iJN1463 /
e_coli_core from BiGG (SBML for BioEMMA, JSON for the subsystem field, which
the SBML export lacks). The 17 maps plus FBA took about a minute. The
ppu00220 organism KGML gave 24 metabolites and 0 reactions, which is what led
to the `rn` recommendation. All numbers in this page come from the TSVs in
`BIOEMMA/results/`; rerun the two scripts to regenerate them.
