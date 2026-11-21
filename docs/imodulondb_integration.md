# iModulonDB integration and evidence use

The KT2440 importer now reproduces **all 84 PRECISE321 modules** from pinned,
published iModulonDB exports. On 2026-11-05, all source member counts, measured
weights, module-specific thresholds and named matrix-column joins passed checks.
The [20-case calibration](../projects/P_PUTIDA/tf_census/calibration-review.md)
records biological evidence separately from the
[importer results](../projects/P_PUTIDA/tf_census/imodulon/calibration-results.md).
These are scoped assessments, not 20 completed GO reviews.

## Implementation and sources

Both [original](../scripts/compare_with_imodulondb.py) and
[v2](../scripts/compare_with_imodulondb_v2.py) entry points call the shared
[importer](../src/ai_gene_review/imodulondb.py). The
[configuration](../src/ai_gene_review/data/imodulondb_organisms.yaml) resolves
`PSEPK`, `p_putida` and `NCBITaxon:160488` to canonical `genes/PSEPK/` paths.

The adapter reads [SBRG/modulytics](https://github.com/SBRG/modulytics/tree/01af982cb604eef842df4209abe39b033d9067d5/organisms/p_putida/precise321)
at commit `01af982cb604eef842df4209abe39b033d9067d5`. Published per-module gene tables
are authoritative for membership. `M.csv` and `M_thresholds.csv` independently
check each member call and measured weight using source module IDs, including
when column order differs. The
[authors' supplement](https://github.com/SBRG/modulome_ppu/blob/f63a0dfab124ea9022123ce6227d132f39de0108/Manuscript_supp_data/Supplementary_Data.xlsx)
at commit `f63a0dfab124ea9022123ce6227d132f39de0108` supplies additional metrics and
regulator-to-locus mappings. Module statistics join by name, with count and
precision/recall consistency checks. The
[export manifest](../projects/P_PUTIDA/tf_census/imodulon/manifest.json) records
exact URLs, retrieval times, SHA-256 hashes, importer hash and validation results.

Legacy E. coli and B. subtilis configuration entries are explicitly unavailable:
their dataset labels and download routes were not verified to describe matching
datasets. They require separately versioned adapters before use; the command
returns an error rather than substituting a differently sized compendium.

## Commands and outputs

```bash
just list-imodulondb-organisms
just compare-imodulondb PSEPK BenR --output-dir /tmp/aigr-imodulondb
uv run python scripts/compare_with_imodulondb_v2.py PSEPK \
  --cache-dir .cache/imodulondb-repaired \
  --export-dataset projects/P_PUTIDA/tf_census/imodulon
uv run python projects/P_PUTIDA/calibrate_tf_imodulons.py
uv run pytest -q tests/test_imodulondb.py tests/test_putida_tf_census.py
```

Add `--offline` to reuse checked raw downloads without network requests. Cache
entries are keyed by URL and paired with checksum provenance; missing, incomplete
or altered entries fail explicitly. Cache location is controlled by `--cache-dir`.
The calibration command works entirely from the committed normalized export and
local review/metadata inputs; re-export if importer code has changed.

A single-gene command writes Markdown and JSON beneath
`<output-dir>/genes/PSEPK/<resolved-review-name-or-accession>/`. It reads
accession/taxon-matched review YAML for context and records input hashes, pending
rows and declared status. It does **not** run gene validation. Ambiguous aliases
fail with a request to use accession/locus; explicit unmatched accessions do not
fall back to names. All assigned modules and all memberships of the queried gene
are reported separately. Source regulator expressions retain their original text.

The dataset export contains `dataset.json`, `memberships.tsv` and `manifest.json`.
The calibration folder adds 20 report pairs, a summary and a checksum manifest.
Published reference-regulon precision/recall/F1 and p/q values remain source
statistics. Missing measurements are null, measured zero remains zero, and
membership-only input never receives invented rank-based weights. No structured
curated target set has been supplied: **target-overlap comparison is not performed**.

## Evidence interpretation

An iModulon is an expression component inferred by Independent Component
Analysis. The approach is described by [Rychel et al. (2021)](https://doi.org/10.1093/nar/gkaa810)
and the KT2440 compendium by [Lim et al. (2022)](https://doi.org/10.1016/j.ymben.2022.04.004).

- Membership supports expression association in sampled conditions; it does not
  establish TF identity, direct promoter regulation or pathway participation.
- A TF need not belong to the module it regulates. Missing assignments are not
  negative evidence of TF function; modules can be unassigned or multi-regulator.
- Weight magnitude is not binding probability, and ICA loading sign does not
  establish activation versus repression. Display cutoffs cannot define membership.
- Imported overlap scores measure agreement with the authors' reference regulon.
  Those labels and scores may reuse the same literature as another database and
  cannot independently validate it. Missing members are not grounds to remove
  literature-supported targets.
- Directness, regulatory sign and ligand binding each require their own evidence.
  A growth condition is not necessarily a TF ligand. No GO edits are generated.

## BenR correction and remaining work

The [corrected BenR summary](../projects/P_PUTIDA/tf_census/imodulon/reports/Q88I42.md)
has **10 published members**, at source threshold **0.12821891758582343**. The
[historical report](../genes/PSEPK/BenR/BenR-iModulonDB-comparison.md) listed 13 genes
above an arbitrary 0.05 cutoff. PP_3765, PP_3168 and PP_3792 are not published
BenR members. Its mechanistic claims require separate literature checks; even
the corrected membership set is not a direct-target list.

Next steps are full gene-level GO reviews, structured experimental regulatory
relationships and new comparisons against those curated target sets. The
[bacterial regulon workstream](../projects/TRANSCRIPTION_FACTORS/bacterial-regulon-evidence.md)
tracks these separately from the completed membership import.
