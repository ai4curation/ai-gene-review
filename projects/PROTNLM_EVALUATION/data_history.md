# ProtNLM2 Data Source History

## REST API (current, recommended)

Predictions are fetched from the UniProt REST API endpoint `https://rest.uniprot.org/uniprotkb/protnlm/{accession}`. The canonical accession list (26,856 entries) is published at the [FTP site](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv).

```bash
python projects/PROTNLM_EVALUATION/fetch_protnlm_api.py          # fetch all + convert to TSVs
python projects/PROTNLM_EVALUATION/fetch_protnlm_api.py --resume  # resume interrupted fetch
python projects/PROTNLM_EVALUATION/fetch_protnlm_api.py --convert-only  # re-convert existing JSONL
```

The API returns JSON with evidence inline per prediction. The fetch script saves raw JSONL (`protnlm_api.jsonl`) for reproducibility and converts to 3 TSV files (entries, predictions, evidence).

## Pre-release XML (historical)

The original exploratory analysis used a pre-release XML export (`post-processed-2026_02_28k.xml`, 28,553 entries) parsed by `parse_protnlm_xml.py`. This included 1,697 entries subsequently removed during quality filtering (64.5% Swiss-Prot entries excluded from the TrEMBL-only public pilot, plus QC-filtered TrEMBL entries). The API serves the same predictions in a cleaner format.

## Dataset statistics

**Current public release** (API fetched 2026-10-19; counted by
[`build_benchmark_funnel.py`](build_benchmark_funnel.py), stored in
[`benchmark-funnel.json`](benchmark-funnel.json)): the published list has 26,856 accessions in
416 taxa. The API serves 26,855 of them (A0A8K0EP25 returns 404). 10,268 records carry GO
predictions or function text, 6,291 of them GO predictions; the rest carry only names,
locations or keywords. Off the list, the API also serves records from the pre-release export:
all 28 *S. pombe* entries of the [pombe cohorts](pombe.md) and all 29 off-list fly accessions
identified for [FLY_NEXT20](fly-next20.md) (9 of which that cohort uses) return predictions. This
is not an exhaustive census of what the API serves.

The table below describes the **pre-release XML export** (28,553 entries) used in the first
exploratory analysis. It is kept for provenance and does not describe the public release.

| Type | Count | Description |
|------|-------|-------------|
| Protein name | 28,553 | Every entry gets a predicted name (22,467 recommended, 6,086 submitted) |
| GO terms | 6,833 entries | GO annotations derived from model predictions |
| Subcellular location | 13,690 entries | Predicted localization |
| Function comment | 5,438 entries | Free-text functional description |
| Name only | 8,690 entries | Only protein name predicted, no GO/location/function |

## Evidencer corroboration provenance

Each prediction has a model score (0–1, threshold 0.05) and post-hoc corroboration from the Evidencer:

- **domain** (9,950): Domain architecture match
- **GO** (8,727): Direct GO term prediction
- **PANTHER** (4,190): PANTHER family/subfamily match
- **keyword** (4,111): UniProt keyword match
- **InterPro** (1,022): InterPro family match
- **recommended_protein_name** (543): Name transferred from characterized homolog
- Plus many smaller categories (Pfam, SUPFAM, Gene3D, CDD, etc.)

## TSV files

| File | Description |
|------|-------------|
| `entries.tsv` | One row per entry (accession, name, prediction counts) |
| `predictions.tsv` | One row per GO/function/location prediction |
| `evidence.tsv` | One row per evidence block (scores, provenance) |
| `taxonomy.tsv` | Accession -> species mapping from UniProt |

## Change log

### 2026-10-29 — narrative rescore and snapshot refresh

