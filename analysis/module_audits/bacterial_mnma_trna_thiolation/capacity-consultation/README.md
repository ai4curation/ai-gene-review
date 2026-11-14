# MnmA capacity and source closure

The production module compiler, combined with explicit biological predicates, supports the E. coli Tus panel, inferred KT2440 Tus panel, Bacillus cognate pair, and either purified Thermus donor pairing. These are evidence-qualified capacities, not measurements of native pathway flux. A false result means the supplied panel/context lacks demonstrated compatible capacity in this modeled implementation; it is not a universal biological impossibility.

The final COMPLETE module hash is `0e523d3e53bd6999225ee3874990bee62a9378eda8b8be4fd01372b10da109df`. The prior independent scientific review read the same science at DRAFT. Closure reconstructs those exact prior bytes by changing only the status line and checks the parent's additive status-supersession receipt. No earlier handoff was rewritten.

## Independent expectations and source gates

`biology.yaml` defines experimentally or curatorially supported roles independently of the Boolean graph. Its panel evidence distinguishes E. coli assays, KT2440 homology/context inference, the Bacillus PS832/168 bridge, and the purified Thermus HB27 experiments. The checker reads all 19 current reviews and their immutable UniProt records, verifies accession/taxon/classification and supported cores, then supplies predicates to the actual `compile_node`, `is_satisfied` and `enumerate_routes` APIs.

TusBCD is treated as a complete role-bearing assembly: B and C contribute structure and D carries sulfur. The production compiler emits one atom for this complex and does not expand its active units; the wrapper checks all actual declared units, their role evidence and compatible panel. It does not assign the complex's sulfurtransferase activity autonomously to B/C. Consequently the separate unit-deletion mutations are biologically meaningful, rather than redundant checks of an already expanded compiler graph.

The terminal reaction requires cysteine-derived sulfur supply, ATP and susceptible U34 tRNA. A Thermus C-type positive additionally assumes active cluster-bearing MnmA under the characterized assay conditions. No universal positive or negative Fe–S requirement is imposed on D-type MnmA. The model leaves TusE's last covalent loading step unresolved and does not infer physiological IscS/SufS dominance from different purified rates.

Compatibility is positive evidence, not a species-label guess. Every accepted route must assemble a characterized or explicitly inferred matched panel; ECOLI/KT2440 component mixtures lack that positive pairing evidence. Two complete panels may coexist and still satisfy capacity. Failed assessment of a mixed panel is not a reported negative substitution assay.

The three counterexample accessions are actual official records in the frozen family consultation: A0R5M7 EgtE shares SF8 with the Thermus SufS; Q59072 SepCysS has a distinct tRNA substrate in the same parent family; O67046 has an SF6 classification without established exact MnmA activity. Their rejection as these module realizers does not assert absence of untested secondary activities.

## Cases and controls

`cases.json` contains 59 source-motivated scenarios, including six basic positive profiles, both Thermus donors together, two independent complete panels co-occurring, each component omission, substrate/ATP deficits, inactive C-type enzyme, mixed interfaces, a true but unqualified desulfurase pairing, broad-family controls and masked source/core/classification evidence. The omitted-component tests assess the canonical specified route. In particular, the isolated E. coli IscS/MnmA pair is a real simplified in-vitro bypass documented by PMID12549933; its failure to satisfy the full Tus profile does not deny that experiment or establish native Tus dispensability.

Nine graph mutations must alter at least one independently specified expected outcome: removing TusA, TusE, the Bacillus donor or terminal C-type MnmA; removing each B/C/D active unit; forcing the Tus route universally; or forcing both Thermus donors to be present together. Eight sensitivity controls demonstrate why source, core, classification, interface, supply and active-cofactor gates matter. A deliberately unsafe family-only predicate admits the same-SF8 EgtE control, showing that the family label cannot substitute for the activity/partner evidence.

## Production limitations

The production graph has ten atoms and four formal routes. `enumerate_routes` enumerates one branch choice at each OR, so the two Thermus donor choices are separate formal routes even when both are present. The evaluator treats `ONE_OR_MORE` and `EXACTLY_ONE` as OR; the current module uses ONE_OR_MORE and no exclusivity claim is inferred. The compiler does not evaluate connection direction, reaction stoichiometry, context conditions, native expression, protein complex assembly, sulfur loading, tRNA identity or active cofactor state. These predicates are explicit biological additions, not claimed native compiler features. A positive result is conditioned on supplied active proteins and assay-compatible substrate conditions.

The oracle is deliberately bounded to the reviewed 19 proteins and three verified controls. Representative lists are not treated as an exhaustive natural taxonomic distribution. A new homolog would need its own role and pairing assessment before this audit could score it positively.

## Preservation and reproducibility

`check_closure.py` verifies all original 166 ordered annotation payloads and qualifiers, all four historical NEW actions/lifecycles (four active, none retired), protected baseline sources, all prior consultant manifests and the exact status-only module supersession. It records module-to-member-to-core-source edges, 57 distinct verbatim quote assertions, hashes of the production compiler and its directly used repository helpers, and all requested root provenance/history additions. No durable input depends on an ignored `.cache` file. Project metadata and project renders remain the root owner's separate freeze scope.

Both checkers are read-only and print their results. Re-run them into temporary files, never over the frozen receipts:

```sh
uv run python analysis/module_audits/bacterial_mnma_trna_thiolation/capacity-consultation/check_capacity.py > /tmp/mnma-capacity-recheck.json
uv run python analysis/module_audits/bacterial_mnma_trna_thiolation/capacity-consultation/check_closure.py > /tmp/mnma-closure-recheck.json
```

Quote and source-edge ordering is explicitly sorted and deduplicated. The release includes repeated-run byte-equality checks; this avoids traversal-order changes masquerading as a changed scientific record. `handoff.json` freezes the outputs; no gene, family, module, project, raw source or earlier receipt was changed by this capacity consultation. No full-corpus validation, commit or push was performed.
