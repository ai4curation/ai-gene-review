---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T05:26:43.354145'
end_time: '2026-07-15T05:44:08.590371'
duration_seconds: 1045.24
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial thiamine diphosphate biosynthesis
  module_summary: 'Species-neutral bacterial pathway for de novo synthesis of thiamine
    diphosphate (ThDP), the active thiamine cofactor. The pathway has two converging
    branches: a hydroxymethylpyrimidine branch in which ThiC converts an AIR-derived
    precursor to HMP phosphate and ThiD phosphorylates it to the diphosphate, and
    a thiazole branch in which Dxs, ThiO, sulfur-relay proteins, and ThiG form the
    thiazole phosphate moiety. ThiE couples the pyrimidine and thiazole moieties to
    thiamine phosphate, and ThiL phosphorylates thiamine phosphate to ThDP.'
  module_outline: "- Thiamine diphosphate biosynthesis\n  - 1. hydroxymethylpyrimidine\
    \ branch\n  - Hydroxymethylpyrimidine diphosphate branch\n    - 1. HMP phosphate\
    \ formation\n    - AIR-derived precursor to HMP phosphate\n      - ThiC: phosphomethylpyrimidine\
    \ synthase (molecular player: ThiC phosphomethylpyrimidine synthase family; activity\
    \ or role: phosphomethylpyrimidine synthase activity)\n    - 2. HMP phosphate\
    \ activation\n    - HMP phosphate to HMP diphosphate\n      - ThiD: phosphomethylpyrimidine\
    \ kinase (molecular player: ThiD hydroxymethylpyrimidine/phosphomethylpyrimidine\
    \ kinase family; activity or role: phosphomethylpyrimidine kinase activity)\n\
    \  - 2. thiazole branch\n  - Thiazole phosphate branch\n    - 1. DXP precursor\
    \ supply\n    - DXP formation\n      - Dxs: 1-deoxy-D-xylulose-5-phosphate synthase\
    \ (molecular player: Dxs 1-deoxy-D-xylulose-5-phosphate synthase family; activity\
    \ or role: 1-deoxy-D-xylulose-5-phosphate synthase activity)\n    - 2. glyoxyl\
    \ imine supply\n    - Glycine oxidation to glyoxyl imine\n      - ThiO: glycine\
    \ oxidase (molecular player: ThiO glycine oxidase family; activity or role: glycine\
    \ oxidase activity)\n    - 3. sulfur mobilization and ThiS thiocarboxylation\n\
    \    - ThiS sulfur-carrier thiocarboxylation\n      - IscS: cysteine desulfurase\
    \ sulfur donor (molecular player: IscS cysteine desulfurase family; activity or\
    \ role: cysteine desulfurase activity)\n      - ThiI: sulfur transfer to ThiS\
    \ (molecular player: ThiI tRNA/ThiS sulfurtransferase family)\n      - ThiS: sulfur\
    \ carrier protein (molecular player: ThiS sulfur carrier protein (Pseudomonas\
    \ putida KT2440))\n    - 4. thiazole phosphate formation\n    - Thiazole phosphate\
    \ synthesis\n      - ThiG: thiazole synthase (molecular player: ThiG thiazole\
    \ synthase family; activity or role: thiazole synthase activity)\n  - 3. pyrimidine-thiazole\
    \ coupling\n  - HMP diphosphate plus thiazole phosphate to thiamine phosphate\n\
    \    - ThiE: thiamine-phosphate diphosphorylase (molecular player: ThiE thiamine-phosphate\
    \ synthase family; activity or role: thiamine-phosphate diphosphorylase activity)\n\
    \  - 4. thiamine diphosphate activation\n  - Thiamine phosphate to thiamine diphosphate\n\
    \    - ThiL: thiamine-phosphate kinase (molecular player: ThiL thiamine-phosphate\
    \ kinase family; activity or role: thiamine-phosphate kinase activity)"
  module_connections: '- AIR-derived precursor to HMP phosphate precedes HMP phosphate
    to HMP diphosphate

    - DXP formation feeds into Thiazole phosphate synthesis

    - Glycine oxidation to glyoxyl imine feeds into Thiazole phosphate synthesis

    - IscS: cysteine desulfurase sulfur donor feeds into ThiI: sulfur transfer to
    ThiS

    - ThiI: sulfur transfer to ThiS feeds into ThiS: sulfur carrier protein

    - ThiS: sulfur carrier protein feeds into Thiazole phosphate synthesis

    - HMP phosphate to HMP diphosphate feeds into HMP diphosphate plus thiazole phosphate
    to thiamine phosphate

    - Thiazole phosphate synthesis feeds into HMP diphosphate plus thiazole phosphate
    to thiamine phosphate

    - HMP diphosphate plus thiazole phosphate to thiamine phosphate precedes Thiamine
    phosphate to thiamine diphosphate'
  pathway_query: ppu00730
  pathway_id: ppu00730
  pathway_name: Thiamine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00730 with 13 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '13'
  candidate_genes: '- thiL: PP_0519 | Q88QH4 | Thiamine-monophosphate kinase (TMP
    kinase) (Thiamine-phosphate kinase) (EC 2.7.4.16) (EC 2.7.4.16; primary bucket
    kegg:ppu00730)

    - dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7)
    (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC 2.2.1.7; primary
    bucket kegg:ppu00730)

    - thiO: PP_0612 | Q88Q83 | Glycine oxidase (GO) (EC 1.4.3.19) (EC 1.4.3.19; primary
    bucket kegg:ppu00730)

    - iscS: PP_0842 | Q88PK8 | Cysteine desulfurase IscS (EC 2.8.1.7) (EC 2.8.1.7;
    primary bucket kegg:ppu00730)

    - adk: PP_1506 | P0A136 | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase)
    (ATP:AMP phosphotransferase) (Adenylate monophosphate kinase) (EC 2.7.4.3; primary
    bucket kegg:ppu00730)

    - iscS-II: PP_2435 | Q88K56 | cysteine desulfurase (EC 2.8.1.7) (EC 2.8.1.7; primary
    bucket kegg:ppu00730)

    - PP_3186: PP_3186 | Q88I16 | Aminopyrimidine aminohydrolase (EC 3.5.99.2) (EC
    3.5.99.2; primary bucket kegg:ppu00730)

    - thiD: PP_4782 | Q88DP2 | hydroxymethylpyrimidine kinase (EC 2.7.1.49) (EC 2.7.1.49;
    primary bucket kegg:ppu00730)

    - thiE: PP_4783 | Q88DP1 | Thiamine-phosphate synthase (TP synthase) (TPS) (EC
    2.5.1.3) (Thiamine-phosphate pyrophosphorylase) (TMP pyrophosphorylase) (TMP-PPase)
    (EC 2.5.1.3; primary bucket kegg:ppu00730)

    - rsgA: PP_4903 | Q88DC4 | Small ribosomal subunit biogenesis GTPase RsgA (EC
    3.6.1.-) (EC 3.6.1.-; primary bucket kegg:ppu00730)

    - thiC: PP_4922 | Q88DA5 | Phosphomethylpyrimidine synthase (EC 4.1.99.17) (Hydroxymethylpyrimidine
    phosphate synthase) (HMP-P synthase) (HMP-phosphate synthase) (HMPP synthase)
    (Thiamine biosynthesis protein ThiC) (EC 4.1.99.17; primary bucket kegg:ppu00730)

    - thiI: PP_5045 | Q88CY4 | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier
    protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) (tRNA 4-thiouridine
    synthase) (EC 2.8.1.4; primary bucket kegg:ppu00730)

    - thiG: PP_5104 | Q88CS6 | Thiazole synthase (EC 2.8.1.10) (EC 2.8.1.10; primary
    bucket kegg:ppu00730)'
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__thiamine_diphosphate_biosynthesis__ppu00730-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__thiamine_diphosphate_biosynthesis__ppu00730-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial thiamine diphosphate biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00730
- Resolved ID: ppu00730
- Resolved name: Thiamine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00730 with 13 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 13

