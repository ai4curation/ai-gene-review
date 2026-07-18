---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T17:31:15.094097'
end_time: '2026-07-17T18:11:22.842113'
duration_seconds: 2407.75
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-arginine biosynthesis via acetylated ornithine (microbial)
  module_summary: De novo microbial L-arginine biosynthesis from L-glutamate through
    N-acetylated intermediates and L-ornithine. The module includes the linear route,
    in which ArgA initiates acetylation and ArgE hydrolyses N-acetyl-L-ornithine,
    and the cyclic route, in which bifunctional ArgJ can initiate the pathway and
    recycle the acetyl group from N-acetyl-L-ornithine. After ornithine formation,
    ArgF, ArgG, and ArgH convert it through L-citrulline and argininosuccinate to
    L-arginine. Carbamoyl-phosphate production is shared with pyrimidine metabolism
    and is intentionally outside the module boundary. Succinylated-intermediate, N-acetylcitrulline,
    and LysW-dependent arginine pathways are distinct implementations not expanded
    in this module.
  module_outline: "- L-arginine biosynthesis via acetylated ornithine\n  - 1. pathway-initiating\
    \ glutamate acetylation\n  - L-glutamate to N-acetyl-L-glutamate\n    - Alternative\
    \ versions by enzyme family: Glutamate acetylation enzyme variants\n      - Dedicated\
    \ ArgA implementation\n        - ArgA N-acetylglutamate synthase (molecular player:\
    \ ArgA N-acetylglutamate synthase family; activity or role: L-glutamate N-acetyltransferase\
    \ activity, acting on acetyl-CoA as donor)\n      - Bifunctional ArgJ initiation\
    \ implementation\n        - ArgJ acetyl-CoA-dependent initiating activity (molecular\
    \ player: bifunctional ArgJ family; activity or role: L-glutamate N-acetyltransferase\
    \ activity, acting on acetyl-CoA as donor)\n  - 2. acetylglutamate kinase\n  -\
    \ N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate\n    - ArgB acetylglutamate\
    \ kinase (molecular player: ArgB acetylglutamate kinase family; activity or role:\
    \ acetylglutamate kinase activity)\n  - 3. acetylglutamyl-phosphate reductase\n\
    \  - N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde\n\
    \    - Alternative versions by enzyme family: ArgC reductase family variants\n\
    \      - Type 1 ArgC implementation\n        - Type 1 ArgC reductase (molecular\
    \ player: type 1 ArgC family; activity or role: N-acetyl-gamma-glutamyl-phosphate\
    \ reductase activity)\n      - Type 2 ArgC implementation\n        - Type 2 ArgC\
    \ reductase (molecular player: type 2 ArgC family; activity or role: N-acetyl-gamma-glutamyl-phosphate\
    \ reductase activity)\n  - 4. acetylornithine aminotransferase\n  - N-acetyl-L-glutamate\
    \ 5-semialdehyde to N-acetyl-L-ornithine\n    - ArgD acetylornithine aminotransferase\
    \ (molecular player: anabolic ArgD-like acetylornithine aminotransferase family;\
    \ activity or role: N2-acetyl-L-ornithine:2-oxoglutarate 5-transaminase activity)\n\
    \  - 5. ornithine release\n  - N-acetyl-L-ornithine to L-ornithine\n    - Alternative\
    \ versions by reaction mechanism: Ornithine-release enzyme variants\n      - Cyclic\
    \ ArgJ transacetylation\n        - ArgJ ornithine acetyltransferase (molecular\
    \ player: bifunctional ArgJ family; activity or role: L-glutamate N-acetyltransferase\
    \ activity, acting on acetyl-L-ornithine as donor)\n      - Hydrolytic ArgE deacetylation\n\
    \        - ArgE acetylornithine deacetylase (molecular player: ArgE acetylornithine\
    \ deacetylase family; activity or role: acetylornithine deacetylase activity)\n\
    \  - 6. ornithine carbamoyltransferase\n  - L-ornithine to L-citrulline\n    -\
    \ Biosynthetic ornithine carbamoyltransferase (molecular player: biosynthetic\
    \ ArgF ornithine carbamoyltransferase family; activity or role: ornithine carbamoyltransferase\
    \ activity)\n  - 7. argininosuccinate synthase\n  - L-citrulline to argininosuccinate\n\
    \    - ArgG argininosuccinate synthase (molecular player: type 1 ArgG argininosuccinate\
    \ synthase family; activity or role: argininosuccinate synthase activity)\n  -\
    \ 8. terminal argininosuccinate lyase\n  - Argininosuccinate to L-arginine\n \
    \   - ArgH argininosuccinate lyase (molecular player: ArgH argininosuccinate lyase\
    \ family; activity or role: argininosuccinate lyase activity)"
  module_connections: '- L-glutamate to N-acetyl-L-glutamate precedes N-acetyl-L-glutamate
    to N-acetyl-L-glutamyl 5-phosphate

    - N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate precedes N-acetyl-L-glutamyl
    5-phosphate to N-acetyl-L-glutamate 5-semialdehyde

    - N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde precedes
    N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine

    - N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine precedes N-acetyl-L-ornithine
    to L-ornithine

    - N-acetyl-L-ornithine to L-ornithine precedes L-ornithine to L-citrulline

    - L-ornithine to L-citrulline precedes L-citrulline to argininosuccinate

    - L-citrulline to argininosuccinate precedes Argininosuccinate to L-arginine'
  pathway_query: ppu00220
  pathway_id: ppu00220
  pathway_name: Arginine biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00220 with 17 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '31'
  candidate_genes: '- argH: PP_0184 | P59618 | Argininosuccinate lyase (ASAL) (EC
    4.3.2.1) (Arginosuccinase) (EC 4.3.2.1; primary bucket kegg:ppu00220)

    - aruC: PP_0372 | Q88QW2 | Acetylornithine aminotransferase 2 (EC 2.6.1.11, EC
    2.6.1.13) (EC 2.6.1.11; 2.6.1.13; primary bucket kegg:ppu00300)

    - argC1: PP_0432 | Q88QQ6 | N-acetyl-gamma-glutamyl-phosphate reductase 1 (AGPR
    1) (EC 1.2.1.38) (N-acetyl-glutamate semialdehyde dehydrogenase 1) (NAGSA dehydrogenase
    1) (EC 1.2.1.38; primary bucket kegg:ppu00220)

    - gdhA: PP_0675 | Q88Q23 | Glutamate dehydrogenase (primary bucket kegg:ppu00910)

    - arcC: PP_0999 | Q88P54 | Carbamate kinase (primary bucket kegg:ppu00910)

    - arcB: PP_1000 | Q88P53 | Ornithine carbamoyltransferase, catabolic (OTCase)
    (EC 2.1.3.3) (EC 2.1.3.3; primary bucket kegg:ppu00220)

    - arcA: PP_1001 | Q88P52 | Arginine deiminase (ADI) (EC 3.5.3.6) (Arginine dihydrolase)
    (AD) (EC 3.5.3.6; primary bucket kegg:ppu00220)

    - argF: PP_1079 | Q88NX4 | Ornithine carbamoyltransferase (OTCase) (EC 2.1.3.3)
    (EC 2.1.3.3; primary bucket kegg:ppu00220)

    - argG: PP_1088 | P59604 | Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate
    ligase) (EC 6.3.4.5; primary bucket kegg:ppu00220)

    - argJ: PP_1346 | P59612 | Arginine biosynthesis bifunctional protein ArgJ [Cleaved
    into: Arginine biosynthesis bifunctional protein ArgJ alpha chain; Arginine biosynthesis
    bifunctional protein ArgJ beta chain] [Includes: Glutamate N-acetyltransferase
    (EC 2.3.1.35) (Ornithine acetyltransferase) (OATase) (Ornithine transacetylase);
    Amino-acid acetyltransferase (EC 2.3.1.1) (N-acetylglutamate synthase) (AGSase)]
    (EC 2.3.1.1; 2.3.1.35; primary bucket kegg:ppu00220)

    - alaA: PP_1872 | Q88LQ7 | Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2)
    (EC 2.6.1.2; primary bucket kegg:ppu00290)

    - gdhB: PP_2080 | Q88L55 | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) (EC
    1.4.1.2; primary bucket kegg:ppu00430)

    - puuA-I: PP_2178 | Q88KW1 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11;
    primary bucket kegg:ppu00910)

    - ansB: PP_2453 | Q88K39 | Glutaminase-asparaginase (EC 3.5.1.38) (L-ASNase/L-GLNase)
    (L-asparagine/L-glutamine amidohydrolase) (EC 3.5.1.38; primary bucket kegg:ppu00470)

    - ureA: PP_2843 | Q88J06 | Urease subunit gamma (EC 3.5.1.5) (Urea amidohydrolase
    subunit gamma) (EC 3.5.1.5; primary bucket kegg:ppu00220)

    - ureB: PP_2844 | Q88J05 | Urease subunit beta (EC 3.5.1.5) (Urea amidohydrolase
    subunit beta) (EC 3.5.1.5; primary bucket kegg:ppu00220)

    - ureC: PP_2845 | Q88J04 | Urease subunit alpha (EC 3.5.1.5) (Urea amidohydrolase
    subunit alpha) (EC 3.5.1.5; primary bucket kegg:ppu00220)

    - PP_3148: PP_3148 | Q88I53 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - PP_3571: PP_3571 | Q88GZ4 | Acetylornithine deacetylase (primary bucket kegg:ppu00220)

    - argC2: PP_3633 | P59308 | N-acetyl-gamma-glutamyl-phosphate reductase 2 (AGPR
    2) (EC 1.2.1.38) (N-acetyl-glutamate semialdehyde dehydrogenase 2) (NAGSA dehydrogenase
    2) (EC 1.2.1.38; primary bucket kegg:ppu00220)

    - PP_4399: PP_4399 | Q88EQ4 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - PP_4547: PP_4547 | Q88EB9 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - carB: PP_4723 | Q88DU6 | Carbamoyl phosphate synthase large chain (EC 6.3.4.16)
    (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain) (EC 6.3.4.16; 6.3.5.5;
    primary bucket kegg:ppu00220)

    - carA: PP_4724 | Q88DU5 | Carbamoyl phosphate synthase small chain (EC 6.3.5.5)
    (Carbamoyl phosphate synthetase glutamine chain) (EC 6.3.5.5; primary bucket kegg:ppu00220)

    - glnA: PP_5046 | Q88CY3 | Glutamine synthetase (EC 6.3.1.2) (EC 6.3.1.2; primary
    bucket kegg:ppu00910)

    - spuB: PP_5183 | Q88CJ7 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)

    - spuI: PP_5184 | Q88CJ6 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)

    - argA: PP_5185 | P0A0Z9 | Amino-acid acetyltransferase (EC 2.3.1.1) (N-acetylglutamate
    synthase) (AGS) (NAGS) (EC 2.3.1.1; primary bucket kegg:ppu00220)

    - argE: PP_5186 | Q88CJ5 | Acetylornithine deacetylase (EC 3.5.1.16) (EC 3.5.1.16;
    primary bucket kegg:ppu00220)

    - argB: PP_5289 | P59300 | Acetylglutamate kinase (EC 2.7.2.8) (N-acetyl-L-glutamate
    5-phosphotransferase) (NAG kinase) (NAGK) (EC 2.7.2.8; primary bucket kegg:ppu00220)

    - puuA-II: PP_5299 | Q88C84 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11;
    primary bucket kegg:ppu00910)'
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__arginine_biosynthesis__ppu00220-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__arginine_biosynthesis__ppu00220-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-arginine biosynthesis via acetylated ornithine (microbial) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00220
- Resolved ID: ppu00220
- Resolved name: Arginine biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00220 with 17 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 31

