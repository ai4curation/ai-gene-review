---
title: "Metabolomics Interpretation — Tools Landscape"
---

# Metabolomics Interpretation — Tools Landscape

Supporting survey for the
[Metabolomics Interpretation with GO and GO-CAM](../METABOLOMICS.md) project.
The goal is to map what existing metabolomics-interpretation tools do, where
they get their networks/identifiers, and **which parts are reusable** versus
**where GO / GO-CAM can add something they currently lack**.

## The standard untargeted-metabolomics interpretation pipeline

```
raw spectra (LC-MS / NMR)
  → feature table (m/z, RT, intensity)
     → metabolite annotation  (formula/adduct → compound; ChEBI / HMDB / KEGG / RefMet)
        → statistics           (differential abundance: significant metabolite set)
           → interpretation     (pathway / set enrichment)   ← GO is absent here
```

The interpretation step is where this project intervenes. Today it is served by
metabolite-centric set databases (KEGG, SMPDB) and, for MS1 peak lists,
network methods (mummichog). GO is not used because GO annotates gene products,
not compounds — the bridge has to be built through reactions (Rhea/Reactome,
which are written in ChEBI).

## Tool-by-tool

### MAGI — Metabolite Annotation and Gene Integration (LBNL)

- **What:** Computes a **metabolite↔gene association score** by propagating
  evidence across a biochemical **reaction network**: a candidate compound
  identity is reinforced if a nearby gene's predicted enzyme activity consumes/
  produces it, and vice-versa. Improves *both* compound IDs and genome
  enzyme annotations by maximizing consensus.
- **Provenance:** LBNL (Trent Northen, Benjamin Bowen, Oliver Rübel, Markus de
  Raad). Validated on *Streptomyces coelicolor* A3(2). PMID:30896917.
- **Why it matters here:** MAGI is the closest existing analogue to what we
  want — it already lives in the metabolite-reaction-gene space. It does **not**
  attach GO semantics. **Reuse:** the consensus-scoring idea; **add:** map the
  reactions to GO MF via `rhea2go`/`ec2go` and lift genes to GO BP so the
  associations become GO-interpretable and multi-omics-joinable (Approach C).

### mummichog (Emory; Li lab)

- **What:** For untargeted MS1 data, maps **every plausible** formula/adduct
  match of each peak onto a **genome-scale metabolic network**, then tests for
  **local network enrichment**. The trick: true metabolites cluster in the same
  pathway neighbourhood, false matches scatter randomly — so structure in the
  network reveals real activity *without* committing to single compound IDs
  first.
- **Provenance:** Li et al., PLoS Comput. Biol. 2013; re-implemented in R inside
  MetaboAnalyst's "MS Peaks to Pathways".
- **Why it matters here:** mummichog's **permutation/null-model framework** is
  directly reusable. Its network is reaction-only (no causal direction, no
  regulation). **Add:** substitute or augment with **GO-CAM** curated causal
  networks (Approach B) — same local-enrichment logic, but over edges that carry
  direction and regulation.

### MetaboAnalyst (Xia / Wishart)

- **What:** The dominant web platform for metabolomics interpretation. Modules:
  ORA, **MSEA** (Metabolite Set Enrichment Analysis), pathway analysis over
  **KEGG** and **SMPDB**, "MS Peaks to Pathways" (mummichog + GSEA), and
  multi-omics integration. Knowledgebase: five curated genome-scale models plus
  ~21 KEGG-derived organism models; metabolite sets from HMDB/SMPDB.
- **Why it matters here:** It defines the **UX and statistical expectations** of
  the field. **Reuse:** enrichment statistics and reporting conventions;
  **add:** a GO-BP enrichment backend (Approach A) so GO results are comparable
  side-by-side with the SMPDB/KEGG outputs analysts already trust.

### SMPDB & HMDB (Wishart group)

