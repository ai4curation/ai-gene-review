# Frozen fly ProtNLM census

The [fly project page](../fly.md) describes the review strategy. The complete
published Drosophila melanogaster subset contains 94 protein records mapping to
94 distinct FlyBase genes. All 41 records with GO or function-text predictions
form the first review cohort; 29 location/keyword-only records form a separate
tier, and 24 name-only records remain in the census.

## Inputs and provenance

- [accessions.tsv](accessions.tsv): every row with `Organism (ID) = 7227` from the
  official ProtNLM2 accession list; original columns and values retained.
- [predictions.jsonl.gz](predictions.jsonl.gz): all 94 original prediction API
  responses, including scores and donor-match metadata.
- [uniprot.jsonl.gz](uniprot.jsonl.gz): all 94 ordinary UniProt API responses,
  including current sequence, entry audit, annotation provenance and identifiers.
- [flybase-identifiers.tsv.gz](flybase-identifiers.tsv.gz): original FlyBase
  FB2026_02 gene-symbol/annotation-ID table. UniProt cross-references resolve through
  primary and secondary FlyBase IDs to current Dmel symbols. This corrects stale
  UniProt symbol fields such as `CG10551` (current `CG31099`) and the numeric
  `28557659` (current `CG5565`), without modifying source records.
- [manifest.json](manifest.json): retrieval time, source URLs, selection rule,
  response counts and SHA-256 checksums. The JSONL checksums refer to decompressed
  bytes. The FlyBase checksum refers to the original downloaded gzip bytes.

Current sequences are not proven prediction-time inputs. Placeholder prediction
API audit dates cannot establish release timing or training-set membership.
Gene-level identifier resolution does not by itself verify the exact FlyBase
protein isoform sequence.

## Derived files

- [inventory.csv](inventory.csv): all 94 records; resolved symbols, FlyBase IDs,
  output counts, exact ordinary-UniProt GO overlaps, sequence checksums and any
  matching review file present when the script runs. A matching file is not a
  completed or validated review. Overlap counts GO IDs only, not polarity-aware equivalence; it is not a correctness assessment.
- [prediction-statements.csv](prediction-statements.csv): all 123 GO, function,
  location and keyword statements, with original text preserved. Protein-name
  predictions and full evidence blocks remain in the raw API snapshot.
- [functional-cohort.csv](functional-cohort.csv): all 41 GO/function records;
  [functional-predictions.csv](functional-predictions.csv): their 63 original
  GO/function statements. Function paragraphs are not split or rewritten here.
- [location-keyword-tier.csv](location-keyword-tier.csv): all 29 records with
  location or keyword outputs but no GO/function output.
- [claim-provenance.csv](claim-provenance.csv): GO/function claims paired with their
  original evidence JSON, scores and phmmer/TMalign donor accession fields. These
  are reported matches, not independent evidence of biological correctness or
  proof of the model's internal generation steps.
- [sequences.fasta](sequences.fasta): all 94 current protein sequences.
- [species-counts.csv](species-counts.csv) and [summary.json](summary.json): census
  aggregates; counts concern records and statements, not correct predictions.
- [review-queue.csv](review-queue.csv): manually prioritized 41-gene queue, with
  bounded review questions. Priority does not change cohort membership or assign
  an assessment. The summarizer does not overwrite this file.

## Review coverage

[review-inventory.json](review-inventory.json) records exact-accession review
coverage, retained original GO IDs/labels and function paragraphs, available
research files, and positive predictions that match a negated GOA term. The
audit also compares fetched UniProt sequences with the frozen snapshot and lists
missing file references, GOA sources, notes, rendered pages and history records.
These artifact checks are reported separately from annotation-action coverage.
The summary also totals authored GO assessment categories and new annotation
proposals; mixed function paragraphs are kept separate from the GO counts.
The [coverage checker](review_inventory.py) does not assign biological verdicts or
replace manual review and schema/evidence validation. Main YAML workflow status
is reported separately from whether annotation actions have been recorded.

```bash
uv run python projects/PROTNLM_EVALUATION/fly-benchmark/review_inventory.py
```

[Validation summary](validation-summary.json) records completed checks and hashes of
the reviewed YAML inputs. [Prediction evidence checks](prediction-evidence-validation.json)
retain the per-file title/excerpt validation results. These are validation records,
not additional biological evidence.

## Reproduce offline

From the repository root:

```bash
uv run python projects/PROTNLM_EVALUATION/fly-benchmark/summarize.py
```

The [summarizer](summarize.py) reuses the existing mammal census parser, verifies
that prediction and ordinary-UniProt accessions match the accession list, resolves
FlyBase identifiers, and regenerates derived census files. It does not fetch or
adjudicate biological evidence. Existing-review paths reflect the working tree at
regeneration time, rather than an immutable initial overlap census.

## Fetch a separate comparison

Preserve these frozen inputs. The [fetcher](fetch.py) requires a new empty output
directory, retrieves all published Dmel accessions and ordinary UniProt records,
and downloads the current FlyBase identifier table:

```bash
uv run python projects/PROTNLM_EVALUATION/fly-benchmark/fetch.py \
  --out-dir /tmp/protnlm-fly-refetch
```

Run the summarizer on a deliberate copy of the new input files when comparing
snapshots. A newer service response is not automatically the same prediction
release or protein model as this snapshot.
