---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:23:54.437427'
end_time: '2026-07-11T17:50:57.775294'
duration_seconds: 1623.34
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Tricarboxylic acid cycle
  module_summary: A taxon-neutral module for the oxidative tricarboxylic acid (TCA)
    cycle, covering acetyl-CoA entry through citrate synthase, citrate/isocitrate
    interconversion, oxidative decarboxylation to succinyl-CoA, succinate-level phosphorylation,
    succinate oxidation through respiratory complex II, fumarate hydration, and malate
    oxidation to regenerate oxaloacetate. The module also records common bacterial
    alternatives at the malate/oxaloacetate node and pyruvate carboxylase as an anaplerotic
    input to oxaloacetate.
  module_outline: "- Tricarboxylic acid cycle\n  - 1. acetyl-CoA entry\n  - Citrate\
    \ synthase\n    - Citrate synthase (molecular player: citrate synthase activity;\
    \ activity or role: citrate synthase activity)\n  - 2. citrate to isocitrate\n\
    \  - Aconitate hydratase\n    - Aconitase (molecular player: aconitate hydratase\
    \ activity; activity or role: aconitate hydratase activity)\n  - 3. isocitrate\
    \ oxidation\n  - Isocitrate dehydrogenase\n    - NADP-dependent isocitrate dehydrogenase\
    \ (molecular player: isocitrate dehydrogenase (NADP+) activity; activity or role:\
    \ isocitrate dehydrogenase (NADP+) activity)\n  - 4. 2-oxoglutarate oxidation\n\
    \  - 2-oxoglutarate dehydrogenase complex\n    - 1. E1 decarboxylation\n    -\
    \ 2-oxoglutarate dehydrogenase E1\n      - 2-oxoglutarate dehydrogenase (molecular\
    \ player: oxoglutarate dehydrogenase (succinyl-transferring) activity; activity\
    \ or role: oxoglutarate dehydrogenase (succinyl-transferring) activity)\n    -\
    \ 2. E2 succinyltransferase\n    - Dihydrolipoyllysine-residue succinyltransferase\n\
    \      - Dihydrolipoyllysine-residue succinyltransferase (molecular player: dihydrolipoyllysine-residue\
    \ succinyltransferase activity; activity or role: dihydrolipoyllysine-residue\
    \ succinyltransferase activity)\n    - 3. E3 lipoamide dehydrogenase\n    - Dihydrolipoyl\
    \ dehydrogenase\n      - Dihydrolipoyl dehydrogenase (molecular player: dihydrolipoyl\
    \ dehydrogenase (NADH) activity; activity or role: dihydrolipoyl dehydrogenase\
    \ (NADH) activity)\n  - 5. succinyl-CoA to succinate\n  - Succinate-CoA ligase\n\
    \    - ADP-forming succinate-CoA ligase (molecular player: succinate-CoA ligase\
    \ (ADP-forming) activity; activity or role: succinate-CoA ligase (ADP-forming)\
    \ activity)\n  - 6. succinate oxidation\n  - Succinate dehydrogenase\n    - Succinate\
    \ dehydrogenase (quinone) (molecular player: succinate dehydrogenase (quinone)\
    \ activity; activity or role: succinate dehydrogenase (quinone) activity)\n  -\
    \ 7. fumarate hydration\n  - Fumarate hydratase\n    - Fumarate hydratase (molecular\
    \ player: fumarate hydratase activity; activity or role: fumarate hydratase activity)\n\
    \  - 8. malate oxidation\n  - Malate to oxaloacetate\n    - NAD-dependent L-malate\
    \ dehydrogenase (molecular player: L-malate dehydrogenase (NAD+) activity; activity\
    \ or role: L-malate dehydrogenase (NAD+) activity)\n    - L-malate dehydrogenase\
    \ (quinone) (molecular player: L-malate dehydrogenase (quinone) activity; activity\
    \ or role: L-malate dehydrogenase (quinone) activity)\n  - 9. anaplerotic oxaloacetate\
    \ input\n  - Pyruvate carboxylase\n    - Pyruvate carboxylase (molecular player:\
    \ pyruvate carboxylase activity; activity or role: pyruvate carboxylase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00020
  pathway_id: ppu00020
  pathway_name: Citrate cycle (TCA cycle)
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00020 with 17 primary genes; module
    area: central_carbon.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '30'
  candidate_genes: '- scpC: PP_0154 | Q88RH5 | Propionyl-CoA:succinate CoA transferase
    (EC 2.8.3.-) (EC 2.8.3.-; primary bucket kegg:ppu00020)

    - aceF: PP_0338 | Q88QZ6 | Acetyltransferase component of pyruvate dehydrogenase
    complex (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)

    - aceE: PP_0339 | Q88QZ5 | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) (EC
    1.2.4.1; primary bucket kegg:ppu00785)

    - acoC: PP_0553 | Q88QE1 | Dihydrolipoyllysine-residue acetyltransferase component
    of acetoin cleaving system (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)

    - mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37;
    primary bucket kegg:ppu00566)

    - mqo1: PP_0751 | Q88PU7 | Probable malate:quinone oxidoreductase 1 (EC 1.1.5.4)
    (MQO 1) (Malate dehydrogenase [quinone] 1) (EC 1.1.5.4; primary bucket kegg:ppu00020)

    - PP_0897: PP_0897 | Q88PF3 | Fumarate hydratase class I (EC 4.2.1.2) (EC 4.2.1.2;
    primary bucket kegg:ppu00020)

    - fumC-I: PP_0944 | Q88PA6 | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2)
    (Aerobic fumarase) (Iron-independent fumarase) (EC 4.2.1.2; primary bucket kegg:ppu00020)

    - mqo2: PP_1251 | Q88NF9 | Probable malate:quinone oxidoreductase 2 (EC 1.1.5.4)
    (MQO 2) (Malate dehydrogenase [quinone] 2) (EC 1.1.5.4; primary bucket kegg:ppu00020)

    - fumC: PP_1755 | Q88M20 | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2)
    (Aerobic fumarase) (Iron-independent fumarase) (EC 4.2.1.2; primary bucket kegg:ppu00020)

    - acnA-I: PP_2112 | Q88L24 | Aconitate hydratase (Aconitase) (EC 4.2.1.3) (EC
    4.2.1.3; primary bucket kegg:ppu00020)

    - prpC: PP_2335 | Q88KF5 | Citrate synthase (primary bucket kegg:ppu00020)

    - acnB: PP_2339 | Q88KF1 | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate
    dehydratase) (EC 4.2.1.3; 4.2.1.99; primary bucket kegg:ppu00020)

    - mqo3: PP_2925 | Q88IS4 | Probable malate:quinone oxidoreductase 3 (EC 1.1.5.4)
    (MQO 3) (Malate dehydrogenase [quinone] 3) (EC 1.1.5.4; primary bucket kegg:ppu00020)

    - icd: PP_4011 | Q88FS2 | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) (EC 1.1.1.42;
    primary bucket kegg:ppu04146)

    - idh: PP_4012 | Q88FS1 | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) (Oxalosuccinate
    decarboxylase) (EC 1.1.1.42; primary bucket kegg:ppu04146)

    - sucD: PP_4185 | Q88FB3 | Succinate--CoA ligase [ADP-forming] subunit alpha (EC
    6.2.1.5) (Succinyl-CoA synthetase subunit alpha) (SCS-alpha) (EC 6.2.1.5; primary
    bucket kegg:ppu00660)

    - sucC: PP_4186 | Q88FB2 | Succinate--CoA ligase [ADP-forming] subunit beta (EC
    6.2.1.5) (Succinyl-CoA synthetase subunit beta) (SCS-beta) (EC 6.2.1.5; primary
    bucket kegg:ppu00660)

    - lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - sucB: PP_4188 | Q88FB0 | Dihydrolipoyllysine-residue succinyltransferase component
    of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxoglutarate dehydrogenase
    complex component E2) (EC 2.3.1.61; primary bucket kegg:ppu00785)

    - sucA: PP_4189 | Q88FA9 | 2-oxoglutarate dehydrogenase E1 component (EC 1.2.4.2)
    (Alpha-ketoglutarate dehydrogenase) (EC 1.2.4.2; primary bucket kegg:ppu00785)

    - sdhB: PP_4190 | Q88FA8 | Succinate dehydrogenase iron-sulfur subunit (EC 1.3.5.1)
    (EC 1.3.5.1; primary bucket kegg:ppu00020)

    - sdhA: PP_4191 | Q88FA7 | Succinate dehydrogenase flavoprotein subunit (EC 1.3.5.1)
    (EC 1.3.5.1; primary bucket kegg:ppu00020)

    - sdhD: PP_4192 | Q88FA6 | Succinate dehydrogenase hydrophobic membrane anchor
    subunit (primary bucket kegg:ppu00020)

    - sdhC: PP_4193 | Q88FA5 | Succinate dehydrogenase cytochrome b556 subunit (primary
    bucket kegg:ppu00020)

    - gltA: PP_4194 | Q88FA4 | Citrate synthase (primary bucket kegg:ppu00020)

    - lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - pycB: PP_5346 | Q88C37 | Pyruvate carboxylase subunit B (EC 6.4.1.1) (EC 6.4.1.1;
    primary bucket kegg:ppu00020)

    - pycA: PP_5347 | Q88C36 | Biotin carboxylase (Acetyl-coenzyme A carboxylase biotin
    carboxylase subunit A) (primary bucket kegg:ppu00020)

    - lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)'
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
  path: PSEPK__tca_cycle__ppu00020-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__tca_cycle__ppu00020-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Tricarboxylic acid cycle in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00020
