---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T07:02:31.632695'
end_time: '2026-07-23T07:28:51.783017'
duration_seconds: 1580.15
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Type-II fatty-acid synthesis
  module_summary: A reusable dissociated bacterial fatty-acid synthase pathway that
    forms malonyl-CoA with acetyl-CoA carboxylase, loads malonate onto acyl carrier
    protein, initiates an acyl-ACP chain, and iteratively elongates that chain through
    condensation, beta-keto reduction, dehydration, and enoyl reduction. A FabA/FabB
    branch introduces and extends cis unsaturation. Enzyme-family and cofactor variants
    are represented explicitly rather than collapsed into a type-I fatty-acid synthase.
  module_outline: "- Type-II fatty-acid synthesis\n  - 1. malonyl-CoA formation\n\
    \  - Acetyl-CoA carboxylase\n    - Heteromeric acetyl-CoA carboxylase (molecular\
    \ player: bacterial AccABCD acetyl-CoA carboxylase; activity or role: acetyl-CoA\
    \ carboxylase activity)\n  - 2. acyl-group carriage\n  - Acyl carrier protein\n\
    \    - Holo-acyl carrier protein (molecular player: PSEPK canonical AcpP; activity\
    \ or role: acyl carrier activity)\n  - 3. malonyl-ACP formation\n  - FabD malonyl-ACP\
    \ loading\n    - Malonyl-CoA:ACP transacylase (molecular player: PSEPK canonical\
    \ FabD; activity or role: acyl-carrier-protein S-malonyltransferase activity)\n\
    \  - 4. fatty-acid chain initiation\n  - KAS-III-type chain initiation\n    -\
    \ Beta-ketoacyl-ACP synthase III initiator (molecular player: PSEPK PP_4379 chain-initiation\
    \ candidate; activity or role: beta-ketoacyl-acyl-carrier-protein synthase III\
    \ activity)\n  - 5. iterative acyl-chain elongation\n  - Four-reaction FAS-II\
    \ elongation cycle\n    - 1. decarboxylative condensation\n    - KAS-I/KAS-II\
    \ condensation\n      - Iterative decarboxylative condensation (molecular player:\
    \ 3-oxoacyl-acyl-carrier-protein synthase activity; activity or role: 3-oxoacyl-acyl-carrier-protein\
    \ synthase activity)\n      - Alternative versions by condensing enzyme: Elongation\
    \ condensing-enzyme variants\n        - FabB KAS-I\n          - FabB 3-oxoacyl-ACP\
    \ synthase (molecular player: PSEPK FabB; activity or role: 3-oxoacyl-acyl-carrier-protein\
    \ synthase activity)\n        - FabF KAS-II\n          - FabF 3-oxoacyl-ACP synthase\
    \ (molecular player: PSEPK FabF; activity or role: 3-oxoacyl-acyl-carrier-protein\
    \ synthase activity)\n        - PP_3303 KAS-II candidate\n          - PP_3303\
    \ 3-oxoacyl-ACP synthase candidate (molecular player: PSEPK PP_3303; activity\
    \ or role: 3-oxoacyl-acyl-carrier-protein synthase activity)\n    - 2. beta-keto\
    \ reduction\n    - 3-oxoacyl-ACP reduction\n      - NADPH-dependent beta-keto\
    \ reduction (molecular player: 3-oxoacyl-acyl-carrier-protein reductase (NADPH)\
    \ activity; activity or role: 3-oxoacyl-acyl-carrier-protein reductase (NADPH)\
    \ activity)\n      - Alternative versions by reductase paralog: 3-oxoacyl-ACP\
    \ reductase variants\n        - Canonical FabG\n          - FabG 3-oxoacyl-ACP\
    \ reductase (molecular player: PSEPK FabG; activity or role: 3-oxoacyl-acyl-carrier-protein\
    \ reductase (NADPH) activity)\n        - PP_0581 reductase candidate\n       \
    \   - PP_0581 3-oxoacyl-ACP reductase candidate (molecular player: PSEPK PP_0581)\n\
    \    - 3. 3-hydroxyacyl dehydration\n    - 3-hydroxyacyl-ACP dehydration\n   \
    \   - Elongation-cycle dehydration (molecular player: (3R)-hydroxyacyl-acyl-carrier-protein\
    \ dehydratase activity; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein\
    \ dehydratase activity)\n      - Alternative versions by dehydratase family: FAS-II\
    \ dehydratase variants\n        - FabZ dehydratase\n          - FabZ 3-hydroxyacyl-ACP\
    \ dehydratase (molecular player: PSEPK FabZ; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein\
    \ dehydratase activity)\n        - FabA dehydratase\n          - FabA 3-hydroxyacyl-ACP\
    \ dehydratase (molecular player: PSEPK FabA; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein\
    \ dehydratase activity)\n    - 4. enoyl reduction\n    - Enoyl-ACP reduction\n\
    \      - Elongation-cycle enoyl reduction (molecular player: enoyl-acyl-carrier-protein\
    \ reductase activity)\n      - Alternative versions by electron donor and enzyme\
    \ family: Enoyl-ACP reductase variants\n        - FabV NADH-dependent reductase\n\
    \          - FabV enoyl-ACP reductase (molecular player: PSEPK FabV; activity\
    \ or role: enoyl-acyl-carrier-protein reductase (NADH) activity)\n        - PP_1852\
    \ NADPH-dependent reductase\n          - PP_1852 enoyl-ACP reductase candidate\
    \ (molecular player: PSEPK PP_1852; activity or role: enoyl-acyl-carrier-protein\
    \ reductase (NADPH) activity)\n  - 6. cis-unsaturated fatty-acid branch\n  - FabA/FabB\
    \ cis-unsaturated branch\n    - 1. trans-2 to cis-3 isomerization\n    - FabA\
    \ trans-2-decenoyl-ACP isomerization\n      - FabA trans-2-decenoyl-ACP isomerase\
    \ (molecular player: PSEPK FabA; activity or role: trans-2-decenoyl-acyl-carrier-protein\
    \ isomerase activity)\n    - 2. cis-unsaturated chain extension\n    - FabB unsaturated-chain\
    \ condensation\n      - FabB cis-unsaturated chain elongation (molecular player:\
    \ PSEPK FabB; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)"
  module_connections: '- Acetyl-CoA carboxylase feeds into FabD malonyl-ACP loading:
    AccABCD supplies malonyl-CoA to FabD.

    - Acyl carrier protein feeds into FabD malonyl-ACP loading: Holo-ACP accepts malonate
    from FabD.

    - FabD malonyl-ACP loading feeds into KAS-III-type chain initiation: Malonyl-ACP
    is the two-carbon donor for chain initiation.

    - KAS-III-type chain initiation feeds into Four-reaction FAS-II elongation cycle:
    The initiated beta-ketoacyl-ACP enters reductive elongation.

    - Four-reaction FAS-II elongation cycle feeds into FabA/FabB cis-unsaturated branch:
    A C10 trans-2-enoyl-ACP intermediate can enter the FabA/FabB branch.

    - KAS-I/KAS-II condensation feeds into 3-oxoacyl-ACP reduction: Condensation produces
    3-oxoacyl-ACP for reduction.

    - 3-oxoacyl-ACP reduction feeds into 3-hydroxyacyl-ACP dehydration: Reduction
    produces 3-hydroxyacyl-ACP for dehydration.

    - 3-hydroxyacyl-ACP dehydration feeds into Enoyl-ACP reduction: Dehydration produces
    trans-2-enoyl-ACP for reduction.

    - Enoyl-ACP reduction feeds into KAS-I/KAS-II condensation: The saturated acyl-ACP
    product re-enters another elongation round.

    - FabA trans-2-decenoyl-ACP isomerization feeds into FabB unsaturated-chain condensation:
    FabA supplies cis-3-decenoyl-ACP to FabB.'
  pathway_query: ppu00061
  pathway_id: ppu00061
  pathway_name: Fatty acid biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00061 with 7 primary genes; module
    area: lipid_cell_envelope_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '19'
  candidate_genes: '- accC: PP_0558 | Q88QD6 | Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme
    A carboxylase biotin carboxylase subunit A) (EC 6.3.4.14; primary bucket kegg:ppu00061)

    - accB: PP_0559 | Q88QD5 | Biotin carboxyl carrier protein of acetyl-CoA carboxylase
    (primary bucket kegg:ppu00061)

    - PP_0581: PP_0581 | Q88QB3 | 3-oxoacyl-(Acyl-carrier-protein) reductase (primary
    bucket kegg:ppu00780)

    - fabZ: PP_1602 | Q88MG9 | 3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabZ
    (EC 4.2.1.59) ((3R)-hydroxymyristoyl-[acyl-carrier-protein] dehydratase) ((3R)-hydroxymyristoyl-ACP
    dehydrase) (Beta-hydroxyacyl-ACP dehydratase) (EC 4.2.1.59; primary bucket kegg:ppu00780)

    - accA: PP_1607 | Q88MG4 | Acetyl-coenzyme A carboxylase carboxyl transferase
    subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyltransferase
    subunit alpha) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)

    - PP_1852: PP_1852 | Q88LS6 | Enoyl-[acyl-carrier-protein] reductase (NADPH, B-specific)
    (EC 1.3.1.10) (EC 1.3.1.10; primary bucket kegg:ppu00780)

    - fabD: PP_1913 | Q88LL7 | Malonyl CoA-acyl carrier protein transacylase (EC 2.3.1.39)
    (EC 2.3.1.39; primary bucket kegg:ppu00074)

    - fabG: PP_1914 | Q88LL6 | 3-oxoacyl-[acyl-carrier-protein] reductase (EC 1.1.1.100)
    (EC 1.1.1.100; primary bucket kegg:ppu00780)

    - fabF: PP_1916 | Q88LL4 | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179)
    (EC 2.3.1.179; primary bucket kegg:ppu00780)

    - accD: PP_1996 | Q88LD9 | Acetyl-coenzyme A carboxylase carboxyl transferase
    subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltransferase
    subunit beta) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)

    - PP_2540: PP_2540 | Q88JV7 | Oxidoreductase, short-chain dehydrogenase/reductase
    family (primary bucket kegg:ppu00780)

    - PP_2783: PP_2783 | Q88J66 | 2,3-dihydroxy-2,3-dihydro-p-cumate dehydrogenase
    (EC 1.3.1.58) (Biphenyl-2,3-dihydro-2,3-diol dehydrogenase) (EC 1.3.1.58; primary
    bucket kegg:ppu00780)

    - PP_3303: PP_3303 | Q88HQ0 | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC
    2.3.1.179) (EC 2.3.1.179; primary bucket kegg:ppu00780)

    - fabA: PP_4174 | Q88FC4 | 3-hydroxydecanoyl-[acyl-carrier-protein] dehydratase
    (EC 4.2.1.59) (3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabA) (Beta-hydroxydecanoyl
    thioester dehydrase) (Trans-2-decenoyl-[acyl-carrier-protein] isomerase) (EC 5.3.3.14)
    (EC 4.2.1.59; 5.3.3.14; primary bucket kegg:ppu00061)

    - fabB: PP_4175 | Q88FC3 | 3-oxoacyl-[acyl-carrier-protein] synthase 1 (EC 2.3.1.41)
    (3-oxoacyl-[acyl-carrier-protein] synthase I) (Beta-ketoacyl-ACP synthase I) (EC
    2.3.1.41; primary bucket kegg:ppu00780)

    - PP_4379: PP_4379 | Q88ES4 | Beta-ketoacyl-acyl-carrier-protein synthase I (EC
    2.3.1.180) (EC 2.3.1.180; primary bucket kegg:ppu00061)

    - fadD-I: PP_4549 | Q88EB7 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain
    acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)

    - fadD-II: PP_4550 | Q88EB6 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain
    acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)

    - fabV: PP_4635 | Q88E33 | Enoyl-[acyl-carrier-protein] reductase [NADH] (ENR)
    (EC 1.3.1.9) (EC 1.3.1.9; primary bucket kegg:ppu00061)'
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__type_ii_fatty_acid_synthesis__ppu00061-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__type_ii_fatty_acid_synthesis__ppu00061-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Type-II fatty-acid synthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00061
- Resolved ID: ppu00061
- Resolved name: Fatty acid biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00061 with 7 primary genes; module area: lipid_cell_envelope_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 19

