> **UPDATE:** the co-expression/expression analysis WAS completed via **EBI Expression
> Atlas** (open FTP, Potri-keyed) — see `RESULTS.md` and `ebi_atlas_analysis.py`. The
> PlantGenIE notes below document why that particular route was not usable.

# Poplar CASPL expression analysis — JGI/PlantGenIE access attempt

## Goal
Test the functional hypotheses from the gene reviews against high-throughput poplar
expression data: do `PtCASPL1B/1D` co-express with suberin/lignin modules (suberization
hypothesis) and do `PtCASPL4C1/4C2` co-express with cold-stress modules?

## What was attempted (reproducible probe log)
The poplar expression atlas (P. trichocarpa) lives in **PlantGenIE / PopGenIE** (JGI
`Potri.*` v3.1 models, the "potri" exAtlas), with the wood series in AspWood.

| Resource | Result |
|---|---|
| `https://plantgenie.org` (+ `/api`, `/Phytozome`, `/ftp/`) | **reachable (200)** but `/api` is a web page ("api doesn't exist"); no REST API; `/ftp/` and `/download/` return the site nav, not a file listing |
| `https://ftp.plantgenie.org/` | 503 |
| `https://aspwood.scilifelab.se`, `https://congenie.org` | **000 (unreachable from this environment / network policy)** |
| GenIE-Sys expression endpoint `plugins/eximage/service/eplant_service.php?primaryGene=<Potri>&view=exatlas` | exists, but returns an **empty body** for every gene/view/cookie combination tried |
| `plugins/eximage/service/download.php` | 404 (referenced by old JS; not the live file) |
| KEGG REST (`rest.kegg.jp/get/pop:<id>`) | reachable, but carries no `Potri.*` model IDs (uses NCBI GeneID) |

## Why it could not be pulled programmatically
The expression endpoint requires the **species database to be selected interactively**
in the GenIE-Sys web UI; that selection is stored in server-side PHP `$_SESSION` state
keyed to the browser session. Replaying the `genie_select_species=beta_plantgenie_potri_v31`
and `genie_select_species_abb=potri` cookies (with a fresh `PHPSESSID`) is **not**
sufficient — `eplant_service.php` still returns empty. There is no public REST/bulk API,
and the bulk/FTP and direct AspWood/CoNekT data hosts are network-blocked here.

Per project policy (no scripts that pretend to fetch), the analysis is therefore delivered
as a **parser for the one-click exImage export** rather than a fake fetcher.

## Gene-ID mapping status (`gene_ids.tsv`)
12 / 20 poplar CASPLs map to current `Potri.*` v3.1/v4.1 models via the UniProt
EnsemblPlants cross-reference. The other 8 carry only legacy JGI v2 `POPTRDRAFT_*` IDs
(no EnsemblPlants xref in UniProt); mapping them to `Potri.*` needs a JGI v2→v3 conversion
table that is not reachable from this environment. Those 8 can be resolved manually on
Phytozome (search the `POPTRDRAFT_*` ID) when running the analysis.

## How to complete the analysis (manual export, ~2 min)
1. Open https://plantgenie.org/exImage and select **Populus trichocarpa v3.1**.
2. Add the `potri_v_id` values from `gene_ids.tsv` to the gene basket, plus suberin- and
   cold-marker genes of interest.
3. Download the TSV (`gene_name, sample_name, log2, rmd, log2fc`) to `data/exatlas_export.tsv`.
4. (optional) Add `data/markers.tsv` (`gene_id <tab> category`) for module summaries.
5. `uv run coexpression_analysis.py`

The script (validated end-to-end on synthetic input) builds the gene×sample matrix,
computes Pearson co-expression, ranks each CASPL's top partners, and—if markers are
provided—summarizes mean correlation to each module. It exits cleanly with no output if
no export is present (it never fabricates values).