- thiL: PP_0519 | Q88QH4 | Thiamine-monophosphate kinase (TMP kinase) (Thiamine-phosphate kinase) (EC 2.7.4.16) (EC 2.7.4.16; primary bucket kegg:ppu00730)
- dxs: PP_0527 | Q88QG7 | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) (EC 2.2.1.7; primary bucket kegg:ppu00730)
- thiO: PP_0612 | Q88Q83 | Glycine oxidase (GO) (EC 1.4.3.19) (EC 1.4.3.19; primary bucket kegg:ppu00730)
- iscS: PP_0842 | Q88PK8 | Cysteine desulfurase IscS (EC 2.8.1.7) (EC 2.8.1.7; primary bucket kegg:ppu00730)
- adk: PP_1506 | P0A136 | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase) (ATP:AMP phosphotransferase) (Adenylate monophosphate kinase) (EC 2.7.4.3; primary bucket kegg:ppu00730)
- iscS-II: PP_2435 | Q88K56 | cysteine desulfurase (EC 2.8.1.7) (EC 2.8.1.7; primary bucket kegg:ppu00730)
- PP_3186: PP_3186 | Q88I16 | Aminopyrimidine aminohydrolase (EC 3.5.99.2) (EC 3.5.99.2; primary bucket kegg:ppu00730)
- thiD: PP_4782 | Q88DP2 | hydroxymethylpyrimidine kinase (EC 2.7.1.49) (EC 2.7.1.49; primary bucket kegg:ppu00730)
- thiE: PP_4783 | Q88DP1 | Thiamine-phosphate synthase (TP synthase) (TPS) (EC 2.5.1.3) (Thiamine-phosphate pyrophosphorylase) (TMP pyrophosphorylase) (TMP-PPase) (EC 2.5.1.3; primary bucket kegg:ppu00730)
- rsgA: PP_4903 | Q88DC4 | Small ribosomal subunit biogenesis GTPase RsgA (EC 3.6.1.-) (EC 3.6.1.-; primary bucket kegg:ppu00730)
- thiC: PP_4922 | Q88DA5 | Phosphomethylpyrimidine synthase (EC 4.1.99.17) (Hydroxymethylpyrimidine phosphate synthase) (HMP-P synthase) (HMP-phosphate synthase) (HMPP synthase) (Thiamine biosynthesis protein ThiC) (EC 4.1.99.17; primary bucket kegg:ppu00730)
- thiI: PP_5045 | Q88CY4 | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) (tRNA 4-thiouridine synthase) (EC 2.8.1.4; primary bucket kegg:ppu00730)
- thiG: PP_5104 | Q88CS6 | Thiazole synthase (EC 2.8.1.10) (EC 2.8.1.10; primary bucket kegg:ppu00730)

