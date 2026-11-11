# Reproduce member grounding and route checks

Run from the repository root:

```sh
uv run python modules/bacterial_4_hydroxybutyrate_oxidation-source-analysis/check_module.py
```

The script runs the production module validator with the six exact gene-review paths and a bounded membership map read from unchanged normal UniProt records. It uses the production ontology and family-review checks; it does not build a multi-gigabyte membership index or replace biological review with a permissive resolver. `member-grounding.json` records the source paths, hashes and official family lines. Classification does not establish a family-wide function.

It then compiles the actual module using the production module-logic compiler and checks all 64 subsets of the six members. Only subsets containing both Cupriavidus catalytic activities satisfy the required route; Pseudomonas-only sets, either isolated native enzyme and cross-species incomplete pairs fail. `route-cases.json` preserves the expected/results snapshot. New outputs go to `.cache/module-audit-logs/`.

The predicate represents available catalytic activities in the stated selected/expressing context. It is not a prediction of native expression, growth, flux or chemistry from genome presence alone. The compiler does not infer the selected-strain condition; the module explicitly states that scientific limit. The required pair records a species-level biochemical implementation, not a jointly purified two-enzyme reconstitution.


### PR #5591 ontology verification

`ssadh-ontology-evidence.json` preserves the live QuickGO definitions and is_a/part_of ancestors retrieved on 2026-10-26, with request URLs. GO:0004777 and GO:0036243 descend from GO:0009013; GO:0009013 is not currently below GO:0004030. The module selects the measured GabD NADP branch and leaves Sad acceptor choice unresolved. This does not exclude the independently supported GabD NAD branch.
