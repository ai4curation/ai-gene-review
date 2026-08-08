---
provider: openscientist
model: openscientist-autonomous
cached: true
start_time: '2026-07-20T18:21:06.141231'
end_time: '2026-07-20T18:21:06.143925'
duration_seconds: 0.0
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-aspartate de novo and selected salvage routes to NAD+
  module_summary: 'A reusable, scope-limited route set for organisms that use the
    L-aspartate de novo pathway and/or selected nicotinate, nicotinamide, and NMN
    salvage alternatives. Every realization is end-to-end: NaMN made by L-aspartate
    de novo synthesis, PncB, or PncC must pass through deamido-NAD to NAD+, whereas
    NMN made by NAMPT must be adenylylated directly to NAD+. Alternative adenylyltransferase
    families and NAD synthetase nitrogen donors are modeled as variants. This is not
    a universal NAD+ biosynthesis hub: de novo synthesis through L-tryptophan and
    the kynurenine pathway is owned by the existing MODULE:kynurenine_nad_de_novo
    module and is not duplicated here. Nicotinate degradation, pyridine-nucleotide
    transhydrogenases, NAD kinase and NADP formation, NAD-consuming reactions, and
    unrelated aldehyde metabolism are outside the boundary.'
  module_outline: "- L-aspartate de novo and selected salvage routes to NAD+\n  -\
    \ Alternative versions by precursor deamidation state and completion chemistry:\
    \ Complete NAD+ route realization\n    - NaMN-producing routes with deamido-NAD\
    \ completion\n      - 1. produce NaMN by de novo synthesis or deamidated salvage\n\
    \      - NaMN-producing precursor alternatives\n        - Alternative versions\
    \ by source precursor and deamidation sequence: NaMN-producing route\n       \
    \   - De novo NaMN synthesis from L-aspartate\n            - 1. L-aspartate oxidation\n\
    \            - L-aspartate oxidase step\n              - L-aspartate oxidase (molecular\
    \ player: L-aspartate oxidase family; activity or role: L-aspartate oxidase activity)\n\
    \            - 2. quinolinate formation\n            - Quinolinate synthase step\n\
    \              - Quinolinate synthase A (molecular player: quinolinate synthase\
    \ A family; activity or role: quinolinate synthetase A activity)\n           \
    \ - 3. quinolinate phosphoribosylation to NaMN\n            - Quinolinate phosphoribosyltransferase\
    \ step\n              - Nicotinate-nucleotide diphosphorylase (carboxylating)\
    \ (molecular player: quinolinate phosphoribosyltransferase family; activity or\
    \ role: nicotinate-nucleotide diphosphorylase (carboxylating) activity)\n    \
    \      - Direct nicotinate Preiss-Handler entry\n            - Nicotinate phosphoribosyltransferase\
    \ (molecular player: nicotinate phosphoribosyltransferase family; activity or\
    \ role: nicotinate phosphoribosyltransferase activity)\n          - Nicotinamide\
    \ deamidation followed by Preiss-Handler entry\n            - 1. nicotinamide\
    \ deamidation\n            - Nicotinamidase step\n              - Nicotinamidase\
    \ (molecular player: nicotinamidase family; activity or role: nicotinamidase activity)\n\
    \            - 2. nicotinate phosphoribosylation\n            - PncB step after\
    \ PncA\n              - Nicotinate phosphoribosyltransferase (molecular player:\
    \ nicotinate phosphoribosyltransferase family; activity or role: nicotinate phosphoribosyltransferase\
    \ activity)\n          - NMN deamidation to NaMN\n            - Nicotinamide-nucleotide\
    \ amidase PncC (molecular player: PncC/CinA C-terminal NMN deamidase family; activity\
    \ or role: nicotinamide-nucleotide amidase activity)\n      - 2. complete NaMN\
    \ through deamido-NAD to NAD+\n      - Shared NaMN completion through deamido-NAD\n\
    \        - 1. NaMN adenylylation to deamido-NAD\n        - NaMN adenylylation\
    \ alternatives\n          - Alternative versions by enzyme family: NaMN adenylyltransferase\
    \ family\n            - Bacterial NadD-family NaMN adenylyltransferase\n     \
    \         - Nicotinate-nucleotide adenylyltransferase (molecular player: bacterial\
    \ NadD family; activity or role: nicotinate-nucleotide adenylyltransferase activity)\n\
    \            - Bifunctional NMNAT-family NaMN adenylylation\n              - NMNAT\
    \ nicotinate-nucleotide adenylyltransferase activity (molecular player: eukaryotic\
    \ NMN adenylyltransferase family; activity or role: nicotinate-nucleotide adenylyltransferase\
    \ activity)\n        - 2. deamido-NAD amidation to NAD+\n        - NAD synthetase\
    \ nitrogen-donor alternatives\n          - Alternative versions by nitrogen donor\
    \ and enzyme architecture: NAD synthetase nitrogen donor\n            - Ammonia-dependent\
    \ NAD synthetase\n              - Ammonia-dependent NAD+ synthase (molecular player:\
    \ ammonia-dependent NAD synthetase subfamily; activity or role: NAD+ synthase\
    \ activity)\n            - Glutamine-dependent NAD synthetase\n              -\
    \ Glutamine-dependent NAD+ synthase (molecular player: human glutamine-dependent\
    \ NAD synthetase NADSYN1; activity or role: NAD+ synthase (glutamine-hydrolyzing)\
    \ activity)\n    - NAMPT-produced NMN with direct NAD+ completion\n      - 1.\
    \ produce NMN from nicotinamide\n      - Nicotinamide phosphoribosylation to NMN\n\
    \        - Nicotinamide phosphoribosyltransferase (molecular player: nicotinamide\
    \ phosphoribosyltransferase family; activity or role: nicotinamide phosphoribosyltransferase\
    \ activity)\n      - 2. adenylylate NMN directly to NAD+\n      - Direct amidated\
    \ NMN completion\n        - Nicotinamide-nucleotide adenylyltransferase (molecular\
    \ player: eukaryotic NMN adenylyltransferase family; activity or role: nicotinamide-nucleotide\
    \ adenylyltransferase activity)"
  module_connections: '- De novo NaMN synthesis from L-aspartate feeds into Shared
    NaMN completion through deamido-NAD: The L-aspartate de novo route supplies NaMN
    to shared completion.

    - Direct nicotinate Preiss-Handler entry feeds into Shared NaMN completion through
    deamido-NAD: Direct nicotinate phosphoribosylation supplies NaMN to shared completion.

    - Nicotinamide deamidation followed by Preiss-Handler entry feeds into Shared
    NaMN completion through deamido-NAD: PncA followed by PncB supplies NaMN to shared
    completion.

    - NMN deamidation to NaMN feeds into Shared NaMN completion through deamido-NAD:
    PncC deamidation supplies NaMN to shared completion.

    - L-aspartate oxidase step feeds into Quinolinate synthase step: NadB supplies
    iminoaspartate to NadA.

    - Quinolinate synthase step feeds into Quinolinate phosphoribosyltransferase step:
    NadA supplies quinolinate to NadC.

    - Nicotinamidase step feeds into PncB step after PncA: PncA supplies nicotinate
    to PncB.

    - NaMN adenylylation alternatives feeds into NAD synthetase nitrogen-donor alternatives:
    NaMN adenylylation supplies deamido-NAD to NAD synthetase.

    - Nicotinamide phosphoribosylation to NMN feeds into Direct amidated NMN completion:
    NAMPT supplies NMN specifically to direct NMN adenylylation.'
  pathway_query: ppu00760
  pathway_id: ppu00760
  pathway_name: Nicotinate and nicotinamide metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00760 with 25 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '30'
  candidate_genes: '- pntB: PP_0155 | Q88RH4 | NAD(P) transhydrogenase subunit beta
    (EC 7.1.1.1) (Nicotinamide nucleotide transhydrogenase subunit beta) (EC 7.1.1.1;
    primary bucket kegg:ppu00760)

    - pntAA: PP_0156 | A0A140FVX4 | NAD(P) transhydrogenase subunit alpha part 1 (EC
    7.1.1.1) (Nicotinamide nucleotide transhydrogenase subunit alpha 1) (Pyridine
    nucleotide transhydrogenase subunit alpha 1) (EC 7.1.1.1; primary bucket kegg:ppu00760)

    - davD: PP_0213 | Q88RC0 | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) (EC
    1.2.1.-; primary bucket kegg:ppu00350)

    - nadC: PP_0787 | Q88PR1 | Probable nicotinate-nucleotide pyrophosphorylase [carboxylating]
    (EC 2.4.2.19) (Quinolinate phosphoribosyltransferase [decarboxylating]) (EC 2.4.2.19;
    primary bucket kegg:ppu00760)

    - nadA: PP_1231 | Q88NH8 | Quinolinate synthase (EC 2.5.1.72) (EC 2.5.1.72; primary
    bucket kegg:ppu00760)

    - ushA: PP_1414 | Q88N04 | 5''-nucleotidase-2'',3''-cyclic phosphodiesterase (EC
    3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) (EC 3.1.3.5; 3.1.4.16; 3.6.1.45; primary bucket
    kegg:ppu00760)

    - nadB: PP_1426 | Q88MZ2 | L-aspartate oxidase (EC 1.4.3.16) (EC 1.4.3.16; primary
    bucket kegg:ppu00760)

    - surE: PP_1620 | Q88MF1 | 5''-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5''-monophosphate
    phosphohydrolase) (EC 3.1.3.5; primary bucket kegg:ppu00760)

    - pncC: PP_1628 | Q88ME5 | NMN amidohydrolase (EC 3.5.1.42) (EC 3.5.1.42; primary
    bucket kegg:ppu00760)

    - mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8)
    (EC 3.6.1.8; primary bucket kegg:ppu00770)

    - nadK: PP_2012 | Q88LC3 | NAD kinase (EC 2.7.1.23) (ATP-dependent NAD kinase)
    (EC 2.7.1.23; primary bucket kegg:ppu00760)

    - sthA: PP_2151 | Q88KY8 | Soluble pyridine nucleotide transhydrogenase (STH)
    (EC 1.6.1.1) (NAD(P)(+) transhydrogenase [B-specific]) (EC 1.6.1.1; primary bucket
    kegg:ppu00760)

    - sad-I: PP_2488 | Q88K05 | NAD+-dependent succinate semialdehyde dehydrogenase
    (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00350)

    - PP_2531: PP_2531 | Q88JW6 | 5-nucleotidase (primary bucket kegg:ppu00760)

    - PP_3103: PP_3103 | Q88I96 | Uncharacterized protein (primary bucket kegg:ppu00760)

    - sad-II: PP_3151 | Q88I50 | NAD+-dependent succinate semialdehyde dehydrogenase
    (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00760)

    - nicF: PP_3941 | Q88FY5 | Maleamate amidohydrolase (EC 3.5.1.107) (Nicotinate
    degradation protein F) (EC 3.5.1.107; primary bucket kegg:ppu00760)

    - maiA: PP_3942 | Q88FY4 | Maleate isomerase (EC 5.2.1.1) (Maleate cis-trans isomerase)
    (Nicotinate degradation protein E) (EC 5.2.1.1; primary bucket kegg:ppu00760)

    - nicD: PP_3943 | Q88FY3 | N-formylmaleamate deformylase (EC 3.5.1.106) (Nicotinate
    degradation protein D) (EC 3.5.1.106; primary bucket kegg:ppu00760)

    - nicC: PP_3944 | Q88FY2 | 6-hydroxynicotinate 3-monooxygenase (6-HNA monooxygenase)
    (EC 1.14.13.114) (Nicotinate degradation protein C) (EC 1.14.13.114; primary bucket
    kegg:ppu00760)

    - nicX: PP_3945 | Q88FY1 | 2,5-dihydroxypyridine 5,6-dioxygenase (2,5-DHP dioxygenase)
    (EC 1.13.11.9) (Nicotinate degradation protein X) (EC 1.13.11.9; primary bucket
    kegg:ppu00760)

    - nicA: PP_3947 | Q88FX9 | Nicotinate dehydrogenase subunit A (EC 1.17.2.1) (Nicotinate
    degradation protein A) (Nicotinate dehydrogenase small subunit) (EC 1.17.2.1;
    primary bucket kegg:ppu00760)

    - nicB: PP_3948 | Q88FX8 | Nicotinate dehydrogenase subunit B (EC 1.17.2.1) (Nicotinate
    degradation protein B) (Nicotinate dehydrogenase large subunit) (EC 1.17.2.1;
    primary bucket kegg:ppu00760)

    - nudC: PP_4029 | Q88FQ8 | NAD-capped RNA hydrolase NudC (DeNADding enzyme NudC)
    (EC 3.6.1.-) (NADH pyrophosphatase) (EC 3.6.1.22) (EC 3.6.1.-; 3.6.1.22; primary
    bucket kegg:ppu04146)

    - gabD-II: PP_4422 | Q88EN2 | Succinate-semialdehyde dehydrogenase (NADP+) (EC
    1.2.1.79) (EC 1.2.1.79; primary bucket kegg:ppu00350)

    - nadD: PP_4810 | Q88DL5 | Probable nicotinate-nucleotide adenylyltransferase
    (EC 2.7.7.18) (Deamido-NAD(+) diphosphorylase) (Deamido-NAD(+) pyrophosphorylase)
    (Nicotinate mononucleotide adenylyltransferase) (NaMN adenylyltransferase) (EC
    2.7.7.18; primary bucket kegg:ppu00760)

    - pncB: PP_4868 | Q88DF7 | Nicotinate phosphoribosyltransferase (NAPRTase) (EC
    6.3.4.21) (EC 6.3.4.21; primary bucket kegg:ppu00760)

    - nadE: PP_4869 | Q88DF6 | NH(3)-dependent NAD(+) synthetase (EC 6.3.1.5) (EC
    6.3.1.5; primary bucket kegg:ppu00760)

    - cobB__Q88BY5: PP_5402 | Q88BY5 | NAD-dependent protein deacylase (EC 2.3.1.286)
    (Regulatory protein SIR2 homolog) (EC 2.3.1.286; primary bucket kegg:ppu00760)

    - pntAB: PP_5747 | A0A140FVX3 | proton-translocating NAD(P)(+) transhydrogenase
    (EC 7.1.1.1) (EC 7.1.1.1; primary bucket kegg:ppu00760)'
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__nad_biosynthesis_salvage__ppu00760-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__nad_biosynthesis_salvage__ppu00760-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-aspartate de novo and selected salvage routes to NAD+ in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00760
- Resolved ID: ppu00760
- Resolved name: Nicotinate and nicotinamide metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00760 with 25 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 30

