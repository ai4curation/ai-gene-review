# Mla carrier capacity: additive ontology-refinement successor

This package supersedes the original capacity oracle **for the current corrected gene inputs**. It does not rewrite the original oracle, fixtures, input hashes, results or any earlier receipt. No gene, module, family, source or raw record was edited.

## The actual regression

BP3761/Q7VSZ6 now asserts GO:0008429 phosphatidylethanolamine binding in its binding core, with exact-target deposited ligand/sequence support. It retains a separate GO:0120014 phospholipid-transfer core. Consequently, the original `core_activity()` still passes the real current protein through that separate transfer core. The complete Bordetella cases nevertheless fail at the **declared unit activity** check: the module declares GO:0005543 phospholipid binding, but the original checker requires that exact ID in the gene's cores.

`original-current-input-probe.json` records that failure without executing the original script's `main()`. Exactly two original cases change between old and successor semantics: `bordetella_five_component` and `bordetella_flux_unknown_not_negative`, both false negatives under the original exact-ID comparison. All other original case outcomes are unchanged.

## Minimal semantic correction

Official QuickGO responses retrieved on 2026-11-07 establish that:

* GO:0008429 is an **is_a** child of GO:0005543, and its `relations=is_a` ancestor response contains GO:0005543.
* GO:0008289 lipid binding does **not** have GO:0005543 as an ancestor. The direction of entailment cannot be reversed.
* All three terms are active molecular functions.

The exact response bytes, URLs, timestamps, headers and SHA256 values are frozen in `binding-terms.json`, `pe-binding-ancestors.json`, `lipid-binding-ancestors.json` and `ontology-provenance.json`. The official endpoint is [QuickGO](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0008429/ancestors?relations=is_a).

The successor accepts the evidenced PE-binding subclass only where the **carrier's GO:0005543 requirement** is being tested: in the binding-plus-transport-process fallback and in the declared carrier activity check. Exact GO:0005543 remains accepted. Unknown terms receive no inferred ancestry; there is no generic lipid-binding exemption or global relaxation of other roles' activity checks.

All original fixtures are copied byte-for-byte. An AST comparison verifies that only `core_activity()` and `evaluate()` change among existing functions; the sole added oracle function is `carrier_binding_satisfies()`. The root-path adjustment directs every output into this new directory. `oracle-successor.diff` records the exact source change.

## Coverage and discriminating controls

The unchanged original suite passes: **18 members, 60 cases, 14 structural mutations, 12 gate sensitivities and eight broad-family controls**.

Nine additional in-memory counterfactuals pass. They test the real PE-binding/transfer cores, the PE-binding-plus-transport-process fallback, insufficient generic lipid binding with and without the separate transfer core, PE binding without the transport process, wrong carrier compartment, isolated carrier without native partners, cross-panel carrier substitution, and missing source support.

The generic-binding negatives are substantive: bypassing only the function gate rescues the two synthetic profiles, establishing that their failure comes from the insufficient activity claim rather than an unrelated missing component. Reverting only the ontology helper to exact-ID matching also recreates the actual Bordetella false negative. These supply **three additional sensitivity checks**, for **69 total cases and 15 sensitivities**, alongside the unchanged 14 structural mutations and eight family controls.

Binding alone does not grant carrier capacity. The fallback still requires the reviewed intermembrane-transfer process, appropriate periplasmic location and the independent source, role, member identity, family, matched-panel, assembly, cargo, ATP, diderm-envelope and compatible-interface conditions. Failures mean insufficient evidence-qualified capacity within this finite profile, not biological impossibility or absence of secondary activity.

## Scientific boundaries retained

The exact-target BP3761 ligand structures establish binding under recombinant structural conditions, not native lipid occupancy, physiological substrate exclusivity or native net transport flux. The Bordetella B213-to-Tohama I locus/lineage bridge remains qualified; no exact experimental sequence identity is newly asserted for every component. Its five-component architecture does not make MlaB universally dispensable. E. coli conditional overexpression rescue remains outside the encoded native reference profile. PSEPK remains a matched conserved-function inference; PAO1 remains a carrier-only comparator. No foreign subunit pairing is licensed.

The production compiler's documented limitations remain in `results.json`: it does not itself evaluate active units, biological contexts or connection edges, and its EXACTLY_ONE implementation is at-least-one. The wrapper's original gates and structural controls remain necessary.

## Reproduction and preservation

From the repository root, use the existing environment:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/review-followup/capacity-successor/run_successor.py
```

The runner writes only successor outputs. The original script must not be run in place. Final execution and Ruff checks passed; exact commands and logs are in `check-receipts.json`. No full validation or new environment was used.

`protected-inputs.json` and `preservation-result.json` verify **731 pre-existing files** unchanged in bytes and modes, including both sealed gene/source-closure handoffs, original capacity artifacts and source dependencies. `successor-input-hashes.json` records actual executable inputs; the handoff and stage manifest enumerate this additive package. Prior receipts remain historical, including their original input versions and successful results.