- accC: PP_0558 | Q88QD6 | Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) (EC 6.3.4.14; primary bucket kegg:ppu00061)
- accB: PP_0559 | Q88QD5 | Biotin carboxyl carrier protein of acetyl-CoA carboxylase (primary bucket kegg:ppu00061)
- PP_0581: PP_0581 | Q88QB3 | 3-oxoacyl-(Acyl-carrier-protein) reductase (primary bucket kegg:ppu00780)
- fabZ: PP_1602 | Q88MG9 | 3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabZ (EC 4.2.1.59) ((3R)-hydroxymyristoyl-[acyl-carrier-protein] dehydratase) ((3R)-hydroxymyristoyl-ACP dehydrase) (Beta-hydroxyacyl-ACP dehydratase) (EC 4.2.1.59; primary bucket kegg:ppu00780)
- accA: PP_1607 | Q88MG4 | Acetyl-coenzyme A carboxylase carboxyl transferase subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyltransferase subunit alpha) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)
- PP_1852: PP_1852 | Q88LS6 | Enoyl-[acyl-carrier-protein] reductase (NADPH, B-specific) (EC 1.3.1.10) (EC 1.3.1.10; primary bucket kegg:ppu00780)
- fabD: PP_1913 | Q88LL7 | Malonyl CoA-acyl carrier protein transacylase (EC 2.3.1.39) (EC 2.3.1.39; primary bucket kegg:ppu00074)
- fabG: PP_1914 | Q88LL6 | 3-oxoacyl-[acyl-carrier-protein] reductase (EC 1.1.1.100) (EC 1.1.1.100; primary bucket kegg:ppu00780)
- fabF: PP_1916 | Q88LL4 | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) (EC 2.3.1.179; primary bucket kegg:ppu00780)
- accD: PP_1996 | Q88LD9 | Acetyl-coenzyme A carboxylase carboxyl transferase subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltransferase subunit beta) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)
- PP_2540: PP_2540 | Q88JV7 | Oxidoreductase, short-chain dehydrogenase/reductase family (primary bucket kegg:ppu00780)
- PP_2783: PP_2783 | Q88J66 | 2,3-dihydroxy-2,3-dihydro-p-cumate dehydrogenase (EC 1.3.1.58) (Biphenyl-2,3-dihydro-2,3-diol dehydrogenase) (EC 1.3.1.58; primary bucket kegg:ppu00780)
- PP_3303: PP_3303 | Q88HQ0 | 3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) (EC 2.3.1.179; primary bucket kegg:ppu00780)
- fabA: PP_4174 | Q88FC4 | 3-hydroxydecanoyl-[acyl-carrier-protein] dehydratase (EC 4.2.1.59) (3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabA) (Beta-hydroxydecanoyl thioester dehydrase) (Trans-2-decenoyl-[acyl-carrier-protein] isomerase) (EC 5.3.3.14) (EC 4.2.1.59; 5.3.3.14; primary bucket kegg:ppu00061)
- fabB: PP_4175 | Q88FC3 | 3-oxoacyl-[acyl-carrier-protein] synthase 1 (EC 2.3.1.41) (3-oxoacyl-[acyl-carrier-protein] synthase I) (Beta-ketoacyl-ACP synthase I) (EC 2.3.1.41; primary bucket kegg:ppu00780)
- PP_4379: PP_4379 | Q88ES4 | Beta-ketoacyl-acyl-carrier-protein synthase I (EC 2.3.1.180) (EC 2.3.1.180; primary bucket kegg:ppu00061)
- fadD-I: PP_4549 | Q88EB7 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)
- fadD-II: PP_4550 | Q88EB6 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)
- fabV: PP_4635 | Q88E33 | Enoyl-[acyl-carrier-protein] reductase [NADH] (ENR) (EC 1.3.1.9) (EC 1.3.1.9; primary bucket kegg:ppu00061)

