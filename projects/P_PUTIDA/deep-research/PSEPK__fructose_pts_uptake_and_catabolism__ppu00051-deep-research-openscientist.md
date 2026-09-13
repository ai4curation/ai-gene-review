---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T14:17:08.980272'
end_time: '2026-07-25T14:39:57.208448'
duration_seconds: 1368.23
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial fructose PTS uptake and entry into central carbon catabolism
  module_summary: A reusable two-part bacterial module in which a fructose-specific
    phosphoenolpyruvate-dependent phosphotransferase system imports fructose while
    converting it to fructose 1-phosphate, and 1-phosphofructokinase then converts
    fructose 1-phosphate to fructose 1,6-bisphosphate. The module stops at fructose
    1,6-bisphosphate. Downstream central-carbon reactions, PTS regulatory cross-talk,
    transcriptional control by Cra/FruR, and pathways for other hexoses are outside
    the boundary.
  module_outline: "- Bacterial fructose PTS uptake and entry into central carbon catabolism\n\
    \  - 1. fructose import coupled to fructose 1-phosphate formation\n  - Fructose-specific\
    \ PTS import and phosphorylation\n    - PEP-dependent fructose PTS phosphorelay\
    \ (molecular player: PEP-utilizing fructose PTS relay proteins; activity or role:\
    \ phosphoenolpyruvate-protein phosphotransferase activity)\n    - Fructose-specific\
    \ EIIB-EIIC transport and phosphorylation (molecular player: fructose-specific\
    \ PTS EIIB-EIIC proteins; activity or role: protein-N(PI)-phosphohistidine-fructose\
    \ phosphotransferase system transporter activity)\n  - 2. fructose 1-phosphate\
    \ conversion to fructose 1,6-bisphosphate\n  - FruK-dependent fructose 1-phosphate\
    \ phosphorylation\n    - 1-phosphofructokinase (molecular player: 1-phosphofructokinase\
    \ family; activity or role: 1-phosphofructokinase activity)"
  module_connections: '- Fructose-specific PTS import and phosphorylation feeds into
    FruK-dependent fructose 1-phosphate phosphorylation: The fructose PTS supplies
    intracellular fructose 1-phosphate to FruK.'
  pathway_query: ppu00051
  pathway_id: ppu00051
  pathway_name: Fructose and mannose metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00051 with 8 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '18'
  candidate_genes: '- fruK: PP_0794 | Q88PQ4 | Phosphofructokinase (primary bucket
    kegg:ppu02060)

    - fruA: PP_0795 | Q88PQ3 | protein-N(pi)-phosphohistidine--D-fructose phosphotransferase
    (EC 2.7.1.202) (EC 2.7.1.202; primary bucket kegg:ppu02060)

    - algA: PP_1277 | Q88ND5 | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate
    isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate
    guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP)
    (GTP--mannose-1-phosphate guanylyltransferase)] (EC 2.7.7.13; 5.3.1.8; primary
    bucket kegg:ppu00051)

    - algL: PP_1281 | Q88ND1 | Alginate lyase (EC 4.2.2.3) (Poly(beta-D-mannuronate)
    lyase) (EC 4.2.2.3; primary bucket kegg:ppu00051)

    - algG: PP_1283 | Q88NC9 | Mannuronan C5-epimerase (EC 5.1.3.37) (Poly(beta-D-mannuronate)
    C5 epimerase) (EC 5.1.3.37; primary bucket kegg:ppu00051)

    - alg44: PP_1286 | Q88NC6 | Alginate biosynthesis protein Alg44 (primary bucket
    kegg:ppu00543)

    - alg8: PP_1287 | Q88NC5 | Glycosyltransferase alg8 (EC 2.4.-.-) (EC 2.4.-.-;
    primary bucket kegg:ppu00543)

    - algD: PP_1288 | Q88NC4 | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) (EC
    1.1.1.132; primary bucket kegg:ppu00051)

    - PP_1776: PP_1776 | Q88M00 | Alginate biosynthesis protein AlgA (EC 2.7.7.13)
    (EC 5.3.1.8) (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - gmd: PP_1799 | Q88LX8 | GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose
    dehydratase) (EC 4.2.1.47; primary bucket kegg:ppu00051)

    - rmd: PP_1800 | Q88LX7 | Oxidoreductase Rmd (primary bucket kegg:ppu00051)

    - PP_2037: PP_2037 | Q88L98 | Aldolase (primary bucket kegg:ppu00040)

    - fucD: PP_2831 | Q88J18 | L-fuconate dehydratase (EC 4.2.1.68) (EC 4.2.1.68;
    primary bucket kegg:ppu00051)

    - tpiA: PP_4715 | Q88DV4 | Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1)
    (Triose-phosphate isomerase) (EC 5.3.1.1; primary bucket kegg:ppu00562)

    - fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC
    4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)

    - fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1)
    (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11;
    primary bucket kegg:ppu00710)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
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
  path: PSEPK__fructose_pts_uptake_and_catabolism__ppu00051-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__fructose_pts_uptake_and_catabolism__ppu00051-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial fructose PTS uptake and entry into central carbon catabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00051