- pntB: PP_0155 | Q88RH4 | NAD(P) transhydrogenase subunit beta (EC 7.1.1.1) (Nicotinamide nucleotide transhydrogenase subunit beta) (EC 7.1.1.1; primary bucket kegg:ppu00760)
- pntAA: PP_0156 | A0A140FVX4 | NAD(P) transhydrogenase subunit alpha part 1 (EC 7.1.1.1) (Nicotinamide nucleotide transhydrogenase subunit alpha 1) (Pyridine nucleotide transhydrogenase subunit alpha 1) (EC 7.1.1.1; primary bucket kegg:ppu00760)
- davD: PP_0213 | Q88RC0 | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) (EC 1.2.1.-; primary bucket kegg:ppu00350)
- nadC: PP_0787 | Q88PR1 | Probable nicotinate-nucleotide pyrophosphorylase [carboxylating] (EC 2.4.2.19) (Quinolinate phosphoribosyltransferase [decarboxylating]) (EC 2.4.2.19; primary bucket kegg:ppu00760)
- nadA: PP_1231 | Q88NH8 | Quinolinate synthase (EC 2.5.1.72) (EC 2.5.1.72; primary bucket kegg:ppu00760)
- ushA: PP_1414 | Q88N04 | 5'-nucleotidase-2',3'-cyclic phosphodiesterase (EC 3.1.3.5, EC 3.1.4.16, EC 3.6.1.45) (EC 3.1.3.5; 3.1.4.16; 3.6.1.45; primary bucket kegg:ppu00760)
- nadB: PP_1426 | Q88MZ2 | L-aspartate oxidase (EC 1.4.3.16) (EC 1.4.3.16; primary bucket kegg:ppu00760)
- surE: PP_1620 | Q88MF1 | 5'-nucleotidase SurE (EC 3.1.3.5) (Nucleoside 5'-monophosphate phosphohydrolase) (EC 3.1.3.5; primary bucket kegg:ppu00760)
- pncC: PP_1628 | Q88ME5 | NMN amidohydrolase (EC 3.5.1.42) (EC 3.5.1.42; primary bucket kegg:ppu00760)
- mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) (EC 3.6.1.8; primary bucket kegg:ppu00770)
- nadK: PP_2012 | Q88LC3 | NAD kinase (EC 2.7.1.23) (ATP-dependent NAD kinase) (EC 2.7.1.23; primary bucket kegg:ppu00760)
- sthA: PP_2151 | Q88KY8 | Soluble pyridine nucleotide transhydrogenase (STH) (EC 1.6.1.1) (NAD(P)(+) transhydrogenase [B-specific]) (EC 1.6.1.1; primary bucket kegg:ppu00760)
- sad-I: PP_2488 | Q88K05 | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00350)
- PP_2531: PP_2531 | Q88JW6 | 5-nucleotidase (primary bucket kegg:ppu00760)
- PP_3103: PP_3103 | Q88I96 | Uncharacterized protein (primary bucket kegg:ppu00760)
- sad-II: PP_3151 | Q88I50 | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00760)
- nicF: PP_3941 | Q88FY5 | Maleamate amidohydrolase (EC 3.5.1.107) (Nicotinate degradation protein F) (EC 3.5.1.107; primary bucket kegg:ppu00760)
- maiA: PP_3942 | Q88FY4 | Maleate isomerase (EC 5.2.1.1) (Maleate cis-trans isomerase) (Nicotinate degradation protein E) (EC 5.2.1.1; primary bucket kegg:ppu00760)
- nicD: PP_3943 | Q88FY3 | N-formylmaleamate deformylase (EC 3.5.1.106) (Nicotinate degradation protein D) (EC 3.5.1.106; primary bucket kegg:ppu00760)
- nicC: PP_3944 | Q88FY2 | 6-hydroxynicotinate 3-monooxygenase (6-HNA monooxygenase) (EC 1.14.13.114) (Nicotinate degradation protein C) (EC 1.14.13.114; primary bucket kegg:ppu00760)
- nicX: PP_3945 | Q88FY1 | 2,5-dihydroxypyridine 5,6-dioxygenase (2,5-DHP dioxygenase) (EC 1.13.11.9) (Nicotinate degradation protein X) (EC 1.13.11.9; primary bucket kegg:ppu00760)
- nicA: PP_3947 | Q88FX9 | Nicotinate dehydrogenase subunit A (EC 1.17.2.1) (Nicotinate degradation protein A) (Nicotinate dehydrogenase small subunit) (EC 1.17.2.1; primary bucket kegg:ppu00760)
- nicB: PP_3948 | Q88FX8 | Nicotinate dehydrogenase subunit B (EC 1.17.2.1) (Nicotinate degradation protein B) (Nicotinate dehydrogenase large subunit) (EC 1.17.2.1; primary bucket kegg:ppu00760)
- nudC: PP_4029 | Q88FQ8 | NAD-capped RNA hydrolase NudC (DeNADding enzyme NudC) (EC 3.6.1.-) (NADH pyrophosphatase) (EC 3.6.1.22) (EC 3.6.1.-; 3.6.1.22; primary bucket kegg:ppu04146)
- gabD-II: PP_4422 | Q88EN2 | Succinate-semialdehyde dehydrogenase (NADP+) (EC 1.2.1.79) (EC 1.2.1.79; primary bucket kegg:ppu00350)
- nadD: PP_4810 | Q88DL5 | Probable nicotinate-nucleotide adenylyltransferase (EC 2.7.7.18) (Deamido-NAD(+) diphosphorylase) (Deamido-NAD(+) pyrophosphorylase) (Nicotinate mononucleotide adenylyltransferase) (NaMN adenylyltransferase) (EC 2.7.7.18; primary bucket kegg:ppu00760)
- pncB: PP_4868 | Q88DF7 | Nicotinate phosphoribosyltransferase (NAPRTase) (EC 6.3.4.21) (EC 6.3.4.21; primary bucket kegg:ppu00760)
- nadE: PP_4869 | Q88DF6 | NH(3)-dependent NAD(+) synthetase (EC 6.3.1.5) (EC 6.3.1.5; primary bucket kegg:ppu00760)
- cobB__Q88BY5: PP_5402 | Q88BY5 | NAD-dependent protein deacylase (EC 2.3.1.286) (Regulatory protein SIR2 homolog) (EC 2.3.1.286; primary bucket kegg:ppu00760)
- pntAB: PP_5747 | A0A140FVX3 | proton-translocating NAD(P)(+) transhydrogenase (EC 7.1.1.1) (EC 7.1.1.1; primary bucket kegg:ppu00760)

