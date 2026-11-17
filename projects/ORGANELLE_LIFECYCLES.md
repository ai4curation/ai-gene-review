---
title: "Organelle Lifecycle Modules"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
autolink_exclude: [ftsZ, FtsZ]
---

# Organelle Lifecycle Modules

**Bottom line:** one lifecycle module per membrane-bounded organelle, across all
eukaryotes. Each one composes existing modules by reference
(`module_ref`), and each is written so it can be evaluated as a
satisfiability rule when annotating a new genome. The first pilot is
`MODULE:mitochondrion_lifecycle`, whose required stages are the
eukaryote-wide `MODULE:mitochondrial_protein_import` and
`MODULE:mitochondrial_iron_sulfur_cluster_assembly`.

## Scope

- **Membrane-bounded organelles only.** Condensates, P granules and other
  membraneless bodies are out of scope; so are centrioles. The cilium stays in,
  as a membrane-bounded projection.
- **All eukaryotes.** Each module's taxon context is Eukaryota. Lineage
  differences are modelled as `variant_sets` (different machinery for the same
  stage) or as `optional` parts (a stage some lineages lack). The exception is
  an organelle confined to one lineage (the plastid and the plant vacuole):
  its umbrella and rule modules take that clade, or the narrower clade their
  grounding supports, as their context, and their required parts assert "every
  member of the clade has this". An organelle scattered across lineages
  (the acidocalcisome) keeps the Eukaryota context, and its rule says in its
  notes which lineages it is meant for; failures outside them are expected.
- **Rules, not compendia.** A non-optional part asserts "every eukaryote with
  this organelle has this". That is a stronger claim than a descriptive pathway
  module makes, and it is what lets the satisfiability engine
  (`ai_gene_review.module_logic`) find gaps in a new genome. Clade-specific
  compendia of the same stage (for example the Drosophila
  `dmel_mitochondrial_protein_import`) are legitimate descriptive modules. An
  umbrella may reference such clade-specific or accession-grounded modules only
  as `optional` parts, named as such in its notes, so that no required part
  depends on them.

## Stage skeleton

Every lifecycle umbrella uses the same part roles, in this order:

| Order | Role | Typical content |
|---|---|---|
| 1 | biogenesis and protein supply | de novo formation, growth by import, membrane protein insertion, lipid supply |
| 2 | division | fission machinery |
| 3 | fusion | homotypic fusion |
| 4 | function | references to the metabolic and transport modules the organelle hosts |
| 5 | quality control | stress responses, resident proteases, repair |
| 6 | turnover | selective autophagy, programmed elimination |

An umbrella part's `order` is the stage's number in this table, not its position
among the parts the umbrella happens to have: an umbrella with only biogenesis and
function parts numbers them 1 and 4, and parts of the same stage share a number.

The skeleton is a naming convention. It is not a `conforms_to` template,
because conformance compares molecular-function terms tier by tier with exact
matching, and lifecycle stages are processes.

## Design rules

1. **One home per annoton.** An umbrella stage is a `module_ref` to the module
   that owns the machinery; it never copies annotons.
2. **Function is referenced, never owned.** The function stage points at
   metabolic modules and is optional unless every lineage keeps that function.
   Proteins that only work *in* the organelle are not part of building it.
3. **Disassembly has three meanings, modelled separately:** turnover by
   selective autophagy (one shared receptor-to-Atg8 module plus organelle-specific
   receptors), reversible mitotic disassembly (nuclear envelope, Golgi), and
   programmed developmental elimination.
4. **A stage is required only when its referenced module is rule-shaped.** That
   means `RULE_READY`, or `RULE_CANDIDATE` with its lineage exceptions named in
   the module (`coverage.yaml` defines both). Genomes from a named exception
   lineage are then reported as gaps, which the engine's abduction step flags
   for explanation rather than treating as absence. Clade-scoped `DESCRIPTIVE`
   modules are linked as optional, so they are visible but cannot produce false
   negatives.

## Two-layer model

A rule makes two kinds of claim: a process step requires a molecular function
(close to binary), and that function is carried out by one of several
families, domains or complexes (open-world and gappy). Variant sets record
which layer they belong to (`variant_kind`, inferred as `REALIZER` when every
variant carries the same function), and the engine reports each gap at its
innermost failing step, labelled by layer. See
[the two-layer design note](ORGANELLE_LIFECYCLES/two-layer-model.md) for the
model, what changed in the engine, and the remaining options.

## Finding: existing modules are not yet rules

The pilot showed that most existing organelle-related modules are descriptive
pathway modules, scoped to a clade, with every part required:

- `mitophagy` (Eumetazoa) requires PINK1/Parkin marking, FBXL4 receptor
  turnover, and a disposal step grounded only on worm FIS-1 and FIS-2.
  Receptor choice is already modelled as alternatives (any one of OPTN/NDP52,
  <gene species="human" symbol="BNIP3">BNIP3</gene>/NIX, FUNDC1 or ALLO-1).
- `mitochondrial_dynamics` (Opisthokonta) requires mitofusin, which plants lack,
  and its fission node requires the metazoan MFF adaptor.
- `mitochondrial_upr` is metazoan.

Making these rule-ready means restructuring them with lineage `variant_sets`.
Until that is done, the umbrella links to them as optional.

## Coverage

The organelle-by-stage matrix lives in
[ORGANELLE_LIFECYCLES/coverage.yaml](ORGANELLE_LIFECYCLES/coverage.yaml).
Every eukaryote-wide rule candidate, plus the phagosome and synaptic vesicle modules, is evaluated
across 24 organisms in [ORGANELLE_LIFECYCLES/rule-evaluation.md](ORGANELLE_LIFECYCLES/rule-evaluation.md).
The per-organism counts and verdicts are in
[ORGANELLE_LIFECYCLES/selector-census.yaml](ORGANELLE_LIFECYCLES/selector-census.yaml), made by
[ORGANELLE_LIFECYCLES/selector_census.py](ORGANELLE_LIFECYCLES/selector_census.py) with the module engine
from PANTHER's release-pinned sequence classification files.

## Plan