- Resolved ID: ppu00051
- Resolved name: Fructose and mannose metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00051 with 8 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 18

- fruK: PP_0794 | Q88PQ4 | Phosphofructokinase (primary bucket kegg:ppu02060)
- fruA: PP_0795 | Q88PQ3 | protein-N(pi)-phosphohistidine--D-fructose phosphotransferase (EC 2.7.1.202) (EC 2.7.1.202; primary bucket kegg:ppu02060)
- algA: PP_1277 | Q88ND5 | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP) (GTP--mannose-1-phosphate guanylyltransferase)] (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- algL: PP_1281 | Q88ND1 | Alginate lyase (EC 4.2.2.3) (Poly(beta-D-mannuronate) lyase) (EC 4.2.2.3; primary bucket kegg:ppu00051)
- algG: PP_1283 | Q88NC9 | Mannuronan C5-epimerase (EC 5.1.3.37) (Poly(beta-D-mannuronate) C5 epimerase) (EC 5.1.3.37; primary bucket kegg:ppu00051)
- alg44: PP_1286 | Q88NC6 | Alginate biosynthesis protein Alg44 (primary bucket kegg:ppu00543)
- alg8: PP_1287 | Q88NC5 | Glycosyltransferase alg8 (EC 2.4.-.-) (EC 2.4.-.-; primary bucket kegg:ppu00543)
- algD: PP_1288 | Q88NC4 | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) (EC 1.1.1.132; primary bucket kegg:ppu00051)
- PP_1776: PP_1776 | Q88M00 | Alginate biosynthesis protein AlgA (EC 2.7.7.13) (EC 5.3.1.8) (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- gmd: PP_1799 | Q88LX8 | GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose dehydratase) (EC 4.2.1.47; primary bucket kegg:ppu00051)
- rmd: PP_1800 | Q88LX7 | Oxidoreductase Rmd (primary bucket kegg:ppu00051)
- PP_2037: PP_2037 | Q88L98 | Aldolase (primary bucket kegg:ppu00040)
- fucD: PP_2831 | Q88J18 | L-fuconate dehydratase (EC 4.2.1.68) (EC 4.2.1.68; primary bucket kegg:ppu00051)
- tpiA: PP_4715 | Q88DV4 | Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1) (Triose-phosphate isomerase) (EC 5.3.1.1; primary bucket kegg:ppu00562)
- fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)
- fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11; primary bucket kegg:ppu00710)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

## Generic Module Context

### Working Scope

A reusable two-part bacterial module in which a fructose-specific phosphoenolpyruvate-dependent phosphotransferase system imports fructose while converting it to fructose 1-phosphate, and 1-phosphofructokinase then converts fructose 1-phosphate to fructose 1,6-bisphosphate. The module stops at fructose 1,6-bisphosphate. Downstream central-carbon reactions, PTS regulatory cross-talk, transcriptional control by Cra/FruR, and pathways for other hexoses are outside the boundary.