## Generic Module Context

### Working Scope

Species-neutral bacterial pathway for de novo synthesis of thiamine diphosphate (ThDP), the active thiamine cofactor. The pathway has two converging branches: a hydroxymethylpyrimidine branch in which ThiC converts an AIR-derived precursor to HMP phosphate and ThiD phosphorylates it to the diphosphate, and a thiazole branch in which Dxs, ThiO, sulfur-relay proteins, and ThiG form the thiazole phosphate moiety. ThiE couples the pyrimidine and thiazole moieties to thiamine phosphate, and ThiL phosphorylates thiamine phosphate to ThDP.

### Provisional Biological Outline

- Thiamine diphosphate biosynthesis
  - 1. hydroxymethylpyrimidine branch
  - Hydroxymethylpyrimidine diphosphate branch
    - 1. HMP phosphate formation
    - AIR-derived precursor to HMP phosphate
      - ThiC: phosphomethylpyrimidine synthase (molecular player: ThiC phosphomethylpyrimidine synthase family; activity or role: phosphomethylpyrimidine synthase activity)
    - 2. HMP phosphate activation
    - HMP phosphate to HMP diphosphate
      - ThiD: phosphomethylpyrimidine kinase (molecular player: ThiD hydroxymethylpyrimidine/phosphomethylpyrimidine kinase family; activity or role: phosphomethylpyrimidine kinase activity)
  - 2. thiazole branch
  - Thiazole phosphate branch
    - 1. DXP precursor supply
    - DXP formation
      - Dxs: 1-deoxy-D-xylulose-5-phosphate synthase (molecular player: Dxs 1-deoxy-D-xylulose-5-phosphate synthase family; activity or role: 1-deoxy-D-xylulose-5-phosphate synthase activity)
    - 2. glyoxyl imine supply
    - Glycine oxidation to glyoxyl imine
      - ThiO: glycine oxidase (molecular player: ThiO glycine oxidase family; activity or role: glycine oxidase activity)
    - 3. sulfur mobilization and ThiS thiocarboxylation
    - ThiS sulfur-carrier thiocarboxylation
      - IscS: cysteine desulfurase sulfur donor (molecular player: IscS cysteine desulfurase family; activity or role: cysteine desulfurase activity)
      - ThiI: sulfur transfer to ThiS (molecular player: ThiI tRNA/ThiS sulfurtransferase family)
      - ThiS: sulfur carrier protein (molecular player: ThiS sulfur carrier protein (Pseudomonas putida KT2440))
    - 4. thiazole phosphate formation
    - Thiazole phosphate synthesis
      - ThiG: thiazole synthase (molecular player: ThiG thiazole synthase family; activity or role: thiazole synthase activity)
  - 3. pyrimidine-thiazole coupling
  - HMP diphosphate plus thiazole phosphate to thiamine phosphate
    - ThiE: thiamine-phosphate diphosphorylase (molecular player: ThiE thiamine-phosphate synthase family; activity or role: thiamine-phosphate diphosphorylase activity)
  - 4. thiamine diphosphate activation
  - Thiamine phosphate to thiamine diphosphate
    - ThiL: thiamine-phosphate kinase (molecular player: ThiL thiamine-phosphate kinase family; activity or role: thiamine-phosphate kinase activity)

### Known Relationships Among Steps

- AIR-derived precursor to HMP phosphate precedes HMP phosphate to HMP diphosphate
- DXP formation feeds into Thiazole phosphate synthesis
- Glycine oxidation to glyoxyl imine feeds into Thiazole phosphate synthesis
- IscS: cysteine desulfurase sulfur donor feeds into ThiI: sulfur transfer to ThiS
- ThiI: sulfur transfer to ThiS feeds into ThiS: sulfur carrier protein
- ThiS: sulfur carrier protein feeds into Thiazole phosphate synthesis
- HMP phosphate to HMP diphosphate feeds into HMP diphosphate plus thiazole phosphate to thiamine phosphate
- Thiazole phosphate synthesis feeds into HMP diphosphate plus thiazole phosphate to thiamine phosphate
- HMP diphosphate plus thiazole phosphate to thiamine phosphate precedes Thiamine phosphate to thiamine diphosphate

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

# Commissioned Review: Bacterial Thiamine Diphosphate Biosynthesis in *Pseudomonas putida* KT2440

**Pathway/bucket:** KEGG ppu00730 (Thiamine metabolism) — de novo ThDP biosynthesis module
**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module area:** cofactors_vitamins_redox
**Scope of this review:** species-aware satisfiability and gene-annotation curation

---

## 1. Executive Summary

The de novo **thiamine diphosphate (ThDP)** biosynthesis module is **satisfiable** in *Pseudomonas putida* KT2440. Ten of eleven core enzymatic steps are encoded by identifiable, high-confidence genes in proteome UP000000556, and the organism is a demonstrated **thiamine prototroph** that grows in defined mineral medium across many single carbon sources without vitamin supplementation. Two of the eleven steps carry *direct target-strain* evidence: the glycine-oxidase ThiO was purified and characterized from KT2440 itself, and the *thiC* leader carries a functional TPP riboswitch validated in KT2440 by in vivo GFP reporter assay. The remaining covered steps rest on strong homology plus EC/InterPro assignment and syntenic clustering (notably the *thiS–thiG* pair).

