# IMPReSS behavioural-assay ingest

Standardized phenotyping assays from **IMPReSS** (the International Mouse
Phenotyping Resource of Standardised Screens, IMPC), ingested to operationalize
the [BEHAVIOR](../../BEHAVIOR.md) ↔ [ASSAY_TO_FUNCTION](../../ASSAY_TO_FUNCTION.md)
cross-link: which standardized assay drives a behaviour annotation, and what GO
process (if any) it can legitimately support.

## Files

- **`ingest_impress.py`** — reproducible fetch of one pipeline's full procedure
  set from the IMPC API (`https://api.mousephenotype.org/impress`). Live fetch;
  nothing hard-coded.
- **`impc_procedures.tsv`** *(generated)* — all procedures in pipeline
  `IMPC_001` (the curated IMPC screen): key, name, level, version, #parameters,
  MP terms parsed from the description, and a transparent
  `behavioural_neurological` flag.
- **`behavioural_assays.yaml`** *(generated)* — the behavioural/neurological
  subset with detail.
- **`REPORT.md`** *(generated)* — counts + the behavioural-assay table.
- **`behavioural_assay_go_map.yaml`** *(hand-curated)* — the bridge: each
  behavioural assay → the GO behaviour term(s) a hit can support, as
  `KEEP_AS_NON_CORE` (all ids QuickGO-verified), with the over-annotation
  caution. This is the layer no public ontology provides.

## Regenerate

```bash
uv run python projects/BEHAVIOR/impress/ingest_impress.py \
    --pipeline IMPC_001 --out-dir projects/BEHAVIOR/impress
```

## Why a hand-curated GO map

The ontology landscape splits the problem three ways and never closes it:

- **NBO** (Neuro Behavior Ontology) and **MP** (`behavior/neurological
  phenotype`, MP:0005386) describe the *process / phenotype*.
- **IMPReSS** (this ingest) and **OBI** describe the *assay / protocol*.
- **CogPO** / **Cognitive Atlas** describe human *cognitive tasks*.

None maps "assay X → GO process P, with reliability R". `behavioural_assay_go_map.yaml`
encodes that for the IMPReSS battery, with the ASSAY_TO_FUNCTION caution baked in:
a behavioural assay is the extreme phenotypic + high-convergence readout, so a
hit licenses at most a non-core BP term — never an MF or core call. Two assays
are deliberately fenced off: **Grip Strength** (neuromuscular, no behaviour term)
and **Auditory Brain Stem Response** (electrophysiology — a hearing/sensory term
at most, *not* `auditory behavior`).

## Caveats

- `IMPC_001` is the current curated pipeline; legacy/other pipelines add assays
  (Rotarod, Hole-board, Tail Suspension, …) — pass a different `--pipeline` to
  ingest them. The `BEHAVIORAL_ASSAY` readout class in
  `ASSAY_TO_FUNCTION/readout_catalog.yaml` already carries patterns for those.
- MP terms here come from the procedure *description*; richer parameter-level MP
  mappings are available via `/ontologyterm/belongingtoparameter/:parameterID`
  for future enrichment.
