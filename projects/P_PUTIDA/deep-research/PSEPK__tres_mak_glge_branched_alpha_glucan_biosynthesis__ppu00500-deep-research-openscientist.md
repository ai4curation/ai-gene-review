---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T14:45:05.772494'
end_time: '2026-09-01T15:04:22.679066'
duration_seconds: 1156.91
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: TreS-Mak-GlgE branched alpha-glucan biosynthesis
  module_summary: A reusable bacterial pathway that channels trehalose into branched
    alpha-glucan. Trehalose synthase operating in the catabolic direction forms maltose,
    maltokinase converts maltose to alpha-maltose 1-phosphate, GlgE uses that activated
    donor to extend alpha-1,4-glucan chains by maltosyl units, and GlgB introduces
    alpha-1,6 branches. TreS and Mak may be separate proteins or domains of one fusion
    protein; that architectural variation does not change the four reaction roles.
  module_outline: "- TreS-Mak-GlgE branched alpha-glucan biosynthesis\n  - 1. trehalose\
    \ isomerization to maltose\n  - TreS-dependent maltose formation\n    - TreS trehalose\
    \ synthase activity in the maltose-forming direction (molecular player: TreS trehalose\
    \ synthase family; activity or role: maltose alpha-D-glucosyltransferase activity)\n\
    \  - 2. maltose 1-phosphate formation\n  - Mak-dependent alpha-maltose 1-phosphate\
    \ formation\n    - Mak maltokinase activity (molecular player: maltokinase family;\
    \ activity or role: carbohydrate kinase activity)\n  - 3. alpha-1,4-glucan chain\
    \ extension\n  - GlgE-dependent alpha-glucan extension\n    - GlgE maltose-1-phosphate\
    \ maltosyltransferase activity (molecular player: GlgE maltosyltransferase family;\
    \ activity or role: hexosyltransferase activity)\n  - 4. alpha-glucan branching\n\
    \  - GlgB-dependent alpha-1,6 branching\n    - GlgB 1,4-alpha-glucan branching\
    \ activity (molecular player: GlgB alpha-glucan branching-enzyme family; activity\
    \ or role: 1,4-alpha-glucan branching enzyme activity)"
  module_connections: '- TreS-dependent maltose formation feeds into Mak-dependent
    alpha-maltose 1-phosphate formation: TreS supplies D-maltose to Mak.

    - Mak-dependent alpha-maltose 1-phosphate formation feeds into GlgE-dependent
    alpha-glucan extension: Mak supplies alpha-maltose 1-phosphate to GlgE.

    - GlgE-dependent alpha-glucan extension feeds into GlgB-dependent alpha-1,6 branching:
    GlgB branches the alpha-1,4-glucan chains extended by GlgE.'
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__tres_mak_glge_branched_alpha_glucan_biosynthesis__ppu00500-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__tres_mak_glge_branched_alpha_glucan_biosynthesis__ppu00500-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

TreS-Mak-GlgE branched alpha-glucan biosynthesis in Pseudomonas putida KT2440

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

A reusable bacterial pathway that channels trehalose into branched alpha-glucan. Trehalose synthase operating in the catabolic direction forms maltose, maltokinase converts maltose to alpha-maltose 1-phosphate, GlgE uses that activated donor to extend alpha-1,4-glucan chains by maltosyl units, and GlgB introduces alpha-1,6 branches. TreS and Mak may be separate proteins or domains of one fusion protein; that architectural variation does not change the four reaction roles.

### Provisional Biological Outline

- TreS-Mak-GlgE branched alpha-glucan biosynthesis
  - 1. trehalose isomerization to maltose
  - TreS-dependent maltose formation
    - TreS trehalose synthase activity in the maltose-forming direction (molecular player: TreS trehalose synthase family; activity or role: maltose alpha-D-glucosyltransferase activity)
  - 2. maltose 1-phosphate formation
  - Mak-dependent alpha-maltose 1-phosphate formation
    - Mak maltokinase activity (molecular player: maltokinase family; activity or role: carbohydrate kinase activity)
  - 3. alpha-1,4-glucan chain extension
  - GlgE-dependent alpha-glucan extension
    - GlgE maltose-1-phosphate maltosyltransferase activity (molecular player: GlgE maltosyltransferase family; activity or role: hexosyltransferase activity)
  - 4. alpha-glucan branching
  - GlgB-dependent alpha-1,6 branching
    - GlgB 1,4-alpha-glucan branching activity (molecular player: GlgB alpha-glucan branching-enzyme family; activity or role: 1,4-alpha-glucan branching enzyme activity)

