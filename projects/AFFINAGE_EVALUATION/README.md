# AFFINAGE_EVALUATION — supporting material

Reproducible comparison of Affinage (affinage.wi.mit.edu) `mechanism_profile` GO
terms against the local AIGR reviews. Project page: [`../AFFINAGE_EVALUATION.md`](../AFFINAGE_EVALUATION.md).

## Layout

| Path | What |
|------|------|
| `compare_affinage.py` | Fetch Affinage JSON (cached, trimmed) + diff vs GOA/`core_functions`, exact and `goslim_generic`-level (closure over the pinned GO release `cache/ontologies/go-basic-2026-03-25.obo`, fetched and checksum-verified on demand by `ai_gene_review.bioreason_ontology.ensure_frozen_go`). No hard-coded numbers. |
| `pilot-genes.txt` | The 12-gene human pilot cohort (one symbol per line). |
| `affinage-cache/<SYM>.json` | Cached Affinage API responses, **trimmed** (by `trim_record`) to the fields we use: `gene`, `run_date`, `narrative.mechanism_profile`, `timeline.current_model`, `prefetch_data.uniprot` (accession/full_name), `evaluation`, `cost.total_usd`. All **42** cohort records are committed (fetched 2026-09-27; Affinage run dates 2026-06-09/10; NDUFA4's record is keyed `COXFA4` by Affinage but cached under the requested symbol). Re-fetching reproduced every previously committed GO set exactly. `--offline` never hits the API; `--refresh` re-fetches and re-trims. |
| `results/per-gene.json` | Full per-gene comparison (GO sets, shared ids, core-MF capture). |
| `results/summary.csv` / `results/summary.md` | Generated summary tables. |
| `batch{2,3,4}-genes.txt` / `results/batch{2,3,4}/` | Extended, stress-test, and hard-case cohorts. |
| `retrieval_recall.py` | Affinage retrieval recall against finished reviews (PAINT campaign). `--split-file` reports a gene subset separately. |
| `results/paint-campaign/campaign-genes.txt` | The pinned 91-gene recall cohort (reconstructed from the first committed `per-gene.json`; `--all` now scores every committed report and is a different, growing set). |
| `fa-cohort-genes.txt` | The 22 Fanconi-anemia genes whose reviews folded in Affinage papers; used with `--split-file` to keep them out of recall headlines. |
| `results/narrative-vs-go.md`, `results/hard-cases.md` | The two qualitative analyses. |
| `affinage_deep_research.py` | **HUMAN-ONLY** tool that emits an Affinage record as an AIGR `-deep-research-affinage.md` source file (see below). |
| `results/example-<GENE>-deep-research-affinage.md` | Committed demo outputs (GPX4, ABCA1, ACADM, ADA, ACAT1). Kept under `results/` — **not** in the live `genes/` tree — so a future review can't ingest a wrong-protein record (see `results/backlog-slice.md`). |

## Rerun the comparison

```bash
uv run python compare_affinage.py --offline --genes-file pilot-genes.txt   # uses cache only
uv run python compare_affinage.py --refresh GPX4 TP53                      # force re-fetch
uv run python compare_affinage.py --offline --genes-file batch4-genes.txt --out-dir results/batch4
uv run python compare_affinage.py --no-slim --genes-file pilot-genes.txt   # exact-id only

# retrieval recall, pinned 91-gene cohort, FA reported separately
uv run python retrieval_recall.py --genes-file results/paint-campaign/campaign-genes.txt \
    --split-file fa-cohort-genes.txt --split-name FA
```

Needs `pyyaml` and `curl`, plus the repo package (for the pinned GO release) unless
`--no-slim` or `--go-obo PATH` is given. The GO release (~32 MB) is gitignored and is
downloaded and SHA-256-checked on first use.

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

- Affinage emits only `goslim_generic` terms (43/43 distinct ids across the 42 genes),
  so exact-id capture is near-impossible by construction; read the slim-level columns.
  Slim capture counts a gene if *any* core MF's bin is emitted, which is lenient for
  genes with many core MFs; the top-supported-MF column is the stricter check.
- The local AIGR references are agent-made reviews, not independently expert-signed
  ground truth; the FA-cohort reviews had Affinage input by design.
- 42 genes across four cohorts: illustrative, not a powered benchmark.