### Provisional Biological Outline

- Bacterial fructose PTS uptake and entry into central carbon catabolism
  - 1. fructose import coupled to fructose 1-phosphate formation
  - Fructose-specific PTS import and phosphorylation
    - PEP-dependent fructose PTS phosphorelay (molecular player: PEP-utilizing fructose PTS relay proteins; activity or role: phosphoenolpyruvate-protein phosphotransferase activity)
    - Fructose-specific EIIB-EIIC transport and phosphorylation (molecular player: fructose-specific PTS EIIB-EIIC proteins; activity or role: protein-N(PI)-phosphohistidine-fructose phosphotransferase system transporter activity)
  - 2. fructose 1-phosphate conversion to fructose 1,6-bisphosphate
  - FruK-dependent fructose 1-phosphate phosphorylation
    - 1-phosphofructokinase (molecular player: 1-phosphofructokinase family; activity or role: 1-phosphofructokinase activity)

### Known Relationships Among Steps

- Fructose-specific PTS import and phosphorylation feeds into FruK-dependent fructose 1-phosphate phosphorylation: The fructose PTS supplies intracellular fructose 1-phosphate to FruK.

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

# Species-Aware Module Review: Fructose PTS Uptake and Entry into Central Carbon Catabolism in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module:** Fructose-specific PEP-PTS import (→ fructose-1-phosphate) + 1-phosphofructokinase (F1P → fructose-1,6-bisphosphate). Boundary ends at fructose-1,6-bisphosphate (FBP).
**Seed bucket:** KEGG ppu00051 "Fructose and mannose metabolism" (18 candidate genes)

---

## 1. Executive summary

The generic "bacterial fructose PTS uptake → F1P → FBP" module is **fully satisfiable in *P. putida* KT2440** and maps cleanly and unambiguously to a single, experimentally characterized operon, **fruBKA** (`PP_0793`–`PP_0794`–`PP_0795`). All three module activities are encoded with matching EC/GO annotations, supported by direct KT2440 experimental work.

The single most important curation issue is a **metadata gap, not a biological gap**: the phosphorelay gene **`fruB` (PP_0793, UniProt Q88PQ5)** is **absent from the 18-gene candidate list**. This is an artifact of seeding candidates from KEGG pathway **ppu00051**, whereas KEGG places `fruB` only on the PTS map **ppu02060**. `fruB` should be added and promoted to full review.

Conversely, **15 of the 18 candidate genes are over-propagated** into this module. They are legitimate members of the broad KEGG "Fructose and mannose metabolism" map (alginate biosynthesis, the GDP-mannose branch, fucose catabolism, and gluconeogenesis/triose enzymes) but lie **outside** the fructose-PTS→F1P→FBP boundary. Only `fruA` and `fruK` from the candidate list are true module members; `fba` and `fbp` are downstream-adjacent context.

---

## 2. Target-organism pathway definition

**Included process (KT2440-specific):** PEP-dependent phosphoryl relay through a fused multiphosphoryl-transfer protein (EI–HPr–EIIA^Fru = FruB), transfer to the membrane EIIBC^Fru permease (FruA) which imports extracellular fructose and phosphorylates it on import to **fructose-1-phosphate (F1P)**, followed by ATP-dependent phosphorylation of F1P to **fructose-1,6-bisphosphate (FBP)** by 1-phosphofructokinase (FruK). The module ends at FBP.

