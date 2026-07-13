---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T12:13:24.258614'
end_time: '2026-07-06T12:35:10.876210'
duration_seconds: 1306.62
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Tricarboxylic acid cycle and central-carbon entry nodes
  module_summary: A taxon-neutral module for the oxidative tricarboxylic acid (TCA)
    cycle and closely coupled entry or anaplerotic reactions. The core cycle oxidizes
    acetyl-CoA-derived carbon through citrate, isocitrate, 2-oxoglutarate, succinyl-CoA,
    succinate, fumarate, malate, and oxaloacetate. Bacterial realizations often include
    multiple malate/oxaloacetate enzymes, quinone- coupled succinate and malate oxidation,
    and adjacent pyruvate dehydrogenase or pyruvate carboxylase nodes that feed acetyl-CoA
    or oxaloacetate into the cycle without being strict cyclic steps.
  module_outline: "- Tricarboxylic acid cycle\n  - 1. acetyl-CoA plus oxaloacetate\
    \ entry\n  - Oxaloacetate and acetyl-CoA to citrate\n    - Citrate synthase (molecular\
    \ player: citrate synthase activity; activity or role: citrate synthase activity)\n\
    \  - 2. citrate to isocitrate\n  - Citrate to isocitrate through cis-aconitate\n\
    \    - Aconitase / aconitate hydratase (molecular player: aconitate hydratase\
    \ activity; activity or role: aconitate hydratase activity)\n  - 3. isocitrate\
    \ oxidative decarboxylation\n  - Isocitrate to 2-oxoglutarate\n    - Alternative\
    \ versions by redox cofactor: Isocitrate dehydrogenase cofactor variants\n   \
    \   - NADP-dependent isocitrate dehydrogenase route\n        - NADP-dependent\
    \ isocitrate dehydrogenase (molecular player: isocitrate dehydrogenase (NADP+)\
    \ activity; activity or role: isocitrate dehydrogenase (NADP+) activity)\n   \
    \   - NAD-dependent isocitrate dehydrogenase route\n        - NAD-dependent isocitrate\
    \ dehydrogenase (molecular player: isocitrate dehydrogenase (NAD+) activity; activity\
    \ or role: isocitrate dehydrogenase (NAD+) activity)\n  - 4. 2-oxoglutarate oxidative\
    \ decarboxylation\n  - 2-oxoglutarate to succinyl-CoA\n    - OGDH E1 oxoglutarate\
    \ dehydrogenase (molecular player: oxoglutarate dehydrogenase (succinyl-transferring)\
    \ activity; activity or role: oxoglutarate dehydrogenase (succinyl-transferring)\
    \ activity)\n    - OGDH E2 dihydrolipoyllysine-residue succinyltransferase (molecular\
    \ player: dihydrolipoyllysine-residue succinyltransferase activity; activity or\
    \ role: dihydrolipoyllysine-residue succinyltransferase activity)\n    - OGDH\
    \ E3 dihydrolipoyl dehydrogenase (molecular player: dihydrolipoyl dehydrogenase\
    \ (NADH) activity; activity or role: dihydrolipoyl dehydrogenase (NADH) activity)\n\
    \  - 5. succinyl-CoA to succinate\n  - Succinyl-CoA synthetase / succinate-CoA\
    \ ligase\n    - Alternative versions by nucleotide specificity: Succinate-CoA\
    \ ligase nucleotide donor variants\n      - ADP-forming succinate-CoA ligase\n\
    \        - ADP-forming succinate-CoA ligase (molecular player: succinate-CoA ligase\
    \ (ADP-forming) activity; activity or role: succinate-CoA ligase (ADP-forming)\
    \ activity)\n      - GDP-forming succinate-CoA ligase\n        - GDP-forming succinate-CoA\
    \ ligase (molecular player: succinate-CoA ligase (GDP-forming) activity; activity\
    \ or role: succinate-CoA ligase (GDP-forming) activity)\n  - 6. succinate to fumarate\n\
    \  - Succinate oxidation through quinone-coupled Complex II\n    - Succinate dehydrogenase\
    \ (quinone) (molecular player: succinate dehydrogenase (quinone) activity; activity\
    \ or role: succinate dehydrogenase (quinone) activity)\n  - 7. fumarate to malate\n\
    \  - Fumarate hydration to L-malate\n    - Fumarate hydratase (molecular player:\
    \ fumarate hydratase activity; activity or role: fumarate hydratase activity)\n\
    \  - 8. malate to oxaloacetate\n  - L-malate oxidation to oxaloacetate\n    -\
    \ Alternative versions by redox acceptor: Malate dehydrogenase electron acceptor\
    \ variants\n      - NAD-dependent malate dehydrogenase\n        - NAD-dependent\
    \ L-malate dehydrogenase (molecular player: L-malate dehydrogenase (NAD+) activity;\
    \ activity or role: L-malate dehydrogenase (NAD+) activity)\n      - Quinone-dependent\
    \ malate:quinone oxidoreductase\n        - Malate:quinone oxidoreductase (molecular\
    \ player: malate:quinone oxidoreductase activity; activity or role: malate:quinone\
    \ oxidoreductase activity)\n  - Alternative versions by pathway boundary: TCA-adjacent\
    \ feeder and anaplerotic nodes\n    - Pyruvate dehydrogenase feeds acetyl-CoA\
    \ into the cycle\n      - Pyruvate dehydrogenase E1 (molecular player: pyruvate\
    \ dehydrogenase (acetyl-transferring) activity; activity or role: pyruvate dehydrogenase\
    \ (acetyl-transferring) activity)\n      - Pyruvate dehydrogenase E2 acetyltransferase\
    \ (molecular player: dihydrolipoyllysine-residue acetyltransferase activity; activity\
    \ or role: dihydrolipoyllysine-residue acetyltransferase activity)\n      - Pyruvate\
    \ dehydrogenase E3 dihydrolipoyl dehydrogenase (molecular player: dihydrolipoyl\
    \ dehydrogenase (NADH) activity; activity or role: dihydrolipoyl dehydrogenase\
    \ (NADH) activity)\n    - Pyruvate carboxylase replenishes oxaloacetate\n    \
    \  - Pyruvate carboxylase (molecular player: pyruvate carboxylase activity; activity\
    \ or role: pyruvate carboxylase activity)\n    - Methylcitrate and propionate-related\
    \ side branch\n      - 2-methylisocitrate dehydratase (molecular player: 2-methylisocitrate\
    \ dehydratase activity; activity or role: 2-methylisocitrate dehydratase activity)"
  module_connections: '- Oxaloacetate and acetyl-CoA to citrate precedes Citrate to
    isocitrate through cis-aconitate

    - Citrate to isocitrate through cis-aconitate precedes Isocitrate to 2-oxoglutarate

    - Isocitrate to 2-oxoglutarate precedes 2-oxoglutarate to succinyl-CoA

    - 2-oxoglutarate to succinyl-CoA precedes Succinyl-CoA synthetase / succinate-CoA
    ligase

    - Succinyl-CoA synthetase / succinate-CoA ligase precedes Succinate oxidation
    through quinone-coupled Complex II

    - Succinate oxidation through quinone-coupled Complex II precedes Fumarate hydration
    to L-malate

    - Fumarate hydration to L-malate precedes L-malate oxidation to oxaloacetate

    - L-malate oxidation to oxaloacetate feeds into Oxaloacetate and acetyl-CoA to
    citrate: Oxaloacetate regenerated from malate is consumed by citrate synthase
    in the next cycle turn.'
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
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PSEPK__tca_cycle__ppu00020-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Tricarboxylic acid cycle and central-carbon entry nodes in Pseudomonas putida KT2440

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

A taxon-neutral module for the oxidative tricarboxylic acid (TCA) cycle and closely coupled entry or anaplerotic reactions. The core cycle oxidizes acetyl-CoA-derived carbon through citrate, isocitrate, 2-oxoglutarate, succinyl-CoA, succinate, fumarate, malate, and oxaloacetate. Bacterial realizations often include multiple malate/oxaloacetate enzymes, quinone- coupled succinate and malate oxidation, and adjacent pyruvate dehydrogenase or pyruvate carboxylase nodes that feed acetyl-CoA or oxaloacetate into the cycle without being strict cyclic steps.

### Provisional Biological Outline

