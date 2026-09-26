---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T13:23:30.499848'
end_time: '2026-07-25T13:47:44.925942'
duration_seconds: 1454.43
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: TreY/TreZ trehalose biosynthesis from alpha-glucan
  module_summary: A reusable two-reaction pathway in which TreY converts the reducing
    end of an alpha-1,4-glucan to a trehalose-containing alpha,alpha-1,1 linkage and
    TreZ hydrolyzes the resulting maltooligosyltrehalose to release trehalose. Alpha-glucan
    synthesis and remodeling, alternative OtsA/OtsB or TreS trehalose routes, and
    trehalose degradation are outside the boundary.
  module_outline: "- TreY/TreZ trehalose biosynthesis from alpha-glucan\n  - 1. maltooligosyltrehalose\
    \ formation\n  - Maltooligosyl trehalose synthase\n    - Maltooligosyl trehalose\
    \ synthase (molecular player: TreY maltooligosyl trehalose synthases; activity\
    \ or role: (1,4)-alpha-D-glucan 1-alpha-D-glucosylmutase activity)\n  - 2. trehalose\
    \ release\n  - Malto-oligosyltrehalose trehalohydrolase\n    - Malto-oligosyltrehalose\
    \ trehalohydrolase (molecular player: TreZ malto-oligosyltrehalose trehalohydrolases;\
    \ activity or role: 4-alpha-D-(1->4)-alpha-D-glucanotrehalose trehalohydrolase\
    \ activity)"
  module_connections: '- Maltooligosyl trehalose synthase feeds into Malto-oligosyltrehalose
    trehalohydrolase: TreY supplies maltooligosyltrehalose to TreZ.'
  pathway_query: ppu00500
  pathway_id: ppu00500
  pathway_name: Starch and sucrose metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00500 with 12 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '18'
  candidate_genes: '- glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase)
    (EC 2.7.1.2; primary bucket kegg:ppu00052)

    - bglX: PP_1403 | Q88N13 | Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside
    glucohydrolase) (Cellobiase) (Gentiobiase) (EC 3.2.1.21; primary bucket kegg:ppu00999)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - pgi1: PP_1808 | Q88LW9 | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9)
    (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) (EC 5.3.1.9;
    primary bucket kegg:ppu00500)

    - bcsA: PP_2635 | Q88JL4 | Cellulose synthase catalytic subunit [UDP-forming]
    (EC 2.4.1.12) (EC 2.4.1.12; primary bucket kegg:ppu00500)

    - pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary
    bucket kegg:ppu00052)

    - galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9)
    (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)

    - glgA: PP_4050 | Q88FN9 | Glycogen synthase (EC 2.4.1.21) (Starch [bacterial
    glycogen] synthase) (EC 2.4.1.21; primary bucket kegg:ppu00500)

    - treZ: PP_4051 | Q88FN8 | Malto-oligosyltrehalose trehalohydrolase (MTHase) (EC
    3.2.1.141) (4-alpha-D-((1->4)-alpha-D-glucano)trehalose trehalohydrolase) (Maltooligosyl
    trehalose trehalohydrolase) (EC 3.2.1.141; primary bucket kegg:ppu00500)

    - malQ: PP_4052 | Q88FN7 | 4-alpha-glucanotransferase (EC 2.4.1.25) (Amylomaltase)
    (Disproportionating enzyme) (EC 2.4.1.25; primary bucket kegg:ppu00500)

    - treY: PP_4053 | Q88FN6 | Maltooligosyl trehalose synthase (EC 5.4.99.15) (EC
    5.4.99.15; primary bucket kegg:ppu00500)

    - glgX: PP_4055 | Q88FN4 | Glycogen debranching enzyme (EC 3.2.1.33) (EC 3.2.1.33;
    primary bucket kegg:ppu00500)

    - glgB: PP_4058 | Q88FN1 | 1,4-alpha-glucan branching enzyme GlgB (EC 2.4.1.18)
    (1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-glucosyl-transferase) (Alpha-(1->4)-glucan
    branching enzyme) (Glycogen branching enzyme) (BE) (EC 2.4.1.18; primary bucket
    kegg:ppu00500)

    - treSB: PP_4059 | Q88FN0 | Maltokinase (EC 2.7.1.175) (EC 5.4.99.16) (Maltose
    alpha-D-glucosyltransferase) (Maltose-1-phosphate synthase) (EC 2.7.1.175; 5.4.99.16;
    primary bucket kegg:ppu00500)

    - glgE: PP_4060 | Q88FM9 | Alpha-1,4-glucan:maltose-1-phosphate maltosyltransferase
    (GMPMT) (EC 2.4.99.16) ((1->4)-alpha-D-glucan:maltose-1-phosphate alpha-D-maltosyltransferase)
    (EC 2.4.99.16; primary bucket kegg:ppu00500)

    - pgi2: PP_4701 | Q88DW7 | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9)
    (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) (EC 5.3.1.9;
    primary bucket kegg:ppu00500)

    - glgP: PP_5041 | Q88CY8 | Alpha-1,4 glucan phosphorylase (EC 2.4.1.1) (EC 2.4.1.1;
    primary bucket kegg:ppu00500)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__trey_trez_trehalose_biosynthesis__ppu00500-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__trey_trez_trehalose_biosynthesis__ppu00500-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

