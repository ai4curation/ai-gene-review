---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T07:54:44.452687'
end_time: '2026-07-15T08:09:00.230210'
duration_seconds: 855.78
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: pentose_phosphate_pathway
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00030
  pathway_id: ppu00030
  pathway_name: Pentose phosphate pathway
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00030 with 19 primary genes; module
    area: central_carbon.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '36'
  candidate_genes: '- rpe: PP_0415 | Q88QS3 | Ribulose-phosphate 3-epimerase (EC 5.1.3.1)
    (EC 5.1.3.1; primary bucket kegg:ppu00040)

    - prs: PP_0722 | Q88PX6 | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1)
    (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosyl diphosphate
    synthase) (Phosphoribosyl pyrophosphate synthase) (P-Rib-PP synthase) (PRPP synthase)
    (PRPPase) (EC 2.7.6.1; primary bucket kegg:ppu00030)

    - trxB: PP_0786 | Q88PR2 | Thioredoxin reductase (EC 1.8.1.9) (EC 1.8.1.9; primary
    bucket kegg:ppu00030)

    - edd: PP_1010 | Q88P43 | Phosphogluconate dehydratase (EC 4.2.1.12) (EC 4.2.1.12;
    primary bucket kegg:ppu00030)

    - zwfA: PP_1022 | Q88P31 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49)
    (EC 1.1.1.49; primary bucket kegg:ppu00480)

    - pgl: PP_1023 | Q88P30 | 6-phosphogluconolactonase (6PGL) (EC 3.1.1.31) (EC 3.1.1.31;
    primary bucket kegg:ppu00030)

    - eda: PP_1024 | Q88P29 | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14)
    (EC 4.1.2.14; primary bucket kegg:ppu00030)

    - ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate
    reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81;
    primary bucket kegg:ppu00030)

    - gcd: PP_1444 | Q88MX4 | Quinoprotein glucose dehydrogenase (EC 1.1.5.2) (EC
    1.1.5.2; primary bucket kegg:ppu00030)

    - PP_1661: PP_1661 | Q88MB3 | Dehydrogenase subunit (primary bucket kegg:ppu00030)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - pgi1: PP_1808 | Q88LW9 | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9)
    (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) (EC 5.3.1.9;
    primary bucket kegg:ppu00500)

    - ppgL: PP_2021 | Q88LB4 | L-alpha-hydroxyglutaric acid gamma-lactonase (primary
    bucket kegg:ppu00030)

    - tal: PP_2168 | Q88KX1 | Transaldolase (EC 2.2.1.2) (EC 2.2.1.2; primary bucket
    kegg:ppu00710)

    - rbsK: PP_2458 | Q88K34 | Ribokinase (RK) (EC 2.7.1.15) (EC 2.7.1.15; primary
    bucket kegg:ppu00030)

    - PP_2744: PP_2744 | Q88JA5 | ribose-phosphate diphosphokinase (EC 2.7.6.1) (EC
    2.7.6.1; primary bucket kegg:ppu00030)

    - ptxD: PP_3376 | Q88HI1 | Phosphonate dehydrogenase (EC 1.20.1.1) (EC 1.20.1.1;
    primary bucket kegg:ppu00480)

    - kguK: PP_3378 | Q88HH9 | 2-ketogluconokinase (EC 2.7.1.13) (EC 2.7.1.13; primary
    bucket kegg:ppu00030)

    - PP_3382: PP_3382 | Q88HH6 | Gluconate 2-dehydrogenase cytochrome c subunit (EC
    1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)

    - PP_3383: PP_3383 | Q88HH5 | Gluconate 2-dehydrogenase flavoprotein subunit (EC
    1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)

    - PP_3384: PP_3384 | Q88HH4 | Gluconate 2-dehydrogenase gamma subunit (EC 1.1.99.3)
    (EC 1.1.99.3; primary bucket kegg:ppu00030)

    - gnuK: PP_3416 | Q88HE4 | Gluconokinase (EC 2.7.1.12) (EC 2.7.1.12; primary bucket
    kegg:ppu00030)

    - PP_3443: PP_3443 | Q88HB7 | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.59)
    (EC 1.2.1.59; primary bucket kegg:ppu00030)

    - pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary
    bucket kegg:ppu00052)

    - adhB: PP_3623 | Q88GU4 | Alcohol dehydrogenase cytochrome c subunit (primary
    bucket kegg:ppu00030)

    - zwfB: PP_4042 | Q88FP7 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49)
    (EC 1.1.1.49; primary bucket kegg:ppu00480)

    - gntZ: PP_4043 | Q88FP6 | 6-phosphogluconate dehydrogenase, decarboxylating (EC
    1.1.1.44) (EC 1.1.1.44; primary bucket kegg:ppu00480)

    - ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81;
    primary bucket kegg:ppu00561)

    - phnN: PP_4469 | Q88EJ3 | Ribose 1,5-bisphosphate phosphokinase PhnN (EC 2.7.4.23)
    (Ribose 1,5-bisphosphokinase) (EC 2.7.4.23; primary bucket kegg:ppu00030)

    - pgi2: PP_4701 | Q88DW7 | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9)
    (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) (EC 5.3.1.9;
    primary bucket kegg:ppu00500)

    - fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC
    4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)

    - tktA: PP_4965 | Q88D62 | Transketolase (EC 2.2.1.1) (EC 2.2.1.1; primary bucket
    kegg:ppu00710)

    - fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1)
    (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11;
    primary bucket kegg:ppu00710)

    - rpiA: PP_5150 | Q88CN0 | Ribose-5-phosphate isomerase A (EC 5.3.1.6) (Phosphoriboisomerase
    A) (PRI) (EC 5.3.1.6; primary bucket kegg:ppu00710)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

    - zwf: PP_5351 | Q88C32 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49)
    (EC 1.1.1.49; primary bucket kegg:ppu00480)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__pentose_phosphate_pathway__ppu00030-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__pentose_phosphate_pathway__ppu00030-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

