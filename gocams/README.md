# GO-CAM cache

This directory caches the **production** GO-CAM (Gene Ontology Causal Activity
Model) set — the ~2,000 reviewed, published causal activity models — alongside
the gene/`reactome`/`publications` caches.

## Layout

```
gocams/
  <model_id>/
    <model_id>-src.yaml      # canonical fetched model (DO NOT EDIT)
    <model_id>-review.yaml   # (optional) reviewer assessment (GoCamReview)
    <model_id>-notes.md      # (optional) reviewer notes
  index.tsv                  # gene_product -> GO-CAM activity (annoton) index
  BEST_PRACTICE.md           # rubric for reading/reviewing GO-CAM activities
  README.md
```

`<model_id>` is the bare local model id (e.g. `568b0f9600000284`); the full
`gomodel:` id is preserved inside the file. The per-model folder leaves room for
reviewer-authored companion files, mirroring the gene-review convention.

## What `-src.yaml` is

Each model is fetched as low-level Minerva JSON from
`https://live-go-cam.geneontology.io/product/json/low-level/<id>.json` and
translated by [`gocam-py`](https://github.com/geneontology/gocam-py) into the
activity-centric representation: a list of **activities** ("annotons"), each
coupling an `enabled_by` gene product to a `molecular_function`, and optionally a
`part_of` biological process, an `occurs_in` cellular component, and
`causal_associations` to downstream activities.

This is the canonical fetched artifact and should **not** be hand-edited.

## Provenance

- Production model list: `https://go-public.s3.amazonaws.com/files/gocam-models.json`
- Per-model JSON: `https://live-go-cam.geneontology.io/product/json/low-level/<id>.json`

## Regenerating

```bash
just fetch-gocam gomodel:568b0f9600000284   # one model
just cache-gocams                           # all production models + index
just cache-gocams --limit 50                # first 50 (for testing)
just gocam-index                            # rebuild index.tsv only
```

## `index.tsv`

One row per activity (annoton) across all cached models, with columns:

`gene_product`, `gene_label`, `model_id`, `model_title`, `taxon`,
`activity_id`, `molecular_function`, `mf_label`, `biological_process`,
`bp_label`, `cellular_component`, `cc_label`.

`gene_product` is the join key used to relate GO-CAM annotons back to gene
reviews (`genes/**/*-ai-review.yaml`) and to module documents (`modules/`).

## Reviewing a model

Each model folder leaves room for a reviewer assessment validated against the
`GoCamReview` schema class. Seed a stub (one entry per cached activity) and
validate it:

```bash
just seed-gocam-review 568b0f9600000284
just validate-gocam-review gocams/568b0f9600000284/568b0f9600000284-review.yaml
```

The stub pre-fills each activity's gene product / MF / BP / CC with `PENDING`
assessments. The rubric behind the schema's enums (verdicts, QC flags, and
consistency-with-gene-review categories) is the **`gocam-curation` skill**
(`.claude/skills/gocam-curation/`); `BEST_PRACTICE.md` is a short pointer to it.

## Referencing GO-CAMs from modules

Module documents (`modules/`) curate more general, often non-grounded biological
modules. A module node or annoton can be grounded in one or more production
GO-CAMs via the `gocam_associations` slot (`GoCamAssociation`: `model` +
optional `activity`). See `modules/README.md`.