- **SMPDB** — Small Molecule Pathway Database: curated human small-molecule
  metabolic and signalling pathways; the set source behind MetaboAnalyst's
  pathway/MSEA modules.
- **HMDB** — Human Metabolome Database: ~exhaustive human metabolite catalogue
  with ChEBI/KEGG/PubChem cross-references and pathway links.
- **Why they matter here:** They are the **incumbent** GO-free interpretation
  resources — the baseline any GO-based method must be compared against. Their
  **ChEBI/KEGG cross-refs** are also part of the identifier bridge.

### Metabolomics Workbench (NIH / UCSD)

- **What:** Public repository of metabolomics studies plus a **Metabolite
  Database** (~174k entries, aggregated from LIPID MAPS, ChEBI, HMDB, KEGG,
  PubChem, etc.) and **RefMet**, a standardized reference nomenclature spanning
  ~500k MS/NMR annotations at four levels of structural resolution.
- **Why it matters here:** **RefMet → ChEBI** is a clean, programmatic on-ramp
  for turning a real study's messy metabolite names into the ChEBI IDs the
  Rhea/GO bridge needs.

### MetaboLights (EBI)

- **What:** EBI's open metabolomics repository (raw data + metadata,
  cross-species, cross-technique). During curation, metabolite names are
  assigned **ChEBI** identifiers (with new compounds submitted to ChEBI).
- **Why it matters here:** The most **ChEBI-grounded** public study source —
  ideal for a demonstration dataset, because the metabolites already carry the
  identifier the whole GO bridge keys on.

## The identifier bridge (why ChEBI is the linchpin)

| Layer | Resource | Identifier |
|-------|----------|-----------|
| Study metabolite | MetaboLights / Workbench | name → **RefMet** → **ChEBI** |
| Reaction | **Rhea** (also Reactome) | participants are **ChEBI** |
| Enzyme activity | **GO MF** | via `rhea2go` (`GO_REF:0000116`) / `ec2go` |
| Gene product | GOA | UniProt + GO |
| Pathway / causal context | **GO-CAM** | activity inputs/outputs are **ChEBI** |

Every hop is keyed on ChEBI or on a mapping this repository already maintains
(`rhea2go`, `ec2go`; see the [RHEA project](../RHEA.md)). That is what makes a
GO-native metabolomics interpretation feasible without inventing new mappings.

## Reuse vs build — summary

| Component | Source | Action |
|-----------|--------|--------|
| Metabolite name → ChEBI | RefMet / MetaboLights | **adopt** |
| ChEBI → Rhea reactions | Rhea API / local | **build** (small probe) |
| Rhea → GO MF | `rhea2go` (RHEA project) | **reuse** |
| GO MF/gene → GO BP | GOA / OLS | **reuse** |
| Closure-aware ORA | standard | **build** thin layer |
| MS1 peak null model | mummichog | **adopt** framework |
| Causal-network trace | GO-CAM / gocam-py | **build** demo |
| Metabolite↔gene consensus | MAGI | **adopt** idea, **add** GO labels |

## Sources

- MAGI — https://pubs.acs.org/doi/10.1021/acschembio.8b01107 (PMID:30896917)
- mummichog — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3701697/
- MetaboAnalyst 6.0 — https://academic.oup.com/nar/article/52/W1/W398/7642060
- MetaboAnalyst functional-analysis vignette —
  https://www.metaboanalyst.ca/resources/vignettes/Functional_Analysis_global_metabolomics.html
- Metabolomics Workbench / RefMet —
  https://www.metabolomicsworkbench.org/databases/refmet/index.php
- MetaboLights — https://pmc.ncbi.nlm.nih.gov/articles/PMC10767962/
- GO-CAM — https://pmc.ncbi.nlm.nih.gov/articles/PMC7012280/ (PMID:31548717)
- GO-CAM metabolic phenotypes (Genetics 2023) —
  https://academic.oup.com/genetics/article/225/2/iyad152/7242464
