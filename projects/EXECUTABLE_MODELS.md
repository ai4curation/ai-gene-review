---
title: "Executable models: running the module knowledge base"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human]
autolink_gene_symbols: false
manifest:
  artifacts:
    - href: https://claude.ai/artifact/RvU9kSUAsvoz17LfaKWAXw
      title: Executable modules brief
      description: AI generated
---

# Executable models

**A module is curated knowledge about a pathway: its steps, who does them, and how
they are wired. This project makes that knowledge runnable. A module can now declare
the executable models that realize it (Boolean networks today; kinetic,
constraint-based and agent-based models on the same footing), the scenarios they
are run under, and what the curated wiring predicts in each. Scenario expectations
are checked in validation, so a wiring change that alters the predicted behaviour
fails like a wrong term id does.**

Try it: the [ERK cascade as a Boolean network](../models/erk_cascade_boolean.html)
runs in the browser. Pick *Sustained stimulus* and press Run. The cascade switches
on tier by tier, then ERK's feedback shuts it off again and it never settles. Pick
*Feedback loops cut* and ERK locks on instead. Click any box to knock it out or force
it on. All models are listed on the [executable models index](../models/index.html),
and the [module index](../modules/index.html) has a filter for modules that carry one.

## The principle: the module is the model

The [BOOLEAN_MODELS](BOOLEAN_MODELS.md) project showed that translating a module
mechanically into a Boolean network is not, on its own, a good model. The modules
had their negative feedback described in prose but cut in the YAML, so the
translated ERK cascade locked on, which is wrong. The fix was not to hand-edit the
generated network. The missing feedback connections were curated **into the module**,
with primary evidence, and the network was regenerated from it. This project turns
that into the rule:

- A model **derived from the module** is generated from its `connections` and
  never edited by hand. Fixing the model means fixing the module.
- An **external** model (a published logical model, a kinetic model) is evidence
  for the module's wiring, reached through a reviewed id-mapping. It is not a
  replacement for the module.
- Anything a model needs that the module cannot express is a **schema gap**, to
  close in the module schema, not a patch to the model.

## What the schema now says

Two additive, optional slots (`src/ai_gene_review/schema/gene_review.yaml`):

