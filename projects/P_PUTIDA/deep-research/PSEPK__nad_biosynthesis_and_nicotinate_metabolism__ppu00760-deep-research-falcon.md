---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T04:05:10.698846'
end_time: '2026-07-07T04:26:55.382849'
duration_seconds: 1304.68
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: NAD biosynthesis and nicotinate metabolism
  module_summary: A bacterial NAD metabolism module covering de novo NAD+ biosynthesis
    from L-aspartate through quinolinate, nicotinate salvage to NAD+, NADP+ formation,
    NAD(H)/NADP(H) redox interconversion, and aerobic nicotinate catabolism. In Pseudomonas
    putida KT2440, KEGG ppu00760 also includes nucleotide hydrolases, NAD-consuming
    enzymes, and central-metabolism spillover nodes; those are tracked as boundary
    context unless they directly form, interconvert, salvage, or catabolize pyridine
    nucleotides/nicotinate.
  module_outline: "- NAD biosynthesis and nicotinate metabolism\n  - 1. de novo NAD+\
    \ biosynthesis from L-aspartate\n  - De novo NAD+ biosynthesis\n    - NadB L-aspartate\
    \ oxidase (molecular player: PSEPK nadB; activity or role: L-aspartate oxidase\
    \ activity)\n    - NadA quinolinate synthase (molecular player: PSEPK nadA; activity\
    \ or role: quinolinate synthetase A activity)\n    - NadC nicotinate-nucleotide\
    \ diphosphorylase (molecular player: PSEPK nadC; activity or role: nicotinate-nucleotide\
    \ diphosphorylase (carboxylating) activity)\n    - NadD nicotinate-nucleotide\
    \ adenylyltransferase (molecular player: PSEPK nadD; activity or role: nicotinate-nucleotide\
    \ adenylyltransferase activity)\n    - NadE NAD+ synthetase (molecular player:\
    \ PSEPK nadE; activity or role: NAD+ synthase (glutamine-hydrolyzing) activity)\n\
    \  - 2. nicotinate salvage to NAD+\n  - Nicotinate salvage to NAD+\n    - PncB\
    \ nicotinate phosphoribosyltransferase (molecular player: PSEPK pncB; activity\
    \ or role: nicotinate phosphoribosyltransferase activity)\n    - PncC nicotinamide-nucleotide\
    \ amidase (molecular player: PSEPK pncC; activity or role: nicotinamide-nucleotide\
    \ amidase activity)\n  - 3. NADP+ formation and NAD(H)/NADP(H) interconversion\n\
    \  - NADP+ formation and transhydrogenase context\n    - NadK NAD+ kinase (molecular\
    \ player: PSEPK nadK; activity or role: NAD+ kinase activity)\n    - SthA soluble\
    \ pyridine nucleotide transhydrogenase (molecular player: PSEPK sthA; activity\
    \ or role: NAD(P)+ transhydrogenase (Si-specific) activity)\n    - PntAA proton-translocating\
    \ NAD(P)+ transhydrogenase subunit alpha (molecular player: PSEPK pntAA; activity\
    \ or role: proton-translocating NAD(P)+ transhydrogenase activity)\n    - PntB\
    \ proton-translocating NAD(P)+ transhydrogenase subunit beta (molecular player:\
    \ PSEPK pntB; activity or role: proton-translocating NAD(P)+ transhydrogenase\
    \ activity)\n    - PntAB proton-translocating NAD(P)+ transhydrogenase alpha part\
    \ 2 (molecular player: PSEPK pntAB; activity or role: proton-translocating NAD(P)+\
    \ transhydrogenase activity)\n  - 4. aerobic nicotinate catabolism\n  - Aerobic\
    \ nicotinate catabolism\n    - NicA nicotinate dehydrogenase small subunit (molecular\
    \ player: PSEPK nicA; activity or role: oxidoreductase activity, acting on CH\
    \ or CH2 groups)\n    - NicB nicotinate dehydrogenase large subunit (molecular\
    \ player: PSEPK nicB; activity or role: oxidoreductase activity, acting on CH\
    \ or CH2 groups)\n    - NicC 6-hydroxynicotinate 3-monooxygenase (molecular player:\
    \ PSEPK nicC; activity or role: 6-hydroxynicotinate 3-monooxygenase activity)\n\
    \    - NicX 2,5-dihydroxypyridine 5,6-dioxygenase (molecular player: PSEPK nicX;\
    \ activity or role: 2,5-dihydroxypyridine 5,6-dioxygenase activity)\n    - NicD\
    \ N-formylmaleamate deformylase (molecular player: PSEPK nicD; activity or role:\
    \ hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)\n   \
    \ - NicF maleamate amidohydrolase (molecular player: PSEPK nicF; activity or role:\
    \ hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)\n   \
    \ - MaiA/NicE maleate isomerase (molecular player: PSEPK maiA; activity or role:\
    \ maleate isomerase activity)\n  - 5. nucleotide and central-metabolism boundary\
    \ context\n  - KEGG side-node context\n    - UshA 5'-nucleotidase/cyclic phosphodiesterase\
    \ (molecular player: PSEPK ushA; activity or role: 5'-nucleotidase activity)\n\
    \    - SurE 5'-nucleotidase (molecular player: PSEPK surE; activity or role: 5'-nucleotidase\
    \ activity)\n    - NudC NAD-capped RNA hydrolase (molecular player: PSEPK nudC;\
    \ activity or role: NADH pyrophosphatase activity)\n    - CobB NAD-dependent protein\
    \ deacylase (molecular player: PSEPK cobB__Q88BY5; activity or role: protein-malonyllysine\
    \ demalonylase activity)"
  module_connections: No explicit connections.
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
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__nad_biosynthesis_and_nicotinate_metabolism__ppu00760-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__nad_biosynthesis_and_nicotinate_metabolism__ppu00760-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

NAD biosynthesis and nicotinate metabolism in Pseudomonas putida KT2440

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

A bacterial NAD metabolism module covering de novo NAD+ biosynthesis from L-aspartate through quinolinate, nicotinate salvage to NAD+, NADP+ formation, NAD(H)/NADP(H) redox interconversion, and aerobic nicotinate catabolism. In Pseudomonas putida KT2440, KEGG ppu00760 also includes nucleotide hydrolases, NAD-consuming enzymes, and central-metabolism spillover nodes; those are tracked as boundary context unless they directly form, interconvert, salvage, or catabolize pyridine nucleotides/nicotinate.

### Provisional Biological Outline