- Tricarboxylic acid cycle
  - 1. acetyl-CoA plus oxaloacetate entry
  - Oxaloacetate and acetyl-CoA to citrate
    - Citrate synthase (molecular player: citrate synthase activity; activity or role: citrate synthase activity)
  - 2. citrate to isocitrate
  - Citrate to isocitrate through cis-aconitate
    - Aconitase / aconitate hydratase (molecular player: aconitate hydratase activity; activity or role: aconitate hydratase activity)
  - 3. isocitrate oxidative decarboxylation
  - Isocitrate to 2-oxoglutarate
    - Alternative versions by redox cofactor: Isocitrate dehydrogenase cofactor variants
      - NADP-dependent isocitrate dehydrogenase route
        - NADP-dependent isocitrate dehydrogenase (molecular player: isocitrate dehydrogenase (NADP+) activity; activity or role: isocitrate dehydrogenase (NADP+) activity)
      - NAD-dependent isocitrate dehydrogenase route
        - NAD-dependent isocitrate dehydrogenase (molecular player: isocitrate dehydrogenase (NAD+) activity; activity or role: isocitrate dehydrogenase (NAD+) activity)
  - 4. 2-oxoglutarate oxidative decarboxylation
  - 2-oxoglutarate to succinyl-CoA
    - OGDH E1 oxoglutarate dehydrogenase (molecular player: oxoglutarate dehydrogenase (succinyl-transferring) activity; activity or role: oxoglutarate dehydrogenase (succinyl-transferring) activity)
    - OGDH E2 dihydrolipoyllysine-residue succinyltransferase (molecular player: dihydrolipoyllysine-residue succinyltransferase activity; activity or role: dihydrolipoyllysine-residue succinyltransferase activity)
    - OGDH E3 dihydrolipoyl dehydrogenase (molecular player: dihydrolipoyl dehydrogenase (NADH) activity; activity or role: dihydrolipoyl dehydrogenase (NADH) activity)
  - 5. succinyl-CoA to succinate
  - Succinyl-CoA synthetase / succinate-CoA ligase
    - Alternative versions by nucleotide specificity: Succinate-CoA ligase nucleotide donor variants
      - ADP-forming succinate-CoA ligase
        - ADP-forming succinate-CoA ligase (molecular player: succinate-CoA ligase (ADP-forming) activity; activity or role: succinate-CoA ligase (ADP-forming) activity)
      - GDP-forming succinate-CoA ligase
        - GDP-forming succinate-CoA ligase (molecular player: succinate-CoA ligase (GDP-forming) activity; activity or role: succinate-CoA ligase (GDP-forming) activity)
  - 6. succinate to fumarate
  - Succinate oxidation through quinone-coupled Complex II
    - Succinate dehydrogenase (quinone) (molecular player: succinate dehydrogenase (quinone) activity; activity or role: succinate dehydrogenase (quinone) activity)
  - 7. fumarate to malate
  - Fumarate hydration to L-malate
    - Fumarate hydratase (molecular player: fumarate hydratase activity; activity or role: fumarate hydratase activity)
  - 8. malate to oxaloacetate
  - L-malate oxidation to oxaloacetate
    - Alternative versions by redox acceptor: Malate dehydrogenase electron acceptor variants
      - NAD-dependent malate dehydrogenase
        - NAD-dependent L-malate dehydrogenase (molecular player: L-malate dehydrogenase (NAD+) activity; activity or role: L-malate dehydrogenase (NAD+) activity)
      - Quinone-dependent malate:quinone oxidoreductase
        - Malate:quinone oxidoreductase (molecular player: malate:quinone oxidoreductase activity; activity or role: malate:quinone oxidoreductase activity)
  - Alternative versions by pathway boundary: TCA-adjacent feeder and anaplerotic nodes
    - Pyruvate dehydrogenase feeds acetyl-CoA into the cycle
      - Pyruvate dehydrogenase E1 (molecular player: pyruvate dehydrogenase (acetyl-transferring) activity; activity or role: pyruvate dehydrogenase (acetyl-transferring) activity)
      - Pyruvate dehydrogenase E2 acetyltransferase (molecular player: dihydrolipoyllysine-residue acetyltransferase activity; activity or role: dihydrolipoyllysine-residue acetyltransferase activity)
      - Pyruvate dehydrogenase E3 dihydrolipoyl dehydrogenase (molecular player: dihydrolipoyl dehydrogenase (NADH) activity; activity or role: dihydrolipoyl dehydrogenase (NADH) activity)
    - Pyruvate carboxylase replenishes oxaloacetate
      - Pyruvate carboxylase (molecular player: pyruvate carboxylase activity; activity or role: pyruvate carboxylase activity)
    - Methylcitrate and propionate-related side branch
      - 2-methylisocitrate dehydratase (molecular player: 2-methylisocitrate dehydratase activity; activity or role: 2-methylisocitrate dehydratase activity)

### Known Relationships Among Steps

- Oxaloacetate and acetyl-CoA to citrate precedes Citrate to isocitrate through cis-aconitate
- Citrate to isocitrate through cis-aconitate precedes Isocitrate to 2-oxoglutarate
- Isocitrate to 2-oxoglutarate precedes 2-oxoglutarate to succinyl-CoA
- 2-oxoglutarate to succinyl-CoA precedes Succinyl-CoA synthetase / succinate-CoA ligase
- Succinyl-CoA synthetase / succinate-CoA ligase precedes Succinate oxidation through quinone-coupled Complex II
- Succinate oxidation through quinone-coupled Complex II precedes Fumarate hydration to L-malate
- Fumarate hydration to L-malate precedes L-malate oxidation to oxaloacetate
- L-malate oxidation to oxaloacetate feeds into Oxaloacetate and acetyl-CoA to citrate: Oxaloacetate regenerated from malate is consumed by citrate synthase in the next cycle turn.

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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Tricarboxylic acid cycle and central-carbon entry nodes in Pseudomonas putida KT2440

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

A taxon-neutral module for the oxidative tricarboxylic acid (TCA) cycle and closely coupled entry or anaplerotic reactions. The core cycle oxidizes acetyl-CoA-derived carbon through citrate, isocitrate, 2-oxoglutarate, succinyl-CoA, succinate, fumarate, malate, and oxaloacetate. Bacterial realizations often include multiple malate/oxaloacetate enzymes, quinone- coupled succinate and malate oxidation, and adjacent pyruvate dehydrogenase or pyruvate carboxylase nodes that feed acetyl-CoA or oxaloacetate into the cycle without being strict cyclic steps.

### Provisional Biological Outline

- Tricarboxylic acid cycle
  - 1. acetyl-CoA plus oxaloacetate entry
  - Oxaloacetate and acetyl-CoA to citrate
    - Citrate synthase (molecular player: citrate synthase activity; activity or role: citrate synthase activity)
  - 2. citrate to isocitrate
  - Citrate to isocitrate through cis-aconitate
    - Aconitase / aconitate hydratase (molecular player: aconitate hydratase activity; activity or role: aconitate hydratase activity)
  - 3. isocitrate oxidative decarboxylation
  - Isocitrate to 2-oxoglutarate
    - Alternative versions by redox cofactor: Isocitrate dehydrogenase cofactor variants
      - NADP-dependent isocitrate dehydrogenase route
        - NADP-dependent isocitrate dehydrogenase (molecular player: isocitrate dehydrogenase (NADP+) activity; activity or role: isocitrate dehydrogenase (NADP+) activity)
      - NAD-dependent isocitrate dehydrogenase route
        - NAD-dependent isocitrate dehydrogenase (molecular player: isocitrate dehydrogenase (NAD+) activity; activity or role: isocitrate dehydrogenase (NAD+) activity)
  - 4. 2-oxoglutarate oxidative decarboxylation
  - 2-oxoglutarate to succinyl-CoA
    - OGDH E1 oxoglutarate dehydrogenase (molecular player: oxoglutarate dehydrogenase (succinyl-transferring) activity; activity or role: oxoglutarate dehydrogenase (succinyl-transferring) activity)
    - OGDH E2 dihydrolipoyllysine-residue succinyltransferase (molecular player: dihydrolipoyllysine-residue succinyltransferase activity; activity or role: dihydrolipoyllysine-residue succinyltransferase activity)
    - OGDH E3 dihydrolipoyl dehydrogenase (molecular player: dihydrolipoyl dehydrogenase (NADH) activity; activity or role: dihydrolipoyl dehydrogenase (NADH) activity)
  - 5. succinyl-CoA to succinate
  - Succinyl-CoA synthetase / succinate-CoA ligase
    - Alternative versions by nucleotide specificity: Succinate-CoA ligase nucleotide donor variants
      - ADP-forming succinate-CoA ligase
        - ADP-forming succinate-CoA ligase (molecular player: succinate-CoA ligase (ADP-forming) activity; activity or role: succinate-CoA ligase (ADP-forming) activity)
      - GDP-forming succinate-CoA ligase
        - GDP-forming succinate-CoA ligase (molecular player: succinate-CoA ligase (GDP-forming) activity; activity or role: succinate-CoA ligase (GDP-forming) activity)
  - 6. succinate to fumarate
  - Succinate oxidation through quinone-coupled Complex II
    - Succinate dehydrogenase (quinone) (molecular player: succinate dehydrogenase (quinone) activity; activity or role: succinate dehydrogenase (quinone) activity)
  - 7. fumarate to malate
  - Fumarate hydration to L-malate
    - Fumarate hydratase (molecular player: fumarate hydratase activity; activity or role: fumarate hydratase activity)
  - 8. malate to oxaloacetate
  - L-malate oxidation to oxaloacetate
    - Alternative versions by redox acceptor: Malate dehydrogenase electron acceptor variants
      - NAD-dependent malate dehydrogenase
        - NAD-dependent L-malate dehydrogenase (molecular player: L-malate dehydrogenase (NAD+) activity; activity or role: L-malate dehydrogenase (NAD+) activity)
      - Quinone-dependent malate:quinone oxidoreductase
        - Malate:quinone oxidoreductase (molecular player: malate:quinone oxidoreductase activity; activity or role: malate:quinone oxidoreductase activity)
  - Alternative versions by pathway boundary: TCA-adjacent feeder and anaplerotic nodes
    - Pyruvate dehydrogenase feeds acetyl-CoA into the cycle
      - Pyruvate dehydrogenase E1 (molecular player: pyruvate dehydrogenase (acetyl-transferring) activity; activity or role: pyruvate dehydrogenase (acetyl-transferring) activity)
      - Pyruvate dehydrogenase E2 acetyltransferase (molecular player: dihydrolipoyllysine-residue acetyltransferase activity; activity or role: dihydrolipoyllysine-residue acetyltransferase activity)
      - Pyruvate dehydrogenase E3 dihydrolipoyl dehydrogenase (molecular player: dihydrolipoyl dehydrogenase (NADH) activity; activity or role: dihydrolipoyl dehydrogenase (NADH) activity)
    - Pyruvate carboxylase replenishes oxaloacetate
      - Pyruvate carboxylase (molecular player: pyruvate carboxylase activity; activity or role: pyruvate carboxylase activity)
    - Methylcitrate and propionate-related side branch
      - 2-methylisocitrate dehydratase (molecular player: 2-methylisocitrate dehydratase activity; activity or role: 2-methylisocitrate dehydratase activity)

