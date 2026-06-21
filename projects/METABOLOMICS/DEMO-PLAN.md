---
title: "Interactive Demo — Plan & Architecture"
---

# Interactive Demo — Plan & Architecture

Planning sub-doc for the
[Metabolomics × GO/GO-CAM project](../METABOLOMICS.md). It answers one question:
**what is the best path from the working [`probe/`](probe/README.md) pipeline to
an interactive demo that lets someone interpret their own metabolomics data with
GO?** — and where that demo should live.

## TL;DR recommendation

1. **The full interactive app does not belong on the static Pages site.** Live,
   arbitrary-input enrichment needs server-side compute and ~tens of MB of
   reference indices (GO closure, the human-enzyme table, the Rhea network). A
   static page cannot do that per request.
2. **But a precomputed *showcase* does belong here**, and is the right first
   step: ship the MTBLS1 (and a few more) results as static JSON + a small
   client-side viewer on `ai4curation.io/ai-gene-review/`. Zero infra, immediate,
   and it nails the UX before any server exists.
3. **Build the interactive app in a new repo** (`ai4curation/metabolomics-go-demo`)
   as a small **FastAPI service** wrapping the existing engine, with a
   **lightweight frontend** that can be embedded back into the Pages site.
   Deploy to **Hugging Face Spaces** (Docker) or Render/Fly.
4. **Keep the engine here.** The [`probe/`](probe/README.md) modules are the
   reproducible scientific core; the app repo depends on them (pip install from a
   pinned tag), so the science stays version-controlled with the curation work
   and the app stays a thin, redeployable shell.

## Why not a static page (the hard constraint)

The current pipeline, per request, needs:

| Need | Source | Why it blocks pure-static |
|---|---|---|
| ChEBI protonation/skeleton normalization | OLS4 (live, cached) | per-metabolite API calls; CORS + latency |
| Rhea reaction network + `rhea2go` | Rhea REST / GO | ~18.6k reactions; rebuilt index |
| GO closure | `go-basic.obo` (32 MB) | too big to parse client-side per visit |
| Human enzyme → Rhea + GO-BP | UniProt REST | ~4.1k entries, paginated |
| KEGG pathway membership | KEGG REST | **licensing** (see Risks) + CORS |
| Hypergeometric ORA + BH-FDR | compute | fine anywhere, but needs the indices above |

Pyodide/WASM "run it all in the browser" is tempting but a trap here: the public
APIs do not all send permissive CORS headers, and shipping a 32 MB OBO + the
UniProt table to every visitor is slow. So: **static for precomputed results,
a server for live arbitrary input.**

## What the demo should let a user do

Three input modes, increasing in ambition:

1. **Pick an example study** from a dropdown (MTBLS1 + a handful) → instant
   precomputed results. *(works statically)*
2. **Paste a metabolite list** — names or ChEBI ids, or a pasted MAF column →
   live normalization + enrichment. *(needs the app)*
3. **Enter a MetaboLights accession** → fetch its MAF, extract ChEBI, run.
   *(needs the app)*

Output panels (the actual value on screen):

- **Coverage / normalization** — per-metabolite tier (`exact` → `protonation` →
  `skeleton` → miss) and the matched Rhea form. A small Sankey or stacked bar
  makes the protonation insight (0→49→58 on MTBLS1) immediately legible. This
  panel *is* the headline finding.
- **Three-way enrichment** — side-by-side ranked tables: **KEGG pathway**, **GO
  molecular function**, **GO biological process**, each with fold + FDR, GO/KEGG
  ids linked out. The point lands when they sit next to each other.
- **Network view (stretch)** — interactive metabolite → reaction → enzyme → GO
  graph (Cytoscape.js), click a metabolite to highlight its enzymes and
  enriched terms.
- **GO-CAM causal view (future, Approach B)** — trace a perturbed metabolite as
  an activity input/output through a curated causal model.
- **Shareable permalink** — encode the input set in the URL so a result is
  citable.

## Architecture options

| Option | Where | Interactivity | Effort | Verdict |
|---|---|---|---|---|
| **A. Precomputed static gallery** | this repo / Pages | example studies only | Low (~1 day) | **Do now (Phase 1)** |
| B. Pyodide in-browser | Pages | full, client-side | Med–High | Avoid — CORS + payload size |
| **C. Streamlit app** | new repo / HF Spaces | full | Med (~3–5 days) | Good MVP if speed matters |
| **D. FastAPI service + static frontend** | new repo (API) + Pages (UI) | full, embeddable | Med–High (~1–2 wk) | **Target (Phase 2)** |

**Recommendation: A now, then D** (with C as an acceptable shortcut to a first
live MVP). D is preferred over C for longevity because the JSON API is reusable
(notebooks, other front-ends) and the frontend can be **embedded directly in the
Pages site**, resolving the "belongs on the page vs needs an app" tension: the UI
lives on `ai4curation.io`, calling a small hosted API.

## Repository strategy

