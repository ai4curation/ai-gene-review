# PSEPK Lgt, LspA and Lnt consultation

This consultation owns three gene reviews, notes, derived renders, new generated gene histories and this audit directory. Module, family, project and other gene edits are outside its scope.

`baseline.yaml` freezes the twelve ordered annotation payloads and eighteen local protected files. `check_preservation.py` additionally verifies the root baseline's protected sources. `preservation-results.yaml` records the union of 66 unchanged sources, the single retained historical NEW row, the action ledger and three in-memory fault checks (row order, changed payload, deleted proposal). Source files are never modified by the checker.

The only action reversal is LspA proteolysis MARK_AS_OVER_ANNOTATED→ACCEPT. LspA core function uses active GO0009003 signal peptidase activity; its existing aspartyl-class annotation remains ACCEPT. No NEW row or retirement is added. The pre-existing lipoprotein-specific proposed MF remains a narrower proposal with corrected parent/rationale. Current GO responses and candidate identity responses are archived separately.

`evidence.md` documents assay organisms, source-access limits, current term definitions, participation reasoning and the PAINT leaf-availability limit. `RESULTS.md` describes the independent alignment and its sensitivity. Genuine OpenScientist research was reused; no invented provider output, experimental assay, PTN or loss event was added. Three genes absent from cached PAINT trees means lineage loss checks are unavailable, not verified loss-free.

Focused commands are listed in `focused-checks.yaml`; final outcomes and log hashes are in `validation-results.yaml`. Standard validations include schema, GO terms, references/quotes and best practices. Nonblocking warnings are documented: primary/curated source support was preferred to provider quotations, and GO0009003 core coverage does not trigger a redundant manufactured annotation. The code does not suppress validators.

Reproduce from the repository root:

```sh
uv run python analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation/check_preservation.py
uv run ruff check analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation
```

Sequence reproduction commands are in `RESULTS.md`. Final `handoff.yaml` freezes all released owned files plus newly acquired publication files, and separately hashes consumed external sources. It excludes itself from its own hash map. No commit, push or full-corpus validation was performed.
