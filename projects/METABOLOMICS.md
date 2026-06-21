---
title: "Metabolomics Interpretation with GO and GO-CAM"
maturity: SCOPING
tags: [PIPELINE]
---

# Metabolomics Interpretation with GO and GO-CAM

## Overview

This project explores **how the Gene Ontology (GO) and GO Causal Activity Models
(GO-CAMs) can be used to interpret metabolomics data** — for example the
differential-abundance metabolite lists that come out of studies deposited in
[MetaboLights](https://www.ebi.ac.uk/metabolights/) (EBI) and the
[Metabolomics Workbench](https://www.metabolomicsworkbench.org/) (NIH). The
guiding question is deliberately practical:

> Can we adopt or build something that demonstrates concrete value of GO /
> GO-CAM for interpreting metabolomics data, beyond the KEGG/SMPDB pathway
> enrichment that is standard today?

There are two complementary handles, matching the two things GO has that a flat
pathway database does not:

1. **Reaction-grounded enzyme activities.** GO molecular-function terms *are*
   enzyme activities, and via **Rhea** (whose reaction participants are
   **ChEBI** compounds) plus the `rhea2go` mapping, a *metabolite* can be linked
   to the GO MF terms of the enzymes that produce/consume it, and onward to the
   GO biological processes those enzymes participate in. This is exactly the
   forward direction already characterised in the
   [RHEA → GO project](RHEA.md) — here we run it *from the metabolite side*.
2. **The full curated causal network.** GO-CAM models of metabolic processes
   already encode enzyme activities **connected by their shared input/output
   ChEBI molecules** and by regulation edges. A GO-CAM *is* a curated
   metabolite-reaction-gene network with causal direction — the missing
   ingredient in the reaction-only networks that drive tools like mummichog.

The core technical insight is that **ChEBI is the bridge**. Metabolomics
repositories curate metabolite identities to ChEBI; Rhea reactions are written
in ChEBI; GO-CAM activity inputs/outputs are ChEBI; and `rhea2go` / GOA carry
those reactions up to GO MF/BP and to gene products. So a chain already exists:

```
metabolite (ChEBI)
   → reaction (Rhea, ChEBI participants)
      → enzyme activity (GO MF, via rhea2go)
         → gene product (GOA)  &  biological process (GO BP)
            → causal pathway context (GO-CAM)
```

The deliverable is to demonstrate that walking this chain gives a metabolomics
analyst something the KEGG/SMPDB enrichment they already run does not:
ontology-structured (closure-aware) enrichment, causal direction and
regulation, and a shared vocabulary with gene-level omics for multi-omics
integration.

**There is a catch that has to be handled first** (and the pilot below confirms
it dominates): Rhea writes participants in their **major protonation state at
pH 7.3** (`citrate(3-)`, `ATP(4-)`, `succinyl-CoA(5-)`), whereas metabolomics
repositories report the **neutral** species (`citric acid`, `ATP`). A direct
ChEBI-id match between the two therefore fails almost completely. The fix is to
expand each metabolite over ChEBI's `is_protonated_form_of` /
`is_deprotonated_form_of` relations into its **protonation family** before
matching.

## Pilot result — the bridge works, but only after protonation normalization

A reproducible coverage probe ([`probe/`](METABOLOMICS/probe/README.md),
[RESULTS.md](METABOLOMICS/probe/RESULTS.md)) ran the
`metabolite → Rhea → rhea2go → GO` bridge on 26 central-carbon / amino-acid /
nucleotide / cofactor metabolites, reported by **neutral name** as a repository
would. Computed live from OLS4 (ChEBI), the Rhea REST API and GO `rhea2go`:

| Match strategy | Metabolites reaching a Rhea reaction / GO MF |
|---|---|
| **Exact ChEBI id** (neutral, as reported) | **0 / 26** |
| **Protonation-normalized** (ChEBI conjugate family) | **22 / 26** |

So the bridge is **essentially empty without protonation normalization and
near-complete with it** — e.g. neutral `ATP (CHEBI:15422)` matches nothing, but
its family member `ATP(4-) (CHEBI:30616)` (the form Rhea uses) reaches **492 GO
molecular-function terms**; `NAD+` → 447, `acetyl-CoA` → 385. This both
validates the core idea and pins down protonation normalization as a mandatory
preprocessing step for *any* metabolite→GO bridge.

The 4 residual misses (isocitric acid, L-lactic acid, D-glucose, D-glucose
6-phosphate) are themselves informative: they are a **second, distinct**
ID-mismatch class — **stereochemistry/anomer** and **generic-vs-structurally-
specific** ChEBI mismatch — that protonation expansion does not fix, and which a
follow-up must address with tautomer/enantiomer traversal or InChIKey-skeleton
matching.

### Confirmed on a real study (MetaboLights MTBLS1)

The same probe was run on the **curator-assigned ChEBI metabolites of a real
deposited study** — [MTBLS1](METABOLOMICS/probe/studies/MTBLS1-RESULTS.md)
(Salek et al., type-2-diabetes urine NMR), 64 distinct metabolites pulled live
from the study's MAF. Real curated data is heterogeneous (a mix of neutral,
charged and generic forms), so it is a sterner test than the idealized demo set:

| Match strategy | Metabolites reaching a Rhea reaction |
|---|---|
| **Exact ChEBI id** (as the curators recorded) | **8 / 64** |
| **Protonation-normalized** | **49 / 64** |

A **6× uplift** (41 metabolites recovered only by normalization) on real data.
The 8 exact matches are almost all the *uncharged* metabolites (acetone,
ethanol, adenosine, uridine, creatinine, allantoin) plus the one anion the
curator happened to enter charged (`2-oxoglutarate(2-)`) — i.e. exactly the
metabolites with no protonation ambiguity. Everything with an ionisable group
needed normalization.

The biological kicker is in the 15 residual misses: they are dominated by the
**branched-chain amino acids isoleucine, leucine, valine** — *the* canonical
type-2-diabetes biomarkers — plus glutamate, glutamine, histidine,
phenylalanine and citrulline. These are lost not to protonation but because the
curators used the **generic (non-stereospecific) ChEBI ids** (e.g. `isoleucine
CHEBI:24898`) while Rhea uses the **L-stereospecific zwitterion**
(`L-isoleucine zwitterion`). So the metabolites most diagnostically important
for this study fall squarely into the stereochemistry/generic-vs-specific
residual class — a concrete, high-value motivation for the InChIKey-skeleton
normalization follow-up.

## Why GO is not used for metabolomics today (the gap)

GO annotates **gene products**, not metabolites — so out of the box GO says
nothing about a list of m/z features or ChEBI IDs. Consequently the metabolomics
field uses metabolite-centric resources instead:

- **Pathway / set databases:** KEGG pathways, **SMPDB** (Wishart group), HMDB
  classes, RefMet/Lipid-class hierarchies.
- **Enrichment methods:** Over-Representation Analysis (ORA) and **Metabolite
  Set Enrichment Analysis (MSEA)** over those sets, and for untargeted
  (MS1-peak) data the network method **mummichog**, which maps *all plausible*
  formula matches onto a genome-scale metabolic network and looks for *local*
  enrichment (true signal clusters; false matches scatter). These are packaged
  in **MetaboAnalyst** (Xia/Wishart) — "MS Peaks to Pathways" is mummichog
  re-implemented in R over five curated genome-scale models + ~21 KEGG-derived
  organism models.

The gap this project targets: **none of these use GO**, so metabolomics
interpretation lives in a separate ontology universe from the gene-level GO
annotations this repository curates. Bridging them via ChEBI/Rhea/GO-CAM is the
opportunity.

See [METABOLOMICS/TOOLS-LANDSCAPE.md](METABOLOMICS/TOOLS-LANDSCAPE.md) for the
full survey of MAGI, MetaboAnalyst/mummichog, Metabolomics Workbench, MetaboLights
and the Wishart-group resources, with what is reusable vs what we would build.

## Existing tools surveyed

| Tool | Group | What it does | Relevance / reuse |
|------|-------|--------------|-------------------|
| **MAGI** | LBNL (Northen, Bowen, et al.) | Scores **metabolite↔gene** associations through a biochemical **reaction network**, boosting consensus between compound IDs and genome enzyme annotations | Closest in spirit: a metabolite-reaction-gene consensus score. We can attach **GO semantics** (rhea2go MF, GO BP) on top of MAGI-style associations |
| **mummichog** | Li (Emory) | MS1 peaks → all formula matches → genome-scale reaction network → **local network enrichment**; bypasses up-front metabolite ID | Reuse the **permutation / null-model** framework; swap/augment the reaction network with **GO-CAM** curated causal networks |
| **MetaboAnalyst** | Xia / Wishart | Web platform: ORA, **MSEA**, pathway analysis (KEGG/SMPDB), "MS Peaks to Pathways" (mummichog), multi-omics | Adopt the **enrichment UX + statistics**; add a **GO-BP** enrichment backend |
| **SMPDB / HMDB** | Wishart | Curated small-molecule pathways and the human metabolome DB with ChEBI/KEGG cross-refs | Cross-reference target; HMDB↔ChEBI gives the ID bridge into Rhea/GO |
| **Metabolomics Workbench** | NIH (UCSD) | Repository + **RefMet** standardized nomenclature (~500k annotations) + 174k-entry Metabolite DB cross-linked to ChEBI/KEGG/LIPID MAPS | **RefMet → ChEBI** harmonization is the data on-ramp for real study inputs |
| **MetaboLights** | EBI | Open metabolomics repository; curators assign metabolites **ChEBI** IDs during curation | Primary **ChEBI-grounded** study source for a demonstration dataset |

## Proposed approaches (to demonstrate value)

### Approach A — GO biological-process enrichment of a metabolite set (Rhea-grounded)

A GO-native counterpart to SMPDB/KEGG enrichment:

1. Harmonize the study's significant metabolites to **ChEBI** (via RefMet /
   MetaboLights mappings).
