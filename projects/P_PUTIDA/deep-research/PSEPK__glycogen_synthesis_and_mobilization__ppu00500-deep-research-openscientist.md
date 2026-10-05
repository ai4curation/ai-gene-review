---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T22:05:31.930457'
end_time: '2026-08-12T22:55:07.774220'
duration_seconds: 2975.84
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial glycogen synthesis and mobilization
  module_summary: A reusable bacterial storage-carbon module coupling synthesis of
    branched glycogen or glycogen-like alpha-glucan to its later mobilization. The
    synthetic arm explicitly distinguishes the widespread GlgC/ADP-glucose route from
    a Pseudomonas GalU/UDP-glucose route, then uses GlgB to introduce alpha-1,6 branches.
    The mobilization arm uses GlgP to release glucose 1-phosphate from non-reducing
    chain ends and GlgX to hydrolyze branch-point alpha-1,6 linkages so phosphorolysis
    can continue. The module ends at glucose 1-phosphate; phosphoglucomutase and central
    carbon metabolism are downstream. TreS-Mak-GlgE alpha-glucan synthesis and TreY-TreZ
    trehalose formation are connected neighboring modules rather than collapsed into
    these reactions.
  module_outline: "- Bacterial glycogen synthesis and mobilization\n  - 1. synthesis\
    \ of branched glycogen\n  - Bacterial glycogen synthesis\n    - 1. nucleotide-sugar\
    \ formation and alpha-1,4-glucan extension\n    - Nucleotide-sugar-dependent glycogen\
    \ chain extension\n      - Alternative versions by nucleotide-sugar donor and\
    \ enzyme-family implementation: Glycogen synthase donor variants\n        - Canonical\
    \ GlgC/ADP-glucose route\n          - 1. ADP-glucose donor formation\n       \
    \   - GlgC-dependent ADP-glucose formation\n            - GlgC glucose-1-phosphate\
    \ adenylyltransferase activity (molecular player: bacterial GlgC ADP-glucose pyrophosphorylase\
    \ family; activity or role: glucose-1-phosphate adenylyltransferase activity)\n\
    \          - 2. ADP-glucose-dependent alpha-1,4 chain extension\n          - ADP-glucose-dependent\
    \ GlgA chain extension\n            - ADP-glucose-dependent GlgA activity (molecular\
    \ player: bacterial GlgA glycogen synthase family; activity or role: alpha-1,4-glucan\
    \ glucosyltransferase (ADP-glucose donor) activity)\n        - Pseudomonas GalU/UDP-glucose\
    \ route\n          - 1. UDP-glucose donor formation\n          - GalU-dependent\
    \ UDP-glucose formation\n            - GalU UTP:glucose-1-phosphate uridylyltransferase\
    \ activity (molecular player: bacterial GalU family; activity or role: UTP:glucose-1-phosphate\
    \ uridylyltransferase activity)\n          - 2. UDP-glucose-dependent alpha-1,4\
    \ chain extension\n          - UDP-glucose-dependent Pseudomonas GlgA chain extension\n\
    \            - Pseudomonas UDP-glucose-dependent GlgA activity (molecular player:\
    \ Pseudomonas GlgA glycogen synthase family; activity or role: alpha-1,4-glucan\
    \ glucosyltransferase (UDP-glucose donor) activity)\n    - 2. alpha-1,6 branch\
    \ formation\n    - GlgB-dependent glycogen branching\n      - GlgB 1,4-alpha-glucan\
    \ branching enzyme activity (molecular player: bacterial GlgB branching-enzyme\
    \ family; activity or role: 1,4-alpha-glucan branching enzyme activity)\n  - 2.\
    \ mobilization of branched glycogen\n  - Bacterial glycogen mobilization\n   \
    \ - 1. phosphorolysis of alpha-1,4-glucan chain ends\n    - GlgP-dependent glycogen\
    \ phosphorolysis\n      - GlgP glycogen phosphorylase activity (molecular player:\
    \ glycogen phosphorylase family; activity or role: glycogen phosphorylase activity)\n\
    \    - 2. hydrolytic removal of alpha-1,6 branch points\n    - GlgX-dependent\
    \ glycogen debranching\n      - GlgX short-chain limit-dextrin debranching activity\
    \ (molecular player: bacterial GlgX glycogen-debranching family; activity or role:\
    \ limit dextrin alpha-1,6-maltotetraose-hydrolase activity)"
  module_connections: '- GlgB-dependent glycogen branching feeds into GlgP-dependent
    glycogen phosphorolysis: Branched glycogen produced by the synthetic arm is the
    stored polymer mobilized by GlgP and GlgX.

    - ADP-glucose-dependent GlgA chain extension feeds into GlgB-dependent glycogen
    branching: GlgB branches alpha-1,4-glucan from the ADP-glucose route.

    - UDP-glucose-dependent Pseudomonas GlgA chain extension feeds into GlgB-dependent
    glycogen branching: GlgB branches alpha-1,4-glucan from the Pseudomonas UDP-glucose
    route.

    - GlgC-dependent ADP-glucose formation feeds into ADP-glucose-dependent GlgA chain
    extension: GlgC supplies ADP-glucose to canonical GlgA.

    - GalU-dependent UDP-glucose formation feeds into UDP-glucose-dependent Pseudomonas
    GlgA chain extension: GalU supplies UDP-glucose to Pseudomonas GlgA.

    - GlgP-dependent glycogen phosphorolysis feeds into GlgX-dependent glycogen debranching:
    GlgP shortens outer chains until branch-proximal glycogen becomes substrate for
    GlgX.

    - GlgX-dependent glycogen debranching feeds into GlgP-dependent glycogen phosphorolysis:
    Debranching exposes linear alpha-1,4 chain ends for continued GlgP phosphorolysis.'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__glycogen_synthesis_and_mobilization__ppu00500-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__glycogen_synthesis_and_mobilization__ppu00500-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial glycogen synthesis and mobilization in Pseudomonas putida KT2440

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