pentose_phosphate_pathway in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00030
- Resolved ID: ppu00030
- Resolved name: Pentose phosphate pathway
- Source: KEGG

Resolved local bucket kegg:ppu00030 with 19 primary genes; module area: central_carbon.

## Candidate Genes From Local Metadata

Candidate gene count: 36

- rpe: PP_0415 | Q88QS3 | Ribulose-phosphate 3-epimerase (EC 5.1.3.1) (EC 5.1.3.1; primary bucket kegg:ppu00040)
- prs: PP_0722 | Q88PX6 | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1) (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosyl diphosphate synthase) (Phosphoribosyl pyrophosphate synthase) (P-Rib-PP synthase) (PRPP synthase) (PRPPase) (EC 2.7.6.1; primary bucket kegg:ppu00030)
- trxB: PP_0786 | Q88PR2 | Thioredoxin reductase (EC 1.8.1.9) (EC 1.8.1.9; primary bucket kegg:ppu00030)
- edd: PP_1010 | Q88P43 | Phosphogluconate dehydratase (EC 4.2.1.12) (EC 4.2.1.12; primary bucket kegg:ppu00030)
- zwfA: PP_1022 | Q88P31 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) (EC 1.1.1.49; primary bucket kegg:ppu00480)
- pgl: PP_1023 | Q88P30 | 6-phosphogluconolactonase (6PGL) (EC 3.1.1.31) (EC 3.1.1.31; primary bucket kegg:ppu00030)
- eda: PP_1024 | Q88P29 | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14) (EC 4.1.2.14; primary bucket kegg:ppu00030)
- ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81; primary bucket kegg:ppu00030)
- gcd: PP_1444 | Q88MX4 | Quinoprotein glucose dehydrogenase (EC 1.1.5.2) (EC 1.1.5.2; primary bucket kegg:ppu00030)
- PP_1661: PP_1661 | Q88MB3 | Dehydrogenase subunit (primary bucket kegg:ppu00030)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- pgi1: PP_1808 | Q88LW9 | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- ppgL: PP_2021 | Q88LB4 | L-alpha-hydroxyglutaric acid gamma-lactonase (primary bucket kegg:ppu00030)
- tal: PP_2168 | Q88KX1 | Transaldolase (EC 2.2.1.2) (EC 2.2.1.2; primary bucket kegg:ppu00710)
- rbsK: PP_2458 | Q88K34 | Ribokinase (RK) (EC 2.7.1.15) (EC 2.7.1.15; primary bucket kegg:ppu00030)
- PP_2744: PP_2744 | Q88JA5 | ribose-phosphate diphosphokinase (EC 2.7.6.1) (EC 2.7.6.1; primary bucket kegg:ppu00030)
- ptxD: PP_3376 | Q88HI1 | Phosphonate dehydrogenase (EC 1.20.1.1) (EC 1.20.1.1; primary bucket kegg:ppu00480)
- kguK: PP_3378 | Q88HH9 | 2-ketogluconokinase (EC 2.7.1.13) (EC 2.7.1.13; primary bucket kegg:ppu00030)
- PP_3382: PP_3382 | Q88HH6 | Gluconate 2-dehydrogenase cytochrome c subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- PP_3383: PP_3383 | Q88HH5 | Gluconate 2-dehydrogenase flavoprotein subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- PP_3384: PP_3384 | Q88HH4 | Gluconate 2-dehydrogenase gamma subunit (EC 1.1.99.3) (EC 1.1.99.3; primary bucket kegg:ppu00030)
- gnuK: PP_3416 | Q88HE4 | Gluconokinase (EC 2.7.1.12) (EC 2.7.1.12; primary bucket kegg:ppu00030)
- PP_3443: PP_3443 | Q88HB7 | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.59) (EC 1.2.1.59; primary bucket kegg:ppu00030)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- adhB: PP_3623 | Q88GU4 | Alcohol dehydrogenase cytochrome c subunit (primary bucket kegg:ppu00030)
- zwfB: PP_4042 | Q88FP7 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) (EC 1.1.1.49; primary bucket kegg:ppu00480)
- gntZ: PP_4043 | Q88FP6 | 6-phosphogluconate dehydrogenase, decarboxylating (EC 1.1.1.44) (EC 1.1.1.44; primary bucket kegg:ppu00480)
- ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81; primary bucket kegg:ppu00561)
- phnN: PP_4469 | Q88EJ3 | Ribose 1,5-bisphosphate phosphokinase PhnN (EC 2.7.4.23) (Ribose 1,5-bisphosphokinase) (EC 2.7.4.23; primary bucket kegg:ppu00030)
- pgi2: PP_4701 | Q88DW7 | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)
- tktA: PP_4965 | Q88D62 | Transketolase (EC 2.2.1.1) (EC 2.2.1.1; primary bucket kegg:ppu00710)
- fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11; primary bucket kegg:ppu00710)
- rpiA: PP_5150 | Q88CN0 | Ribose-5-phosphate isomerase A (EC 5.3.1.6) (Phosphoriboisomerase A) (PRI) (EC 5.3.1.6; primary bucket kegg:ppu00710)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)
- zwf: PP_5351 | Q88C32 | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) (EC 1.1.1.49; primary bucket kegg:ppu00480)

