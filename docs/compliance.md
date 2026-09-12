# Evidence-aware compliance

`just compliance-all` writes individual gaps to `reports/compliance-all.tsv`
and per-file scores to `reports/compliance-summary.tsv`. `just compliance-dashboard`
uses the same policy and reports to generate an HTML dashboard.

The policy is [conf/qc_config.yaml](../conf/qc_config.yaml), a symlink to the
packaged default at `src/ai_gene_review/schema/qc_config.yaml`. Edit either path.
The CLI uses this packaged default even when run outside the repository.

```bash
uv run ai-gene-review compliance genes/ARATH/EIN2/EIN2-ai-review.yaml \
  --config conf/qc_config.yaml --json-output /tmp/ein2-qc.json
```

## What earns credit

The default policy replaces unconditional annotation `supported_by` checks with
two contextual metrics. Each applicable annotation contributes one opportunity:

| Metric | Applies to | Credit |
| --- | --- | --- |
| `literature_support` | Conclusive experimental/TAS decisions, including MODIFY, REMOVE and non-core decisions | At least one PMID/DOI support item with nonblank `supporting_text` or `supporting_text_fulltext` |
| `inference_support` | Corrective or NEW inferred annotations, including IEA/IBA | Nonblank `review.reason` plus a support reference, an `additional_reference_ids` entry, or a propagation source with `source_id` |

See the YAML for the exact evidence-code and action lists. PENDING and UNDECIDED
are excluded from these metrics; an IEA ACCEPT needs no quotation. Multiple
quotes on one annotation earn no additional credit. An inference's
`original_reference_id` alone does not count as a source supporting the reviewer's
correction. Literature from a different paper can support a decision; it need
not quote the original annotation reference.

Quotes are a recommendation, not a prerequisite for a defensible decision.
Inaccessible papers may leave advisory gaps; do not fabricate snippets or reverse
a correct decision to increase the score. Coverage is not a measure of truth:
this command checks presence, while `just validate` checks reference identifiers,
titles and verifiable quotes. Full-text-only excerpts earn presence credit but
remain outside cached-text verification. Scientific relevance requires review.

Other recommended fields, including core-function evidence, retain schema checks.
The traversal follows nested YAML objects using induced class-specific LinkML
slots, including implicit inlining. This fixes an upstream traversal limitation
that skipped `existing_annotations` and `core_functions`; scores therefore are
not directly comparable to historical compliance output. Root fields now
participate in weighted scoring as well as list fields.

## Configuration and extension

The weight/threshold vocabulary follows dismech and `linkml-data-qc`:
`default_weight`, `default_min_compliance`, `slots`, and `paths`. Exact normalized
paths override slot settings, which override defaults. List indices become `[]`;
root slot paths use `(root).slot_name`.

```yaml
paths:
  existing_annotations[].review.literature_support:
    weight: 3.0
    min_compliance: 80.0
annotation_rules:
  literature_support:
    evidence_types: [EXP, IDA, IMP]
    actions: [MODIFY, REMOVE]
    support: literature_quote
excluded_paths:
  - existing_annotations[].review.supported_by
  - existing_annotations[].review.supported_by[].**
```

A supplied config replaces the default policy; it is not merged into it. Start
by copying the default. `annotation_rules` can add named metrics or adjust their
applicability without Python changes. Available support modes are
`literature_quote` and `sourced_rationale`. Overlapping rules intentionally count
as separate metrics, so use distinct applicability sets unless that is desired.
`excluded_paths` removes raw schema checks by exact slot path or subtree (`.**`)
before computed checks run. It affects both the numerator and denominator;
setting a weight to zero affects only weighted scoring.

For checks that need other logic, implement `QCMetricPlugin.evaluate(data, config)`
in `ai_gene_review.compliance` style and pass plugins to `GeneComplianceAnalyzer`.
Plugins return per-instance `PathCompliance` records with `SlotCompliance`
entries. Omit inapplicable instances entirely and use unique metric names.
The engine recomputes details, aggregates, slot summaries, global and weighted
scores, and threshold violations from the combined checks. These standard
`linkml-data-qc` reports feed both JSON output and the existing dashboard renderer.

`--schema-only` disables contextual policy for inspecting schema recommendations
(with corrected traversal). `--summary-output`, `--json-output`, and
`--dashboard-dir` expose scores and denominators; default TSV output remains a
list of gaps. Threshold misses are advisory unless `--fail-on-threshold` is
supplied, in which case they produce exit status 1. Default thresholds are null.