### Known Relationships Among Steps

- Oxaloacetate and acetyl-CoA to citrate precedes Citrate to isocitrate through cis-aconitate
- Citrate to isocitrate through cis-aconitate precedes Isocitrate to 2-oxoglutarate
- Isocitrate to 2-oxoglutarate precedes 2-oxoglutarate to succinyl-CoA
- 2-oxoglutarate to succinyl-CoA precedes Succinyl-CoA synthetase / succinate-CoA ligase
- Succinyl-CoA synthetase / succinate-CoA ligase precedes Succinate oxidation through quinone-coupled Complex II
- Succinate oxidation through quinone-coupled Complex II precedes Fumarate hydration to L-malate
- Fumarate hydration to L-malate precedes L-malate oxidation to oxaloacetate
- L-malate oxidation to oxaloacetate feeds into Oxaloacetate and acetyl-CoA to citrate: Oxaloacetate regenerated from malate is consumed by citrate synthase in the next cycle turn.

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

# Tricarboxylic Acid Cycle and Central-Carbon Entry Nodes in *Pseudomonas putida* KT2440: A Species-Aware Module Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 (NCBI taxon 160488, proteome UP000000556) encodes a complete oxidative TCA cycle with several notable features: (i) a large PP_4185–PP_4194 gene cluster encoding the 2-oxoglutarate dehydrogenase complex (sucAB/lpdG), succinate-CoA ligase (sucCD), succinate dehydrogenase (sdhABCD), and citrate synthase (gltA); (ii) three malate:quinone oxidoreductase (MQO) paralogs plus a canonical NAD-dependent malate dehydrogenase; (iii) three fumarase paralogs (one class I, two class II); (iv) two NADP-dependent isocitrate dehydrogenase paralogs (icd/idh); and (v) well-characterized pyruvate dehydrogenase and pyruvate carboxylase entry/anaplerotic nodes. Of the 30 candidate genes provided, approximately 20 are high-confidence core TCA or entry-node assignments, while several others belong to the methylcitrate cycle (prpC, acnB, scpC), represent paralog redundancy with unresolved isoform-specific roles (mqo1-3, fumC paralogs), or are likely over-propagated annotations (acoC, lpdV). The pathway is fully satisfiable in this organism, with all eight canonical TCA steps covered by at least one high-confidence gene.

## 2. Target-Organism Pathway Definition

### 2.1 Pathway Scope

The module encompasses the eight-step oxidative TCA cycle converting acetyl-CoA through citrate, isocitrate, 2-oxoglutarate, succinyl-CoA, succinate, fumarate, malate, and oxaloacetate, plus the immediately adjacent feeder reactions:

- **Pyruvate dehydrogenase complex (PDH)**: irreversible decarboxylation of pyruvate to acetyl-CoA (moreno2024inactivationofpseudomonas pages 4-5, moreno2024inactivationofpseudomonas pages 7-9).
- **Pyruvate carboxylase (Pyc)**: anaplerotic carboxylation of pyruvate to oxaloacetate, providing 16–45% of oxaloacetate depending on carbon source (zhou2025quantitativedecodingof pages 5-7, sudarsan2014thefunctionalstructure pages 8-10).

### 2.2 Neighboring Pathways to Keep Separate

- **Glyoxylate shunt** (aceA/glcB): bypasses the two decarboxylation steps; highly active during growth on aromatics (~85% of isocitrate flux on benzoate) but minimal on glucose (sudarsan2014thefunctionalstructure pages 8-10, sudarsan2014thefunctionalstructure pages 7-8). Not part of the core oxidative cycle.
- **Methylcitrate cycle** (prpC, prpB, acnB/acnD, prpD, prpF): propionate detoxification pathway; shares enzyme families with TCA but is functionally distinct (dolan2022systemswidedissectionof pages 2-4).
- **Pentose phosphate pathway and EDEMP cycle**: glucose catabolism upstream of pyruvate.
- **Oxidative phosphorylation**: electron transport downstream of SDH/MQO quinone reduction.

### 2.3 Alternate Names and Database Definitions

KEGG ppu00020 ("Citrate cycle (TCA cycle)") includes core cycle enzymes plus some entry nodes. The module as defined here extends to include pyruvate dehydrogenase (KEGG ppu00785) and pyruvate carboxylase, consistent with the working scope. BioCyc/MetaCyc defines the P. putida TCA cycle similarly but sometimes separates SDH into respiratory complex II.

## 3. Expected Step Model

### Step 1: Acetyl-CoA + Oxaloacetate → Citrate (Citrate synthase)
**Primary gene: gltA (PP_4194)**. High confidence. Located in the large PP_4185–PP_4194 TCA cluster. Overexpression of gltA in P. putida increases succinate production from acetate, confirming its functional role as the primary citrate synthase (sudarsan2014thefunctionalstructure pages 6-7). **Status: COVERED.**

**prpC (PP_2335)** is annotated as "citrate synthase" but is most likely a 2-methylcitrate synthase functioning in propionate metabolism, as demonstrated for the homologous PrpC in *P. aeruginosa* where it condenses propionyl-CoA with oxaloacetate (dolan2022systemswidedissectionof pages 2-4). It may have residual citrate synthase activity (as shown by suppressor mutations in *P. aeruginosa* gltA knockouts), but should not satisfy the core TCA citrate synthase step. **Status: methylcitrate side branch; candidate_uncertain for TCA core.**

### Step 2: Citrate → Isocitrate (Aconitase)
**Primary gene: acnA-I (PP_2112)**. High confidence. Proteomically detected and differentially expressed across carbon sources in KT2440 (nikel2014metabolicandregulatory pages 38-42, sudarsan2014thefunctionalstructure pages 6-7). Functions as a canonical aconitate hydratase.

**acnB (PP_2339)** carries dual EC annotations (4.2.1.3 and 4.2.1.99, 2-methylisocitrate dehydratase). By analogy to the *P. aeruginosa* methylcitrate cycle organization, acnB likely primarily serves the methylcitrate pathway, rehydrating 2-methylaconitate (dolan2022systemswidedissectionof pages 2-4). It may contribute to TCA aconitase activity under some conditions but represents paralog ambiguity. **Status: COVERED by acnA-I; acnB is candidate_uncertain for core TCA.**

