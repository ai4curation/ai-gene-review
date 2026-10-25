---
title: "Executable models — who depends on what, and where the code should live"
maturity: SCOPING
tags: [PIPELINE]
autolink_gene_symbols: false
---

# Executable models: architecture and long-term plan

Part of [EXECUTABLE_MODELS](../EXECUTABLE_MODELS.md).

Two viewers now run module-derived Boolean models: this repository's
[model pages](../../models/index.html) and the **Dynamics** tab on AmiGO 3 module
pages (merged in [cmungall/amigo3#74](https://github.com/cmungall/amigo3/pull/74); that
repository is private for now, so the AmiGO 3 links and figures on this page are not yet
publicly checkable). Both are
interactive: you can perturb steps, run curated scenarios and check expectations. They
were written separately, so the code is duplicated. This page sets out what depends on
what, which duplication matters, and where each piece should end up.

## Four layers

| Layer | What it is | Module-specific? | Implementations (2026-10-25) |
|---|---|---|---|
| 1. Schema | `connections`, `activation_logic`, `omitted_regulators`, `executable_models` and scenarios | yes | `src/ai_gene_review/schema/gene_review.yaml` |
| 2. Translator | module YAML to a Boolean network: container flattening, signs, the default rule, declared logic, removed connections | yes | `module_boolean.py` here; `amigo3/boolean.py` (a port) |
| 3. Engine | network to stepping, attractors and scenario verdicts | **no** | the stepping and attractor search in `module_dynamics.py` (Python); the inline JS in `executable_model.html.j2`; `amigo3/web/boolean-engine.js` |
| 4. Viewer | interactive pages | – | model pages here; the AmiGO 3 Dynamics tab |

Each layer depends only on the one above it. The engine needs nothing from the module
schema: it consumes a network. The browser engines already work that way, reading only
the payload. The Python file does not yet: `module_dynamics.py` also holds the scenario
glue, which reads `executable_models`, settings and removed connections from module
YAML and calls the translator. Replacing its engine with aeon or mpbn (Plan step 3)
therefore means splitting the file, not swapping it.

**The translator encodes what the schema means**, and it has changed twice in a week
(`activation_logic` in #4966, `omitted_regulators` in #5041). A copy that drifts
produces a model that runs and looks plausible, but is wrong without any error. That is
the duplication to remove.

**The engine is generic, textbook code** (asynchronous update; terminal strongly
connected components of the state graph). Duplicating it is cheap and low-risk, as
long as the copies are tested against each other.

Two facts make consolidation easier:

- **The data contract already exists, in two close variants.** Both
  `module_dynamics.boolean_model_payload()` and AmiGO 3's `/api/boolean` emit the base
  network, the `.bnet` text, and for each scenario its settings and removed edges.
  They differ as follows (2026-10-25), and reconciling these is the substance of
  Plan step 1:

  | | `boolean_model_payload()` | AmiGO 3 `/api/boolean` |
  |---|---|---|
  | Unit | one payload per executable model | one per module, with the scenarios of every derived Boolean model |
  | Rules | `rules` map of regulated variables to `{text, tree}` | `rule` string on each variable, `null` for inputs |
  | Variables | `id`, `label`, `input` | also `group`, `kind`, `activators`, `inhibitors`, `members` (resolved to loaded genes) |
  | Declared logic | top-level `declared_logic` list and `omitted` map | `declared_logic` flag and `omitted_regulators` list on each variable; `omitted` flag on each edge |
  | Edges | `[source, target, sign]` | objects with `source`, `target`, `sign`, `connection_types`, `omitted` |
  | Scenario rules | `rule_overrides`: only the changed rules, `null` for a variable that became an input | `rules`: the full map, or `null` when nothing is removed |
  | Scenario results | precomputed `attractors` and `failures` | the `expected_*` fields, checked in the browser |
  | Inconsistent declared logic | translation refuses (no payload) | `logic_problems` listed; that step alone falls back to the default rule |
  | Layout | precomputed layered `layout` | none (laid out in the browser) |
- **The translator and engine depend on very little.** `module_boolean` and
  `module_dynamics` themselves need only `pyyaml` and the standard library. The
  exception is the one-line `as_list` helper, which `module_boolean`,
  `module_dynamics` and `module_notation` import from `render_modules`; that module
  in turn imports `jinja2` and `module_qc`. Moving `as_list` into a leaf module is a
  prerequisite for the package extraction below.

## Plan

1. **Make the payload the contract.** Write a versioned JSON Schema for the
   `boolean_model_payload` output and add a `--json` mode to `ai-gene-review
   module-to-bnet`, which together with its existing `--all` emits it for every
   module. Viewers then consume the payload, never module YAML,
   so `activation_logic` and flattening are known only to the translator.
2. **One translator, kept with the schema.**
   - **Now:** `amigo3 build --repository` already snapshots this repository. It should
     also run this repository's own translator, through the command above, and store
     the payloads. Translator and data then always come from the same commit, so they
     cannot drift.
   - **Later:** once `as_list` has moved, extract a small `pyyaml`-only package
     containing `module_boolean` and `module_dynamics`. Do this only when the module
     schema itself moves out of this repository and gains other consumers, for example
     GO-CAM tooling. Before then, a pinned package version would lag the data it reads.
3. **Engines: reuse in Python, publish one in the browser.**
   - **Python:** validation should use existing tools rather than grow its own engine.
     `biodivine-aeon` is a dev dependency, so the cross-checks of the exhaustive search
     against aeon (`tests/test_module_dynamics.py` and every conformance case) run in
     CI. Networks above the exhaustive limit of 18 variables should go to aeon or mpbn.
   - **Browser:** we have not found a maintained JS library that does asynchronous
     attractors and scenario checks on `.bnet` input; check before building. If none
     exists, extract one dependency-free file of about 150 lines, with `.bnet` or the
     payload as input. Both viewers would vendor the same pinned copy. A standalone
     engine could also run external models, such as GINsim or BBM exports.
4. **Shared conformance fixtures, run in both repositories' CI.** These now exist in
   [`models/boolean/conformance/`](https://github.com/ai4curation/ai-gene-review/tree/main/models/boolean/conformance): six
   synthetic modules, one per translation rule or dynamic behaviour, plus frozen
   snapshots of three modules with curated scenarios (ERK, JAK-STAT, p38) and two with
   omitted regulators. Each case pins the variables, rules, signed edges, the rules
   under each scenario's removed connections, and the asynchronous attractors with
   inputs free and under each scenario. `tests/test_boolean_conformance.py` checks them
   against this repository's translator and engine, and against biodivine-aeon. Every
   other implementation runs the same cases, so drift fails a build instead of going
   unnoticed.
5. **Viewers specialise.**
   - The model pages here stay static and light, part of the published site with no
     server.
   - AmiGO 3 is the explorer: it adds gene resolution across loaded species, links to
     annotations, and later the external-model calibration panel.
   - Once AmiGO 3 is publicly deployed, the model pages can link each model to it.

### Order

1. ~~Merge [amigo3#74](https://github.com/cmungall/amigo3/pull/74), which carries the
   port and its parity tests.~~ Merged 2026-10-21.
2. Conformance fixtures here, run in both repositories' CI. This depends on nothing
   else, and every later step then lands with a check underneath it. Done here
   2026-10-25; AmiGO 3 runs them from a pinned copy.
3. Here: a `--json` mode for `module-to-bnet`, plus the payload JSON Schema.
4. AmiGO 3 build consumes the payload, with the port kept as a fallback for one
   release.
5. Extract the JS engine and point `executable_model.html.j2` at it.
6. Retire the AmiGO 3 port.

## Parity

Measured by translating every module with both implementations, not by the fixtures:

| Date | ai-gene-review commit | Modules that translate | Rules differing | Scenario networks differing |
|---|---|---|---|---|
| 2026-10-20 | `924358b17` | 559 | 0 | 0 |
| 2026-10-25 | `6987a3bd0` | 574 | 0 | 0 |

Both runs include every module with `activation_logic` and the network of every
scenario that removes connections. The JS engine confirms all twelve curated ERK and
JAK-STAT scenarios. The conformance fixtures turn this one-off measurement into a
standing check on a fixed set of cases.