## Generic Module Context

### Working Scope

A reusable dissociated bacterial fatty-acid synthase pathway that forms malonyl-CoA with acetyl-CoA carboxylase, loads malonate onto acyl carrier protein, initiates an acyl-ACP chain, and iteratively elongates that chain through condensation, beta-keto reduction, dehydration, and enoyl reduction. A FabA/FabB branch introduces and extends cis unsaturation. Enzyme-family and cofactor variants are represented explicitly rather than collapsed into a type-I fatty-acid synthase.

### Provisional Biological Outline

- Type-II fatty-acid synthesis
  - 1. malonyl-CoA formation
  - Acetyl-CoA carboxylase
    - Heteromeric acetyl-CoA carboxylase (molecular player: bacterial AccABCD acetyl-CoA carboxylase; activity or role: acetyl-CoA carboxylase activity)
  - 2. acyl-group carriage
  - Acyl carrier protein
    - Holo-acyl carrier protein (molecular player: PSEPK canonical AcpP; activity or role: acyl carrier activity)
  - 3. malonyl-ACP formation
  - FabD malonyl-ACP loading
    - Malonyl-CoA:ACP transacylase (molecular player: PSEPK canonical FabD; activity or role: acyl-carrier-protein S-malonyltransferase activity)
  - 4. fatty-acid chain initiation
  - KAS-III-type chain initiation
    - Beta-ketoacyl-ACP synthase III initiator (molecular player: PSEPK PP_4379 chain-initiation candidate; activity or role: beta-ketoacyl-acyl-carrier-protein synthase III activity)
  - 5. iterative acyl-chain elongation
  - Four-reaction FAS-II elongation cycle
    - 1. decarboxylative condensation
    - KAS-I/KAS-II condensation
      - Iterative decarboxylative condensation (molecular player: 3-oxoacyl-acyl-carrier-protein synthase activity; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)
      - Alternative versions by condensing enzyme: Elongation condensing-enzyme variants
        - FabB KAS-I
          - FabB 3-oxoacyl-ACP synthase (molecular player: PSEPK FabB; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)
        - FabF KAS-II
          - FabF 3-oxoacyl-ACP synthase (molecular player: PSEPK FabF; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)
        - PP_3303 KAS-II candidate
          - PP_3303 3-oxoacyl-ACP synthase candidate (molecular player: PSEPK PP_3303; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)
    - 2. beta-keto reduction
    - 3-oxoacyl-ACP reduction
      - NADPH-dependent beta-keto reduction (molecular player: 3-oxoacyl-acyl-carrier-protein reductase (NADPH) activity; activity or role: 3-oxoacyl-acyl-carrier-protein reductase (NADPH) activity)
      - Alternative versions by reductase paralog: 3-oxoacyl-ACP reductase variants
        - Canonical FabG
          - FabG 3-oxoacyl-ACP reductase (molecular player: PSEPK FabG; activity or role: 3-oxoacyl-acyl-carrier-protein reductase (NADPH) activity)
        - PP_0581 reductase candidate
          - PP_0581 3-oxoacyl-ACP reductase candidate (molecular player: PSEPK PP_0581)
    - 3. 3-hydroxyacyl dehydration
    - 3-hydroxyacyl-ACP dehydration
      - Elongation-cycle dehydration (molecular player: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity)
      - Alternative versions by dehydratase family: FAS-II dehydratase variants
        - FabZ dehydratase
          - FabZ 3-hydroxyacyl-ACP dehydratase (molecular player: PSEPK FabZ; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity)
        - FabA dehydratase
          - FabA 3-hydroxyacyl-ACP dehydratase (molecular player: PSEPK FabA; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity)
    - 4. enoyl reduction
    - Enoyl-ACP reduction
      - Elongation-cycle enoyl reduction (molecular player: enoyl-acyl-carrier-protein reductase activity)
      - Alternative versions by electron donor and enzyme family: Enoyl-ACP reductase variants
        - FabV NADH-dependent reductase
          - FabV enoyl-ACP reductase (molecular player: PSEPK FabV; activity or role: enoyl-acyl-carrier-protein reductase (NADH) activity)
        - PP_1852 NADPH-dependent reductase
          - PP_1852 enoyl-ACP reductase candidate (molecular player: PSEPK PP_1852; activity or role: enoyl-acyl-carrier-protein reductase (NADPH) activity)
  - 6. cis-unsaturated fatty-acid branch
  - FabA/FabB cis-unsaturated branch
    - 1. trans-2 to cis-3 isomerization
    - FabA trans-2-decenoyl-ACP isomerization
      - FabA trans-2-decenoyl-ACP isomerase (molecular player: PSEPK FabA; activity or role: trans-2-decenoyl-acyl-carrier-protein isomerase activity)
    - 2. cis-unsaturated chain extension
    - FabB unsaturated-chain condensation
      - FabB cis-unsaturated chain elongation (molecular player: PSEPK FabB; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)

