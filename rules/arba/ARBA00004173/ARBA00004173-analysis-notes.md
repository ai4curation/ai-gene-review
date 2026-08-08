# ARBA00004173 — reproducible rule statistics

Generated for the ARBA00004173 review. Regenerate with:

```
uv run python rules/arba/ARBA00004173/ARBA00004173-stats.py
```

(The sibling location rules ARBA00004496 and ARBA00004275 are fetched from
`https://rest.uniprot.org/arba/{id}.json` into /tmp; the cross-rule lines are
skipped if they are not cached.)

## 1. `just analyze-rule ARBA00004173` refuses to run

Quantitative pairwise-overlap analysis, the heatmap, `sync-rule-review-single`
and `render-rule` are all unavailable for this rule, because the analyser
declines rules with more than 12 condition sets:

```
ValueError: Rule ARBA00004173 has 1490 condition sets, which exceeds the maximum of 12. Analysis is skipped for rules with too many condition sets as they would require excessive UniProt API queries and take too long.
```

(raised at `src/ai_gene_review/etl/rule_analysis.py:1073`, via `examples/rule_analysis_demo.py`)

## 2. Structural statistics

```
condition_sets: 1490
statistics: {"reviewedProteinCount": 0, "unreviewedProteinCount": 536854}
condition_type_usage: {'taxon': 1490, 'FunFam id': 1359, 'InterPro id': 885, 'PANTHER id': 287}
single_funfam_only_sets: 693 (46.5%)
single_funfam_only_sets_with_no_resolved_label: 240
condition_set_shapes: {('FunFam id',): 693, ('FunFam id', 'FunFam id'): 180, ('InterPro id', 'InterPro id', 'PANTHER id'): 131, ('FunFam id', 'FunFam id', 'FunFam id'): 102, ('InterPro id', 'PANTHER id'): 99, ('InterPro id', 'InterPro id', 'InterPro id'): 99, ('InterPro id',): 81, ('InterPro id', 'InterPro id'): 67, ('PANTHER id',): 19, ('InterPro id', 'PANTHER id', 'PANTHER id'): 12, ('PANTHER id', 'PANTHER id'): 7}
sets_with_no_positive_taxon_condition: 1303 (87.4%)
sets_with_positive_taxon_condition: 187 ; distinct_clades: 140
sets_with_a_signature_label_matching_mitochondri*: 422 (28.3%)
distinct_InterPro_ids: 885 ; with_any_InterPro2GO_mapping: 493 ; mapped_to_GO:0005739: 35
distinct_signature_sets_within_rule: 1490 (of 1490 -> no exact duplicates)
signature_sets_shared_with_ARBA00004496_Cytoplasm: 139 (9.3%)
signature_sets_shared_with_ARBA00004275_Peroxisome: 19 (1.3%)
shared_with_both: 3
```

## 3. Notes on interpretation

- `sets_with_a_signature_label_matching_mitochondri*` is a **weak proxy** only: many
  genuinely mitochondrial families (e.g. TOM40, the small Tim chaperones) do not carry
  "mitochondri" in their InterPro/FunFam label, and 240 single-FunFam sets have no
  resolved label at all.
- The InterPro2GO counts are computed against the cached `rules/arba/_interpro2go.txt`.
  Only 35 of the 885 distinct InterPro entries used by this rule are mapped to
  GO:0005739 by InterPro curators. This is a **weak proxy**, and an argument from
  silence: absence of an InterPro2GO mapping is not a curatorial rejection. InterPro2GO
  maps a term only where it holds for *all* matches, its CC coverage is deliberately
  sparse, and this rule's condition sets are **conjunctive** — in the 131
  `InterPro+InterPro+PANTHER`, 99 `InterPro x3`, 99 `InterPro+PANTHER` and 67
  `InterPro x2` sets, no individual entry needs to imply mitochondrion for the *set*
  to. Only the 81 single-`InterPro` sets support a like-for-like comparison; that
  restricted statistic is not computed by the script below.
- `signature_sets_shared_with_*` compares the set of positive (non-taxon) signature
  values per condition set. An identical signature set appearing in two different
  location rules means one architecture is asserted to live in two compartments — which
  is **not by itself a defect**: mitochondrion/cytoplasm and mitochondrion/peroxisome
  co-annotation is common and often correct (fumarase, aconitase, several aaRSs,
  beta-oxidation enzymes). Treat these counts as an upper bound on sets warranting
  per-set triage, not as a defect count. Confirming collapse for a given set requires
  showing, as for CS779, that the shared signature requires a domain absent from the
  isoform the location comment is scoped to.

## 4. Regenerating the inputs

`ARBA00004173.json` (raw rule) and `ARBA00004173.enriched.json` (same rule with
InterPro/FunFam/PANTHER/taxon labels resolved) are **not committed** — `rules/.gitignore`
excludes `arba/*/*.json`. The review cites the raw rule by path as a source identifier,
but you must regenerate both locally before running the stats script (label resolution
takes roughly 15 minutes):

```
rm -f rules/arba/ARBA00004173/ARBA00004173-review.yaml   # init refuses to overwrite; restore afterwards
just init-rule-review ARBA00004173
uv run python rules/arba/ARBA00004173/ARBA00004173-stats.py
```

The cross-rule comparison lines additionally need the sibling location rules cached:

```
curl -s https://rest.uniprot.org/arba/ARBA00004496.json -o /tmp/ARBA00004496.json
curl -s https://rest.uniprot.org/arba/ARBA00004275.json -o /tmp/ARBA00004275.json
```
