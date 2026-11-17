# Additive PR6196 gene review follow-up

This release addresses review 5811920552 and comment 6706163015 against published head `21996f473bb1e5375bab529d1aaf98146a3cc86a`. Read `decisions.md` for the scientific adjudication and `action-changes.json` for all 19 action changes.

Thirteen reviews, their notes and renders are updated. Thirteen append-only histories are new. The 18-member panel retains all 192 ordered published annotation payloads, all four existing NEW rows and their lifecycle, and all core functions. Five MtaD replacement lists now retain SAH/MTA while preserving measured weaker substrates as findings with unresolved physiological relevance. No annotation row is added, deleted or retired.

`preservation-supersession.json` records 39 exact published-before/after file transitions, 654 unchanged pre-existing files, 13 byte-preserved historical handoffs, and the exact affected entries of seven historical handoffs. Apply this additive map after the earlier receipts; never rewrite their hashes or conclusions. The parent-acquired new PMID12705835 cache is an additional immutable source. Its abstract does not name the assay organism, and the LuxS inference is qualified accordingly.

All 13 focused gene validations, 13 renders and 13 history validations passed. Remaining advisories concern inherited GO0035999 labels, provider-use suggestions and process coverage; none licenses adding unsupported or redundant rows. `validation-warnings.json` preserves those messages. Core functions, module topology and reaction capacity did not change. No module, family, project or production-checker files are included in this release.

Reproduce the additive preservation check from the repository root:

```sh
uv run python analysis/module_audits/bacterial_methionine_cycle/review-followup/verify_followup.py
uv run ruff check analysis/module_audits/bacterial_methionine_cycle/review-followup
```

The default verifier is read-only. The `--write` option and `apply_followup.py` document initial receipt creation and manual adjudication; do not use them to refresh a frozen release. All receipt inputs are durable repository paths, with no ignored-cache-only dependency. The existing source notes, provider artifacts, GOA, UniProt and publication files remain unchanged.
