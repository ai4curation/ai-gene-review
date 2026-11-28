# PR 6182 round-one capacity follow-up

This additive audit reruns the published independent capacity checker without changing the original checker, fixture, reports, source caches, consultation receipts or histories. Gene consultation outputs remain separately owned and frozen. The module retains its topology and chemistry; only six occurrences of three supporting quotations were expanded to complete clauses.

Run from the repository root:

```sh
uv run python analysis/module_audits/bacterial_l_carnitine_catabolism/round1/check_followup.py
uv run ruff check analysis/module_audits/bacterial_l_carnitine_catabolism/round1/check_followup.py
```

The default command checks the frozen input hashes. `--capture-inputs` was used only after both consultation handoffs were released and the authorized changes reviewed; it is an explicit recapture operation, not an automatic response to a mismatch.

The wrapper imports the unchanged published `capacity/audit_capacity.py` and reruns its actual production-compiler oracle: **49 cases, 14 module mutations and five evidence-gate sensitivities** pass. The exact independent chemistry fixture, evidence tiers, member identities, source quotes, family/taxon/assembly gates and fused-protein checks remain in force. Native phenotypes and growth are not computed from assembled capacity.

PP_0303 now expresses its previously proposed exact reaction through `core_functions.proposed_molecular_function`. The finite bridge accepts only Q88R31, the exact proposal name, reaction definition, GO:0016747 parent and independently checked catalytic source quotation on both the core and proposal. This recognizes a supported specific activity as satisfying a genus consistency check; it does not infer exact chemistry from the genus. The unchanged independent fixture still supplies the exact substrate/product reaction and evidence tier. Ten corruption tests reject missing/duplicate proposals, wrong name/parent/chemistry/target, missing core or proposal evidence, irrelevant evidence and fabricated quotations. This is not a general mapper for all proposed terms or family members.

Preservation is explicit:

- Fourteen reviews retain all **146 ordered source payloads**, including qualifiers and historical proposal rows. Only the two individually identified RHIME proposal rows gain `retired: true`; actions remain `NEW`.
- **11 historical NEW rows: six active and five retired.** The current two retirements are added to the three previously retired proposals. No row was deleted or manufactured.
- All **63 protected source files** and all five family reviews remain byte-identical to the baseline.
- Of the **255 published closure inputs**, 237 are unchanged and 18 are the explicitly authorized five gene review/notes/render trios plus module YAML/notes/render. The actual module page is `pages/modules/bacterial_l_carnitine_catabolism.html`; the initial draft's `modules/...html` allowlist path was corrected to this exact renderer output.
- **101 historical audit, receipt and preexisting history files** additionally match their Git bytes at the published baseline commit. Newly generated histories are additive.
- Both released gene consultation manifests are verified. The fresh closure includes all their files, all 255 previous inputs, new module history and the wrapper/proof inputs: **303 current inputs**. The old closure is not narrowed or rewritten.
- All module fields compare exactly after applying only the six authorized quotation substitutions; each expanded quotation passes the repository reference matcher.

`preservation.json` records exact action changes, lifecycle changes, before/after hashes and module quote occurrences. `results.yaml` contains the inherited capacity results. `proposed-core-guards.json` records the ten new defect checks. `input-hashes.yaml` freezes inputs; `capacity-handoff.json` freezes the new owned artifacts and closure. Ruff passes. This audit did not edit any gene, module, family, project, source cache or historical record, and did not run whole-corpus validation. Ownership is released to root for metadata integration, final validation and publication.
