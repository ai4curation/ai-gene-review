# Boolean-model conformance fixtures

The behaviour every implementation of the module-to-Boolean translator and the
asynchronous engine must reproduce. Two implementations read modules as Boolean networks
today: this repository (`ai_gene_review.module_boolean`, `module_dynamics`, and the model
pages' inline JavaScript) and the AmiGO 3 Dynamics tab, which ports the translator and has
its own JavaScript engine. The plan behind these fixtures is in
[EXECUTABLE_MODELS/architecture](../../../projects/EXECUTABLE_MODELS/architecture.md).

## Layout

```
models/boolean/conformance/
  README.md
  cases/<name>/
    module.yaml      # the input: a module document
    expected.json    # the output every implementation must produce
```

There are two kinds of case:

- **Synthetic**: small hand-written modules. Each isolates one translation rule or
  dynamic behaviour:

  | Case | Behaviour |
  |---|---|
  | `relay_with_phosphatase` | default rule; structural `PART_OF` edges ignored |
  | `negative_feedback_oscillator` | cycling under negative feedback; a removed connection gives a fixed point |
  | `toggle_switch` | bistability: two fixed points, one when a side is forced on |
  | `container_flattening` | entry and exit tiers of a wired container; a GAP tier is neither; annotons are atomic |
  | `unwired_container_expansion` | an unwired container is one step unless a child is itself an endpoint |
  | `declared_logic` | `all_of`, `any_of` and nested `none_of`; an omitted regulator; removing its connection drops it |
  | `container_lumped_by_removal` | removing a container's only internal connection turns it into one step |

- **Frozen**: slimmed copies of real modules that have curated Boolean scenarios
  (`erk_cascade`, `jak_stat_signaling`, `p38_cascade`) or omitted regulators
  (`c_elegans_dbl1_body_size_signaling`, `bacterial_type_iv_secretion_apparatus`). They
  keep only what translation reads (the tree, connections, declared logic and the derived
  Boolean models' scenarios), so later curation of the live module does not change them.

The `module.yaml` files are translator inputs, not full module documents: frozen copies
keep only the keys translation reads, and annotons carry an empty `participant` stub.
Do not run them through module validation.

## expected.json

| Field | Meaning |
|---|---|
| `format_version` | currently `1` |
| `source` | `synthetic` or `frozen` |
| `variables` | variable ids, in translation order |
| `inputs` | variables with no rule |
| `rules` | each variable's update rule in BoolNet syntax; `null` for an input |
| `edges` | `[source, target, sign, omitted]`, sorted; `omitted` marks a regulator the declared logic leaves out |
| `free_attractors` | the asynchronous attractors with every input free |
| `scenarios[]` | `id`, `model` (the executable model it belongs to), `settings` (fixed values), `removed_connections`, then the scenario's own network after those removals: `variables` (a variable left with no connection drops out; a container whose internal wiring is removed appears as one step), `rules` and `edges` (as above, keyed by those variables); `attractors` (with the settings fixed and other inputs free), and `expectations_hold` (the curated expectations pass) |

Each attractor is `{size, always_on, always_off, oscillating}`: the number of states in
the terminal strongly connected component, and which variables are constant on, constant
off, or change within it. Attractors are listed in ascending order of their smallest
state, so implementations should compare them as sets.

## Maintaining

```bash
uv run python scripts/build_boolean_conformance.py --check            # what CI runs (via the test)
uv run python scripts/build_boolean_conformance.py                    # rewrite expected.json
uv run python scripts/build_boolean_conformance.py --refresh-inputs   # re-copy frozen modules
```

`tests/test_boolean_conformance.py` fails when `expected.json` no longer matches this
repository's translator and engine, when a case's curated scenario fails, or when an
attractor disagrees with biodivine-aeon. A deliberate change to translation or dynamics
means rebuilding, reviewing the diff, and updating every other implementation to match.