- NAD biosynthesis and nicotinate metabolism
  - 1. de novo NAD+ biosynthesis from L-aspartate
  - De novo NAD+ biosynthesis
    - NadB L-aspartate oxidase (molecular player: PSEPK nadB; activity or role: L-aspartate oxidase activity)
    - NadA quinolinate synthase (molecular player: PSEPK nadA; activity or role: quinolinate synthetase A activity)
    - NadC nicotinate-nucleotide diphosphorylase (molecular player: PSEPK nadC; activity or role: nicotinate-nucleotide diphosphorylase (carboxylating) activity)
    - NadD nicotinate-nucleotide adenylyltransferase (molecular player: PSEPK nadD; activity or role: nicotinate-nucleotide adenylyltransferase activity)
    - NadE NAD+ synthetase (molecular player: PSEPK nadE; activity or role: NAD+ synthase (glutamine-hydrolyzing) activity)
  - 2. nicotinate salvage to NAD+
  - Nicotinate salvage to NAD+
    - PncB nicotinate phosphoribosyltransferase (molecular player: PSEPK pncB; activity or role: nicotinate phosphoribosyltransferase activity)
    - PncC nicotinamide-nucleotide amidase (molecular player: PSEPK pncC; activity or role: nicotinamide-nucleotide amidase activity)
  - 3. NADP+ formation and NAD(H)/NADP(H) interconversion
  - NADP+ formation and transhydrogenase context
    - NadK NAD+ kinase (molecular player: PSEPK nadK; activity or role: NAD+ kinase activity)
    - SthA soluble pyridine nucleotide transhydrogenase (molecular player: PSEPK sthA; activity or role: NAD(P)+ transhydrogenase (Si-specific) activity)
    - PntAA proton-translocating NAD(P)+ transhydrogenase subunit alpha (molecular player: PSEPK pntAA; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
    - PntB proton-translocating NAD(P)+ transhydrogenase subunit beta (molecular player: PSEPK pntB; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
    - PntAB proton-translocating NAD(P)+ transhydrogenase alpha part 2 (molecular player: PSEPK pntAB; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
  - 4. aerobic nicotinate catabolism
  - Aerobic nicotinate catabolism
    - NicA nicotinate dehydrogenase small subunit (molecular player: PSEPK nicA; activity or role: oxidoreductase activity, acting on CH or CH2 groups)
    - NicB nicotinate dehydrogenase large subunit (molecular player: PSEPK nicB; activity or role: oxidoreductase activity, acting on CH or CH2 groups)
    - NicC 6-hydroxynicotinate 3-monooxygenase (molecular player: PSEPK nicC; activity or role: 6-hydroxynicotinate 3-monooxygenase activity)
    - NicX 2,5-dihydroxypyridine 5,6-dioxygenase (molecular player: PSEPK nicX; activity or role: 2,5-dihydroxypyridine 5,6-dioxygenase activity)
    - NicD N-formylmaleamate deformylase (molecular player: PSEPK nicD; activity or role: hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)
    - NicF maleamate amidohydrolase (molecular player: PSEPK nicF; activity or role: hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)
    - MaiA/NicE maleate isomerase (molecular player: PSEPK maiA; activity or role: maleate isomerase activity)
  - 5. nucleotide and central-metabolism boundary context
  - KEGG side-node context
    - UshA 5'-nucleotidase/cyclic phosphodiesterase (molecular player: PSEPK ushA; activity or role: 5'-nucleotidase activity)
    - SurE 5'-nucleotidase (molecular player: PSEPK surE; activity or role: 5'-nucleotidase activity)
    - NudC NAD-capped RNA hydrolase (molecular player: PSEPK nudC; activity or role: NADH pyrophosphatase activity)
    - CobB NAD-dependent protein deacylase (molecular player: PSEPK cobB__Q88BY5; activity or role: protein-malonyllysine demalonylase activity)

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

NAD biosynthesis and nicotinate metabolism in Pseudomonas putida KT2440

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

A bacterial NAD metabolism module covering de novo NAD+ biosynthesis from L-aspartate through quinolinate, nicotinate salvage to NAD+, NADP+ formation, NAD(H)/NADP(H) redox interconversion, and aerobic nicotinate catabolism. In Pseudomonas putida KT2440, KEGG ppu00760 also includes nucleotide hydrolases, NAD-consuming enzymes, and central-metabolism spillover nodes; those are tracked as boundary context unless they directly form, interconvert, salvage, or catabolize pyridine nucleotides/nicotinate.

### Provisional Biological Outline

- NAD biosynthesis and nicotinate metabolism
  - 1. de novo NAD+ biosynthesis from L-aspartate
  - De novo NAD+ biosynthesis
    - NadB L-aspartate oxidase (molecular player: PSEPK nadB; activity or role: L-aspartate oxidase activity)
    - NadA quinolinate synthase (molecular player: PSEPK nadA; activity or role: quinolinate synthetase A activity)
    - NadC nicotinate-nucleotide diphosphorylase (molecular player: PSEPK nadC; activity or role: nicotinate-nucleotide diphosphorylase (carboxylating) activity)
    - NadD nicotinate-nucleotide adenylyltransferase (molecular player: PSEPK nadD; activity or role: nicotinate-nucleotide adenylyltransferase activity)
    - NadE NAD+ synthetase (molecular player: PSEPK nadE; activity or role: NAD+ synthase (glutamine-hydrolyzing) activity)
  - 2. nicotinate salvage to NAD+
  - Nicotinate salvage to NAD+
    - PncB nicotinate phosphoribosyltransferase (molecular player: PSEPK pncB; activity or role: nicotinate phosphoribosyltransferase activity)
    - PncC nicotinamide-nucleotide amidase (molecular player: PSEPK pncC; activity or role: nicotinamide-nucleotide amidase activity)
  - 3. NADP+ formation and NAD(H)/NADP(H) interconversion
  - NADP+ formation and transhydrogenase context
    - NadK NAD+ kinase (molecular player: PSEPK nadK; activity or role: NAD+ kinase activity)
    - SthA soluble pyridine nucleotide transhydrogenase (molecular player: PSEPK sthA; activity or role: NAD(P)+ transhydrogenase (Si-specific) activity)
    - PntAA proton-translocating NAD(P)+ transhydrogenase subunit alpha (molecular player: PSEPK pntAA; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
    - PntB proton-translocating NAD(P)+ transhydrogenase subunit beta (molecular player: PSEPK pntB; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
    - PntAB proton-translocating NAD(P)+ transhydrogenase alpha part 2 (molecular player: PSEPK pntAB; activity or role: proton-translocating NAD(P)+ transhydrogenase activity)
  - 4. aerobic nicotinate catabolism
  - Aerobic nicotinate catabolism
    - NicA nicotinate dehydrogenase small subunit (molecular player: PSEPK nicA; activity or role: oxidoreductase activity, acting on CH or CH2 groups)
    - NicB nicotinate dehydrogenase large subunit (molecular player: PSEPK nicB; activity or role: oxidoreductase activity, acting on CH or CH2 groups)
    - NicC 6-hydroxynicotinate 3-monooxygenase (molecular player: PSEPK nicC; activity or role: 6-hydroxynicotinate 3-monooxygenase activity)
    - NicX 2,5-dihydroxypyridine 5,6-dioxygenase (molecular player: PSEPK nicX; activity or role: 2,5-dihydroxypyridine 5,6-dioxygenase activity)
    - NicD N-formylmaleamate deformylase (molecular player: PSEPK nicD; activity or role: hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)
    - NicF maleamate amidohydrolase (molecular player: PSEPK nicF; activity or role: hydrolase activity, acting on carbon-nitrogen bonds, in linear amides)
    - MaiA/NicE maleate isomerase (molecular player: PSEPK maiA; activity or role: maleate isomerase activity)
  - 5. nucleotide and central-metabolism boundary context
  - KEGG side-node context
    - UshA 5'-nucleotidase/cyclic phosphodiesterase (molecular player: PSEPK ushA; activity or role: 5'-nucleotidase activity)
    - SurE 5'-nucleotidase (molecular player: PSEPK surE; activity or role: 5'-nucleotidase activity)
    - NudC NAD-capped RNA hydrolase (molecular player: PSEPK nudC; activity or role: NADH pyrophosphatase activity)
    - CobB NAD-dependent protein deacylase (molecular player: PSEPK cobB__Q88BY5; activity or role: protein-malonyllysine demalonylase activity)

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

# NAD Biosynthesis and Nicotinate Metabolism in *Pseudomonas putida* KT2440: A Species-Aware Pathway Review

## 1. Executive Summary

This review assesses the satisfiability of KEGG pathway ppu00760 (Nicotinate and nicotinamide metabolism) in *Pseudomonas putida* KT2440 (NCBI taxon 160488, proteome UP000000556). The module encompasses four functional blocks: (i) de novo NAD⁺ biosynthesis from L-aspartate via quinolinate (NadB→NadA→NadC→NadD→NadE), (ii) nicotinate salvage to NAD⁺ (PncB, PncC), (iii) NADP⁺ formation and NAD(H)/NADP(H) interconversion (NadK, SthA, PntAB), and (iv) aerobic nicotinate catabolism via the nic gene cluster (NicAB→NicC→NicX→NicD→NicF→MaiA). Additionally, the KEGG bucket includes 11 boundary/context genes with broad enzymatic activities (nucleotidases, semialdehyde dehydrogenases, NAD-consuming enzymes) that do not represent core pathway steps.

Of the 30 candidate genes, **19 are assessed as genuine pathway components** with covered status, **1 step (PncA, nicotinamidase) represents a potential gap** in the salvage pathway, and **10 genes are boundary context** that should not be used for module satisfiability. The strongest experimental evidence comes from the nic gene cluster (direct gene knockouts, enzymatic characterization, regulatory studies in KT2440) and the transhydrogenase system (biochemical and physiological characterization in KT2440). The de novo biosynthesis and salvage genes are supported primarily by genome annotation and metabolic model reconstruction rather than direct KT2440 enzymology.

## 2. Target-Organism Pathway Definition

### 2.1 Pathway boundaries

The pathway covers the complete lifecycle of pyridine nucleotides in *P. putida* KT2440: de novo synthesis of NAD⁺ from L-aspartate, salvage recycling from nicotinate/nicotinamide precursors, phosphorylation to NADP⁺, reversible interconversion of NAD(H) and NADP(H) pools, and aerobic catabolism of nicotinate as a carbon/nitrogen source. The pathway is named "Nicotinate and nicotinamide metabolism" in KEGG (ppu00760) and corresponds to MetaCyc pathways for NAD biosynthesis I (from aspartate) and the nicotinate degradation I pathway.

### 2.2 Neighboring pathways to keep separate

The following should be kept distinct: (i) purine/pyrimidine nucleotide metabolism (ppu00230/00240), which shares nucleotidase activities (UshA, SurE) but has separate biosynthetic logic; (ii) lysine degradation (ppu00310) and GABA metabolism (ppu00350), which share semialdehyde dehydrogenase enzymes (davD, sad-I/II, gabD-II) but operate on different substrates; (iii) the broader cofactor/vitamin pathways such as riboflavin and folate metabolism.

### 2.3 Significance in *P. putida* KT2440

*P. putida* KT2440 has a characteristically reductive metabolic regime that favors NADPH generation over ATP production, a trait central to its oxidative stress tolerance and value as an industrial biotechnology chassis (i.2021reconfigurationofmetabolic pages 1-2, nikel2020redoxstressreshapes pages 1-4). The EDEMP cycle (Entner-Doudoroff–Embden-Meyerhof-Parnas–pentose phosphate cycle) generates NADPH fluxes exceeding biosynthetic demands by approximately 50% under oxidative stress (i.2021reconfigurationofmetabolic pages 1-2, i.2021reconfigurationofmetabolic pages 7-8). This makes the NAD(P)H interconversion machinery and NAD⁺/NADP⁺ biosynthetic pathways particularly important in this organism.

## 3. Expected Step Model

The following comprehensive tables detail (i) all 30 candidate genes with their functional categorization and assessment, and (ii) the step-by-step module satisfiability analysis.

| Gene name | Locus tag | UniProt ID | Functional category | Evidence type | Module step status assessment | Key curation notes |
|---|---|---|---|---|---|---|
| pntB | PP_0155 | Q88RH4 | NADP+ formation & transhydrogenases | direct experimental in KT2440 | covered | Membrane transhydrogenase beta subunit; part of proton-translocating PntAB system for NADH/NADPH balancing; strong KT2440 evidence from transhydrogenase studies (nikel2016pyridinenucleotidetranshydrogenases pages 1-2, nikel2016pyridinenucleotidetranshydrogenases pages 6-7) |
| pntAA | PP_0156 | A0A140FVX4 | NADP+ formation & transhydrogenases | direct experimental in KT2440 | covered | Alpha part 1 of membrane PntAB complex; gene architecture in KT2440 split relative to some bacteria; experimentally implicated in redox homeostasis (partipilo2025integratedcontrolof pages 1-6, nikel2016pyridinenucleotidetranshydrogenases pages 6-7) |
| davD | PP_0213 | Q88RC0 | boundary context | homology | boundary_only | Glutarate-semialdehyde dehydrogenase from lysine/glutarate catabolism, not a core nicotinate/NAD step; inclusion in module is spillover from aldehyde/NAD usage (candidate list context) |
| nadC | PP_0787 | Q88PR1 | de novo biosynthesis | genome annotation | covered | Quinolinate phosphoribosyltransferase/NaMN-forming step of de novo NAD biosynthesis; expected canonical bacterial step and retained in KT2440 reconstructions (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2, belda2016therevisitedgenome pages 10-12) |
| nadA | PP_1231 | Q88NH8 | de novo biosynthesis | genome annotation | covered | Quinolinate synthase; canonical de novo NAD step from iminoaspartate; supported by genome annotation and metabolic models (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2, kampers2019insilicoguidedengineering pages 5-7) |
| ushA | PP_1414 | Q88N04 | boundary context | homology | boundary_only | Broad periplasmic 5'-nucleotidase/cyclic phosphodiesterase; may act on nucleotide derivatives but not a dedicated NAD/nicotinate pathway enzyme (candidate list context) |
| nadB | PP_1426 | Q88MZ2 | de novo biosynthesis | genome annotation | covered | L-aspartate oxidase initiating de novo NAD biosynthesis; important aerobic constraint in KT2440 metabolic models, possibly oxygen-dependent in vivo (kampers2019insilicoguidedengineering pages 5-7, kampers2019insilicoguidedengineering pages 3-5) |
| surE | PP_1620 | Q88MF1 | boundary context | homology | boundary_only | General 5'-nucleotidase/nucleotide stress enzyme; not specific to nicotinate or pyridine nucleotide metabolism (candidate list context) |
| pncC | PP_1628 | Q88ME5 | salvage | genome annotation | covered | NMN amidohydrolase linking NMN to NaMN in bacterial pyridine nucleotide salvage; annotated in KT2440 but little direct species-specific experimental validation found |
| mazG | PP_1657 | Q88MB7 | boundary context | homology | boundary_only | NTP pyrophosphohydrolase involved in nucleotide quality control/stress, not a dedicated nicotinate/NAD pathway enzyme (candidate list context) |
| nadK | PP_2012 | Q88LC3 | NADP+ formation & transhydrogenases | genome annotation | covered | ATP-dependent NAD kinase producing NADP+ from NAD+; core cofactor-pool step expected in KT2440 though direct gene-specific experimental evidence is limited |
| sthA | PP_2151 | Q88KY8 | NADP+ formation & transhydrogenases | direct experimental in KT2440 | covered | Soluble transhydrogenase; >70% of total transhydrogenase activity in cell extracts; key redox-balancing enzyme, especially important under some substrates (nikel2016pyridinenucleotidetranshydrogenases pages 4-6, nikel2016pyridinenucleotidetranshydrogenases pages 7-9) |
| sad-I | PP_2488 | Q88K05 | boundary context | homology | boundary_only | NAD+-dependent succinate semialdehyde dehydrogenase; belongs to GABA/4-hydroxybutyrate or related aldehyde metabolism, not nicotinate/NAD core pathway |
| PP_2531 | PP_2531 | Q88JW6 | boundary context | homology | boundary_only | Unspecified 5'-nucleotidase; possible broad nucleotide phosphatase only; no specific evidence for pyridine nucleotide salvage role |
| PP_3103 | PP_3103 | Q88I96 | boundary context | genome annotation | candidate_uncertain | Uncharacterized protein in KEGG bucket; no convincing functional evidence tying it directly to NAD/nicotinate metabolism; merits separate review if conserved near pathway genes |
| sad-II | PP_3151 | Q88I50 | boundary context | homology | boundary_only | Second NAD+-dependent succinate semialdehyde dehydrogenase paralog; likely central/aldehyde metabolism rather than pyridine nucleotide pathway |
| nicF | PP_3941 | Q88FY5 | nicotinate catabolism | direct experimental in KT2440 | covered | Maleamate amidohydrolase in validated nic cluster; downstream step in aerobic nicotinate degradation to maleate/fumarate branch (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 5-6) |
| maiA | PP_3942 | Q88FY4 | nicotinate catabolism | direct experimental in KT2440 | covered | Maleate cis-trans isomerase, equivalent to NicE function in pathway descriptions; final nicotinate-catabolic step to fumarate; name mismatch is a curation caveat (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 5-6) |
| nicD | PP_3943 | Q88FY3 | nicotinate catabolism | direct experimental in KT2440 | covered | N-formylmaleamate deformylase in validated nic cluster; direct role shown through cluster characterization (jimenez2008decipheringthegenetic pages 1-2, jimenez2008decipheringthegenetic pages 5-6) |
| nicC | PP_3944 | Q88FY2 | nicotinate catabolism | direct experimental in KT2440 | covered | 6-hydroxynicotinate 3-monooxygenase; essential for growth on nicotinate; also under FinR/NicR regulation (jimenez2008decipheringthegenetic pages 1-2, xiao2018finrregulatesexpression pages 6-8) |
| nicX | PP_3945 | Q88FY1 | nicotinate catabolism | direct experimental in KT2440 | covered | 2,5-dihydroxypyridine 5,6-dioxygenase; hallmark ring-cleavage step of maleamate pathway; experimentally validated and transcriptionally regulated (jimenez2008decipheringthegenetic pages 2-3, xiao2018finrregulatesexpression pages 6-8) |
| nicA | PP_3947 | Q88FX9 | nicotinate catabolism | direct experimental in KT2440 | covered | Small subunit of two-component nicotinate hydroxylase (NicAB); required for first catabolic step NA -> 6HNA (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 1-2) |
| nicB | PP_3948 | Q88FX8 | nicotinate catabolism | direct experimental in KT2440 | covered | Large subunit of NicAB nicotinate hydroxylase; part of validated nic locus; annotation as dehydrogenase-family molybdoenzyme subunit is appropriate (jimenez2008decipheringthegenetic pages 2-3, brickman2018thebordetellabronchiseptica pages 3-4) |
| nudC | PP_4029 | Q88FQ8 | boundary context | homology | boundary_only | NAD-capped RNA hydrolase/DeNADding enzyme; relevant to NAD turnover and RNA cap biology but outside core biosynthesis/salvage/catabolism boundaries |
| gabD-II | PP_4422 | Q88EN2 | boundary context | homology | boundary_only | NADP+-dependent succinate semialdehyde dehydrogenase; central aldehyde/GABA metabolism paralog, not specific nicotinate pathway component |
| nadD | PP_4810 | Q88DL5 | de novo biosynthesis | genome annotation | covered | NaMN adenylyltransferase forming deamido-NAD from NaMN; canonical downstream de novo/salvage convergence step in bacterial NAD biosynthesis |
| pncB | PP_4868 | Q88DF7 | salvage | genome annotation | covered | Nicotinate phosphoribosyltransferase; establishes nicotinate salvage entry to NaMN; expected bona fide salvage step in KT2440 though direct gene-specific experiments were not found |
| nadE | PP_4869 | Q88DF6 | de novo biosynthesis | genome annotation | covered | NAD synthetase amidating deamido-NAD to NAD+; convergent terminal step for de novo and salvage routes; standard core enzyme in bacterial NAD metabolism |
| cobB__Q88BY5 | PP_5402 | Q88BY5 | boundary context | homology | boundary_only | NAD-dependent sirtuin-like protein deacylase; consumes NAD+ in regulatory protein deacylation, but is not part of pathway satisfiability for NAD biosynthesis or nicotinate catabolism |
| pntAB | PP_5747 | A0A140FVX3 | NADP+ formation & transhydrogenases | direct experimental in KT2440 | covered | Alpha part 2 of split membrane PntAB transhydrogenase; should be curated together with pntAA and pntB as one enzyme complex rather than separate independent steps (partipilo2025integratedcontrolof pages 1-6, nikel2016pyridinenucleotidetranshydrogenases pages 1-2) |


*Table: This table summarizes all 30 candidate genes associated with KEGG ppu00760 in Pseudomonas putida KT2440, organized by functional category, evidence strength, module-status assessment, and curation notes. It is useful for deciding which genes truly satisfy NAD biosynthesis/nicotinate metabolism steps versus genes that are only pathway-adjacent boundary context.*

| Module Step | Step Description | Covering Gene(s) | Status | Evidence Level | Notes |
|---|---|---|---|---|---|
| De novo: NadB | L-aspartate oxidase; initiates de novo NAD biosynthesis from L-aspartate | **nadB / PP_1426** | covered | genome annotation | Canonical bacterial first step is present in KT2440 annotations and metabolic models; also highlighted as an O\_2-linked limitation for anoxic growth models, supporting functional expectation in this species (kampers2019insilicoguidedengineering pages 5-7, kampers2019insilicoguidedengineering pages 3-5) |
| De novo: NadA | Quinolinate synthase | **nadA / PP_1231** | covered | genome annotation | Expected canonical partner of NadB in quinolinate formation; present in KT2440 genome annotations and retained in species-scale reconstructions, but no step-specific direct experiment found in KT2440 (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2, belda2016therevisitedgenome pages 10-12) |
| De novo: NadC | Quinolinate phosphoribosyltransferase | **nadC / PP_0787** | covered | genome annotation | Standard de novo step converting quinolinate to NaMN; supported by curated genome/metabolic reconstructions rather than direct biochemical study in KT2440 (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2, belda2016therevisitedgenome pages 10-12) |
| De novo: NadD | NaMN adenylyltransferase | **nadD / PP_4810** | covered | genome annotation | Canonical convergent step for de novo and salvage routes; present in KT2440 annotation, but no direct KT2440 enzymology located (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2) |
| De novo: NadE | NAD+ synthetase | **nadE / PP_4869** | covered | genome annotation | Terminal amidation step to NAD+ is expected and annotated in KT2440; no direct KT2440 gene-specific experiment found in retrieved evidence (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2) |
| Salvage: PncB | Nicotinate phosphoribosyltransferase | **pncB / PP_4868** | covered | genome annotation | Nicotinate salvage entry to NaMN is annotated in KT2440; direct species-specific validation was not found, so evidence is annotation-level rather than experimental (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2, belda2016therevisitedgenome pages 10-12) |
| Salvage: PncC | NMN amidohydrolase | **pncC / PP_1628** | covered | genome annotation | Supports NMN-to-NaMN deamidating salvage branch; annotated in candidate set, but direct KT2440 validation not found in retrieved literature (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2) |
| Salvage: PncA | Nicotinamidase; nicotinamide-to-nicotinate salvage entry | **No clear candidate in provided set** | gap | homology-based | Important curation gap: a canonical bacterial nicotinamide salvage enzyme was not present in the candidate list, and no confident KT2440 assignment was recovered here. This may indicate true absence, noncanonical salvage, or missing annotation; should be reviewed explicitly rather than assumed present (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2, belda2016therevisitedgenome pages 10-12) |
| NADP+: NadK | NAD kinase; converts NAD+ to NADP+ | **nadK / PP_2012** | covered | genome annotation | Core pyridine nucleotide pool-forming step is annotated and expected in KT2440; direct KT2440 gene-focused validation not retrieved, but NADPH-centered physiology of the species makes this step biologically essential (i.2021reconfigurationofmetabolic pages 1-2, i.2021reconfigurationofmetabolic pages 7-8) |
| Transhydrogenase: SthA | Soluble pyridine nucleotide transhydrogenase | **sthA / PP_2151** | covered | direct experimental | Strong KT2440 evidence: SthA is the soluble transhydrogenase, contributes >70% of total transhydrogenase activity in extracts, and is important for redox homeostasis and some substrate regimes (nikel2016pyridinenucleotidetranshydrogenases pages 1-2, nikel2016pyridinenucleotidetranshydrogenases pages 7-9, nikel2016pyridinenucleotidetranshydrogenases pages 6-7) |
| Transhydrogenase: PntAB | Membrane-bound proton-translocating transhydrogenase | **pntAA / PP_0156 + pntAB / PP_5747 + pntB / PP_0155** | covered | direct experimental | KT2440 uses a split gene architecture for the alpha subunit; together these encode the membrane transhydrogenase complex. Directly studied in KT2440 redox balancing and aromatic-compound metabolism (partipilo2025integratedcontrolof pages 1-6, nikel2016pyridinenucleotidetranshydrogenases pages 1-2, nikel2016pyridinenucleotidetranshydrogenases pages 6-7) |
| Nicotinate catabolism: NicAB | Nicotinate hydroxylase converting nicotinate to 6-hydroxynicotinate | **nicA / PP_3947 + nicB / PP_3948** | covered | direct experimental | Part of the experimentally validated **nic** cluster; knockout and transfer studies support necessity for aerobic nicotinate utilization in KT2440 (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 1-2, brickman2018thebordetellabronchiseptica pages 3-4) |
| Nicotinate catabolism: NicC | 6-hydroxynicotinate 3-monooxygenase | **nicC / PP_3944** | covered | direct experimental | Directly assigned in the KT2440 nic cluster and required for growth on nicotinate; also under NicR/FinR control (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 1-2, xiao2018finrregulatesexpression pages 6-8) |
| Nicotinate catabolism: NicX | 2,5-dihydroxypyridine 5,6-dioxygenase | **nicX / PP_3945** | covered | direct experimental | Key ring-cleavage step in the maleamate pathway; directly validated in KT2440 nic-cluster work and later regulatory studies (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 1-2, xiao2018finrregulatesexpression pages 6-8) |
| Nicotinate catabolism: NicD | N-formylmaleamate deformylase | **nicD / PP_3943** | covered | direct experimental | Experimentally assigned within the KT2440 nic locus; converts N-formylmaleamate to maleamate/formate branch products (jimenez2008decipheringthegenetic pages 1-2, jimenez2008decipheringthegenetic pages 5-6) |
| Nicotinate catabolism: NicF | Maleamate amidohydrolase | **nicF / PP_3941** | covered | direct experimental | Downstream maleamate-pathway enzyme in the validated KT2440 nic cluster; direct cluster-level evidence supports assignment (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 5-6) |
| Nicotinate catabolism: MaiA/NicE | Maleate isomerase converting maleate to fumarate | **maiA / PP_3942** | covered | direct experimental | Curation note: pathway literature often calls this step **NicE**, but the KT2440 candidate list labels the gene **maiA**. Functionally this is the nicotinate-catabolic maleate isomerase step and should be mapped accordingly (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 5-6) |


*Table: This table summarizes step-by-step pathway coverage for NAD biosynthesis, salvage, redox interconversion, and nicotinate catabolism in Pseudomonas putida KT2440. It is useful for curation because it distinguishes experimentally supported steps from annotation-only assignments and highlights the unresolved PncA salvage gap.*

## 4. Candidate Genes and Evidence

### 4.1 De novo NAD⁺ biosynthesis (NadB → NadA → NadC → NadD → NadE)

The canonical bacterial de novo pathway converts L-aspartate to NAD⁺ in five enzymatic steps. All five genes are annotated in the KT2440 genome and incorporated into genome-scale metabolic models including iJN1462 (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2). **NadB** (PP_1426, L-aspartate oxidase, EC 1.4.3.16) has received particular attention because it uses molecular oxygen as an electron acceptor, constituting one of three O₂-dependent reactions that limit anaerobic growth of KT2440 (kampers2019insilicoguidedengineering pages 5-7, kampers2019insilicoguidedengineering pages 3-5, kampers2020microbiallifestyleengineering pages 79-82). In *E. coli*, NadB can alternatively use fumarate, but whether the *P. putida* ortholog retains this capacity has not been experimentally verified (kampers2019insilicoguidedengineering pages 5-7). **NadA** (PP_1231, quinolinate synthase, EC 2.5.1.72), **NadC** (PP_0787, quinolinate phosphoribosyltransferase, EC 2.4.2.19), **NadD** (PP_4810, NaMN adenylyltransferase, EC 2.7.7.18), and **NadE** (PP_4869, NAD⁺ synthetase, EC 6.3.1.5) are all supported by genome annotation and metabolic model inclusion. Notably, nadE and pncB are genomically adjacent (PP_4869 and PP_4868), consistent with the convergent nature of the de novo and salvage routes at the NadD step. No direct biochemical characterization of these individual enzymes in *P. putida* KT2440 was identified in the retrieved literature; evidence is genome-annotation-level supported by functional metabolic modeling.

**Evidence type**: Genome annotation, metabolic model validation. **Confidence**: High for presence; moderate for biochemical properties (inferred from *E. coli* and general bacterial homology).

### 4.2 Nicotinate salvage to NAD⁺ (PncB, PncC, and the PncA gap)

**PncB** (PP_4868, nicotinate phosphoribosyltransferase, EC 6.3.4.21) converts nicotinate to nicotinate mononucleotide (NaMN) using PRPP, providing the salvage entry point. **PncC** (PP_1628, NMN amidohydrolase, EC 3.5.1.42) deamidates nicotinamide mononucleotide (NMN) to NaMN. Both are annotated in the KT2440 genome and included in metabolic reconstructions (belda2016therevisitedgenome pages 10-12).

A notable gap is the absence of **PncA** (nicotinamidase) from the candidate gene list. In many bacteria, PncA converts nicotinamide (Nam) to nicotinate (NA), providing the upstream step that feeds into PncB. The lack of a clearly identified PncA ortholog in the candidate set could indicate: (a) true absence if *P. putida* KT2440 does not recycle nicotinamide via this route; (b) annotation under a different gene name not captured in this module; or (c) replacement by a non-orthologous enzyme. This warrants explicit curation review.

**Evidence type**: Genome annotation. **Confidence**: High for PncB/PncC presence; uncertain for completeness of salvage pathway without PncA clarification.

### 4.3 NADP⁺ formation and transhydrogenase system

**NadK** (PP_2012, NAD kinase, EC 2.7.1.23) phosphorylates NAD⁺ to NADP⁺ and is annotated in the KT2440 genome. No direct enzymology in KT2440 was recovered, but the step is biologically essential given the organism's heavy reliance on NADPH.

The transhydrogenase system in *P. putida* KT2440 has been extensively characterized with direct experimental evidence. **SthA** (PP_2151, soluble transhydrogenase, EC 1.6.1.1) is a 464-amino-acid FAD-containing protein (50.9 kDa) sharing 99% identity with *P. aeruginosa* PAO1 SthA and 60% with *E. coli* SthA (nikel2016pyridinenucleotidetranshydrogenases pages 4-6). SthA accounts for greater than 70% of total transhydrogenase activity in cell-free extracts and is indispensable for growth on acetate (nikel2016pyridinenucleotidetranshydrogenases pages 7-9, partipilo2025integratedcontrolof pages 6-9). The **membrane-bound PntAB complex** is encoded by three genes in a split architecture: pntAA (PP_0156, alpha subunit part 1), pntAB (PP_5747, alpha subunit part 2), and pntB (PP_0155, beta subunit, 478 amino acids, 50.2 kDa) (partipilo2025integratedcontrolof pages 1-6, nikel2016pyridinenucleotidetranshydrogenases pages 6-7). This proton-translocating transhydrogenase is coupled to the proton-motive force.

Recent work by Partipilo et al. (2025) demonstrated that both transhydrogenases function as a cooperative, reversible redox-balancing system rather than operating in fixed directions (partipilo2025integratedcontrolof pages 15-18, partipilo2025integratedcontrolof pages 6-9). In wild-type cells, transhydrogenation favors NADH over NADPH formation at a 3.5-fold faster rate (partipilo2025integratedcontrolof pages 6-9). While single deletions of either enzyme have minimal fitness impact, the double ΔpntAB ΔsthA mutant exhibits growth defects, reduced NAD⁺ and ATP levels, increased NADP⁺ and ADP, and severe glutathione depletion (partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6). Transhydrogenase expression increases significantly during growth on aromatic substrates such as benzoate and *m*-xylene, where activity approximately doubles (nikel2016pyridinenucleotidetranshydrogenases pages 7-9, nikel2016pyridinenucleotidetranshydrogenases pages 6-7). During formate co-feeding, both enzymes function synergistically to redistribute electrons and counter redox stress (partipilo2025integratedcontrolof pages 18-21, zobel2017metabolicresponseof pages 6-8).

**Evidence type**: Direct experimental in KT2440. **Confidence**: Very high.

### 4.4 Aerobic nicotinate catabolism (nic cluster)

The **nic gene cluster** (PP_3939–PP_3948, organized as nicTPFEDCXRAB) represents the best-characterized component of this module in KT2440, with extensive direct experimental evidence from Jiménez et al. (2008) (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 1-2, jimenez2008decipheringthegenetic pages 5-6, jimenez2008decipheringthegenetic pages 6-6). This was the first complete gene set identified for aerobic nicotinic acid degradation in any organism. The pathway proceeds through the maleamate pathway:

1. **NicAB** (PP_3947/PP_3948): A two-component nicotinate hydroxylase converting nicotinic acid (NA) to 6-hydroxynicotinic acid (6HNA). NicA is the small subunit containing a [2Fe-2S] cluster binding motif; NicB is the large subunit with sequence similarity to xanthine dehydrogenase family members (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 1-2).
2. **NicC** (PP_3944, EC 1.14.13.114): 6-hydroxynicotinate 3-monooxygenase, an FAD-dependent monooxygenase catalyzing decarboxylative hydroxylation of 6HNA to 2,5-dihydroxypyridine (2,5-DHP) (jimenez2008decipheringthegenetic pages 1-2).
3. **NicX** (PP_3945, EC 1.13.11.9): Fe²⁺-dependent 2,5-DHP 5,6-dioxygenase catalyzing ring cleavage to N-formylmaleamic acid (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 1-2).
4. **NicD** (PP_3943, EC 3.5.1.106): N-formylmaleamate deformylase converting N-formylmaleamic acid to maleamic acid and formate (jimenez2008decipheringthegenetic pages 1-2, jimenez2008decipheringthegenetic pages 5-6).
5. **NicF** (PP_3941, EC 3.5.1.107): Maleamate amidohydrolase converting maleamic acid to maleic acid and ammonia (jimenez2008decipheringthegenetic pages 5-6).
6. **MaiA/NicE** (PP_3942, EC 5.2.1.1): Maleate cis-trans isomerase converting maleic acid to fumaric acid, a TCA cycle intermediate (jimenez2008decipheringthegenetic pages 5-6).

Gene knockout studies confirmed that disruption of nicA, nicB, nicC, nicD, or nicX prevents growth on NA as sole carbon source (jimenez2008decipheringthegenetic pages 1-2). The complete cluster was transferable to other bacteria on a plasmid, conferring the ability to grow on NA (jimenez2008decipheringthegenetic pages 6-6). Orthologs of the nic cluster are found in selected *P. putida* strains (KT2440, F1, GB-1, W619) and in β-proteobacteria of the Burkholderiales order, including *Bordetella* species (jimenez2008decipheringthegenetic pages 5-6, brickman2018thebordetellabronchiseptica pages 3-3).

**Regulation**: The nic cluster is organized into three NA-inducible operons: nicAB (Pa promoter), nicXR (Px promoter), and nicCDEFTP (Pc promoter) (xiao2018finrregulatesexpression pages 3-4). NicR is a MarR-family transcriptional repressor whose activity is relieved by 6-hydroxynicotinic acid (6HNA) as the physiological inducer (xiao2018finrregulatesexpression pages 6-8, xiao2018finrregulatesexpression pages 4-6). FinR is a LysR-type transcriptional activator that cooperates with NicR; both proteins bind directly to the nicC and nicX promoter regions (xiao2018finrregulatesexpression pages 6-8, xiao2018finrregulatesexpression pages 8-10, xiao2018finrregulatesexpression pages 1-2, xiao2018finrregulatesexpression pages 12-13). Deletion of finR impairs growth on NA/6HNA and weakens operon induction (xiao2018finrregulatesexpression pages 1-2, xiao2018finrregulatesexpression pages 2-3).

**Curation note**: The gene commonly called **nicE** in pathway literature (maleate isomerase) is listed as **maiA** (PP_3942) in the candidate set. This name discrepancy should be harmonized in annotation databases.

**Evidence type**: Direct experimental in KT2440. **Confidence**: Very high.

### 4.5 Boundary/context genes

Ten genes in the candidate list are assessed as **boundary context** that should not be counted toward core module satisfiability:

- **davD** (PP_0213): Glutarate-semialdehyde dehydrogenase involved in lysine/glutarate catabolism (primary bucket ppu00350), not a pyridine nucleotide pathway step.
- **sad-I** (PP_2488), **sad-II** (PP_3151): NAD⁺-dependent succinate semialdehyde dehydrogenases involved in GABA/succinate metabolism (primary bucket ppu00350).
- **gabD-II** (PP_4422): NADP⁺-dependent succinate semialdehyde dehydrogenase, another GABA metabolism enzyme (primary bucket ppu00350).
- **ushA** (PP_1414): Periplasmic 5'-nucleotidase/cyclic phosphodiesterase with broad substrate specificity for nucleotide monophosphates; not specific to pyridine nucleotides.
- **surE** (PP_1620): 5'-nucleotidase involved in nucleotide stress response, not a dedicated NAD pathway enzyme.
- **PP_2531** (PP_2531): Annotated as 5'-nucleotidase without evidence for pyridine nucleotide specificity.
- **PP_3103** (PP_3103): Uncharacterized protein with no convincing functional evidence tying it to NAD/nicotinate metabolism.
- **nudC** (PP_4029): NAD-capped RNA hydrolase (DeNADding enzyme) relevant to RNA cap biology and NAD turnover, but not part of biosynthesis/salvage/catabolism (primary bucket ppu04146).
- **cobB** (PP_5402): NAD-dependent sirtuin-like protein deacylase that consumes NAD⁺ as a substrate; a downstream NAD-utilizing enzyme rather than a biosynthetic component.
- **mazG** (PP_1657): NTP pyrophosphohydrolase for nucleotide quality control (primary bucket ppu00770).

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Gaps

**PncA (nicotinamidase)**: The most notable gap is the absence of a clearly identified nicotinamidase (PncA) from the candidate gene list. In many Gram-negative bacteria, PncA converts nicotinamide to nicotinate, feeding the PncB salvage step. Whether *P. putida* KT2440 possesses a functional PncA ortholog under a different gene name, uses an alternative nicotinamide recycling mechanism, or genuinely lacks this salvage branch requires explicit investigation.

**NadB electron acceptor flexibility**: Whether KT2440 NadB can use fumarate as an alternative electron acceptor (as in *E. coli*) remains experimentally unresolved, though metabolic modeling has flagged this as relevant for anaerobic engineering (kampers2019insilicoguidedengineering pages 5-7).

### 5.2 Ambiguities

**maiA vs. nicE nomenclature**: The maleate isomerase step is called nicE in the original Jiménez et al. (2008) characterization (jimenez2008decipheringthegenetic pages 5-6) but listed as maiA in the candidate gene set. Both refer to PP_3942. This should be reconciled in annotation.

**PP_3103**: The uncharacterized protein at PP_3103 is included in the KEGG bucket but lacks functional annotation. Its placement within the module is uncertain and potentially represents over-propagated annotation.

**pntAA/pntAB split architecture**: The alpha subunit of the membrane-bound transhydrogenase is encoded by two genes (PP_0156 and PP_5747) at distant genomic loci. This split architecture is unusual and should be verified as genuine rather than an assembly or annotation artifact (partipilo2025integratedcontrolof pages 1-6).

### 5.3 Likely over-annotations (KEGG bucket spillover)

The inclusion of davD, sad-I/II, gabD-II, ushA, surE, PP_2531, mazG, nudC, and cobB in the ppu00760 bucket represents KEGG's broad assignment policy. These genes use NAD(P)⁺ as cofactors or act on nucleotides generally, but they do not participate in pyridine nucleotide biosynthesis, salvage, or catabolism. They should be flagged as **boundary_only** and excluded from module satisfiability scoring.

## 6. Module and GO-Curation Recommendations

### 6.1 Module step status recommendations

| Step | Recommended status |
|---|---|
| De novo: NadB, NadA, NadC, NadD, NadE | **covered** |
| Salvage: PncB, PncC | **covered** |
| Salvage: PncA (nicotinamidase) | **gap** — requires explicit search |
| NADP⁺ formation: NadK | **covered** |
| Transhydrogenases: SthA, PntAB | **covered** |
| Nicotinate catabolism: NicAB, NicC, NicX, NicD, NicF, MaiA | **covered** |
| Boundary genes (10 total) | **boundary_only** — exclude from satisfiability |
| PP_3103 | **candidate_uncertain** — needs review |

### 6.2 Module boundary revision

The generic KEGG module boundary is too broad for KT2440 curation purposes. It is recommended to split the 30-gene set into:
- **Core module**: nadB, nadA, nadC, nadD, nadE, pncB, pncC, nadK, sthA, pntAA, pntAB, pntB (12 genes for biosynthesis/salvage/interconversion)
- **Catabolic module**: nicA, nicB, nicC, nicX, nicD, nicF, maiA (7 genes for nicotinate catabolism)
- **Boundary context**: remaining 11 genes, tracked as peripheral

### 6.3 GO term considerations

- SthA (PP_2151) should carry GO:0008746 (NAD(P)⁺ transhydrogenase, Si-specific) and contextual annotation noting its primary contribution (>70%) to total transhydrogenase activity.
- PntAB subunits should be annotated as a single functional complex (GO:0008750, proton-translocating NAD(P)⁺ transhydrogenase) rather than three independent activities.
- MaiA (PP_3942) should carry both the systematic name and the nicE alias to reduce confusion in pathway literature cross-referencing.

## 7. Genes to Promote to Full Review

The following genes merit full fetch-gene review based on this analysis:

1. **nadB (PP_1426)**: Critical for understanding aerobic/anaerobic growth limitation; electron acceptor flexibility question unresolved.
2. **sthA (PP_2151)**: Central to KT2440 redox physiology; extensively characterized but complex reversible role warrants deep review.
3. **pntAA/pntAB/pntB (PP_0156/PP_5747/PP_0155)**: Split gene architecture and complex subunit organization require verification.
4. **PncA candidate search**: Dedicated search needed to determine if a nicotinamidase exists under an unrecognized gene name or paralog.
5. **PP_3103**: Uncharacterized protein needs explicit functional assessment.
6. **nicA/nicB (PP_3947/PP_3948)**: Well-characterized but molybdoenzyme cofactor dependency (molybdopterin, [2Fe-2S], cytochrome c) makes them interesting for deep review.

## 8. Key References

The primary literature supporting this review includes:

- **Jiménez et al. (2008)** PNAS 105:11329–11334 — Definitive characterization of the nic cluster for aerobic nicotinic acid degradation in KT2440 (jimenez2008decipheringthegenetic pages 2-3, jimenez2008decipheringthegenetic pages 1-2, jimenez2008decipheringthegenetic pages 5-6, jimenez2008decipheringthegenetic pages 6-6).
- **Xiao et al. (2018)** Appl. Environ. Microbiol. 84(20) — FinR regulatory role in nicC/nicX operon expression in KT2440 (xiao2018finrregulatesexpression pages 6-8, xiao2018finrregulatesexpression pages 8-10, xiao2018finrregulatesexpression pages 1-2, xiao2018finrregulatesexpression pages 4-6, xiao2018finrregulatesexpression pages 3-4).
- **Nikel et al. (2016)** Environ. Microbiol. 18:3565–3582 — Transhydrogenase characterization during aromatic compound biodegradation in KT2440 (nikel2016pyridinenucleotidetranshydrogenases pages 1-2, nikel2016pyridinenucleotidetranshydrogenases pages 4-6, nikel2016pyridinenucleotidetranshydrogenases pages 7-9, nikel2016pyridinenucleotidetranshydrogenases pages 6-7).
- **Partipilo et al. (2025)** BioRxiv doi:10.1101/2025.11.04.686620 — Integrated control of redox metabolism by PntAB and SthA across metabolic regimes (partipilo2025integratedcontrolof pages 15-18, partipilo2025integratedcontrolof pages 6-9, partipilo2025integratedcontrolof pages 1-6, partipilo2025integratedcontrolof pages 18-21).
- **Nikel et al. (2021)** ISME J. 15:1751–1766 — Metabolic flux reconfiguration for NADPH surplus under oxidative stress in KT2440 (i.2021reconfigurationofmetabolic pages 1-2, i.2021reconfigurationofmetabolic pages 7-8, nikel2020redoxstressreshapes pages 1-4).
- **Belda et al. (2016)** Environ. Microbiol. 18:3403–3424 — Revisited genome annotation of KT2440 including nic cluster and pyridine nucleotide metabolism (belda2016therevisitedgenome pages 10-12).
- **Nogales et al. (2020)** Environ. Microbiol. 22:255–269 — iJN1462 genome-scale metabolic model of KT2440 (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2).
- **Kampers et al. (2019)** Microb. Cell Fact. 18:170 — NadB oxygen dependency and anaerobic growth engineering (kampers2019insilicoguidedengineering pages 5-7, kampers2019insilicoguidedengineering pages 3-5, kampers2019insilicoguidedengineering pages 1-2).
- **Zobel et al. (2017)** Eng. Life Sci. 17:47–57 — Metabolic response to increased NADH regeneration rates (zobel2017metabolicresponseof pages 6-8).
- **Brickman & Armstrong (2018)** Mol. Microbiol. 108:397–409 — Bordetella nic locus comparison with KT2440 (brickman2018thebordetellabronchiseptica pages 3-3, brickman2018thebordetellabronchiseptica pages 3-4).

References

1. (i.2021reconfigurationofmetabolic pages 1-2): Pablo I Nikel, Tobias Fuhrer, Max Chavarría, Alberto Sánchez-Pascuala, Uwe Sauer, and Víctor de Lorenzo. Reconfiguration of metabolic fluxes in <i>pseudomonas putida</i> as a response to sub-lethal oxidative stress. The ISME Journal, 15:1751-1766, Jan 2021. URL: https://doi.org/10.1038/s41396-020-00884-9, doi:10.1038/s41396-020-00884-9. This article has 165 citations.

2. (nikel2020redoxstressreshapes pages 1-4): Pablo I. Nikel, Tobias Fuhrer, Max Chavarría, Alberto Sánchez-Pascuala, Uwe Sauer, and Víctor de Lorenzo. Redox stress reshapes carbon fluxes of pseudomonas putida for cytosolic glucose oxidation and nadph generation. bioRxiv, Jun 2020. URL: https://doi.org/10.1101/2020.06.13.149542, doi:10.1101/2020.06.13.149542. This article has 11 citations.

3. (i.2021reconfigurationofmetabolic pages 7-8): Pablo I Nikel, Tobias Fuhrer, Max Chavarría, Alberto Sánchez-Pascuala, Uwe Sauer, and Víctor de Lorenzo. Reconfiguration of metabolic fluxes in <i>pseudomonas putida</i> as a response to sub-lethal oxidative stress. The ISME Journal, 15:1751-1766, Jan 2021. URL: https://doi.org/10.1038/s41396-020-00884-9, doi:10.1038/s41396-020-00884-9. This article has 165 citations.

4. (nikel2016pyridinenucleotidetranshydrogenases pages 1-2): Pablo I. Nikel, Danilo Pérez‐Pantoja, and Víctor de Lorenzo. Pyridine nucleotide transhydrogenases enable redox balance of pseudomonas putida during biodegradation of aromatic compounds. Environmental microbiology, 18 10:3565-3582, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13434, doi:10.1111/1462-2920.13434. This article has 87 citations and is from a domain leading peer-reviewed journal.

5. (nikel2016pyridinenucleotidetranshydrogenases pages 6-7): Pablo I. Nikel, Danilo Pérez‐Pantoja, and Víctor de Lorenzo. Pyridine nucleotide transhydrogenases enable redox balance of pseudomonas putida during biodegradation of aromatic compounds. Environmental microbiology, 18 10:3565-3582, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13434, doi:10.1111/1462-2920.13434. This article has 87 citations and is from a domain leading peer-reviewed journal.

6. (partipilo2025integratedcontrolof pages 1-6): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

7. (nogales2020high‐qualitygenome‐scalemetabolic pages 1-2): Juan Nogales, Joshua Mueller, Steinn Gudmundsson, Francisco J. Canalejo, Estrella Duque, Jonathan Monk, Adam M. Feist, Juan Luis Ramos, Wei Niu, and Bernhard O. Palsson. High‐quality genome‐scale metabolic modelling of pseudomonas putida highlights its broad metabolic capabilities. Environmental Microbiology, 22:255-269, Nov 2020. URL: https://doi.org/10.1111/1462-2920.14843, doi:10.1111/1462-2920.14843. This article has 229 citations and is from a domain leading peer-reviewed journal.

8. (belda2016therevisitedgenome pages 10-12): Eugeni Belda, Ruben G. A. van Heck, Maria José Lopez‐Sanchez, Stéphane Cruveiller, Valérie Barbe, Claire Fraser, Hans‐Peter Klenk, Jörn Petersen, Anne Morgat, Pablo I. Nikel, David Vallenet, Zoé Rouy, Agnieszka Sekowska, Vitor A. P. Martins dos Santos, Víctor de Lorenzo, Antoine Danchin, and Claudine Médigue. The revisited genome of pseudomonas putida kt2440 enlightens its value as a robust metabolic chassis. Environmental microbiology, 18 10:3403-3424, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13230, doi:10.1111/1462-2920.13230. This article has 376 citations and is from a domain leading peer-reviewed journal.

9. (kampers2019insilicoguidedengineering pages 5-7): Linde F. C. Kampers, Ruben G. A. van Heck, Stefano Donati, Edoardo Saccenti, Rita J. M. Volkers, Peter J. Schaap, Maria Suarez-Diez, Pablo I. Nikel, and Vitor A. P. Martins dos Santos. In silico-guided engineering of pseudomonas putida towards growth under micro-oxic conditions. Microbial Cell Factories, Oct 2019. URL: https://doi.org/10.1186/s12934-019-1227-5, doi:10.1186/s12934-019-1227-5. This article has 39 citations and is from a peer-reviewed journal.

10. (kampers2019insilicoguidedengineering pages 3-5): Linde F. C. Kampers, Ruben G. A. van Heck, Stefano Donati, Edoardo Saccenti, Rita J. M. Volkers, Peter J. Schaap, Maria Suarez-Diez, Pablo I. Nikel, and Vitor A. P. Martins dos Santos. In silico-guided engineering of pseudomonas putida towards growth under micro-oxic conditions. Microbial Cell Factories, Oct 2019. URL: https://doi.org/10.1186/s12934-019-1227-5, doi:10.1186/s12934-019-1227-5. This article has 39 citations and is from a peer-reviewed journal.

11. (nikel2016pyridinenucleotidetranshydrogenases pages 4-6): Pablo I. Nikel, Danilo Pérez‐Pantoja, and Víctor de Lorenzo. Pyridine nucleotide transhydrogenases enable redox balance of pseudomonas putida during biodegradation of aromatic compounds. Environmental microbiology, 18 10:3565-3582, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13434, doi:10.1111/1462-2920.13434. This article has 87 citations and is from a domain leading peer-reviewed journal.

12. (nikel2016pyridinenucleotidetranshydrogenases pages 7-9): Pablo I. Nikel, Danilo Pérez‐Pantoja, and Víctor de Lorenzo. Pyridine nucleotide transhydrogenases enable redox balance of pseudomonas putida during biodegradation of aromatic compounds. Environmental microbiology, 18 10:3565-3582, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13434, doi:10.1111/1462-2920.13434. This article has 87 citations and is from a domain leading peer-reviewed journal.

13. (jimenez2008decipheringthegenetic pages 2-3): José I. Jiménez, Ángeles Canales, Jesús Jiménez-Barbero, Krzysztof Ginalski, Leszek Rychlewski, José L. García, and Eduardo Díaz. Deciphering the genetic determinants for aerobic nicotinic acid degradation: the nic cluster from pseudomonas putida kt2440. Proceedings of the National Academy of Sciences, 105:11329-11334, Aug 2008. URL: https://doi.org/10.1073/pnas.0802273105, doi:10.1073/pnas.0802273105. This article has 174 citations and is from a highest quality peer-reviewed journal.

14. (jimenez2008decipheringthegenetic pages 5-6): José I. Jiménez, Ángeles Canales, Jesús Jiménez-Barbero, Krzysztof Ginalski, Leszek Rychlewski, José L. García, and Eduardo Díaz. Deciphering the genetic determinants for aerobic nicotinic acid degradation: the nic cluster from pseudomonas putida kt2440. Proceedings of the National Academy of Sciences, 105:11329-11334, Aug 2008. URL: https://doi.org/10.1073/pnas.0802273105, doi:10.1073/pnas.0802273105. This article has 174 citations and is from a highest quality peer-reviewed journal.

15. (jimenez2008decipheringthegenetic pages 1-2): José I. Jiménez, Ángeles Canales, Jesús Jiménez-Barbero, Krzysztof Ginalski, Leszek Rychlewski, José L. García, and Eduardo Díaz. Deciphering the genetic determinants for aerobic nicotinic acid degradation: the nic cluster from pseudomonas putida kt2440. Proceedings of the National Academy of Sciences, 105:11329-11334, Aug 2008. URL: https://doi.org/10.1073/pnas.0802273105, doi:10.1073/pnas.0802273105. This article has 174 citations and is from a highest quality peer-reviewed journal.

16. (xiao2018finrregulatesexpression pages 6-8): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

17. (brickman2018thebordetellabronchiseptica pages 3-4): Timothy J. Brickman and Sandra K. Armstrong. The bordetella bronchiseptica nic locus encodes a nicotinic acid degradation pathway and the 6‐hydroxynicotinate‐responsive regulator bpsr. Molecular Microbiology, 108:397-409, May 2018. URL: https://doi.org/10.1111/mmi.13943, doi:10.1111/mmi.13943. This article has 14 citations and is from a domain leading peer-reviewed journal.

18. (kampers2020microbiallifestyleengineering pages 79-82): Linde F.C. Kampers. Microbial lifestyle engineering. ArXiv, 2020. URL: https://doi.org/10.18174/516082, doi:10.18174/516082. This article has 0 citations.

19. (partipilo2025integratedcontrolof pages 6-9): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

20. (partipilo2025integratedcontrolof pages 15-18): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

21. (partipilo2025integratedcontrolof pages 18-21): Michele Partipilo, Giusi Favoino, Òscar Puiggené, Catarina Rocha, Carina Meiners, Nicolás Gurdo, Stefano Donati, Daniel C. Volke, and Pablo I. Nikel. Integrated control of redox and energy metabolism by the membrane-bound and soluble transhydrogenases of <i>pseudomonas putida</i> across metabolic regimes. BioRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.04.686620, doi:10.1101/2025.11.04.686620. This article has 0 citations.

22. (zobel2017metabolicresponseof pages 6-8): Sebastian Zobel, Jannis Kuepper, Birgitta Ebert, Nick Wierckx, and Lars M. Blank. Metabolic response of pseudomonas putida to increased nadh regeneration rates. Engineering in Life Sciences, 17:47-57, Jan 2017. URL: https://doi.org/10.1002/elsc.201600072, doi:10.1002/elsc.201600072. This article has 48 citations and is from a peer-reviewed journal.

23. (jimenez2008decipheringthegenetic pages 6-6): José I. Jiménez, Ángeles Canales, Jesús Jiménez-Barbero, Krzysztof Ginalski, Leszek Rychlewski, José L. García, and Eduardo Díaz. Deciphering the genetic determinants for aerobic nicotinic acid degradation: the nic cluster from pseudomonas putida kt2440. Proceedings of the National Academy of Sciences, 105:11329-11334, Aug 2008. URL: https://doi.org/10.1073/pnas.0802273105, doi:10.1073/pnas.0802273105. This article has 174 citations and is from a highest quality peer-reviewed journal.

24. (brickman2018thebordetellabronchiseptica pages 3-3): Timothy J. Brickman and Sandra K. Armstrong. The bordetella bronchiseptica nic locus encodes a nicotinic acid degradation pathway and the 6‐hydroxynicotinate‐responsive regulator bpsr. Molecular Microbiology, 108:397-409, May 2018. URL: https://doi.org/10.1111/mmi.13943, doi:10.1111/mmi.13943. This article has 14 citations and is from a domain leading peer-reviewed journal.

25. (xiao2018finrregulatesexpression pages 3-4): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

26. (xiao2018finrregulatesexpression pages 4-6): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

27. (xiao2018finrregulatesexpression pages 8-10): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

28. (xiao2018finrregulatesexpression pages 1-2): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

29. (xiao2018finrregulatesexpression pages 12-13): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

30. (xiao2018finrregulatesexpression pages 2-3): Yujie Xiao, Wenjing Zhu, Huizhong Liu, Hailing Nie, Wenli Chen, and Qiaoyun Huang. Finr regulates expression of <i>nicc</i> and <i>nicx</i> operons, involved in nicotinic acid degradation in pseudomonas putida kt2440. Applied and Environmental Microbiology, Oct 2018. URL: https://doi.org/10.1128/aem.01210-18, doi:10.1128/aem.01210-18. This article has 10 citations and is from a peer-reviewed journal.

31. (kampers2019insilicoguidedengineering pages 1-2): Linde F. C. Kampers, Ruben G. A. van Heck, Stefano Donati, Edoardo Saccenti, Rita J. M. Volkers, Peter J. Schaap, Maria Suarez-Diez, Pablo I. Nikel, and Vitor A. P. Martins dos Santos. In silico-guided engineering of pseudomonas putida towards growth under micro-oxic conditions. Microbial Cell Factories, Oct 2019. URL: https://doi.org/10.1186/s12934-019-1227-5, doi:10.1186/s12934-019-1227-5. This article has 39 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__nad_biosynthesis_and_nicotinate_metabolism__ppu00760-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__nad_biosynthesis_and_nicotinate_metabolism__ppu00760-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. kampers2019insilicoguidedengineering pages 5-7
2. belda2016therevisitedgenome pages 10-12
3. nikel2016pyridinenucleotidetranshydrogenases pages 4-6
4. partipilo2025integratedcontrolof pages 6-9
5. jimenez2008decipheringthegenetic pages 1-2
6. jimenez2008decipheringthegenetic pages 5-6
7. jimenez2008decipheringthegenetic pages 6-6
8. xiao2018finrregulatesexpression pages 3-4
9. partipilo2025integratedcontrolof pages 1-6
10. zobel2017metabolicresponseof pages 6-8
11. nikel2020redoxstressreshapes pages 1-4
12. nikel2016pyridinenucleotidetranshydrogenases pages 1-2
13. nikel2016pyridinenucleotidetranshydrogenases pages 6-7
14. kampers2019insilicoguidedengineering pages 3-5
15. nikel2016pyridinenucleotidetranshydrogenases pages 7-9
16. jimenez2008decipheringthegenetic pages 2-3
17. xiao2018finrregulatesexpression pages 6-8
18. brickman2018thebordetellabronchiseptica pages 3-4
19. kampers2020microbiallifestyleengineering pages 79-82
20. partipilo2025integratedcontrolof pages 15-18
21. partipilo2025integratedcontrolof pages 18-21
22. brickman2018thebordetellabronchiseptica pages 3-3
23. xiao2018finrregulatesexpression pages 4-6
24. xiao2018finrregulatesexpression pages 8-10
25. xiao2018finrregulatesexpression pages 1-2
26. xiao2018finrregulatesexpression pages 12-13
27. xiao2018finrregulatesexpression pages 2-3
28. kampers2019insilicoguidedengineering pages 1-2
29. carboxylating
30. decarboxylating
31. B-specific
32. 2Fe-2S
33. https://doi.org/10.1038/s41396-020-00884-9,
34. https://doi.org/10.1101/2020.06.13.149542,
35. https://doi.org/10.1111/1462-2920.13434,
36. https://doi.org/10.1101/2025.11.04.686620,
37. https://doi.org/10.1111/1462-2920.14843,
38. https://doi.org/10.1111/1462-2920.13230,
39. https://doi.org/10.1186/s12934-019-1227-5,
40. https://doi.org/10.1073/pnas.0802273105,
41. https://doi.org/10.1128/aem.01210-18,
42. https://doi.org/10.1111/mmi.13943,
43. https://doi.org/10.18174/516082,
44. https://doi.org/10.1002/elsc.201600072,