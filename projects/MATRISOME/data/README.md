# Matrisome masterlist data (not committed)

The matrisome masterlist CSVs (`matrisome_human.csv`, `matrisome_mouse.csv`,
`matrisome_zebrafish.csv`, `matrisome_drosophila.csv`, `matrisome_c_elegans.csv`) are **not committed**
(≈36k rows total) because this project is parked (see [`../README.md`](../README.md)). Regenerate them
on demand from the source before re-running `missing_annotation_report.py`.

Source: [`Matrisome/MatrisomeAnalyzeR`](https://github.com/Matrisome/MatrisomeAnalyzeR) @ `d8aec6d`,
`data/matrisome.list.rda` (R list of one `gene`/`category`/`family` data.frame per species),
licensed GPL (≥3). Each gene appears as multiple rows — one per identifier namespace (symbol, alias,
UniProt, RefSeq, Ensembl, NCBI GeneID) — so any identifier resolves to its family. The canonical
human matrisome is ~1,027 genes (the NCBI-GeneID row count).

## Regenerate

```bash
git clone --depth 1 https://github.com/Matrisome/MatrisomeAnalyzeR.git /tmp/MatrisomeAnalyzeR
uv run --with rdata --with pandas python - <<'PY'
import rdata
from pathlib import Path
conv = rdata.conversion.convert(
    rdata.parser.parse_file("/tmp/MatrisomeAnalyzeR/data/matrisome.list.rda")
)
out = Path("projects/MATRISOME/data")
for species, df in conv["matrisome.list"].items():
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    for c in df.columns:
        df[c] = df[c].astype(str).str.strip()
    df.to_csv(out / f"matrisome_{str(species).replace('.', '_')}.csv", index=False)
    print("wrote", species, df.shape)
PY
```