## Generic Module Context

### Working Scope

No module YAML was resolved; use the pathway and taxon context.

### Provisional Biological Outline

No module YAML outline available.

### Known Relationships Among Steps

No module YAML connections available.

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

# Module/Pathway/Taxon Review: Pentose Phosphate Pathway (ppu00030) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00030` — "Pentose phosphate pathway" (resolved local bucket with 19 primary genes; 36 candidate genes; module area central_carbon)
**Prepared for:** manual module satisfiability and gene-annotation curation

---

## 1. Executive Summary

The classical **pentose phosphate pathway (PPP)** is **fully satisfiable** in *Pseudomonas putida* KT2440. Every canonical step of both the oxidative branch (glucose-6-phosphate dehydrogenase, 6-phosphogluconolactonase, decarboxylating 6-phosphogluconate dehydrogenase) and the non-oxidative branch (ribose-5-phosphate isomerase, ribulose-5-phosphate 3-epimerase, transketolase, transaldolase), plus the PRPP entry point (ribose-phosphate pyrophosphokinase), is encoded in the genome with no reaction gaps. The satisfiability conclusion is **high-confidence at the pathway level** because pathway operation is supported by direct ¹³C metabolic flux analysis (¹³C-MFA) and in-vitro enzyme assays in KT2440, even though the individual gene assignments are only homology-inferred (UniProt protein-existence level 3).

The most important curation issue is **not** a gap but a **boundary/over-annotation problem**. The KEGG `ppu00030` bucket is over-broad: it bundles together three biochemically distinct processes — (i) the PPP proper, (ii) the **Entner-Doudoroff (ED) pathway**, and (iii) **peripheral periplasmic glucose/gluconate oxidation** — plus PRPP synthesis and several broadly-mapped isomerases/mutases. Of the 36 candidate genes, only ~10 encode PPP-proper enzymes (plus 2 for PRPP entry). The remaining ~15–24 candidates are ED enzymes (`edd`, `eda`), peripheral-oxidation enzymes (`gcd`, `gnuK`, `kguK`, gluconate-2-dehydrogenase subunits, `adhB`), gluconeogenic/EDEMP enzymes (`fba`, `fbp`), or likely over-propagated annotations from unrelated pathways (`trxB`, `ptxD`, `phnN`, `ttuD`, `rbsK`, `pgm`, `algC`, `cpsG`).