## Generic Module Context

### Working Scope

A reusable, scope-limited route set for organisms that use the L-aspartate de novo pathway and/or selected nicotinate, nicotinamide, and NMN salvage alternatives. Every realization is end-to-end: NaMN made by L-aspartate de novo synthesis, PncB, or PncC must pass through deamido-NAD to NAD+, whereas NMN made by NAMPT must be adenylylated directly to NAD+. Alternative adenylyltransferase families and NAD synthetase nitrogen donors are modeled as variants. This is not a universal NAD+ biosynthesis hub: de novo synthesis through L-tryptophan and the kynurenine pathway is owned by the existing MODULE:kynurenine_nad_de_novo module and is not duplicated here. Nicotinate degradation, pyridine-nucleotide transhydrogenases, NAD kinase and NADP formation, NAD-consuming reactions, and unrelated aldehyde metabolism are outside the boundary.

### Provisional Biological Outline

- L-aspartate de novo and selected salvage routes to NAD+
  - Alternative versions by precursor deamidation state and completion chemistry: Complete NAD+ route realization
    - NaMN-producing routes with deamido-NAD completion
      - 1. produce NaMN by de novo synthesis or deamidated salvage
      - NaMN-producing precursor alternatives
        - Alternative versions by source precursor and deamidation sequence: NaMN-producing route
          - De novo NaMN synthesis from L-aspartate
            - 1. L-aspartate oxidation
            - L-aspartate oxidase step
              - L-aspartate oxidase (molecular player: L-aspartate oxidase family; activity or role: L-aspartate oxidase activity)
            - 2. quinolinate formation
            - Quinolinate synthase step
              - Quinolinate synthase A (molecular player: quinolinate synthase A family; activity or role: quinolinate synthetase A activity)
            - 3. quinolinate phosphoribosylation to NaMN
            - Quinolinate phosphoribosyltransferase step
              - Nicotinate-nucleotide diphosphorylase (carboxylating) (molecular player: quinolinate phosphoribosyltransferase family; activity or role: nicotinate-nucleotide diphosphorylase (carboxylating) activity)
          - Direct nicotinate Preiss-Handler entry
            - Nicotinate phosphoribosyltransferase (molecular player: nicotinate phosphoribosyltransferase family; activity or role: nicotinate phosphoribosyltransferase activity)
          - Nicotinamide deamidation followed by Preiss-Handler entry
            - 1. nicotinamide deamidation
            - Nicotinamidase step
              - Nicotinamidase (molecular player: nicotinamidase family; activity or role: nicotinamidase activity)
            - 2. nicotinate phosphoribosylation
            - PncB step after PncA
              - Nicotinate phosphoribosyltransferase (molecular player: nicotinate phosphoribosyltransferase family; activity or role: nicotinate phosphoribosyltransferase activity)
          - NMN deamidation to NaMN
            - Nicotinamide-nucleotide amidase PncC (molecular player: PncC/CinA C-terminal NMN deamidase family; activity or role: nicotinamide-nucleotide amidase activity)
      - 2. complete NaMN through deamido-NAD to NAD+
      - Shared NaMN completion through deamido-NAD
        - 1. NaMN adenylylation to deamido-NAD
        - NaMN adenylylation alternatives
          - Alternative versions by enzyme family: NaMN adenylyltransferase family
            - Bacterial NadD-family NaMN adenylyltransferase
              - Nicotinate-nucleotide adenylyltransferase (molecular player: bacterial NadD family; activity or role: nicotinate-nucleotide adenylyltransferase activity)
            - Bifunctional NMNAT-family NaMN adenylylation
              - NMNAT nicotinate-nucleotide adenylyltransferase activity (molecular player: eukaryotic NMN adenylyltransferase family; activity or role: nicotinate-nucleotide adenylyltransferase activity)
        - 2. deamido-NAD amidation to NAD+
        - NAD synthetase nitrogen-donor alternatives
          - Alternative versions by nitrogen donor and enzyme architecture: NAD synthetase nitrogen donor
            - Ammonia-dependent NAD synthetase
              - Ammonia-dependent NAD+ synthase (molecular player: ammonia-dependent NAD synthetase subfamily; activity or role: NAD+ synthase activity)
            - Glutamine-dependent NAD synthetase
              - Glutamine-dependent NAD+ synthase (molecular player: human glutamine-dependent NAD synthetase NADSYN1; activity or role: NAD+ synthase (glutamine-hydrolyzing) activity)
    - NAMPT-produced NMN with direct NAD+ completion
      - 1. produce NMN from nicotinamide
      - Nicotinamide phosphoribosylation to NMN
        - Nicotinamide phosphoribosyltransferase (molecular player: nicotinamide phosphoribosyltransferase family; activity or role: nicotinamide phosphoribosyltransferase activity)
      - 2. adenylylate NMN directly to NAD+
      - Direct amidated NMN completion
        - Nicotinamide-nucleotide adenylyltransferase (molecular player: eukaryotic NMN adenylyltransferase family; activity or role: nicotinamide-nucleotide adenylyltransferase activity)

