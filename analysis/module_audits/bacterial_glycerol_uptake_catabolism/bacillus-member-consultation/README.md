# Bacillus member consultation — 2026-11-07

Reviewed BACSU GlpF/P18156, GlpK/P18157 and GlpD/P18158. The 27 original annotation payloads and their order are unchanged: 18 ACCEPT, 8 MODIFY, 1 UNDECIDED; no historical or active NEW rows. The baseline's six raw files are byte-identical. The reproducible verifier also protects eight relevant publication caches, including four publications fetched normally during this consultation.

Native Bacillus evidence establishes the glycerol kinase/G3P-dehydrogenase route. The 1974 primary experiment uses tetrazolium reduction and a 17,000×g supernatant: it does not directly establish physiological quinone specificity or soluble localization. Quinone activity remains a reviewed-target/PAINT synthesis. SF35 membership alone does not prove acceptor specificity, a membrane location, or a GlpABC heterotrimer. GlpD's membrane row is UNDECIDED; broad cytoplasm is retained without refinement. The GlpF primary paper establishes its assignment through hydropathy, family conservation, homolog comparison and operon structure, not direct target conductance. GlpK ATP binding is supported by its ATP substrate requirement; G3P metabolism is retained because this kinase produces G3P, rather than degrading it.

Primary full-text reading/provenance:
- `genes/BACSU/glpD/glpD-source-analysis/primary-physiology-reading.md`
- `genes/BACSU/glpF/glpF-source-analysis/PMID8436953-reading.md`

The shared publication files remain machine-fetched. PMID8436953 and PMID4368746 were read externally in full despite abstract-only caches, so their review metadata does not falsely mark full text unavailable. The other primary papers used only at abstract level retain that limitation.

Three real Falcon attempts failed with HTTP 403 authentication errors. No provider-labelled research was fabricated. Three PAINT checks found no IRD/IKR losses; these checks do not reconstruct ancestral node placement. Standard record-section backfill added 71 fields; its second pass made no changes. All three focused validations passed, all reviews rendered, and matching histories were generated with `just new-history` and validated. No full validation, commit, push or shared module/family edits were performed by this consultation.

Reproduce preservation and inference-boundary checks from repository root:

```sh
uv run python analysis/module_audits/bacterial_glycerol_uptake_catabolism/bacillus-member-consultation/verify.py
```

Full logs and exact handoff hashes are in `.cache/module-audit-logs/glycerol-20261107/bacillus-review/`. The committed proof captures the source assertions separately from newly authored review judgments and evidence metadata.
