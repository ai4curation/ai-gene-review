# Frozen pombe ProtNLM cohort

The [pombe project page](../pombe.md) reports the biological assessments.
This snapshot identifies 28 original-export accessions matching current
*Schizosaccharomyces pombe* UniProt primary accessions. All 20 entries with GO or
function text form the initial review cohort: 32 GO claims and 11 function
paragraphs. Eight other records remain in the census.

## Sources and scope

The published 26,856-record [ProtNLM2 accession list](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv)
contains no pombe records. However, all 28 original-export pombe accessions return
predictions from the live ProtNLM API. List omission is not API unavailability.
All 28 ordinary UniProt entries are currently reviewed/Swiss-Prot; the prediction
API's placeholder TrEMBL classification is not their curated record status.

The source export `post-processed-2026_02_28k.xml` contains 28,553 entries with
placeholder organism, sequence and date fields. Membership is therefore resolved
by joining original primary accessions to the current UniProt `taxonomy_id:4896`
index, followed by the PomBase accession-to-gene table. This identifies the cohort
without treating placeholder taxonomy as biology. It does not establish an
exhaustive census of all API-served pombe accessions or search historical secondary
accessions. Gene symbols follow the frozen PomBase table, including `mre11`
(UniProt `rad32`), `crt10` (`pi073`), `cem1` (`SPBC887.13c`) and `asr1`
(`SPCC126.07c`).

## Frozen inputs

- [Original subset XML](snapshot/predictions.xml): all 28 complete entry elements,
  reserialized with original element values, attributes, paragraphs and evidence
  retained. The full export's filename, record count and SHA-256 are in the
  [manifest](manifest.json); the local original export is not redistributed here.
- [Published accession list](snapshot/published-accessions.tsv): exact downloaded
  bytes, retaining the evidence for absence from that list.
- [Current pombe UniProt index](snapshot/uniprot-pombe-index.tsv): 5,228 records.
- [PomBase identifiers](snapshot/pombase-identifiers.tsv): original downloaded
  identifier table, including systematic identifiers and current gene symbols.
- [Current UniProt records](snapshot/uniprot.jsonl.gz): 28 complete ordinary API
  JSON objects, serialized as sorted-key JSON lines and deterministic gzip.
- [Prediction API responses](snapshot/api-availability.jsonl.gz): all 28 complete
  responses with accessions, URLs and HTTP status, in the same gzip format.

The manifest hashes the **stored bytes**, including compressed bytes for gzip
files. Current sequences do not prove the exact input sequences used for model
prediction. Placeholder dates and annotation overlap do not establish training
membership.

## Derived tables

- [Inventory](inventory.csv): all 28 accessions with resolved gene symbols,
  systematic IDs, current lengths/status and GO/function counts.
- [Functional cohort](functional-cohort.csv): all 20 GO/function-bearing entries.
- [Original GO/function statements](functional-predictions.csv): 32 GO labels and
  11 intact paragraphs, with original evidence keys.
- [Claim provenance](claim-provenance.csv): the same claims with their full
  referenced XML evidence fragments. Scores and phmmer/TMalign matches describe
  prediction provenance, not independent biological validation.
- [All statements](prediction-statements.csv): also retains the 10 location
  statements and one keyword. Predicted protein names remain in the raw snapshots.
- [API/source comparison](api-source-comparison.csv): all GO IDs/labels agree.
  All 11 API function paragraphs omit the XML's final period; otherwise their
  text agrees exactly. Evidence metadata may differ between representations and
  remains available in both frozen sources.
- [Current sequences](sequences.fasta) and [census summary](summary.json).

The [coverage checker](review_inventory.py) writes a [review inventory](review-inventory.json) checking exact-accession coverage,
source GO IDs/labels, retained original paragraphs, annotation actions, available
research files, source/reference paths and sequence consistency. It does not
assign biological assessments or replace schema/evidence validation.
[Validation summary](validation-summary.json) records checked input hashes;
[prediction evidence results](prediction-evidence-validation.json) preserve
per-file title and excerpt checks.

## Reproduce

From the repository root, regenerate the tables without network access:

```bash
uv run python projects/PROTNLM_EVALUATION/pombe-benchmark/summarize.py
uv run python projects/PROTNLM_EVALUATION/pombe-benchmark/review_inventory.py
```

The [summarizer](summarize.py) verifies the snapshot checksums before reading the frozen inputs.
To retrieve a **separate** comparison snapshot, supply the original XML export
and a new empty output directory:

```bash
uv run python projects/PROTNLM_EVALUATION/pombe-benchmark/fetch.py \
  --source-xml /path/to/post-processed-2026_02_28k.xml \
  --out-dir /tmp/protnlm-pombe-refetch
```

The [fetcher](fetch.py) computes cohort membership and counts from the supplied export and
current sources. It refuses to overwrite an existing nonempty directory. A later
snapshot can differ in annotation, identifier mapping or prediction availability;
it is not automatically the same release.
