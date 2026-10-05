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

## Comparing curation revisions

Default scores change when annotations move into or out of applicable action
sets. In particular, UNDECIDED leaves the default support denominator. Report
these scores as contextual completeness, not as an improvement in evidence alone.

For a comparison that keeps these decisions in scope, use:

```bash
uv run python scripts/compare_compliance.py \
  --base 429666d2e90edbbab38886f6a53d279b9a8280ab \
  --output docs/arath-compliance-comparison.md
```

The script defaults to the eleven ARATH genes re-reviewed in PR2996; override
with `--genes SYMBOL ...`. Both baseline git YAMLs and current working-tree YAMLs
use the same current schema, analyzer and config. An optional `--baseline-json`
compares the recalculated contextual baseline with a historical CLI report;
historical scores never supply the inclusive denominator. The Markdown and
companion JSON contain contextual and inclusive scores, weighted numerators and
denominators, evidence-rule counts, exact policies, and input hashes.

The inclusive sensitivity policy selects **all conclusive actions and UNDECIDED**
for each evidence rule, including ACCEPT and KEEP_AS_NON_CORE for inference
support. Consequently action changes within this set cannot remove evidence
opportunities. IEA still uses sourced rationale rather than a quotation check.
PENDING and missing reviews remain outside both action-conditioned support
rules. This policy is for comparisons; it does not change the default treatment
of routine IEA acceptance or demand a citation for every unresolved decision.

This controls action applicability, not every source of score variation. Changes
to references, core functions and other recommended fields, and added or deleted
annotations, can change the scores and denominators. Do not describe the resulting
delta as the fraction caused by added evidence. The [PR2996 comparison](arath-compliance-comparison.md)
provides the bounded before/after example.

`recommended_slots` in JSON lists schema recommendations encountered before
policy exclusions. Plugin names appear in `summary_by_slot` and aggregated
metrics, but are not schema recommendation metadata.
