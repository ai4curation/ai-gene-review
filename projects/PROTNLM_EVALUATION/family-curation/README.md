---
title: "Reproducing the ProtNLM family-curation coverage"
autolink_gene_symbols: false
---

# Reproducing the family-curation coverage

[Overview](../family-curation.md) · [Gene index](gene-index.md) · [Family index](family-index.md)

The curated records live in `interpro/panther/PTHR*/PTHR*-review.yaml`. This directory holds the scoped input snapshots, source extracts, index builders and validation reports. The scripts reproduce retrieval, joins and reports; they do not generate biological judgments.

From the repository root:

```bash
UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/family-curation/build_mapping.py
UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/family-curation/build_index.py
UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/family-curation/unassigned-checks.py
UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/family-curation/validate_families.py
```

- `scope.csv` freezes 288 cohort memberships, representing 282 distinct accessions. `build_scope.py` can rebuild selection from the explicit cohort files and available gene-review identifiers; compare its output before using it with newer cohorts.
- `uniprot-records.jsonl.gz` preserves exact-accession responses, request URLs, retrieval times and errors. `uniprot-retries.jsonl.gz` resolves six failed initial requests without altering the initial snapshot. All 282 records have successful responses; no accession redirects were silently substituted.
- `baseline-membership.csv` preserves the applicable membership-index observations from the start of this pass. `build_mapping.py` uses that frozen baseline and the successful UniProt responses. No gene-symbol inference or canonical bridge is used to create an exact-record PANTHER assignment.
- `fetch_records.py` refuses to overwrite a snapshot. Use a new dated bundle for a refresh. `fetch_family_sources.py` preserves cached PANTHER metadata and raw integrated InterPro responses under `family-sources/`; three integrated entries return HTTP 410. Such responses are absence of usable source content, not negative biological evidence.
- `mapping.csv` and `family-groups.json` cover the 210 exact-assignment families. `additional-context-families.json` records the additional SPCS2 family separately. `coverage.csv` joins every exact input to either a family review or an individual domain/family assessment.
- `unmapped-sources.jsonl.gz`, `unassigned-results.json` and `unassigned-checks.py` preserve independent checks of the 18 inputs without exact-record PANTHER assignment, including shared MOD identifiers and sequence relationships.
- Family source extracts retain reviewed status, evidence codes and generated-description flags. `extract_root_sources.py` regenerates one batch of deterministic source extracts. `dossiers/` contains working source leads, which are not independent experimental validation. Raw sources remain available for checking the excerpts.
- `decisions.jsonl` and `root-term-decisions.json` mirror the final root-batch family judgments. The authored family YAMLs are authoritative; `assignments.json` and the batch result files delimit work and checks.
- `membership-update.json`, the batch-C result file and `additional-context-families.json` document additions to the shared accession-to-PANTHER index. Only observed exact-record assignments were added. Canonical family assignments were not projected onto short benchmark inputs.
- `validation-all.json` reports schema, family membership, anchored residues, source paths and literal quotations for all 211 reviews. `validation-go.json` and its frozen QuickGO responses cover ontology identifiers in the 210 exact-assignment families. `PTHR13085-go.json` checks the additional SPCS2 term. `family-gene-crosscheck.txt` records comparison with the available gene-review corpus.

Family summaries and term assessments describe the current biological interpretation. Curation-session provenance is recorded separately under `history/other/PTHR*/` and `history/projects/PROTNLM_EVALUATION/`.