### Step 3: Isocitrate → 2-Oxoglutarate (Isocitrate dehydrogenase)
**Primary gene: icd (PP_4011)**. High confidence. Enzymatic characterization shows ~89% NADP+ preference under quasi-in-vivo conditions (nikel2015pseudomonasputidakt2440 pages 21-25). Routinely included in all KT2440 flux models and transcriptomic/proteomic studies (sudarsan2014thefunctionalstructure pages 6-7).

**idh (PP_4012)** is a second NADP-dependent isocitrate dehydrogenase. Proteomic detection shows it is expressed and responsive to stress conditions (>2-fold downregulation under GraT toxin stress) (ainelo2019pseudomonasputidaresponds pages 5-9). The two genes are adjacent, suggesting a tandem duplication. Specific contribution of each isoform to total flux is unresolved. **Status: COVERED by icd; idh is a confirmed expressed paralog.**

*Note: P. putida KT2440 lacks a dedicated NAD-dependent isocitrate dehydrogenase; both isoforms are NADP-dependent.* **NAD-dependent IDH route: not_expected_in_target_taxon.**

### Step 4: 2-Oxoglutarate → Succinyl-CoA (OGDH complex)
**sucA (PP_4189, E1)**: High confidence. Proteomically identified; downregulated under GraT stress (ainelo2019pseudomonasputidaresponds pages 5-9, sudarsan2014thefunctionalstructure pages 6-7).
**sucB (PP_4188, E2)**: High confidence. Canonical succinyltransferase in the suc cluster (sudarsan2014thefunctionalstructure pages 6-7).
**lpdG (PP_4187, E3)**: High confidence for OGDH-associated E3 based on genomic colocalization (sudarsan2014thefunctionalstructure pages 6-7, nikel2014metabolicandregulatory pages 38-42). **Status: COVERED.**

### Step 5: Succinyl-CoA → Succinate (Succinate-CoA ligase)
**sucD (PP_4185, α-subunit)** and **sucC (PP_4186, β-subunit)**: High confidence. Both are ADP-forming (EC 6.2.1.5), proteomically detected, and part of the conserved TCA cluster (nikel2014metabolicandregulatory pages 38-42, ainelo2019pseudomonasputidaresponds pages 5-9). **GDP-forming variant: not_expected_in_target_taxon** (no genomic evidence). **Status: COVERED.**

### Step 6: Succinate → Fumarate (Succinate dehydrogenase / Complex II)
**sdhA (PP_4191)**, **sdhB (PP_4190)**, **sdhC (PP_4193)**, **sdhD (PP_4192)**: High confidence. Four-subunit quinone-coupled complex; all genes in the central TCA cluster (sudarsan2014thefunctionalstructure pages 6-7). **Status: COVERED.**

### Step 7: Fumarate → Malate (Fumarate hydratase)
Three paralogs exist:
- **PP_0897**: Class I (iron-sulfur) fumarase. Recent work demonstrates it is not universally essential but becomes critical for growth on aromatic carbon sources such as p-coumarate in engineered strain backgrounds. Deletion causes nutrient auxotrophy and reveals additional functions beyond canonical fumarase activity (banerjee2025addressinggenomescale pages 1-2, banerjee2025addressinggenomescale pages 8-9, banerjee2025addressinggenomescale pages 5-7, banerjee2025addressinggenomescale pages 7-8).
- **fumC-I (PP_0944)**: Class II fumarase. Earlier metabolic model work noted possible nonfunctionality or misannotation (puchałka2008genomescalereconstructionand pages 9-10).
- **fumC (PP_1755)**: Class II fumarase. Similarly uncertain contribution.

The redundancy among three fumarase paralogs makes single-gene knockouts non-lethal under standard conditions (puchałka2008genomescalereconstructionand pages 9-10). However, PP_0897 has the strongest direct experimental support for physiological relevance. **Status: COVERED (with paralog ambiguity); PP_0897 recommended for full review.**

### Step 8: Malate → Oxaloacetate (Malate dehydrogenase / MQO)
This step has the most complex paralog situation in KT2440:
- **mdh (PP_0654)**: NAD-dependent malate dehydrogenase. Present in genome annotations and metabolic models (sudarsan2014thefunctionalstructure pages 6-7).
- **mqo1 (PP_0751)**, **mqo2 (PP_1251)**, **mqo3 (PP_2925)**: Three malate:quinone oxidoreductases. mqo2 expression is regulated by the Crc global regulator, with levels increasing in a crc mutant (morales2004thepseudomonasputida pages 3-4). In *P. aeruginosa*, MQO is essential for growth on ethanol/acetate (morales2004thepseudomonasputida pages 3-4).

The relative contribution of NAD-MDH versus MQO to physiological malate oxidation is unresolved in KT2440. In many pseudomonads, MQO is considered the primary route due to thermodynamic favorability of quinone-coupled oxidation. **Status: COVERED (with significant paralog ambiguity); isoform-specific roles need resolution.**

### Entry Node A: Pyruvate → Acetyl-CoA (Pyruvate dehydrogenase)
**aceE (PP_0339, E1)** and **aceF (PP_0338, E2)**: High confidence. Inactivation of aceE abolishes growth on glucose, citrate, succinate, and pyruvate as sole carbon sources, demonstrating its essential role for acetyl-CoA supply (moreno2024inactivationofpseudomonas pages 4-5, moreno2024inactivationofpseudomonas pages 7-9). The PDH-null strain can only grow on compounds that directly generate acetyl-CoA (moreno2024inactivationofpseudomonas pages 7-9).

**E3 subunit assignment**: Three dihydrolipoyl dehydrogenase paralogs exist—lpdG (PP_4187), lpdV (PP_4404), and lpd (PP_5366). lpdG is genomically colocalized with the OGDH complex. The E3 subunit serving the PDH complex is likely lpd (PP_5366) or shared with lpdG, but isoform-specific assignment lacks direct experimental resolution in KT2440. **lpdV (PP_4404)** is annotated in the branched-chain amino acid dehydrogenase context and is likely over-propagated if assigned to PDH or TCA entry. **Status: COVERED; E3 paralog assignment needs review.**

**acoC (PP_0553)**: Annotated as dihydrolipoyllysine-residue acetyltransferase of the acetoin cleaving system. Despite sharing EC 2.3.1.12 with aceF, this enzyme functions in acetoin metabolism, not pyruvate dehydrogenation. **Status: likely over-annotation for TCA/PDH; should not satisfy PDH E2 step.**

### Entry Node B: Pyruvate → Oxaloacetate (Pyruvate carboxylase)
**pycB (PP_5346)** and **pycA (PP_5347)**: High confidence. The two-subunit pyruvate carboxylase is strongly upregulated (up to 30-fold) during growth on aromatic/phenolic compounds, where 30–45% of oxaloacetate derives from pyruvate carboxylation (zhou2025quantitativeanalysisof pages 1-3, zhou2025quantitativedecodingof pages 5-7). During glucose growth, the anaplerotic flux is lower but still present (sudarsan2014thefunctionalstructure pages 8-10). Genes are upregulated ~2-fold when PDH is inactivated, demonstrating compensatory anaplerosis (moreno2024inactivationofpseudomonas pages 4-5). **Status: COVERED.**

### Methylcitrate Side Branch
**scpC (PP_0154)**: Propionyl-CoA:succinate CoA transferase. This enzyme participates in propionate metabolism, not the core TCA cycle. Its inclusion in KEGG ppu00020 is likely due to broad pathway mapping. **Status: not core TCA; methylcitrate/propionate side branch.**

## 4. Candidate Genes and Evidence Summary

The following table provides a comprehensive assessment of all 30 candidate genes:

