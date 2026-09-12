# MCH2 (YKL221W / P36032) bioinformatics

Comparative/structural analysis supporting the GO-annotation review of the dark
*S. cerevisiae* monocarboxylate-transporter homolog MCH2.

## Run

Requires `uv` and `mafft` on PATH.

```bash
just all        # full pipeline
# individual steps: just fetch tm topology corroborate align identity tree motif
```

See `RESULTS.md` for findings, provenance, caveats, and the analysis checklist.
Scripts are in `scripts/`, inputs (accession lists) in `data/`, outputs in `results/`.
No sequences or results are hardcoded; sequences are fetched from UniProt at run time.