**`activation_logic` on a node or annoton**: declarative Boolean logic over the
elements that regulate it. By default a step is ON when any activator is ON and no
inhibitor is (the CaSQ convention, [PMID:32403123](https://pubmed.ncbi.nlm.nih.gov/32403123/)).
Where that is wrong, the curator states the logic as a tree, not as a rule string:

```yaml
- id: pstsacb_phosphate_translocation
  activation_logic:
    all_of:            # an ABC importer needs the loaded binding protein AND ATP hydrolysis
      - element: psts_phosphate_capture
      - element: pstb_energy_coupling
```

`all_of`, `any_of` and `none_of` (NOT-OR) nest freely. Validation requires every
named element to have a matching signed connection into the step (an activator in a
positive position, an inhibitor under `none_of`), and every such regulator to be
used. This is the regulatory counterpart of the structural AND/OR the schema already
had: `parts` are conjunctive and `variant_sets` disjunctive, but those say what a
step is *made of*, not how its incoming regulation combines.

**`executable_models` on a module**: each entry has a `model_type` (`BOOLEAN`,
`KINETIC`, `CONSTRAINT_BASED`, `AGENT_BASED`), a `derivation` (`DERIVED_FROM_MODULE`
or `EXTERNAL`), files, evidence, and `scenarios`. A scenario holds elements fixed
(`settings`: stimulus, knockout, constitutive mutant), can remove connections for a
counterfactual, and states its expectations: attractor kind (`FIXED_POINT` or
`CYCLIC`), attractor count, and elements that must be on, off or oscillating.

```yaml
- id: feedback_cut
  label: Feedback loops cut
  settings:
    - {element: adaptor_recruitment, active: true}
    - {element: mapk_negative_regulation, active: false}
  removed_connections:
    - {source: erk_mapk, target: raf_map3k}
    # ...
  expected_attractor_kind: FIXED_POINT
  expected_active: [erk_mapk]
```

## How it is checked

`src/ai_gene_review/module_dynamics.py` finds the attractors of a derived Boolean
model by exhaustive enumeration of the asynchronous state-transition graph (terminal
strongly connected components). That is exact and needs no solver for module-sized
networks (up to 18 variables, 262,144 states). On the ERK module it agrees with
biodivine-aeon's symbolic algorithm: one 188-state cyclic attractor under sustained
stimulus (`tests/test_module_dynamics.py` cross-checks the two when aeon is
installed). The module validator runs every declared scenario, and a failed
expectation is a blocking error.

The same computation runs in the browser: the model page carries the network as
JSON and recomputes the attractors whenever a box is locked.

## Current models

| module | model | type | derivation | scenarios |
|---|---|---|---|---|
| [ERK cascade](../modules/erk_cascade.html) | [ERK cascade as a Boolean network](../models/erk_cascade_boolean.html) | Boolean | derived | 6, all hold |
| [ERK cascade](../modules/erk_cascade.html) | MAPK network and cancer cell fate (Grieco 2013, BBM-070) | Boolean | external | |
| [Methionine cycle](../modules/methionine_cycle.html) | Maud kinetic model (biosustain) | Kinetic | external | |

The ERK scenarios encode what the curated wiring predicts: no stimulus → rest;
sustained stimulus → no steady state (transient ERK, as in Grieco et al.,
[PMID:24250280](https://pubmed.ncbi.nlm.nih.gov/24250280/)); feedback loops cut →
ERK locked on; DUSP and Sprouty both knocked out → still transient (the direct ERK
→ RAF and ERK → SOS feedbacks suffice on their own); MEK inhibited or RasGAP active
→ ERK off.

## Roadmap

1. **More Boolean modules.** JAK-STAT, p38 and NF-κB translate already. Each
   needs curated scenarios before it is listed. NF-κB first needs its
   negative-regulation step (IκB resynthesis, A20).
2. **Audit the default rule across the corpus.** Translating all 364 modules
   with connections (`module-to-bnet --all`, 2026-10-05) gives 159 steps in 100
   modules with two or more activators, each defaulting to OR. Some are genuine
   OR: two routes to one intermediate, as in purine oxidation, where guanine
   deamination and hypoxanthine oxidation both yield xanthine. Others plainly
   need every input: complex assembly and transport steps such as the Pst
   transporter above, or Fe-S cluster assembly on IscU, which needs both
   sulfur delivery and electron delivery. Each is a curation decision for
   `activation_logic`, not a bulk change.
3. **External models per node.** `executable_models` attaches an external model to
   the module as a whole; the variable-level mapping still lives in sidecar files
   (`models/boolean/*/mapping_to_modules.yaml`). A node-level `model_associations`
   slot ([schema gaps §5](BOOLEAN_MODELS/schema_gaps.md)) would make the mapping
   visible on module pages.
4. **Constraint-based models (GEMMs).** Metabolic modules map to reactions. A
   derived flux model per module (or a module's reactions checked against a
   genome-scale model's) is the next type to add. Small ones can run in the
   browser with a JS LP solver.
5. **Agent-based models.** Developmental modules (neuronal migration, cerebellum
   development) are rules about cells, not molecules, and want an agent-based
   runner like dismech's
   [neuronal migration ABM](https://dismech.monarchinitiative.org/pages/models/neuronal_migration_abm.html),
   whose spec + Python runner + in-browser runner + committed results layout fits
   `executable_models` directly.
6. **GO-CAM as a source.** A GO-CAM is a signed causal graph over activities and
   can be read by the same translator. It has the same blind spot for feedback as
   uncurated modules, so its value is calibration, not a ready-made model.

## Files

- `src/ai_gene_review/module_boolean.py`: translation, now honouring
  `activation_logic` and removed connections.
- `src/ai_gene_review/module_dynamics.py`: attractors, scenario checks, browser
  payload.
- `src/ai_gene_review/render_models.py` and templates
  `executable_model.html.j2`, `executable_model_index.html.j2`: model pages,
  rendered with the module pages into `pages/models/`.
- `src/ai_gene_review/validation/module_validator.py`:
  `validate_executable_models` (blocking).
- `tests/test_module_dynamics.py`, `tests/test_render_models.py`.

---
# STATUS

- [x] Schema: `activation_logic` (declarative AND/OR/NOT over regulators) on nodes and annotons
- [x] Schema: `executable_models` with typed models, derivation, scenarios and expectations
- [x] Translator honours `activation_logic`; consistency checks against declared connections
- [x] Exhaustive asynchronous attractor search, cross-checked against biodivine-aeon
- [x] Scenario expectations checked in module validation (blocking)
- [x] ERK cascade: derived Boolean model with six curated scenarios; BBM-070 as external model
- [x] Methionine cycle: Maud kinetic model as external model
- [x] Pst phosphate transporter: first curated `activation_logic` (capture AND ATPase)
- [x] Interactive model page, models index, module-page card, module-index filter
- [ ] Curated scenarios for JAK-STAT and p38
- [ ] Corpus audit of multi-activator steps for `activation_logic`
- [ ] Node-level `model_associations` for external model variables
- [ ] First constraint-based model type
- [ ] First agent-based model, following the dismech layout

# NOTES

## 2026-10-05

Project created from the BOOLEAN_MODELS follow-up. The design choice was declarative
logic over an `update_rule` string: the tree form validates against the declared
connections, nests, and maps one-to-one onto SBML-qual function terms, while a
string would have needed its own parser and could name anything. `none_of` stands in
for NOT so the slot names stay valid identifiers in the generated Python model.

The attractor search is pure Python so validation needs no solver dependency;
biodivine-aeon stays the tool for large networks and for the BOOLEAN_MODELS demo,
and the test suite compares the two on the ERK module when aeon is present.

The ERK module had gained a Sprouty/Spred feedback step on `main` after the
BOOLEAN_MODELS work, which doubled the cyclic attractor from 94 to 188 states. The
BOOLEAN_MODELS demo now reads its counterfactual from the module's `feedback_cut`
scenario, so the report and validation simulate the same thing; its RESULTS were
regenerated.

A YAML pitfall worth knowing: a scenario id of `on`, `off`, `yes` or `no` is
parsed as a boolean by YAML 1.1 loaders. Use descriptive ids.