| Step | Gene name | Locus tag | UniProt | EC number | Primary role | Evidence type | Confidence | Curation notes |
|---|---|---|---|---|---|---|---|---|
| Acetyl-CoA + oxaloacetate → citrate | gltA | PP_4194 | Q88FA4 | 2.3.3.1 | TCA core | direct experiment / database | high | Best-supported citrate synthase for core oxidative TCA cycle in KT2440; overexpression alters citrate-cycle flux and succinate production from acetate; colocated with suc/sdh cluster, consistent with core role (sudarsan2014thefunctionalstructure pages 6-7, banerjee2025addressinggenomescale pages 1-2) |
| Acetyl-CoA + oxaloacetate → citrate | prpC | PP_2335 | Q88KF5 | 2.3.3.5 / 2.3.3.1? | methylcitrate | homology / database | medium | Likely 2-methylcitrate synthase for propionyl-CoA assimilation, not primary TCA citrate synthase; may have weak or latent citrate synthase side activity as seen in other pseudomonads, but should not satisfy core TCA step by default in KT2440 (dolan2022systemswidedissectionof pages 2-4) |
| Citrate ↔ cis-aconitate ↔ isocitrate | acnA-I | PP_2112 | Q88L24 | 4.2.1.3 | TCA core / paralog | direct experiment / database | high | Experimentally observed as aconitate hydratase in KT2440 central metabolism; strongly expressed under some carbon regimes; clear TCA-cycle assignment (nikel2014metabolicandregulatory pages 38-42, sudarsan2014thefunctionalstructure pages 6-7) |
| Citrate ↔ cis-aconitate ↔ isocitrate | acnB | PP_2339 | Q88KF1 | 4.2.1.3; 4.2.1.99 | methylcitrate / paralog | homology / database | medium | Broad annotation likely conflates aconitase with 2-methylisocitrate dehydratase-like function; by analogy to other pseudomonads, probably linked more to propionate/methylcitrate metabolism than to primary TCA flux; needs targeted review (dolan2022systemswidedissectionof pages 2-4) |
| Isocitrate → 2-oxoglutarate | icd | PP_4011 | Q88FS2 | 1.1.1.42 | TCA core | direct experiment / database | high | Main NADP-dependent isocitrate dehydrogenase represented in metabolic/enzymatic datasets; cofactor specificity measured (~89% NADP preference) and repeatedly included in KT2440 flux models (nikel2015pseudomonasputidakt2440 pages 21-25, sudarsan2014thefunctionalstructure pages 6-7) |
| Isocitrate → 2-oxoglutarate | idh | PP_4012 | Q88FS1 | 1.1.1.42 | TCA core / paralog | direct experiment / database | medium | Protein named Idh is detected in KT2440 proteomics and responds to stress, indicating expression; specific contribution versus Icd remains unresolved, so paralog ambiguity remains (ainelo2019pseudomonasputidaresponds pages 5-9, sudarsan2014thefunctionalstructure pages 6-7) |
| 2-Oxoglutarate → succinyl-CoA | sucA | PP_4189 | Q88FA9 | 1.2.4.2 | TCA core | direct experiment / database | high | Canonical E1 of 2-oxoglutarate dehydrogenase complex; included in core central-carbon reconstructions and proteomics-based TCA regulation studies (sudarsan2014thefunctionalstructure pages 6-7, ainelo2019pseudomonasputidaresponds pages 5-9) |
| 2-Oxoglutarate → succinyl-CoA | sucB | PP_4188 | Q88FB0 | 2.3.1.61 | TCA core | database / operon context | high | Canonical E2 succinyltransferase of OGDH complex; strong support from conserved cluster organization with sucA/lpdG/sucCD/sdh/gltA in KT2440 models (sudarsan2014thefunctionalstructure pages 6-7) |
| 2-Oxoglutarate → succinyl-CoA | lpdG | PP_4187 | Q88FB1 | 1.8.1.4 | TCA core / shared E3 | direct experiment / database | high | Most likely E3 supplying the OGDH complex because of genomic colocalization in the suc cluster; direct proteomic identification in KT2440 supports expression, though E3 sharing among complexes remains a curation caveat (nikel2014metabolicandregulatory pages 38-42, sudarsan2014thefunctionalstructure pages 6-7) |
| Succinyl-CoA ↔ succinate | sucD | PP_4185 | Q88FB3 | 6.2.1.5 | TCA core | direct experiment / database | high | Canonical succinate-CoA ligase alpha subunit; detected/used in KT2440 central metabolism studies and stress proteomics (nikel2014metabolicandregulatory pages 38-42, ainelo2019pseudomonasputidaresponds pages 5-9) |
| Succinyl-CoA ↔ succinate | sucC | PP_4186 | Q88FB2 | 6.2.1.5 | TCA core | direct experiment / database | high | Canonical succinate-CoA ligase beta subunit; assigned in KT2440 pathway reconstructions and expression studies (nikel2014metabolicandregulatory pages 38-42, sudarsan2014thefunctionalstructure pages 6-7) |
| Succinate → fumarate | sdhA | PP_4191 | Q88FA7 | 1.3.5.1 | TCA core | database / model / operon context | high | Canonical flavoprotein subunit of succinate dehydrogenase; part of well-supported sdhABCD block in central carbon models for KT2440 (sudarsan2014thefunctionalstructure pages 6-7) |
| Succinate → fumarate | sdhB | PP_4190 | Q88FA8 | 1.3.5.1 | TCA core | database / model / operon context | high | Canonical Fe-S subunit of succinate dehydrogenase; part of TCA/respiratory complex II locus (sudarsan2014thefunctionalstructure pages 6-7) |
| Succinate → fumarate | sdhC | PP_4193 | Q88FA5 | 1.3.5.1 | TCA core | database / model / operon context | high | Membrane/cytochrome b subunit of complex II; routinely included in KT2440 TCA cycle maps (sudarsan2014thefunctionalstructure pages 6-7) |
| Succinate → fumarate | sdhD | PP_4192 | Q88FA6 | 1.3.5.1 | TCA core | database / model / operon context | high | Membrane anchor subunit of complex II; supports quinone-linked succinate oxidation in aerobic TCA operation (sudarsan2014thefunctionalstructure pages 6-7) |
| Fumarate ↔ malate | PP_0897 | PP_0897 | Q88PF3 | 4.2.1.2 | TCA core / paralog | direct experiment / database | high | Class I fumarase candidate with strong recent functional evidence: not universally essential, but required in some engineered/aromatic-growth contexts; under-characterized and should be promoted to full review (puchałka2008genomescalereconstructionand pages 9-10, banerjee2025addressinggenomescale pages 5-7) |
| Fumarate ↔ malate | fumC-I | PP_0944 | Q88PA6 | 4.2.1.2 | paralog | database / homology | medium | Class II fumarase paralog; older model work suggested possible nonfunctionality or misannotation when PP_0897 deletion lacked phenotype under acetate conditions, but redundancy remains plausible (puchałka2008genomescalereconstructionand pages 9-10) |
| Fumarate ↔ malate | fumC | PP_1755 | Q88M20 | 4.2.1.2 | paralog | database / homology | medium | Second class II fumarase paralog; likely contributes conditionally or redundantly; exact substrate/condition specificity unresolved in KT2440 (puchałka2008genomescalereconstructionand pages 9-10) |
| Malate → oxaloacetate | mdh | PP_0654 | Q88Q44 | 1.1.1.37 | paralog | database / model | medium | NAD-dependent malate dehydrogenase is encoded and present in central metabolic reconstructions, but multiple MQO paralogs complicate assignment of the dominant physiological malate-oxidizing route (sudarsan2014thefunctionalstructure pages 6-7) |
| Malate → oxaloacetate | mqo1 | PP_0751 | Q88PU7 | 1.1.5.4 | TCA core / paralog | database / model | medium | One of three malate:quinone oxidoreductases encoded in KT2440; central models include MQO activity, but isoform-specific functional ranking is unresolved (sudarsan2014thefunctionalstructure pages 6-7) |
| Malate → oxaloacetate | mqo2 | PP_1251 | Q88NF9 | 1.1.5.4 | TCA core / paralog | direct experiment / database | medium | Expressed protein under Crc control; regulation demonstrated, but not enough direct evidence to call it the sole/primary malate oxidation enzyme in TCA (morales2004thepseudomonasputida pages 3-4) |
| Malate → oxaloacetate | mqo3 | PP_2925 | Q88IS4 | 1.1.5.4 | TCA core / paralog | database / model | medium | Third MQO paralog; likely contributes redundancy or condition-specific function; needs full gene-level curation with transcript/proteome evidence (sudarsan2014thefunctionalstructure pages 6-7) |
| Pyruvate → acetyl-CoA | aceE | PP_0339 | Q88QZ5 | 1.2.4.1 | entry node | direct experiment | high | Pyruvate dehydrogenase E1; aceE knockout abolishes growth on glucose and other pyruvate-generating substrates, showing major acetyl-CoA entry into TCA (moreno2024inactivationofpseudomonas pages 4-5, moreno2024inactivationofpseudomonas pages 7-9) |
| Pyruvate → acetyl-CoA | aceF | PP_0338 | Q88QZ6 | 2.3.1.12 | entry node | direct experiment / homology | high | PDH E2 acetyltransferase partner of AceE; strong inference from canonical PDH architecture and aceE mutant study context in KT2440 (moreno2024inactivationofpseudomonas pages 4-5, sudarsan2014thefunctionalstructure pages 7-8) |
| Pyruvate → acetyl-CoA | lpd | PP_5366 | Q88C17 | 1.8.1.4 | entry node / shared E3 | homology / database | medium | Likely one of several E3 dihydrolipoyl dehydrogenases that can serve pyruvate dehydrogenase; paralog ambiguity with lpdG and lpdV prevents unqualified assignment (moreno2024inactivationofpseudomonas pages 4-5) |
| Pyruvate → acetyl-CoA | lpdV | PP_4404 | Q88EP9 | 1.8.1.4 | entry node / shared E3 paralog | homology / database | low | Additional E3 paralog without direct step-specific evidence for PDH or OGDH participation in KT2440; likely over-propagated if assigned automatically to TCA entry (moreno2024inactivationofpseudomonas pages 4-5) |
| Acetoin cleavage / pyruvate-related acetyl transfer | acoC | PP_0553 | Q88QE1 | 2.3.1.12 | over-annotated / non-TCA | database | low | Acetoin-cleaving system component; same EC as PDH E2 but not evidence for core pyruvate dehydrogenase or TCA function; should not satisfy TCA entry step (moreno2024inactivationofpseudomonas pages 4-5) |
| Pyruvate → oxaloacetate | pycB | PP_5346 | Q88C37 | 6.4.1.1 | entry node / anaplerotic | direct experiment / fluxomics | high | Pyruvate carboxylase subunit supporting anaplerotic refill of oxaloacetate; pycAB upregulated in PDH mutant and strong flux through Pyc documented in aromatic growth studies (moreno2024inactivationofpseudomonas pages 4-5, zhou2025quantitativedecodingof pages 5-7) |
| Pyruvate → oxaloacetate | pycA | PP_5347 | Q88C36 | 6.4.1.1 (complex subunit) | entry node / anaplerotic | direct experiment / fluxomics | high | Biotin carboxylase subunit of pyruvate carboxylase; together with PycB supports 30-45% oxaloacetate derivation from pyruvate during phenolic growth and lower but present anaplerosis on sugars (zhou2025quantitativedecodingof pages 5-7, sudarsan2014thefunctionalstructure pages 8-10) |
| Propionyl-CoA/propionate side branch | scpC | PP_0154 | Q88RH5 | 2.8.3.- | methylcitrate / non-core side branch | database / homology | low | Propionyl-CoA:succinate CoA transferase fits propionate/methylcitrate metabolism, not oxidative TCA cycle core; likely over-included in KEGG bucket (dolan2022systemswidedissectionof pages 2-4) |


