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
positive position, an inhibitor under `none_of`), and every regulator to be used.
A regulator may be left out on purpose, as a modulator that tunes an already-active
step rather than switching it (MAPK serine-phosphorylating STATs, for example), but
only by naming it under `omitted_regulators` on the same element; an unused regulator
that is not listed is a validation error. Model pages draw such a regulator as a faint dotted edge
and name it beside the rule, so the asserted connection stays visible without being
mistaken for part of the logic. A scenario may remove an omitted regulator's
connection (an ERK-less counterfactual, say) without tripping the check. This is the regulatory counterpart of the structural AND/OR the schema already
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
| [JAK-STAT signaling](../modules/jak_stat_signaling.html) | [JAK-STAT signaling as a Boolean network](../models/jak_stat_signaling_boolean.html) | Boolean | derived | 6, all hold |
| [p38 cascade](../modules/p38_cascade.html) | [p38 cascade as a Boolean network](../models/p38_cascade_boolean.html) | Boolean | derived | 4, all hold |
| [Methionine cycle](../modules/methionine_cycle.html) | Maud kinetic model (biosustain) | Kinetic | external | |

The ERK scenarios encode what the curated wiring predicts: no stimulus → rest;
sustained stimulus → no steady state; feedback loops cut → ERK locked on; DUSP and
Sprouty both knocked out → still transient (in this model the direct ERK → RAF and
ERK → SOS feedbacks suffice on their own); MEK inhibited or RasGAP active → ERK off.

