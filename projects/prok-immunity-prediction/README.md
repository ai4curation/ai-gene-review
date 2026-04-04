# Prokaryotic Immunity Prediction

## Objective

Build an AIGR-aligned pipeline for predicting known and novel prokaryotic immunity genes from genomes or proteomes, then export those predictions into the standard `PredictionReview` workflow used elsewhere in this repository.

The design is explicitly based on Mordret et al. 2026 (*Science*, DOI `10.1126/science.adv8275`), which used both protein and genomic language models to expand the known landscape of bacterial antiphage defense. The currently implemented architecture mirrors that idea in a practical, reproducible way:

1. Use a protein language model (`ESM-2`, defaulting to the lightweight `facebook/esm2_t6_8M_UR50D`) to embed proteins.
2. Use genomic neighborhood density as a first-pass proxy for the genomic language-model signal.
3. Cross-reference the sample against curated defense databases and tools:
   - DefenseFinder
   - PADLOC / PADLOC-DB
   - CasFinder
4. Propagate known-family labels from database-backed seed hits into embedding space.
5. Nominate novel candidates when proteins look defense-like in embedding/context space but are absent from current defense databases.
6. Export each candidate into an AIGR `*-predictions-review.yaml` file so it can enter the normal curation pipeline.

## Current Scope

This is the initial architecture and core pipeline code. It is intentionally conservative:

- It supports protein FASTA, GenBank, and nucleotide FASTA inputs.
- Nucleotide FASTA requires `prodigal` for gene calling.
- External database support is real, but depends on local tool installation.
- Known-family predictions are strongest when DefenseFinder/PADLOC/CasFinder are available.
- Novel calls are ranked candidates, not experimental validations.

## Project Layout

```text
projects/prok-immunity-prediction/
  README.md
  justfile
  config/defense_families.yaml
  benchmark/
    README.md
    raw/
    normalized/
  data/example/
    example_proteome.faa
    example_annotations.gff

src/ai_gene_review/prok_immunity_prediction/
  cli.py
  pipeline.py
  io.py
  embeddings.py
  cross_reference.py
  classifier.py
  aigr_export.py
  evaluation.py
```

## Pipeline

### 1. Input normalization

- Protein FASTA: parsed directly.
- GenBank: CDS translations and coordinates are extracted, then rewritten as normalized FASTA + GFF.
- Nucleotide FASTA: CDSs are called with `prodigal`, then treated like a normalized proteome.

### 2. Protein language model embeddings

- `ESM-2` is the main embedding backend.
- A small composition-based embedder exists for tests, smoke runs, and environments where `torch` / `transformers` are unavailable.

### 3. Known defense-family prediction

Canonical families are defined in [`config/defense_families.yaml`](config/defense_families.yaml).

The current classifier combines:

- direct external-tool evidence
- embedding similarity to database-backed seed proteins
- local defense-neighborhood density on the same contig

Supported family buckets include:

- CRISPR-Cas
- Restriction-modification
- Abortive infection
- CBASS
- Thoeris
- Gabija
- BREX
- DISARM
- Zorya
- Hachiman
- Wadjet
- Retrons
- PARIS

### 4. Novel candidate nomination

A protein is promoted to a novel immunity candidate when it:

- lacks DefenseFinder/PADLOC/CasFinder support
- scores near the learned defense manifold in embedding space
- sits in a defense-rich genomic neighborhood

This is a direct operationalization of the Mordret-style idea: combine sequence-level representation learning with context-aware reasoning to reach beyond currently curated defense catalogs.

### 5. AIGR export

Predictions are exported as AIGR `PredictionReview` YAML files using a new `DEFENSE_SYSTEM` predicted-term type in the shared schema. That keeps the immunity workflow inside the repository’s normal curation surface instead of creating a one-off format.

The exporter writes:

- `genes/<organism>/<gene>/<gene>-predictions-review.yaml`
- `aigr_manifest.json`

Use `--export-aigr-root /path/to/repo-root` or the `just sync-aigr ...` target to write directly into the main repository `genes/` tree.

## Evaluation

The evaluation utilities assume a normalized benchmark table with at least:

- `protein_id`
- `is_defense`
- `family`
- `is_novel`

Place raw supplement tables under [`benchmark/raw`](benchmark/raw), normalize them with the CLI, then evaluate against `predictions.tsv`.

## Running

From this directory:

```bash
just run-example
just run data/example/example_proteome.faa output=outputs/example organism=ECOLI taxon=NCBITaxon:83333 embedder=composition
just run-esm2 data/example/example_proteome.faa output=outputs/esm2 organism=ECOLI taxon=NCBITaxon:83333
just sync-aigr data/example/example_proteome.faa output=outputs/aigr organism=ECOLI taxon=NCBITaxon:83333
```

The ESM-2 target uses `uv run --with torch --with transformers ...` so the main repository dependencies do not need to permanently absorb those heavy ML packages.

## External References

- Mordret et al. 2026, *Science*, DOI: https://doi.org/10.1126/science.adv8275
- Preprint / abstract version: https://sciencecast.org/casts/t1molfuexnkh
- DefenseFinder: https://github.com/mdmparis/defense-finder
- PADLOC: https://github.com/padlocbio/padloc
- CasFinder: https://github.com/macsy-models/CasFinder

## Notes

- DefenseFinder’s README documents `defense_finder_systems.tsv`, `defense_finder_genes.tsv`, and `defense_finder_hmmer.tsv` outputs and accepts ordered protein FASTA input.
- PADLOC screens genomes against HMMs and system classifications, and emits `_padloc.csv` summaries.
- CasFinder provides subtype-level CRISPR-Cas calls through MacSyFinder models and outputs `best_solution.tsv`.

Those three tools are used here as database-backed anchors for “known defense” calls, while the embedding/context layers handle extrapolation and novelty ranking.
