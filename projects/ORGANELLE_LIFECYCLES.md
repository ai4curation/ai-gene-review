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
`MODULE:mitochondrion_lifecycle`, whose only required stage is the new
eukaryote-wide `MODULE:mitochondrial_protein_import`.

## Scope

- **Membrane-bounded organelles only.** Condensates, P granules and other
  membraneless bodies are out of scope; so are centrioles. The cilium stays in,
  as a membrane-bounded projection.
- **All eukaryotes.** Each module's taxon context is Eukaryota. Lineage
  differences are modelled as `variant_sets` (different machinery for the same
  stage) or as `optional` parts (a stage some lineages lack).
- **Rules, not compendia.** A non-optional part asserts "every eukaryote with
  this organelle has this". That is a stronger claim than a descriptive pathway
  module makes, and it is what lets the satisfiability engine
  (`ai_gene_review.module_logic`) find gaps in a new genome. Clade-specific
  compendia of the same stage (for example the Drosophila
  `dmel_mitochondrial_protein_import`) are legitimate descriptive modules, but
  the umbrella does not reference them.

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

## Plan

- [x] `module_ref` schema slot, engine, validator and rendering (PR #5108)
- [x] `mitochondrial_protein_import` (eukaryote-wide, PAINT-grounded; `RULE_CANDIDATE`)
- [ ] Model the kinetoplastid inner-membrane translocase as a lineage `variant_set` in `mitochondrial_protein_import`, then mark it `RULE_READY`
- [x] `mitochondrion_lifecycle` umbrella (import required; other stages optional)
- [ ] Make mitochondrial division rule-ready (Mff / Mdv1-Fis1 / FtsZ variants), then make it required
- [ ] Mitochondrial iron-sulfur cluster assembly module (universal to mitochondrion-related organelles; start from the Drosophila-only `dmel_iron_sulfur_cluster_assembly`)
- [ ] Extract a shared receptor-to-Atg8 capture module from `mitophagy`
- [ ] Peroxisome: split `peroxisome-lifecycle` into an umbrella plus referenced modules; add pexophagy
- [ ] Lysosome/endosome, ER, Golgi, nucleus, lipid droplet, autophagosome
- [ ] Plastid, plant vacuole, specialized organelles
- [ ] Evaluate the umbrellas against reference proteomes (mitosome- and hydrogenosome-bearing lineages first)