The single genuine **gap** in the module is the **ThiF-type ThiS C-terminal adenylylation step (EC 2.7.7.73)**, which activates the sulfur-carrier protein ThiS for thiocarboxylate formation. KT2440 encodes **no dedicated ThiF**. Exhaustive proteome searches (gene name, EC 2.7.7.73, and the HesA/MoeB/ThiF E1-like family InterPro signatures) return only **MoeB/PP_0735** (molybdopterin-synthase adenylyltransferase, EC 2.7.7.80) and the t6A-committed TcdA/PP_1527. MoeB is therefore the sole plausible substitute activity and should be marked **candidate_uncertain** and promoted to full gene review.

Several candidate-list items require curation corrections. **ThiS/PP_5105** is functionally required and syntenic with *thiG* but is **missing from the 13-gene candidate list** — it should be added. **adk/PP_1506** (adenylate kinase) and **rsgA/PP_4903** (ribosome-biogenesis GTPase) are KEGG overview-map inclusion artifacts with no role in de novo synthesis and should be excluded. The **TenA** paralogs **PP_3185/PP_3186** (EC 3.5.99.2, aminopyrimidine aminohydrolase / thiaminase II) and the absent **ThiM** belong to a separate thiamine-**salvage** module, not de novo biosynthesis. Finally, **Dxs/PP_0527**, **ThiI/PP_5045**, and **IscS/PP_0842** are pleiotropic branch-point/shared enzymes and should be tagged as such; the second desulfurase **PP_2435** is a lower-priority paralog.

---

## 2. Target-Organism Pathway Definition

### 2.1 What the module includes

The module covers **de novo synthesis of thiamine diphosphate (ThDP)**, the catalytically active thiamine cofactor, from central-metabolism precursors. It comprises two converging branches that are coupled and then activated:

- **Hydroxymethylpyrimidine (HMP) branch:** ThiC converts an AIR-derived precursor to HMP phosphate; ThiD phosphorylates HMP-P to HMP diphosphate (ThiD is typically bifunctional HMP kinase / HMP-P kinase).
- **Thiazole branch:** Dxs supplies 1-deoxy-D-xylulose-5-phosphate (DXP); ThiO oxidizes glycine to the glyoxyl-imine; a sulfur relay (IscS → ThiI → ThiS, with ThiS thiocarboxylation requiring an E1-like ThiF-type adenylylation) delivers sulfur; ThiG condenses these into thiazole phosphate.
- **Coupling and activation:** ThiE couples HMP-PP and thiazole phosphate to thiamine phosphate (TMP); ThiL phosphorylates TMP to ThDP.

### 2.2 Neighboring processes to keep separate

The KEGG map ppu00730 ("Thiamine metabolism") is broader than the de novo biosynthesis module and pulls in peripheral edges that should **not** be scored as de novo steps:

- **Thiamine salvage / degradation:** TenA thiaminase II (PP_3185 *pet*, PP_3186), the TenA-family regulator PP_1762, and (where present) ThiM hydroxyethylthiazole kinase. ThiM is **absent** in KT2440, so the thiazole salvage branch is incomplete.
- **Nucleotide-phosphate interconversion / ThTP metabolism:** adk/PP_1506 (adenylate kinase) and the thiamine-triphosphate node (e.g., ygiF/PP_5187) appear on the overview map via cofactor-phosphate edges but are not de novo biosynthetic.
- **Ribosome biogenesis:** rsgA/PP_4903 is a small-subunit GTPase with no thiamine role; its presence on the bucket is a map artifact.
- **Isoprenoid (MEP) and PLP pathways:** these share the Dxs/DXP branch point but are separate modules.

### 2.3 Alternate names / database definitions

- ThiC = phosphomethylpyrimidine synthase / HMP-P synthase (EC 4.1.99.17).
- ThiD = HMP/HMP-P kinase (EC 2.7.1.49); often bifunctional.
- ThiE = thiamine-phosphate synthase / pyrophosphorylase / diphosphorylase (EC 2.5.1.3).
- ThiL = thiamine-monophosphate kinase / thiamine-phosphate kinase (EC 2.7.4.16).
- ThiO = glycine oxidase (EC 1.4.3.19); the alternative glyoxyl-imine route uses ThiH tyrosine lyase, which is **not** present here.

---

## 3. Expected Step Model and Per-Step Verdicts

The following table consolidates the per-step curation verdicts for the de novo ThDP module in KT2440.