### Known Relationships Among Steps

- De novo NaMN synthesis from L-aspartate feeds into Shared NaMN completion through deamido-NAD: The L-aspartate de novo route supplies NaMN to shared completion.
- Direct nicotinate Preiss-Handler entry feeds into Shared NaMN completion through deamido-NAD: Direct nicotinate phosphoribosylation supplies NaMN to shared completion.
- Nicotinamide deamidation followed by Preiss-Handler entry feeds into Shared NaMN completion through deamido-NAD: PncA followed by PncB supplies NaMN to shared completion.
- NMN deamidation to NaMN feeds into Shared NaMN completion through deamido-NAD: PncC deamidation supplies NaMN to shared completion.
- L-aspartate oxidase step feeds into Quinolinate synthase step: NadB supplies iminoaspartate to NadA.
- Quinolinate synthase step feeds into Quinolinate phosphoribosyltransferase step: NadA supplies quinolinate to NadC.
- Nicotinamidase step feeds into PncB step after PncA: PncA supplies nicotinate to PncB.
- NaMN adenylylation alternatives feeds into NAD synthetase nitrogen-donor alternatives: NaMN adenylylation supplies deamido-NAD to NAD synthetase.
- Nicotinamide phosphoribosylation to NMN feeds into Direct amidated NMN completion: NAMPT supplies NMN specifically to direct NMN adenylylation.

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

