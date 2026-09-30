---
title: "Boolean models — what the module schema lacks"
maturity: SCOPING
tags: [PIPELINE]
autolink_gene_symbols: false
---

# What the module schema lacks to be a Boolean model

Companion to [BOOLEAN_MODELS](../BOOLEAN_MODELS.md). The translator
(`ai_gene_review.module_boolean`, CLI `module-to-bnet`) already produces a runnable
Boolean network from any module that has `connections`, so nothing here is a blocker.
It is a list of what the translation has to **assume** because the schema cannot say
it, ordered by how often the assumption was wrong on the MAPK modules, with a
proposed slot for each. Proposed slots are additive and optional; existing modules
stay valid.

## 1. Feedback is modelled as an input, not a loop

**Observed.** Every one of the five signalling modules translated (ERK, p38, JNK,
JAK-STAT, NF-κB) has a "negative regulation" step (`mapk_negative_regulation`,
`p38_negative_regulation`, `jak_stat_negative_regulation`, …) that inhibits a kinase
tier but has **no incoming edge**, so it becomes a free input. JAK-STAT even had a
`socs_feedback` node that STAT transcription `CAUSES`, but SOCS's inhibition of JAK was
routed through the enclosing `jak_stat_negative_regulation` bundle rather than from
`socs_feedback` (fixed: SOCS now inhibits JAK directly, and the translator expands a
bundle with no internal wiring to its children when one of them is an endpoint, so
the bundle no longer doubles as a free input beside its own child). The module
*knew* the loop (the prose says "many ERK-induced as feedback") and the YAML cut it.

**Consequence.** As first translated, the ERK module had only fixed points; the
published model (BBM-070) oscillates under sustained EGFR stimulus because ERK
inhibits RAF and RSK inhibits SOS. With those loops now curated in, the translated
module oscillates too ([RESULTS §3a](RESULTS.md)); the counterfactual with the loops
cut, the module's earlier wiring, is the fixed point ([RESULTS §3c](RESULTS.md)).
Feedback is the single most consequential wiring fact for dynamics, and it is the
one the schema encouraged curators to drop.

**Proposal.** No new slot — a curation convention: a regulatory step that is *induced
by* the pathway's own output must carry the `CAUSES`/`POSITIVELY_REGULATES` edge from
the output step, so the loop closes.

**Status (2026-09-27): done for ERK, p38 and JAK-STAT; check implemented.** The
loops are now wired in `erk_cascade` (ERK ⊣ RAF, ERK output ⊣ SOS, ERK output → DUSP),
`p38_cascade` (p38 output → DUSP1) and `jak_stat_signaling` (SOCS ⊣ JAK), each with
primary evidence; the JNK step was reworded as an external input because its
phosphatase is p38/ERK-induced, not JNK-induced. `module_qc.feedback_loop_findings`
flags any `NEGATIVELY_REGULATES` source whose prose asserts feedback or induction
(negated sentences excluded) but has no upstream activating edge, counting a
container as closed through its children; it is advisory (a validator warning and a
"Feedback loops" card on the module page), never an error.

## 2. No sign on `CAUSES`-family edges, no way to say "no effect on its own"

**Observed.** `CAUSES`, `PRECEDES`, `PROVIDES_INPUT_FOR`, `HAS_INPUT`, `HAS_OUTPUT` are
all read as activating; only `NEGATIVELY_REGULATES` is inhibiting. That is right for
every edge in the MAPK modules, but `PRECEDES` (temporal order) and `HAS_INPUT`
(material flow) do not always mean "the source activates the target": a metabolite
pool that a reaction consumes `PRECEDES` nothing in a regulatory sense.

**Proposal.** An optional `sign` attribute on `ModuleConnection`
(`POSITIVE | NEGATIVE | NONE | UNKNOWN`), defaulting per `connection_type` as the
translator does now. `NONE` lets a curator keep a `PRECEDES` edge for ordering while
excluding it from the regulatory graph.

## 3. Rule combination is a convention, not a statement