A reusable bacterial storage-carbon module coupling synthesis of branched glycogen or glycogen-like alpha-glucan to its later mobilization. The synthetic arm explicitly distinguishes the widespread GlgC/ADP-glucose route from a Pseudomonas GalU/UDP-glucose route, then uses GlgB to introduce alpha-1,6 branches. The mobilization arm uses GlgP to release glucose 1-phosphate from non-reducing chain ends and GlgX to hydrolyze branch-point alpha-1,6 linkages so phosphorolysis can continue. The module ends at glucose 1-phosphate; phosphoglucomutase and central carbon metabolism are downstream. TreS-Mak-GlgE alpha-glucan synthesis and TreY-TreZ trehalose formation are connected neighboring modules rather than collapsed into these reactions.

### Provisional Biological Outline

- Bacterial glycogen synthesis and mobilization
  - 1. synthesis of branched glycogen
  - Bacterial glycogen synthesis
    - 1. nucleotide-sugar formation and alpha-1,4-glucan extension
    - Nucleotide-sugar-dependent glycogen chain extension
      - Alternative versions by nucleotide-sugar donor and enzyme-family implementation: Glycogen synthase donor variants
        - Canonical GlgC/ADP-glucose route
          - 1. ADP-glucose donor formation
          - GlgC-dependent ADP-glucose formation
            - GlgC glucose-1-phosphate adenylyltransferase activity (molecular player: bacterial GlgC ADP-glucose pyrophosphorylase family; activity or role: glucose-1-phosphate adenylyltransferase activity)
          - 2. ADP-glucose-dependent alpha-1,4 chain extension
          - ADP-glucose-dependent GlgA chain extension
            - ADP-glucose-dependent GlgA activity (molecular player: bacterial GlgA glycogen synthase family; activity or role: alpha-1,4-glucan glucosyltransferase (ADP-glucose donor) activity)
        - Pseudomonas GalU/UDP-glucose route
          - 1. UDP-glucose donor formation
          - GalU-dependent UDP-glucose formation
            - GalU UTP:glucose-1-phosphate uridylyltransferase activity (molecular player: bacterial GalU family; activity or role: UTP:glucose-1-phosphate uridylyltransferase activity)
          - 2. UDP-glucose-dependent alpha-1,4 chain extension
          - UDP-glucose-dependent Pseudomonas GlgA chain extension
            - Pseudomonas UDP-glucose-dependent GlgA activity (molecular player: Pseudomonas GlgA glycogen synthase family; activity or role: alpha-1,4-glucan glucosyltransferase (UDP-glucose donor) activity)
    - 2. alpha-1,6 branch formation
    - GlgB-dependent glycogen branching
      - GlgB 1,4-alpha-glucan branching enzyme activity (molecular player: bacterial GlgB branching-enzyme family; activity or role: 1,4-alpha-glucan branching enzyme activity)
  - 2. mobilization of branched glycogen
  - Bacterial glycogen mobilization
    - 1. phosphorolysis of alpha-1,4-glucan chain ends
    - GlgP-dependent glycogen phosphorolysis
      - GlgP glycogen phosphorylase activity (molecular player: glycogen phosphorylase family; activity or role: glycogen phosphorylase activity)
    - 2. hydrolytic removal of alpha-1,6 branch points
    - GlgX-dependent glycogen debranching
      - GlgX short-chain limit-dextrin debranching activity (molecular player: bacterial GlgX glycogen-debranching family; activity or role: limit dextrin alpha-1,6-maltotetraose-hydrolase activity)