- **Snapshot.** The ProtNLM2 review snapshot moves to `ac95c69686` (2026-10-29), the merge of the
  narrative rescore (#5718).
- **Narratives.** All 65 narrative reviews were rescored under the gene-level novelty and
  product-level correctness rules, with novelty judged against GO terms (in GOA or asserted by the
  curated review) and not review prose. Over the 57 indexed function narratives, category
  presence is COR 1→4, CNN 19→24, LSP 1→2, SUPPORTED 8→1, UNC 25→26, NPI 14→16 and PLI 13.
  `narrative-review-index.yaml` carries the new categories and hashes, a revised HORSE/SIRT5 note and
  a DARS2/GPAM/HSPA4 note.
- **GO claims.** Two sidecars move LSP→CNN (NCU04637 cytoplasm, rfc3 DNA replication), because GOA
  carries the exact term: CNN 46→48 and LSP 85→83 over the same 288 claims.

### 2026-10-24 — separate review snapshot and full rescore

- **Snapshot.** ProtNLM2 now pins its own review snapshot in `review-snapshot.yaml` (commit
  `1ca4af83c6`, 2026-10-24); the BioReason benchmark stays on its 2026-09-27 snapshot.
  `just refresh-protnlm-snapshot` regenerates the summary, COR entailment, OpenScientist
  reconciliation, DONKEY40 comparison and funnel from that commit.
- **Rescore.** All cohort sidecars were re-reviewed with product-level correctness and gene-level
  novelty. In-snapshot counts over 288 claims: COR 35, CNN 46, LSP 85, UNC 78, NPI 42, PLI 2.
- **Funnel.** Added `build_benchmark_funnel.py refresh-reviews`, which recomputes only the
  review-derived fields so a new snapshot does not need a fresh API dump; the UniProt and API counts
  stay as committed.
- **Entailment.** `cor-goa-entailment.tsv` gains a `descendant_terms` column; none of the 35 COR
  calls is entailed by an existing annotation and 4 are more specific than one.
- **DONKEY40.** Both comparison tables were regenerated; the ProtNLM2 and TreeGrafter sections of
  `donkey40.md` and `../TREEGRAFTER.md` were recounted from them.

### 2026-10-20 — provenance figures: review fixes

- The cohort figure now lists all ten cohorts, including the queued FLY location/keyword,
  FLY_NEXT20 and POMBE remaining-8 tiers, so in-snapshot memberships (248) reconcile with the
  242 distinct targets. Cohort wording moved to `benchmark-cohorts.yaml`; `compute` fails if
  `benchmark-summary.json` has a cohort the sidecar does not describe.
- The funnel no longer draws the targets as nested inside the GO/function set: 86 of the 242
  targets lie outside it (37 off the list, 28 *S. pombe* and 9 fly; 49 listed with only names,
  locations or keywords). `benchmark-funnel.json` records the breakdown, the pilot counts of the
  taxa named in the prose (`pilot_taxa`), and the API fetch date (`api_fetched`).
- REP is included in the outcome categories, and unknown assessment codes raise.
- `fetch_protnlm_api.py` writes each chunk of results before submitting the next, so a long
  fetch streams to disk and `--resume` works after an interruption.
- `tests/test_protnlm_benchmark_funnel.py` checks that the committed SVGs match the renderer
  and that cohort counts reconcile.
- `figures/overclaim-cases.svg` is hand-drawn rather than generated. It is used by the project
  brief and the slide deck; its verdicts (A0A3B6GK97, F6LAX4, A0A3B6RKV1) were re-checked
  against the prediction reviews on 2026-10-20.

### 2026-10-19 — benchmark provenance figures

- Added `build_benchmark_funnel.py`. `compute` counts each stage from UniProtKB (2026_03) to
  the pilot list, the pilot records with GO/function output (from a full API fetch) and our
  cohorts, and writes `benchmark-funnel.json`; `render` draws `figures/benchmark-funnel.svg`,
  `figures/benchmark-cohorts.svg` and `figures/benchmark-outcomes.svg` from that file.
- `fetch_protnlm_api.py` gained `--workers` (default 8). Requests take about 0.7 s each, so the
  serial fetch ran at about 1.4 per second rather than the intended 10.
- The project page, the new HTML slide deck (linked from the page's manifest) and the project
  brief now open with these figures. The XML-era Marp deck moved to `archive/`.

### 2026-10-01 — rebase onto the frozen review snapshot

After rebasing the 2026-09-27 changes onto main, which pins benchmark counts to
`review_snapshot_commit` and had folded OpenScientist audits into the ProtNLM reviews:

- `build_benchmark_summary.py` additions (assessed-target counts, per-cohort table, cached-GOA
  dates) were ported to the snapshot `SourceTree` API, so they are computed at the same commit as
  the other counts. ARGO-50 now reads 18 COR, 2 PLI and 10 NPI of 77 at that snapshot.
- `cor_goa_entailment.py` now reads reviews and GOA at the snapshot too: 3 of 52 COR calls are
  entailed by an existing annotation.
- The OpenScientist reconciliation was regenerated against the current reviews: 13 agree, 5 differ
  within the same polarity group, 12 are decided differently and 1 has no verdict. 30 of the 31
  terms now cite the investigation. Eight rationale excerpts that no longer appear verbatim in the
  revised reviews were dropped from `override-rationale.tsv`.
- Horse and fly selection pages updated: five horse and three fly reviews now cite their reports.

### 2026-09-27 — reporting fixes from the function-prediction review

These changes follow the ProtNLM2 section of
[REVIEW-2026-09-26](../FUNCTION_PREDICTION_EVALUATION/REVIEW-2026-09-26.md). No assessment in any
`*-protnlm-predictions-review.yaml` was changed.

- **OpenScientist reconciliation.** Added `reconcile_openscientist.py`, a transcription of the
  adjudication report's per-term verdicts (`openscientist-reconciliation/openscientist-verdicts.tsv`),
  and verbatim rationale excerpts from the current YAMLs (`override-rationale.tsv`). The generated
  output is `openscientist-reconciliation.md`/`.tsv`. Of 31 terms in 21 genes: 8 agree, 4 differ
  within the same polarity group, 18 are overridden by the current YAML, and 1 has no verdict.
  The adjudication report's "wired into per-gene YAMLs" statement is corrected, and the main page
  no longer says OpenScientist "carries substantial weight".
- **Per-cohort assessments.** `build_benchmark_summary.py` now also reports:
  - assessed vs unreviewed targets: 186 of 242 assessed, 56 with no review;
  - per-cohort category counts with COR share;
  - median cached GOA rows per target;
  - the latest-annotation-date distribution of the cached GOA files.
- **COR entailment check.** Added `cor_goa_entailment.py`. It uses the pinned go-basic 2026-03-25
  release through `ai_gene_review.bioreason_ontology`. It checks all 53 COR calls against the
  target's cached GOA with is_a/part_of closure. Three calls (HORSE/WDPCP) are generalisations of
  an existing annotation.
- **Archive.** Moved `generate_prediction_reviews.py` and `bench50_novel_review.csv` to `archive/`
  as superseded. The script now refuses to run.
- **Other fixes.**
  - Corrected stale table descriptions.
  - Added the PLI/NPI rule and the known UBE2F/NCU04302 inconsistency.
  - Added the fragment caveat and the reference-independence notes.
  - Updated the horse and fly OpenScientist selection pages: 8/8 horse and 3/4 fly reports have
    been downloaded; CG5611 finished without a report.
  - Marked the slide deck as a dated snapshot.