*Table: This table maps all 30 candidate genes from the brief to oxidative TCA-cycle steps, adjacent entry nodes, or likely off-pathway side branches in Pseudomonas putida KT2440. It is designed to support manual curation by separating high-confidence core assignments from paralogs, methylcitrate genes, and probable over-annotations.*

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Gaps
- **No NAD-dependent isocitrate dehydrogenase**: KT2440 relies exclusively on NADP-dependent isoforms (icd, idh). The NAD-dependent IDH alternative in the generic module should be marked **not_expected_in_target_taxon** (nikel2015pseudomonasputidakt2440 pages 21-25).
- **No GDP-forming succinate-CoA ligase**: Only the ADP-forming variant (sucCD) is present. The GDP-forming alternative should be marked **not_expected_in_target_taxon**.

### 5.2 Major Paralog Ambiguities
- **Malate oxidation (mdh vs. mqo1/2/3)**: Four enzymes potentially catalyze the same step. Isoform-specific contributions are unresolved. Condition-dependent regulation (Crc control of mqo2) suggests differential roles (morales2004thepseudomonasputida pages 3-4).
- **Fumarase (PP_0897 vs. fumC-I vs. fumC)**: Three paralogs with overlapping function. PP_0897 has the strongest experimental support but the other two lack clear functional characterization (puchałka2008genomescalereconstructionand pages 9-10, banerjee2025addressinggenomescale pages 1-2).
- **Aconitase (acnA-I vs. acnB)**: acnA-I is the primary TCA aconitase; acnB likely serves primarily in the methylcitrate cycle (dolan2022systemswidedissectionof pages 2-4, nikel2014metabolicandregulatory pages 38-42).
- **Isocitrate dehydrogenase (icd vs. idh)**: Both are expressed NADP-dependent isoforms; relative flux contributions unresolved (ainelo2019pseudomonasputidaresponds pages 5-9, nikel2015pseudomonasputidakt2440 pages 21-25).
- **E3 dihydrolipoyl dehydrogenase (lpdG vs. lpd vs. lpdV)**: Three paralogs potentially shared between PDH, OGDH, and branched-chain keto acid dehydrogenase complexes.

### 5.3 Likely Over-Annotations
- **acoC (PP_0553)**: Acetoin cleaving system E2, not PDH E2. Should not satisfy TCA entry node despite shared EC number.
- **lpdV (PP_4404)**: Branched-chain amino acid dehydrogenase E3; assignment to TCA/PDH pathways is likely over-propagated.
- **scpC (PP_0154)**: Propionate metabolism enzyme, not core TCA.
- **prpC (PP_2335)**: Methylcitrate synthase, not primary citrate synthase (dolan2022systemswidedissectionof pages 2-4).

## 6. Module and GO-Curation Recommendations

### 6.1 Step Coverage Status

| Module Step | Status | Notes |
|---|---|---|
| Citrate synthase | **covered** | gltA (PP_4194) |
| Aconitase | **covered** | acnA-I (PP_2112) |
| Isocitrate dehydrogenase (NADP) | **covered** | icd (PP_4011), idh (PP_4012) |
| Isocitrate dehydrogenase (NAD) | **not_expected_in_target_taxon** | No NAD-IDH encoded |
| OGDH complex | **covered** | sucA/sucB/lpdG |
| Succinate-CoA ligase (ADP) | **covered** | sucC/sucD |
| Succinate-CoA ligase (GDP) | **not_expected_in_target_taxon** | Not encoded |
| Succinate dehydrogenase | **covered** | sdhABCD |
| Fumarate hydratase | **covered** (paralog ambiguity) | PP_0897, fumC-I, fumC |
| Malate dehydrogenase (NAD) | **candidate_uncertain** | mdh present but MQO may dominate |
| Malate:quinone oxidoreductase | **covered** (paralog ambiguity) | mqo1/2/3 |
| Pyruvate dehydrogenase | **covered** | aceE/aceF; E3 paralog uncertain |
| Pyruvate carboxylase | **covered** | pycA/pycB |
| Methylcitrate branch | **module_needs_revision** | prpC, acnB, scpC should be in separate methylcitrate module |

### 6.2 Module Boundary Recommendations
- The generic module correctly includes PDH and pyruvate carboxylase as entry nodes.
- The methylcitrate-related genes (prpC, acnB, scpC) should be assigned to a separate methylcitrate cycle module rather than TCA core.
- The three MQO paralogs and mdh collectively satisfy the malate→oxaloacetate step, but individual gene-level assignments should flag the "quinone-dependent vs. NAD-dependent" distinction.

## 7. Genes to Promote to Full Review

1. **PP_0897** (fumarase class I): Has context-dependent essentiality and possible non-canonical functions beyond fumarase activity (banerjee2025addressinggenomescale pages 1-2, banerjee2025addressinggenomescale pages 5-7).
2. **mqo1/mqo2/mqo3**: Isoform-specific roles are critical for accurate TCA cycle modeling; mqo2 has Crc-regulation evidence (morales2004thepseudomonasputida pages 3-4).
3. **acnB (PP_2339)**: Dual TCA/methylcitrate annotation needs resolution.
4. **idh (PP_4012)**: Contribution relative to icd (PP_4011) should be clarified.
5. **lpd (PP_5366) / lpdV (PP_4404)**: E3 paralog assignment to specific dehydrogenase complexes needs resolution.

## 8. Key References