The key species-specific context is that **KT2440 lacks a functional Embden-Meyerhof-Parnas (EMP) pathway** (no phosphofructokinase) and catabolizes glucose almost exclusively through the ED route, operating a cyclic **EDEMP** architecture that recycles ~10% of triose phosphates back to hexose phosphates for NADPH overproduction. As a consequence, the oxidative PPP carries only **minor catabolic flux** and the non-oxidative branch is **flux-limited** (biosynthetic/anabolic role rather than a glycolytic conduit). Curation recommendation: mark all core PPP steps **covered**, keep ED as a **separate module**, and flag the peripheral-oxidation, PRPP, gluconeogenic, and redox genes as **not_expected_in_target_taxon as PPP steps / likely over-annotation**. The bucket itself should be marked **module_needs_revision**.

---

## 2. Target-Organism Pathway Definition

**What the PPP is (scope to keep):** The pentose phosphate pathway is the set of reactions that (a) oxidize glucose-6-phosphate (G6P) to ribulose-5-phosphate (Ru5P) with generation of NADPH and CO₂ (oxidative branch), and (b) interconvert pentose phosphates and other sugar phosphates (Ru5P ⇌ ribose-5-phosphate/xylulose-5-phosphate; C3–C7 sugar-phosphate shuffling by transketolase/transaldolase) to supply R5P for nucleotide biosynthesis and E4P for aromatic amino-acid biosynthesis, and to interface with glycolysis/gluconeogenesis at F6P and GAP (non-oxidative branch).

**Neighboring processes to keep separate (do NOT satisfy PPP steps with these):**

| Neighboring process | Genes co-mapped in ppu00030 | Correct home |
|---|---|---|
| **Entner-Doudoroff pathway** (6PG → KDPG → pyruvate + GAP) | `edd` (PP_1010), `eda` (PP_1024) | KEGG module M00008 / map ppu00030 co-display, but a distinct pathway |
| **Periplasmic glucose/gluconate oxidation** (glucose → gluconate → 2-ketogluconate) | `gcd` (PP_1444), `gnuK` (PP_3416), `kguK` (PP_3378), `PP_3382/3383/3384` (gluconate-2-DH), `adhB` (PP_3623), `ghrB` (PP_1261), `PP_1661` | Peripheral glucose catabolism (upstream feeder reactions) |
| **PRPP biosynthesis** | `prs` (PP_0722), `PP_2744`, `phnN` (PP_4469) | Nucleotide-precursor branch (M00005); `phnN` is phosphonate metabolism |
| **Gluconeogenesis / EDEMP recycling** | `fba` (PP_4960), `fbp` (PP_5040) | Glycolysis/gluconeogenesis (map ppu00010) |
| **Redox / other pathways** (likely over-propagation) | `trxB` (PP_0786), `ptxD` (PP_3376), `ttuD` (PP_4300), `rbsK` (PP_2458), `pgm`/`algC`/`cpsG` | Thioredoxin, phosphonate, hydroxypyruvate, ribose salvage, nucleotide-sugar/alginate |

**Alternate names / database definitions:** KEGG map ppu00030 explicitly notes that the map "also shows the Entner-Doudoroff pathway where 6-P-gluconate is dehydrated and then cleaved into pyruvate and glyceraldehyde-3P," which is why ED enzymes appear in the bucket. The PPP is decomposed by KEGG into modules **M00006** (oxidative phase, G6P→Ru5P), **M00007** (non-oxidative phase, F6P→R5P), and **M00005** (PRPP biosynthesis), and the map additionally co-displays **M00008** (Entner-Doudoroff) and **M00004** (PP cycle). Curators should treat "PPP" as M00006 + M00007 (+ optionally M00005 as an entry point), and explicitly exclude M00008.

---

## 3. Expected Step Model

The canonical PPP step model and its coverage status in KT2440:

```
OXIDATIVE BRANCH (M00006)
  G6P --[G6P dehydrogenase, EC 1.1.1.49]--> 6-phosphogluconolactone   [COVERED: zwf/zwfA/zwfB]
  6-PGL --[6-phosphogluconolactonase, EC 3.1.1.31]--> 6-phosphogluconate  [COVERED: pgl (+ppgL?)]
  6-PG --[6-PG dehydrogenase (decarb.), EC 1.1.1.44]--> Ru5P + CO2 + NADPH [COVERED: gntZ]

NON-OXIDATIVE BRANCH (M00007)
  Ru5P --[R5P isomerase A, EC 5.3.1.6]--> R5P                          [COVERED: rpiA]
  Ru5P --[Ru5P 3-epimerase, EC 5.1.3.1]--> Xu5P                        [COVERED: rpe]
  Xu5P + R5P --[transketolase, EC 2.2.1.1]--> S7P + GAP                 [COVERED: tktA]
  S7P + GAP --[transaldolase, EC 2.2.1.2]--> F6P + E4P                  [COVERED: tal, flux-limited]
  Xu5P + E4P --[transketolase, EC 2.2.1.1]--> F6P + GAP                 [COVERED: tktA]

PRPP ENTRY (M00005)
  R5P --[ribose-P pyrophosphokinase, EC 2.7.6.1]--> PRPP               [COVERED: prs (+PP_2744?)]

LINKER
  G6P <--[G6P isomerase, EC 5.3.1.9]--> F6P                            [COVERED: pgi1/pgi2]
```