### Known Relationships Among Steps

- Acetyl-CoA carboxylase feeds into FabD malonyl-ACP loading: AccABCD supplies malonyl-CoA to FabD.
- Acyl carrier protein feeds into FabD malonyl-ACP loading: Holo-ACP accepts malonate from FabD.
- FabD malonyl-ACP loading feeds into KAS-III-type chain initiation: Malonyl-ACP is the two-carbon donor for chain initiation.
- KAS-III-type chain initiation feeds into Four-reaction FAS-II elongation cycle: The initiated beta-ketoacyl-ACP enters reductive elongation.
- Four-reaction FAS-II elongation cycle feeds into FabA/FabB cis-unsaturated branch: A C10 trans-2-enoyl-ACP intermediate can enter the FabA/FabB branch.
- KAS-I/KAS-II condensation feeds into 3-oxoacyl-ACP reduction: Condensation produces 3-oxoacyl-ACP for reduction.
- 3-oxoacyl-ACP reduction feeds into 3-hydroxyacyl-ACP dehydration: Reduction produces 3-hydroxyacyl-ACP for dehydration.
- 3-hydroxyacyl-ACP dehydration feeds into Enoyl-ACP reduction: Dehydration produces trans-2-enoyl-ACP for reduction.
- Enoyl-ACP reduction feeds into KAS-I/KAS-II condensation: The saturated acyl-ACP product re-enters another elongation round.
- FabA trans-2-decenoyl-ACP isomerization feeds into FabB unsaturated-chain condensation: FabA supplies cis-3-decenoyl-ACP to FabB.

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

# Type-II Fatty-Acid Synthesis in *Pseudomonas putida* KT2440 — Module/Pathway Curation Review

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Pathway bucket:** KEGG `ppu00061` "Fatty acid biosynthesis" (module area: lipid_cell_envelope_metabolism)
**Assignment:** Species-aware satisfiability and annotation-curation review of the dissociated (type-II) bacterial fatty-acid synthase (FAS-II) module. The candidate gene list is treated as a starting point, not ground truth.

---

## 1. Executive Summary

The complete **type-II (dissociated) fatty-acid synthesis pathway is encoded and satisfiable** in *Pseudomonas putida* KT2440. Every canonical FAS-II step — malonyl-CoA supply by the heteromeric acetyl-CoA carboxylase (AccABCD), malonyl-ACP loading by FabD, KAS-III chain initiation, the four-reaction elongation cycle (condensation, β-keto reduction, dehydration, enoyl reduction), and the FabA/FabB *cis*-unsaturation branch — is covered by high-confidence canonical genes present in the genome. From a module-satisfiability standpoint this module should be marked **covered**, subject to a small number of curation actions.

Three findings are the curation focus. **First**, the essential **acyl carrier protein AcpP (PP_1915, Q88LL5)** — the physical substrate carrier on which the entire pathway operates — is present, essential, and supported by protein-level evidence (PE:1), yet is **missing from the 19-gene candidate list**. It sits in the canonical *plsX–fabD–fabG–acpP–fabF* cluster and must be added. **Second**, enoyl reduction is served **solely by FabV (PP_4635, NADH-dependent, EC 1.3.1.9)**: KT2440 encodes no FabI or FabL, so FabV is a single point of coverage for this step, not a redundant paralog. **Third**, ACP activation (holo-ACP synthesis, EC 2.7.8.7) is not performed by a dedicated AcpS; instead a single **bifunctional Sfp/EntD-type 4′-phosphopantetheinyl transferase (PP_1183)** most plausibly activates both AcpP and secondary-metabolite carrier proteins — a *Pseudomonas* lineage substitution rather than a genuine gap.