### Known Relationships Among Steps

- GlgB-dependent glycogen branching feeds into GlgP-dependent glycogen phosphorolysis: Branched glycogen produced by the synthetic arm is the stored polymer mobilized by GlgP and GlgX.
- ADP-glucose-dependent GlgA chain extension feeds into GlgB-dependent glycogen branching: GlgB branches alpha-1,4-glucan from the ADP-glucose route.
- UDP-glucose-dependent Pseudomonas GlgA chain extension feeds into GlgB-dependent glycogen branching: GlgB branches alpha-1,4-glucan from the Pseudomonas UDP-glucose route.
- GlgC-dependent ADP-glucose formation feeds into ADP-glucose-dependent GlgA chain extension: GlgC supplies ADP-glucose to canonical GlgA.
- GalU-dependent UDP-glucose formation feeds into UDP-glucose-dependent Pseudomonas GlgA chain extension: GalU supplies UDP-glucose to Pseudomonas GlgA.
- GlgP-dependent glycogen phosphorolysis feeds into GlgX-dependent glycogen debranching: GlgP shortens outer chains until branch-proximal glycogen becomes substrate for GlgX.
- GlgX-dependent glycogen debranching feeds into GlgP-dependent glycogen phosphorolysis: Debranching exposes linear alpha-1,4 chain ends for continued GlgP phosphorolysis.

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