- Resolved ID: ppu00020
- Resolved name: Citrate cycle (TCA cycle)
- Source: KEGG

Resolved local bucket kegg:ppu00020 with 17 primary genes; module area: central_carbon.

## Candidate Genes From Local Metadata

Candidate gene count: 30

- scpC: PP_0154 | Q88RH5 | Propionyl-CoA:succinate CoA transferase (EC 2.8.3.-) (EC 2.8.3.-; primary bucket kegg:ppu00020)
- aceF: PP_0338 | Q88QZ6 | Acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)
- aceE: PP_0339 | Q88QZ5 | Pyruvate dehydrogenase E1 component (EC 1.2.4.1) (EC 1.2.4.1; primary bucket kegg:ppu00785)
- acoC: PP_0553 | Q88QE1 | Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system (EC 2.3.1.12) (EC 2.3.1.12; primary bucket kegg:ppu00785)
- mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37; primary bucket kegg:ppu00566)
- mqo1: PP_0751 | Q88PU7 | Probable malate:quinone oxidoreductase 1 (EC 1.1.5.4) (MQO 1) (Malate dehydrogenase [quinone] 1) (EC 1.1.5.4; primary bucket kegg:ppu00020)
- PP_0897: PP_0897 | Q88PF3 | Fumarate hydratase class I (EC 4.2.1.2) (EC 4.2.1.2; primary bucket kegg:ppu00020)
- fumC-I: PP_0944 | Q88PA6 | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2) (Aerobic fumarase) (Iron-independent fumarase) (EC 4.2.1.2; primary bucket kegg:ppu00020)
- mqo2: PP_1251 | Q88NF9 | Probable malate:quinone oxidoreductase 2 (EC 1.1.5.4) (MQO 2) (Malate dehydrogenase [quinone] 2) (EC 1.1.5.4; primary bucket kegg:ppu00020)
- fumC: PP_1755 | Q88M20 | Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2) (Aerobic fumarase) (Iron-independent fumarase) (EC 4.2.1.2; primary bucket kegg:ppu00020)
- acnA-I: PP_2112 | Q88L24 | Aconitate hydratase (Aconitase) (EC 4.2.1.3) (EC 4.2.1.3; primary bucket kegg:ppu00020)
- prpC: PP_2335 | Q88KF5 | Citrate synthase (primary bucket kegg:ppu00020)
- acnB: PP_2339 | Q88KF1 | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate dehydratase) (EC 4.2.1.3; 4.2.1.99; primary bucket kegg:ppu00020)
- mqo3: PP_2925 | Q88IS4 | Probable malate:quinone oxidoreductase 3 (EC 1.1.5.4) (MQO 3) (Malate dehydrogenase [quinone] 3) (EC 1.1.5.4; primary bucket kegg:ppu00020)
- icd: PP_4011 | Q88FS2 | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) (EC 1.1.1.42; primary bucket kegg:ppu04146)
- idh: PP_4012 | Q88FS1 | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) (Oxalosuccinate decarboxylase) (EC 1.1.1.42; primary bucket kegg:ppu04146)
- sucD: PP_4185 | Q88FB3 | Succinate--CoA ligase [ADP-forming] subunit alpha (EC 6.2.1.5) (Succinyl-CoA synthetase subunit alpha) (SCS-alpha) (EC 6.2.1.5; primary bucket kegg:ppu00660)
- sucC: PP_4186 | Q88FB2 | Succinate--CoA ligase [ADP-forming] subunit beta (EC 6.2.1.5) (Succinyl-CoA synthetase subunit beta) (SCS-beta) (EC 6.2.1.5; primary bucket kegg:ppu00660)
- lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- sucB: PP_4188 | Q88FB0 | Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxoglutarate dehydrogenase complex component E2) (EC 2.3.1.61; primary bucket kegg:ppu00785)
- sucA: PP_4189 | Q88FA9 | 2-oxoglutarate dehydrogenase E1 component (EC 1.2.4.2) (Alpha-ketoglutarate dehydrogenase) (EC 1.2.4.2; primary bucket kegg:ppu00785)
- sdhB: PP_4190 | Q88FA8 | Succinate dehydrogenase iron-sulfur subunit (EC 1.3.5.1) (EC 1.3.5.1; primary bucket kegg:ppu00020)
- sdhA: PP_4191 | Q88FA7 | Succinate dehydrogenase flavoprotein subunit (EC 1.3.5.1) (EC 1.3.5.1; primary bucket kegg:ppu00020)
- sdhD: PP_4192 | Q88FA6 | Succinate dehydrogenase hydrophobic membrane anchor subunit (primary bucket kegg:ppu00020)
- sdhC: PP_4193 | Q88FA5 | Succinate dehydrogenase cytochrome b556 subunit (primary bucket kegg:ppu00020)
- gltA: PP_4194 | Q88FA4 | Citrate synthase (primary bucket kegg:ppu00020)
- lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- pycB: PP_5346 | Q88C37 | Pyruvate carboxylase subunit B (EC 6.4.1.1) (EC 6.4.1.1; primary bucket kegg:ppu00020)
- pycA: PP_5347 | Q88C36 | Biotin carboxylase (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) (primary bucket kegg:ppu00020)
- lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)