Consequently, several genes in the candidate bucket are **out-of-scope or over-propagated** annotations: the long-chain acyl-CoA ligases *fadD-I/II* (PP_4549/PP_4550) belong to β-oxidation/fatty-acid activation; PP_2783 is an aromatic (p-cumate) catabolism dehydrogenase; and PP_0581, PP_1852, and PP_2540 are bare short-chain dehydrogenase/reductase (SDR) paralogs with no gene name, EC, or function comment that were swept into the bucket by broad EC/GO mapping. The 84-aa PP_4529 "3-oxoacyl-ACP synthase" is a fragment, not a real condensing enzyme. The chain-initiation gene **PP_4379/FabH** is genuinely present but weakly and inconsistently annotated (labelled "synthase I" while carrying the KAS-III EC number 2.3.1.180) and should be promoted to full review, alongside **PP_1183** (ACP-activating PPTase) and **AcpP**.

---

## 2. Target-Organism Pathway Definition

### What the module includes

The module is the **dissociated bacterial FAS-II system**: a set of discrete, monofunctional, freely diffusing enzymes that iteratively build a saturated or *cis*-monounsaturated acyl chain on a small acidic acyl carrier protein (ACP). This is mechanistically and evolutionarily distinct from the **type-I FAS** of animals/fungi (a single large multidomain megasynthase) and from **type-I/type-II polyketide synthases**. In KT2440 the biochemical scope is:

1. **Malonyl-CoA formation** — biotin-dependent carboxylation of acetyl-CoA by the four-subunit AccABCD acetyl-CoA carboxylase.
2. **ACP provision and activation** — apo-AcpP is converted to holo-AcpP by transfer of a 4′-phosphopantetheine arm (PPTase; EC 2.7.8.7).
3. **Malonyl-ACP formation** — FabD transacylates malonate from CoA to holo-ACP.
4. **Chain initiation** — KAS-III (FabH) condenses acetyl-CoA with malonyl-ACP to give acetoacetyl-ACP.
5. **Iterative elongation** — a four-reaction cycle: KAS-I/KAS-II condensation → NADPH β-keto reduction (FabG) → (3R)-hydroxyacyl dehydration (FabZ/FabA) → enoyl reduction (FabV).
6. ***cis*-unsaturation branch** — FabA isomerizes trans-2- to cis-3-decenoyl-ACP; FabB elongates it, committing the chain to the unsaturated series (16:1, 18:1 vaccenate).

### Neighboring pathways to keep separate

- **KEGG ppu00071 / β-oxidation (fatty-acid degradation and activation):** the *fadD* long-chain acyl-CoA ligases (PP_4549/PP_4550) activate exogenous fatty acids for catabolism, **not** de novo synthesis. They should not satisfy any FAS-II step.
- **Aromatic-compound catabolism (p-cumate/biphenyl degradation):** PP_2783 is an SDR of this pathway, unrelated to acyl-ACP chemistry.
- **Phospholipid / membrane-lipid assembly (downstream):** PlsX/PlsB/PlsC acyltransferases consume acyl-ACP; they are the sink of FAS-II but not part of the elongation module.
- **Secondary-metabolite / polyketide biosynthesis:** shares the PPTase (PP_1183) and SDR/KS enzyme families, a frequent source of over-propagated annotations.
- **Broad overview maps** (KEGG map01100 "Metabolic pathways", map01212 "Fatty acid metabolism") aggregate synthesis + degradation and should not be used to define this module's boundaries.

### Alternate names / database definitions

Type-II FAS; dissociated FAS; FAS-II; KEGG "Fatty acid biosynthesis" (map00061 / ppu00061); MetaCyc "fatty acid biosynthesis initiation/elongation". Condensing enzymes carry the historical "β-ketoacyl-ACP synthase" (KAS I/II/III = FabB/FabF/FabH) nomenclature, which is a recurring source of EC/label confusion (see §5).

---

## 3. Expected Step Model and Satisfiability

| # | Step | Activity (EC) | KT2440 gene(s) | Status |
|---|------|---------------|----------------|--------|
| 1 | Malonyl-CoA formation | ACC (6.3.4.14 / 2.1.3.15) | accA PP_1607, accB PP_0559, accC PP_0558, accD PP_1996 | **covered** |
| 2a | ACP (carrier) | acyl carrier activity | **acpP PP_1915** | **covered (missing from list)** |
| 2b | ACP activation → holo-ACP | 2.7.8.7 | **PP_1183 (Sfp/EntD-type)** | **covered by lineage substitution** |
| 3 | Malonyl-ACP loading | 2.3.1.39 | fabD PP_1913 | **covered** |
| 4 | Chain initiation (KAS-III) | 2.3.1.180 | **PP_4379 (FabH)** | **covered (weak annotation)** |
| 5a | Condensation (KAS-I) | 2.3.1.41 | fabB PP_4175 | **covered** |
| 5a | Condensation (KAS-II) | 2.3.1.179 | fabF PP_1916 (+ paralog PP_3303) | **covered** |
| 5b | β-keto reduction | 1.1.1.100 | fabG PP_1914 | **covered** |
| 5c | Dehydration | 4.2.1.59 | fabZ PP_1602 (+ fabA PP_4174) | **covered** |
| 5d | Enoyl reduction | 1.3.1.9 (NADH) | **fabV PP_4635 (sole)** | **covered (single point)** |
| 6 | *cis*-unsaturation branch | 5.3.3.14 + 2.3.1.41 | fabA PP_4174 + fabB PP_4175 | **covered** |

**Every expected step is satisfiable.** Two entries require curator attention because the responsible gene is either missing from the metadata (AcpP) or provided by a lineage-specific alternative (PP_1183 for ACP activation; FabV as sole enoyl reductase).

---

## 4. Candidate Genes and Evidence

### High-confidence core genes (covered)

**Acetyl-CoA carboxylase — accA/B/C/D (PP_1607, PP_0559, PP_0558, PP_1996).** UniProt annotates the full heteromeric ACC: biotin carboxylase AccC (EC 6.3.4.14), biotin carboxyl carrier AccB, and the carboxyltransferase α/β subunits AccA/AccD (EC 2.1.3.15), with PATHWAY "malonyl-CoA biosynthesis; step 1/1". This is the committed entry into FAS-II and is fully covered (Finding F005).

**FabD (PP_1913, EC 2.3.1.39).** Malonyl-CoA:ACP transacylase, fabD family — canonical, unambiguous (F005). *Curation note:* the metadata assigns FabD to bucket `ppu00074`, but its function is squarely FAS-II; the bucket label is a database artifact, not a functional discrepancy.