# Module/Pathway/Taxon Review: L-aspartate de novo and selected salvage routes to NAD+ in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00760 — Nicotinate and nicotinamide metabolism
**Module area:** cofactors_vitamins_redox
**Scope:** L-aspartate de novo NAD+ synthesis plus selected nicotinate / nicotinamide / NMN salvage routes to NAD+ (kynurenine/tryptophan de novo route explicitly out of scope; owned by MODULE:kynurenine_nad_de_novo)

---

## 1. Executive summary

In *Pseudomonas putida* KT2440 the aspartate-de-novo-and-salvage NAD+ module is **satisfiable end-to-end**. The organism encodes a complete, single-copy L-aspartate de novo route to nicotinate mononucleotide (NaMN) — **NadB** (L-aspartate oxidase, PP_1426), **NadA** (quinolinate synthase, PP_1231), and **NadC** (quinolinate phosphoribosyltransferase, PP_0787) — which converges with two functional salvage entry points, the nicotinate Preiss–Handler enzyme **PncB** (PP_4868) and the NMN-deamidase **PncC** (PP_1628), onto a shared NaMN → deamido-NAD → NAD+ completion carried by **NadD** (NaMN adenylyltransferase, PP_4810, bacterial NadD family) and **NadE** (NH₃-dependent NAD synthetase, PP_4869). Every core biosynthetic step of the module is covered by a clearly annotated candidate gene whose EC number matches the expected activity, and each core step is single-copy — there is little paralog ambiguity in the biosynthetic backbone.

The one genuine **gap** is the nicotinamide-deamidation salvage branch. KT2440 has **no canonical nicotinamidase (PncA, EC 3.5.1.19)**: a proteome-wide EC and name search of UP000000556 returns no PncA, and the only member of the parent isochorismatase superfamily is a single uncharacterized protein (Q88JT5). Consequently, the deamidating route from nicotinamide (Nm → nicotinate → NaMN via PncA+PncB) cannot currently be marked covered. Two module *variants* are **not expected** in this organism at all: the NAMPT-to-direct-NMN route (no EC 2.4.2.12, no NadM/NMNAT EC 2.7.7.1) and the glutamine-dependent NAD-synthetase architecture (the resident NadE is ammonia-dependent, EC 6.3.1.5).

Finally, the KEGG bucket ppu00760 is a **poor proxy for the module boundary**: of the 30 candidate genes, only ~8 lie inside the aspartate-de-novo/salvage-to-NAD+ scope. The remaining ~22 are out-of-scope over-inclusions — the entire aerobic nicotinate *degradation* cluster (nicAB/nicCDEFX/maiA), pyridine-nucleotide transhydrogenases (pntAA/pntB/pntAB/sthA), NAD kinase (nadK), NAD-consuming enzymes (cobB sirtuin, nudC NAD-cap hydrolase), promiscuous 5′-nucleotidases (ushA/surE/PP_2531), and succinate/glutarate-semialdehyde dehydrogenases that actually belong to ppu00350. This is a **bucket-level over-annotation problem**, not a module defect.

---

## 2. Target-organism pathway definition

### What is included

The module covers the routes that **produce NAD+** from (a) the L-aspartate de novo pathway and (b) selected pyridine salvage precursors (nicotinate, nicotinamide, NMN), through the universal downstream completion NaMN → deamido-NAD (NaAD) → NAD+. Concretely, for KT2440 the in-scope chemistry is:

- **De novo:** L-aspartate → iminoaspartate (NadB) → quinolinate (NadA) → NaMN (NadC, with decarboxylation and PRPP condensation).
- **Preiss–Handler salvage:** nicotinate + PRPP → NaMN (PncB).
- **NMN-deamidation salvage:** NMN → NaMN (PncC).
- **Shared completion:** NaMN + ATP → deamido-NAD (NadD); deamido-NAD + NH₃ → NAD+ (NadE).

### What must be kept separate