- argH: PP_0184 | P59618 | Argininosuccinate lyase (ASAL) (EC 4.3.2.1) (Arginosuccinase) (EC 4.3.2.1; primary bucket kegg:ppu00220)
- aruC: PP_0372 | Q88QW2 | Acetylornithine aminotransferase 2 (EC 2.6.1.11, EC 2.6.1.13) (EC 2.6.1.11; 2.6.1.13; primary bucket kegg:ppu00300)
- argC1: PP_0432 | Q88QQ6 | N-acetyl-gamma-glutamyl-phosphate reductase 1 (AGPR 1) (EC 1.2.1.38) (N-acetyl-glutamate semialdehyde dehydrogenase 1) (NAGSA dehydrogenase 1) (EC 1.2.1.38; primary bucket kegg:ppu00220)
- gdhA: PP_0675 | Q88Q23 | Glutamate dehydrogenase (primary bucket kegg:ppu00910)
- arcC: PP_0999 | Q88P54 | Carbamate kinase (primary bucket kegg:ppu00910)
- arcB: PP_1000 | Q88P53 | Ornithine carbamoyltransferase, catabolic (OTCase) (EC 2.1.3.3) (EC 2.1.3.3; primary bucket kegg:ppu00220)
- arcA: PP_1001 | Q88P52 | Arginine deiminase (ADI) (EC 3.5.3.6) (Arginine dihydrolase) (AD) (EC 3.5.3.6; primary bucket kegg:ppu00220)
- argF: PP_1079 | Q88NX4 | Ornithine carbamoyltransferase (OTCase) (EC 2.1.3.3) (EC 2.1.3.3; primary bucket kegg:ppu00220)
- argG: PP_1088 | P59604 | Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate ligase) (EC 6.3.4.5; primary bucket kegg:ppu00220)
- argJ: PP_1346 | P59612 | Arginine biosynthesis bifunctional protein ArgJ [Cleaved into: Arginine biosynthesis bifunctional protein ArgJ alpha chain; Arginine biosynthesis bifunctional protein ArgJ beta chain] [Includes: Glutamate N-acetyltransferase (EC 2.3.1.35) (Ornithine acetyltransferase) (OATase) (Ornithine transacetylase); Amino-acid acetyltransferase (EC 2.3.1.1) (N-acetylglutamate synthase) (AGSase)] (EC 2.3.1.1; 2.3.1.35; primary bucket kegg:ppu00220)
- alaA: PP_1872 | Q88LQ7 | Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2) (EC 2.6.1.2; primary bucket kegg:ppu00290)
- gdhB: PP_2080 | Q88L55 | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) (EC 1.4.1.2; primary bucket kegg:ppu00430)
- puuA-I: PP_2178 | Q88KW1 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11; primary bucket kegg:ppu00910)
- ansB: PP_2453 | Q88K39 | Glutaminase-asparaginase (EC 3.5.1.38) (L-ASNase/L-GLNase) (L-asparagine/L-glutamine amidohydrolase) (EC 3.5.1.38; primary bucket kegg:ppu00470)
- ureA: PP_2843 | Q88J06 | Urease subunit gamma (EC 3.5.1.5) (Urea amidohydrolase subunit gamma) (EC 3.5.1.5; primary bucket kegg:ppu00220)
- ureB: PP_2844 | Q88J05 | Urease subunit beta (EC 3.5.1.5) (Urea amidohydrolase subunit beta) (EC 3.5.1.5; primary bucket kegg:ppu00220)
- ureC: PP_2845 | Q88J04 | Urease subunit alpha (EC 3.5.1.5) (Urea amidohydrolase subunit alpha) (EC 3.5.1.5; primary bucket kegg:ppu00220)
- PP_3148: PP_3148 | Q88I53 | Glutamine synthetase (primary bucket kegg:ppu00910)
- PP_3571: PP_3571 | Q88GZ4 | Acetylornithine deacetylase (primary bucket kegg:ppu00220)
- argC2: PP_3633 | P59308 | N-acetyl-gamma-glutamyl-phosphate reductase 2 (AGPR 2) (EC 1.2.1.38) (N-acetyl-glutamate semialdehyde dehydrogenase 2) (NAGSA dehydrogenase 2) (EC 1.2.1.38; primary bucket kegg:ppu00220)
- PP_4399: PP_4399 | Q88EQ4 | Glutamine synthetase (primary bucket kegg:ppu00910)
- PP_4547: PP_4547 | Q88EB9 | Glutamine synthetase (primary bucket kegg:ppu00910)
- carB: PP_4723 | Q88DU6 | Carbamoyl phosphate synthase large chain (EC 6.3.4.16) (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain) (EC 6.3.4.16; 6.3.5.5; primary bucket kegg:ppu00220)
- carA: PP_4724 | Q88DU5 | Carbamoyl phosphate synthase small chain (EC 6.3.5.5) (Carbamoyl phosphate synthetase glutamine chain) (EC 6.3.5.5; primary bucket kegg:ppu00220)
- glnA: PP_5046 | Q88CY3 | Glutamine synthetase (EC 6.3.1.2) (EC 6.3.1.2; primary bucket kegg:ppu00910)
- spuB: PP_5183 | Q88CJ7 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)
- spuI: PP_5184 | Q88CJ6 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)
- argA: PP_5185 | P0A0Z9 | Amino-acid acetyltransferase (EC 2.3.1.1) (N-acetylglutamate synthase) (AGS) (NAGS) (EC 2.3.1.1; primary bucket kegg:ppu00220)
- argE: PP_5186 | Q88CJ5 | Acetylornithine deacetylase (EC 3.5.1.16) (EC 3.5.1.16; primary bucket kegg:ppu00220)
- argB: PP_5289 | P59300 | Acetylglutamate kinase (EC 2.7.2.8) (N-acetyl-L-glutamate 5-phosphotransferase) (NAG kinase) (NAGK) (EC 2.7.2.8; primary bucket kegg:ppu00220)
- puuA-II: PP_5299 | Q88C84 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11; primary bucket kegg:ppu00910)