### Known Relationships Among Steps

- TreS-dependent maltose formation feeds into Mak-dependent alpha-maltose 1-phosphate formation: TreS supplies D-maltose to Mak.
- Mak-dependent alpha-maltose 1-phosphate formation feeds into GlgE-dependent alpha-glucan extension: Mak supplies alpha-maltose 1-phosphate to GlgE.
- GlgE-dependent alpha-glucan extension feeds into GlgB-dependent alpha-1,6 branching: GlgB branches the alpha-1,4-glucan chains extended by GlgE.

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

# Commissioned Review: TreS–Mak–GlgE Branched α-Glucan Biosynthesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00500 "Starch and sucrose metabolism"
**Module under review:** TreS–Mak–GlgE–GlgB branched α-glucan biosynthesis (generic reusable bacterial module)

---

## 1. Executive Summary

The four-step **TreS–Mak–GlgE–GlgB** module that channels trehalose into intracellular branched α-glucan is **fully satisfiable** in *Pseudomonas putida* KT2440. Every reaction role maps cleanly onto a candidate gene within a single contiguous glycogen/trehalose locus spanning **PP_4050–PP_4060**. The defining architectural feature in KT2440 is that **steps 1 (trehalose synthase, TreS) and 2 (maltokinase, Mak) are fused into one bifunctional 1106-aa polypeptide, PP_4059 (treSB, Q88FN0)**, carrying two EC numbers (5.4.99.16 and 2.7.1.175). Steps 3 and 4 are encoded by dedicated single-copy genes: **GlgE = PP_4060 (Q88FM9, EC 2.4.99.16)** and **GlgB = PP_4058 (Q88FN1, EC 2.4.1.18)**. In mycobacteria, by contrast, TreS and the maltokinase Pep2 are *separate* proteins that assemble into a hetero-octameric complex — so KT2440 represents an architectural variant of the same two reaction roles, not a functional difference.

Critically, KT2440 **lacks GlgC (ADP-glucose pyrophosphorylase, EC 2.7.7.27) and the OtsAB trehalose-6-phosphate synthase/phosphatase pair**. An exhaustive proteome search returned glgA, glgB, glgE, glgP, and glgX but no glgC and no OtsAB. This configuration — the complete GlgE-pathway gene set present while glgC is absent — parallels *Streptomyces venezuelae* and supports the inference that the **maltose-1-phosphate/GlgE route is the primary (and possibly sole) pathway to intracellular branched α-glucan** in this organism. Because OtsAB is absent, the trehalose pool feeding module step 1 most plausibly derives from the **TreYZ pathway** (treY/PP_4053 + treZ/PP_4051), which produces trehalose from maltooligosaccharides/glycogen, and/or from environmental trehalose.

For curation, the practical message is that the KEGG ppu00500 candidate list of 18 genes is **over-broad**: only **PP_4058, PP_4059, and PP_4060** are true members of this specific biosynthetic module. The remaining candidates belong to neighboring processes — cellulose (β-1,4-glucan) synthesis, the TreYZ trehalose-*from*-glycogen route, classic glycogen turnover, and central hexose-phosphate metabolism — and should be excluded from the module while remaining valid members of the broader starch/sucrose map. All module gene calls are **homology-grade (evidence PE=3)**; no direct KT2440 biochemistry exists, but same-species *P. putida* TreS biochemistry and UniProt's explicit pathway assignment for PP_4060 substantially strengthen the calls. **Bottom line:** mark the module **SATISFIED** with a three-gene membership {PP_4058, PP_4059, PP_4060}; flag glgA/PP_4050 as *candidate_uncertain* given the GlgC gap; and exclude the remaining 14 candidates from this module.

---

## 2. Target-Organism Pathway Definition

### 2.1 What the module includes

The TreS–Mak–GlgE–GlgB module is a **reusable, cytosolic bacterial pathway that converts trehalose into a branched α-1,4/α-1,6-glucan** through four sequential reaction roles:

1. **Trehalose → maltose** — trehalose synthase (TreS) operating in the maltose-forming (catabolic) direction; maltose α-D-glucosyltransferase activity (EC 5.4.99.16).
2. **Maltose → α-maltose 1-phosphate** — maltokinase (Mak/Pep2); carbohydrate kinase activity (EC 2.7.1.175).
3. **α-maltose 1-phosphate + [α-1,4-glucan]ₙ → [α-1,4-glucan]ₙ₊₂ + Pᵢ** — GlgE maltosyltransferase; extends chains by maltosyl units (EC 2.4.99.16).
4. **α-1,4-glucan → branched α-glucan** — GlgB branching enzyme introduces α-1,6 linkages (EC 2.4.1.18).