## Generic Module Context

### Working Scope

A taxon-neutral module for the oxidative tricarboxylic acid (TCA) cycle, covering acetyl-CoA entry through citrate synthase, citrate/isocitrate interconversion, oxidative decarboxylation to succinyl-CoA, succinate-level phosphorylation, succinate oxidation through respiratory complex II, fumarate hydration, and malate oxidation to regenerate oxaloacetate. The module also records common bacterial alternatives at the malate/oxaloacetate node and pyruvate carboxylase as an anaplerotic input to oxaloacetate.

### Provisional Biological Outline

- Tricarboxylic acid cycle
  - 1. acetyl-CoA entry
  - Citrate synthase
    - Citrate synthase (molecular player: citrate synthase activity; activity or role: citrate synthase activity)
  - 2. citrate to isocitrate
  - Aconitate hydratase
    - Aconitase (molecular player: aconitate hydratase activity; activity or role: aconitate hydratase activity)
  - 3. isocitrate oxidation
  - Isocitrate dehydrogenase
    - NADP-dependent isocitrate dehydrogenase (molecular player: isocitrate dehydrogenase (NADP+) activity; activity or role: isocitrate dehydrogenase (NADP+) activity)
  - 4. 2-oxoglutarate oxidation
  - 2-oxoglutarate dehydrogenase complex
    - 1. E1 decarboxylation
    - 2-oxoglutarate dehydrogenase E1
      - 2-oxoglutarate dehydrogenase (molecular player: oxoglutarate dehydrogenase (succinyl-transferring) activity; activity or role: oxoglutarate dehydrogenase (succinyl-transferring) activity)
    - 2. E2 succinyltransferase
    - Dihydrolipoyllysine-residue succinyltransferase
      - Dihydrolipoyllysine-residue succinyltransferase (molecular player: dihydrolipoyllysine-residue succinyltransferase activity; activity or role: dihydrolipoyllysine-residue succinyltransferase activity)
    - 3. E3 lipoamide dehydrogenase
    - Dihydrolipoyl dehydrogenase
      - Dihydrolipoyl dehydrogenase (molecular player: dihydrolipoyl dehydrogenase (NADH) activity; activity or role: dihydrolipoyl dehydrogenase (NADH) activity)
  - 5. succinyl-CoA to succinate
  - Succinate-CoA ligase
    - ADP-forming succinate-CoA ligase (molecular player: succinate-CoA ligase (ADP-forming) activity; activity or role: succinate-CoA ligase (ADP-forming) activity)
  - 6. succinate oxidation
  - Succinate dehydrogenase
    - Succinate dehydrogenase (quinone) (molecular player: succinate dehydrogenase (quinone) activity; activity or role: succinate dehydrogenase (quinone) activity)
  - 7. fumarate hydration
  - Fumarate hydratase
    - Fumarate hydratase (molecular player: fumarate hydratase activity; activity or role: fumarate hydratase activity)
  - 8. malate oxidation
  - Malate to oxaloacetate
    - NAD-dependent L-malate dehydrogenase (molecular player: L-malate dehydrogenase (NAD+) activity; activity or role: L-malate dehydrogenase (NAD+) activity)
    - L-malate dehydrogenase (quinone) (molecular player: L-malate dehydrogenase (quinone) activity; activity or role: L-malate dehydrogenase (quinone) activity)
  - 9. anaplerotic oxaloacetate input
  - Pyruvate carboxylase
    - Pyruvate carboxylase (molecular player: pyruvate carboxylase activity; activity or role: pyruvate carboxylase activity)

