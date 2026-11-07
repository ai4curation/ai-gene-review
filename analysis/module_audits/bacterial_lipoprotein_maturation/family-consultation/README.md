# Lipoprotein family audit

Scope: PTHR30589, PTHR33695 and PTHR38686 only. The eight released gene reviews, module, project and original source caches remain unchanged.

- `evidence.md`: manual source findings and scientific boundaries.
- `tree-inspection.json`: actual resolved ancestral-node and representative coverage, with cached-tree hashes.
- `ontology.json`: official term definitions and independent endopeptidase ancestor checks.
- `official-labels.json`: exact family/subfamily names checked against PANTHER's ontology.
- `fusion-classification.json`, `O53493.txt`, `A0QZ13.txt`, `uniprot-provenance.json`: source-specific fusion versus standalone-domain evidence.
- `baseline.json`, `check_preservation.py`, `preservation-results.json`: original full review snapshots, ordered assertion payloads and immutable input proof. Run `uv run python analysis/module_audits/bacterial_lipoprotein_maturation/family-consultation/check_preservation.py` from the repository root.
- `gene-crosscheck.json`: eight frozen core activities checked against supported family term scopes. The repository's standard conflict checker separately found no applicable negative/scope conflicts; its zero-case count is not presented as eight experimental validations.
- `history-paths.json`: helper-created append-only records and start marker.
- `validation-results.json`: focused check results and limitations.

The added signal-peptidase family assessment is a manual ontology-specific refinement, not a new PAINT assertion. All ten original PAINT node/term/evidence/date/seed payloads remain unchanged. The Lnt amidase scope changes from an unjustified blanket negative to unresolved; three unresolved cross-domain nodes remain unresolved. No universal cross-species rescue or fusion-derived catalytic capacity is asserted.
