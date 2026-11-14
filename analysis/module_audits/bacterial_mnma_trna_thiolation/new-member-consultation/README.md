# Eleven new MnmA-panel reviews

All eleven reviews are COMPLETE. All 93 imported rows retain their exact ordered source payloads and qualifiers. No row was added, deleted or retired. Four bare protein-binding claims have the policy action REMOVE, while the rows themselves remain present.

The final decisions are 63 ACCEPT, 23 MODIFY, four REMOVE, one KEEP_AS_NON_CORE, one MARK_AS_OVER_ANNOTATED and one UNDECIDED. `action-ledger.json` records each row; `evidence.md` explains source-specific biology and access limits. `preservation-and-evidence.json` records protected-byte, quote and scientific-boundary checks with a durable source dependency map.

Eleven gene validations, eleven renders and eleven helper-generated histories pass. PAINT checks report no loss for the eight resolved E. coli/Bacillus targets; the three Thermus targets are absent from their cached reference trees and therefore unresolved. The only remaining validation advisories concern absent annotation-block coverage of donor-core process/location terms. No NEW row was manufactured to silence these six advisories.

All eleven genuine Falcon attempts failed with HTTP 403. Exact commands/errors remain in the per-gene logs, which contain public gene context and no detected authentication secrets. Manual primary/review evidence and official identity bridges were used. The original publication caches, seed sources and provider artifacts were not modified.

Recheck the released state without rewriting its receipt:

```sh
uv run python analysis/module_audits/bacterial_mnma_trna_thiolation/new-member-consultation/verify.py --check-only
uv run ruff check analysis/module_audits/bacterial_mnma_trna_thiolation/new-member-consultation/*.py
```

`curate.py` records explicit manual decisions and can reproduce the gene edits in an isolated copy; it is not an inference engine or an independent assay oracle. Its identical-output rerun is recorded in `determinism.json`. Do not rerun the mutation script on released files during downstream work. Prior `*-validation.log` files are the initial check; final focused logs are `*-validate.log`, and `focused-results.json` is authoritative for the final validation/render/history run.

Scope: the eleven new gene folders, their eleven new history records and this consultation only. No existing PSEPK or IscS review, module, family, project, publication cache, previous receipt or full-corpus validation was changed or run. Ownership is released with the immutable `handoff.json`.