TreY/TreZ trehalose biosynthesis from alpha-glucan in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00500
- Resolved ID: ppu00500
- Resolved name: Starch and sucrose metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00500 with 12 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 18

- glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2; primary bucket kegg:ppu00052)
- bglX: PP_1403 | Q88N13 | Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) (EC 3.2.1.21; primary bucket kegg:ppu00999)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- pgi1: PP_1808 | Q88LW9 | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- bcsA: PP_2635 | Q88JL4 | Cellulose synthase catalytic subunit [UDP-forming] (EC 2.4.1.12) (EC 2.4.1.12; primary bucket kegg:ppu00500)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)
- glgA: PP_4050 | Q88FN9 | Glycogen synthase (EC 2.4.1.21) (Starch [bacterial glycogen] synthase) (EC 2.4.1.21; primary bucket kegg:ppu00500)
- treZ: PP_4051 | Q88FN8 | Malto-oligosyltrehalose trehalohydrolase (MTHase) (EC 3.2.1.141) (4-alpha-D-((1->4)-alpha-D-glucano)trehalose trehalohydrolase) (Maltooligosyl trehalose trehalohydrolase) (EC 3.2.1.141; primary bucket kegg:ppu00500)
- malQ: PP_4052 | Q88FN7 | 4-alpha-glucanotransferase (EC 2.4.1.25) (Amylomaltase) (Disproportionating enzyme) (EC 2.4.1.25; primary bucket kegg:ppu00500)
- treY: PP_4053 | Q88FN6 | Maltooligosyl trehalose synthase (EC 5.4.99.15) (EC 5.4.99.15; primary bucket kegg:ppu00500)
- glgX: PP_4055 | Q88FN4 | Glycogen debranching enzyme (EC 3.2.1.33) (EC 3.2.1.33; primary bucket kegg:ppu00500)
- glgB: PP_4058 | Q88FN1 | 1,4-alpha-glucan branching enzyme GlgB (EC 2.4.1.18) (1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-glucosyl-transferase) (Alpha-(1->4)-glucan branching enzyme) (Glycogen branching enzyme) (BE) (EC 2.4.1.18; primary bucket kegg:ppu00500)
- treSB: PP_4059 | Q88FN0 | Maltokinase (EC 2.7.1.175) (EC 5.4.99.16) (Maltose alpha-D-glucosyltransferase) (Maltose-1-phosphate synthase) (EC 2.7.1.175; 5.4.99.16; primary bucket kegg:ppu00500)
- glgE: PP_4060 | Q88FM9 | Alpha-1,4-glucan:maltose-1-phosphate maltosyltransferase (GMPMT) (EC 2.4.99.16) ((1->4)-alpha-D-glucan:maltose-1-phosphate alpha-D-maltosyltransferase) (EC 2.4.99.16; primary bucket kegg:ppu00500)
- pgi2: PP_4701 | Q88DW7 | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- glgP: PP_5041 | Q88CY8 | Alpha-1,4 glucan phosphorylase (EC 2.4.1.1) (EC 2.4.1.1; primary bucket kegg:ppu00500)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

## Generic Module Context

### Working Scope

A reusable two-reaction pathway in which TreY converts the reducing end of an alpha-1,4-glucan to a trehalose-containing alpha,alpha-1,1 linkage and TreZ hydrolyzes the resulting maltooligosyltrehalose to release trehalose. Alpha-glucan synthesis and remodeling, alternative OtsA/OtsB or TreS trehalose routes, and trehalose degradation are outside the boundary.

### Provisional Biological Outline

