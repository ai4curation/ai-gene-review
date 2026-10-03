---
title: "Boolean models — sources and tooling landscape"
maturity: SCOPING
tags: [PIPELINE]
autolink_gene_symbols: false
---

# Sources and tooling landscape

Companion to [BOOLEAN_MODELS](../BOOLEAN_MODELS.md). Everything below was checked
from this container on 2026-09-26 (API calls, downloads, package installs); facts
that could not be verified are marked as such.

## What a Boolean model is, for this project

A Boolean (logical) model is a set of variables, each with an update rule that is a
Boolean function of its regulators; the regulatory graph is the signed dependency
graph of those rules. Its behaviour is the set of **attractors** (fixed points and
cyclic/complex attractors) under an update scheme (synchronous, or asynchronous as
used by GINsim and most published models). The SBML Level 3 **qual** package is the
interchange standard ([PMID:24321545](https://pubmed.ncbi.nlm.nih.gov/24321545/)), and
BoolNet `.bnet` text (`target, factors`) is the de facto lightweight format.

The relevance to a curation KB: a module's `connections` graph *is* a regulatory graph
with signs, so a Boolean network is the cheapest dynamical reading of a module, and
the published Boolean models are hand-curated signed wiring for many of the same
pathways.

## External sources

| Source | What it holds | Access from here | Boolean-model relevance |
|---|---|---|---|
| **SIGNOR 3.0** ([PMID:36243968](https://pubmed.ncbi.nlm.nih.gov/36243968/)) | Signed, mechanism-typed causal relations between proteins/complexes/families/phenotypes, curated with PMID + sentence; about 130 named pathways | `getPathwayData.php?pathway=SIGNOR-EGF&relations=only` returns a TSV; `?list` lists pathways. Works from this container. CC BY 4.0. | Not a Boolean model, but exactly the signed-edge layer a Boolean regulatory graph is built from. SIGNOR's own Boolean pipeline goes SIGNOR → CaSQ → SBML-qual ([PMID:32403123](https://pubmed.ncbi.nlm.nih.gov/32403123/)). Snapshot: `models/boolean/signor/SIGNOR-EGF.tsv` (102 rows, 61 unique signed pairs; P38 143 rows, SAPK-JNK 72, NFKBC 44, TA 68). |
| **BioModels** ([PMID:31701150](https://pubmed.ncbi.nlm.nih.gov/31701150/)) | Published models incl. SBML-qual logical models | REST search works via `https://www.ebi.ac.uk/biomodels/search?query=...&format=json` with an `Accept: application/json` header (the bare URL redirects to `www.biomodels.org` and loses the format). A free-text `Boolean` query returns 37 models; the `modellingapproach` facet counts 16 *logical model* and 13 *boolean model* entries (overlapping). Facet-filtered queries with quoted values were rejected by the proxy path and need the web UI or a different encoding. Model files download from `/biomodels/model/download/<id>?filename=...`. | Manually curated SBML-qual examples: `BIOMD0000000562` (Chaouiya 2013 EGF/TNFα demo, 28 qualitative species), `MODEL2106070001` (Montagud 2022 prostate cancer), `MODEL1611180000` (Verlingue 2016 S-phase entry), `MODEL2006170001`/`MODEL2006170002` (Regan/Sizek cell-cycle–apoptosis models), `MODEL2304070002` (Ruscone 2023 tumour invasion). |
| **BBM — Biodivine Boolean Models** (Pastva et al., bioRxiv 10.1101/2023.06.12.544361) | 285 logically consistent real-world Boolean networks harvested from GINsim, Cell Collective, BioModels and papers, each as `.bnet`/`.aeon`/`.sbml` with metadata and a `summary.csv` | `raw.githubusercontent.com/sybila/biodivine-boolean-models/main/models/…` works from here (github.com HTML pages do not). | The most convenient corpus: uniform format, inputs explicit, provenance JSON. MAPK-relevant entries: 070 MAPK-CANCER-CELL-FATE (Grieco 2013), 089–091 its reductions, 018 EGFR-ERBB, 136 EGF-TNFα, 012/032/080 T-cell receptor, 020/111/138 apoptosis, 219 WNT-PI3K-AKT. Snapshot: `models/boolean/bbm-070-mapk-cancer-cell-fate/`. |
| **GINsim model repository** ([PMID:29971008](https://pubmed.ncbi.nlm.nih.gov/29971008/)) | The canonical multi-valued/Boolean logical models (`.zginml`) | `ginsim.org` TLS handshake fails from this container; use BBM's mirror or bioLQM offline. | Original source of many BBM entries (e.g. Grieco 2013 = `ginsim.org/node/173`). |
| **Cell Collective** ([PMID:22871178](https://pubmed.ncbi.nlm.nih.gov/22871178/), REST API [PMID:26589448](https://pubmed.ncbi.nlm.nih.gov/26589448/)) | Community-built logical models with per-edge literature annotation | `api.cellcollective.org` is not reachable through the proxy (502). | Its edge-level citations would be the natural counterpart to module `evidence`; reachable only via BBM copies for now. |
| **GO-CAM** (in-repo `gocams/`, [PMID:31548717](https://pubmed.ncbi.nlm.nih.gov/31548717/)) | 2,036 cached production causal-activity models with `causal_associations` (RO relations such as *directly positively regulates*, *provides input for*) | Local cache; `gocams/index.tsv` joins gene products to activities. | A GO-CAM is already a signed causal graph over activities and translates by the same rule as a module (RO relation → sign). Human MAPK-relevant models exist (e.g. `65d7e4ac00001732`, `685de18700001720`) but are receptor-specific slices rather than the whole cascade. |
| **Reactome** (in-repo `reactome/`) | Reaction-level pathway diagrams; SBML-qual export via CaSQ-style tools exists in the literature | Local cache. | Reaction graphs are not regulatory graphs; a Boolean reading needs the CaSQ transformation (AND reactants, OR activators, AND-NOT inhibitors). Out of scope for the first pass. |

## Tooling

All Python packages below installed into a scratch virtualenv from PyPI through the
container proxy and imported successfully; `uv run --with biodivine-aeon` also works
as an ephemeral overlay on the project environment (this is how the demo runs).

| Tool | Role | Notes |
|---|---|---|
| **biodivine-aeon** (AEON.py, [PMID:36102786](https://pubmed.ncbi.nlm.nih.gov/36102786/)) | Symbolic (BDD) attractor analysis of asynchronous Boolean networks; reads/writes `.bnet`, `.aeon`, SBML-qual; infers a signed regulatory graph from rules (`infer_valid_graph`) | Used by the demo. Free inputs (rules omitted) are treated as *parameters*, so fix them to constants before computing attractors or every input combination is folded into one "coloured" attractor. Attractor projection is done symbolically by intersecting with `mk_subspace`. Computes the 53-variable Grieco model in ~1 s. |
| **mpbn** | Most-permissive Boolean network semantics (Paulevé lab); attractor/reachability via ASP | Installs (`pip install mpbn`), needs clingo wheel; not used yet. Reference to cite when the most-permissive semantics is adopted. |
| **PyBoolNet** ([PMID:27797783](https://pubmed.ncbi.nlm.nih.gov/27797783/)) | Trap spaces, model checking (NuSMV), primes | Installable; heavier native deps. |
| **bioLQM** ([PMID:30510517](https://pubmed.ncbi.nlm.nih.gov/30510517/)) / **GINsim** | Java toolkit: format conversion (zginml ↔ SBML-qual ↔ bnet ↔ BoolNet), Booleanisation of multi-valued models | Reference converters; would need a JVM here. |
| **CoLoMoTo notebook** ([PMID:29971009](https://pubmed.ncbi.nlm.nih.gov/29971009/)) | Docker image bundling all of the above with reproducible notebooks | The right vehicle for a shareable, reproducible analysis once the pipeline stabilises. |
| **MaBoSS** ([PMID:28881959](https://pubmed.ncbi.nlm.nih.gov/28881959/)) | Stochastic continuous-time Boolean simulation (probabilities of phenotypes) | For phenotype-probability read-outs (e.g. proliferation vs apoptosis) rather than attractor enumeration. |
| **CaSQ** ([PMID:32403123](https://pubmed.ncbi.nlm.nih.gov/32403123/)) | Map (SBGN/CellDesigner, SIGNOR) → Boolean model with the default rule *AND reactants, OR activators, AND NOT inhibitors* | The default-rule convention adopted by `module_boolean.py`; the tool itself targets SBGN maps. |
| **boolean.py** | Boolean expression algebra | Not needed; `module_boolean.py` carries a 60-line parser/evaluator sufficient for `.bnet` rules. |

## Formats

- **`.bnet`** (BoolNet): `targets, factors` header then `x, expr` lines; `&`, `|`, `!`,
  parentheses. Inputs are conventionally `x, x`. `module-to-bnet` writes this.
- **SBML-qual**: XML with `qual:qualitativeSpecies` and `qual:transition`
  elements whose `functionTerm`s are MathML. The demo emits it through aeon
  (`BooleanNetwork.to_sbml()`), so no MathML writer is needed in this repo.
- **`.aeon`**: AEON's native text (regulations with signs + functions).
- **`.zginml`**: GINsim XML (multi-valued); convert with bioLQM.
