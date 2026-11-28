# Expanded topology-flag pilot

This panel tests the existing flagging rules on additional human proteins selected
without examining their DeepTMHMM2 predictions. It is a curation-workflow pilot,
not a held-out assessment of model accuracy: overlap with model training data is
unknown, and existing GOA claims enrich the sample for specific biology.

Read [RESULTS.md](RESULTS.md) for interpretation and adjudication. Raw flags retain
source disagreements; they do not imply that an annotation is wrong.

## Selection

Scan existing human reviews with all three required files (review YAML, UniProt,
GOA). Exclude the previous 31-protein panel. Include every review with a positive
canonical GOA row either in FRR:0004 scope or on exact GO:0005811 lipid droplet,
and add ATP5F1B, ATP6V1A and HSPA5 as explicit controls. Selection uses source GOA,
including claims that reviews subsequently removed; this lets us measure recovery
of known annotation problems. The lipid-droplet flag itself uses retained review
claims and their effective replacements.

The scan found 3,396 eligible reviews after exclusions and 14 other reviews
missing required files. The selected panel contains 205 proteins: 176 FRR:0004
candidates, 26 lipid-droplet candidates and three controls. The cohorts do not
overlap in this snapshot. The excluded genes, unavailable reviews, exact GO
closure and rule-file hash are in `selection.json`. `inputs.tsv` pins source
records and sequence hashes. No sequences were truncated or filtered by length.

## Reproduce

Use the repository environment for selection, flagging and reporting, and the
parent benchmark's locked environment and downloaded checkpoints for inference.
The source commit remains `526f6c60f93c0868c7315413da8e669d12373cc3`; dependency
installation and weights provenance are documented in the parent directory.

From this directory:

```bash
just select
just prepare
just predict
just flag
just cli-check
just summarize
just test
```

The run uses CPU, eight threads, one pass, no marginals, default task-model
precision, and the previously validated unbatching workaround. Prediction and
report scripts take explicit input and output arguments. Long sequences use the
upstream ESM chunking implementation. The existing 31-protein study assessed
API/CLI precision differences; this run adds a targeted check of five cases.
The committed `cli-check.fasta` selects APOB, AUP1, CAV1, LPCAT2 and GSDMD from
the input FASTA; the summarizer verifies their sequence hashes against the manifest.

`api/` contains per-protein JSON, GFF3, three-line topology and membrane-label
exports plus timings. `summary.tsv` includes unflagged proteins, the original
FRR verdict and predicted feature counts; absence of a flag does not validate the
annotation. `source-hashes.json` pins reviews, GOA, UniProt and prediction JSON.
`flags.json` is the unadjudicated output. Manual judgments are kept separately in
`adjudication.yaml` and the results narrative. The checker does not mutate reviews
or emit GO NOT assertions.