- **Tryptophan/kynurenine de novo route** — owned by MODULE:kynurenine_nad_de_novo; not duplicated here.
- **Nicotinate catabolism / degradation** — the aerobic NA degradation cluster (nic genes) channels nicotinate to central metabolism and is a **separate catabolic module**, even though several nic genes carry the ppu00760 KEGG tag ([PMID: 18678916](https://pubmed.ncbi.nlm.nih.gov/18678916/), [PMID: 21450002](https://pubmed.ncbi.nlm.nih.gov/21450002/)).
- **Pyridine-nucleotide transhydrogenases** (pntAB, sthA), **NAD kinase / NADP formation** (nadK), **NAD-consuming reactions** (cobB deacylase, nudC NAD-cap hydrolase), and **unrelated aldehyde metabolism** (semialdehyde dehydrogenases). These are explicitly outside the module boundary in the working scope.

### Alternate names / database definitions

The KEGG map ppu00760 "Nicotinate and nicotinamide metabolism" is a broad overview map that mixes biosynthesis, salvage, and degradation. The MetaCyc/BioCyc equivalents split these into **NAD biosynthesis I (from aspartate)**, **NAD salvage pathway**, and **nicotinate degradation**. The module reviewed here corresponds to the biosynthesis + salvage-to-NAD+ subset only. Curators should not treat "gene tagged ppu00760" as equivalent to "gene in this module."

---

## 3. Expected step model

The table below is the module's expected step model instantiated for KT2440.

| Step | Expected activity (EC) | Enzyme family | KT2440 gene | Call |
|------|------------------------|---------------|-------------|------|
| De novo 1: L-aspartate oxidation | L-aspartate oxidase (1.4.3.16) | NadB | PP_1426 / Q88MZ2 | **covered** |
| De novo 2: quinolinate formation | quinolinate synthase (2.5.1.72) | NadA | PP_1231 / Q88NH8 | **covered** |
| De novo 3: quinolinate → NaMN | NaMN pyrophosphorylase, carboxylating (2.4.2.19) | NadC | PP_0787 / Q88PR1 | **covered** |
| Salvage: nicotinate → NaMN | nicotinate PRTase (6.3.4.21 / 2.4.2.11) | PncB | PP_4868 / Q88DF7 | **covered** |
| Salvage: Nm → nicotinate | nicotinamidase (3.5.1.19) | PncA | — | **gap / candidate_uncertain** |
| Salvage: NMN → NaMN | NMN amidohydrolase (3.5.1.42) | PncC | PP_1628 / Q88ME5 | **covered** |
| Completion 1: NaMN → deamido-NAD | NaMN adenylyltransferase (2.7.7.18) | NadD (bacterial) | PP_4810 / Q88DL5 | **covered** |
| Completion 2: deamido-NAD → NAD+ | NAD synthetase, NH₃-dependent (6.3.1.5) | NadE | PP_4869 / Q88DF6 | **covered** |
| Variant: NAMPT direct route | Nm phosphoribosyltransferase (2.4.2.12) | NAMPT/NadV | — | **not_expected** |
| Variant: direct NMN adenylylation | NMN adenylyltransferase (2.7.7.1) | NadM/NMNAT | — | **not_expected** |
| Variant: Gln-dependent completion | NAD synthetase, Gln-hydrolyzing (6.3.5.1) | NADSYN1-type | — | **not_expected** (resident NadE is NH₃-dependent) |

```
                    L-aspartate
                        │  NadB (PP_1426, 1.4.3.16)
                        ▼
                  iminoaspartate
                        │  NadA (PP_1231, 2.5.1.72)
                        ▼
                   quinolinate
                        │  NadC (PP_0787, 2.4.2.19)
   nicotinate ──PncB──► NaMN ◄──PncC── NMN
   (PP_4868,6.3.4.21)    │      (PP_1628,3.5.1.42)
                         │  NadD (PP_4810, 2.7.7.18)
                         ▼
                   deamido-NAD (NaAD)
                         │  NadE (PP_4869, 6.3.1.5, NH3-dependent)
                         ▼
                        NAD+

   nicotinamide ──X──►  (no PncA; EC 3.5.1.19 absent)  ── GAP
   nicotinamide ──X──►  NMN (no NAMPT; EC 2.4.2.12 absent) ── NOT EXPECTED
```

---

## 4. Candidate genes and evidence

### 4.1 High-confidence, in-scope core genes (covered)

**NadB — PP_1426 / Q88MZ2 — L-aspartate oxidase (EC 1.4.3.16).** First committed step of de novo synthesis. UniProt EC annotation matches the expected activity exactly; single copy. Evidence type: sequence/EC annotation in the target proteome, strong homology to characterized enterobacterial NadB. Curation call: **covered**, no caveat.

**NadA — PP_1231 / Q88NH8 — quinolinate synthase (EC 2.5.1.72).** Condenses iminoaspartate + DHAP to quinolinate; carries a [4Fe-4S] cluster in characterized homologs. EC match exact, single copy. Curation call: **covered**.

**NadC — PP_0787 / Q88PR1 — quinolinate phosphoribosyltransferase / NaMN pyrophosphorylase, carboxylating (EC 2.4.2.19).** Converts quinolinate + PRPP to NaMN. This is the convergence node where de novo synthesis meets the shared completion. Note the cross-species precedent that NadC can also function in **quinolinate salvage** even where the rest of de novo synthesis is absent ([PMID: 23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/)); in KT2440 the full de novo route is present, so NadC is the terminal de novo step. Curation call: **covered**.

**PncB — PP_4868 / Q88DF7 — nicotinate phosphoribosyltransferase (EC 6.3.4.21).** Preiss–Handler entry: nicotinate + PRPP → NaMN (ATP-dependent NAPRTase). Physically adjacent to nadE (PP_4869), a common bacterial salvage/completion gene arrangement. Curation call: **covered** for the nicotinate salvage branch.

**PncC — PP_1628 / Q88ME5 — NMN amidohydrolase / nicotinamide-nucleotide amidase (EC 3.5.1.42).** Deamidates NMN to NaMN, feeding NMN back into the deamido-NAD completion. Member of the PncC/CinA C-terminal amidase family. Curation call: **covered** for the NMN-deamidation branch. Caveat: PncC provides only an *indirect* nicotinamide-salvage capacity (Nm would still need to first become NMN), so it does not substitute for a missing PncA in the classical Nm → nicotinate deamidation step.

**NadD — PP_4810 / Q88DL5 — NaMN adenylyltransferase (EC 2.7.7.18), bacterial NadD family.** Adenylylates NaMN to deamido-NAD; the module's "Bacterial NadD-family" variant, not the eukaryotic bifunctional NMNAT variant. This and NadE are the two indispensable downstream enzymes of NAD synthesis and validated antibacterial targets in other bacteria ([PMID: 23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/), [PMID: 20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/)). Curation call: **covered**.

**NadE — PP_4869 / Q88DF6 — NH₃-dependent NAD synthetase (EC 6.3.1.5).** Amidates deamido-NAD to NAD+. The UniProt annotation explicitly specifies the **ammonia-dependent** subfamily, which resolves the module's nitrogen-donor variant question: KT2440 uses the ammonia-dependent architecture, **not** the glutamine-hydrolyzing NADSYN1-type ([PMID: 29581233](https://pubmed.ncbi.nlm.nih.gov/29581233/)). Curation call: **covered**; glutamine-dependent variant **not_expected**.

### 4.2 In-bucket but out-of-scope genes (should NOT count toward module satisfiability)

| Gene(s) | Annotation / EC | Why out of scope |
|---------|-----------------|------------------|
| pntB, pntAA, pntAB (PP_0155/0156/5747), sthA (PP_2151) | transhydrogenases (7.1.1.1; 1.6.1.1) | interconvert NAD(H)/NADP(H); not NAD+ *biosynthesis* |
| nadK (PP_2012) | NAD kinase (2.7.1.23) | makes NADP from NAD+; downstream of module boundary |
| cobB (PP_5402) | NAD-dependent deacylase / sirtuin (2.3.1.286) | NAD-**consuming**, not biosynthetic |
| nudC (PP_4029) | NAD-cap RNA hydrolase / NADH pyrophosphatase (3.6.1.22) | NAD turnover/decapping |
| mazG (PP_1657) | NTP pyrophosphohydrolase (3.6.1.8) | primary bucket is ppu00770; house-cleaning |
| ushA, surE, PP_2531 | 5′-nucleotidases (3.1.3.5) | promiscuous phosphatases; not committed NAD steps |
| nicAB, nicC, nicD, nicF, nicX, maiA (PP_3941–3948) | nicotinate degradation cluster | catabolic; separate module ([PMID: 18678916](https://pubmed.ncbi.nlm.nih.gov/18678916/)) |
| davD, sad-I, sad-II, gabD-II | semialdehyde dehydrogenases (1.2.1.-/24/79) | belong to ppu00350; unrelated aldehyde metabolism |
| PP_3103 | uncharacterized protein | no assigned activity; unclear relevance |

---

## 5. Gaps, ambiguities, and likely over-annotations

### 5.1 The nicotinamide-deamidation gap (PncA)

A proteome-wide SPARQL search of UP000000556 / taxon 160488 returned **no protein carrying EC 3.5.1.19** (nicotinamidase/PncA) and no protein named "nicotinamidase" or "PncA." The classical deamidating nicotinamide-salvage branch (Nm → nicotinate → NaMN, via PncA then PncB) is therefore **not encoded by a canonical gene**. In comparative studies, PncA is the enzyme that specifically enables **deamidating** utilization of nicotinamide, distinct from the nondeamidating NAMPT/NadV route ([PMID: 20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/)), and its essentiality for Nm utilization has been shown directly in other bacteria ([PMID: 23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/)). Its absence in KT2440 removes the deamidating Nm route while leaving the nicotinate (PncB) branch intact.

The **only cryptic candidate** is Q88JT5, a single "isochorismatase-like domain-containing protein" — the isochorismatase superfamily is the fold that houses PncA — but it is uncharacterized and its EC is unassigned. This is a weak, fold-only lead. Curation call for the Nm-deamidation step: **gap / candidate_uncertain**, with Q88JT5 as the sole promotion candidate.

### 5.2 Precursor uptake ambiguity

No protein is annotated as a **nicotinate/niacin transporter (NiaP)** by name in the proteome. The only NAD-precursor transporter present is **PnuC (Q88IY9)**, a nicotinamide-riboside transporter, together with an **NadR/Ttd14-like AAA-domain protein (Q88IZ0)** — but the latter is *not* a classical bifunctional NadR NMNAT. Thus even the salvage precursor-uptake picture is incomplete/ambiguous, which is relevant when assessing whether salvage branches are physiologically operative versus merely genetically latent.

### 5.3 Variants not expected in KT2440

- **NAMPT/NadV direct route** (Nm → NMN, EC 2.4.2.12): **absent** — no EC 2.4.2.12 in the proteome. → **not_expected_in_target_taxon**.
- **NadM/NMNAT direct NMN adenylylation** (NMN → NAD+, EC 2.7.7.1): **absent** — this is the alternative "amidate-then-adenylylate" route characterized in *Francisella tularensis* ([PMID: 19204287](https://pubmed.ncbi.nlm.nih.gov/19204287/)), and KT2440 lacks it. → **not_expected_in_target_taxon**.
- **Glutamine-dependent NAD synthetase**: resident NadE is NH₃-dependent → glutamine-dependent variant **not_expected**.

### 5.4 Bucket-level over-annotation

The dominant over-annotation issue is at the **KEGG bucket level**: ppu00760 sweeps in degradation, transhydrogenation, NADP formation, NAD consumption, and unrelated aldehyde metabolism. ~22 of 30 candidates are out of scope. This is a systematic mismatch between a broad KEGG overview map and a mechanistically-scoped biosynthesis+salvage module — a **module_needs_revision flag against the bucket→module mapping**, not against the module content itself.

---

## 6. Module and GO-curation recommendations

**Per-step module status calls:**

| Module step | Status |
|-------------|--------|
| De novo: L-aspartate oxidase (NadB) | **covered** |
| De novo: quinolinate synthase (NadA) | **covered** |
| De novo: quinolinate PRTase (NadC) | **covered** |
| Preiss–Handler: PncB | **covered** |
| NMN deamidation: PncC | **covered** |
| NaMN adenylylation: NadD (bacterial family) | **covered** |
| Deamido-NAD amidation: NadE (NH₃-dependent) | **covered** |
| Nm deamidation: PncA | **gap / candidate_uncertain** |
| NAMPT direct NMN production | **not_expected_in_target_taxon** |
| Direct NMN adenylylation (NadM/NMNAT) | **not_expected_in_target_taxon** |
| Gln-dependent NAD synthetase variant | **not_expected_in_target_taxon** |

**Overall module verdict:** **SATISFIABLE.** A complete route from L-aspartate to NAD+ exists (de novo → NadD → NadE), and two independent salvage entries (PncB, PncC) also converge on the same completion. Module satisfiability does not depend on the missing PncA branch.

**Boundary corrections:** The generic module boundaries are **correct for this organism**; it is the KEGG **ppu00760 → module bucket mapping** that is wrong. Recommend that curation:
1. Restrict the module's KT2440 gene set to the ~8 in-scope genes (nadB, nadA, nadC, nadD, nadE, pncB, pncC; plus transporter context).
2. Reassign nic-cluster genes to a nicotinate-degradation module, semialdehyde dehydrogenases to ppu00350, and transhydrogenase/NAD-kinase/NAD-consuming genes to their own redox/turnover modules.

**GO/annotation actions:** No new GO term appears necessary — all covered activities map to existing EC/GO terms. Flag Q88JT5 for possible future annotation if experimentally shown to be a nicotinamidase. No new module document is needed; the existing module is adequate once the bucket over-inclusion is pruned.

---

## 7. Genes to promote to full `fetch-gene` review

1. **Q88JT5 (isochorismatase-like domain protein)** — highest priority. Sole fold-level candidate for the missing PncA/nicotinamidase step. Full review should assess active-site residues (the Cys-Asp-Lys catalytic triad of nicotinamidases), operon context, and any phenotypic/expression data. Resolving this decides whether the Nm-deamidation step is a true gap or a cryptic assignment.
2. **Q88IZ0 (NadR/Ttd14-like AAA-domain protein)** — clarify whether it retains any NMN adenylyltransferase / salvage-regulatory function, given it is *not* a classical bifunctional NadR.
3. **PncC — PP_1628** — confirm that the annotation reflects genuine NMN amidohydrolase activity versus the regulatory CinA-associated role, since PncC/CinA-family proteins are bifunctional in some taxa.
4. **NadE — PP_4869** — verify the ammonia-dependent subfamily assignment (vs. any latent glutaminase capacity), as this fixes the nitrogen-donor variant call.

---

## 8. Limitations and knowledge gaps

- **Absence calls rest on negative searches.** No-hit results for PncA (EC 3.5.1.19), NAMPT (EC 2.4.2.12), and NadM (EC 2.7.7.1) are strong but not absolute: a diverged or mis-annotated ORF could evade EC-based matching. This is exactly why Q88JT5 is flagged for full review rather than the gap being declared final.
- **No direct KT2440 enzymology was reviewed for the biosynthetic backbone.** The covered calls are based on target-strain proteome annotation (UniProt UP000000556, EC-matched, single-copy) and strong homology, not on strain-specific in vitro assays. This is standard and adequate for curation but is homology/annotation evidence, not direct experiment.
- **Salvage physiology is uncertain.** The incomplete transporter annotation (only PnuC named; no NiaP nicotinate permease) means we cannot confirm from genetics alone whether the PncB/PncC salvage branches are physiologically active under given conditions or merely latent.
- **Species transfer.** Mechanistic and target-relevance context is transferred from *Acinetobacter*, group A streptococci, *Francisella*, and *Bordetella*. Transfer is **strong** for the conserved downstream completion enzymes (NadD/NadE) and **moderate** for salvage-branch physiology.

---

## 9. Proposed follow-up experiments / curator actions

1. **Characterize Q88JT5** — heterologous expression + nicotinamidase assay (Nm → nicotinate + NH₃) to accept or reject it as the missing PncA. Highest-value single experiment.
2. **Growth-phenotype panel** — test KT2440 growth on nicotinamide vs. nicotinate vs. quinolinate as sole pyridine source (and in de novo-blocked backgrounds) to confirm which salvage entries are functional in vivo.
3. **Prune the ppu00760 bucket→module mapping** — reassign the ~22 out-of-scope genes to degradation/redox/turnover modules; retain only nadB, nadA, nadC, nadD, nadE, pncB, pncC (+ transporter context) for this module.
4. **Confirm NadE nitrogen donor** — verify ammonia- vs glutamine-dependence to finalize the nitrogen-donor variant call.
5. **Search for a NiaP-type nicotinate transporter** by profile/HMM to close the precursor-uptake gap.

---

## 10. Key references

- **Nicotinate degradation cluster in KT2440** — *Deciphering the genetic determinants for aerobic nicotinic acid degradation: the nic cluster from Pseudomonas putida KT2440.* [PMID: 18678916](https://pubmed.ncbi.nlm.nih.gov/18678916/). Establishes the nic genes as **catabolic**, supporting their exclusion from the biosynthesis module.
- **Regulation of the nic pathway** — *A finely tuned regulatory circuit of the nicotinic acid degradation pathway in Pseudomonas putida.* [PMID: 21450002](https://pubmed.ncbi.nlm.nih.gov/21450002/). Confirms nicAB / nicCDEFTP / nicXR operon structure and degradation role; notes the link to preserving vitamin B3 for cofactor synthesis.
- **PncA role in deamidating Nm salvage** — *Genomics-driven reconstruction of acinetobacter NAD metabolism.* [PMID: 20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/). Distinguishes the deamidating (PncA) and nondeamidating (NadV/NAMPT) nicotinamide routes — basis for calling the KT2440 PncA branch a gap.
- **PncA essentiality; NadC quinolinate salvage; NadD/NadE as targets** — *Quinolinate salvage and insights for targeting NAD biosynthesis in group A streptococci.* [PMID: 23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/). Supports the interpretation of NadC and identifies NadD/NadE as the indispensable downstream completion enzymes.
- **Alternative NaMN→NMN→NAD route** — *Nicotinamide mononucleotide synthetase is the key enzyme for an alternative route of NAD biosynthesis in Francisella tularensis.* [PMID: 19204287](https://pubmed.ncbi.nlm.nih.gov/19204287/). Defines the NadM/NMNAT variant that KT2440 lacks (not_expected).
- **NAD synthetase nitrogen-donor architectures** — *Kinetics and structural features of dimeric glutamine-dependent bacterial NAD synthetase.* [PMID: 29581233](https://pubmed.ncbi.nlm.nih.gov/29581233/). Context for the ammonia- vs glutamine-dependent NadE variant distinction.
- **Cross-taxon nic locus conservation** — *The Bordetella bronchiseptica nic locus encodes a nicotinic acid degradation pathway... highly similar to that characterized in Pseudomonas putida KT2440.* [PMID: 29485696](https://pubmed.ncbi.nlm.nih.gov/29485696/). Corroborates that the KT2440 nic locus is a degradation system that nonetheless influences NAD precursor pools.

---

### Evidence provenance note

Core gene calls (NadB, NadA, NadC, NadD, NadE, PncB, PncC) rest on **direct proteome evidence for the target strain** (UniProt UP000000556 / taxon 160488, EC-number matched, single-copy). Absence calls (PncA, NAMPT, NadM) rest on **negative proteome-wide EC/name searches** — strong but not absolute. Mechanistic roles and target relevance are transferred from related bacteria; this transfer is **strong for conserved downstream completion enzymes** but only **moderate for salvage-branch physiology**, since precursor-transport annotation in KT2440 is incomplete.


## Artifacts

- [OpenScientist final report](PSEPK__nad_biosynthesis_salvage__ppu00760-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__nad_biosynthesis_salvage__ppu00760-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:18678916
2. PMID:21450002
3. PMID:23204464
4. PMID:20926389
5. PMID:29581233
6. PMID:19204287
7. PMID:29485696