| # | Step | Enzyme / player | KT2440 gene (UniProt, EC) | Verdict | Evidence type |
|---|------|-----------------|---------------------------|---------|---------------|
| 1 | HMP-P synthesis | ThiC | PP_4922 (Q88DA5, 4.1.99.17) | **Covered** | Direct (TPP riboswitch, PMID 27111755) + homology |
| 2 | HMP-P activation | ThiD (bifunctional) | PP_4782 (Q88DP2, 2.7.1.49) | **Covered** | Homology/EC |
| 3 | DXP supply | Dxs (shared branch point) | PP_0527 (Q88QG7, 2.2.1.7) | **Covered (shared)** | Homology; branch point (PMID 41279295) |
| 4 | Glyoxyl-imine supply | ThiO (glycine-oxidase route) | PP_0612 (Q88Q83, 1.4.3.19) | **Covered** | Direct KT2440 biochemistry (PMID 26875494) |
| 5 | Sulfur donor | IscS (housekeeping) | PP_0842 (Q88PK8, 2.8.1.7) | **Covered** | Mechanism in *E. coli* (PMID 10781607); operon synteny |
| 6 | Sulfur transfer | ThiI (shared w/ tRNA s4U) | PP_5045 (Q88CY4, 2.8.1.4) | **Covered (shared)** | Homology + mechanism (PMID 10781607) |
| 7 | Sulfur carrier | ThiS | PP_5105 (Q88CS5) | **Covered — ADD to list** | InterPro IPR010035; *thiS–thiG* synteny |
| 8 | ThiS adenylylation | ThiF (E1-like) | — (no dedicated gene) | **Candidate_uncertain / Gap** | Absence verified; MoeB/PP_0735 substitute |
| 9 | Thiazole synthase | ThiG | PP_5104 (Q88CS6, 2.8.1.10) | **Covered** | Homology/EC |
| 10 | Pyrimidine–thiazole coupling | ThiE | PP_4783 (Q88DP1, 2.5.1.3) | **Covered** | Homology/EC |
| 11 | TMP → ThDP | ThiL | PP_0519 (Q88QH4, 2.7.4.16) | **Covered** | Homology/EC |
| — | Aminopyrimidine hydrolysis | TenA (salvage) | PP_3186/PP_3185 (3.5.99.2) | **Move to salvage module** | Paralogs; not de novo |
| — | Hydroxyethylthiazole kinase | ThiM (salvage) | absent | **Not expected** | No gene encoded |
| — | Adenylate kinase | Adk | PP_1506 (P0A136, 2.7.4.3) | **Exclude (map artifact)** | No de novo role |
| — | Ribosome GTPase | RsgA | PP_4903 (Q88DC4, 3.6.1.-) | **Exclude (map artifact)** | No thiamine role |

**Bottom line:** 10/11 core steps covered; 1 genuine gap (ThiF). Functional prototrophy confirms the pathway is operational, so the "gap" is an annotation/enzyme-family question, not a metabolic capability question.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence, target-strain evidence

**ThiO — glycine oxidase (PP_0612, Q88Q83, EC 1.4.3.19).** This is the strongest single piece of species-specific evidence in the module. ThiO was **purified and characterized directly from KT2440** (Equar, Tani & Mihara 2015). The KT2440 enzyme is *monomeric* — distinct from the homotetrameric ThiO of *Bacillus subtilis* and *Geobacillus kaustophilus* — and *uniquely prefers glycine* as substrate. This establishes both that KT2440 uses the **ThiO glycine-oxidase route** (not the ThiH tyrosine-lyase route) for glyoxyl-imine supply and that the enzyme is genuinely functional in this organism. **Curation note:** the ThiH alternative should be marked *not_expected_in_target_taxon*.