1. Sudarsan et al. (2014) "The Functional Structure of Central Carbon Metabolism in *Pseudomonas putida* KT2440." *Appl. Environ. Microbiol.* 80:5292–5303. DOI: 10.1128/aem.01643-14 (sudarsan2014thefunctionalstructure pages 6-7, sudarsan2014thefunctionalstructure pages 7-8, sudarsan2014thefunctionalstructure pages 8-10).
2. Nikel et al. (2014) "Metabolic and regulatory rearrangements underlying glycerol metabolism in *Pseudomonas putida* KT2440." *Environ. Microbiol.* 16:239–54. DOI: 10.1111/1462-2920.12224 (nikel2014metabolicandregulatory pages 38-42).
3. Morales et al. (2004) "The *Pseudomonas putida* Crc Global Regulator Controls the Expression of Genes from Several Chromosomal Catabolic Pathways." *J. Bacteriol.* 186:1337–1344. DOI: 10.1128/jb.186.5.1337-1344.2004 (morales2004thepseudomonasputida pages 3-4).
4. Moreno et al. (2024) "Inactivation of *Pseudomonas putida* KT2440 pyruvate dehydrogenase relieves catabolite repression." *Microb. Biotechnol.* 17. DOI: 10.1111/1751-7915.14514 (moreno2024inactivationofpseudomonas pages 4-5, moreno2024inactivationofpseudomonas pages 7-9).
5. Puchałka et al. (2008) "Genome-Scale Reconstruction and Analysis of the *Pseudomonas putida* KT2440 Metabolic Network." *PLoS Comput. Biol.* 4:e1000210. DOI: 10.1371/journal.pcbi.1000210 (puchałka2008genomescalereconstructionand pages 9-10, puchałka2008genomescalereconstructionand pages 12-13).
6. Banerjee et al. (2025) "Addressing genome scale design tradeoffs in *Pseudomonas putida* for bioconversion of an aromatic carbon source." *NPJ Syst. Biol. Appl.* 11. DOI: 10.1038/s41540-024-00480-z (banerjee2025addressinggenomescale pages 1-2, banerjee2025addressinggenomescale pages 8-9, banerjee2025addressinggenomescale pages 5-7, banerjee2025addressinggenomescale pages 7-8).
7. Ainelo et al. (2019) "*Pseudomonas putida* Responds to the Toxin GraT by Inducing Ribosome Biogenesis Factors and Repressing TCA Cycle Enzymes." *Toxins* 11:103. DOI: 10.3390/toxins11020103 (ainelo2019pseudomonasputidaresponds pages 5-9).
8. Nikel et al. (2015) "*Pseudomonas putida* KT2440 Strain Metabolizes Glucose through a Cycle Formed by Enzymes of the ED, EMP, and PP Pathways." *J. Biol. Chem.* 290:25920–25932. DOI: 10.1074/jbc.m115.687749 (nikel2015pseudomonasputidakt2440 pages 21-25).
9. Molina et al. (2019) "*Pseudomonas putida* KT2440 metabolism undergoes sequential modifications during exponential growth." *Environ. Microbiol.* 21:2375–2390. DOI: 10.1111/1462-2920.14622 (molina2019pseudomonasputidakt2440 pages 5-6).
10. Dolan et al. (2022) "Systems-Wide Dissection of Organic Acid Assimilation in *Pseudomonas aeruginosa*." *mBio* 13. DOI: 10.1128/mbio.02541-22 (dolan2022systemswidedissectionof pages 2-4).
11. Nogales et al. (2020) "High-quality genome-scale metabolic modelling of *Pseudomonas putida*." *Environ. Microbiol.* 22:255–269. DOI: 10.1111/1462-2920.14843 (nogales2020high‐qualitygenome‐scalemetabolic pages 7-9, nogales2020high‐qualitygenome‐scalemetabolic pages 1-2, nogales2020high‐qualitygenome‐scalemetabolic pages 10-12).
12. Zhou et al. (2025) "Quantitative decoding of coupled carbon and energy metabolism in *Pseudomonas putida* for lignin carbon utilization." *Commun. Biol.* 8. DOI: 10.1038/s42003-025-08723-3 (zhou2025quantitativeanalysisof pages 1-3, zhou2025quantitativedecodingof pages 5-7).


References

1. (moreno2024inactivationofpseudomonas pages 4-5): Renata Moreno, Luis Yuste, Gracia Morales, and Fernando Rojo. Inactivation of pseudomonas putida kt2440 pyruvate dehydrogenase relieves catabolite repression and improves the usefulness of this strain for degrading aromatic compounds. Microbial Biotechnology, Jun 2024. URL: https://doi.org/10.1111/1751-7915.14514, doi:10.1111/1751-7915.14514. This article has 8 citations and is from a peer-reviewed journal.

2. (moreno2024inactivationofpseudomonas pages 7-9): Renata Moreno, Luis Yuste, Gracia Morales, and Fernando Rojo. Inactivation of pseudomonas putida kt2440 pyruvate dehydrogenase relieves catabolite repression and improves the usefulness of this strain for degrading aromatic compounds. Microbial Biotechnology, Jun 2024. URL: https://doi.org/10.1111/1751-7915.14514, doi:10.1111/1751-7915.14514. This article has 8 citations and is from a peer-reviewed journal.

3. (zhou2025quantitativedecodingof pages 5-7): Nanqing Zhou, Rebecca A. Wilkes, Xinyu Chen, Kelly P. Teitel, James A. Belgrave, Gregg T. Beckham, Allison Z. Werner, Yanbao Yu, and Ludmilla Aristilde. Quantitative decoding of coupled carbon and energy metabolism in pseudomonas putida for lignin carbon utilization. Communications Biology, Aug 2025. URL: https://doi.org/10.1038/s42003-025-08723-3, doi:10.1038/s42003-025-08723-3. This article has 11 citations and is from a peer-reviewed journal.

4. (sudarsan2014thefunctionalstructure pages 8-10): Suresh Sudarsan, Sarah Dethlefsen, Lars M. Blank, Martin Siemann-Herzberg, and Andreas Schmid. The functional structure of central carbon metabolism in pseudomonas putida kt2440. Applied and Environmental Microbiology, 80:5292-5303, Sep 2014. URL: https://doi.org/10.1128/aem.01643-14, doi:10.1128/aem.01643-14. This article has 155 citations and is from a peer-reviewed journal.

5. (sudarsan2014thefunctionalstructure pages 7-8): Suresh Sudarsan, Sarah Dethlefsen, Lars M. Blank, Martin Siemann-Herzberg, and Andreas Schmid. The functional structure of central carbon metabolism in pseudomonas putida kt2440. Applied and Environmental Microbiology, 80:5292-5303, Sep 2014. URL: https://doi.org/10.1128/aem.01643-14, doi:10.1128/aem.01643-14. This article has 155 citations and is from a peer-reviewed journal.

6. (dolan2022systemswidedissectionof pages 2-4): Stephen K. Dolan, Andre Wijaya, Michael Kohlstedt, Lars Gläser, Paul Brear, Rafael Silva-Rocha, Christoph Wittmann, and Martin Welch. Systems-wide dissection of organic acid assimilation in pseudomonas aeruginosa reveals a novel path to underground metabolism. Dec 2022. URL: https://doi.org/10.1128/mbio.02541-22, doi:10.1128/mbio.02541-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

7. (sudarsan2014thefunctionalstructure pages 6-7): Suresh Sudarsan, Sarah Dethlefsen, Lars M. Blank, Martin Siemann-Herzberg, and Andreas Schmid. The functional structure of central carbon metabolism in pseudomonas putida kt2440. Applied and Environmental Microbiology, 80:5292-5303, Sep 2014. URL: https://doi.org/10.1128/aem.01643-14, doi:10.1128/aem.01643-14. This article has 155 citations and is from a peer-reviewed journal.

8. (nikel2014metabolicandregulatory pages 38-42): Pablo I. Nikel, Juhyun Kim, and Víctor de Lorenzo. Metabolic and regulatory rearrangements underlying glycerol metabolism in pseudomonas putida kt2440. Environmental microbiology, 16 1:239-54, Aug 2014. URL: https://doi.org/10.1111/1462-2920.12224, doi:10.1111/1462-2920.12224. This article has 151 citations and is from a domain leading peer-reviewed journal.

9. (nikel2015pseudomonasputidakt2440 pages 21-25): Pablo I. Nikel, Max Chavarría, Tobias Fuhrer, Uwe Sauer, and Víctor de Lorenzo. Pseudomonas putida kt2440 strain metabolizes glucose through a cycle formed by enzymes of the entner-doudoroff, embden-meyerhof-parnas, and pentose phosphate pathways. Journal of Biological Chemistry, 290:25920-25932, Oct 2015. URL: https://doi.org/10.1074/jbc.m115.687749, doi:10.1074/jbc.m115.687749. This article has 446 citations and is from a domain leading peer-reviewed journal.

10. (ainelo2019pseudomonasputidaresponds pages 5-9): Andres Ainelo, Rando Porosk, Kalle Kilk, Sirli Rosendahl, Jaanus Remme, and Rita Hõrak. Pseudomonas putida responds to the toxin grat by inducing ribosome biogenesis factors and repressing tca cycle enzymes. Toxins, 11:103, Feb 2019. URL: https://doi.org/10.3390/toxins11020103, doi:10.3390/toxins11020103. This article has 10 citations.