**FabG (PP_1914, EC 1.1.1.100).** NADPH-dependent 3-oxoacyl-ACP reductase, located immediately upstream of *acpP* in the fab cluster — the canonical, essential β-keto reductase (F005). PP_0581 and PP_2540 (below) are **not** substitutes.

**FabZ (PP_1602, EC 4.2.1.59).** (3R)-hydroxyacyl-ACP dehydratase, the general elongation-cycle dehydratase; covered (F005).

**FabF (PP_1916, KAS-II, EC 2.3.1.179) and FabB (PP_4175, KAS-I, EC 2.3.1.41).** The two elongation condensing enzymes. FabF/PP_3303 carry the classic 16:1→18:1 *cis*-vaccenate thermal-regulation role in their UniProt FUNCTION text. **PP_3303 (EC 2.3.1.179)** is a genuine second KAS-II paralog (F005/F006) — a real duplication in *Pseudomonas*, not spurious. Curation may mark PP_3303 as **candidate/redundant paralog** (covered but not the primary).

**FabA (PP_4174, EC 4.2.1.59 + 5.3.3.14).** Bifunctional 3-hydroxydecanoyl-ACP dehydratase/isomerase — supplies both a dehydratase activity and, critically, the trans-2 → cis-3 isomerization that commits chains to the unsaturated series. Together with FabB it covers the entire *cis*-unsaturation branch (F005).