**Every canonical step maps to at least one KO-assigned candidate gene, with no missing reaction.** The oxidative branch has paralog redundancy at the first step (three G6PD genes) and a single copy of the decarboxylating dehydrogenase (`gntZ`). The non-oxidative branch is single-copy at every step. KEGG module→gene links confirm exactly one gene per canonical non-oxidative step (M00007 = tktA, tal, rpe, rpiA), and place both `pgl` and the candidate second lactonase `ppgL` within the oxidative module M00006.

---

## 4. Candidate Genes and Evidence

### 4.1 PPP-proper core genes (high confidence — mark covered)

| Step (EC / KO) | Gene(s) | Locus | Evidence | Curation caveat |
|---|---|---|---|---|
| G6P dehydrogenase (1.1.1.49 / K00036) | **zwf, zwfA, zwfB** | PP_5351, PP_1022, PP_4042 | Homology (UniProt PE3); three real paralogs | Paralog redundancy; `zwf` primary. In *P. bharatica* CSV86, ZwfA is a dual cofactor-specific isozyme predominant in glucose metabolism ([PMID: 36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/)) — suggests functional differentiation worth checking in KT2440 |
| 6-phosphogluconolactonase (3.1.1.31 / K01057) | **pgl** | PP_1023 | Homology (PE3) | `ppgL` (PP_2021, K07404) is a candidate second lactonase — **candidate_uncertain**; annotation score 1/5, no recommended enzyme name |
| 6-PG dehydrogenase, decarboxylating (1.1.1.44 / K00033) | **gntZ** | PP_4043 | Homology (PE3); single copy | Low catabolic flux; `gntZ` deletion improves muconate production ([PMID: 31931111](https://pubmed.ncbi.nlm.nih.gov/31931111/)) — confirms it is a real, active branch |
| R5P isomerase A (5.3.1.6 / K01807) | **rpiA** | PP_5150 | Homology (PE3) | Single copy |
| Ru5P 3-epimerase (5.1.3.1 / K01783) | **rpe** | PP_0415 | Homology (PE3) | Local metadata assigns primary bucket ppu00040 (over-broad); functionally PPP |
| Transketolase (2.2.1.1 / K00615) | **tktA** | PP_4965 | Homology (PE3) | Single copy |
| Transaldolase (2.2.1.2 / K00616) | **tal** | PP_2168 | Homology (PE3) | **Flux-limited** — engineering studies implant exogenous transketolase/transaldolase to reinforce PPP ([PMID: 38531855](https://pubmed.ncbi.nlm.nih.gov/38531855/)) |
| PRPP synthase (2.7.6.1 / K00948) | **prs** | PP_0722 | Homology (PE3) | `PP_2744` is a paralog, **candidate_uncertain** (PE4 "Predicted," score 2, no gene symbol) |
| G6P/F6P isomerase (5.3.1.9 / K01810) | **pgi1, pgi2** | PP_1808, PP_4701 | Homology | Linker isomerase shared with glycolysis/gluconeogenesis |

### 4.2 Entner-Doudoroff genes (present in genome; keep as SEPARATE module)

`edd` (PP_1010, K01690, phosphogluconate dehydratase) and `eda` (PP_1024, K01625, KDPG aldolase) are the core ED enzymes. In KT2440 these carry the **dominant** glycolytic flux (the strain routes glucose to 6-phosphogluconate and cleaves it via Edd/Eda to pyruvate and glyceraldehyde-3-phosphate), but they are **not PPP steps** — they belong to KEGG module M00008 and should be curated under an ED module, not counted toward PPP satisfiability.

### 4.3 Peripheral glucose/gluconate oxidation (upstream feeders; not PPP)

`gcd` (K00117, quinoprotein glucose dehydrogenase), `gnuK` (K00851, gluconokinase), `kguK` (K11441, 2-ketogluconokinase), `PP_3382/3383/3384` (gluconate-2-dehydrogenase subunits, K06150/1/2), `adhB` (K06150), `ghrB` (K00090), and `PP_1661` (K19813) constitute the periplasmic oxidation network that converts glucose → gluconate → 2-ketogluconate before carbon enters central metabolism as 6-phosphogluconate. These are biochemically upstream feeder reactions, **not** PPP steps.

### 4.4 Likely over-propagated / other-pathway annotations (mark not_expected as PPP)

`trxB` (PP_0786, K22345, thioredoxin reductase — redox, not PPP), `ptxD` (PP_3376, phosphonate dehydrogenase), `phnN` (PP_4469, K05774, phosphonate metabolism), `ttuD` (PP_4300, hydroxypyruvate reductase), `rbsK` (PP_2458, ribokinase — ribose salvage), `pgm`/`algC`/`cpsG` (phosphoglucomutase/phosphomannomutase — nucleotide-sugar/alginate), `PP_3443` (gapN, K00131), and `fba`/`fbp` (gluconeogenesis/EDEMP). None of these should satisfy a canonical PPP step.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**No reaction gaps.** Every canonical PPP step has an assigned gene. The oxidative and non-oxidative branches, plus PRPP entry and the G6P/F6P linker, are all covered.

**Key ambiguities:**

1. **Zwf paralog assignment.** Three G6PD paralogs (`zwf`, `zwfA`, `zwfB`) is unusual. Which one carries oxidative-PPP flux vs. ED-feeding flux vs. oxidative-stress response is not resolved by homology alone. The *P. bharatica* CSV86 finding that ZwfA is a dual-cofactor (NAD⁺/NADP⁺) predominant isozyme ([PMID: 36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/)) is suggestive but is **weak-to-moderate species transfer** (different *Pseudomonas* species).

2. **`ppgL` (PP_2021) as second lactonase.** UniProt annotation score 1/5, no recommended enzyme name → **candidate_uncertain**. Do not count as a required step (pgl already covers it). KEGG places it in oxidative module M00006, so it is plausibly a genuine second lactonase but needs confirmation.

3. **`PP_2744` as second PRPP synthase.** UniProt PE4 "Predicted," no gene symbol → **candidate_uncertain**.

4. **Evidence-level mismatch.** All core PPP gene annotations are **homology-inferred** (UniProt PE3), whereas pathway operation is **experimentally proven** by ¹³C-MFA and enzyme assays. Satisfiability is therefore strong at the pathway level but individual gene-to-function mappings remain inferential.

**Over-annotation summary:** ~15 of the 36 candidates (ED, peripheral oxidation, PRPP, gluconeogenesis, redox) are not PPP-proper. The bucket bundles ≥3 distinct processes; this is the dominant curation problem.

---

## 6. Module and GO-Curation Recommendations

**Per-step status:**

| Canonical step | Status | Gene(s) |
|---|---|---|
| G6P dehydrogenase | **covered** | zwf (primary); zwfA, zwfB (paralogs) |
| 6-P-gluconolactonase | **covered** | pgl; ppgL = candidate_uncertain |
| 6-P-gluconate DH (decarb.) | **covered** | gntZ (single copy) |
| R5P isomerase A | **covered** | rpiA |
| Ru5P 3-epimerase | **covered** | rpe |
| Transketolase | **covered** | tktA |
| Transaldolase | **covered** (flag flux-limited) | tal |
| PRPP synthase | **covered** | prs; PP_2744 = candidate_uncertain |
| G6P/F6P isomerase (linker) | **covered** | pgi1, pgi2 |
| Entner-Doudoroff (edd/eda) | **separate module** (present, not a PPP step) | edd, eda |
| Peripheral oxidation, PRPP-phosphonate, redox, gluconeogenesis | **not_expected_in_target_taxon as PPP steps / over-annotation** | gcd, gnuK, kguK, PP_3382-3384, adhB, ghrB, PP_1661, trxB, ptxD, phnN, ttuD, rbsK, pgm, algC, cpsG, fba, fbp, PP_3443 |

**Bucket-level recommendation:** mark `kegg:ppu00030` **module_needs_revision** — the generic KEGG boundary is wrong for curation purposes because it co-mingles PPP, ED, and peripheral oxidation. Recommend splitting into: (a) oxidative + non-oxidative PPP (M00006 + M00007), (b) a distinct ED module (M00008), and (c) a peripheral periplasmic glucose-oxidation module. No new GO terms appear necessary; standard PPP GO terms suffice, but the gene-to-term mappings for the ~15 over-annotated genes should be down-weighted or removed from the PPP context.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **zwf / zwfA / zwfB (PP_5351 / PP_1022 / PP_4042)** — resolve paralog roles (oxidative PPP vs. ED-feeding vs. stress); cofactor specificity.
2. **ppgL (PP_2021)** — very low annotation confidence (score 1/5); confirm or reject as second 6-P-gluconolactonase.
3. **PP_2744** — "Predicted" second PRPP synthase; confirm functionality vs. `prs`.
4. **gntZ (PP_4043)** — single-copy decarboxylating dehydrogenase; deletion phenotype documented in muconate engineering; confirm it is the sole 6PGDH.
5. **tal (PP_2168)** — flux-limiting transaldolase flagged by pentose-engineering studies; verify it is the only transaldolase.

---

## 8. Mechanistic Model / Interpretation

KT2440's central-carbon architecture reframes what "PPP satisfiability" means for this organism. Because the strain **lacks phosphofructokinase**, linear EMP glycolysis is nonfunctional, and glucose is instead funneled — largely through periplasmic oxidation to gluconate/2-ketogluconate — into **6-phosphogluconate**, which is then cleaved by the **Entner-Doudoroff** enzymes Edd/Eda to pyruvate and GAP:

```
                periplasm                          cytoplasm
  glucose --gcd--> gluconate --gnuK--> 6-P-gluconate --edd--> KDPG --eda--> pyruvate + GAP
     |                 |                    ^                                    |
     |         (2-KG via gluconate-2-DH, kguK)                                  | (EDEMP recycle ~10%)
     |                                      |                                   v
     +--gts--> G6P <--pgi--> F6P <----------+------------ hexose-P <--- triose-P (gluconeogenic EMP)
                 |                                              ^
              (oxidative PPP: minor flux)                       |
               zwf -> pgl -> gntZ -> Ru5P --rpe/rpiA--> Xu5P/R5P|
                                        |                       |
                          (non-oxidative PPP: tktA/tal) --------+
```

In this **EDEMP cycle**, ~10% of triose phosphates are recycled back to hexose phosphates by a merged set of ED, gluconeogenic-EMP, and PPP reactions, tuned to overproduce NADPH. Consequently:

- The **oxidative PPP** (zwf→pgl→gntZ) is present and active but carries **minor catabolic flux**; its main role is NADPH supply, not glucose disposal.
- The **non-oxidative PPP** (rpe/rpiA/tktA/tal) functions primarily in an **anabolic/biosynthetic** direction (R5P for nucleotides, E4P for aromatics) and is **flux-limited** — engineering efforts must reinforce transketolase/transaldolase to route pentoses efficiently.
- The **ED pathway** is the true glycolytic workhorse and must be curated as a separate entity, even though KEGG co-displays it on the PPP map.

This is why the correct curation stance is "PPP fully present, but the bucket is over-broad and the pathway is flux-minor" rather than "PPP is the main glucose route."

---

## 9. Evidence Base

| PMID | Paper | Role in this review |
|---|---|---|
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | *P. putida KT2440 metabolizes glucose through a cycle formed by enzymes of the ED, EMP, and PPP pathways* (Nikel et al. 2015) | **Primary direct evidence.** ¹³C-MFA + enzyme assays establish ED dominance, absent functional EMP, and the EDEMP cycle recycling ~10% of triose-P; documents oxidative/non-oxidative PPP operation |
| [17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/) | *Convergent peripheral pathways catalyze initial glucose catabolism in P. putida* (del Castillo et al. 2007) | Confirms three convergent peripheral pathways converging on 6-phosphogluconate, metabolized by Edd/Eda |
| [18245293](https://pubmed.ncbi.nlm.nih.gov/18245293/) | *A set of activators and repressors control peripheral glucose pathways in P. putida* | Regulatory architecture (HexR, GnuR, PtxS, GltR-2) of peripheral oxidation and ED genes — supports separating these from PPP |
| [18493743](https://pubmed.ncbi.nlm.nih.gov/18493743/) | *Physiological states and energetic adaptation of P. putida mt-2 on glucose* | Glucose → gluconate → 2-ketogluconate flux; periplasmic oxidation dominates over biosynthesis |
| [31931111](https://pubmed.ncbi.nlm.nih.gov/31931111/) | *Engineering glucose metabolism for enhanced muconic acid production in P. putida KT2440* | `gcd`, `gntZ`, `hexR` deletions reshape flux — confirms `gntZ` and peripheral-oxidation genes are real and active |
| [38531855](https://pubmed.ncbi.nlm.nih.gov/38531855/) | *Synthetically-primed adaptation of P. putida to D-xylose* | Implanting exogenous transketolase/transaldolase to reinforce PPP — supports "covered but flux-limited" for `tal`/`tktA` |
| [36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/) | *ZwfA, a dual cofactor-specific isozyme, in P. bharatica CSV86* | Suggests G6PD paralog functional differentiation; weak-to-moderate species transfer to KT2440 |
| [41141486](https://pubmed.ncbi.nlm.nih.gov/41141486/) | *Engineering mixed sugar metabolic channels* | Context on pentose (xylose/arabinose) utilization and PPP interfacing |
| [30831266](https://pubmed.ncbi.nlm.nih.gov/30831266/) | *GC-MS-based analysis of Pseudomonas* | Methodological / genus context |

**Verified supporting quotes (from stored abstracts):**

- [PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/): *"The soil bacterium Pseudomonas putida KT2440 lacks a functional Embden-Meyerhof-Parnas (EMP) pathway, and glycolysis is known to proceed almost exclusively through the Entner-Doudoroff (ED) route."* — establishes ED dominance and absent functional EMP.
- [PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/): *"about 10% of the triose phosphates were found to be recycled back to form hexose phosphates. This set of reactions merges activities belonging to the ED, the EMP (operating in a gluconeogenic fashion), and the pentose phosphate pathways to form an unforeseen metabolic architecture (EDEMP cycle)"* — defines the EDEMP cycle intertwining PPP with ED and EMP.
- [PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/): *"glucose catabolism in Pseudomonas putida occurs through the simultaneous operation of three pathways that converge at the level of 6-phosphogluconate, which is metabolized by the Edd and Eda Entner/Doudoroff enzymes to central metabolites"* — confirms convergence on 6-phosphogluconate and ED exit.
- [PMID: 38531855](https://pubmed.ncbi.nlm.nih.gov/38531855/): *"We then enhance the pentose phosphate pathway by implanting exogenous transketolase and transaldolase..."* — supports native non-oxidative PPP being flux-limited.

---

## 10. Limitations and Knowledge Gaps

- **Gene-level annotations are homology-inferred.** All core PPP genes are UniProt protein-existence level 3 ("Inferred from homology"); `PP_2744` is level 4 ("Predicted") and `ppgL` has a 1/5 annotation score. Direct biochemical characterization of most individual KT2440 PPP enzymes is lacking — the strong evidence is at the **pathway** (flux) level, not the **gene** level.
- **Paralog roles unresolved.** The functional division of labor among the three `zwf` paralogs is not established from these data.
- **Second-copy uncertainty.** Whether `ppgL` and `PP_2744` are genuine functional second copies or spurious annotations is unresolved.
- **Species transfer.** The ZwfA cofactor-specificity insight comes from *P. bharatica*, not KT2440 — transfer is uncertain.
- **KEGG boundary artifact.** The `ppu00030` bucket's over-breadth is a database-definition artifact (KEGG deliberately co-displays ED on the PPP map); this is a curation-tooling issue, not a biological gap.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Promote to full `fetch-gene` review:** `zwf`/`zwfA`/`zwfB`, `ppgL`, `PP_2744`, `gntZ`, `tal` (see Section 7).
2. **Split the bucket:** Create/curate three distinct modules — oxidative+non-oxidative PPP (M00006+M00007), Entner-Doudoroff (M00008), and peripheral periplasmic glucose oxidation — replacing the monolithic `ppu00030` mapping. Mark `kegg:ppu00030` **module_needs_revision**.
3. **Down-weight over-annotations:** Remove or flag PPP-context GO/EC mappings for `trxB`, `ptxD`, `phnN`, `ttuD`, `rbsK`, `pgm`, `algC`, `cpsG`, `fba`, `fbp`, `PP_3443`.
4. **Experimental resolution (expert questions):** (a) Single- and combinatorial `zwf` paralog knockouts with ¹³C-MFA to assign each paralog's flux role and cofactor preference; (b) enzymatic confirmation of `ppgL` lactonase activity and `PP_2744` PRPP-synthase activity; (c) transaldolase/transketolase activity assays to quantify the flux limitation flagged by xylose-engineering studies.
5. **Verify single-copy assumptions:** Confirm `gntZ`, `rpiA`, `rpe`, `tktA`, `tal` are the sole genes for their reactions via genome-wide EC/KO scan.

---

*Prepared as a species-aware module satisfiability and annotation-curation review. Satisfiability conclusions are high-confidence at the pathway level (direct ¹³C-MFA in KT2440) and moderate at the individual-gene level (homology-inferred). The dominant curation action is bucket revision, not gap-filling.*


## Artifacts

- [OpenScientist final report](PSEPK__pentose_phosphate_pathway__ppu00030-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__pentose_phosphate_pathway__ppu00030-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:36354357
2. PMID:31931111
3. PMID:38531855
4. PMID:26350459
5. PMID:17483213