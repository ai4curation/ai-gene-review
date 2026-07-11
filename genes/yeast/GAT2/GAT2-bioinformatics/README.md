# GAT2-bioinformatics

Reproducible analysis confirming the GATA-type Cys4 zinc finger in *S. cerevisiae*
GAT2 (P40209 / YMR136W) and placing GAT2 relative to the other yeast GATA factors
by DNA-binding-domain identity.

See `RESULTS.md` for findings.

## Run

```bash
just all          # zinc-finger detection + pairwise DBD identity
# or individually:
just zinc-finger
just dbd-identity
```

Requires `uv` (Python deps in `pyproject.toml`) and `mafft` on PATH.

## Layout
- `data/` — input FASTA (downloaded from UniProt REST) + ACT1 negative control
- `scripts/` — analysis scripts (no hardcoded results)
- `results/` — script outputs (motif JSON, DBD identity TSV, alignment)
- `RESULTS.md` — write-up with provenance and caveats
