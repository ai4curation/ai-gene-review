# AP3D1 bioinformatics

Reproducible sequence checks backing the human AP3D1 (O14617) annotation review.
Everything is fetched live from the UniProt REST API into a disposable `cache/`
directory; nothing is hardcoded. See `RESULTS.md` for the findings.

```
uv run python delta_interfaces.py      # -> delta_interfaces.tsv
uv run python goa_reconcile.py         # -> goa_reconcile.tsv
```

`delta_interfaces.py` needs `mafft` on PATH (used for the multiple alignment).