11. (banerjee2025addressinggenomescale pages 1-2): Deepanwita Banerjee, Javier Menasalvas, Yan Chen, Jennifer W. Gin, Edward E. K. Baidoo, Christopher J. Petzold, Thomas Eng, and Aindrila Mukhopadhyay. Addressing genome scale design tradeoffs in pseudomonas putida for bioconversion of an aromatic carbon source. NPJ Systems Biology and Applications, Jan 2025. URL: https://doi.org/10.1038/s41540-024-00480-z, doi:10.1038/s41540-024-00480-z. This article has 13 citations.

12. (banerjee2025addressinggenomescale pages 8-9): Deepanwita Banerjee, Javier Menasalvas, Yan Chen, Jennifer W. Gin, Edward E. K. Baidoo, Christopher J. Petzold, Thomas Eng, and Aindrila Mukhopadhyay. Addressing genome scale design tradeoffs in pseudomonas putida for bioconversion of an aromatic carbon source. NPJ Systems Biology and Applications, Jan 2025. URL: https://doi.org/10.1038/s41540-024-00480-z, doi:10.1038/s41540-024-00480-z. This article has 13 citations.

13. (banerjee2025addressinggenomescale pages 5-7): Deepanwita Banerjee, Javier Menasalvas, Yan Chen, Jennifer W. Gin, Edward E. K. Baidoo, Christopher J. Petzold, Thomas Eng, and Aindrila Mukhopadhyay. Addressing genome scale design tradeoffs in pseudomonas putida for bioconversion of an aromatic carbon source. NPJ Systems Biology and Applications, Jan 2025. URL: https://doi.org/10.1038/s41540-024-00480-z, doi:10.1038/s41540-024-00480-z. This article has 13 citations.

14. (banerjee2025addressinggenomescale pages 7-8): Deepanwita Banerjee, Javier Menasalvas, Yan Chen, Jennifer W. Gin, Edward E. K. Baidoo, Christopher J. Petzold, Thomas Eng, and Aindrila Mukhopadhyay. Addressing genome scale design tradeoffs in pseudomonas putida for bioconversion of an aromatic carbon source. NPJ Systems Biology and Applications, Jan 2025. URL: https://doi.org/10.1038/s41540-024-00480-z, doi:10.1038/s41540-024-00480-z. This article has 13 citations.

15. (puchałka2008genomescalereconstructionand pages 9-10): Jacek Puchałka, Matthew A. Oberhardt, Miguel Godinho, Agata Bielecka, Daniela Regenhardt, Kenneth N. Timmis, Jason A. Papin, and Vítor A. P. Martins dos Santos. Genome-scale reconstruction and analysis of the pseudomonas putida kt2440 metabolic network facilitates applications in biotechnology. PLoS Computational Biology, 4:e1000210, Oct 2008. URL: https://doi.org/10.1371/journal.pcbi.1000210, doi:10.1371/journal.pcbi.1000210. This article has 336 citations and is from a highest quality peer-reviewed journal.

16. (morales2004thepseudomonasputida pages 3-4): Gracia Morales, Juan Francisco Linares, Ana Beloso, Juan Pablo Albar, José Luis Martínez, and Fernando Rojo. The pseudomonas putida crc global regulator controls the expression of genes from several chromosomal catabolic pathways for aromatic compounds. Journal of Bacteriology, 186:1337-1344, Mar 2004. URL: https://doi.org/10.1128/jb.186.5.1337-1344.2004, doi:10.1128/jb.186.5.1337-1344.2004. This article has 172 citations and is from a peer-reviewed journal.

17. (zhou2025quantitativeanalysisof pages 1-3): Nanqing Zhou, Rebecca A. Wilkes, Xinyu Chen, Kelly P. Teitel, James A. Belgrave, Gregg T. Beckham, Allison Z. Werner, Yanbao Yu, and Ludmilla Aristilde. Quantitative analysis of coupled carbon and energy metabolism for lignin carbon utilization in pseudomonas putida. bioRxiv, Mar 2025. URL: https://doi.org/10.1101/2025.03.24.645021, doi:10.1101/2025.03.24.645021. This article has 4 citations.

18. (puchałka2008genomescalereconstructionand pages 12-13): Jacek Puchałka, Matthew A. Oberhardt, Miguel Godinho, Agata Bielecka, Daniela Regenhardt, Kenneth N. Timmis, Jason A. Papin, and Vítor A. P. Martins dos Santos. Genome-scale reconstruction and analysis of the pseudomonas putida kt2440 metabolic network facilitates applications in biotechnology. PLoS Computational Biology, 4:e1000210, Oct 2008. URL: https://doi.org/10.1371/journal.pcbi.1000210, doi:10.1371/journal.pcbi.1000210. This article has 336 citations and is from a highest quality peer-reviewed journal.

19. (molina2019pseudomonasputidakt2440 pages 5-6): Lázaro Molina, Ruggero La Rosa, Juan Nogales, and Fernando Rojo. Pseudomonas putida kt2440 metabolism undergoes sequential modifications during exponential growth in a complete medium as compounds are gradually consumed. Environmental Microbiology, 21:2375-2390, Apr 2019. URL: https://doi.org/10.1111/1462-2920.14622, doi:10.1111/1462-2920.14622. This article has 77 citations and is from a domain leading peer-reviewed journal.

20. (nogales2020high‐qualitygenome‐scalemetabolic pages 7-9): Juan Nogales, Joshua Mueller, Steinn Gudmundsson, Francisco J. Canalejo, Estrella Duque, Jonathan Monk, Adam M. Feist, Juan Luis Ramos, Wei Niu, and Bernhard O. Palsson. High‐quality genome‐scale metabolic modelling of pseudomonas putida highlights its broad metabolic capabilities. Environmental Microbiology, 22:255-269, Nov 2020. URL: https://doi.org/10.1111/1462-2920.14843, doi:10.1111/1462-2920.14843. This article has 229 citations and is from a domain leading peer-reviewed journal.

21. (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2): Juan Nogales, Joshua Mueller, Steinn Gudmundsson, Francisco J. Canalejo, Estrella Duque, Jonathan Monk, Adam M. Feist, Juan Luis Ramos, Wei Niu, and Bernhard O. Palsson. High‐quality genome‐scale metabolic modelling of pseudomonas putida highlights its broad metabolic capabilities. Environmental Microbiology, 22:255-269, Nov 2020. URL: https://doi.org/10.1111/1462-2920.14843, doi:10.1111/1462-2920.14843. This article has 229 citations and is from a domain leading peer-reviewed journal.

22. (nogales2020high‐qualitygenome‐scalemetabolic pages 10-12): Juan Nogales, Joshua Mueller, Steinn Gudmundsson, Francisco J. Canalejo, Estrella Duque, Jonathan Monk, Adam M. Feist, Juan Luis Ramos, Wei Niu, and Bernhard O. Palsson. High‐quality genome‐scale metabolic modelling of pseudomonas putida highlights its broad metabolic capabilities. Environmental Microbiology, 22:255-269, Nov 2020. URL: https://doi.org/10.1111/1462-2920.14843, doi:10.1111/1462-2920.14843. This article has 229 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__tca_cycle__ppu00020-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. dolan2022systemswidedissectionof pages 2-4
2. sudarsan2014thefunctionalstructure pages 6-7
3. ainelo2019pseudomonasputidaresponds pages 5-9
4. morales2004thepseudomonasputida pages 3-4
5. moreno2024inactivationofpseudomonas pages 7-9
6. sudarsan2014thefunctionalstructure pages 8-10
7. moreno2024inactivationofpseudomonas pages 4-5
8. nikel2014metabolicandregulatory pages 38-42
9. zhou2025quantitativedecodingof pages 5-7
10. sudarsan2014thefunctionalstructure pages 7-8
11. banerjee2025addressinggenomescale pages 1-2
12. banerjee2025addressinggenomescale pages 8-9
13. banerjee2025addressinggenomescale pages 5-7
14. banerjee2025addressinggenomescale pages 7-8
15. zhou2025quantitativeanalysisof pages 1-3
16. quinone
17. NADP
18. ADP-forming
19. https://doi.org/10.1111/1751-7915.14514,
20. https://doi.org/10.1038/s42003-025-08723-3,
21. https://doi.org/10.1128/aem.01643-14,
22. https://doi.org/10.1128/mbio.02541-22,
23. https://doi.org/10.1111/1462-2920.12224,
24. https://doi.org/10.1074/jbc.m115.687749,
25. https://doi.org/10.3390/toxins11020103,
26. https://doi.org/10.1038/s41540-024-00480-z,
27. https://doi.org/10.1371/journal.pcbi.1000210,
28. https://doi.org/10.1128/jb.186.5.1337-1344.2004,
29. https://doi.org/10.1101/2025.03.24.645021,
30. https://doi.org/10.1111/1462-2920.14622,
31. https://doi.org/10.1111/1462-2920.14843,