**Key species-specific facts:**
- KT2440 has **only two PTS branches**: a *complete* fructose-specific PTS (PTS^Fru = FruBKA) and the sugar-unrelated nitrogen PTS^Ntr (PtsP/PtsO/PtsN). Fructose is the **only** sugar taken up by a PTS in this organism (Chavarría et al. 2012, PMID 22434849).
- **Glucose is NOT PTS-transported** in KT2440; it enters via porins/ABC transport and three convergent peripheral routes converging at 6-phosphogluconate, feeding the **Entner–Doudoroff (Edd/Eda)** pathway (del Castillo et al. 2007, PMID 17483213).
- Downstream of the module endpoint, KT2440 **lacks 6-phosphofructokinase (Pfk)** — confirmed by KEGG: neither K00850 (ATP-dependent 6-PFK, EC 2.7.1.11) nor K00895 (PPi-dependent PFK) is encoded in `ppu`; the only phosphofructokinase-type gene is K00882 = `fruK`/PP_0794 (1-PFK, EC 2.7.1.56). Net glycolytic (EMP) flux from F6P→FBP therefore does not occur. Fructose-derived FBP is instead routed via FBP aldolase (Fba) to trioses and/or recycled to F6P by fructose-1,6-bisphosphatase (Fbp) to enter the ED pathway — the "EDEMP cycle." This is **outside** the module boundary but explains why `fbp` is physiologically essential for fructose catabolism here.
- **Operon context (KEGG-confirmed gene order):** `PP_0792 cra` → `PP_0793 fruB` → `PP_0794 fruK` → `PP_0795 fruA` → `PP_0796` (unknown). The Cra/FruR regulator is immediately upstream of the fruBKA operon, consistent with F1P-dependent operon-level regulation (regulation itself is outside the module boundary).

**Neighboring pathways/maps to keep separate:** ppu02060 (PTS map — where `fruB` lives), ppu00010/ppu00030 (glycolysis/ED/PPP downstream of FBP), ppu00520/ppu00051 mannose & GDP-mannose branch, ppu00543/ppu00040 alginate & fucose. **Alternate names:** PTS^Fru / PTSFru / fructose PTS; the operon is also cited as *fruBKA*; FruB is variously called MTP (multiphosphoryl transfer protein), FPr, or DTP.

---

## 3. Expected step model (generic → KT2440)

| # | Generic module step | Activity (GO/EC) | KT2440 gene | Status |
|---|---------------------|------------------|-------------|--------|
| 1a | PEP-dependent fructose PTS phosphorelay (EI/HPr/EIIA) | PEP–protein phosphotransferase, EC 2.7.3.9; GO:0009401 | **fruB / PP_0793 / Q88PQ5** | **covered** (but missing from metadata) |
| 1b | Fructose-specific EIIB-EIIC transport + phosphorylation → F1P | fructose PTS EIIBC transporter, EC 2.7.1.202; GO:0022877 | **fruA / PP_0795 / Q88PQ3** | covered |
| 2 | 1-phosphofructokinase: F1P → FBP | 1-phosphofructokinase, EC 2.7.1.56; GO:0008662 | **fruK / PP_0794 / Q88PQ4** | covered |

All three steps are **covered**. No step is a gap or "not expected." The known step relationship (PTS supplies F1P to FruK) holds and is reinforced by regulation: F1P is the sole physiological effector of the Cra/FruR repressor of the fruBKA operon (Chavarría et al. 2014, PMID 24918052) — regulatory detail that lies just outside the module boundary but confirms the operon logic.

---

## 4. Candidate genes and evidence

### 4.1 True module genes (high confidence)

