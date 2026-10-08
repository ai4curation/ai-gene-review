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