The canonical four-step scheme was defined in *Mycobacterium tuberculosis* by Kalscheuer et al. ([PMID: 20305657](https://pubmed.ncbi.nlm.nih.gov/20305657/)), who described "a new pathway from trehalose to alpha-glucan … comprising four enzymatic steps mediated by TreS, Pep2, GlgE … and GlgB."

### 2.2 Neighboring pathways to keep separate

For accurate module boundaries in KT2440, the following processes — although co-listed under KEGG ppu00500 — must be **excluded**:

- **Cellulose (β-1,4-glucan) synthesis:** bcsA/PP_2635 (EC 2.4.1.12, GT2/PilZ). This makes a β-linked, not α-linked, glucan and is mechanistically unrelated.
- **TreYZ trehalose-*from*-glycogen pathway:** treY/PP_4053 (EC 5.4.99.15) + treZ/PP_4051 (EC 3.2.1.141). This runs in the *reverse* metabolic direction (glucan → trehalose) and is a *supplier* of trehalose, not part of the α-glucan biosynthetic module itself.
- **Classic glycogen/maltodextrin turnover:** glgA/PP_4050 (EC 2.4.1.21), glgP/PP_5041 (EC 2.4.1.1), glgX/PP_4055 (glycogen debranching), malQ/PP_4052 (amylomaltase, GH77).
- **Central hexose-phosphate metabolism:** glk, pgi1/pgi2, pgm, algC, cpsG, galU.

### 2.3 Alternate names and database definitions

- The module is variously called the **"GlgE pathway"**, the **"TreS–Mak–GlgE pathway"**, or the **"trehalose-to-α-glucan"** pathway.
- The maltokinase is called **Mak** in the generic module but **Pep2** in mycobacterial literature (e.g., Rv0127).
- KEGG folds all of these genes into the broad overview map **ppu00500 "Starch and sucrose metabolism"**, which is far broader than the biosynthetic module and is the source of the candidate-list over-breadth.
- GlgE is EC **2.4.99.16**; its systematic name is **(1→4)-α-D-glucan:α-maltose-1-phosphate α-D-maltosyltransferase (GMPMT)**.

---

## 3. Expected Step Model and Satisfiability

The table below maps each expected step to its KT2440 gene, copy number, evidence type, and disposition.

| Step | Reaction role | EC | KT2440 gene | UniProt | Copy number | Disposition |
|------|---------------|-----|-------------|---------|-------------|-------------|
| 1 | Trehalose ⇌ maltose (TreS) | 5.4.99.16 | **PP_4059** (treSB, fused) + PP_2918 (treSA, standalone) | Q88FN0 / Q88IT1 | 2 paralogs | **covered** |
| 2 | Maltose → α-maltose 1-P (Mak) | 2.7.1.175 | **PP_4059** (treSB, fused C-terminal domain) | Q88FN0 | 1 | **covered** |
| 3 | α-glucan extension (GlgE) | 2.4.99.16 | **PP_4060** (glgE) | Q88FM9 | 1 | **covered** |
| 4 | α-1,6 branching (GlgB) | 2.4.1.18 | **PP_4058** (glgB) | Q88FN1 | 1 | **covered** |

**Satisfiability verdict: all four steps covered.** Steps 2, 3, and 4 are single-copy and unambiguous. Only step 1 (TreS) has paralog redundancy (see §4.5). No expected step is missing, and none is judged *not_expected_in_target_taxon*.

```
   [trehalose]                                                    (from TreYZ:
        |                                                          PP_4053 + PP_4051,
        |  Step 1  TreS  (EC 5.4.99.16)   -- PP_4059 N-terminal    or environment)
        v          treSB fusion                GH13 domain
   [D-maltose]
        |
        |  Step 2  Mak  (EC 2.7.1.175)    -- PP_4059 C-terminal
        v          treSB fusion                kinase-like domain
   [alpha-maltose 1-phosphate]
        |
        |  Step 3  GlgE (EC 2.4.99.16)    -- PP_4060
        v          maltosyltransferase
   [alpha-1,4-glucan]n+2  (chain extended by maltosyl units)
        |
        |  Step 4  GlgB (EC 2.4.1.18)     -- PP_4058
        v          branching enzyme
   [branched alpha-1,4/1,6-glucan]   <-- final product

   NOTE: GlgC (ADP-glucose pyrophosphorylase, EC 2.7.7.27) ABSENT
         OtsAB (EC 2.4.1.15 / 3.1.3.12) ABSENT
         => GlgE/maltose-1-P route is the PRIMARY alpha-glucan pathway
```

---

## 4. Candidate Genes and Evidence

### 4.1 The three true module members (Findings F001, F006, F007)

All four module steps are encoded within the contiguous PP_4050–PP_4060 glycogen/trehalose locus. UniProt/InterPro annotation (homology-based, PE=3) maps every step:

- **PP_4058 / GlgB / Q88FN1** — 1,4-α-glucan branching enzyme (EC 2.4.1.18), GH13 GlgB subfamily (InterPro IPR006407, GlgB-specific). Single-copy for EC 2.4.1.18. Covers **step 4**.
- **PP_4059 / TreSB / Q88FN0** — bifunctional TreS–maltokinase fusion (see §4.2). Covers **steps 1 and 2**.
- **PP_4060 / GlgE / Q88FM9** — maltosyltransferase (EC 2.4.99.16), GH13 GlgE subfamily (InterPro IPR026585, GlgE-specific). Single-copy for EC 2.4.99.16. Covers **step 3**.

UniProt's curated FUNCTION comment for PP_4060 is decisive for module assignment: GlgE is "a maltosyltransferase that uses maltose 1-phosphate (M1P) … involved in a branched alpha-glucan biosynthetic pathway from trehalose, together with TreS, Mak and GlgB." This is an explicit, curator-level placement of PP_4060 into exactly this module (Finding F006).

### 4.2 PP_4059 — the TreS–Mak fusion (Finding F002)

PP_4059 (Q88FN0, 1106 aa) is the pivotal gene. It carries **two EC numbers on one polypeptide**: 5.4.99.16 (maltose α-D-glucosyltransferase = trehalose synthase) and 2.7.1.175 (maltokinase). Its domain architecture is an N-terminal GH13 α-amylase/TreS module (InterPro IPR012810 TreS/α-amylase_N + IPR006047 GH13; Pfam PF00128) fused to a C-terminal aminoglycoside-phosphotransferase-like maltokinase (InterPro IPR012811 TreS_maltokinase_C + IPR040999 Mak_N_cap + IPR011009 kinase-like superfamily; Pfam PF18085 Mak_N_cap + PF16657).

This fusion contrasts with mycobacteria, where TreS (Rv0126) and Pep2/Mak (Rv0127) are **separate genes**. Roldán et al. ([PMID: 23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/)) showed that "Together with Pep2, TreS forms a hetero-octameric complex, and we demonstrate that complex formation markedly accelerates maltokinase activity of Pep2." The KT2440 fusion co-localizes the two activities covalently rather than by complex formation — an architectural variant that does not change the reaction roles. This same physical association is structurally corroborated by the crystal structure of the TreS:Pep2 complex ([PMID: 30877199](https://pubmed.ncbi.nlm.nih.gov/30877199/)).

### 4.3 Same-species biochemical support (Finding F006)

Although all KT2440 module calls are homology-grade (PE=3), two *Pseudomonas*-genus biochemical studies materially strengthen step 1:

- **TreS from *P. putida* P06** experimentally catalyzes the reversible maltose ⇌ trehalose interconversion ([PMID: 24563286](https://pubmed.ncbi.nlm.nih.gov/24563286/)): "Trehalose synthase (TreS) from Pseudomonas putida P06 catalyzes the reversible interconversion of maltose and trehalose." This is direct, *same-species* biochemistry for the TreS activity.
- A **~1,122-aa *Pseudomonas* sp. P8005 TreS** ([PMID: 23715900](https://pubmed.ncbi.nlm.nih.gov/23715900/)) closely matches the 1106-aa length of KT2440 treSB, corroborating that the extended/fused architecture is characteristic within the genus.

### 4.4 The GlgC/OtsAB gap and pathway primacy (Finding F004)

An exhaustive UniProt proteome search (organism_id:160488) returned glgA, glgB, glgE, glgP, glgX but **no glgC** — EC 2.7.7.27 (glucose-1-phosphate adenylyltransferase) is absent, and no ADP-glucose-producing enzyme appears among any annotated adenylyltransferase. **OtsAB is also absent**: EC 2.4.1.15 (trehalose-6-P synthase) and EC 3.1.3.12 (trehalose-6-P phosphatase) returned zero hits.

This matters for pathway primacy. In *M. tuberculosis*, α-glucan is "exclusively assembled intracellularly utilizing the building block α-maltose-1-phosphate as the substrate for the maltosyltransferase GlgE, with subsequent branching … by the branching enzyme GlgB" ([PMID: 27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/)). In *S. venezuelae*, "The genome … contains all the genes coding for the GlgE pathway enzymes but none of those of related pathways, including glgC and glgA of the glycogen pathway" ([PMID: 27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/)). KT2440's configuration (complete GlgE gene set, glgC absent) parallels these precedents and supports the inference that the **GlgE/maltose-1-P route is the primary intracellular α-glucan pathway** in KT2440.

### 4.5 Paralog ambiguity and trehalose supply (Finding F005)

Two TreS paralogs exist in KT2440:
- **treSB / PP_4059 / Q88FN0** — 1106 aa, **fused** to the maltokinase domain, in the glg/tre cluster.
- **treSA / PP_2918 / Q88IT1** — 688 aa, **standalone** (no Mak domain), at a distant locus.

Only PP_4059 carries the maltokinase activity required for step 2, so **PP_4059 is the module-relevant TreS**; PP_2918 is a paralog that may contribute maltose but cannot phosphorylate it. Because OtsAB is absent, the trehalose pool feeding step 1 most plausibly derives from **TreYZ** (treY/PP_4053 EC 5.4.99.15 + treZ/PP_4051 EC 3.2.1.141), which converts maltooligosaccharides/glycogen into trehalose, and/or from environmental trehalose.

### 4.6 Full 18-gene candidate disposition (Finding F003)

| Gene | Locus | UniProt | Annotation / EC | Process | Module disposition |
|------|-------|---------|-----------------|---------|--------------------|
| **glgB** | PP_4058 | Q88FN1 | Branching enzyme (2.4.1.18) | α-glucan branching | **MODULE — step 4** |
| **treSB** | PP_4059 | Q88FN0 | TreS + Mak fusion (5.4.99.16; 2.7.1.175) | trehalose→maltose→M1P | **MODULE — steps 1+2** |
| **glgE** | PP_4060 | Q88FM9 | Maltosyltransferase (2.4.99.16) | α-glucan extension | **MODULE — step 3** |
| glgA | PP_4050 | Q88FN9 | Glycogen synthase (2.4.1.21) | glycogen synth (ADP-glc) | candidate_uncertain |
| treZ | PP_4051 | Q88FN8 | Trehalohydrolase (3.2.1.141) | TreYZ (trehalose supply) | exclude (supplier) |
| malQ | PP_4052 | Q88FN7 | Amylomaltase (2.4.1.25) | maltodextrin turnover | exclude |
| treY | PP_4053 | Q88FN6 | Maltooligosyl-tre synthase (5.4.99.15) | TreYZ (trehalose supply) | exclude (supplier) |
| glgX | PP_4055 | Q88FN4 | Debranching (3.2.1.33) | glycogen turnover | exclude |
| glgP | PP_5041 | Q88CY8 | Glucan phosphorylase (2.4.1.1) | glycogen turnover | exclude |
| bcsA | PP_2635 | Q88JL4 | Cellulose synthase (2.4.1.12) | β-1,4-glucan (cellulose) | exclude (β-glucan) |
| glk | PP_1011 | Q88P42 | Glucokinase (2.7.1.2) | central metabolism | exclude |
| bglX | PP_1403 | Q88N13 | β-glucosidase (3.2.1.21) | glycoside hydrolysis | exclude |
| cpsG | PP_1777 | Q88LZ9 | Phosphomannomutase (5.4.2.8) | central metabolism | exclude |
| pgi1 | PP_1808 | Q88LW9 | G6P isomerase (5.3.1.9) | central metabolism | exclude |
| pgm | PP_3578 | Q88GY7 | Phosphoglucomutase (5.4.2.2) | central metabolism | exclude |
| galU | PP_3821 | Q88GA4 | UDP-glucose PPase (2.7.7.9) | UDP-glucose supply | exclude |
| pgi2 | PP_4701 | Q88DW7 | G6P isomerase (5.3.1.9) | central metabolism | exclude |
| algC | PP_5288 | Q88C93 | PMM/PGM (5.4.2.2; 5.4.2.8) | central metabolism | exclude |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

1. **KEGG ppu00500 breadth is the main over-annotation risk.** 15 of 18 candidates are not members of the biosynthetic module. Curators pulling from the ppu00500 bucket will over-populate the module unless it is trimmed to {PP_4058, PP_4059, PP_4060}. This is a bucket-scope artifact, not an error in any individual gene annotation.

2. **glgA/PP_4050 is genuinely ambiguous (candidate_uncertain).** Classic GlgA glycogen synthase (EC 2.4.1.21) uses ADP-glucose produced by GlgC. With **glgC absent**, the physiological substrate/role of PP_4050 is unclear — it may be non-functional for its annotated reaction, may use a different sugar-nucleotide donor, or may be an over-propagated annotation. This gene warrants explicit *candidate_uncertain* flagging and full review.

3. **TreS paralog ambiguity.** treSA/PP_2918 and treSB/PP_4059 both carry EC 5.4.99.16. Only the fused PP_4059 is module-relevant. A naive EC-based mapping could incorrectly assign PP_2918 to the module.

4. **All calls are homology-grade (PE=3).** No direct KT2440 experiment demonstrates GlgE maltosyltransferase activity, maltokinase activity, or α-glucan production. A dedicated PubMed search for KT2440-specific GlgE/α-glucan/maltose-1-phosphate evidence returned **zero papers** (Finding F007). Confidence rests on: (a) same-genus *P. putida* TreS biochemistry; (b) UniProt's explicit pathway-level curation of PP_4060; and (c) InterPro subfamily-specific signatures (GlgE-specific IPR026585, GlgB-specific IPR006407) that are diagnostic rather than broad.

5. **Broad EC/GO mappings.** GlgE's EC (2.4.99.16) and GH13 membership are specific enough, but generic "hexosyltransferase" GO terms could over-generalize. GlgB shares GH13 with many α-amylase-family enzymes; rely on the GlgB-specific InterPro signature, not GH13 alone.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Gene(s) | Rationale |
|-------------|--------------------|---------|-----------|
| 1 — TreS (trehalose→maltose) | **covered** | PP_4059 (module), PP_2918 (paralog) | Fused GH13 TreS domain; same-species P. putida TreS biochemistry |
| 2 — Mak (maltose→M1P) | **covered** | PP_4059 (fused kinase domain) | Single-copy EC 2.7.1.175; Mak_N_cap + kinase-like domains |
| 3 — GlgE (α-glucan extension) | **covered** | PP_4060 | Single-copy; GlgE-specific InterPro; explicit UniProt pathway comment |
| 4 — GlgB (α-1,6 branching) | **covered** | PP_4058 | Single-copy; GlgB-specific InterPro |

**Module verdict: SATISFIED.**

Additional curation actions:
- **Trim module membership** to exactly {PP_4058, PP_4059, PP_4060}. Do not inherit the full ppu00500 candidate list.
- **Flag glgA/PP_4050 as candidate_uncertain** and note the GlgC gap in the module rationale.
- **Document the fusion architecture** of PP_4059 explicitly (steps 1+2 in one protein) so that automated "one gene per step" checks do not falsely report step 2 as a gap.
- **Record the GlgC/OtsAB absence** as supporting evidence that the GlgE route is primary; this is a positive discriminating feature, not a gap in *this* module.
- **Note trehalose supply via TreYZ** (PP_4053/PP_4051) as an upstream dependency, but keep TreYZ genes *out* of the module itself (they are suppliers running in the reverse direction).
- **GO terms:** existing GO/EC mappings are adequate; no new GO term request appears necessary. If a module-specific GO annotation is desired, the "α-glucan biosynthetic process from trehalose" framing is well supported by the mycobacterial literature and can be transferred with a homology (ISS/IEA) evidence code, explicitly flagged as inferred.
- **Module boundaries are correct for this organism**; the generic module does not need revision for KT2440 beyond documenting the TreS–Mak fusion, which the generic scope already anticipates ("TreS and Mak may be separate proteins or domains of one fusion protein").

---

## 7. Genes to Promote to Full `fetch-gene` Review

Priority order:

1. **PP_4059 (treSB, Q88FN0)** — highest priority. Confirm the bifunctional TreS+Mak assignment, both EC numbers, domain boundaries, and that this (not PP_2918) is the module-relevant TreS. The dual-EC fusion is the single most curation-sensitive call in the module.
2. **PP_4060 (glgE, Q88FM9)** — confirm GlgE-specific subfamily assignment and the maltose-1-phosphate substrate; UniProt already places it in the pathway, but a full review cements step 3.
3. **PP_4050 (glgA, Q88FN9)** — resolve the candidate_uncertain status: is glycogen synthase functional/relevant given the GlgC gap? Determine sugar-nucleotide donor availability.
4. **PP_4058 (glgB, Q88FN1)** — confirm branching-enzyme assignment (lower priority; annotation is clean and single-copy).
5. **PP_2918 (treSA, Q88IT1)** — clarify the role of the standalone TreS paralog and whether it feeds maltose into the pathway independently of PP_4059.

---

## 8. Evidence Base and Key References

| PMID | Title (abbrev.) | Organism | How it supports the review |
|------|-----------------|----------|----------------------------|
| [20305657](https://pubmed.ncbi.nlm.nih.gov/20305657/) | Self-poisoning of *M. tuberculosis* by targeting GlgE | *M. tuberculosis* | Defines the canonical four-step TreS–Pep2(Mak)–GlgE–GlgB module mapped onto KT2440 (F001) |
| [23901909](https://pubmed.ncbi.nlm.nih.gov/23901909/) | α-glucan synthesis via a hetero-octameric TreS–Pep2 complex | *M. tuberculosis* | Shows TreS and Mak are separate, complex-forming proteins in mycobacteria; KT2440 fuses them into PP_4059 (F002) |
| [27513637](https://pubmed.ncbi.nlm.nih.gov/27513637/) | Metabolic network for α-glucan biosynthesis | *M. tuberculosis* | α-glucan "exclusively assembled … from α-maltose-1-phosphate … GlgE … GlgB"; supports GlgE route as primary where glgC-independent (F004) |
| [27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/) | glgE null mutant accumulates α-maltose 1-phosphate | *S. venezuelae* | Precedent for a complete GlgE pathway with glgC/glgA absent, paralleling KT2440 (F004) |
| [24563286](https://pubmed.ncbi.nlm.nih.gov/24563286/) | Homology modeling and function of TreS from *P. putida* P06 | ***P. putida*** | Direct same-species biochemistry: TreS catalyzes reversible maltose⇌trehalose, supporting step 1 (F006) |
| [23715900](https://pubmed.ncbi.nlm.nih.gov/23715900/) | Novel TreS from marine *Pseudomonas* sp. P8005 | *Pseudomonas* sp. | ~1,122-aa TreS matches the fused KT2440 treSB length (1106 aa), corroborating fusion architecture in the genus (F006) |
| [20118231](https://pubmed.ncbi.nlm.nih.gov/20118231/) | GMPMT transfers maltose from maltose-1-P to glycogen | *M. smegmatis* | Biochemically characterizes the GlgE (GMPMT) reaction and proposes trehalose→glycogen via TreS+Mak+GMPMT |
| [26616850](https://pubmed.ncbi.nlm.nih.gov/26616850/) | Structure of *M. thermoresistibile* GlgE | *M. thermoresistibile* | Structural context for GlgE catalytic mechanism (step 3) |
| [27531751](https://pubmed.ncbi.nlm.nih.gov/27531751/) | Acceptor/secondary sites of *S. coelicolor* GlgE | *S. coelicolor* | Defines GlgE acceptor specificity, informing step-3 substrate model |
| [26245983](https://pubmed.ncbi.nlm.nih.gov/26245983/) | Crystal structures of *M. tuberculosis* GlgE + inhibitors | *M. tuberculosis* | GlgE elongates cytosolic branched α-glucan using M1P; structural validation |
| [30877199](https://pubmed.ncbi.nlm.nih.gov/30877199/) | Crystal structure of the TreS:Pep2 complex | *M. tuberculosis* | Structural basis of the TreS–Mak interaction that KT2440 replaces with a fusion |
| [25137149](https://pubmed.ncbi.nlm.nih.gov/25137149/) | Poly-hydroxypyrolidine GlgE inhibitor | *M. tuberculosis* | Confirms GlgE M1P substrate and the toxic-M1P-accumulation phenotype on GlgE loss |
| [24820953](https://pubmed.ncbi.nlm.nih.gov/24820953/) | Homology model of *M. tuberculosis* GlgE | *M. tuberculosis* | GlgE belongs to the α-amylase (GH13) family; five-domain architecture |

**Evidence provenance summary:**
- **Direct for target species (*P. putida*):** TreS maltose⇌trehalose biochemistry ([PMID: 24563286](https://pubmed.ncbi.nlm.nih.gov/24563286/)) and genus-level TreS length ([PMID: 23715900](https://pubmed.ncbi.nlm.nih.gov/23715900/)). These are strongest for step 1.
- **Direct for target strain (KT2440):** None. All gene calls are PE=3 homology inferences plus UniProt/InterPro curation.
- **Transferred from related organisms (mycobacteria, *Streptomyces*):** The four-step module scheme, GlgE mechanism, and GlgC-independence precedent. Transfer strength is **moderate-to-strong** for the reaction roles (deeply conserved GH13 chemistry) but **weaker** for regulation, flux direction, and the physiological role of the α-glucan product in KT2440.

---

## 9. Limitations and Knowledge Gaps

1. **No strain-specific experiments.** No published study demonstrates GlgE-pathway function, α-glucan production, or maltose-1-phosphate metabolism directly in KT2440. All module calls are homology-grade (PE=3).
2. **glgA/PP_4050 role unresolved.** The GlgC gap leaves the classic glycogen-synthase branch physiologically ambiguous; whether glycogen and GlgE-derived α-glucan are the same or distinct polymers in KT2440 is unknown.
3. **Trehalose source inferred, not measured.** TreYZ is the most plausible trehalose supplier given the OtsAB absence, but flux from TreYZ (or environmental uptake) into module step 1 has not been quantified in KT2440.
4. **Product identity and localization unknown.** Whether the α-glucan is intracellular storage, a capsule, or both — as it varies across mycobacteria — is not established for KT2440.
5. **Directionality of TreS.** TreS is reversible; whether PP_4059 runs net in the maltose-forming direction in vivo (as the module requires) versus the trehalose-forming direction depends on cellular conditions not measured here.
6. **Absence calls rely on annotation completeness.** The GlgC/OtsAB "absent" conclusions rest on UniProt proteome annotation; a highly diverged or mis-annotated ortholog cannot be fully excluded without dedicated HMM/structural searches.

---

## 10. Proposed Follow-up Experiments and Actions

**Curation actions (immediate):**
1. Set module status to **SATISFIED** with membership {PP_4058, PP_4059, PP_4060}; record the PP_4059 fusion so automated step-2 gap checks are suppressed.
2. Flag **glgA/PP_4050 as candidate_uncertain**; promote PP_4059, PP_4060, and PP_4050 to full `fetch-gene` review (§7).
3. Annotate the **GlgC/OtsAB absence** as a positive discriminator that the GlgE route is primary; note **TreYZ (PP_4053/PP_4051)** as the upstream trehalose supplier, kept outside the module.

**Bioinformatic follow-up:**
4. Run HMM/structure-based searches (e.g., against Pfam GlgC HMMs and AlphaFold models) to confirm GlgC and OtsAB are truly absent rather than diverged.
5. Verify PP_4059 domain boundaries and confirm that maltokinase catalytic residues are intact in the C-terminal domain.

**Experimental validation (if warranted):**
6. Construct ΔglgE (PP_4060) and ΔtreSB (PP_4059) mutants and assay for α-maltose-1-phosphate accumulation and loss of α-glucan — the diagnostic phenotype seen in *S. venezuelae* ([PMID: 27121970](https://pubmed.ncbi.nlm.nih.gov/27121970/)) and the toxic-accumulation death phenotype in mycobacteria ([PMID: 25137149](https://pubmed.ncbi.nlm.nih.gov/25137149/)).
7. Assay recombinant PP_4059 for both TreS and maltokinase activities to confirm the fusion is doubly active, and PP_4060 for maltosyltransferase activity using α-maltose-1-phosphate as donor.
8. Characterize the α-glucan product (linkage analysis, localization) to establish its physiological role in KT2440.
9. Test whether TreYZ supplies the trehalose feeding step 1 via ΔtreYZ metabolite profiling.

---

*Prepared as a species-aware module satisfiability review. All gene-level calls for KT2440 are homology-grade (PE=3) unless otherwise noted; species transfer from mycobacteria/Streptomyces is explicitly flagged throughout.*


## Artifacts

- [OpenScientist final report](PSEPK__tres_mak_glge_branched_alpha_glucan_biosynthesis__ppu00500-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__tres_mak_glge_branched_alpha_glucan_biosynthesis__ppu00500-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20305657
2. PMID:23901909
3. PMID:30877199
4. PMID:24563286
5. PMID:23715900
6. PMID:27513637
7. PMID:27121970
8. PMID:25137149