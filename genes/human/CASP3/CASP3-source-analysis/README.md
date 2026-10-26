# CASP3/Casp3 transfer evidence audit for PR5558

This audit concerns exactly 37 previously templated UNDECIDED rows: 25 in human CASP3 and 12 in mouse Casp3. It does not recreate GOA or infer functions from annotation counts.

- `transfer-evidence-audit.tsv` records each manually assessed claim, donor provenance, primary citation, inspected access status, action and rationale.
- `donor-trace.json` retains seed WITH/FROM provenance. The human legacy review lacked some supporting-entity fields, so the normal TSV was consulted **only for donor tracing**. No machine row was rewritten, and relationship qualifiers were ignored.
- `rat-annotation-provenance.json` is a filtered live QuickGO response for rat Casp3/P55213. It identifies donor references; it is annotation state, never independent evidence for function. The mouse donor papers were traced through the existing mouse review and read directly.
- `publication-access.json` identifies inspected normal source caches, full-text availability and hashes. All functional or uncertainty support in the gene reviews cites those primary papers directly. No review cites GOA or the QuickGO annotation response as functional support.
- `go-definitions.json` contains the exact QuickGO term definitions used to distinguish stimulus responses, axon bundling, swimming locomotion, steady-state T-cell numbers and anterior neural-fold fusion. `cobalt-response-ancestry.json` verifies that the cobalt-response refinement is a descendant of response to metal ion.

Run `uv run python genes/human/CASP3/CASP3-source-analysis/trace_donors.py` from the repository root to regenerate donor tracing. Live annotation provenance may change; the fixed TSV records the manual audit's original scope. The script does not generate biological review decisions.

The 37 outcomes are 26 KEEP_AS_NON_CORE, one MODIFY, one MARK_AS_OVER_ANNOTATED and nine precisely UNDECIDED. A stimulus-response term can include altered enzyme production or expression without asserting receptor activity or catalytic activation. Cellular-component transfer was assessed separately from behavior or development. The only over-annotation judgment is the mouse swimming-behavior transfer from an IGF1-treated-rat cognitive assay that measured caspase-3 as a marker; no general lack of neuronal function is asserted.

The unresolved claims are not generic placeholders: the audit records each exact missing assay or physiological distinction. Full text resolves the Casp3 hith2 genotype and encephalocele phenotype but not anterior-fold fusion specifically. Independent full T-cell anergy experiments support restraint of activated T-cell responses, while their stimulus-dependent design does not establish steady-state T-cell population homeostasis. Neither a B-cell-focused abstract nor a caspase-6-focused abstract is treated as proof that CASP3 was not also tested in the complete article.
