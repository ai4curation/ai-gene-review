# AP3M2 bioinformatics

Reproducible analyses supporting the human AP3M2 (mu3B) GO annotation review.

```
uv run python analyze.py
```

Everything is fetched live (UniProt, PDBe/SIFTS, RCSB, Human Protein Atlas) into
`data/` (git-ignored) and `RESULTS.md` is regenerated from it. No result is
hardcoded; wrong accessions raise rather than being silently accepted.
