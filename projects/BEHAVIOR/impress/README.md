# IMPReSS behavioural-assay ingest + assay→GO check

Standardized phenotyping assays from **IMPReSS** (the International Mouse
Phenotyping Resource of Standardised Screens, IMPC), ingested to operationalize
the [BEHAVIOR](../../BEHAVIOR.md) ↔ [ASSAY_TO_FUNCTION](../../ASSAY_TO_FUNCTION.md)
cross-link: which standardized assay drives a behaviour annotation, and what GO
process (if any) it can legitimately support.

## Files

- **`ingest_impress.py`** — reproducible fetch of one or more pipelines' full
  procedure sets from the IMPC API (`https://api.mousephenotype.org/impress`),
  classifying behavioural/neurological procedures into canonical assay *types*.
  Live fetch; nothing hard-coded.
- **`procedures.tsv`** *(generated)* — every procedure across the ingested
  pipelines (pipeline, key, name, level, version, #parameters, MP terms,
  behavioural flag, canonical assay type).
- **`behavioural_assays.yaml`** *(generated)* — behavioural/neurological assays
  grouped by canonical type, each listing every (pipeline, key) instance.
- **`REPORT.md`** *(generated)* — counts + the canonical behavioural-assay table.
- **`behavioural_assay_go_map.yaml`** *(hand-curated)* — the bridge: each
  behavioural assay type → the GO behaviour term(s) a hit can support, as
  `KEEP_AS_NON_CORE` (all ids QuickGO-verified), with the over-annotation
  caution. `assay_type` joins to `behavioural_assays.yaml`. Includes the
  Morris Water Maze (flagged `not_in_impress`: a classic literature assay).
- **`check_behaviour_assays.py`** + **`ASSAY_CHECK.md` / `assay_check_flags.csv`**
  *(generated)* — scans every annotation whose evidence text *names* a
  recognised assay and flags `MISMATCH` (assay doesn't license the GO term),
  `OVER_CORE` (accepted as core), or `FENCED` (assay licenses no behaviour term).
- **`validate_map.py`** — validates `behavioural_assay_go_map.yaml` (these files
  are bespoke project data, not bound to the LinkML gene-review schema, so this
  is their dedicated check). Offline: parse, structure, unique `assay_type`,
  well-formed `GO:nnnnnnn`/label entries, and an exact join to the ingested
  canonical assay types. `--online`: every GO id resolves in QuickGO, is
  non-obsolete, is a `biological_process`, and its label matches verbatim
  (checked per occurrence). Exits non-zero on failure.

  ```bash
  uv run python projects/BEHAVIOR/impress/validate_map.py --online
  ```

## Regenerate

A project-local `justfile` wraps the workflow (recipes `cd` to the repo root):

```bash
cd projects/BEHAVIOR/impress
just                 # list recipes
just ingest          # refresh procedures.tsv / behavioural_assays.yaml / REPORT.md
just validate-online # structure + exact join + QuickGO id/label check
just check           # ASSAY_CHECK.md / assay_check_flags.csv
just all             # ingest -> validate-online -> check
```

Or call the scripts directly from the repo root:

```bash
uv run python projects/BEHAVIOR/impress/ingest_impress.py --out-dir projects/BEHAVIOR/impress
uv run python projects/BEHAVIOR/impress/check_behaviour_assays.py --out-dir projects/BEHAVIOR/impress
uv run python projects/BEHAVIOR/impress/validate_map.py --online
```

The default ingest covers **15 canonical behavioural/neurological assay types**
across 5 pipelines — including the assays absent from the IMPC core pipeline
(Rotarod, Hole-board, Hot Plate, Tail Suspension, Von Frey, Sleep-Wake). Pass
`--pipelines` to ingest others.

## How the check wires into the readout mining

Two complementary layers:

1. **Generic** — `BEHAVIORAL_ASSAY` is a readout class in
   `ASSAY_TO_FUNCTION/readout_catalog.yaml`, so `mine_readouts.py` already
   cross-tabulates behavioural-assay mentions against reviewer action.
2. **Specific** — `check_behaviour_assays.py` uses
   `behavioural_assay_go_map.yaml` to verify the *exact GO term* against the
   *specific assay*. This independently re-derived the **Casp3 `swimming
   behavior` → Morris Water Maze** over-annotation (the assay is a spatial-memory
   test; swimming is only the modality).

The check is **exact-id and advisory**: it matches the annotated term id against
the assay's licensed set (a future refinement would use GO subsumption so child
terms pass automatically), and `OVER_CORE` should be read as "confirm this gene
is genuinely proximal" — bona-fide clock genes / receptors are the documented
rubric exceptions (e.g. CRY sleep/wake is correctly near-core).

## Why a hand-curated GO map

No public ontology maps "assay → GO process": **NBO** / **MP**
(`behavior/neurological phenotype`, MP:0005386) describe the *process/phenotype*,
**IMPReSS** (this ingest) / **OBI** the *assay*, **CogPO** / **Cognitive Atlas**
human *cognitive tasks*. `behavioural_assay_go_map.yaml` closes that gap for the
IMPReSS battery, with the ASSAY_TO_FUNCTION caution baked in (phenotypic +
high-convergence → non-core only). Two assays are deliberately fenced (empty
`supports_go`): **Grip Strength** (neuromuscular) and **Tail Suspension** (no GO
term for depression-like immobility); **Auditory Brain Stem Response** is capped
at a hearing term and fenced against `auditory behavior`.

## Caveats

- MP terms come from the procedure *description*; richer parameter-level MP
  mappings are available via `/ontologyterm/belongingtoparameter/:parameterID`.
- The checker only sees annotations that *name* an assay in their evidence text;
  most cite a PMID instead, so its flag count is a floor, not the full
  population.
