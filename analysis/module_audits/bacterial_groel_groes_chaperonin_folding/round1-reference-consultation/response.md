# PR 6164: PSEPK reference consultation

The two established citation corrections are restored using `reference_review.replacement` on the original wrong PMID, as required by `docs/reference_curation.md`: groEL 38987603 → 39169181 and groES 38092042 → 38064510. Both original papers are real, unrelated publications, so neither is marked invalid. Existing biological evidence continues to cite the intended paper. Original annotation reference fields are unchanged.

`historical-correction-evidence.json` preserves the pre-audit correction notes from `6332a1d51e^`. `reference-identities.json` contains the corresponding NCBI EFetch article titles and publication DOIs, checked 2026-11-07. The complete EFetch response is cached in `.cache/module-audit-logs/groel-20261107/round1/reference-consultation/pubmed-identity.xml`. This establishes intended-paper identity rather than inferring a replacement from title similarity.

GroEL's standalone description now explains the double-ring tetradecamer, apical client capture, equatorial ATP binding/hydrolysis and GroES-dependent encapsulation/release. Its mechanistic core description is similarly direct. Notes retain the distinction between target curated HAMAP assignment and comparative E. coli structural experiments. No unsupported KT2440-specific client spectrum or RpoH regulation was added.

PSEPK GroES now names GO:1990220 as its core complex. Target UniProt's curated FUNCTION explicitly describes binding/capping the GroEL ring; this supports complex participation independently of other genes' review shapes. The official QuickGO definition is archived in `GO1990220.json`. Existing contribution to ATP-dependent folding remains distinct from independent ATPase activity. BACSU and MYCTU GroES already carry `contributes_to_molecular_function: GO:0140662`, so that part of suggestion 7 needs no correction. No other genes were edited.

## Checks and remaining advisories

Both focused gene validations, both renders, both generated history validations, and Ruff pass. Scoped standard UniProt record-section backfill requires no changes. GroEL retains the unused-provider advisory; GroES retains it and has the expected complex-without-existing-annotation advisory. No NEW row was added merely to suppress the latter. The rendered HTML files are generated alongside the reviews as ignored HTML and are included by hash in the cache handoff.

Run `uv run python analysis/module_audits/bacterial_groel_groes_chaperonin_folding/round1-reference-consultation/verify.py` from this checkout. The checker compares the frozen baseline to Git HEAD 04e7322f4c2f032c8f88737ba78bf3197563f2ba and requires equality of all 11 complete ordered annotation rows (including every review/action), all pre-existing reference objects and all functional fields except the explicitly permitted GroES complex relationship. It permits only the two documented new provenance reference objects and GroEL prose updates. Historical NEW: 0; active NEW: 0. All protected raw/provider/publication hashes remain unchanged. The receipt lists them individually.

No annotation action-ledger correction is needed: groEL has five ACCEPT actions; groES has four ACCEPT and two UNDECIDED actions, exactly as before. Other PR review requests belong to the parent/other consultation. No full-corpus validation, commit or push was performed.
