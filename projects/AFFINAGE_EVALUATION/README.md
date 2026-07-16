# AFFINAGE_EVALUATION — supporting material

Reproducible comparison of Affinage (affinage.wi.mit.edu) `mechanism_profile` GO
terms against the local AIGR reviews. Project page: [`../AFFINAGE_EVALUATION.md`](../AFFINAGE_EVALUATION.md).

## Layout

| Path | What |
|------|------|
| `compare_affinage.py` | Fetch Affinage JSON (cached) + diff vs GOA/`core_functions`. No hard-coded numbers. |
| `pilot-genes.txt` | The 12-gene human pilot cohort (one symbol per line). |
| `affinage-cache/<SYM>.json` | Cached Affinage API responses, **trimmed** to the fields we use: `narrative.mechanism_profile`, `timeline.current_model`, `prefetch_data.uniprot` (accession/name), `evaluation`, `cost.total_usd`. Two **representative** records are committed as provenance — `GPX4.json` (worked example) and `ADA.json` (the symbol-collision case). The full 12-gene cache regenerates on demand via the script; the extracted GO data for all 12 is already committed in `results/per-gene.json`. `--refresh` re-fetches the full record from the API. |
| `results/per-gene.json` | Full per-gene comparison (GO sets, shared ids, core-MF capture). |
| `results/summary.csv` / `results/summary.md` | Generated summary tables. |

## Rerun

```bash
python compare_affinage.py --genes-file pilot-genes.txt   # uses cache
python compare_affinage.py --refresh GPX4 TP53            # force re-fetch
```

Requires only Python 3 stdlib + `pyyaml` (already a repo dependency) and `curl`.

## Caveats

- Exact-GO-id agreement only; it **understates** agreement where Affinage grounds
  to a true GO ancestor of the curated term (the dominant pattern — read
  qualitatively on the project page).
- The local AIGR references are mixed-maturity, not independently expert-signed
  ground truth.
- n=12 pilot: illustrative, not a powered benchmark.