2. **Normalize protonation state** — expand each ChEBI compound into its
   protonation family (`is_protonated_form_of` / `is_deprotonated_form_of`) so it
   can match the charged form Rhea uses. The pilot shows this step is *not*
   optional: it moves coverage from 0/26 to 22/26.
3. For each family, collect **Rhea reactions** in which any member is a
   participant.
4. Map those reactions to **GO MF** enzyme-activity terms via `rhea2go`
   (already tooled in the [RHEA project](RHEA.md)), and to genes via GOA.
5. Lift to **GO biological process** (via the enzymes' BP annotations and/or
   GO-CAM context) and run **closure-aware ORA** over the GO BP graph.

The argument for value: GO's `is_a`/`part_of` structure gives principled
closure (no arbitrary pathway boundaries), the same ontology is used for
transcriptomics/proteomics (multi-omics on one vocabulary), and it is
cross-species by construction.

### Approach B — Locate the metabolite in the curated GO-CAM causal network

Use **GO-CAM** as the "full metabolic network" the user asked about:

1. A perturbed ChEBI metabolite is matched to GO-CAM **activity inputs/outputs**.
2. Trace **upstream producing** and **downstream consuming** activities along
   the causal chain, including **regulatory** edges (which mummichog's
   reaction-only network lacks).