# Species-Aware Module Review: Bacterial Glycogen / α-Glucan Synthesis and Mobilization in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK, NCBI txid 160488, proteome UP000000556)
**Module / bucket:** kegg:ppu00500 "Starch and sucrose metabolism" (generic storage-carbon module: branched glycogen/α-glucan synthesis + mobilization)
**Evidence basis:** Direct genome/proteome enumeration (UniProt UP000000556, InterPro/Pfam) for the target strain; mechanistic transfer from *Mycobacterium*/*Streptomyces* GlgE-pathway biochemistry (species transfer flagged throughout).

---

## 1. Executive summary

The generic module assumes glycogen is built by a nucleotide-sugar glycogen synthase (canonical **GlgC/ADP-glucose → GlgA**, or a proposed **GalU/UDP-glucose → GlgA**) and branched by GlgB, then mobilized by GlgP + GlgX. **This framing is wrong for *P. putida* KT2440.**

Direct proteome evidence shows:

- **`glgC` (ADP-glucose pyrophosphorylase, EC 2.7.7.27) is entirely absent** (0 hits by gene name, EC, and protein name). The canonical ADP-glucose route therefore **cannot operate** → `not_expected_in_target_taxon`.
- The only annotated glycogen synthase, **PP_4050 `glgA` (EC 2.4.1.21)**, carries an **ADP-glucose-type GT5 / starch-synthase family signature** (IPR011835, IPR013534/PF08323) but has **no ADP-glucose donor and no UDP-glucose-synthase alternative** (EC 2.4.1.11 absent). It is a **substrate-orphan** → `candidate_uncertain`; **promote to full review**.
- The organism instead encodes a **complete actinobacterial-type GlgE (TreS–Mak–GlgE–GlgB) α-glucan pathway** (PP_4059 TreS-Mak fusion, PP_4060 GlgE, PP_4058 GlgB) plus **TreY–TreZ** (PP_4053/PP_4051) and **MalQ** (PP_4052). This is the operative synthetic arm and is the glycogen-like α-glucan polymer source in this strain.
- Mobilization is cleanly covered by a **single GlgP** (PP_5041, EC 2.4.1.1; no separate MalP) and a **family-confident GlgX** (PP_4055, IPR011837).
- Trehalose that feeds the GlgE pathway is made by **TreY–TreZ + TreS**, **not OtsAB** (OtsA/OtsB absent), so the "glycogen", "α-glucan (GlgE)" and "trehalose" modules are a single interconnected network here and cannot be cleanly separated as the generic boundaries assume → **`module_needs_revision`**.

**Bottom line:** In *P. putida* KT2440 the storage α-glucan is a **GlgE-pathway product from trehalose/maltose-1-phosphate, not a GlgC/ADP-glucose glycogen**. Curate the ADP-glucose route as a gap, the UDP-glucose route as unsupported/uncertain, and add the TreS–Mak–GlgE + TreY–TreZ steps into the operative module.

---

## 2. Target-organism pathway definition

**Included biochemical process (as realized in KT2440):**
Cytoplasmic synthesis of a branched α-1,4/α-1,6-glucan (glycogen-like) from **maltose-1-phosphate** via the maltosyltransferase **GlgE**, with branching by **GlgB**; and its mobilization back to glucose-1-phosphate via **GlgP** (phosphorolysis) and **GlgX** (α-1,6 debranching), with **MalQ** (amylomaltase) redistributing maltooligosaccharides. The α-glucan is metabolically continuous with trehalose through **TreS/Mak** (trehalose↔maltose→maltose-1-P) and **TreY–TreZ** (α-glucan/maltooligosaccharide→trehalose). Module endpoint is glucose-1-phosphate.

**Neighboring processes to keep separate (boundaries):**
- **Central carbon interconversion downstream of G1P** — `pgm` (PP_3578) and `algC` (PP_5288) phosphoglucomutases, and `pgi1`/`pgi2` glucose-6-P isomerases (PP_1808/PP_4701). These are glycolysis/gluconeogenesis, **not** storage-glucan steps; they are boundary/downstream, not module members.
- **Cellulose biosynthesis** — `bcsA` (PP_2635, cellulose synthase, EC 2.4.1.12) makes β-1,4-glucan; **wrong polymer**, exclude from this α-glucan module despite its ppu00500 bucket tag.
- **Periplasmic β-glucoside catabolism** — `bglX` (PP_1403, β-glucosidase, EC 3.2.1.21); unrelated hydrolysis, exclude.
- **Free-glucose phosphorylation / mannose branch** — `glk` (PP_1011), `cpsG` (PP_1777 phosphomannomutase); peripheral, exclude.
- **Nucleotide-sugar supply for LPS/EPS** — `galU` (PP_3821, UDP-glucose pyrophosphorylase); UDP-glucose primarily serves LPS/exopolysaccharide, not α-glucan (see §5).

**Alternate names / database definitions:** KEGG ppu00500 "Starch and sucrose metabolism" is a broad overview map that lumps glycogen, trehalose, maltose, cellulose and sucrose reactions; it should not be equated with a mechanistic "glycogen module". The operative route is the **GlgE / TreS–Mak–GlgE pathway** (a.k.a. the trehalose→α-glucan pathway; MetaCyc "glycogen biosynthesis II / GlgE pathway"). "Glycogen" and "α-glucan/capsular glucan" are used interchangeably in the GlgE literature.

---

## 3. Expected step model (generic step → status in KT2440)

| Generic module step | Status in *P. putida* KT2440 | Basis |
|---|---|---|
| GlgC-dependent ADP-glucose formation | **not_expected_in_target_taxon (gap)** | No EC 2.7.7.27 / `glgC` in proteome (direct) |
| ADP-glucose-dependent GlgA chain extension | **gap / likely over-annotation** | Only PP_4050 GlgA present but no ADP-glucose donor (direct) |
| GalU-dependent UDP-glucose formation | **covered (but for LPS/EPS, not glucan)** | PP_3821 GalU present (direct); role assignment uncertain |
| UDP-glucose-dependent Pseudomonas GlgA extension | **candidate_uncertain** | No dedicated UDP-glucan synthase (EC 2.4.1.11 absent); PP_4050 family is ADP-glucose-type (direct) |
| GlgB α-1,6 branching | **covered** | PP_4058 GlgB, IPR006407 (direct) |
| GlgP phosphorolysis | **covered** | PP_5041 GlgP, sole EC 2.4.1.1 (direct); glycogen vs maltodextrin substrate caveat |
| GlgX debranching | **covered** | PP_4055 GlgX, IPR011837 (direct) |
| *(missing from generic model)* TreS–Mak → maltose-1-P | **covered; should be ADDED to module** | PP_4059 TreS-Mak fusion (direct) |
| *(missing from generic model)* GlgE maltosyltransferase (α-glucan synthesis) | **covered; the OPERATIVE synthesis step** | PP_4060 GlgE, EC 2.4.99.16 (direct) |
| *(missing)* TreY–TreZ trehalose formation; MalQ | **covered; interlinked** | PP_4053/PP_4051/PP_4052 (direct) |

---

## 4. Candidate genes and evidence

**High-confidence, module-core (direct proteome + family evidence):**
- **PP_4060 `glgE`** — α-1,4-glucan:maltose-1-P maltosyltransferase (EC 2.4.99.16; GH13 PF00128 + IPR026585 GlgE). **Operative α-glucan synthase.** Confident.
- **PP_4059 `treSB`** — bifunctional **TreS–maltokinase (Mak/Pep2) fusion** (EC 5.4.99.16 + EC 2.7.1.175; 1106 aa; TreS + maltokinase InterPro domains). Supplies maltose-1-P. Confident; note the dual EC/fusion when mapping GO.
- **PP_4058 `glgB`** — 1,4-α-glucan branching enzyme (EC 2.4.1.18). Confident.
- **PP_4055 `glgX`** — glycogen/limit-dextrin debranching enzyme (EC 3.2.1.33; IPR011837 GlgX). Confident.
- **PP_5041 `glgP`** — α-1,4-glucan phosphorylase (EC 2.4.1.1; IPR011833/IPR000811). Confident for phosphorolysis; **caveat:** the GlgP vs MalP (maltodextrin phosphorylase) physiological distinction is not resolvable from sequence alone — single-copy enzyme likely serves both.
- **PP_4052 `malQ`** — 4-α-glucanotransferase/amylomaltase (EC 2.4.1.25). Confident; maltooligosaccharide remodeling.
- **PP_4053 `treY` / PP_4051 `treZ`** — maltooligosyltrehalose synthase/trehalohydrolase (EC 5.4.99.15 / 3.2.1.141). Confident; trehalose formation from α-glucan (interlinked module).

**Ambiguous / caveated:**
- **PP_4050 `glgA`** — annotated glycogen synthase (EC 2.4.1.21), ADP-glucose-type GT5 family (IPR011835). **Orphan: no ADP-glucose donor; no UDP-glucan-synthase paralog.** Roles possible: (a) vestigial/substrate-starved; (b) non-canonical donor (UDP-glucose) — unproven; (c) maltose-1-P-forming activity feeding GlgE (by analogy to *M. tuberculosis* GlgA, PMID 27513637) — but that too needs ADP-glucose. **candidate_uncertain; promote to full review.**
- **PP_3821 `galU`** — UDP-glucose pyrophosphorylase (EC 2.7.7.9). Present, but UDP-glucose in *Pseudomonas* is principally for LPS/EPS; its role as a glucan-synthesis donor is **inferential and weak** without a UDP-dependent synthase.
- **PP_2918 `treSA`** — standalone trehalose synthase (EC 5.4.99.16); paralog of the TreS moiety of PP_4059; relevant to trehalose↔maltose interconversion, not directly α-glucan.

**Off-target / boundary candidates (exclude from module):** `bcsA` (β-glucan/cellulose), `bglX` (β-glucosidase), `glk`, `cpsG`, `pgi1`, `pgi2`, `pgm`, `algC` — central-carbon or unrelated-polymer genes bucketed into ppu00500 by the broad KEGG map.

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **`glgC` gap (high confidence, direct, two databases):** No ADP-glucose pyrophosphorylase → the canonical glycogen route is genomically absent. **Independently confirmed in KEGG:** ortholog K00975 (glgC) returns no `ppu` gene, while PP_4050 maps to K00703 (ADP-glucose glycogen synthase), PP_4060→K16147 (glgE), PP_5041→K00688 (glgP). Standalone maltokinase KO K16149 also has no `ppu` gene, consistent with the Mak activity being fused into PP_4059. Contrast: other proteobacteria (e.g., *Rhodobacter sphaeroides*) carry a full `glgCAPXB` operon (PMID 10729189), so absence in *P. putida* is a real lineage difference, not a database artifact.
2. **PP_4050 `glgA` = likely over-propagated "glycogen synthase":** EC 2.4.1.21 implies an ADP-glucose glycogen synthase that has no substrate here. The annotation should be softened (e.g., "putative glycogen/α-glucan synthase, donor uncertain") pending experimental donor determination.
3. **"Pseudomonas GalU/UDP-glucose GlgA route" (generic module hypothesis) is unsupported by the genome:** there is no EC 2.4.1.11 UDP-glucose-dependent glucan synthase, and the sole GlgA is ADP-glucose-family-typed. Mark this module branch **candidate_uncertain / speculative** for KT2440.
4. **GlgP substrate ambiguity:** GlgP/MalP cannot be distinguished by annotation; single-copy PP_5041 likely acts on both glycogen and maltodextrins.
5. **Module-boundary error:** GlgE, TreS–Mak and TreY–TreZ are treated as "neighboring modules" generically, but in KT2440 they are the **only** functional α-glucan synthesis/interconversion route and must be folded in.

---

## 6. Module and GO-curation recommendations

- **Mark `covered`:** GlgB (PP_4058), GlgX (PP_4055), GlgP (PP_5041), plus the GlgE-pathway steps GlgE (PP_4060), TreS-Mak (PP_4059), TreY/TreZ (PP_4053/PP_4051), MalQ (PP_4052).
- **Mark `not_expected_in_target_taxon` / `gap`:** GlgC-dependent ADP-glucose formation and the ADP-glucose-dependent GlgA extension step.
- **Mark `candidate_uncertain`:** the UDP-glucose/GlgA branch (donor unproven) and PP_4050 GlgA itself.
- **Mark `module_needs_revision`:** promote **TreS–Mak–GlgE α-glucan synthesis** and **TreY–TreZ** from "neighboring" to **in-module** for *Pseudomonas*/KT2440; add maltose-1-phosphate as an explicit intermediate. Consider a distinct module document **"Glycogen/α-glucan biosynthesis via the GlgE (trehalose→maltose-1-P) route"** for glgC-negative bacteria.
- **Cross-database coverage confirmation:** every "covered" gene is confirmed in both UniProt and KEGG — glgB K00700→PP_4058, glgX K01214→PP_4055, treY K06044→PP_4053, treZ K01236→PP_4051, malQ K00705→PP_4052, treS K05343→PP_4059, glgE K16147→PP_4060, glgP K00688→PP_5041. **Caveat:** the standalone maltokinase/Pep2 KOs (K16055, K16149) have no `ppu` gene, so the maltose-1-phosphate-forming Mak step is invisible in KEGG's KO scheme; it must be credited to the **PP_4059 TreS-Mak fusion** (EC 2.7.1.175) and **not** marked a gap on the basis of KEGG KO absence.
- **GO considerations:** GlgE activity = GO:0102500 (maltose-1-phospho-...maltosyltransferase-type); ensure PP_4060 is annotated to the GlgE/maltosyltransferase term, not to generic glycogen synthase (GO:0004373). Flag PP_4050 for review of GO:0004373 (glycogen [starch] synthase) given missing donor — note its KEGG assignment K00703 (ADP-glucose glycogen synthase) is the source of the over-propagated ADP-glucose activity. Maltokinase GO:0043915 for PP_4059's Mak activity.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_4050 `glgA` (Q88FN9)** — highest priority: resolve donor specificity (ADP- vs UDP-glucose), functionality, and whether it feeds GlgE; its annotation drives the module's synthetic-arm decision.
2. **PP_5041 `glgP` (Q88CY8)** — resolve GlgP vs MalP physiological substrate.
3. **PP_3821 `galU` (Q88GA4)** — confirm whether UDP-glucose has any glucan-synthesis role vs LPS/EPS only.
4. **PP_4059 `treSB` (Q88FN0)** — verify the TreS+maltokinase bifunctionality and correct dual-EC/GO mapping.