The JAK-STAT model needed rewiring before its scenarios meant anything. Its
negative-regulation bundle was wired with two edges, to JAK and to STAT
transcription, and translation expanded each to every child, so SOCS, PTPs and PIAS
all inhibited both. The module's own text is more specific, and the connections now
follow it child by child: SOCS and the phosphatases act on JAK, the phosphatases and
PIAS on nuclear STATs. The drawn graph and the update rules therefore agree. STAT
transcription still carries `activation_logic`, because ERK serine phosphorylation
only tunes maximal transcription; it is listed under `omitted_regulators`. Under
sustained cytokine the SOCS loop makes the response transient (Starr et al.,
[PMID:9202125](https://pubmed.ncbi.nlm.nih.gov/9202125/)). Without SOCS it locks on.
With PIAS active, STATs reach the nucleus but transcription is blocked, so SOCS is
never induced and JAK stays on. A JAK-independent STAT input is not terminated at all,
because SOCS acts only on JAK; that is a property of this wiring, recorded as such.

The p38 model has one loop, p38 output inducing MKP-1/DUSP1. Under sustained stress
p38 activity is transient. With MKP-1 lost it locks on, matching the prolonged p38
activation Hu et al. report when MKP-1 expression is blocked
([PMID:16978838](https://pubmed.ncbi.nlm.nih.gov/16978838/)).

The published MAPK model (Grieco et al.,
[PMID:24250280](https://pubmed.ncbi.nlm.nih.gov/24250280/)) also has a cyclic ERK
attractor under growth-factor input, which its authors read as transient ERK
activation. The agreement is in attractor kind, not mechanism: Grieco et al.
attribute their transience to feedback on the receptors (receptor degradation and
PKC), which the ERK module does not include, and report that disrupting the
downstream feedbacks does not qualitatively change their outcome. The module's
transience comes entirely from those downstream feedbacks. So the scenarios test
what the curated wiring implies; they are not a literature-validated mechanism.

## Roadmap

1. **More Boolean modules.** JAK-STAT and p38 are done. NF-κB translates but
   first needs its negative-regulation step (IκB resynthesis, A20).
2. **Audit the default rule across the corpus.** The
   [activator convergence audit](EXECUTABLE_MODELS/activator_convergence_audit.md)
   (generated by `audit_activator_convergence.py`) lists every step with two or
   more activators, which the translation ORs by default: 274 steps on
   2026-10-16. 40 are settled by structure, because their activators are
   alternative variants of one `variant_set`, so OR is right by construction.
   8 now carry `activation_logic`. 226 still need a curator to read the module.
   Some of those are genuine OR (two routes to one intermediate, as in purine
   oxidation). Others need every input, like the complex assembly and
   transport steps curated so far. Each is a decision, not a bulk change.
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
6. **Consolidate the code.** The translator, engine and viewer now exist twice, here
   and in AmiGO 3's Dynamics tab. [Architecture and long-term plan](EXECUTABLE_MODELS/architecture.md)
   sets out what depends on what, and plans one translator kept with the schema and
   a JSON payload as the contract between translator and viewers.
7. **GO-CAM as a source.** A GO-CAM is a signed causal graph over activities and
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
- `projects/EXECUTABLE_MODELS/architecture.md`: dependency layers and the
  consolidation plan with AmiGO 3.

---
# STATUS

- [x] Schema: `activation_logic` (declarative AND/OR/NOT over regulators) on nodes and annotons
- [x] Schema: `executable_models` with typed models, derivation, scenarios and expectations
- [x] Translator honours `activation_logic`; consistency checks against declared connections
- [x] Exhaustive asynchronous attractor search, cross-checked against biodivine-aeon (opt-in: the test skips unless `biodivine-aeon` is installed, which CI does not do)
- [x] Scenario expectations checked in module validation (blocking)
- [x] ERK cascade: derived Boolean model with six curated scenarios; BBM-070 as external model
- [x] Methionine cycle: Maud kinetic model as external model
- [x] Pst phosphate transporter: first curated `activation_logic` (capture AND ATPase)
- [x] Interactive model page, models index, module-page card, module-index filter
- [x] Curated scenarios for JAK-STAT and p38 (JAK-STAT with `activation_logic` placing each negative regulator)
- [x] Corpus audit of multi-activator steps for `activation_logic`: generated, 40 settled by structure, 8 curated
- [ ] Curate the 226 undecided steps in the audit
- [ ] Node-level `model_associations` for external model variables
- [ ] First constraint-based model type
- [ ] First agent-based model, following the dismech layout
- [ ] Payload JSON Schema and a `--json` mode for `module-to-bnet` ([architecture](EXECUTABLE_MODELS/architecture.md), Order step 3)
- [ ] Shared conformance fixtures run by every implementation (architecture, Order step 2)

# NOTES

## 2026-10-20

AmiGO 3 is adding a Dynamics tab to module pages
([cmungall/amigo3#74](https://github.com/cmungall/amigo3/pull/74), opened today, merged
2026-10-21). It ports this
repository's translator, which reproduces `module-to-bnet` on all 559 translating
modules at `924358b17`, and has its own JS engine. With two viewers, the translator
now exists twice. [Architecture](EXECUTABLE_MODELS/architecture.md) records the
dependency layers and the plan to make `boolean_model_payload` the contract.

## 2026-10-16

Follow-up to the merged PR. JAK-STAT and p38 got derived Boolean models with curated
scenarios; JAK-STAT also got `activation_logic` on JAK activation and STAT
transcription, because its negative-regulation bundle's two edges expanded to every
child and so mis-placed SOCS, PTPs and PIAS. On review the bundle edges were replaced
by child-level connections, so the graph no longer contradicts the rules, and JAK
activation went back to the default rule. The model page now opens on the first
scenario with a cyclic outcome, and wide graphs get the full page width.

`activation_logic` may now leave a declared regulator out on purpose. A Boolean rule
can make a regulator necessary, sufficient or part of a combination, but it cannot
say "tunes the output", and the modulators met so far (ERK on STAT Ser727, SecDF-YajC
on SecYEG, SMA-10 on the BMP receptors, LigD end processing) are exactly that. A
first version made the omission a warning; on review that removed the only
completeness check, so the omission must now be declared under `omitted_regulators`
and an undeclared one is still an error. The type IV secretion module wires
mating-pair stabilization as regulating the pilus, though the text reads it as
downstream of pilus contact; that pre-existing direction is left for a curator. The
three new JAK-STAT child-level connections (PTP on JAK, PTP and PIAS on nuclear STATs)
carry descriptions from the node text but no evidence items yet, as their nodes did
before; since PIAS's placement decides the `pias_restraint` scenario, attaching the
canonical references is the next curation step for that module.

The activator convergence audit classifies steps from structure alone. Curated from
the modules' own text: SsuD desulfonation (substrate AND reduced FMN), IscU cluster
assembly (persulfide sulfur AND ferredoxin electrons), the type IV secretion pilus
(core platform AND VirB4 ATPase; mating-pair stabilization left out), SecYEG
translocation (SecA; SecDF-YajC left out), SMA-6/DAF-4 receptor activation (DBL-1;
SMA-10 left out) and LigD end sealing (Ku end recognition; conditional processing left
out). The chemotaxis motor output was left undecided: its C-ring node models the bias
switch, not the rotor, so whether rotation needs it is not settled by the module.

Review leftovers from the PR: `validate_executable_models` now requires a
`repo_root` (the validator passes the project root), and there are tests for the
working-directory independence and the missing-`module` guard. The suggested guard
for a "cyclic module tree" was not added: element ids are indexed by their last
occurrence in a pre-order walk, which is never an ancestor of another occurrence, so a
duplicated id cannot create a cycle and the raise in `_descendants` guards an
invariant rather than a reachable input. That reasoning is now in its docstring.

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
