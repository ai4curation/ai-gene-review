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

| Layer | What it is | Module-specific? | Implementations (2026-10-24) |
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

- **The data contract already exists.** `module_dynamics.boolean_model_payload()`
  emits nearly the same JSON as AmiGO 3's `/api/boolean`: the base network, plus for
  each scenario its settings, rule overrides and removed edges.
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
     `tests/test_module_dynamics.py` has a cross-check of the exhaustive search against
     biodivine-aeon, but it is opt-in: `biodivine-aeon` is not a project or dev
     dependency, so the test is skipped in CI. Making it run there belongs with the
     conformance fixtures (Plan step 4). Networks above the exhaustive limit of 18
     variables should go to aeon or mpbn.
   - **Browser:** we have not found a maintained JS library that does asynchronous
     attractors and scenario checks on `.bnet` input; check before building. If none
     exists, extract one dependency-free file of about 150 lines, with `.bnet` or the
     payload as input. Both viewers would vendor the same pinned copy. A standalone
     engine could also run external models, such as GINsim or BBM exports.
4. **Shared conformance fixtures, run in both repositories' CI.** Keep a small set
   here: module YAML, its expected `.bnet`, and each scenario's expected verdict. Every
   implementation, in either language, runs it, and the aeon cross-check runs with
   them. Drift then fails a build instead of going unnoticed. AmiGO 3's
   `tests/test_boolean.py` already does a two-module version of this against
   `module-to-bnet` output.
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
   else, and every later step then lands with a check underneath it.
3. Here: a `--json` mode for `module-to-bnet`, plus the payload JSON Schema.
4. AmiGO 3 build consumes the payload, with the port kept as a fallback for one
   release.
5. Extract the JS engine and point `executable_model.html.j2` at it.
6. Retire the AmiGO 3 port.

## Parity today

At commit `924358b17`, AmiGO 3's port produced the same rules as `module-to-bnet` for
all 559 modules that translate. That includes the eight modules with
`activation_logic` and the network of every scenario that removes connections. Its JS
engine confirms all twelve curated ERK and JAK-STAT scenarios.