- **fruA — PP_0795 (Q88PQ3).** Fructose PTS EIIBC permease, EC 2.7.1.202, 580 aa (fused EIIB+EIIC). GO:0022877 (fructose PTS transporter activity), GO:0009401 (PTS). Direct KT2440 evidence: member of experimentally studied fruBKA operon (PMID 22434849, 24918052). **Role:** step 1b (import + phosphorylation to F1P). *Caveat:* candidate metadata bucket shown as ppu02060, correct; EC is specific, no over-mapping.
- **fruK — PP_0794 (Q88PQ4).** 1-phosphofructokinase, KEGG K00882, EC 2.7.1.56, 315 aa. GO:0008662 (1-phosphofructokinase activity) + ATP binding. **Role:** step 2 (F1P→FBP). *Caveat:* candidate metadata labels it generically "Phosphofructokinase" — this is **not** 6-phosphofructokinase (EC 2.7.1.11); the name should be curated to "1-phosphofructokinase" to avoid conflation with the (absent) Pfk.
- **fruB — PP_0793 (Q88PQ5). MISSING FROM CANDIDATE LIST.** Multiphosphoryl transfer protein (EI–HPr–EIIA^Fru), EC 2.7.3.9 (also EC 2.7.1.202 via KEGG K23993), 950 aa (multidomain, consistent with a fused relay). **Role:** step 1a (PEP phosphorelay). First gene of the fruBKA operon; contiguous UniProt accession (Q88PQ5) with fruK/fruA. Omitted only because it is annotated to ppu02060, not the ppu00051 seed bucket.

### 4.2 Over-propagated candidates (outside module boundary)

These are correctly annotated to their own functions but do **not** belong to the fructose-PTS module:

- **GDP-mannose / mannose branch:** `algA` (PP_1277), `PP_1776`, `cpsG` (PP_1777), `algC` (PP_5288), `gmd` (PP_1799), `rmd` (PP_1800) — mannose-6-P isomerase / GDP-mannose pyrophosphorylase / phosphomannomutase / GDP-mannose dehydratase. Function in GDP-mannose and cell-envelope sugar-nucleotide metabolism.
- **Alginate biosynthesis:** `algL` (PP_1281), `algG` (PP_1283), `alg44` (PP_1286), `alg8` (PP_1287), `algD` (PP_1288) — alginate polymerization/modification (largely cryptic under standard conditions in KT2440).
- **Other sugar catabolism:** `fucD` (PP_2831, L-fuconate dehydratase), `PP_2037` (aldolase, ppu00040).
- **Downstream-adjacent (FBP fate), still outside boundary:** `fba` (PP_4960, FBP aldolase EC 4.1.2.13) cleaves the module product FBP; `fbp` (PP_5040, FBPase EC 3.1.3.11) recycles FBP→F6P (essential for fructose→ED flux given Pfk absence); `tpiA` (PP_4715, triose-P isomerase) acts on triose products. These provide biological context but should not be counted as module members.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Metadata gap (highest priority):** `fruB`/PP_0793 is missing. Not a biological gap — the step is covered. Root cause: bucket seeded from ppu00051 while fruB maps to ppu02060.
- **Naming ambiguity:** `fruK`/PP_0794 carries the generic label "Phosphofructokinase," which risks conflation with 6-phosphofructokinase (Pfk, EC 2.7.1.11). KT2440 **lacks** a functional 6-PFK; the only F1P kinase is FruK (EC 2.7.1.56). Curate the name/EC explicitly.
- **Broad EC/GO on non-module genes:** `algA`/`PP_1776` carry dual EC (2.7.7.13 + 5.3.1.8) and `algC` dual PMM/PGM activity — legitimate but irrelevant to this module; they are pathway-map over-propagation, not per-gene errors.
- **No lineage-specific replacement needed:** unlike some bacteria that split EI/HPr/EIIA into separate genes, KT2440 uses a single fused FruB — this is captured correctly by the 950-aa multidomain protein.

---

## 6. Module and GO-curation recommendations

| Module step | Recommended mark | Rationale |
|-------------|------------------|-----------|
| 1a PEP phosphorelay (fruB) | **covered** | fruB/PP_0793 present with EC 2.7.3.9; add to gene set |
| 1b EIIBC transport → F1P (fruA) | **covered** | fruA/PP_0795, EC 2.7.1.202, direct evidence |
| 2 1-PFK: F1P→FBP (fruK) | **covered** | fruK/PP_0794, EC 2.7.1.56, GO:0008662 |