3. Report the enzymes/genes and processes whose curated causal neighbourhood is
   enriched for perturbed metabolites — a causal, direction-aware analogue of
   mummichog's local-enrichment idea.

The Genetics 2023 study (human glucose-metabolism GO-CAMs → mouse, mapping
pathway perturbations to phenotypes) is direct precedent that GO-CAM metabolic
models support exactly this kind of perturbation→outcome reasoning.

### Approach C — MAGI-style consensus, GO-annotated

Run a MAGI-style metabolite↔gene consensus over the reaction network, then
**annotate the resulting associations with GO MF/BP** so the output is
GO-interpretable and joinable to gene-level omics. This is the most direct
"adopt an existing tool and add GO" path.

## What we can adopt vs build

- **Adopt:** ChEBI/RefMet harmonization (Workbench RefMet, MetaboLights ChEBI),
  the mummichog permutation/null framework, MetaboAnalyst's enrichment
  statistics + UX patterns, MAGI's reaction-network consensus idea.
- **Build (in this repo):** the `ChEBI → Rhea → rhea2go GO MF → GOA gene → GO
  BP` enrichment, reusing the [RHEA project's](RHEA.md) `rhea2go`/`ec2go`
  tooling; and a GO-CAM "trace the perturbed metabolite" demo. Both are small,
  self-contained, and exercise data we already work with.

## Relationship to other projects in this repo

This sits at the intersection of several existing efforts and reuses their
tooling rather than duplicating it:

- **[RHEA → GO](RHEA.md)** — provides the `rhea2go`/`ec2go` mappings and the
  ChEBI-grounded reaction→GO machinery that Approaches A and C depend on. The
  "rare project" the request alludes to.
- **[Metabolic Model Analysis](METABOLIC_MODEL_ANALYSIS.md)** — genome-scale
  metabolic models (GEMs) are exactly the networks mummichog uses; this project
  found systematic GEM gene-EC representation issues that matter for any
  network-based metabolite interpretation.
- **[UniPathway](UNIPATHWAY.md)** and **[Enzyme Specificity](ENZYME_SPECIFICITY.md)**
  — pathway/reaction representation and substrate-specificity altitude, which
  govern how cleanly a metabolite maps to a single GO MF term.
- **[Reactome Gap Filling](REACTOME_GAP_FILLING.md)** — Reactome is another
  curated, ChEBI-grounded reaction source convertible to/from GO-CAM.

## Open questions

- How many MetaboLights/Workbench study metabolites actually resolve to ChEBI
  IDs that participate in a `rhea2go`-mapped reaction (coverage of the bridge)?
- Does GO-BP enrichment recover the same biology as SMPDB/KEGG enrichment on a
  benchmark study, and where does the GO closure structure add or remove signal?
- Do GO-CAM causal/regulatory edges materially change interpretation versus a
  reaction-only network on the same metabolite set?
- Can GO-CAM metabolic coverage (which processes have models) support a useful
  fraction of typical metabolomics readouts, or is it currently too sparse?

## Follow-Up Targets

| Target | Status | Rationale |
|--------|--------|-----------|
| ChEBI→Rhea→`rhea2go` coverage probe + protonation normalization | **DONE** ([probe](METABOLOMICS/probe/RESULTS.md)) | Bridge connects 22/26 only after protonation normalization (0/26 exact) |
| Run the probe over a real MetaboLights study | **DONE** ([MTBLS1](METABOLOMICS/probe/studies/MTBLS1-RESULTS.md)) | 64 curated metabolites: 8/64 exact → 49/64 normalized (6× uplift); `fetch_metabolights.py` pulls any accession |
| Add stereochemistry/anomer + generic-vs-specific resolution | TODO (high value) | The residual-miss class — and on MTBLS1 it captures the diabetes BCAAs (Ile/Leu/Val) — needs InChIKey-skeleton / tautomer / stereo traversal |
| Lift matched reactions to GO BP + closure-aware ORA | TODO | Turn coverage into a statistical enrichment (Approach A vs SMPDB/KEGG baseline) |
| Inventory GO-CAM metabolic models + their ChEBI input/output compounds | TODO | Feasibility of Approach B (the "full network" path) |
| Glucose-metabolism GO-CAM perturbation worked example | TODO | Direct analogue of the Genetics 2023 precedent |

## References

- **MAGI** — Erbilgin et al., *MAGI: A Method for Metabolite Annotation and Gene
  Integration*, ACS Chem. Biol. 2019. PMID:30896917.
  [ACS](https://pubs.acs.org/doi/10.1021/acschembio.8b01107)
- **GO-CAM** — Thomas et al., *Gene Ontology Causal Activity Modeling (GO-CAM)
  moves beyond GO annotations to structured descriptions of biological functions
  and systems*, Nat. Genet. 2019. PMID:31548717.
  [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7012280/)
- **GO-CAM metabolic phenotypes** — *Biochemical pathways represented by GO
  Causal Activity Models identify distinct phenotypes resulting from mutations in
  pathways*, Genetics 225(2):iyad152, 2023.
  [Genetics](https://academic.oup.com/genetics/article/225/2/iyad152/7242464)
- **mummichog** — Li et al., *Predicting Network Activity from High Throughput
  Metabolomics*, PLoS Comput. Biol. 2013.
  [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3701697/)
- **MetaboAnalyst 6.0** — Pang et al., Nucleic Acids Res. 2024.
  [NAR](https://academic.oup.com/nar/article/52/W1/W398/7642060)
- **MetaboLights** — Yurekten et al., *MetaboLights: open data repository for
  metabolomics*, Nucleic Acids Res. 2024.
  [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767962/)
- **Metabolomics Workbench / RefMet** —
  [Workbench](https://www.metabolomicsworkbench.org/) ·
  [RefMet](https://www.metabolomicsworkbench.org/databases/refmet/index.php)
- **gocam-py** — GO-CAM Python tooling.
  [docs](https://geneontology.github.io/gocam-py/)

## Project Status

- **Started**: 2026-06-21
- **Maturity**: SCOPING — problem framed, tool landscape surveyed, three
  candidate approaches defined around the ChEBI→Rhea→GO→GO-CAM bridge, and a
  **working coverage probe** ([`probe/`](METABOLOMICS/probe/README.md)) that
  confirms the bridge connects (22/26) but only after **protonation
  normalization** (0/26 exact). Enrichment (GO-BP ORA) is the next step.
- **Computed live**: coverage probe over a 26-metabolite demo set **and the 64
  curated metabolites of MetaboLights MTBLS1** via OLS4 (ChEBI), Rhea REST
  (18,558 reactions, 14,251 participant ChEBIs) and GO `rhea2go` (7,746
  mappings); protonation families via ChEBI
  `is_protonated_form_of`/`is_deprotonated_form_of`. MTBLS1: exact 8/64 →
  normalized 49/64.
- **Key idea**: ChEBI is the bridge from metabolite repositories (MetaboLights,
  Workbench/RefMet) into Rhea reactions, `rhea2go` GO molecular functions, GOA
  genes, and GO-CAM causal networks — giving a GO-native, closure-aware,
  multi-omics-compatible alternative/complement to KEGG/SMPDB/mummichog
  enrichment.
</content>
</invoke>
