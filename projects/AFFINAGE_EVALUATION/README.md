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
| `results/example-<GENE>-deep-research-affinage.md` | Committed demo outputs (GPX4, ABCA1, ACADM, ADA, ACAT1). Kept under `results/` — **not** in the live `genes/` tree — so a future review can't ingest a wrong-protein record (see `results/backlog-slice.md`). |

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
python affinage_deep_research.py human ADA   --write   # refused: wrong-protein gate trips (--force to override)
```

It is deliberately scoped to the **only** use the [evaluation](results/narrative-vs-go.md)
endorses — a *free precomputed first pass for the human backlog*.

**The emitted file is a faithful, unedited rendering of the external-provider record — no
AIGR interpretation.** A `-deep-research-*.md` file reproduces what the provider returned
(like a falcon/perplexity report): Affinage's mechanistic narrative, its own
`mechanism_profile` GO/Reactome grounding, the dated discoveries, and the citations. (A few
emitted fields are mechanical derivations of that content rather than provider fields —
`citation_count` and the `## Citations` list union the discovery PMIDs with the `PMID:NNN`
tokens in the narrative, and `n_discoveries` is a count — but nothing is edited or
adjudicated.) The file carries **no
CAUTION banners, no "these GO terms are coarse, do not import them" advice, and no trust
adjudication** — mixing AIGR's own opinion into the file would launder it into something
that looks like the provider said it. Curatorial judgment of the record — relevance,
correctness, whether to import its GO grounding, and the trust gates below — is the
reviewer's, and belongs in the gene review's `references[].reference_review`
(`relevance` / `correctness` / `review_notes`) and `findings`, **not** in the source file.

The tool still helps the reviewer form that judgment via two checks, printed to **stderr**
(never written into the file):

1. **Human only.** Refuses any other species (Affinage is human-only).
2. **Trust gates (stderr reminder).** It surfaces Affinage's own `evaluation.pairwise`
   self-signal, compares the record's UniProt accession to the local `<GENE>-uniprot.txt`,
   and scans the narrative's opening for a non-human organism token (the ADA symbol-collision
   case). A tripped gate prints a ⚠️ warning telling you to record it in the review's
   `reference_review` — it does not touch the file.
3. **Blocking write gate.** Since the file itself carries no warning, the two *wrong-protein*
   gates (accession mismatch, non-human organism token) also **refuse the write** when the
   destination is inside `genes/` — a record describing a different protein must not land in
   a gene folder, where a later review of that gene would ingest it. Exit is non-zero and
   nothing is written unless `--force` is passed (or `--out` targets a path outside `genes/`).
   The soft `pairwise` gate only warns; it is already in the frontmatter as
   `self_evaluation_pairwise`.

Only factual provenance (source URL, run date, accession, and Affinage's own self-evaluation
numbers) is recorded in the file frontmatter. It is external, LLM-generated preliminary
research — treat it like a falcon/perplexity report, not a curated annotation.

## Caveats

- Exact-GO-id agreement only; it **understates** agreement where Affinage grounds
  to a true GO ancestor of the curated term (the dominant pattern — read
  qualitatively on the project page).
- The local AIGR references are mixed-maturity, not independently expert-signed
  ground truth.
- n=12 pilot: illustrative, not a powered benchmark.
