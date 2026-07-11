# septal_junction module — genome scan

Reproducible scan that uses the groundings in `modules/septal_junction.yaml` to
detect septal-junction module members in other cyanobacterial genomes, with
filamentous heterocyst-formers as positive controls and unicellular
cyanobacteria as negative controls.

## Run

```bash
cd analysis/septal_junction_genome_scan
uv run python scan.py            # both methods
uv run python scan.py --method A # InterPro family membership only (API, no downloads)
uv run python scan.py --method B # phmmer homology only (downloads proteomes)
```

## What it does

- **Method A** queries the InterPro REST API for members of each component's
  InterPro family in each target proteome's taxon (no local tools/downloads).
- **Method B** downloads each Nostoc PCC 7120 exemplar sequence and each target
  reference proteome from UniProt, then runs `phmmer` (via `pyhmmer`, which bundles
  HMMER — no system install) to find the best homolog of each exemplar in each genome.

Targets, exemplars, family terms and the E-value cutoff are in `config.py`, all
traceable to `modules/septal_junction.yaml` and `genes/NOSS1/`.

## Outputs

- `results/family_membership.tsv` — Method A
- `results/homology_besthits.tsv` — Method B
- `RESULTS.md` — interpretation and tables

`data/` (downloaded FASTAs) is git-ignored and repopulated on demand.

## Dependencies

`pyhmmer`, `requests` (see `pyproject.toml` / `uv.lock`). Network access to
`rest.uniprot.org` and `www.ebi.ac.uk` is required.
