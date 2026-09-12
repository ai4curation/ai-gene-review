# A0A3B6GK97 bioinformatics

Reproducible analysis to (1) place wheat patatin protein **A0A3B6GK97**
(TraesCS3D02G033600) within the plant pPLA subfamilies and (2) check whether its
catalytic machinery (patatin Ser-Asp dyad) is intact.

## Run

```bash
just all        # fetch sequences from UniProt, analyze, run control
# or individually:
just fetch
just analyze
just test-control
```

Requires `uv` (deps pinned in `pyproject.toml` / `uv.lock`: biopython, pyfamsa, requests).

## Layout

- `data/reference_accessions.tsv` — input config: query + reference UniProt accessions (provenance).
- `scripts/fetch_sequences.py` — fetch FASTA from UniProt (live; nothing hardcoded).
- `scripts/analyze.py` — MSA (FAMSA), %identity, NJ tree, catalytic-motif scan + site analysis.
- `scripts/make_control.py` — builds an input-driven control (active patatin as query).
- `results/`, `results_control/` — direct script outputs.
- **`RESULTS.md`** — findings, interpretation, caveats, and reproducibility checklist.

## Headline result

A0A3B6GK97 is a **pPLAII-type** patatin protein, **but the deposited 302-aa model lacks the
N-terminal catalytic core (oxyanion DGGG + catalytic-serine GTSTG nucleophile elbow)** and is
**predicted inactive as modeled** — most likely an incomplete/incorrect gene model (not
resolved here). See `RESULTS.md`.