- TreY/TreZ trehalose biosynthesis from alpha-glucan
  - 1. maltooligosyltrehalose formation
  - Maltooligosyl trehalose synthase
    - Maltooligosyl trehalose synthase (molecular player: TreY maltooligosyl trehalose synthases; activity or role: (1,4)-alpha-D-glucan 1-alpha-D-glucosylmutase activity)
  - 2. trehalose release
  - Malto-oligosyltrehalose trehalohydrolase
    - Malto-oligosyltrehalose trehalohydrolase (molecular player: TreZ malto-oligosyltrehalose trehalohydrolases; activity or role: 4-alpha-D-(1->4)-alpha-D-glucanotrehalose trehalohydrolase activity)

### Known Relationships Among Steps

- Maltooligosyl trehalose synthase feeds into Malto-oligosyltrehalose trehalohydrolase: TreY supplies maltooligosyltrehalose to TreZ.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

## Output

# TreY/TreZ Trehalose Biosynthesis from α-Glucan in *Pseudomonas putida* KT2440

**Commissioned Module/Pathway/Taxon Review Brief**

- **Target taxon:** *Pseudomonas putida* KT2440 (organism code PSEPK; NCBI taxon 160488; proteome UP000000556)
- **Module under review:** TreY/TreZ trehalose biosynthesis from α-1,4-glucan (KEGG map ppu00500, *Starch and sucrose metabolism*, local bucket `kegg:ppu00500`)
- **Module area:** other_kegg_pathway
- **Verdict at a glance:** Module **SATISFIABLE / COVERED**, with TreY flagged **candidate_uncertain** and promoted to full gene review.

---

## 1. Executive Summary

The two-reaction **TreY/TreZ** module — in which TreY (maltooligosyltrehalose synthase, EC 5.4.99.15) isomerizes the reducing-end α-1,4 linkage of an α-glucan into an α,α-1,1 (trehalose) linkage, and TreZ (malto-oligosyltrehalose trehalohydrolase, EC 3.2.1.141) hydrolyzes the resulting maltooligosyltrehalose to release free trehalose — is **gene-complete and satisfiable** in *Pseudomonas putida* KT2440. Both catalytic steps are encoded within a single contiguous glycogen/GlgE/trehalose locus on the chromosome: **treZ = PP_4051 (Q88FN8)** and **treY = PP_4053 (Q88FN6)**, flanking `glgA (PP_4050)`, `malQ (PP_4052)`, and physically clustered with `glgX (PP_4055)`, `glgB (PP_4058)`, `treSB/Mak (PP_4059)`, and `glgE (PP_4060)`. The polymeric α-glucan substrate on which TreY/TreZ act is supplied *in cis* by the glycogen/GlgE machinery of the same locus. This co-localization is the strongest single line of evidence for module satisfiability.

The module's biological importance in KT2440 is **elevated rather than redundant**, because the canonical OtsA/OtsB (trehalose-6-phosphate synthase/phosphatase) route is **entirely absent** from the reference proteome. We confirmed this absence twice and by two independent methods: (i) name/EC-based screens returned zero hits for OtsA (EC 2.4.1.15), OtsB (EC 3.1.3.12), any `ots*` gene, or trehalase (EC 3.2.1.28); and (ii) a name-independent InterPro domain screen returned zero proteins carrying the OtsA glycosyltransferase-20 family domain (IPR001830/IPR012766) or the trehalose-6-phosphate phosphatase domain (IPR003337). Because the domain search does not depend on gene naming, a mis-named or divergent OtsA/OtsB is effectively excluded. TreYZ, together with a genuine standalone TreS (treSA/PP_2918) and the GlgE-pathway maltokinase-TreS fusion (treSB/PP_4059), constitute the trehalose-related enzymology of this strain.

For curation, the actionable conclusions are: **mark both module steps covered**, but flag **step 1 (TreY) as candidate_uncertain** and promote it to full `fetch-gene` review because UniProt records it at protein-existence level PE=4 ("Predicted") with **no EC number and no catalytic-activity reaction populated**, in contrast to TreZ (PE=3, EC 3.2.1.141, populated reaction). The generic module boundary — which keeps α-glucan synthesis, GlgE remodeling, the TreS interconversion, the OtsAB route, and trehalose degradation outside the module — is **correct for this organism** and needs no revision. The OtsAB branch of any parent trehalose-biosynthesis supermodule should be marked **not_expected_in_target_taxon** for KT2440.

---

## 2. Target-Organism Pathway Definition

### 2.1 Exact process included in the module

The module comprises exactly two enzymatic reactions acting on a preformed α-1,4-glucan (glycogen-like polymer or maltooligosaccharide):