- [x] `module_ref` schema slot, engine, validator and rendering (PR #5108)
- [x] `mitochondrial_protein_import` (eukaryote-wide, PAINT-grounded; `RULE_CANDIDATE`)
- [ ] Add the kinetoplastid Tim17-lineage realizer to the TIM23 and TIM22 activity steps of `mitochondrial_protein_import` (layer 2, see the [two-layer note](ORGANELLE_LIFECYCLES/two-layer-model.md)), after confirming its PANTHER placement; then mark it `RULE_READY`
- [x] Engine: label gaps by layer (`variant_kind`, declared or inferred), report gaps inside referenced modules, filter gap candidates to absent atoms, and carry family/domain selectors on atoms for proteome oracles
- [ ] Revisit a realizer list on each annoton (option 2 in the two-layer note) once proteome runs show how often realizer choices are written as variant sets
- [x] `mitochondrion_lifecycle` umbrella (import and iron-sulfur cluster assembly required; other stages optional)
- [ ] Make mitochondrial division rule-ready (Mff / Mdv1-Fis1 / FtsZ variants), then make it required
- [x] `mitochondrial_iron_sulfur_cluster_assembly`: core ISC machinery (NFS1-ISD11, ISCU with frataxin, HSCB-mtHsp70, GLRX5), eukaryote-wide and PAINT-grounded; `RULE_CANDIDATE` (Archamoebae use a NIF system)
- [ ] Extend the Fe-S module: Archamoebae NIF (and any SUF) realizers for the desulfurase and scaffold steps, the ferredoxin electron supply, and the late [4Fe-4S] machinery; check the frataxin/HSCB/GLRX5 arm against reduced mitosomal proteomes
- [ ] Extract a shared receptor-to-Atg8 capture module from `mitophagy`
- [x] Peroxisome: split `peroxisome-lifecycle` into an umbrella plus `peroxisomal_protein_import` (eukaryote-wide, PAINT-grounded per subunit; `RULE_CANDIDATE`); metabolism referenced as optional modules
- [ ] Peroxisome: ground the receptor E2 (Pex4/Pex22 and animal E2s) and the PEX1/PEX6 anchor (PEX26, Pex15, APEM9) per lineage; check the PEX3 step in kinetoplastid genomes and Pex16 and PTS2 losses against proteomes; add pexophagy
- [x] Lysosome/endosome: `lysosome_lifecycle` umbrella with two eukaryote-wide rule modules, `vacuolar_atpase_acidification` (V-ATPase, one PANTHER family per subunit) and `escrt_iii_intralumenal_vesicle_formation` (ESCRT-III and Vps4 by subfamily); both `RULE_CANDIDATE`
- [ ] Lysosome/endosome: add ESCRT-I (TSG101, VPS28, VPS37 reviews exist) and ESCRT-II; model endosome maturation (Rab7, Mon1-Ccz1, HOPS) eukaryote-wide; Vps10/VSR hydrolase sorting; lysophagy
- [x] ER: `endoplasmic_reticulum_lifecycle` umbrella with two eukaryote-wide rule modules, `er_cotranslational_translocation` (SRP, SRP receptor, Sec61) and `er_oxidative_protein_folding` (BiP, PDI; Ero1 and the calnexin cycle optional); both `RULE_CANDIDATE`
- [ ] ER: ground ERAD (Hrd1/Hrd3, Derlin, Cdc48-Ufd1-Npl4) once Hrd1's family table and per-lineage Cdc48/Hrd3 subfamilies are in place; add ER shaping, COPII export and a eukaryote-wide (IRE1) UPR; resolve SRbeta's PANTHER placement; add plant SRalpha and SRP68/72 selectors
- [x] Golgi: `golgi_apparatus_lifecycle` umbrella with one eukaryote-wide rule module, `golgi_copi_vesicle_coat` (GBF1/Gea, Arf1, coatomer); `RULE_CANDIDATE`; COPII referenced as the optional Drosophila module
- [ ] Golgi: ground a eukaryote-wide COPII module once Sec24, Sec31 and Sec12 have local PANTHER entries; add ArfGAPs, Golgi tethers and SNAREs, and TGN exit
- [x] Autophagosome: `autophagosome_lifecycle` umbrella with one eukaryote-wide rule module, `autophagosome_core_biogenesis` (Atg1 kinase, PI3-kinase complex I, Atg9/Atg2/Atg18, Atg12 and Atg8 conjugation); `RULE_CANDIDATE`; the metazoan and yeast assembly modules referenced as optional
- [ ] Autophagosome: add fungal Atg16 and plant Atg14 selectors, FIP200/Atg17 and ATG101, Atg10; model closure and fusion with the lysosome or vacuole
- [x] Nucleus: `nucleus_lifecycle` umbrella with one partial eukaryote-wide rule module, `nuclear_pore_transport_core` (four nucleoporins, Ran, NTF2, Crm1, Cse1); `RULE_CANDIDATE`
- [ ] Nucleus: add importin beta and alpha, RCC1, RanGAP and the remaining scaffold and FG nucleoporins as family selectors once they have local PANTHER entries (they are modelled by UniProt accession in `karyopherin_nuclear_protein_import`); model envelope sealing (CHMP7, LEM2) and open-mitosis disassembly
- [x] Lipid droplet: `lipid_droplet_lifecycle` umbrella with one eukaryote-wide rule module, `lipid_droplet_neutral_lipid_storage` (DGAT1 or DGAT2; FIT optional); `RULE_CANDIDATE`; TAG pathway and lipolysis modules referenced as optional
- [ ] Lipid droplet: add seipin once BSCL2 has a local PANTHER entry, the PDAT route, and a eukaryote-wide lipolysis step
- [x] Plastid: `plastid_lifecycle` umbrella (Embryophyta) with two rule modules, `plastid_protein_import` (Toc34 and Toc159 receptors, Toc75, Tic20, Tic110, ClpC, stromal processing peptidase; Tic214 and Tic40 optional) and `plastid_division` (FtsZ1, FtsZ2, ARC6, ARC5; MinD and PDV1/PDV2 optional), Arabidopsis-grounded; both `RULE_CANDIDATE`; photosynthesis modules referenced as optional
- [x] Plastid: stromal motor partners (cpHsc70 required; Hsp90C, FtsHi optional), Tic236 linker (required) and the remaining TIC subunits (Tic56, Tic100, Tic21, Tic22, Tic62, Tic32, Tic55, optional) added to `plastid_protein_import`
- [ ] Plastid: model Ycf2 once it has a reviewed entry; resolve the PANTHER-file placements of Tic100, Tic32 and ClpC1; make the required cpHsc70 step checkable per genome (the PTHR19375 entries table is capped at 1,000 rows); other green lineages' subfamilies (a green-algal import rule needs its own Toc34 selector, as Chlamydomonas TOC34 is in PTHR10903:SF135); a tighter MinD selector; model plastid quality control and chlorophagy; decide how red-algal and secondary plastids are scoped
- [x] Plant vacuole: `plant_vacuole_lifecycle` umbrella (Viridiplantae) with one new rule module, `plant_vacuole_fusion` (Mon1-Ccz1, RabG3, Vps41 and Vps39, SYP22 and VTI11), Arabidopsis-grounded; `RULE_CANDIDATE`; requires the eukaryote-wide ESCRT-III and V-ATPase rules
- [x] Plant vacuole: `plant_vacuolar_sorting_receptor_cycle` (VSR, retromer; RMR optional) and `plant_tonoplast_transport` (V-PPase, TIP1, vacuolar NHX; TPC1, TPK1, CLC-a, ALMT9 optional), both required by `plant_vacuole_lifecycle`; `RULE_CANDIDATE`
- [ ] Plant vacuole: add the HOPS core, SYP51 and VAMP713; resolve the VSR and RMR placements between UniProt and PANTHER's files; add fungal and animal Rab7 and SNARE selectors, and Vps39 from PTHR12894:SF49 (SF27 holds the CORVET TGFBRAP1/Vps3 proteins outside plants), so the fusion step can join `lysosome_lifecycle`
- [x] Cilium: `cilium_lifecycle` umbrella (Eukaryota) requiring one new rule module, `intraflagellar_transport_core` (nine IFT-B and four IFT-A subunits and the dynein-2 intermediate chain; IFT88, IFT56, IFT54, IFT20, the other dynein-2 chains and kinesin-2 optional), human-grounded at Eukaryota-level PAINT nodes; `RULE_CANDIDATE`
- [ ] Cilium: check the moss IFT gaps and the optional subunits' missing lineages against proteomes; add the BBSome, transition zone and motile axoneme as eukaryote-wide rules; model ciliary membrane trafficking and resorption
- [x] Phagosome: assessed; `phagosome_maturation` stays descriptive. Its core is the endolysosomal machinery, which the lysosome/endosome endosome-maturation item will model as a rule; three of its required selectors miss the human proteins in PANTHER's files and two required steps (RILP, LAMP) are holozoan-only (see coverage)
- [x] Synaptic vesicle: assessed; `synaptic_vesicle_cycle` stays `DESCRIPTIVE`. Its required steps hold in human, fly, worm and Nematostella, but only its synapsin step separates neuronal animals from other lineages (Trichoplax fails on it alone), and its Metazoa context, which the module does not qualify, includes sponges and placozoans (see coverage and `selector-census.yaml`)
- [ ] Synaptic vesicle: narrow the cycle's context to animals with neurons and name the exceptions in the module; find selectors confined to neuronal animals; check ctenophores and proteomes; then reassess as a rule candidate
- [ ] Phagosome: repoint the three `phagosome_maturation` selectors that miss human (Rab5, PIKfyve, V0a), already named in the module's own notes
- [x] Acidocalcisome: `acidocalcisome_lifecycle` umbrella requiring one new rule module, `acidocalcisome_polyphosphate_storage` (a VTC-domain subunit of `PTHR46140:SF1`, Vtc4 in most lineages, plus an H+-PPase or the V-ATPase; AP-3 delta optional); inositol pyrophosphate synthesis optional; `RULE_CANDIDATE` for the VTC lineages, met in the nine census organisms that have Vtc4 ([rule-evaluation](ORGANELLE_LIFECYCLES/rule-evaluation.md#the-acidocalcisome-rule))
- [ ] Acidocalcisome: add the Ca2+-ATPase, polyphosphate turnover and the contractile-vacuole link; separate the catalytic Vtc4 from Vtc2/Vtc3-type subunits that PANTHER places in `PTHR46140:SF1` (Toxoplasma Vtc2; the *Plasmodium* pass rests on such a protein); decide whether the fungal polyphosphate vacuole should be separated from the acidocalcisome; check Paramecium and Phytophthora, which have no Vtc4-type protein in PANTHER's files
- [ ] Specialized organelles: other lineage-specific organelles (contractile vacuole, lysosome-related organelles, hydrogenosome and mitosome variants)
- [x] Evaluate the rule candidates against PANTHER's reference-proteome classification files for 24 organisms, with the module engine ([rule-evaluation](ORGANELLE_LIFECYCLES/rule-evaluation.md)); mitosome- and hydrogenosome-bearing lineages fail the mitochondrial and peroxisomal rules as expected, and several rules fail in model organisms on one selector
- [x] Fix the MPP beta and alpha selectors (#6416) and the Pex2 selector (#6418), and rerun the rule evaluation with the fixes
- [ ] Fix the remaining model-organism selector defects listed in the rule evaluation; several of the smaller ones (Nup88, Seh1, Atg steps, SRbeta) also fail in protist lineages, so check each against the full gap list before narrowing the fix to one organism
- [ ] Triage the remaining gaps in the rule evaluation's full gap list (early animals, protists and the reduced-organelle lineages)
- [ ] Check the cilium rule's fly (IFT81, IFT74, IFT139), worm (DYNC2I2) and Trichoplax (IFT74) gaps
- [ ] Find out whether the lineages that PTHR13166 misses (plants and green algae, Monosiga, the chytrid, Phytophthora, Thalassiosira, Giardia, Trichomonas, Entamoeba) carry an ISD11 the family does not capture
- [ ] Compile protein-complex annotons into their active units in `module_logic`, so family-keyed oracles can evaluate complex steps
- [ ] Check the census gaps against the proteomes themselves, starting with the mitosome and hydrogenosome lineages once the selector defects are fixed