**ThiC — phosphomethylpyrimidine synthase (PP_4922, Q88DA5, EC 4.1.99.17).** Genome-wide TSS mapping in KT2440 identified a **TPP riboswitch** upstream of *thiC*, and an in vivo GFP-fusion assay showed it acts by **translational repression** (D'Arrigo et al. 2016). This is direct target-strain evidence that *thiC* is present, expressed, and thiamine-responsive — exactly the regulatory signature expected of a functional de novo pyrimidine branch.

### 4.2 Covered by strong homology / synteny / mechanism

**ThiS — sulfur carrier (PP_5105, Q88CS5).** Not in the candidate list, but required. It carries the ThiS-specific InterPro signature **IPR010035** ("Sulphur carrier protein ThiS") plus the ThiS/MoaD β-grasp folds (IPR003749, IPR012675, IPR016155), and it sits immediately adjacent to *thiG* (PP_5104), a strong syntenic indicator. **Action: add PP_5105 to the module gene list.**

**ThiG — thiazole synthase (PP_5104, EC 2.8.1.10); ThiE — thiamine-phosphate synthase (PP_4783, EC 2.5.1.3); ThiL — TMP kinase (PP_0519, EC 2.7.4.16); ThiD — HMP/HMP-P kinase (PP_4782, EC 2.7.1.49).** These are covered by unambiguous EC/family assignment. ThiD is likely bifunctional (HMP kinase + HMP-P kinase), which is the norm in γ-proteobacteria. Gene arrangement is scattered (thiS–thiG adjacent; thiD–thiE adjacent; thiC and thiI solo) rather than a single operon.

**IscS — cysteine desulfurase (PP_0842, EC 2.8.1.7) and ThiI — sulfurtransferase (PP_5045, EC 2.8.1.4).** The IscS→ThiI→ThiS sulfur relay is mechanistically validated in *E. coli*: IscS mobilizes sulfur for transfer to the C-terminal carboxylate of ThiS, and ThiI stimulates this transfer (Lauhon & Kambampati 2000). In KT2440 the paralog ambiguity is resolved in favor of the housekeeping **IscS/PP_0842**, which sits in the *isc* operon with *iscU*/PP_0843 — matching the canonical *E. coli* arrangement. The second desulfurase **PP_2435** is not operonically linked to Fe-S/thiamine machinery and is a lower-priority paralog. **Both IscS/PP_0842 and ThiI/PP_5045 are shared/pleiotropic** (Fe-S clusters, tRNA 4-thiouridine), so their presence is guaranteed but not thiamine-specific.

**Dxs — DXP synthase (PP_0527, EC 2.2.1.7).** A single-copy gene supplying the branch-point metabolite DXP, which feeds PLP, ThDP, and isoprenoid (MEP) biosynthesis (Kramer et al.). It is essential and covered, but it is **not a thiamine-specific gene** — tag as shared branch point.

### 4.3 Non-core candidates and likely over-annotations

**adk/PP_1506 (EC 2.7.4.3)** and **rsgA/PP_4903 (EC 3.6.1.-)** have no role in de novo ThDP synthesis; they appear on map ppu00730 only through peripheral nucleotide-phosphate / ThTP-interconversion and ribosome-biogenesis edges. **Exclude from the de novo module.**

**PP_3186 (TenA, EC 3.5.99.2)** has a paralog **PP_3185 (pet, same EC)** and a TenA-family regulator **PP_1762**. These are **thiamine salvage/degradation (thiaminase II)**, not de novo biosynthesis. Because **ThiM** (hydroxyethylthiazole kinase) is absent, the thiazole salvage branch is incomplete. **Move TenA to a separate salvage module; mark ThiM not_expected.**

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 The one genuine gap: ThiF (EC 2.7.7.73)

The sole missing step is **ThiS C-terminal adenylylation**, the E1-like activation that precedes ThiS thiocarboxylate formation. Proteome checks were exhaustive:

- `gene:thiF` → **0 hits**
- EC 2.7.7.73 → **0 hits**
- HesA/MoeB/ThiF E1-like family (InterPro IPR000594 / IPR045886) → exactly **two** members: **MoeB/PP_0735** (Q88PW3, EC 2.7.7.80, molybdopterin-synthase adenylyltransferase) and **TcdA/PP_1527** (t6A tRNA-modification dehydratase).

TcdA is committed to threonylcarbamoyladenosine (t6A) synthesis, leaving **MoeB/PP_0735 as the only plausible ThiF-like enzyme**. ThiF and MoeB are paralogous ubiquitin-like-protein-activating (E1-like) adenylyltransferases, each able in principle to activate the C-terminal Gly of a sulfur-carrier (ThiS or MoaD). Because KT2440 is a confirmed prototroph, the thiazole sulfur relay must operate — so MoeB (or an unannotated activity) most likely covers this step in vivo. **Verdict: candidate_uncertain; assign MoeB/PP_0735 as substitute; promote to full review.**

### 5.2 Ambiguities

- **IscS paralogs:** PP_0842 (housekeeping, *isc* operon) vs. PP_2435. Resolved to PP_0842 by synteny; PP_2435 down-weighted but not excluded.
- **TenA paralogs:** PP_3185/PP_3186 both EC 3.5.99.2 — salvage, separate module.
- **Broad/shared EC-GO mappings:** Dxs, ThiI, IscS carry pleiotropic roles; their thiamine annotation is correct but should not imply thiamine-exclusive function.

### 5.3 Likely over-annotations / map artifacts

adk/PP_1506 and rsgA/PP_4903 are the clearest cases of KEGG overview-map bleed-through and should not be scored as de novo module members.

---

## 6. Module and GO-Curation Recommendations

| Action | Gene(s) | Recommended status |
|--------|---------|--------------------|
| **ADD** to module gene list | ThiS/PP_5105 | covered |
| Mark step candidate_uncertain; assign substitute | ThiF step → MoeB/PP_0735 | candidate_uncertain |
| **REMOVE** (overview-map artifacts) | adk/PP_1506, rsgA/PP_4903 | not in de novo module |
| **MOVE** to salvage module | TenA PP_3185/PP_3186 | separate salvage module |
| Mark not_expected | ThiM (absent); ThiH route | not_expected_in_target_taxon |
| Resolve paralog | IscS → PP_0842 (down-weight PP_2435) | covered |
| Tag shared/pleiotropic | Dxs/PP_0527, ThiI/PP_5045, IscS/PP_0842 | covered (shared) |
| Keep out of de novo module | ThTP metabolism (ygiF/PP_5187), transporters | separate |

**Module boundary assessment:** the generic module scope is correct for KT2440 in requiring a ThiF-type adenylylation step, but the *candidate metadata* is wrong in three ways — it omits ThiS, includes two overview artifacts (adk, rsgA), and conflates salvage (TenA) with de novo synthesis. No new module document is strictly required, but a **companion thiamine-salvage module** would cleanly hold TenA/PP_1762 and clarify that ThiM is absent. No new GO term request is needed; the ThiF step should be flagged for expert curation of whether MoeB moonlights or whether an unannotated ThiF exists.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **MoeB/PP_0735** — highest priority. Resolve whether it provides the missing ThiF-type ThiS-adenylylation activity or whether an unannotated enzyme does. This is the only genuine gap.
2. **ThiS/PP_5105** — confirm addition to the module and verify thiocarboxylate competence.
3. **PP_2435 (iscS-II)** — confirm it is not the physiological thiamine sulfur donor; document paralog roles.
4. **ThiD/PP_4782** — confirm bifunctional HMP/HMP-P kinase assignment.
5. **TenA PP_3185/PP_3186 and PP_1762** — reassign to a salvage module.

---

## 8. Mechanistic Model

```
        HMP (pyrimidine) branch                 Thiazole branch
        ------------------------                 ---------------
        AIR-derived precursor                    Pyruvate + GAP
              |                                        |
        [ThiC PP_4922]  <-- TPP riboswitch        [Dxs PP_0527]  --> also PLP, MEP/isoprenoids
        EC 4.1.99.17    (translational repr.)     EC 2.2.1.7 (shared branch point)
              |                                        |
           HMP-P                                      DXP           Glycine
              |                                        |               |
        [ThiD PP_4782]                                 |         [ThiO PP_0612]  (glycine-oxidase route;
        EC 2.7.1.49                                    |          EC 1.4.3.19    direct KT2440 evidence)
              |                                        |               |
          HMP-PP                                       |          glyoxyl-imine
              |            Sulfur relay: IscS(PP_0842) -> ThiI(PP_5045) -> ThiS(PP_5105)
              |                     (ThiS adenylylation = ThiF step: GAP -> MoeB/PP_0735?)
              |                                        |
              |                                  [ThiG PP_5104]  EC 2.8.1.10
              |                                        |
              |                                 thiazole phosphate
              +----------------+-----------------------+
                               |
                        [ThiE PP_4783]  EC 2.5.1.3
                               |
                        thiamine phosphate (TMP)
                               |
                        [ThiL PP_0519]  EC 2.7.4.16
                               |
                        thiamine diphosphate (ThDP)  <-- active cofactor
```

The narrative: KT2440 builds both moieties from central metabolism, joins them (ThiE), and activates them (ThiL). Every arrow above has an encoded enzyme except the ThiF adenylylation preceding ThiG, where MoeB is the best candidate. Functional prototrophy (Section 4) confirms flux through the entire chain.

---

## 9. Evidence Base

| Finding | Support | Key citation(s) |
|---------|---------|-----------------|
| ThiO glycine-oxidase route, direct KT2440 biochemistry | Direct (target strain) | [PMID: 26875494](https://pubmed.ncbi.nlm.nih.gov/26875494/) |
| *thiC* present, expressed, TPP-regulated | Direct (target strain) | [PMID: 27111755](https://pubmed.ncbi.nlm.nih.gov/27111755/) |
| IscS→ThiI→ThiS sulfur-relay mechanism | Mechanism (*E. coli*, strong transfer) | [PMID: 10781607](https://pubmed.ncbi.nlm.nih.gov/10781607/) |
| Dxs/DXP is a shared branch-point metabolite | Mechanism/biochemistry | [PMID: 41279295](https://pubmed.ncbi.nlm.nih.gov/41279295/), [PMID: 41972430](https://pubmed.ncbi.nlm.nih.gov/41972430/) |
| KT2440 thiamine prototrophy (growth in defined mineral medium) | Functional (target strain) | [PMID: 28294579](https://pubmed.ncbi.nlm.nih.gov/28294579/), [PMID: 37665664](https://pubmed.ncbi.nlm.nih.gov/37665664/) |
| ThiO structure/mechanism reference (route biology) | Homology (*B. subtilis*) | [PMID: 12627963](https://pubmed.ncbi.nlm.nih.gov/12627963/) |

**How the evidence combines:** two independent lines pin the pathway to KT2440 directly (ThiO purification; *thiC* riboswitch), while the sulfur-relay mechanism and the Dxs branch-point are established in closely related bacteria and transfer strongly given conserved synteny and EC assignments. The prototrophy studies are the functional capstone: growth on acetate, glycerol, citrate, succinate, malate, and methanol in defined mineral medium without thiamine (PMID 28294579), and growth-coupled production in *para*-coumarate minimal medium (PMID 37665664), both require an operational de novo ThDP pathway.

Direct quotations underpinning the strongest claims:

- ThiO (PMID 26875494): *"We have purified and characterized ThiO from Pseudomonas putida KT2440. It has a monomeric structure that is distinct from the homotetrameric ThiOs from Bacillus subtilis and Geobacillus kaustophilus. The P. putida ThiO is unique in that glycine is its preferred substrate."*
- Riboswitch (PMID 27111755): *"The thiamine pyrophosphate riboswitch upstream of the thiC gene was examined using an in vivo assay with GFP-fusion vectors and shown to function via a translational repression mechanism."*
- Sulfur relay (PMID 10781607): *"we show that IscS mobilizes sulfur for transfer to the C-terminal carboxylate of ThiS. ThiI, a known factor involved in both thiazole and s(4)U synthesis, stimulates this sulfur transfer step."*
- Prototrophy (PMID 28294579): *"The batch growth of P. putida KT2440 with six individual carbon sources … (acetate, glycerol, citrate, succinate, malate and methanol …) was studied in a defined mineral medium."*
- Branch point (PMID 41279295): *"Its product DXP sits at a metabolic branchpoint between the biosynthesis of pyridoxal phosphate (PLP), thiamin diphosphate (ThDP), and isoprenoids."*

---

## 10. Limitations and Knowledge Gaps

- **No direct KT2440 biochemistry for most steps.** Only ThiO and *thiC* have target-strain evidence. ThiD, ThiE, ThiG, ThiL, ThiS, IscS, ThiI, and Dxs rest on homology/EC/synteny plus the functional prototrophy inference. These transfers are strong (γ-proteobacterial conservation) but not experimentally verified in KT2440.
- **ThiF step unresolved.** Whether MoeB/PP_0735 genuinely adenylylates ThiS, or whether an unannotated ThiF or an alternative sulfur-transfer chemistry operates, is not established. This is the single most important open question.
- **IscS paralog assignment is inferential.** The choice of PP_0842 over PP_2435 rests on operon context, not on a deletion/complementation experiment in KT2440.
- **Salvage module not fully characterized.** TenA paralogs and the absence of ThiM imply an incomplete salvage capability, but this was not exhaustively tested (e.g., HMP/thiazole uptake and reuse).
- **Regulatory scope.** Only the *thiC* TPP riboswitch is documented; whether other thiamine genes are TPP-regulated in KT2440 is unknown.

---

## 11. Proposed Follow-up Experiments and Curator Actions

**Immediate curation (no experiments needed):**
1. Add **ThiS/PP_5105** to the module gene list (covered).
2. Remove **adk/PP_1506** and **rsgA/PP_4903** from the de novo module.
3. Move **TenA PP_3185/PP_3186** (and regulator PP_1762) to a thiamine-salvage module; mark **ThiM** not_expected.
4. Resolve **IscS → PP_0842**; down-weight PP_2435.
5. Tag **Dxs/PP_0527, ThiI/PP_5045, IscS/PP_0842** as shared/pleiotropic.
6. Mark the **ThiF step candidate_uncertain**; assign **MoeB/PP_0735** as substitute and promote to full review.

**Experiments to resolve the gap and ambiguities:**
1. **ThiF/MoeB test:** delete *moeB* (PP_0735) in KT2440 and assay thiamine auxotrophy vs. rescue by thiazole precursor; complement with a heterologous ThiF to confirm the missing activity. In vitro adenylylation of ThiS by purified MoeB.
2. **IscS paralog test:** single and double knockouts of PP_0842 and PP_2435; score thiamine (thiazole) requirement and tRNA s4U levels.
3. **Prototrophy/auxotrophy panel:** targeted knockouts of thiC, thiG, thiE, thiL to confirm each is required for de novo synthesis in KT2440.
4. **Salvage capacity:** growth assays supplementing HMP and/or the thiazole alcohol to a de novo mutant, to test whether TenA-based salvage (without ThiM) supports any rescue.

**Expert questions:**
- Does MoeB in *Pseudomonas* moonlight for ThiS activation, or is there an as-yet-unannotated ThiF paralog?
- Should the curation framework encode "shared E1-like adenylyltransferase" as an accepted substitute for the ThiF step in organisms lacking a dedicated *thiF*?

---

## 12. Key References

- D'Arrigo I, et al. *Genome-wide mapping of transcription start sites yields novel insights into the primary transcriptome of Pseudomonas putida.* [PMID: 27111755](https://pubmed.ncbi.nlm.nih.gov/27111755/)
- Equar MY, Tani Y, Mihara H. *Purification and Properties of Glycine Oxidase from Pseudomonas putida KT2440.* [PMID: 26875494](https://pubmed.ncbi.nlm.nih.gov/26875494/)
- Lauhon CT, Kambampati R. *The iscS gene in Escherichia coli is required for the biosynthesis of 4-thiouridine, thiamin, and NAD.* [PMID: 10781607](https://pubmed.ncbi.nlm.nih.gov/10781607/)
- Settembre E, et al. *Structural and mechanistic studies on ThiO, a glycine oxidase essential for thiamin biosynthesis in Bacillus subtilis.* [PMID: 12627963](https://pubmed.ncbi.nlm.nih.gov/12627963/)
- Kramer et al. *DXPS branch-point / closed-conformation studies (DXP feeds PLP, ThDP, isoprenoids).* [PMID: 41279295](https://pubmed.ncbi.nlm.nih.gov/41279295/), [PMID: 41972430](https://pubmed.ncbi.nlm.nih.gov/41972430/)
- Hintermayer S, Weuster-Botz D. *Experimental validation of in silico estimated biomass yields of Pseudomonas putida KT2440.* [PMID: 28294579](https://pubmed.ncbi.nlm.nih.gov/28294579/)
- *Maximizing microbial bioproduction from sustainable carbon sources using iterative systems engineering* (KT2440 growth-coupled production in minimal medium). [PMID: 37665664](https://pubmed.ncbi.nlm.nih.gov/37665664/)

---

*Prepared for manual module satisfiability and gene-annotation curation. Evidence is explicitly distinguished as direct (target-strain), homology/synteny-based, or transferred from related organisms throughout.*


## Artifacts

- [OpenScientist final report](PSEPK__thiamine_diphosphate_biosynthesis__ppu00730-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__thiamine_diphosphate_biosynthesis__ppu00730-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26875494
2. PMID:27111755
3. PMID:10781607
4. PMID:41279295
5. PMID:41972430
6. PMID:28294579
7. PMID:37665664
8. PMID:12627963