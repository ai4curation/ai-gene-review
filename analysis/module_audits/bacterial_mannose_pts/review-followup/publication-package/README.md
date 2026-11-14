# Scoped, checkout-ready publication package

This package separates the PR's scientific dependencies from the prior global source-pool immutability audit. The earlier 68,437-path closure and every earlier receipt remain unchanged. They describe a local verification event, not an instruction to stage all those files. `publication-input-map.json` is the current scoped dependency map: old PR inputs, current gene/family/module references, all released artifacts, their identified source dependencies, and this bounded source package. Entries whose only origin was the unrelated global preservation pool are not publication requirements. Their hashes remain preserved in the old pool proof.

The input map is not a staging list: existing tracked inputs stay where they are, while root stages only the reviewed modifications and new authorized audit artifacts. No unrelated or untracked publication is added merely because it existed during the earlier pool check. Four shared project metadata paths remain represented by the prior/current published-head provenance receipt rather than locked as current scientific inputs; root will freeze its own final metadata separately.

## Acquired-source treatment

`acquisition-mapping.json` accounts explicitly for all 32 ignored dependencies. Each original path, byte count and hash is retained. Four generated/factual provenance files have byte-identical durable copies: the original publication manifest, two fetch logs, and the small UniProt proteome query response. No full article, PDF, scraped full-text extract or publisher image is copied.

Scientific claims from the selected full articles are retained as bounded exact excerpts and interpretation records in `bounded-excerpts.json`, with acquisition URLs and original hashes in the mapping. The exact excerpts were independently checked against the existing acquired source bytes while preparing this package. They include the three review-article anchors, source-specific primary statements, and the updated UA159 amino-sugar assay result. Current review citations still resolve to the already committed normal publication caches or scoped source analyses; no curated citation is silently redirected.

`identity-observations.md` records the small primary Figure1 locus observation, independently re-inspected, and the limited CECT strain-alias observation. Already committed official identity JSON/EMBL records and the U28163 partial-IID sequence preserve the reproducible sequence checks. The original image/catalogue are not required for the current computational closure. No experimental full-construct identity is inferred from a figure or strain alias.

Six failed/superseded discovery captures (2008 failed page, 2020 failed page, and unused 2019 chapter, each raw/extracted pair) remain historical acquisition observations. They are not current scientific evidence dependencies. Their exact hashes and access status remain in the original acquisition ledger and the new map. The old raw files are untouched.

No license is asserted for the articles. Bounded excerpts do not constitute byte-identical replacements for full articles. Full-source reacquisition can change web extraction bytes; a changed retrieval must receive new provenance rather than overwrite the recorded old hash. Current checkout checks validate the preserved scoped evidence and its provenance, not an absent full paper.

## Reproduction without ignored files

From the repository root:

```sh
uv run python analysis/module_audits/bacterial_mannose_pts/review-followup/publication-package/check_package.py --deny-ignored-reads
uv run ruff check analysis/module_audits/bacterial_mannose_pts/review-followup/publication-package/check_package.py
```

The first command actively prohibits reads beneath the repository's `.cache` directory. It validates the scoped dependency hashes, 93 ordered rows/two active historical NEW rows, 114 current quotations, the 15 bounded excerpts' ledger correspondence, all 32 source dispositions, and the unchanged 60/13/9 capacity expectations. It imports old reusable functions without calling mutating old entry points. It does not run old local-acquisition/global-pool checkers, which remain historical proofs.

An optional local provenance audit, only where the original ignored captures still exist, checks their original bytes and rechecks every excerpt:

```sh
uv run python analysis/module_audits/bacterial_mannose_pts/review-followup/publication-package/check_package.py --verify-local-acquisitions
```

The current full-corpus validation has not run. The exact new-run command/log paths remain in the prior `final-closure/README.md`; root must freeze the committed head and scoped publication manifest before recording that run. Nothing in this package converts the previous full-corpus result into a result for the current follow-up.