### Known Relationships Among Steps

No explicit connections.

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

# Module/Pathway/Taxon Review: Tricarboxylic Acid Cycle in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target pathway:** KEGG ppu00020 — Citrate cycle (TCA cycle); module area: central_carbon
**Candidate genes reviewed:** 30 (local metadata)

---

## 1. Executive Summary

The complete **oxidative tricarboxylic acid (TCA) cycle is encoded and satisfiable** in *Pseudomonas putida* KT2440. All nine steps of the taxon-neutral module — acetyl-CoA entry via citrate synthase, citrate/isocitrate interconversion, isocitrate oxidative decarboxylation, 2-oxoglutarate oxidation, succinyl-CoA-level phosphorylation, succinate oxidation through respiratory complex II, fumarate hydration, malate oxidation, and anaplerotic oxaloacetate input — map to identifiable genes with unambiguous or redundant coverage. There are **no true gaps** in the core cycle.

The single most important lineage-specific feature is the **malate → oxaloacetate node**. KT2440 dedicates three malate:quinone oxidoreductase (MQO) paralogs (*mqo1*/PP_0751, *mqo2*/PP_1251, *mqo3*/PP_2925; K00116, EC 1.1.5.4) to this reaction, while carrying only a single, "putative", non-TCA-bucketed NAD-dependent malate dehydrogenase (*mdh*/PP_0654, K00024). Biochemical evidence from close relatives — *P. aeruginosa* and *P. pseudoalcaligenes* — shows that NAD-MDH activity is often undetectable and that MQO is the physiologically dominant, and sometimes essential, route for malate oxidation. The module's quinone branch should therefore be treated as **primary** in this organism, and PP_0654 flagged `candidate_uncertain`.

The main curation actions are pruning **over-propagated and boundary annotations** that KEGG appends to map00020. Three candidates are methylcitrate/propionate-cycle or CoA-transfer enzymes mis-labelled as core TCA members: *prpC*/PP_2335 is 2-methylcitrate synthase (K01659, EC 2.3.3.5), not citrate synthase; *scpC*/PP_0154 is a succinyl-CoA:acetate CoA-transferase (K18118, EC 2.8.3.18), not the ADP-forming succinyl-CoA synthetase; and both aconitases (*acnA*/PP_2112, *acnB*/PP_2339) are bifunctional aconitate hydratase / 2-methylisocitrate dehydratase enzymes shared with the methylcitrate cycle. In addition, the pyruvate dehydrogenase complex (*aceE*/*aceF*/*acoC*) and the glyoxylate shunt (*aceA*/PP_4116, *glcB*/PP_0356) are neighboring pathways that should be kept as separate modules. Critically, **every KT2440 TCA annotation is homology-inferred** (UniProt protein-existence level 3, or level 4 for pyruvate carboxylase); there is no direct protein- or transcript-level evidence for any individual core gene in this strain.

---

## 2. Target-Organism Pathway Definition

### 2.1 What the module includes

The module covers the **oxidative (clockwise) TCA cycle** as it operates aerobically in *P. putida* KT2440: the eight canonical enzymatic steps from acetyl-CoA + oxaloacetate → citrate around to regeneration of oxaloacetate, plus two curatorial extensions specific to bacterial biology — the **quinone-linked malate oxidation alternative** and **pyruvate carboxylase anaplerosis** feeding the oxaloacetate node.

*P. putida* KT2440 is an obligate aerobe with a strongly respiratory, oxidative central metabolism. It lacks a canonical Embden–Meyerhof–Parnas glycolysis flux (using the Entner–Doudoroff route and the cyclic EDEMP topology instead) and relies heavily on the TCA cycle, glyoxylate shunt, and gluconeogenesis for growth on organic acids. 13C flux analysis places the TCA cycle firmly within the tightly-regulated, transcriptionally-invariant core of central carbon metabolism ([PMID: 24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/)).

### 2.2 Neighboring pathways to keep separate