## Generic Module Context

### Working Scope

De novo microbial L-arginine biosynthesis from L-glutamate through N-acetylated intermediates and L-ornithine. The module includes the linear route, in which ArgA initiates acetylation and ArgE hydrolyses N-acetyl-L-ornithine, and the cyclic route, in which bifunctional ArgJ can initiate the pathway and recycle the acetyl group from N-acetyl-L-ornithine. After ornithine formation, ArgF, ArgG, and ArgH convert it through L-citrulline and argininosuccinate to L-arginine. Carbamoyl-phosphate production is shared with pyrimidine metabolism and is intentionally outside the module boundary. Succinylated-intermediate, N-acetylcitrulline, and LysW-dependent arginine pathways are distinct implementations not expanded in this module.

### Provisional Biological Outline

- L-arginine biosynthesis via acetylated ornithine
  - 1. pathway-initiating glutamate acetylation
  - L-glutamate to N-acetyl-L-glutamate
    - Alternative versions by enzyme family: Glutamate acetylation enzyme variants
      - Dedicated ArgA implementation
        - ArgA N-acetylglutamate synthase (molecular player: ArgA N-acetylglutamate synthase family; activity or role: L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor)
      - Bifunctional ArgJ initiation implementation
        - ArgJ acetyl-CoA-dependent initiating activity (molecular player: bifunctional ArgJ family; activity or role: L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor)
  - 2. acetylglutamate kinase
  - N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate
    - ArgB acetylglutamate kinase (molecular player: ArgB acetylglutamate kinase family; activity or role: acetylglutamate kinase activity)
  - 3. acetylglutamyl-phosphate reductase
  - N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde
    - Alternative versions by enzyme family: ArgC reductase family variants
      - Type 1 ArgC implementation
        - Type 1 ArgC reductase (molecular player: type 1 ArgC family; activity or role: N-acetyl-gamma-glutamyl-phosphate reductase activity)
      - Type 2 ArgC implementation
        - Type 2 ArgC reductase (molecular player: type 2 ArgC family; activity or role: N-acetyl-gamma-glutamyl-phosphate reductase activity)
  - 4. acetylornithine aminotransferase
  - N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine
    - ArgD acetylornithine aminotransferase (molecular player: anabolic ArgD-like acetylornithine aminotransferase family; activity or role: N2-acetyl-L-ornithine:2-oxoglutarate 5-transaminase activity)
  - 5. ornithine release
  - N-acetyl-L-ornithine to L-ornithine
    - Alternative versions by reaction mechanism: Ornithine-release enzyme variants
      - Cyclic ArgJ transacetylation
        - ArgJ ornithine acetyltransferase (molecular player: bifunctional ArgJ family; activity or role: L-glutamate N-acetyltransferase activity, acting on acetyl-L-ornithine as donor)
      - Hydrolytic ArgE deacetylation
        - ArgE acetylornithine deacetylase (molecular player: ArgE acetylornithine deacetylase family; activity or role: acetylornithine deacetylase activity)
  - 6. ornithine carbamoyltransferase
  - L-ornithine to L-citrulline
    - Biosynthetic ornithine carbamoyltransferase (molecular player: biosynthetic ArgF ornithine carbamoyltransferase family; activity or role: ornithine carbamoyltransferase activity)
  - 7. argininosuccinate synthase
  - L-citrulline to argininosuccinate
    - ArgG argininosuccinate synthase (molecular player: type 1 ArgG argininosuccinate synthase family; activity or role: argininosuccinate synthase activity)
  - 8. terminal argininosuccinate lyase
  - Argininosuccinate to L-arginine
    - ArgH argininosuccinate lyase (molecular player: ArgH argininosuccinate lyase family; activity or role: argininosuccinate lyase activity)