1. **Maltooligosyltrehalose formation** — TreY (EC 5.4.99.15; (1,4)-α-D-glucan 1-α-D-glucosylmutase) intramolecularly transglycosylates the terminal α-1,4 linkage at the reducing end into an α,α-1,1 linkage, producing **maltooligosyltrehalose** (a trehalose cap on the end of the glucan chain).
2. **Trehalose release** — TreZ (EC 3.2.1.141; 4-α-D-((1→4)-α-D-glucano)trehalose trehalohydrolase) hydrolyzes the α-1,4 glucosidic bond adjacent to the newly formed trehalose unit, releasing **free trehalose** and a shortened α-glucan that can re-enter the cycle.

### 2.2 Neighboring processes to keep separate

The following are **outside** the module boundary and should not be conflated with TreYZ steps:

- **α-Glucan synthesis and remodeling** — glycogen synthase `glgA` (PP_4050, EC 2.4.1.21), branching enzyme `glgB` (PP_4058, EC 2.4.1.18), debranching `glgX` (PP_4055, EC 3.2.1.33), amylomaltase `malQ` (PP_4052, EC 2.4.1.25), glucan phosphorylase `glgP` (PP_5041, EC 2.4.1.1). These *supply and recycle* the substrate but are not trehalose-forming steps.
- **The GlgE pathway** — maltokinase/TreS fusion `treSB` (PP_4059, EC 2.7.1.175 / 5.4.99.16) and maltosyltransferase `glgE` (PP_4060, EC 2.4.99.16), which build α-glucan from α-maltose-1-phosphate.
- **Alternative trehalose routes** — the OtsA/OtsB (trehalose-6-phosphate) route and the standalone TreS (maltose⇌trehalose isomerase) route.
- **Trehalose degradation** — trehalase (EC 3.2.1.28).
- **Peripheral central-carbon and cell-envelope genes** — `glk` (glucokinase), `bglX` (β-glucosidase), `pgi1`/`pgi2` (phosphoglucose isomerase), `bcsA` (cellulose synthase, β-glucan), `pgm`/`cpsG`/`algC` (phosphogluco/mannomutases), `galU` (UDP-glucose pyrophosphorylase). These are members of KEGG map ppu00500/adjacent maps but are **not** TreYZ steps.

### 2.3 Alternate names and database definitions

- KEGG pathway **ppu00500** = "Starch and sucrose metabolism" (the parent map; TreY/TreZ are two nodes within it).
- The TreY/TreZ route is also referred to as the **"OtsAB-independent" or "maltooligosyltrehalose (MOT) pathway"** of trehalose biosynthesis, distinct from the OtsAB and TreS pathways.
- Enzyme synonyms: TreY = "malto-oligosyltrehalose synthase / MTSase"; TreZ = "malto-oligosyltrehalose trehalohydrolase / MTHase."
- InterPro provides **dedicated family signatures**: IPR012767 (Trehalose_TreY) and IPR012768 (Trehalose_TreZ), both built on the GH13 α-amylase superfamily (IPR006047).

---

## 3. Expected Step Model

| Step | Enzyme (activity) | Expected EC | KT2440 gene | Status |
|------|-------------------|-------------|-------------|--------|
| 1. Maltooligosyltrehalose formation | TreY — (1,4)-α-D-glucan 1-α-D-glucosylmutase | 5.4.99.15 | **treY / PP_4053 / Q88FN6** | **Covered but candidate_uncertain** |
| 2. Trehalose release | TreZ — 4-α-D-(1→4)-α-D-glucanotrehalose trehalohydrolase | 3.2.1.141 | **treZ / PP_4051 / Q88FN8** | **Covered** |
| (Substrate supply, *outside module*) | α-glucan synthesis/remodeling | 2.4.1.21 / 2.4.1.18 / 2.4.99.16 | glgA, glgB, glgE, malQ | Present (context) |

Both required steps map cleanly onto KT2440 genes. There are **no missing steps** in the two-reaction core; the only uncertainty is the depth of annotation evidence for TreY (see §4–§5).

```
             α-1,4-glucan (glycogen-like, supplied by glgA/glgB/glgE/malQ)
                        │
                        │  TreY  (PP_4053, EC 5.4.99.15)   ── STEP 1
                        ▼         reducing-end α-1,4 → α,α-1,1 isomerization
             maltooligosyltrehalose  (trehalose-capped glucan)
                        │
                        │  TreZ  (PP_4051, EC 3.2.1.141)   ── STEP 2
                        ▼         hydrolysis adjacent to trehalose cap
             free trehalose  +  shortened α-glucan ──┐ (recycles)
                                                     └──► back to substrate pool
```