| Neighboring process | KEGG map | Genes in candidate list | Curation note |
|---|---|---|---|
| Pyruvate dehydrogenase complex (acetyl-CoA generation) | ppu00785 (lipoic acid) | *aceE*/PP_0339, *aceF*/PP_0338, *acoC*/PP_0553 | Feeds acetyl-CoA **into** the cycle; not a cycle reaction |
| Methylcitrate / propionate cycle | ppu00640 | *prpC*/PP_2335, and bifunctional *acnA*/*acnB* | Over-propagated into map00020 |
| Glyoxylate bypass | ppu00630 | *aceA*/PP_4116, *glcB*/PP_0356 (NOT in candidate set) | Separate module; anaplerotic on C2 substrates |
| Acetate/CoA-transfer activation | — | *scpC*/PP_0154 | CoA-transferase, not SCS |
| Isocitrate DH bucket artifact | ppu04146 | *icd*/PP_4011, *idh*/PP_4012 | Genuinely TCA; KEGG primary-bucket artifact |

### 2.3 Alternate names and database definitions

The pathway is variously called the **citrate cycle**, **citric acid cycle**, **Krebs cycle**, or **TCA cycle**. KEGG defines it as ppu00020 "Citrate cycle (TCA cycle)". BioCyc/MetaCyc split the same chemistry across "TCA cycle I (prokaryotic)" and related variants. The key definitional subtlety for KT2440 is the **isocitrate dehydrogenase cofactor specificity** (NADP-only here) and the **malate-oxidation cofactor** (quinone-linked MQO, not NAD-MDH), both of which distinguish the *Pseudomonas* realization from the *E. coli* textbook version.

---

## 3. Expected Step Model and Satisfiability

| # | Step | Expected activity | KT2440 gene(s) | KO / EC | Status |
|---|---|---|---|---|---|
| 1 | Acetyl-CoA entry | Citrate synthase (2.3.3.1) | **gltA**/PP_4194 | K01647 | **covered** (single canonical) |
| 2 | Citrate → isocitrate | Aconitate hydratase (4.2.1.3) | **acnA**/PP_2112, **acnB**/PP_2339 | K27802 / K01682 | **covered** (bifunctional caveat) |
| 3 | Isocitrate oxidation | Isocitrate DH, NADP (1.1.1.42) | **icd**/PP_4011, **idh**/PP_4012 | K00031 | **covered** (NADP-only) |
| 4 | 2-Oxoglutarate oxidation | 2-OGDH complex E1/E2/E3 | **sucA**/PP_4189, **sucB**/PP_4188, E3 (lpd pool) | K00164/K00658/K00382 | **covered** |
| 5 | Succinyl-CoA → succinate | Succinate-CoA ligase, ADP (6.2.1.5) | **sucC**/PP_4186, **sucD**/PP_4185 | K01902/K01903 | **covered** (scpC is a decoy) |
| 6 | Succinate oxidation | Succinate DH, quinone (1.3.5.1) | **sdhC/D/A/B**/PP_4193–4190 | K00239–K00242 | **covered** (full operon) |
| 7 | Fumarate hydration | Fumarate hydratase (4.2.1.2) | PP_0897 (class I), **fumC-I**/PP_0944, **fumC**/PP_1755 (class II) | K01676 / K01679 | **covered** (triply redundant) |
| 8 | Malate oxidation | L-malate DH (NAD) **or** MQO (quinone) | **mqo1/2/3**/PP_0751,1251,2925; *mdh*/PP_0654 (putative) | K00116 / K00024 | **covered via quinone branch** |
| 9 | Anaplerotic OAA input | Pyruvate carboxylase (6.4.1.1) | **pycB**/PP_5346, **pycA**/PP_5347 | K01960 / K01959 | **covered** (two-subunit biotin form) |

**Bottom line:** every module step is satisfiable. The only cofactor/branch decisions a curator must lock in are (i) NADP-only IDH at step 3, and (ii) the quinone (MQO) branch as primary at step 8.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence core TCA genes

**gltA (PP_4194) — citrate synthase, step 1.** KEGG genome-wide link queries return **exactly one** gene for the canonical Si-citrate synthase KO K01647 (EC 2.3.3.1) in organism *ppu*: PP_4194 (Finding F007). This makes *gltA* the unambiguous citrate-synthase call. The second "citrate synthase" in the candidate list, *prpC*/PP_2335, is a decoy (see §5). *gltA* sits in the large *sdhCDAB-sucABlpd-gltA* respiratory operon (PP_4185–4194), consistent with co-regulation of the oxidative cycle.

**acnA (PP_2112) and acnB (PP_2339) — aconitase, step 2.** Both are present, but both carry bifunctional aconitate hydratase / 2-methylisocitrate dehydratase annotations (EC 4.2.1.3 + 4.2.1.99). *acnB* is explicitly labelled a 2-methylisocitrate dehydratase. Step 2 is covered, but a curator should note these enzymes are **shared with the methylcitrate cycle** and their EC 4.2.1.99 activity is not a TCA reaction.

**icd (PP_4011) and idh (PP_4012) — isocitrate dehydrogenase, step 3.** Both map to **K00031, NADP-dependent ICD (EC 1.1.1.42)** — *icd* is the dimeric NADP-ICD and *idh* the monomeric NADP-ICD. A KEGG genome check for K00030 (NAD-dependent ICD, EC 1.1.1.41) returns **zero genes** in *ppu* (Finding F007). KT2440 therefore has **NADP-only** isocitrate dehydrogenase, exactly matching the module's "NADP-dependent isocitrate dehydrogenase" step. No NAD-ICD step should be expected.

