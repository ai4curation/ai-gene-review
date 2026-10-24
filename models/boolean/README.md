# Boolean models — external sources and reviewed bridges

Cached external Boolean/logical models and signed-interaction exports, with the
reviewed id-mappings that bridge them to curated modules under `modules/`. Used by
the [BOOLEAN_MODELS](../../projects/BOOLEAN_MODELS.md) project.

External models are treated as **evidence, not truth** (the same posture as
`models/methionine/` for the Maud kinetic model): their wiring is reduced to signed
edges, projected through a reviewed mapping onto the module's element ids, and
diffed against the curated module. Nothing is merged automatically; agreements and
discrepancies are reported for a curator to adjudicate.

## Layout

```
models/boolean/
  README.md
  bbm-070-mapk-cancer-cell-fate/     # one folder per external Boolean model
    model.bnet                        # verbatim source (DO NOT EDIT)
    metadata.json                     # verbatim source metadata (DO NOT EDIT)
    README.md                         # provenance: where, when, licence, checksum
    mapping_to_modules.yaml           # reviewed bridge: module elements <-> model variables
  signor/
    SIGNOR-EGF.tsv                    # verbatim SIGNOR pathway export (DO NOT EDIT)
    SIGNOR-EGF.mapping_to_modules.yaml
    README.md
```

## Mapping file format

A mapping defines a **shared symbol namespace** and names, on each side, the ids
that collapse onto each symbol:

```yaml
source: <where the external model came from>
publication: PMID:24250280
modules:                 # module file stem -> {symbol: module element id(s)}
  erk_cascade:
    RAS: ras_active
    RAF: raf_map3k
external:                # {symbol: external variable id(s)}
  RAS: v_RAS
  RAF: v_RAF
  ERK_OUTPUT: [v_RSK, v_ELK1]   # several external variables may lump into one symbol
notes: |
  Free text explaining non-obvious choices.
```

Symbols are curation knowledge, not lexical matches: a module's family-level
annoton (e.g. "RAF kinases") may correspond to one lumped model variable
(`v_RAF`), while a module's single "ERK output" step may correspond to several
model variables (`v_RSK`, `v_ELK1`). Edges whose endpoints both map are compared;
edges with one mapped endpoint are reported as external regulators the module does
not name; wholly unmapped ids are reported for coverage.

## Usage

```bash
# translate a module to a Boolean network (BoolNet .bnet)
ai-gene-review module-to-bnet modules/erk_cascade.yaml

# run the calibration + dynamics demo (needs biodivine-aeon; installed ephemerally)
uv run --with biodivine-aeon python projects/BOOLEAN_MODELS/run_mapk_demo.py
```
