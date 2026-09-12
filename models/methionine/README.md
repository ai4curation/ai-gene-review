# Methionine cycle — 3rd-party model ingest

Source files and the reviewed bridge for ingesting the **biosustain Maud** methionine
kinetic model as a regulatory-evidence source for `modules/methionine_cycle.yaml`.

The Maud model is treated as **evidence, not truth**: its `[[allostery]]` and
`[[competitive_inhibition]]` tables are parsed into canonical regulatory edges,
mediated by a reviewed id-mapping, and compared against the curated module. Nothing
is merged automatically.

## Files

- `methionine_cycle.regulation.toml` — the regulation-relevant sections (enzymes,
  enzyme↔reaction, allostery, competitive inhibition) transcribed from the upstream
  Maud model `data/methionine/methionine_cycle.toml`
  (<https://github.com/biosustain/Methionine_model>). Stoichiometry, kinetics, and
  priors are omitted.
- `maud_methionine_mapping.yaml` — reviewed mapping from Maud ids to curated module
  symbols. This is curation knowledge (e.g. MAT1/MAT3 are distinct isozymes, while the
  trailing `1` in GNMT1/MTHFR1 is just an instance suffix), not something a lexical
  heuristic can infer.

## Usage

Diff the curated module against the source regulation:

```bash
ai-gene-review compare-module-regulation \
  modules/methionine_cycle.yaml \
  models/methionine/methionine_cycle.regulation.toml \
  -m models/methionine/maud_methionine_mapping.yaml
```

Add `--emit-candidates` to print the source edges as candidate module `connections`
(SBO-grounded, with provenance) for review. The same command works against the full
upstream TOML if you fetch it:

```bash
curl -sSL https://raw.githubusercontent.com/biosustain/Methionine_model/main/data/methionine/methionine_cycle.toml \
  -o /tmp/methionine_cycle.toml
ai-gene-review compare-module-regulation modules/methionine_cycle.yaml /tmp/methionine_cycle.toml \
  -m models/methionine/maud_methionine_mapping.yaml
```

The curated module was transcribed from this source, so the diff currently reports
**full agreement** (10/10 regulatory edges) — a round-trip validation that the
curation faithfully captured the model's regulatory wiring.