**FabV (PP_4635, EC 1.3.1.9, NADH).** The **sole** enoyl-ACP reductase (F002). This is a defining lineage feature: proteome searches (organism_id:160488) returned **0 hits for gene:fabI and 0 for gene:fabL**, while FabV is annotated as TER-reductase-family enoyl-ACP reductase with PATHWAY "fatty acid biosynthesis". The physiological importance of FabV in *Pseudomonas* is directly demonstrated in the sister species *P. aeruginosa* PAO1, where *fabV* deletion made cells >2,000-fold more triclosan-sensitive ([PMID: 19933806](https://pubmed.ncbi.nlm.nih.gov/19933806/)). Because it is a single point of coverage, FabV warrants a **covered but non-redundant** flag.

### Present but weakly annotated (covered, promote to review)

**PP_4379 / FabH (EC 2.3.1.180, KAS-III).** The **sole** KAS-III chain initiator: a proteome search for EC 2.3.1.180 in taxon 160488 returns exactly one hit, PP_4379, and no gene is annotated `fabH` (F003). It is, however, PE:4 "Predicted", carries **no recommended name and no EC in the current UniProt entry**, and the review metadata mislabels it "Beta-ketoacyl-ACP synthase I (EC 2.3.1.180)" — an internal inconsistency, since EC 2.3.1.180 is KAS-III (FabH), whereas KAS-I (EC 2.3.1.41) is the true *fabB* = PP_4175. Its 309-aa length is consistent with the FabH family. **Promote to full `fetch-gene` review** and re-annotate as *fabH*.

**PP_1183 (Sfp/EntD-type PPTase, EC 2.7.8.7 candidate).** ACP activation is an apparent gap by name — proteome searches for EC 2.7.8.7 and "holo-[acyl-carrier-protein] synthase" returned **0 hits**, and the InterPro AcpS/PPTase family IPR008278 in this proteome contains **exactly one protein: PP_1183**, an EntD/Sfp-type "Enterobactin synthase component D" (F006/F007). This mirrors the known *Pseudomonas* architecture in which a single Sfp-type PPTase activates both the primary FAS-II ACP and secondary-metabolite carrier proteins, replacing the enterobacterial two-PPTase (AcpS + EntD) system. This is a **lineage substitution, not a true gap**; promote PP_1183 to full review to confirm it acts on AcpP.

### Missing from the list but essential (add)

**AcpP (PP_1915, Q88LL5).** The acyl carrier protein — 78 aa, PE:1 "Evidence at protein level" (the highest tier) — is present and essential but **absent from the 19 candidate genes** (F001). It sits in the canonical cluster PP_1912 *plsX* – PP_1913 *fabD* – PP_1914 *fabG* – **PP_1915 *acpP*** – PP_1916 *fabF*, mirroring the *E. coli fabD-fabG-acpP-fabF* operon. Without ACP the entire module is mechanistically inoperable; this is the single most important metadata correction.

### Out-of-scope / likely over-propagated (exclude)

| Gene | Locus | UniProt annotation | Why excluded |
|------|-------|--------------------|--------------|
| fadD-I | PP_4549 | Long-chain acyl-CoA ligase, EC 6.2.1.3 | PATHWAY = β-oxidation; fatty-acid **activation**, not synthesis (F004) |
| fadD-II | PP_4550 | Long-chain acyl-CoA ligase, EC 6.2.1.3 | Same as above (F004) |
| PP_2783 | PP_2783 | 2,3-dihydroxy-p-cumate dehydrogenase, EC 1.3.1.58 | PATHWAY = p-cumate degradation; aromatic catabolism SDR (F004) |
| PP_0581 | PP_0581 | "SDR family", no gene/EC/function (PE:3) | Generic SDR propagated by broad GO/EC mapping (F004) |
| PP_1852 | PP_1852 | "SDR family", no gene/EC/function (PE:3) | Metadata labels it "enoyl-ACP reductase EC 1.3.1.10" but UniProt gives no such evidence; enoyl step already covered by FabV (F002/F004) |
| PP_2540 | PP_2540 | "SDR family", no gene/EC/function (PE:3) | Generic SDR (F004) |
| PP_4529 | PP_4529 | "3-oxoacyl-ACP synthase", PE:4, **84 aa** | Far too short for a ~330–410 aa KAS; fragment/spurious (F007) |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**No genuine pathway gaps.** All four elongation activities, initiation, loading, malonyl-CoA supply, the carrier, and the unsaturation branch are encoded. The two apparent "gaps" resolve to lineage substitutions:

- **ACP activation (EC 2.7.8.7):** no dedicated AcpS; PP_1183 (Sfp/EntD-type) is the sole PPTase and the most plausible AcpP activator (F006/F007). Mark **covered by lineage substitution**, not gap.
- **Enoyl reduction (EC 1.3.1.9):** no FabI/FabL; FabV is the sole reductase (F002). Mark **covered (single point)**.

**Paralog ambiguity.**
- **KAS-II:** two paralogs share EC 2.3.1.179 — FabF (PP_1916) and PP_3303. Primary = FabF; PP_3303 = candidate/redundant.
- **β-keto reductase family:** PP_0581, PP_2540 (and the mislabelled PP_1852) are bare SDRs pulled into the bucket by the broad SDR/oxidoreductase GO terms. FabG (PP_1914) is the real reductase; the others are **likely over-annotation**.

**Nomenclature/EC mislabels (curation-relevant).**
- PP_4379: labelled "synthase I" but EC 2.3.1.180 = KAS-III/FabH. Fix name → *fabH*.
- PP_1852: metadata claims "Enoyl-ACP reductase (NADPH, B-specific) EC 1.3.1.10" but UniProt carries only a generic SDR annotation with no EC. Do not treat as an enoyl reductase.
- FabD bucket `ppu00074` and several genes bucketed to `ppu00780` reflect KEGG sub-map fragmentation; functionally all are FAS-II.

**Broad EC/GO over-propagation.** The recurring pattern is generic **SDR-family** and **"oxidoreductase"** annotations (PP_0581, PP_1852, PP_2540, PP_2783) being swept into a fatty-acid-synthesis bucket. These should be demoted unless direct evidence links them to acyl-ACP substrates.

---

## 6. Mechanistic Model

```
   acetyl-CoA
       │  AccABCD (accA PP_1607 / accB PP_0559 / accC PP_0558 / accD PP_1996)
       ▼
   malonyl-CoA
       │  FabD (PP_1913)              apo-AcpP (PP_1915)
       ▼                                   │ PP_1183 (Sfp/EntD PPTase, EC 2.7.8.7)
   malonyl-ACP  ◄───── holo-AcpP ◄─────────┘
       │
       │  FabH / PP_4379 (KAS-III, EC 2.3.1.180)  + acetyl-CoA
       ▼
   acetoacetyl-ACP
       │
   ┌───┴─────────────── ELONGATION CYCLE ───────────────────┐
   │  ① FabB PP_4175 (KAS-I) / FabF PP_1916 (+PP_3303) KAS-II │
   │  ② FabG PP_1914  (β-keto reduction, NADPH)               │
   │  ③ FabZ PP_1602 / FabA PP_4174 (dehydration)             │
   │  ④ FabV PP_4635  (enoyl reduction, NADH — SOLE ENR)      │
   └──────────────────────────┬──────────────────────────────┘
                              │  at C10: FabA isomerization (5.3.3.14)
                              ▼
                     cis-3-decenoyl-ACP ──FabB──► 16:1 / 18:1 (cis-vaccenate)
                              │
                              ▼
                     acyl-ACP → membrane phospholipids (PlsX/B/C, downstream)
```

The narrative: KT2440 runs a textbook dissociated FAS-II with two *Pseudomonas*-specific twists — a **single Sfp/EntD-type PPTase** replacing the enterobacterial AcpS, and a **single NADH-dependent FabV** replacing FabI as the enoyl reductase (with no FabL backup). These are exactly the features a naive homology transfer from *E. coli* would miss, which is why the module needs the explicit PPTase sub-step and the FabV-only enoyl node.

---

## 7. Module and GO-Curation Recommendations

**Module-step dispositions:**

| Module step | Disposition | Rationale |
|-------------|-------------|-----------|
| Malonyl-CoA formation (ACC) | **covered** | accABCD canonical |
| Acyl carrier protein | **covered — metadata fix** | add AcpP PP_1915 (F001) |
| ACP activation (holo-ACP) | **covered — lineage substitution** | PP_1183 Sfp/EntD PPTase; add sub-step + note (F007) |
| Malonyl-ACP loading (FabD) | **covered** | PP_1913 |
| Chain initiation (KAS-III) | **covered — candidate_uncertain annotation** | PP_4379/FabH; promote & re-annotate (F003) |
| Condensation KAS-I/II | **covered** | fabB, fabF (+PP_3303 redundant) |
| β-keto reduction | **covered** | fabG; exclude SDR paralogs |
| Dehydration | **covered** | fabZ (+fabA) |
| Enoyl reduction | **covered — single point** | FabV only; no FabI/FabL (F002) |
| *cis*-unsaturation branch | **covered** | fabA + fabB |

**Module-boundary / document actions:**
1. **Add AcpP (PP_1915)** as an explicit module player — the generic outline names "PSEPK canonical AcpP" but the locus is absent from candidates.
2. **Add an ACP-activation (PPTase, EC 2.7.8.7) sub-step** to the module with PP_1183 as a *Pseudomonas*-specific bifunctional Sfp/EntD-type player, distinct from enterobacterial AcpS. Add a GO/module note that in *Pseudomonas* a single Sfp-type PPTase serves both primary and secondary metabolism.
3. **Flag the enoyl-reduction node as FabV-only** (NADH, EC 1.3.1.9) and remove the PP_1852 "NADPH-dependent reductase (EC 1.3.1.10)" variant from the module unless direct evidence emerges — the current outline over-represents an enoyl-ACP reductase paralog with no supporting UniProt annotation.
4. **Remove/relabel out-of-scope genes** fadD-I/II, PP_2783, PP_0581, PP_2540, PP_4529 from the FAS-II bucket.
5. **No new GO term requests are strictly required**, but a curation note distinguishing the *Pseudomonas* single-Sfp-PPTase architecture from the two-enzyme enterobacterial model would prevent future "acpS gap" false positives.

Existing generic module boundaries are largely correct; the main corrections are that the module should explicitly encode the **PPTase activation sub-step** and the **FabV-only enoyl node**, and should not carry an NADPH enoyl-reductase variant for this organism.

---

## 8. Genes to Promote to Full `fetch-gene` Review

1. **PP_4379 (FabH / KAS-III, EC 2.3.1.180)** — sole chain initiator, PE:4, no name/EC in UniProt, mislabelled "synthase I". Highest priority: it anchors initiation and its annotation is internally inconsistent (F003).
2. **PP_1183 (Sfp/EntD-type PPTase, EC 2.7.8.7 candidate)** — sole PPTase; confirm it activates AcpP (holo-ACP synthesis) versus being dedicated to siderophore carriers (F007).
3. **AcpP (PP_1915)** — add to the module and confirm as the canonical FAS-II carrier (PE:1) (F001).
4. *(Secondary)* **PP_3303** — confirm KAS-II redundancy vs. specialized role; **FabV (PP_4635)** — confirm sole-enoyl-reductase status and cofactor.

---

## 9. Evidence Base

| Evidence | Source | Type | Supports |
|----------|--------|------|----------|
| FabV deletion → >2,000-fold triclosan hypersensitivity in *P. aeruginosa* PAO1; FabI-only mutant stays resistant | [PMID: 19933806](https://pubmed.ncbi.nlm.nih.gov/19933806/) | Direct experiment (sister species) | FabV is a functional, physiologically dominant enoyl-ACP reductase in *Pseudomonas* (F002) |
| acpP PP_1915 PE:1, 78 aa, in plsX-fabD-fabG-acpP-fabF cluster | UniProt Q88LL5 | Protein-level annotation (target) | AcpP present & essential (F001) |
| 0 hits for fabI/fabL; fabV = TER-reductase-family ENR | UniProt proteome 160488 | Homology/proteome census (target) | FabV sole ENR (F002) |
| EC 2.3.1.180 → single hit PP_4379; no fabH gene | UniProt proteome 160488 | Proteome census (target) | Sole KAS-III initiator (F003) |
| ACC, FabD, FabG, FabZ, FabF, FabB, FabA pathway-consistent | UniProt (target) | Annotation (target) | Core elongation covered (F005) |
| IPR008278 PPTase family = single protein PP_1183 (EntD/Sfp) | UniProt/InterPro (target) | Family census (target) | ACP activation by lineage substitution (F007) |
| fadD-I/II PATHWAY = β-oxidation; PP_2783 = p-cumate | UniProt (target) | Annotation (target) | Out-of-scope genes (F004) |

The **species-transfer strength** varies. Target-organism UniProt/InterPro evidence is **strong/direct** for gene presence and family membership. The FabV physiological-dominance claim is **direct in *P. aeruginosa* PAO1** and transfers **strongly** to *P. putida* KT2440 (same genus, identical FabV-family enzyme, no FabI/FabL in either). The supporting quote from [PMID: 19933806](https://pubmed.ncbi.nlm.nih.gov/19933806/): *"Upon deletion of the fabV gene, the mutant strain became extremely sensitive to triclosan (>2,000-fold more sensitive than the wild-type strain), whereas the mutant strain lacking FabI remained completely resistant to the biocide."* No dedicated KT2440 biochemical study of PP_4379/FabH or PP_1183 was found; these remain **homology/family-level inferences** (hence the promotion recommendations). Retrieved rhamnolipid/PHA papers (e.g., [PMID: 41117507](https://pubmed.ncbi.nlm.nih.gov/41117507/), [PMID: 41046915](https://pubmed.ncbi.nlm.nih.gov/41046915/), [PMID: 42393666](https://pubmed.ncbi.nlm.nih.gov/42393666/)) confirm that de novo FAS supplies acyl precursors in KT2440 metabolism but do not test individual FAS-II gene functions.

---

## 10. Limitations and Knowledge Gaps

- **No direct KT2440 biochemistry** was located for PP_4379/FabH (initiation) or PP_1183 (ACP activation); both rest on family/EC inference. The FabH annotation is internally inconsistent and PE:4.
- **PP_1183 substrate scope** is unconfirmed — whether it activates AcpP in addition to siderophore carrier proteins is inferred from the *Pseudomonas* single-PPTase paradigm, not demonstrated in KT2440.
- **PP_3303 role** (specialized vs. redundant KAS-II) is unresolved.
- The **SDR paralogs** (PP_0581, PP_2540, PP_1852) have no functional data; their exclusion is based on absence of specific annotation, which is suggestive but not definitive.
- Analysis was annotation- and literature-based (UniProt, InterPro, KEGG, PubMed); no experimental or structural validation was performed in this review.

---

## 11. Proposed Follow-up Actions

1. **Curate AcpP (PP_1915) into the module** as the carrier player — immediate, high-value metadata fix.
2. **Promote PP_4379 to full `fetch-gene` review**; re-annotate as *fabH*, EC 2.3.1.180, KAS-III initiator; correct the "synthase I" mislabel.
3. **Promote PP_1183 to full review**; add an ACP-activation sub-step (EC 2.7.8.7) and confirm bifunctional Sfp/EntD-type activity on AcpP (e.g., in-vitro holo-ACP synthase assay, or conditional-lethality/ACP-modification phenotype).
4. **Flag FabV (PP_4635) as the sole enoyl reductase**; a Δ*fabV* triclosan-sensitivity assay in KT2440 would directly confirm (mirroring the PAO1 result).
5. **Remove out-of-scope genes** (fadD-I/II, PP_2783, PP_0581, PP_2540, PP_4529) and the metadata's PP_1852 "enoyl reductase" claim from the FAS-II bucket.
6. **Add a curation note** distinguishing the *Pseudomonas* single-Sfp-PPTase architecture from the enterobacterial AcpS+EntD system, to suppress future false "acpS gap" flags.

---

### Key References

- Zhu L, *et al.* *Triclosan resistance of Pseudomonas aeruginosa PAO1 is due to FabV, a triclosan-resistant enoyl-acyl carrier protein reductase.* [PMID: 19933806](https://pubmed.ncbi.nlm.nih.gov/19933806/)
- *Heterologous rhamnolipid biosynthesis — role of de novo fatty acid synthesis in supplying the hydrophobic moiety.* [PMID: 41117507](https://pubmed.ncbi.nlm.nih.gov/41117507/)
- *Co-feeding phenolic acids with fatty acids for PHA synthesis in P. putida KT2440.* [PMID: 41046915](https://pubmed.ncbi.nlm.nih.gov/41046915/)
- *Acetate as alternative carbon source for rhamnolipid production in P. putida KT2440 (de novo FAS precursor supply).* [PMID: 42393666](https://pubmed.ncbi.nlm.nih.gov/42393666/)
- Primary annotation sources: UniProt proteome UP000000556 / taxon 160488 (Q88LL5 AcpP, Q88E33 FabV, Q88ES4 PP_4379, Q88NM4 PP_1183, and core fab/acc entries); InterPro IPR008278 (PPTase family); KEGG ppu00061.


## Artifacts

- [OpenScientist final report](PSEPK__type_ii_fatty_acid_synthesis__ppu00061-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__type_ii_fatty_acid_synthesis__ppu00061-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19933806
2. PMID:41117507
3. PMID:41046915
4. PMID:42393666