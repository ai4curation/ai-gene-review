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
| `batch{2,3,4}-genes.txt` / `results/batch{2,3,4}/` | Extended, stress-test, and hard-case cohorts. |
| `results/narrative-vs-go.md`, `results/hard-cases.md` | The two qualitative analyses. |
| `affinage_deep_research.py` | **HUMAN-ONLY** tool that emits an Affinage record as an AIGR `-deep-research-affinage.md` source file (see below). |
| `results/example-GPX4-deep-research-affinage.md` | Demo output of that tool. |

## Rerun the comparison

```bash
python compare_affinage.py --genes-file pilot-genes.txt   # uses cache
python compare_affinage.py --refresh GPX4 TP53            # force re-fetch
python compare_affinage.py --genes-file batch4-genes.txt --out-dir results/batch4
```

Requires only Python 3 stdlib + `pyyaml` (already a repo dependency) and `curl`.

## Affinage as a deep-research source (human only)

The AIGR review workflow already ingests any `genes/<sp>/<GENE>/<GENE>-deep-research-*.md`
file, so no pipeline change is needed to "wire in" Affinage — this tool just writes one:

```bash
python affinage_deep_research.py human GPX4            # print to stdout
python affinage_deep_research.py human GPX4 --write    # -> genes/human/GPX4/GPX4-deep-research-affinage.md
```

It is deliberately scoped to the **only** use the [evaluation](results/narrative-vs-go.md)
endorses — a *free precomputed first pass for the human backlog* — and enforces the two
required gates:

1. **Human only.** Refuses any other species (Affinage is human-only).
2. **Trust gates surfaced, never hidden.** It writes Affinage's own `evaluation.pairwise`
   self-signal, compares the record's UniProt accession to the local `<GENE>-uniprot.txt`,
   and scans the narrative's opening for a non-human organism token; any tripped gate
   becomes a ⚠️ CAUTION banner at the top of the file (see the ADA symbol-collision case).

The emitted file records the raw `mechanism_profile` GO ids **only for reference**, with an
explicit note *not* to import them directly (the evaluation showed that layer is coarse and
can contradict the narrative). It is external, LLM-generated preliminary research — treat it
like a falcon/perplexity report, not a curated annotation.

## Caveats

- Exact-GO-id agreement only; it **understates** agreement where Affinage grounds
  to a true GO ancestor of the curated term (the dominant pattern — read
  qualitatively on the project page).
- The local AIGR references are mixed-maturity, not independently expert-signed
  ground truth.
- n=12 pilot: illustrative, not a powered benchmark.
