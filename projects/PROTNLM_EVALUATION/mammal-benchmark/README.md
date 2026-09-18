# Mammalian ProtNLM2 availability census

Frozen on 8 September 2026 to support the
[benchmark design](../mammal-benchmark-design.md). This is an inventory, not a
biological assessment. No new gene-review verdicts are supplied.

## Selected horse cohort

The [40-gene review list](../horse40.md) is a targeted selection from this census:
[selection CSV](horse40.csv), [89 GO predictions and 17 function descriptions](horse40-predictions.csv),
[current sequences](horse40-sequences.fasta), [ordinary UniProt records](horse40-uniprot.jsonl.gz),
and [selection manifest with checksums](horse40-manifest.json).
The census remains the full 813-record inventory; `summarize.py` does not change
this manually selected cohort.

## Files

- [accessions.tsv](accessions.tsv): the four-species subset of the official
  [accession list](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv),
  retaining the original column values. Taxa: horse 9796, human 9606, mouse 10090,
  rat 10116. No filtering on prediction quality, gene name or annotation content.
- [predictions.jsonl.gz](predictions.jsonl.gz): all 813 successful responses from
  `https://rest.uniprot.org/uniprotkb/protnlm/{accession}`, one JSON object per line.
  Original prediction text, scores and Evidencer properties are preserved.
- [manifest.json](manifest.json): retrieval date, source URLs, checksums, selection
  rule and full-list species counts. The compressed payload is deterministic;
  the manifest's payload checksum refers to its decompressed bytes.
- [inventory.csv](inventory.csv): one record per accession; counts of each output
  type and predicted protein name. `release_length` is from the official accession
  list, not a verification of the model's input sequence.
- [prediction-statements.csv](prediction-statements.csv): emitted GO, function,
  location and keyword statements. Function paragraphs remain intact here;
  atomic claim splitting belongs to the later biological review.
- [species-counts.csv](species-counts.csv): aggregate counts. Name-only records
  have none of GO, function, location or keyword outputs. Other columns overlap.
- [candidate-goa-check.csv](candidate-goa-check.csv) and
  [raw QuickGO responses](candidate-goa-2026-09-08.json): exact accession/GO queries
  for the twelve challenge leads, including provider and evidence code. A zero
  count means absent from this dated live query; it does not establish why or when
  an older assertion disappeared.
- [supplemental API examples](supplemental-api-examples.json): the eight previously
  discussed AIGR-overlap accessions, checked separately. These are excluded from
  the four-species published-list census, even when the API serves them.

## Reproduce offline

From this directory, using Python 3.10 or later (standard library only):

```bash
python summarize.py
```

This regenerates the three census CSVs from the frozen inputs and fails if the
accession sets differ or the payload contains duplicate accessions. Protein names
are metadata, not verified orthology assignments. The source JSON contains
placeholder entry-audit dates and no reliable prediction-time sequence record;
do not use those placeholders for temporal holdouts or sequence-version matching.
The [summarization script](summarize.py) is included alongside the data.

## Fetch a separate updated comparison

The existing project fetcher can retrieve these accessions again:

```bash
python ../fetch_protnlm_api.py --accessions accessions.tsv --out-dir /tmp/protnlm-mammal-refetch
```

Its output is a new, mutable-service snapshot; preserve the frozen inputs when
comparing releases. Retrieve a new official list as well if assessing release
coverage changes. The census intentionally does not search the whole API for
unlisted records.

Before selecting or scoring a benchmark, add the actual sequence and checksum,
entry version, isoform/gene model, orthology evidence, and prediction version where
recoverable. Historical error annotations need their own dated source snapshot.
