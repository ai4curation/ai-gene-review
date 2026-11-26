# Additive Lol module and capacity integration

Seven module UniProt `term.label` values now match the frozen 17-record source map exactly. Functional descriptions remain in `preferred_term` and descriptive fields. The parsed module differs only at those seven labels: no topology, participant identity, activity, evidence, scope or route changed. The rendered page is byte-identical because its preferred display terms did not change. A new scaffolded module history records the integration.

`check_integration.py` imports the original capacity checker without editing it, redirects its fixture/output directory into `original-rerun/`, and runs all 32 original cases, five original structural mutations and five original gate-sensitivity checks against the current module and current 17 reviews. The original cases are copied byte-for-byte. All historical capacity files remain unchanged.

An additional external predicate checks source-supported core locations, official Pfam domains, explicit ATPase core activity and positive core support. Domains and compartment assignments are not sufficient activity evidence: the original exact-member/family/activity/role/partner gates remain conjunctive. Six sensitivity tests mask carrier or membrane domains, carrier or insertase compartments, carrier source support, or the canonical ATPase activity, while preserving other evidence. The qualified profile fails and disabling the relevant gate restores the false positive. Four further mutations alter actual module function/location declarations and are rejected. These are methodological tests, not claims that the real proteins lack those functions.

This closes a limit in the earlier checker: it did not explicitly bind all module function declarations or compartment/domain metadata to its activity predicates. The new tests are external gates, not newly implemented production-compiler semantics. The compiler still does not independently infer active-unit assembly, compatibility, proposed insertion chemistry or construct context. A negative bounded profile does not establish biological impossibility. The original positive conditional LolDE and engineered LolAB-bypass observations remain outside the canonical encoded profiles, without being called negative biology.

All five insertion proposals have the same name, definition and parent. Their evidence tiers remain distinct. In particular the broad Fjoh_2111 source qualifier is preserved; the SUSPECTED/CHECK request concerns relation precision, while inferred direct carriage and outer-membrane localization rest on native client-trafficking evidence plus architecture. The capacity oracle does not use that qualifier or an ACCEPT action as a substitute for functional evidence.

`check_closure.py` verifies all 278 source dependencies of the frozen gene-follow-up release, all 111 release-file hashes, and preserved historical receipt bytes. It applies exact before/after transitions to original capacity inputs and records an explicit additive supersession map, including the module label update. It also checks every current module/member/boundary quotation using production reference/local-source matchers without baseline exemption. Two historical ignored-cache sources are resolved to the earlier byte-identical durable copies. No cache write or source refresh is performed.

Reproduce into these additive output paths before freeze:

```sh
uv run python analysis/module_audits/bacterial_lol_lipoprotein_trafficking/review-followup/module-integration/check_integration.py
uv run python analysis/module_audits/bacterial_lol_lipoprotein_trafficking/review-followup/module-integration/check_closure.py
```

After freeze, hash verification is preferable to rewriting the reports. `determinism.json` records byte-identical repeated outputs. Module schema and semantic checks, render, new history validation and file-scoped Ruff pass. Existing family-scope/membership and no-GO-ID advisories are preserved in `semantic.log`; a proposed insertion function is not assigned an invented GO identifier.

Prior module/capacity and gene-follow-up receipts remain immutable. No project edit, full-corpus validation, stage, commit or push was performed. The PR6186 ECO-import dependency hold remains unchanged; local code support is not evidence of an upstream merge. Ownership is released to root with the final handoff.