---

## 8. Key references

- Kalscheuer R *et al.* 2010, **PMID 20305657** — TreS–Pep2(Mak)–GlgE–GlgB pathway from trehalose to α-glucan (*M. tuberculosis*); defines the operative route (species transfer: mechanism strong, genes homologous to KT2440 PP_4059/PP_4060/PP_4058).
- Koliwer-Brandl H *et al.* 2016, **PMID 27513637** — α-glucan made **exclusively** via maltose-1-P/GlgE; GlgA's classical glycogen-synthase activity is weak; convergence of TreS-Pep2 and GlgC-GlgA routes.
- Miah F *et al.* 2016, **PMID 27121970** — *Streptomyces venezuelae* has the GlgE pathway but **lacks glgC and glgA**; GlgE necessary and sufficient for α-glucan — the closest genomic analogue of the KT2440 configuration.
- Roy R *et al.* 2013, **PMID 23901909** — TreS–Pep2 hetero-octameric complex regulating maltose-1-P flux.
- Mendes V *et al.* 2015, **PMID 26616850**; Kermani AA *et al.* 2019, **PMID 30877199** — GlgE and TreS:Pep2 structures.
- Igarashi RY & Meyer CR 2000, **PMID 10729189** — canonical `glgCAPXB` operon and ADP-glucose pyrophosphorylase in the proteobacterium *Rhodobacter sphaeroides* (contrast: canonical route present elsewhere, absent in *P. putida*).

**Direct vs inferred:** Gene presence/absence statements (glgC, OtsAB, EC counts, family signatures) are **direct** for UP000000556. Pathway *function* (that α-glucan is made by GlgE and not GlgA) is **inferred** from homology + the cited GlgE-pathway biochemistry in Actinobacteria; species transfer to *Pseudomonas* is **moderate-to-strong** at the genomic level but lacks a direct KT2440 knockout/metabolite study — the key open experiment.


## Artifacts

- [OpenScientist final report](PSEPK__glycogen_synthesis_and_mobilization__ppu00500-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__glycogen_synthesis_and_mobilization__ppu00500-deep-research-openscientist_artifacts/final_report.pdf)