### Known Relationships Among Steps

- L-glutamate to N-acetyl-L-glutamate precedes N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate
- N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate precedes N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde
- N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde precedes N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine
- N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine precedes N-acetyl-L-ornithine to L-ornithine
- N-acetyl-L-ornithine to L-ornithine precedes L-ornithine to L-citrulline
- L-ornithine to L-citrulline precedes L-citrulline to argininosuccinate
- L-citrulline to argininosuccinate precedes Argininosuccinate to L-arginine

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

# Module/Pathway/Taxon Review: L-Arginine Biosynthesis via Acetylated Ornithine in *Pseudomonas putida* KT2440

**Target pathway:** KEGG ppu00220 "Arginine biosynthesis" (acetylated-ornithine microbial route)
**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module area:** amino_acid_metabolism

---

## 1. Executive Summary

The acetylated-ornithine route to L-arginine is **complete and satisfiable** in *Pseudomonas putida* KT2440. All eight canonical steps of the module — from L-glutamate acetylation through argininosuccinate lysis to L-arginine — are encoded by identifiable genes in the KT2440 genome, and the strain is a documented prototroph, providing physiological confirmation that the pathway is functional. The module should therefore be marked **COVERED**.

However, the 31-gene candidate list supplied by local metadata is a substantial over-collection: only roughly **10–11 of the 31 candidates are true de novo arginine-biosynthesis pathway members**. The remainder are over-propagated or out-of-boundary assignments that co-map to KEGG map00220 for reasons of shared nodes or reaction chemistry: the entire catabolic arginine deiminase (ADI) operon (*arcABC*), carbamoyl-phosphate synthase (*carAB*, a shared precursor node explicitly outside the module boundary), urease (*ureABC*), five glutamine-synthetase / polyamine-ligase paralogs, and several glutamate/glutamine-handling enzymes (*gdhA*, *gdhB*, *alaA*, *ansB*). These should be flagged as **not_in_module** during curation.

Three curation-critical nuances emerged. First, the **K00611 paralog ambiguity** (ornithine carbamoyltransferase) is resolved by regulatory evidence from *Pseudomonas*: PP_1079 (*argF*) is the anabolic, arginine-repressed biosynthetic OTCase (module step 6), while PP_1000 (*arcB*) is the catabolic OTCase of the ADI operon and is **out of module**. Second, KT2440 has **no dedicated E. coli-type ArgD** (K00818) for step 4; the acetylornithine aminotransferase activity is supplied by promiscuous class-III AST-pathway transaminases. Third — and important for curation completeness — the candidate metadata **omits PP_4481 (argD/astC, K00840)**, a second dual-function transaminase relevant to step 4 that should be added to the module gene set. Redundancy is a recurring theme: dedicated ArgA plus bifunctional ArgJ at step 1, hydrolytic ArgE plus ArgJ transacetylase at step 5, and two ArgC paralogs at step 3.

---

## 2. Target-Organism Pathway Definition

### What is included

The module covers **de novo microbial L-arginine biosynthesis from L-glutamate through N-acetylated intermediates and L-ornithine**. The biochemical scope is the eight-reaction sequence:

```
L-glutamate
   │ (1) ArgA / ArgJ         N-acetylglutamate synthase
N-acetyl-L-glutamate
   │ (2) ArgB                acetylglutamate kinase
N-acetyl-L-glutamyl-5-phosphate
   │ (3) ArgC                N-acetyl-γ-glutamyl-phosphate reductase
N-acetyl-L-glutamate-5-semialdehyde
   │ (4) ArgD / AruC         acetylornithine aminotransferase
N-acetyl-L-ornithine
   │ (5) ArgE / ArgJ         ornithine release (hydrolysis or transacetylation)
L-ornithine
   │ (6) ArgF                ornithine carbamoyltransferase (anabolic)
L-citrulline
   │ (7) ArgG                argininosuccinate synthase
argininosuccinate
   │ (8) ArgH                argininosuccinate lyase
L-arginine
```

*P. putida* encodes both the **cyclic (ArgJ-dependent) implementation** and elements of the **linear (ArgA/ArgE) implementation** — the two are not mutually exclusive here, and the genome carries redundant machinery for the acetyl-management steps (1 and 5). This dual capacity is well-documented across *Pseudomonas* and consistent with the KEGG modules M00028 (glutamate ⇒ ornithine) and M00844 (ornithine ⇒ arginine).

### What must be kept separate

Several neighboring processes co-locate on the broad KEGG overview map00220 but must **not** be conflated with de novo biosynthesis for this module:

- **Catabolic arginine deiminase (ADI) pathway** (*arcABC*): runs arginine → ornithine + carbamoyl-P → CO₂ + ATP, the reverse physiological direction.
- **Arginine succinyltransferase (AST) catabolic pathway** (*aru* genes): the major aerobic arginine/ornithine utilization route in *Pseudomonas*; it shares transaminase enzymes with biosynthesis but is a distinct pathway (ppu00330).
- **Carbamoyl-phosphate synthesis** (*carAB*): a shared substrate node with pyrimidine metabolism, explicitly **outside** the module boundary per the working scope.
- **Urea cycle / urease** (*ureABC*): urea amidohydrolase chemistry, unrelated to de novo arg biosynthesis.
- **Glutamate/glutamine precursor supply** (glutamine synthetase paralogs, glutamate dehydrogenases): upstream precursor metabolism, outside module boundary.

### Alternate names / database definitions

- **KEGG:** ppu00220 "Arginine biosynthesis"; modules **M00028** (ornithine biosynthesis, glutamate ⇒ ornithine) and **M00844** (arginine biosynthesis, ornithine ⇒ arginine).
- **Route distinction:** the module intentionally excludes the succinylated-intermediate route, the N-acetylcitrulline route, and the **LysW-dependent** arginine/lysine route — these are distinct implementations not expanded here and not used by *P. putida* for this pathway.

---

## 3. Expected Step Model

| Step | Reaction | Expected family | KT2440 gene(s) | KO | Disposition |
|------|----------|-----------------|----------------|----|-----|
| 1 | L-Glu → N-acetyl-L-Glu | ArgA (dedicated) **or** ArgJ (bifunctional) | *argA*/PP_5185; *argJ*/PP_1346 | K14682; K00620 | **covered** (redundant) |
| 2 | N-acetyl-L-Glu → N-acetyl-L-Glu-5-P | ArgB | *argB*/PP_5289 | K00930 | **covered** |
| 3 | N-acetyl-L-Glu-5-P → N-acetyl-L-Glu-5-semialdehyde | ArgC (type 1/2) | *argC1*/PP_0432; *argC2*/PP_3633 | K00145 | **covered** (2 paralogs) |
| 4 | semialdehyde → N-acetyl-L-ornithine | ArgD / promiscuous AST transaminase | *aruC*/PP_0372; **+ *argD*/PP_4481 (add)** | K00821; K00840 | **covered** (via promiscuous enzymes) |
| 5 | N-acetyl-L-ornithine → L-ornithine | ArgE (hydrolytic) **or** ArgJ (transacetylase) | *argE*/PP_5186; *argJ*/PP_1346; PP_3571 (uncertain) | K01438; K00620 | **covered** (redundant) |
| 6 | L-ornithine → L-citrulline | ArgF (anabolic OTCase) | *argF*/PP_1079 | K00611 | **covered** |
| 7 | L-citrulline → argininosuccinate | ArgG | *argG*/PP_1088 | K01940 | **covered** |
| 8 | argininosuccinate → L-arginine | ArgH | *argH*/PP_0184 | K01755 | **covered** |

Every step is encoded. The step-ordering constraints in the module definition (1→2→3→4→5→6→7→8) are all satisfied.

---

## 4. Candidate Genes and Evidence

### 4.1 Core pathway genes (high confidence — module members)