**Observed.** The translator applies the CaSQ default (OR of activators, AND NOT of
inhibitors). For `stat_recruitment_phosphorylation` in JAK-STAT this yields
`alt_stat_inputs | receptor_phosphorylation` — correct, either route suffices. For a
complex-assembly step that needs *all* of several inputs, OR is wrong and AND is right;
for a dominant inhibitor vs. a strong activator the choice of AND-NOT vs. OR-NOT is the
whole biology (the model's `v_RAF, (v_PKC & !(v_ERK | v_AKT)) | (v_RAS & !(v_ERK | v_AKT))`
says inhibition dominates; a curator might disagree).

**Proposal.** Two optional attributes on `ModuleNode` and `ModuleAnnoton`:

```yaml
input_combination: ANY | ALL         # how activating inputs combine (default ANY = OR)
update_rule: "ras_active & !erk_mapk" # explicit bnet-syntax rule over element ids;
                                      # overrides the default entirely
```

`update_rule` is what `BooleanModel.with_logic()` already accepts; the demo's
"calibrated" ERK network is exactly a module with two `update_rule` values set.
Validation: every identifier in `update_rule` must be an element id of the document
(or a declared input), and the rule's regulators must be consistent with the declared
`connections` (each regulator has an edge to the node with a compatible sign). This is
the same "declared graph vs. function" consistency check that AEON's
`infer_valid_graph` performs.

## 4. Inputs, outputs, and read-outs are implicit

**Observed.** An input is "whatever has no incoming edge" — which conflates genuine
stimuli (`adaptor_recruitment`, `stress_input`) with the cut feedback nodes of §1 and
with regulators the module simply does not describe (`rasgap_step`). Outputs are
"whatever has no outgoing edge", which is usually a transcriptional-output step but
carries no phenotype label; BBM-070 has explicit `Proliferation`/`Apoptosis`/
`Growth_Arrest` read-out variables that the module has no place for.

**Proposal.** An optional `boolean_role` on `ModuleNode`/`ModuleAnnoton`:
`INPUT | OUTPUT | READOUT | INTERNAL`. `READOUT` nodes (phenotype-level, e.g. a GO BP
such as *cell population proliferation*) would let attractors be labelled by phenotype
the way published models do, and let a module's `processes` descriptors act as
read-outs.

## 5. External-model cross-references have no home

**Observed.** `gocam_associations` grounds a node in a GO-CAM activity. There is no
equivalent for "this node is variable `v_RAF` of BBM-070 / species `raf1` of
BIOMD0000000562 / entity `BRAF` in SIGNOR-EGF". The mapping now lives in a sidecar
(`models/boolean/*/mapping_to_modules.yaml`) keyed by a shared symbol namespace,
which works but is invisible to the module page and to QC.

**Proposal.** A `model_associations` list on `ModuleNode`/`ModuleAnnoton`, parallel to
`GoCamAssociation`:

```yaml
model_associations:
  - model: BBM:070            # or biomodels:BIOMD0000000562, signor:SIGNOR-EGF
    variable: v_RAF
    title: "MAPK cancer cell fate (Grieco 2013)"
    evidence: [{source_id: "PMID:24250280"}]
```

With this in place the sidecar mapping becomes a derived view, the module page can
render "this tier is calibrated against N models", and the calibration diff can run in
`module_qc` as an advisory panel like reaction chaining.

## 6. Levels, timing, and context

Multi-valued logical models (GINsim) distinguish e.g. ERK low/high; modules have a
single activity state. Priority classes/time scales (fast phosphorylation vs. slow
transcription) have no representation; neither do initial conditions. `ModuleContext`
already carries taxa/cell types/compartments and could scope a `update_rule` or a
`model_association` to a context. None of these are needed for the first pass and
they are recorded here so the omission is deliberate.

## What is *not* a gap

- **Hierarchy.** Container nodes flatten cleanly to entry/exit tiers (a GAP tier with
  only inhibitory internal edges is correctly excluded from a container's entry set).
  No slot needed.
- **Family-level tiers.** A `FAMILY` participant (RAF kinases) maps naturally onto a
  published model's lumped variable (`v_RAF`); the mapping file handles many-to-one in
  both directions.
- **Tier granularity.** Where the module has a MAP2K tier and the external model
  jumps MAP3K → MAPK, the diff reports the external edge as a *collapsed path*, not a
  disagreement (`path_sign`).