**sucA/sucB + E3 (PP_4189/PP_4188 + lpd pool) — 2-OGDH complex, step 4.** E1 (*sucA*, K00164) and E2 (*sucB*, K00658) are single-copy. The E3 dihydrolipoyl dehydrogenase is supplied by **three interchangeable paralogs** all mapping to K00382 (EC 1.8.1.4): *lpdG*/PP_4187, *lpdV*/PP_4404, *lpd*/PP_5366 (Finding F003). This same E3 pool is shared with pyruvate dehydrogenase (*aceE*/*aceF*) and branched-chain 2-oxoacid dehydrogenase — a normal bacterial arrangement. The E3 paralogs are correctly bucketed to ppu00785, and their presence in the candidate list reflects moonlighting across complexes rather than three separate TCA enzymes.

**sucC/sucD (PP_4186/PP_4185) — succinate-CoA ligase, step 5.** Canonical ADP-forming SCS α (*sucD*, K01903) and β (*sucC*, K01902) subunits. This is the correct call for step 5; *scpC* is a decoy (§5).

**sdhCDAB (PP_4193–PP_4190) — succinate dehydrogenase / complex II, step 6.** The complete four-subunit operon: cytochrome b556 (*sdhC*, K00241), membrane anchor (*sdhD*, K00242), flavoprotein (*sdhA*, K00239), and iron-sulfur subunit (*sdhB*, K00240) (Finding F005). Fully covered, quinone-linked (EC 1.3.5.1).

**Fumarases (PP_0897, fumC-I/PP_0944, fumC/PP_1755) — step 7.** Triply redundant: one class-I fumarate hydratase (PP_0897, K01676) plus two class-II fumarases (K01679) (Finding F005). Class-II ("aerobic/iron-independent") fumarases are the expected aerobic workhorses; the class-I enzyme provides oxidative-stress/iron-limitation backup. Step 7 is robustly covered.

**mqo1/2/3 (PP_0751, PP_1251, PP_2925) — malate oxidation, step 8.** Three MQO paralogs (K00116, EC 1.1.5.4) constitute the dominant malate-oxidation route (see §4.2). This is the defining lineage-specific feature.

**pycA/pycB (PP_5347/PP_5346) — pyruvate carboxylase, step 9.** The two-subunit biotin-dependent form: biotin carboxylase *pycA* (K01959) + carboxyltransferase *pycB* (K01960) (Finding F004). Provides anaplerotic oxaloacetate. UniProt protein-existence level 4 ("Predicted") — the weakest evidence tier in the set.

### 4.2 The MQO malate node (Finding F001)

KEGG ppu00020 assigns **three** genes to K00116 malate:quinone oxidoreductase (*mqo1*, *mqo2*, *mqo3*), whereas only one gene — *mdh*/PP_0654 — carries K00024 NAD-MDH (EC 1.1.1.37), and that gene is annotated "probable/putative" with a primary bucket **outside** the TCA cycle (ppu00566). This gene-dosage asymmetry strongly implies quinone-linked malate oxidation is the physiological default.

Transfer from close relatives is **strong at the genus level**: in *P. aeruginosa*, an *mqo* knockout abolished growth on ethanol or acetate, and "*an NAD-dependent malate dehydrogenase activity could not be detected*" ([PMID: 12480887](https://pubmed.ncbi.nlm.nih.gov/12480887/)). In *P. pseudoalcaligenes* CECT5344, "*Malate dehydrogenase activity was undetectable, but a malate:quinone oxidoreductase activity coupled to the cyanide-insensitive alternative oxidase was found in membrane fractions*" ([PMID: 21178163](https://pubmed.ncbi.nlm.nih.gov/21178163/)). Both are same-genus *Pseudomonas* observations, so transfer to KT2440 is reasonable, though direct KT2440 enzymatic confirmation is still lacking (KT2440 itself remains homology-level).

**Curation implication:** mark the quinone branch of step 8 as the **primary/covered** route; mark *mdh*/PP_0654 as `candidate_uncertain` (present, but likely minor or anabolic rather than the main oxidative-cycle enzyme).

### 4.3 Evidence tier summary (Finding F005)

All 22 core candidates were checked against UniProt protein-existence levels: **all are level 3 "Inferred from homology"**; *pycA*/*pycB* are level 4 "Predicted". **None are PE1 (protein-level) or PE2 (transcript-level).** This means every gene call in this module rests on sequence homology and pathway-database inference, not on direct KT2440 biochemistry.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Over-propagated / decoy annotations to prune (Finding F002)

These candidates are bucketed to ppu00020 but are **not** core oxidative-TCA enzymes:

| Gene | Locus | Labelled as | Authoritative call | Action |
|---|---|---|---|---|
| **prpC** | PP_2335 | "Citrate synthase" | K01659 **2-methylcitrate synthase** (EC 2.3.3.5) | Reassign to methylcitrate cycle; NOT step 1 |
| **scpC** | PP_0154 | CoA transferase (EC 2.8.3.-) | K18118 **succinyl-CoA:acetate CoA-transferase** (EC 2.8.3.18) | Acetate activation; NOT step 5 SCS |
| **acnA** | PP_2112 | Aconitase | K27802 bifunctional aconitase / 2-methylisocitrate dehydratase | Covers step 2 but shared w/ methylcitrate |
| **acnB** | PP_2339 | Aconitate hydratase B | K01682 bifunctional (EC 4.2.1.3 + 4.2.1.99) | Covers step 2 but shared w/ methylcitrate |

Canonical single-copy TCA reactions (*gltA* CS, *sucCD* SCS, *sdhABCD* SDH, *sucAB*+*lpd* 2-OGDH) contrast sharply with these ambiguous/duplicated entries.

### 5.2 Boundary pathways (Finding F004)

- **PDH complex** (*aceE*/PP_0339 K00163, *aceF*/PP_0338 K00627, *acoC*/PP_0553 K00627 acetoin-cleaving system) carry primary bucket **ppu00785**, not ppu00020. They generate acetyl-CoA that enters the cycle. *acoC* belongs to a distinct acetoin-cleaving complex. Keep as a separate PDH/lipoic-acid module.
- **Glyoxylate shunt**: KEGG genome checks place isocitrate lyase *aceA*/PP_4116 (K01637) and malate synthase *glcB*/PP_0356 (K01638) in the genome, but **both are absent from the 30-gene candidate list** (Finding F007), confirming the glyoxylate bypass is a genomically and curatorially separate module. This matters because KT2440 routes heavy flux through the glyoxylate shunt and gluconeogenesis when growing on acetate/succinate ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/); [PMID: 41390427](https://pubmed.ncbi.nlm.nih.gov/41390427/)).

### 5.3 Genuine ambiguities

- **mdh/PP_0654**: present but "probable", non-TCA bucket, and biochemically often silent in *Pseudomonas*. Status: `candidate_uncertain`.
- **E3 paralog attribution**: three *lpd* genes serve multiple complexes; a curator should not count them as three TCA enzymes.
- **IDH primary bucket**: *icd*/*idh* are bucketed ppu04146, an artifact; they are genuine TCA step-3 enzymes.

### 5.4 No true gaps

No expected oxidative-TCA reaction lacks a gene. There is no NAD-ICD (not expected here) and no missing succinate/fumarate/malate node.

---

## 6. Mechanistic Model / Interpretation

```
                    acetyl-CoA (from PDH: aceE/aceF — SEPARATE MODULE ppu00785)
                         |
                         v   [gltA / PP_4194  (unique K01647 CS)]
        oxaloacetate --> citrate
             ^                |  [acnA/acnB — bifunctional, shared w/ methylcitrate]
             |                v
   [MALATE NODE]          isocitrate
   mqo1/2/3 (PRIMARY,         |  [icd + idh — NADP-ONLY, no NAD-ICD]
    quinone-linked)          v
   mdh/PP_0654 (uncertain) 2-oxoglutarate
             ^                |  [sucA + sucB + lpd(x3 shared E3)]
             |                v
          malate          succinyl-CoA
             ^                |  [sucC/sucD — canonical ADP-forming SCS]
             |                |   (scpC = DECOY CoA-transferase)
   [fumC-I/fumC/PP_0897]     v
          fumarate <----- succinate
                  [sdhCDAB — full complex II operon]

   Anaplerosis: pyruvate --pycA/pycB--> oxaloacetate  (biotin-dependent, PE4)
```

The KT2440 oxidative TCA cycle is **complete and redundant at three nodes** (malate oxidation: 3 MQO; E3: 3 lpd; fumarate: 3 fumarases) and **single-copy at the diagnostic committed steps** (citrate synthase, SCS, SDH, 2-OGDH E1/E2). The redundancy pattern is itself informative: it concentrates at metabolic branch points that serve multiple pathways (malate node feeds gluconeogenesis; E3 serves three dehydrogenase complexes; fumarases hedge against oxidative stress), while the linear oxidative-decarboxylation core is streamlined. The two cofactor "surprises" relative to the *E. coli* textbook — NADP-only IDH and quinone-linked MQO — reflect *Pseudomonas*'s respiratory, NADPH-provisioning lifestyle and should be encoded as the taxon-default in the module, not treated as anomalies or gaps.

---

## 7. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|---|---|---|
| 1. Citrate synthase | **covered** | *gltA*/PP_4194, unique K01647 hit |
| 2. Aconitase | **covered** (annotate bifunctional caveat) | *acnA*, *acnB* |
| 3. Isocitrate DH (NADP) | **covered** — lock NADP-only | *icd*, *idh*; K00030 absent |
| 4. 2-OGDH complex | **covered** | *sucA*, *sucB*, shared *lpd* E3 |
| 5. Succinate-CoA ligase | **covered** | *sucC*, *sucD*; exclude *scpC* |
| 6. Succinate DH (complex II) | **covered** | *sdhCDAB* full operon |
| 7. Fumarate hydratase | **covered** (redundant) | PP_0897 + two class-II fumC |
| 8a. Malate DH (NAD) | **candidate_uncertain** | *mdh*/PP_0654 putative, non-TCA bucket |
| 8b. Malate:quinone oxidoreductase | **covered — mark primary** | *mqo1/2/3*; genus biochemical support |
| 9. Pyruvate carboxylase (anaplerotic) | **covered** (PE4, weak) | *pycA*, *pycB* |

**Module boundary corrections:**
- Move *prpC*, *scpC* out of the TCA module (into methylcitrate / acetate-activation).
- Keep PDH (*aceE/aceF/acoC*) and glyoxylate shunt (*aceA/glcB*) as separate modules.
- Set the **quinone-linked malate branch as primary** in the module definition for this taxon; the generic module's default NAD-MDH branch is misleading for *Pseudomonas*.

**GO / module-document requests:**
- No new GO terms are required — existing terms (malate:quinone oxidoreductase activity GO:0008924; isocitrate dehydrogenase (NADP+) GO:0004450; etc.) cover all activities.
- Consider a **taxon-note on the module document** flagging (i) MQO dominance and (ii) NADP-only IDH as *Pseudomonas*-characteristic features, so downstream curators do not re-add NAD-MDH/NAD-ICD steps as "gaps".

---

## 8. Genes to Promote to Full `fetch-gene` Review

Priority candidates for individual `fetch-gene` review, ranked by curation impact:

1. **mdh / PP_0654** — resolve whether it has any physiological NAD-MDH role in KT2440 or is functionally silent; determines whether step 8a is `candidate_uncertain` or `not_expected`.
2. **prpC / PP_2335** — confirm 2-methylcitrate synthase identity and formally remove from citrate-synthase step.
3. **scpC / PP_0154** — confirm CoA-transferase role and remove from SCS step.
4. **mqo1/2/3 / PP_0751, PP_1251, PP_2925** — determine paralog division of labour (which is the primary TCA MQO vs. condition-specific); relevant to marking a single primary gene.
5. **acnA / PP_2112 and acnB / PP_2339** — confirm which is the dominant TCA aconitase vs. methylcitrate dehydratase.
6. **pycA/pycB / PP_5347, PP_5346** — PE4 "Predicted"; verify subunit assignment and anaplerotic role.

---

## 9. Evidence Base (Key Literature)

| PMID | Paper (abbrev.) | How it supports / challenges findings |
|---|---|---|
| [24951791](https://pubmed.ncbi.nlm.nih.gov/24951791/) | *Functional structure of central carbon metabolism in P. putida KT2440* | Direct KT2440: places TCA in tightly-regulated, transcriptionally-invariant central metabolism; supports pathway-level (not per-gene) evidence (F006) |
| [12480887](https://pubmed.ncbi.nlm.nih.gov/12480887/) | *MQO essential for growth on ethanol/acetate in P. aeruginosa* | Genus-level: "*NAD-dependent malate dehydrogenase activity could not be detected*" — supports MQO-primary malate node (F001) |
| [21178163](https://pubmed.ncbi.nlm.nih.gov/21178163/) | *Cyanide degradation in P. pseudoalcaligenes CECT5344* | Genus-level: "*Malate dehydrogenase activity was undetectable, but a malate:quinone oxidoreductase activity...was found*" — supports F001 |
| [41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/) | *HexR regulatory landscape in KT2440* | Direct KT2440: glyoxylate-shunt/gluconeogenic rerouting on acetate/succinate — supports separate glyoxylate module (F004, F007) |
| [41390427](https://pubmed.ncbi.nlm.nih.gov/41390427/) | *Ethanol-to-3-HP platform in KT2440* | Direct KT2440: genome-scale model shows dominant glyoxylate-shunt flux and oxaloacetate limitation — supports F004 |
| [38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/) | *ML analysis of RB-TnSeq fitness data, P. putida* | Resource for resolving per-gene functional confidence (F006) — not yet per-gene mined |

**Evidence quality note:** direct KT2440 evidence exists only at the **pathway/flux/regulation level**. The pivotal MQO-vs-NAD-MDH claim is transferred from same-genus *Pseudomonas* biochemistry (strong genus-level, but not KT2440-direct). All 22 core gene calls are homology-inferred (UniProt PE3/PE4).

---

## 10. Limitations and Knowledge Gaps

- **No direct KT2440 protein/transcript evidence.** All core annotations are UniProt PE3 (homology) or PE4 (predicted). Targeted literature searches for KT2440-specific knockout or biochemical phenotypes of *gltA*, *sdh*, *sucAB*, or *mqo* returned no dedicated studies (Finding F006).
- **Species transfer for the MQO claim** rests on *P. aeruginosa* and *P. pseudoalcaligenes* biochemistry, not KT2440 itself. Genus-level transfer is reasonable but not proven for this strain.
- **RB-TnSeq data are available but not per-gene mined here.** Genome-wide fitness data with ML-derived functional modules exist for KT2440 ([PMID: 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/)); these could confirm essentiality/conditional-essentiality of each TCA gene but were not integrated at the individual-gene level.
- **Paralog division of labour** among the three MQOs, three E3s, and three fumarases is unresolved; the module treats each set as collectively covering its step.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Mine existing RB-TnSeq fitness data** ([PMID: 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/)) for per-gene fitness of all 22 core TCA loci across carbon sources — the fastest route to per-gene confidence without new experiments.
2. **Query enzyme-assay literature / BioCyc** for direct KT2440 MQO vs. NAD-MDH activity measurements; if absent, flag as an experimental gap.
3. **Targeted deletion / CRISPRi** of *mdh*/PP_0654 vs. *mqo1/2/3* on succinate/malate/acetate to establish the primary malate-oxidation route in KT2440 directly (CRISPRi toolkits for KT2440 are established — [PMID: 39163848](https://pubmed.ncbi.nlm.nih.gov/39163848/), [PMID: 36158112](https://pubmed.ncbi.nlm.nih.gov/36158112/)).
4. **Curatorial edits**: implement the §7 status assignments; move *prpC*/*scpC* out of the module; add the taxon-note on MQO/NADP-IDH.
5. **Expert question**: confirm whether the three MQO paralogs are functionally redundant or condition-specialized (e.g., stress, alternative electron acceptors).

---

*Report generated from a 5-iteration autonomous review. All KT2440 gene-level conclusions are homology-inferred (UniProt PE3/PE4); species-transfer of the MQO claim is genus-level (P. aeruginosa, P. pseudoalcaligenes). The curation actions in §7–8 are the actionable deliverables.*


## Artifacts

- [OpenScientist final report](PSEPK__tca_cycle__ppu00020-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__tca_cycle__ppu00020-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:24951791
2. PMID:12480887
3. PMID:21178163
4. PMID:41260329
5. PMID:41390427
6. PMID:38323821
7. PMID:39163848
8. PMID:36158112