```
ai4curation/ai-gene-review                 (this repo — unchanged role)
  projects/METABOLOMICS/                    methodology, results, provenance
    probe/                                  the ENGINE (reproducible reference)
  pages/projects/METABOLOMICS/showcase/     Phase-1 precomputed static gallery

ai4curation/metabolomics-go-demo            (NEW repo — the app)
  engine: depends on the probe package (pinned tag) or vendors it
  api/    FastAPI: /normalize /coverage /enrich /study/{acc}
  web/    static frontend (also embeddable into the Pages site)
  data/   prebuilt indices (built in CI, see below)
  Dockerfile  -> Hugging Face Spaces / Render / Fly
```

To make the engine installable, lightly refactor [`probe/`](probe/README.md) into
a package (`metabolomics_go`) with a clean function API
(`normalize()`, `coverage()`, `enrich(aspect=…)`) — the CLIs become thin wrappers.
That refactor is also good hygiene for this repo.

## Data & caching strategy (the make-or-break detail)

Per-request latency must be small, so the heavy reference data is **prebuilt
offline** (a scheduled CI job) into compact artifacts shipped with the app:

| Artifact | Built from | ~size | Refresh |
|---|---|---|---|
| `rhea_participant_index` | Rhea REST | small | monthly |
| `reaction_to_go` (`rhea2go`) | GO external2go | small | monthly |
| `reaction_to_human_enzyme` + `enzyme_to_go_bp` | UniProt REST | ~MB | monthly |
| `go_bp_closure` | `go-basic.obo` | ~MB (pickled ancestors) | monthly |
| `kegg_pathway_compounds` | KEGG REST | small | see licensing |
| `chebi_normalization_cache` | OLS4 (warm) | grows | persistent disk |

Per request the app then only does: **normalize the user's metabolites**
(OLS4, cached → mostly hits) + **stats** (fast). A prebuilt SQLite/Parquet of
the ChEBI protonation+skeleton families for the few thousand common metabolites
makes the common case instant; arbitrary metabolites fall back to live OLS4 with
write-through caching.

## Phased plan

**Phase 1 — Precomputed static showcase (in this repo, ~1 day).**
- Emit the probe results as `showcase/<study>.json` (coverage tiers + 3 enrichment
  tables) for MTBLS1 + 2–3 more studies.
- A single `showcase/index.html` + vanilla JS renders the coverage bar and the
  three side-by-side tables. Lives under `pages/projects/METABOLOMICS/showcase/`.
- Deliverable: a clickable demo on the existing site, no server. Validates UX.

**Phase 2 — Live app MVP (new repo, ~1 week).**
- Package the engine; build the prebuilt indices + CI refresh.
- FastAPI: `/normalize`, `/coverage`, `/enrich`, `/study/{acc}`.
- Frontend: paste-a-list + pick-a-study; render the same panels live.
- Deploy to HF Spaces (Docker). Embed the frontend into the Pages site via an
  `<iframe>` or by hosting the static UI on Pages and pointing it at the API.

**Phase 3 — Polish & depth (stretch).**
- Cytoscape network view; permalinks; CSV/MAF upload; multiple organisms for BP.
- GO-CAM causal trace (Approach B) once the GO-CAM inventory exists.

## Risks & constraints

- **KEGG licensing.** ChEBI, Rhea, GO, UniProt, MetaboLights are open
  (CC-BY / CC0) and fine to cache and redistribute in a demo. **KEGG is not** —
  KEGG REST is free for academic *use* but its data has redistribution
  restrictions. For a public app: keep KEGG as an **optional, live-fetched**
  baseline (don't bundle/redistribute KEGG tables), or swap the baseline to an
  open pathway source (**Reactome** / **SMPDB**) to avoid the issue entirely.
  Flag this prominently in the UI.
- **API rate limits / etiquette.** A public app must not proxy every click to
  OLS4/UniProt/Rhea. The prebuilt-index + persistent-cache design above is what
  keeps it polite and fast; add a request cap + cache-by-input.
- **CORS.** Several upstreams don't set permissive CORS, which is exactly why the
  browser calls them *through* the FastAPI backend rather than directly.
- **BP is organism-specific.** The GO-BP enrichment routes through human enzymes;
  the app should expose an organism selector (default human) and say so.
- **Normalization latency on cold input.** First-seen metabolites incur OLS4
  round-trips; mitigate with the prebuilt common-metabolite table + a spinner +
  write-through cache.

## Open questions for sign-off

- **Baseline:** keep KEGG (with the licensing caveat) or switch to Reactome/SMPDB
  for a cleanly redistributable demo?
- **Frontend taste:** fastest-MVP (Streamlit) vs embeddable-on-Pages
  (FastAPI + static UI)? The doc recommends the latter.
- **Hosting:** Hugging Face Spaces (simplest for a Python demo) vs Render/Fly?
- **Scope of v1:** is "paste a list / pick a study → coverage + 3-way enrichment"
  the right MVP cut, deferring the network and GO-CAM views to Phase 3?