---

## 4. Candidate Genes and Evidence

### 4.1 Core module genes (high priority)

**treZ — PP_4051 (Q88FN8) — Malto-oligosyltrehalose trehalohydrolase (Step 2).**
This is the **best-supported** gene in the module. UniProt records it at protein-existence level **PE=3 "Inferred from homology"**, with **EC 3.2.1.141** and a **fully populated catalytic-activity reaction** (hydrolysis of the (1→4)-α-D-glucosidic linkage in maltooligosyltrehalose to yield trehalose + α-glucan). It carries the dedicated InterPro **TreZ family signature IPR012768** (Trehalose_TreZ). Evidence type: homology + dedicated family assignment + populated EC/reaction. Curation caveat: no experimental (PE=1) evidence *in the target strain*, but the annotation is internally consistent and family-specific. **Mark covered.**

**treY — PP_4053 (Q88FN6) — Maltooligosyl trehalose synthase (Step 1).**
The 924-aa protein carries the dedicated InterPro **TreY family signature IPR012767** and the GH13 catalytic domain (IPR006047) — architecturally a bona fide TreY. However, UniProt records it at **PE=4 "Predicted"** with **no EC number and no catalytic-activity reaction populated**, making its evidence base weaker than TreZ's. The protein length (924 aa) is consistent with a large GH13 maltooligosyltrehalose synthase. Evidence type: family-signature homology only. Curation caveat: the family assignment is strong, but the missing EC/reaction and PE=4 status mean the functional call has not been formally curated. **Mark covered but candidate_uncertain; promote to full review.**

### 4.2 Substrate-supply / GlgE-pathway context genes (present, outside module)

| Gene | Locus | UniProt | Annotation | EC | Role relative to module |
|------|-------|---------|------------|-----|------------------------|
| glgA | PP_4050 | Q88FN9 | Glycogen synthase | 2.4.1.21 | Supplies α-glucan substrate |
| malQ | PP_4052 | Q88FN7 | 4-α-glucanotransferase (amylomaltase) | 2.4.1.25 | Glucan remodeling |
| glgX | PP_4055 | Q88FN4 | Glycogen debranching enzyme | 3.2.1.33 | Glucan remodeling |
| glgB | PP_4058 | Q88FN1 | 1,4-α-glucan branching enzyme | 2.4.1.18 | Glucan branching |
| treSB | PP_4059 | Q88FN0 | Maltokinase + TreS (bifunctional) | 2.7.1.175 / 5.4.99.16 | GlgE-pathway maltokinase |
| glgE | PP_4060 | Q88FM9 | Maltose-1-P maltosyltransferase | 2.4.99.16 | α-glucan synthesis |
| glgP | PP_5041 | Q88CY8 | α-1,4 glucan phosphorylase | 2.4.1.1 | Glucan degradation |

The GlgE-pathway gene set is complete and co-located with treY/treZ, defining the pathway neighborhood. In *M. tuberculosis* and *S. venezuelae*, the TreS-Pep2-GlgE and GlgC-GlgA routes converge on **α-maltose-1-phosphate** to build branched α-glucan — the polymeric substrate on which TreY/TreZ act ([PMID: 27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/); [PMID: 27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/)).

### 4.3 TreS-family paralogs (resolved)

A key curation subtlety is the presence of **two distinct TreS-family paralogs** that must not be conflated:

- **treSA — PP_2918 (Q88IT1), 688 aa, PE=4** — carries the TreS family signature **IPR012665 (Trehalose_synth)** + GH domain (IPR017853) and **no maltokinase domain**. This is a **classic standalone trehalose synthase** (maltose ⇌ trehalose isomerase). A TreS from *P. putida* ATCC47054 has been used industrially to convert maltose to trehalose in one step ([PMID: 29602391](https://pubmed.ncbi.nlm.nih.gov/29602391/)), consistent with a functional standalone TreS existing in the species.
- **treSB — PP_4059 (Q88FN0), 1106 aa, PE=3** — carries the TreS/α-amylase N-domain (IPR012810) **AND** the dedicated TreS-maltokinase C-domain (**IPR012811**, TreS_maltokin_C_dom) plus Mak_N_cap (IPR040999) and a kinase-like domain (IPR011009), with **both reactions populated** (D-maltose + ATP → α-maltose-1-phosphate; D-maltose → trehalose). A proteome scan for IPR012810 returned only treSB. This is a **genuine bifunctional TreS-maltokinase (Pep2/Mak-type)** whose in-operon role is to supply the GlgE pathway with maltose-1-phosphate — **not** a canonical stand-alone trehalose synthase.

### 4.4 Peripheral central-carbon genes (not module steps)

`glk` (PP_1011), `bglX` (PP_1403), `cpsG` (PP_1777), `pgi1` (PP_1808), `bcsA` (PP_2635, cellulose synthase → β-glucan, not α-glucan), `pgm` (PP_3578), `galU` (PP_3821), `pgi2` (PP_4701), and `algC` (PP_5288) are members of ppu00500 or adjacent maps but are **peripheral to** the TreYZ module. They participate in general hexose-phosphate interconversion, UDP-glucose supply, or cell-envelope polysaccharide synthesis, and should be excluded from module satisfiability accounting.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 The single genuine gap: TreY annotation depth

The only substantive gap is the **weak annotation evidence for TreY (PP_4053)**. Despite carrying the dedicated TreY InterPro family signature, it is PE=4 ("Predicted") with no EC number and no catalytic-activity reaction populated in UniProt. This is an **annotation-completeness gap, not a gene-presence gap** — the gene is clearly present and family-assigned, but its functional call has not been formally curated to the level of TreZ. This is why it is flagged candidate_uncertain and promoted to full review.

### 5.2 Absence of the OtsAB route (confirmed, not a gap in the module)

The OtsA/OtsB trehalose-6-phosphate route is **truly absent** from KT2440, confirmed by two independent methods:

1. **Name/EC screen** of proteome UP000000556 — zero hits for OtsA (EC 2.4.1.15), OtsB (EC 3.1.3.12), any `ots*` gene, and trehalase (EC 3.2.1.28).
2. **Domain-level screen** — zero proteins with the OtsA glycosyltransferase-20 family domain (IPR001830 / IPR012766) or the trehalose-6-phosphate phosphatase domain (IPR003337).

Because the second method is name-independent, a mis-annotated or divergently named OtsA/OtsB is effectively excluded. This is a **biologically real absence**, and it raises the physiological importance of the TreYZ route: KT2440 accumulates trehalose as a desiccation protectant ([PMID: 31323038](https://pubmed.ncbi.nlm.nih.gov/31323038/)), so an active OtsAB-independent trehalose source is required.

### 5.3 Potential over-annotation / paralog ambiguity to watch

- **treSB (PP_4059)** could be over-simplified in downstream databases as a plain "trehalose synthase." Its dedicated maltokinase C-domain (IPR012811) shows it is really a **bifunctional GlgE-pathway maltokinase**; annotation pipelines that collapse it to "TreS" would misrepresent its in-operon role.
- **treSA vs treSB** must be kept distinct — both hit TreS-family signatures but have different architectures and roles.
- **Broad EC mappings**: several substrate-supply genes carry broad GH13 or transferase EC numbers that overlap the trehalose enzymes' superfamily; care is needed not to let superfamily-level EC promiscuity leak into TreYZ step assignments.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|-------------|--------------------|-----------|
| Step 1 — Maltooligosyltrehalose formation (TreY) | **covered / candidate_uncertain** | Present (PP_4053, dedicated TreY family IPR012767) but PE=4, no EC/reaction populated → promote to full review |
| Step 2 — Trehalose release (TreZ) | **covered** | PP_4051, PE=3, EC 3.2.1.141, populated reaction, dedicated TreZ family IPR012768 |
| OtsAB branch (parent supermodule) | **not_expected_in_target_taxon** | Absent by both name/EC and domain-level screens |

**Module boundary assessment:** The generic module boundary is **correct for KT2440** and needs no revision. Keeping α-glucan synthesis, GlgE remodeling, TreS interconversion, OtsAB, and trehalose degradation outside the module accurately reflects the biology, where these are distinct (if physically co-located) processes.

**GO / new-document needs:** No new module document or GO term request is strictly required. The two required GO/EC activities already exist (EC 5.4.99.15 for TreY; EC 3.2.1.141 for TreZ). The main curation action is to **populate the EC number (5.4.99.15) and catalytic-activity reaction for TreY (Q88FN6)** upon full review, upgrading it from PE=4 to a curated homology call, so that automated module satisfiability tools register step 1 as fully covered.

---

## 7. Genes to Promote to Full Review

1. **treY / PP_4053 / Q88FN6 (HIGH PRIORITY).** Promote to full `fetch-gene` review to confirm the maltooligosyltrehalose-synthase function, assign EC 5.4.99.15, and populate the catalytic reaction. Rationale: it is the one module step whose evidence (PE=4, no EC/reaction) lags behind its family assignment.
2. **treZ / PP_4051 / Q88FN8 (optional confirmatory).** Already well-annotated (PE=3, EC 3.2.1.141, populated reaction); a light review to confirm the family call would fully close the module.
3. **treSB / PP_4059 / Q88FN0 (context, medium).** Worth a review to ensure downstream databases retain its bifunctional TreS-maltokinase (GlgE-pathway) identity and do not over-collapse it to "trehalose synthase."

---

## 8. Mechanistic Model / Interpretation

The picture that emerges is of a **single, tightly organized chromosomal locus** in *P. putida* KT2440 that couples glycogen/α-glucan metabolism directly to trehalose production:

```
Chromosomal locus (P. putida KT2440):

 PP_4050   PP_4051   PP_4052   PP_4053   ...  PP_4055  PP_4058  PP_4059   PP_4060
  glgA      treZ      malQ      treY           glgX     glgB    treSB     glgE
 (synth)  (STEP 2)  (remodel) (STEP 1)        (debr.) (branch) (Mak-TreS) (GlgE)
   │         ▲          │         │              │        │        │         │
   └─────────┼──────────┴─────────┼──────────────┴────────┴────────┴─────────┘
             │   α-GLUCAN SUBSTRATE POOL (supplied/recycled in cis)
             │                     │
   trehalose ◄── TreZ ◄── maltooligosyltrehalose ◄── TreY ◄── α-1,4-glucan
```

The substrate for TreY — a branched, glycogen-like α-1,4-glucan — is manufactured and maintained *in cis* by the same locus (glgA/glgB synthesis and branching; glgE/treSB building from maltose-1-phosphate; malQ/glgX/glgP remodeling and turnover). TreY then caps the reducing end with a trehalose unit, and TreZ liberates free trehalose. Because KT2440 has **no OtsAB route**, this MOT (maltooligosyltrehalose) pathway is the principal *de novo* trehalose-synthesis route from glucan, complemented by the standalone TreS (treSA) that can interconvert maltose and trehalose. This architecture is physiologically coherent: trehalose is a validated desiccation/osmotic protectant in KT2440 ([PMID: 31323038](https://pubmed.ncbi.nlm.nih.gov/31323038/)), and coupling its synthesis to the glycogen store provides an on-demand protectant reservoir.

---

## 9. Evidence Base

| PMID | Title (short) | How it supports the findings |
|------|---------------|------------------------------|
| [27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/) | *Metabolic Network for Biosynthesis of α-Glucans Required for Virulence of M. tuberculosis* | "There is an unexpected convergence of the TreS-Pep2 and GlgC-GlgA pathways that both generate α-maltose-1-phosphate." Documents that both routes feed α-maltose-1-phosphate into GlgE-dependent α-glucan synthesis — the substrate pool supplying TreY/TreZ — supporting the module boundary between α-glucan supply and the TreYZ steps. |
| [27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/) | *Developmental delay in a Streptomyces venezuelae glgE null mutant …* | "The GlgE pathway is thought to be responsible for the conversion of trehalose into a glycogen-like α-glucan polymer in bacteria." Confirms the GlgE-pathway genes co-located with treY/treZ interconvert trehalose and α-glucan, defining the neighboring process bordering the TreYZ module. |
| [31323038](https://pubmed.ncbi.nlm.nih.gov/31323038/) | *Desiccation-induced viable but nonculturable state in P. putida KT2440* | "The BSR in the presence of nonreducing disaccharides, such as trehalose, was high after 15 days of desiccation stress." Direct KT2440 evidence that trehalose is a physiologically relevant protectant, supporting the biological importance of an active trehalose-biosynthesis route (TreYZ) in this strain. |
| [29602391](https://pubmed.ncbi.nlm.nih.gov/29602391/) | *A process for production of trehalose by recombinant trehalose synthase …* | A TreS from *P. putida* ATCC47054 converts maltose to trehalose in one step, consistent with a functional standalone TreS (treSA) existing in the species and complementing the TreYZ route. |

Supporting molecular evidence is drawn from UniProt (proteome UP000000556) and InterPro family/domain assignments: dedicated TreY (IPR012767) and TreZ (IPR012768) family signatures; the GlgE domain (IPR026585); the TreS-maltokinase C-domain (IPR012811); and the absence of OtsA (IPR001830/IPR012766) and OtsB (IPR003337) domains.

---

## 10. Limitations and Knowledge Gaps

- **No experimental (PE=1) evidence in the target strain** for either TreY or TreZ. Both functional calls are homology/family-based. Direct enzymatic assays or knockout phenotypes in KT2440 have not been reported in the literature reviewed here.
- **TreY annotation incompleteness.** TreY is PE=4 with no EC/reaction populated; while its family signature is strong, formal functional confirmation is pending.
- **Regulation and flux not addressed.** This review establishes gene presence and module satisfiability; it does not quantify trehalose flux through TreYZ vs TreS under specific conditions (desiccation, osmotic stress, carbon source).
- **Literature is sparse for KT2440-specific trehalose enzymology.** Much mechanistic transfer relies on *M. tuberculosis* and *S. venezuelae* (GlgE pathway) — strong at the pathway-architecture level but not a substitute for direct KT2440 biochemistry.
- **Substrate specificity of treSB** as a maltokinase vs TreS in vivo is inferred from domain architecture, not measured in KT2440.

---

## 11. Proposed Follow-up Experiments / Actions

**Curation actions (immediate):**
1. Promote **treY (PP_4053/Q88FN6)** to full `fetch-gene` review; assign EC 5.4.99.15 and populate the catalytic-activity reaction based on the IPR012767 family call. Upgrade module step 1 from candidate_uncertain to covered.
2. Confirm **treZ (PP_4051/Q88FN8)** family call (optional, light review).
3. Annotate **treSB (PP_4059)** explicitly as a bifunctional TreS-maltokinase (GlgE pathway) to prevent over-collapse to "trehalose synthase."
4. Mark the OtsAB branch of any parent trehalose-biosynthesis supermodule as **not_expected_in_target_taxon** for KT2440.

**Experimental / expert questions (to resolve gaps):**
5. **Knockout phenotyping:** Construct ΔtreY, ΔtreZ, and ΔtreY ΔtreSA double mutants in KT2440 and measure intracellular trehalose under desiccation/osmotic stress. If TreYZ is the principal route, ΔtreY or ΔtreZ should show a substantial trehalose-synthesis defect that ΔtreSA alone does not.
6. **Enzyme assays:** Express and assay recombinant TreY (PP_4053) and TreZ (PP_4051) on glycogen/maltooligosaccharide substrates to confirm EC 5.4.99.15 and EC 3.2.1.141 activities directly in the target strain background.
7. **Flux/regulation:** Use ¹³C tracing or targeted metabolomics under osmotic/desiccation stress to quantify the relative contributions of TreYZ, TreS (treSA), and any residual routes to the trehalose pool.
8. **Confirm OtsAB absence functionally:** Verify that no trehalose-6-phosphate synthase activity is detectable in KT2440 lysates, corroborating the genomic/domain-level absence.

---

## Appendix: Consolidated Findings (from investigation)

- **F001** — Both TreY/TreZ module steps are encoded by a contiguous glgE/glycogen/trehalose locus (PP_4050–PP_4060) in KT2440; treZ carries EC 3.2.1.141 + IPR012768, treY carries IPR012767 + GH13.
- **F002** — TreY (PP_4053) evidence (PE=4, no EC/reaction) is weaker than TreZ (PE=3, EC + reaction) → promote to full review.
- **F003** — Co-located GlgE-pathway gene set defines the module boundary; convergence on α-maltose-1-phosphate supplies the α-glucan substrate ([PMID: 27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/), [PMID: 27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/)).
- **F004** — TreYZ is the principal trehalose-synthesis route; OtsAB absent from the proteome (zero EC/name hits).
- **F005** — Domain-level InterPro scan independently confirms complete absence of OtsAB (IPR001830/IPR012766/IPR003337 = 0).
- **F006** — Two distinct TreS paralogs: treSA/PP_2918 standalone TreS; treSB/PP_4059 bifunctional TreS-maltokinase.
- **F007** — Final verdict: module covered/satisfiable; TreY candidate_uncertain; OtsAB not_expected_in_target_taxon; generic boundary correct.


## Artifacts

- [OpenScientist final report](PSEPK__trey_trez_trehalose_biosynthesis__ppu00500-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__trey_trez_trehalose_biosynthesis__ppu00500-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27513637
2. PMID:27121970
3. PMID:29602391
4. PMID:31323038