**Step 1 — N-acetylglutamate synthase.** Two independent implementations are present. *argA*/**PP_5185** (UniProt **P0A0Z9**, K14682) is the dedicated ArgA/NAGS. This assignment is verified: a UniProtKB lookup of P0A0Z9 returns organism "*Pseudomonas putida* (strain KT2440)", gene *argA*/PP_5185, "Amino-acid acetyltransferase (NAGS)", and an organism_id:160488 + gene:argA search returns exactly this entry (F005). Comparative evidence from the close relative *P. aeruginosa* establishes that these organisms carry a classical AAK-GNAT NAGS: *"In many microorganisms, the first step of arginine biosynthesis is catalyzed by the classical N-acetylglutamate synthase (NAGS), an enzyme composed of N-terminal amino acid kinase (AAK) and C-terminal histone acetyltransferase (GNAT) domains"* ([PMID: 22447897](https://pubmed.ncbi.nlm.nih.gov/22447897/)). The second implementation, *argJ*/**PP_1346** (UniProt **P59612**, K00620), is confirmed bifunctional (α/β cleaved chains; glutamate N-acetyltransferase EC 2.3.1.35 + amino-acid acetyltransferase EC 2.3.1.1), providing the acetyl-CoA-dependent initiating activity (F005). Cross-species mechanistic support that ArgJ operates at both step 1 and step 5 comes from *N. gonorrhoeae*, whose *argJ* complements both *E. coli argE* and *argA* mutations ([PMID: 1339419](https://pubmed.ncbi.nlm.nih.gov/1339419/)).

**Step 2 — Acetylglutamate kinase.** *argB*/**PP_5289** (UniProt **P59300**, K00930), acetylglutamate kinase / NAGK (EC 2.7.2.8). Confirmed KT2440 entry (F005). Unambiguous, single-copy assignment.

**Step 3 — N-acetyl-γ-glutamyl-phosphate reductase (AGPR).** Two paralogs: *argC1*/**PP_0432** (Q88QQ6) and *argC2*/**PP_3633** (P59308), both K00145 (EC 1.2.1.38). This matches the module's "Type 1 / Type 2 ArgC" alternative-versions design. Both are annotated NAGSA dehydrogenases; either likely suffices for the step, so the step is robustly covered.

**Step 4 — Acetylornithine aminotransferase.** *No dedicated E. coli-type ArgD (K00818) exists in KT2440.* The activity is supplied by promiscuous class-III AST-pathway transaminases. *aruC*/**PP_0372** (Q88QW2, K00821, EC 2.6.1.11/2.6.1.13) is the only step-4 candidate in the 31-gene list, but its **primary local bucket is ppu00300** (lysine biosynthesis), signalling a cross-pathway/promiscuous assignment (it also carries N-succinyl-diaminopimelate aminotransferase activity, EC 2.6.1.17). In *P. aeruginosa* PAO1, *aruC* encodes the AST-pathway N2-succinylornithine 5-aminotransferase — the major aerobic arginine utilization route — and the same transaminase family supplies biosynthetic acetylornithine transamination: *"The arginine succinyltransferase (AST) pathway is the major arginine and ornithine utilization (aru) pathway under aerobic conditions in Pseudomonas aeruginosa"* and *"the aruR, aruC, aruD, aruB, and aruE genes specify the ArgR regulatory protein, N2-succinylornithine 5-aminotransferase"* ([PMID: 9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/)) (F002).

**Step 5 — Ornithine release.** Two mechanisms are present. Hydrolytic: *argE*/**PP_5186** (Q88CJ5, K01438, acetylornithine deacetylase EC 3.5.1.16). Transacetylation: the bifunctional *argJ*/PP_1346 ornithine acetyltransferase (OAT) activity recycles the acetyl group. A third candidate, **PP_3571** (Q88GZ4, "Acetylornithine deacetylase"), is of **uncertain** status (see §5). The redundancy of ArgE + ArgJ means the step is robustly covered regardless of PP_3571's true function.

**Step 6 — Ornithine carbamoyltransferase (anabolic).** *argF*/**PP_1079** (Q88NX4, K00611, EC 2.1.3.3). The K00611 paralog ambiguity is resolved by regulatory evidence: in *P. aeruginosa* PAO1, the arginine-inducible regulator ArgR binds the control regions of the *car* and *argF* operons, and *argF* encodes the anabolic OTCase required for arginine biosynthesis: *"an arginine-inducible DNA-binding protein that interacts with the control regions for the car and argF operons, encoding carbamoylphosphate synthetase and anabolic ornithine carbamoyltransferase, respectively. Both enzymes are required for arginine biosynthesis"* ([PMID: 9286980](https://pubmed.ncbi.nlm.nih.gov/9286980/)) and *"the arginine-repressible gene for anabolic ornithine carbamoyltransferase"* ([PMID: 1538697](https://pubmed.ncbi.nlm.nih.gov/1538697/)). By orthology, PP_1079 is the biosynthetic OTCase, whereas PP_1000 (*arcB*) is catabolic (F004). This is reinforced by *P. syringae*, where *argF*/OCTase is negatively regulated by *argR* similarly to *P. aeruginosa* ([PMID: 15150254](https://pubmed.ncbi.nlm.nih.gov/15150254/)).

**Step 7 — Argininosuccinate synthase.** *argG*/**PP_1088** (P59604, K01940, EC 6.3.4.5). Single-copy, unambiguous.

**Step 8 — Argininosuccinate lyase.** *argH*/**PP_0184** (P59618, K01755, EC 4.3.2.1). Confirmed KT2440 entry (F005). Single-copy, unambiguous; the terminal enzyme.

### 4.2 Metadata gap — gene to add

**PP_4481 (*argD*/*astC*, UniProt P59319, K00840).** A UniProt organism_id:160488 search returns **two** acetylornithine aminotransferases: Q88QW2 (*aruC*/PP_0372, in the candidate list) and **P59319 (argD/PP_4481, EC 2.6.1.11), which is NOT in the 31-gene candidate list** (F006). KEGG assigns PP_4481 to K00840 (*astC*, succinylornithine aminotransferase EC 2.6.1.81, pathway ppu00330, module M00879 AST pathway). Its *P. aeruginosa* ortholog PA0895 is the biochemically characterized AST N2-succinylornithine 5-aminotransferase ([PMID: 9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/)). Because both KT2440 transaminases are promiscuous dual catabolic/biosynthetic class-III enzymes, PP_4481 is a legitimate step-4 contributor and should be added to the module gene set for completeness.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Out-of-boundary / over-propagated candidates (flag not_in_module)

Of the 31 candidates, approximately 20 are not de novo arginine-biosynthesis members (F003):

| Category | Genes | KO | Why out of boundary |
|----------|-------|----|---------------------|
| Catabolic ADI operon | *arcA*/PP_1001, *arcB*/PP_1000, *arcC*/PP_0999 | K01478, K00611, K00926 | Arginine deiminase pathway — opposite direction (arginine degradation → ATP) |
| Carbamoyl-P synthase | *carA*/PP_4724, *carB*/PP_4723 | K01956, K01955 | Shared pyrimidine node; explicitly outside module scope |
| Urease | *ureA/B/C*/PP_2843-45 | K01430/K01429/K01428 | Urea amidohydrolase; urea-cycle node of map00220, not biosynthesis |
| Glutamine synthetase / polyamine ligase paralogs | *glnA*/PP_5046, PP_3148, PP_4399, PP_4547, *puuA-I*/PP_2178, *puuA-II*/PP_5299, *spuB*/PP_5183, *spuI*/PP_5184 | K01915 | Glutamate/glutamine and polyamine precursor supply — upstream of module |
| Glutamate handling | *gdhA*/PP_0675, *gdhB*/PP_2080, *alaA*/PP_1872, *ansB*/PP_2453 | K00262, K15371, K14260, K05597 | Precursor / amino-acid interconversion, not de novo arg biosynthesis |

The catabolic *arcABC* operon deserves emphasis: *arcB*/PP_1000 shares K00611 with the biosynthetic *argF* but is embedded in the ADI operon alongside *arcA* (arginine deiminase, K01478) and *arcC* (carbamate kinase, K00926) and runs toward citrulline degradation and ATP generation (F004). Transcriptomic data show KT2440 induces arginine-fermentation / ADI genes under anoxic and stress conditions ([PMID: 23036925](https://pubmed.ncbi.nlm.nih.gov/23036925/), [PMID: 23537069](https://pubmed.ncbi.nlm.nih.gov/23537069/)), confirming these are physiologically catabolic rather than biosynthetic.

### 5.2 Genuine ambiguities

- **PP_3571 (second "acetylornithine deacetylase", Q88GZ4):** annotated as an ArgE-family deacetylase but of uncertain physiological role. With *argE*/PP_5186 and ArgJ already covering step 5, PP_3571's contribution is redundant/uncertain — mark **candidate_uncertain**. It may be a substrate-promiscuous amidohydrolase rather than the biosynthetic enzyme.
- **Step 4 broad EC/GO mappings:** both PP_0372 (K00821, EC 2.6.1.11/2.6.1.13/2.6.1.17) and PP_4481 (K00840, EC 2.6.1.81/2.6.1.11) carry broad, multi-pathway EC assignments. Neither is a "clean" dedicated ArgD; both are promiscuous AST-type class-III transaminases. This is a genuine lineage-specific alternative, not an over-annotation to discard — but it should be curated as "promiscuous enzyme fills step" rather than "dedicated ArgD present."
- **Step 1/5 ArgJ vs ArgA/ArgE redundancy:** whether the cyclic (ArgJ) or linear (ArgA+ArgE) route dominates in vivo is not resolved from sequence alone; both are encoded.

### 5.3 Likely annotation over-propagation

The primary over-propagation driver is KEGG map00220's inclusion of urea-cycle and catabolic nodes, plus broad K01915 (glutamine synthetase) mapping. The single most consequential curation error to avoid is treating *arcB*/PP_1000 as the biosynthetic OTCase; regulatory evidence firmly assigns that role to *argF*/PP_1079.

---

## 6. Module and GO-Curation Recommendations

**Overall module disposition: COVERED (satisfiable).** All 8 steps are encoded and KT2440 is a documented prototroph (F001, F007).

Per-step curation marks:

| Step | Mark | Notes |
|------|------|-------|
| 1 | **covered** | argA/PP_5185 (dedicated) + argJ/PP_1346 (bifunctional) |
| 2 | **covered** | argB/PP_5289 |
| 3 | **covered** | argC1/PP_0432 + argC2/PP_3633 (two paralogs) |
| 4 | **covered** (via promiscuous enzymes) | aruC/PP_0372 + **add argD/PP_4481**; no dedicated E. coli-type ArgD |
| 5 | **covered** | argE/PP_5186 + argJ OAT; PP_3571 = candidate_uncertain |
| 6 | **covered** | argF/PP_1079 (anabolic); arcB/PP_1000 = not_in_module |
| 7 | **covered** | argG/PP_1088 |
| 8 | **covered** | argH/PP_0184 |

Actions:
1. **Add PP_4481 (argD/astC, K00840, UniProt P59319)** to the module gene set as a step-4 contributor.
2. **Flag ~20 candidates as not_in_module:** *arcABC*, *carAB*, *ureABC*, the eight K01915 GS/polyamine paralogs, *gdhA*, *gdhB*, *alaA*, *ansB*.
3. **Mark PP_3571 candidate_uncertain** (redundant/ambiguous step-5 deacetylase).
4. **Module boundaries are correct for this organism** — no module_needs_revision at the structural level. The generic scope (excluding carbamoyl-P, succinyl/LysW routes) fits KT2440 well. The only refinement is documenting that step 4 is served by promiscuous AST-type transaminases rather than a dedicated ArgD, which may warrant a GO annotation note (acetylornithine aminotransferase activity, GO:0003992, attributed to promiscuous class-III enzymes).
5. No new module document is required; a curation note on the ArgJ/ArgA + ArgE dual-implementation and the promiscuous step-4 transaminases is sufficient.

---

## 7. Genes to Promote to Full `fetch-gene` Review

Priority for full individual review:

1. **PP_4481 (argD/astC, P59319, K00840)** — highest priority; missing from candidate metadata, dual catabolic/biosynthetic transaminase, needs formal step-4 assignment.
2. **PP_0372 (aruC, Q88QW2, K00821)** — promiscuous transaminase with primary bucket in ppu00300; confirm biosynthetic step-4 role vs. catabolic/lysine roles.
3. **PP_3571 (Q88GZ4, ArgE-family)** — resolve whether it is a genuine biosynthetic step-5 deacetylase or a promiscuous amidohydrolase.
4. **PP_1079 (argF) vs PP_1000 (arcB)** — document the K00611 anabolic/catabolic split so downstream curation does not confuse them.
5. **PP_0432 (argC1) vs PP_3633 (argC2)** — clarify whether both AGPR paralogs are biosynthetic or one is condition-specific.

---

## 8. Mechanistic Model / Interpretation

The KT2440 pathway is best understood as a **redundant, promiscuity-tolerant biosynthetic network** overlaid on a strong catabolic arginine-handling capacity:

```
                 ┌─────────── DE NOVO BIOSYNTHESIS (module) ───────────┐
  L-Glu ─ArgA/ArgJ─▶ NAG ─ArgB─▶ NAG-5-P ─ArgC1/ArgC2─▶ NAG-semialdehyde
                                                                     │
                                            AruC/ArgD (promiscuous)  │ (4)
                                                                     ▼
  L-Arg ◀─ArgH─ ArgSucc ◀─ArgG─ L-Cit ◀─ArgF─ L-Orn ◀─ArgE/ArgJ─ N-Ac-Orn
   (8)            (7)            (6, anabolic)   (5)
   ▲
   │  ═══════ CATABOLISM (out of module) ═══════
   └─ ArcA (deiminase) ▶ L-Cit ─ ArcB (catabolic OTCase) ▶ Orn + carbamoyl-P
                                  ArcC (carbamate kinase) ▶ ATP
       AST pathway: shares AruC/ArgD transaminases with biosynthesis
```

Two features distinguish KT2440 from the textbook *E. coli* model. (1) It uses the **cyclic ArgJ route** (acetyl recycling) in addition to linear ArgA/ArgE, which is metabolically economical because the acetyl group is retained rather than lost as acetate. (2) Step 4 lacks a dedicated ArgD; instead the **catabolic AST-pathway transaminases (AruC, ArgD/PP_4481) moonlight** to supply the biosynthetic transamination — a form of enzyme sharing between the anabolic and catabolic arms. This shared-enzyme architecture is why so many candidate genes (transaminases, OTCases) show paralog ambiguity: the biosynthetic and catabolic pathways use structurally similar enzymes and co-map in KEGG. Regulatory control (ArgR repression of *argF* and *carAB*) is the biological signal that cleanly separates the anabolic member (*argF*) from its catabolic paralog (*arcB*).

---

## 9. Evidence Base

| PMID | Title (abbrev.) | Organism | Supports | Transfer strength |
|------|------|----------|----------|-------------------|
| [22447897](https://pubmed.ncbi.nlm.nih.gov/22447897/) | ArgA/NAGS functional dissection | *P. aeruginosa* | Classical AAK-GNAT NAGS = PP_5185 step-1 assignment (F001) | Strong (close relative) |
| [9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/) | *aru* genes of AST pathway | *P. aeruginosa* | AruC / ArgD are AST N2-succinylornithine 5-aminotransferases; promiscuous step-4 (F002, F006) | Strong (close relative) |
| [9286980](https://pubmed.ncbi.nlm.nih.gov/9286980/) | *argR* regulation | *P. aeruginosa* PAO1 | *argF* = anabolic OTCase required for arg biosynthesis (F004) | Strong |
| [1538697](https://pubmed.ncbi.nlm.nih.gov/1538697/) | *argF*/*aru* regulation | *P. aeruginosa* PAO | *argF* = arginine-repressible anabolic OTCase (F004) | Strong |
| [15150254](https://pubmed.ncbi.nlm.nih.gov/15150254/) | ArgR controls *argF* | *P. syringae* pv. phaseolicola | *argF*/OCTase ArgR-repressed, generalizes across *Pseudomonas* | Moderate |
| [1339419](https://pubmed.ncbi.nlm.nih.gov/1339419/) | *argJ* ornithine acetyltransferase | *N. gonorrhoeae* | ArgJ catalyzes acetylornithine→ornithine (step 5); complements *E. coli argE/argA* | Weak-moderate (distant, mechanism conserved) |
| [23036925](https://pubmed.ncbi.nlm.nih.gov/23036925/) | Anoxic KT2440 strains | *P. putida* KT2440 | Direct: anaerobic life induces arginine-fermentation (ADI) genes — confirms *arc* is catabolic | Direct (target) |
| [23537069](https://pubmed.ncbi.nlm.nih.gov/23537069/) | Pressure transcriptome | *P. putida* KT2440 | Direct: arginine deiminase pathway differentially expressed under stress | Direct (target) |
| [23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/) | D-amino acid metabolism | *P. putida* KT2440 | Direct: KT2440 catabolizes D/L-arginine; racemase/catabolic context | Direct (target) |

**Direct target-organism evidence** confirms KT2440 has an active catabolic arginine apparatus (ADI, AST, racemization) and is a prototroph. **The biosynthetic gene-to-step assignments rely primarily on strong homology transfer from *P. aeruginosa* PAO1** plus UniProt/KEGG annotation of the KT2440 proteome itself (verified for argA, argB, argH, argJ via UniProt REST, F005). No KT2440-specific enzymatic characterization of the individual biosynthetic Arg enzymes was located; this is the main evidence limitation.

---

## 10. Limitations and Knowledge Gaps

1. **Homology-based step assignments.** Most biosynthetic gene→step calls rest on ortholog transfer from *P. aeruginosa* and on KEGG/UniProt automated annotation, not on direct KT2440 enzymology. Transfer is strong (same genus, high identity) but not experimentally verified in the target strain.
2. **Step 4 enzyme identity.** The precise in vivo contribution of AruC/PP_0372 vs ArgD/PP_4481 to biosynthetic (vs catabolic) transamination in KT2440 is unresolved. Both are promiscuous; kinetic partitioning is unknown.
3. **PP_3571 function.** Its role (biosynthetic step-5 deacetylase vs promiscuous amidohydrolase) is undetermined.
4. **ArgJ vs ArgA/ArgE flux.** Which acetyl-management route dominates physiologically is not established.
5. **Metadata completeness.** The candidate list omitted PP_4481, indicating the local metadata bucket did not capture all relevant transaminases — other cross-mapped genes may also be incompletely represented.

---

## 11. Proposed Follow-up Experiments / Actions

**Curation actions (immediate):**
- Add PP_4481 (argD/astC, P59319) to the ppu00220 module gene set (step 4).
- Flag the ~20 out-of-boundary candidates as not_in_module (arcABC, carAB, ureABC, K01915 paralogs, gdhA/B, alaA, ansB).
- Mark PP_3571 candidate_uncertain; promote PP_4481, PP_0372, PP_3571, argF/arcB to full fetch-gene review.
- Add a curation note: step 4 served by promiscuous class-III AST transaminases (no dedicated ArgD).

**Experimental (to resolve gaps):**
- **Gene knockouts:** single deletions of *argA*, *argB*, *argC1*/*argC2* (double), *argE*, *argF*, *argG*, *argH*, *argJ*, and *aruC*/*argD* (single and double), scoring arginine auxotrophy on minimal medium ± arginine. This would directly confirm which genes are essential for de novo biosynthesis in KT2440 — the single most decisive experiment.
- **Enzyme assays:** recombinant AruC (PP_0372) and ArgD (PP_4481) tested for acetylornithine:2-oxoglutarate aminotransferase activity vs succinylornithine activity, to quantify biosynthetic vs catabolic partitioning.
- **PP_3571 characterization:** acetylornithine deacetylase activity assay and knockout phenotype in an *argE* background.
- **Regulatory confirmation:** verify ArgR-mediated arginine repression of PP_1079 (*argF*) but not PP_1000 (*arcB*) by qRT-PCR ± arginine, confirming the anabolic/catabolic split in KT2440 directly rather than by *P. aeruginosa* orthology.

**Expert questions:**
- Does KT2440 ever require a dedicated ArgD, or is the promiscuous-transaminase solution complete under all growth conditions?
- Is a GO-term request warranted to annotate "acetylornithine aminotransferase activity" onto the AST-type transaminases?

---

## 12. Key References

- [PMID: 22447897](https://pubmed.ncbi.nlm.nih.gov/22447897/) — Functional dissection of ArgA/NAGS in *P. aeruginosa*.
- [PMID: 9393691](https://pubmed.ncbi.nlm.nih.gov/9393691/) — Cloning of the *aru* genes (AST catabolic pathway) in *P. aeruginosa*.
- [PMID: 9286980](https://pubmed.ncbi.nlm.nih.gov/9286980/) — *argR* regulation of arginine biosynthesis/catabolism in *P. aeruginosa* PAO1.
- [PMID: 1538697](https://pubmed.ncbi.nlm.nih.gov/1538697/) — Regulation of anabolic *argF* and catabolic *aru* genes.
- [PMID: 15150254](https://pubmed.ncbi.nlm.nih.gov/15150254/) — ArgR control of *argF* in *P. syringae*.
- [PMID: 1339419](https://pubmed.ncbi.nlm.nih.gov/1339419/) — *argJ* ornithine acetyltransferase (*N. gonorrhoeae*), complements *E. coli argE/argA*.
- [PMID: 23036925](https://pubmed.ncbi.nlm.nih.gov/23036925/) — Anoxic KT2440 induces arginine-fermentation/ADI genes.
- [PMID: 23537069](https://pubmed.ncbi.nlm.nih.gov/23537069/) — KT2440 transcriptome: ADI pathway stress-sensitive.
- [PMID: 23995642](https://pubmed.ncbi.nlm.nih.gov/23995642/) — D-amino acid metabolism in KT2440 (arginine catabolism/prototrophy context).

---

### Consensus

The acetylated-ornithine L-arginine biosynthesis module is complete and satisfiable in *P. putida* KT2440: all eight steps are encoded, with redundant implementations at the acetyl-management steps (ArgA + bifunctional ArgJ at step 1; hydrolytic ArgE + ArgJ transacetylase at step 5) and two ArgC paralogs at step 3. Step 4 uses no dedicated ArgD but promiscuous AST-type transaminases — *aruC*/PP_0372 and *argD*/PP_4481 (the latter missing from the candidate list and needing to be added). Only ~10–11 of the 31 candidates are true pathway members; urease, glutamine-synthetase/polyamine paralogs, glutamate dehydrogenases, the catabolic *arc* (arginine-deiminase) operon, and carbamoyl-phosphate synthase are out-of-boundary over-propagations, and the biosynthetic OTCase is *argF*/PP_1079, not its catabolic K00611 paralog *arcB*/PP_1000.


## Artifacts

- [OpenScientist final report](PSEPK__arginine_biosynthesis__ppu00220-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__arginine_biosynthesis__ppu00220-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22447897
2. PMID:1339419
3. PMID:9393691
4. PMID:9286980
5. PMID:1538697
6. PMID:15150254
7. PMID:23036925
8. PMID:23537069
9. PMID:23995642