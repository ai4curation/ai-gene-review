# NIT1 (P40447 / YIL164C) bioinformatics

Reproducible analysis of the S. cerevisiae putative nitrilase-superfamily protein
NIT1: catalytic-triad integrity, truncation / split-ORF (YIL164C + YIL165C), and
orthology to human NIT1/NIT2.

Run:

```
just all
```

Requires `mafft` on PATH and `uv` (deps: biopython). See `RESULTS.md` for findings.

- `data/` — input FASTA sequences (fetched from UniProt REST)
- `scripts/` — generic analysis scripts (positions/paths passed as args)
- `results/` — direct outputs (do not edit)
- `RESULTS.md` — written summary and checklist