- **Module status: covered / satisfiable.** No `gap`, `candidate_uncertain`, or `not_expected_in_target_taxon` calls are warranted for the three steps.
- **module_needs_revision (metadata only):** add `fruB`/PP_0793/Q88PQ5 to the module gene set; the generic module boundary itself is **correct** for KT2440.
- **Bucket caveat for curators:** do not treat KEGG ppu00051 membership as module membership — 15/18 candidates are out-of-scope map neighbors. Prefer KEGG modules/orthology (K23993, K02770, K00882) or the fruBKA operon as the seed for this module.
- **GO requests:** none needed — existing terms suffice (GO:0009401 PTS; GO:0022877 fructose PTS transporter activity; GO:0008662 1-phosphofructokinase activity; EC 2.7.3.9 for FruB). Recommend ensuring FruB carries a PEP–protein phosphotransferase / PTS term in the target proteome.

---

## 7. Genes to promote to full `fetch-gene` review

1. **fruB / PP_0793 / Q88PQ5** — *highest priority*; currently missing; confirm EI-HPr-EIIA^Fru domain architecture and PTS relay role.
2. **fruK / PP_0794 / Q88PQ4** — confirm/curate name to 1-phosphofructokinase (EC 2.7.1.56); disambiguate from absent 6-PFK.
3. **fruA / PP_0795 / Q88PQ3** — confirm EIIBC fructose permease; verify F1P (not F6P) product specificity.

(Context-only, not module members: `fbp`/PP_5040 and `fba`/PP_4960 warrant a note re: EDEMP downstream fate but need not be promoted for this module.)

---

## 8. Evidence and open questions

**Direct KT2440 experimental support:**
- Complete fructose PTS (PTS^Fru) and glucose-independent-of-PTS transport: Chavarría et al. 2012, *mBio* (PMID 22434849).
- fruBKA operon identity and F1P as sole Cra/FruR effector: Chavarría et al. 2014, *Environ Microbiol* (PMID 24918052).
- ED-based downstream sugar catabolism, glucose peripheral pathways: del Castillo et al. 2007, *Environ Microbiol* (PMID 17483213).

**Inferred (homology/database):** exact FruB domain boundaries and F1P product specificity of FruA are assigned from KEGG orthology (K23993/K02770) and UniProt EC/GO; these are strong (fused-domain length and operon context are consistent) but not individually enzymatically re-verified in KT2440.

**Open questions / resolving experiments:**
- Direct biochemical confirmation that FruA delivers fructose as F1P (vs F6P) in KT2440 (in vitro PTS assay).
- Whether any secondary fructose uptake route operates in a ΔfruBKA background (growth/transport assay) — literature implies none.
- Confirm FruK is strictly a 1-phosphofructokinase and cannot substitute for the missing 6-PFK.

---

## Key references
- Chavarría M, Kleijn RJ, Sauer U, Pflüger-Grau K, de Lorenzo V. Regulatory tasks of the PEP-PTS of *Pseudomonas putida* in central carbon metabolism. *mBio* 2012. **PMID 22434849**.
- Chavarría M, Durante-Rodríguez G, Krell T, et al. Fructose 1-phosphate is the one and only physiological effector of the Cra (FruR) regulator of *Pseudomonas putida*. *Environ Microbiol* 2014. **PMID 24918052**.
- del Castillo T, Ramos JL, Rodríguez-Herva JJ, Fuhrer T, Sauer U, Duque E. Convergent peripheral pathways catalyze initial glucose catabolism in *Pseudomonas putida*. *J Bacteriol* 2007. **PMID 17483213**.
- KEGG entries ppu:PP_0793 (K23993), ppu:PP_0794 (K00882), ppu:PP_0795 (K02770); UniProt Q88PQ5, Q88PQ4, Q88PQ3 (queried 2026).


## Artifacts

- [OpenScientist final report](PSEPK__fructose_pts_uptake_and_catabolism__ppu00051-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__fructose_pts_uptake_and_catabolism__ppu00051-deep-research-openscientist_artifacts/final_report.pdf)