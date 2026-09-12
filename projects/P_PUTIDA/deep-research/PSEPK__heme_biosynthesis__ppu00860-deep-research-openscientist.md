---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T21:08:39.514872'
end_time: '2026-07-20T21:40:43.193781'
duration_seconds: 1923.68
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Heme B biosynthesis through alternative entry and oxidation routes
  module_summary: A reusable cross-taxon model of protoporphyrin-dependent heme B
    biosynthesis. C5 glutamyl-tRNA and C4/Shemin reactions are alternative routes
    to 5-aminolevulinate (ALA). A shared tetrapyrrole trunk then feeds independently
    selected oxygen-dependent or oxygen-independent coproporphyrinogen oxidases and
    HemJ-, HemG-, or HemY/PPOX-family protoporphyrinogen oxidases. All realizations
    converge at protoporphyrin IX, which a species-neutral ferrochelatase reaction
    converts to heme B.
  module_outline: "- Protoporphyrin-dependent heme B biosynthesis\n  - 1. formation\
    \ of protoporphyrin IX\n  - Formation of protoporphyrin IX\n    - 1. route-specific\
    \ formation of 5-aminolevulinate\n    - Alternative formation of 5-aminolevulinate\n\
    \      - Alternative versions by precursor route: 5-Aminolevulinate entry chemistry\n\
    \        - C5 glutamyl-tRNA formation of ALA\n          - Glutamyl-tRNA reductase\
    \ (molecular player: glutamyl-tRNA reductase family; activity or role: glutamyl-tRNA\
    \ reductase (NADP+) activity)\n          - Glutamate-1-semialdehyde 2,1-aminomutase\
    \ (molecular player: glutamate-1-semialdehyde 2,1-aminomutase family; activity\
    \ or role: glutamate-1-semialdehyde 2,1-aminomutase activity)\n        - C4/Shemin\
    \ ALA formation\n          - 5-Aminolevulinate synthase (molecular player: 5-aminolevulinate\
    \ synthase family; activity or role: 5-aminolevulinate synthase activity)\n  \
    \  - 2. shared ALA-to-coproporphyrinogen III trunk\n    - Shared tetrapyrrole\
    \ trunk\n      - 1. condensation of ALA to porphobilinogen\n      - ALA condensation\n\
    \        - Porphobilinogen synthase (molecular player: delta-aminolevulinate dehydratase\
    \ family; activity or role: porphobilinogen synthase activity)\n      - 2. polymerization\
    \ to hydroxymethylbilane\n      - Hydroxymethylbilane formation\n        - Hydroxymethylbilane\
    \ synthase (molecular player: porphobilinogen deaminase family; activity or role:\
    \ hydroxymethylbilane synthase activity)\n      - 3. cyclization to uroporphyrinogen\
    \ III\n      - Uroporphyrinogen III formation\n        - Uroporphyrinogen-III\
    \ synthase (molecular player: uroporphyrinogen-III synthase family; activity or\
    \ role: uroporphyrinogen-III synthase activity)\n      - 4. decarboxylation to\
    \ coproporphyrinogen III\n      - Coproporphyrinogen III formation\n        -\
    \ Uroporphyrinogen decarboxylase (molecular player: uroporphyrinogen decarboxylase\
    \ lineage; activity or role: uroporphyrinogen decarboxylase activity)\n    - 3.\
    \ formation of protoporphyrinogen IX\n    - Coproporphyrinogen III oxidation\n\
    \      - Alternative versions by oxygen dependence: Coproporphyrinogen oxidation\
    \ chemistry\n        - Oxygen-dependent HemF route\n          - Oxygen-dependent\
    \ coproporphyrinogen oxidase (molecular player: oxygen-dependent coproporphyrinogen\
    \ oxidase lineage; activity or role: coproporphyrinogen oxidase activity)\n  \
    \      - Oxygen-independent HemN route\n          - Oxygen-independent coproporphyrinogen\
    \ dehydrogenase (molecular player: oxygen-independent coproporphyrinogen oxidase\
    \ lineage; activity or role: coproporphyrinogen dehydrogenase activity)\n    -\
    \ 4. formation of protoporphyrin IX\n    - Protoporphyrinogen IX oxidation\n \
    \     - Alternative versions by enzyme family and terminal electron acceptor:\
    \ Protoporphyrinogen oxidase chemistry\n        - HemJ acceptor-dependent route\n\
    \          - HemJ-family protoporphyrinogen oxidase (molecular player: HemJ protoporphyrinogen\
    \ IX oxidase lineage; activity or role: protoporphyrinogen oxidase activity)\n\
    \        - HemG quinone-acceptor route\n          - HemG quinone-acceptor protoporphyrinogen\
    \ dehydrogenase (molecular player: HemG quinone-acceptor protoporphyrinogen dehydrogenase\
    \ lineage; activity or role: protoporphyrinogen oxidase activity, quinone as acceptor)\n\
    \        - HemY oxygen-acceptor route\n          - HemY/PgoX oxygen-dependent\
    \ protoporphyrinogen oxidase (molecular player: HemY/PPOX protoporphyrinogen oxidase\
    \ lineage; activity or role: protoporphyrinogen oxidase activity, oxygen as acceptor)\n\
    \  - 2. insertion of ferrous iron to form heme B\n  - Species-neutral ferrochelation\
    \ of protoporphyrin IX\n    - Protoporphyrin ferrochelatase (molecular player:\
    \ ferrochelatase family; activity or role: protoporphyrin ferrochelatase activity)"
  module_connections: '- Formation of protoporphyrin IX feeds into Species-neutral
    ferrochelation of protoporphyrin IX: Every valid combination of entry and late-step
    variants supplies protoporphyrin IX to ferrochelatase.

    - Alternative formation of 5-aminolevulinate feeds into Shared tetrapyrrole trunk:
    Either entry route supplies 5-aminolevulinate to the shared trunk.

    - Shared tetrapyrrole trunk feeds into Coproporphyrinogen III oxidation: Coproporphyrinogen
    III feeds an applicable oxygen-dependent or oxygen-independent oxidase.

    - Coproporphyrinogen III oxidation feeds into Protoporphyrinogen IX oxidation:
    Protoporphyrinogen IX feeds an applicable HemJ-, HemG-, or HemY/PPOX-family oxidase.

    - Glutamyl-tRNA reductase feeds into Glutamate-1-semialdehyde 2,1-aminomutase:
    HemA supplies glutamate-1-semialdehyde to HemL.

    - ALA condensation feeds into Hydroxymethylbilane formation: Porphobilinogen feeds
    HemC.

    - Hydroxymethylbilane formation feeds into Uroporphyrinogen III formation: Hydroxymethylbilane
    feeds HemD.

    - Uroporphyrinogen III formation feeds into Coproporphyrinogen III formation:
    Uroporphyrinogen III feeds HemE.'
  pathway_query: ppu00860
  pathway_id: ppu00860
  pathway_name: Porphyrin metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00860 with 45 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '46'
  candidate_genes: '- hemF: PP_0073 | Q88RQ6 | Oxygen-dependent coproporphyrinogen-III
    oxidase (CPO) (Coprogen oxidase) (Coproporphyrinogenase) (EC 1.3.3.3) (EC 1.3.3.3;
    primary bucket kegg:ppu00860)

    - PP_0109: PP_0109 | Q88RM0 | Cytochrome B (primary bucket kegg:ppu00860)

    - cyoE1: PP_0110 | Q88RL9 | Protoheme IX farnesyltransferase 1 (EC 2.5.1.141)
    (Heme B farnesyltransferase 1) (Heme O synthase 1) (EC 2.5.1.141; primary bucket
    kegg:ppu00860)

    - hemC: PP_0186 | Q88RE5 | Porphobilinogen deaminase (PBG) (EC 2.5.1.61) (Hydroxymethylbilane
    synthase) (HMBS) (Pre-uroporphyrinogen synthase) (EC 2.5.1.61; primary bucket
    kegg:ppu00860)

    - hemD: PP_0187 | Q88RE4 | Uroporphyrinogen-III synthase (EC 4.2.1.75) (EC 4.2.1.75;
    primary bucket kegg:ppu00860)

    - PP_0188: PP_0188 | Q88RE3 | Uroporphyrin-III C-methyltransferase (primary bucket
    kegg:ppu00860)

    - PP_0431: PP_0431 | Q88QQ7 | Protoporphyrinogen IX oxidase (PPO) (EC 1.3.99.-)
    (EC 1.3.99.-; primary bucket kegg:ppu00860)

    - bfr-I: PP_0482 | Q88QK8 | Bacterioferritin (EC 1.16.3.1) (EC 1.16.3.1; primary
    bucket kegg:ppu00860)

    - hemA: PP_0732 | Q88PW6 | Glutamyl-tRNA reductase (GluTR) (EC 1.2.1.70) (EC 1.2.1.70;
    primary bucket kegg:ppu00860)

    - hemH: PP_0744 | Q88PV4 | Ferrochelatase (EC 4.98.1.1) (Heme synthase) (Protoheme
    ferro-lyase) (EC 4.98.1.1; primary bucket kegg:ppu00860)

    - cyoE2: PP_0816 | Q88PN3 | Protoheme IX farnesyltransferase 2 (EC 2.5.1.141)
    (Heme B farnesyltransferase 2) (Heme O synthase 2) (EC 2.5.1.141; primary bucket
    kegg:ppu00860)

    - hemO: PP_1005 | Q88P48 | Heme oxygenase (primary bucket kegg:ppu00860)

    - bfr-II: PP_1082 | Q88NX1 | Bacterioferritin (EC 1.16.3.1) (EC 1.16.3.1; primary
    bucket kegg:ppu00860)

    - pduO: PP_1349 | Q88N66 | Corrinoid adenosyltransferase (EC 2.5.1.17) (Cob(II)alamin
    adenosyltransferase) (Cob(II)yrinic acid a,c-diamide adenosyltransferase) (Cobinamide/cobalamin
    adenosyltransferase) (EC 2.5.1.17; primary bucket kegg:ppu04980)

    - PP_1358: PP_1358 | Q88N58 | Heme iron utilization protein (primary bucket kegg:ppu00860)

    - cobO: PP_1672 | Q88MA2 | Corrinoid adenosyltransferase (EC 2.5.1.17) (Cob(II)alamin
    adenosyltransferase) (Cob(II)yrinic acid a,c-diamide adenosyltransferase) (EC
    2.5.1.17; primary bucket kegg:ppu00860)

    - cobB__Q88MA1: PP_1673 | Q88MA1 | Hydrogenobyrinate a,c-diamide synthase (EC
    6.3.5.9) (Hydrogenobyrinic acid a,c-diamide synthase) (EC 6.3.5.9; primary bucket
    kegg:ppu00860)

    - cobD: PP_1675 | Q88M99 | Cobalamin biosynthesis protein CobD (primary bucket
    kegg:ppu00860)

    - cobC: PP_1676 | Q88M98 | threonine-phosphate decarboxylase (EC 4.1.1.81) (L-threonine-O-3-phosphate
    decarboxylase) (EC 4.1.1.81; primary bucket kegg:ppu00860)

    - cobQ: PP_1677 | Q88M97 | Cobyric acid synthase (primary bucket kegg:ppu00860)

    - cobP: PP_1678 | Q88M96 | Bifunctional adenosylcobalamin biosynthesis protein
    (EC 2.7.1.156) (EC 2.7.7.62) (EC 2.7.1.156; 2.7.7.62; primary bucket kegg:ppu00860)

    - cobT: PP_1679 | Q88M95 | Nicotinate-nucleotide--dimethylbenzimidazole phosphoribosyltransferase
    (NN:DBI PRT) (EC 2.4.2.21) (N(1)-alpha-phosphoribosyltransferase) (EC 2.4.2.21;
    primary bucket kegg:ppu00860)

    - PP_1680: PP_1680 | Q88M94 | Alpha-ribazole-5''-phosphate phosphatase (EC 3.1.3.73)
    (EC 3.1.3.73; primary bucket kegg:ppu00860)

    - cobS: PP_1681 | Q88M93 | Adenosylcobinamide-GDP ribazoletransferase (EC 2.7.8.26)
    (Cobalamin synthase) (Cobalamin-5''-phosphate synthase) (EC 2.7.8.26; primary
    bucket kegg:ppu00860)

    - gltX: PP_1977 | Q88LF6 | Glutamate--tRNA ligase (EC 6.1.1.17) (Glutamyl-tRNA
    synthetase) (GluRS) (EC 6.1.1.17; primary bucket kegg:ppu00860)

    - cobA: PP_2090 | Q88L45 | uroporphyrinogen-III C-methyltransferase (EC 2.1.1.107)
    (EC 2.1.1.107; primary bucket kegg:ppu00860)

    - PP_2582: PP_2582 | Q88JR7 | Heme oxygenase (primary bucket kegg:ppu00860)

    - hemB: PP_2913 | Q88IT6 | Delta-aminolevulinic acid dehydratase (EC 4.2.1.24)
    (EC 4.2.1.24; primary bucket kegg:ppu00860)

    - hemBB: PP_3322 | Q88HN1 | Delta-aminolevulinic acid dehydratase (EC 4.2.1.24)
    (EC 4.2.1.24; primary bucket kegg:ppu00860)

    - PP_3409: PP_3409 | Q88HF1 | Cobalamin biosynthesis protein cobE (primary bucket
    kegg:ppu00860)

    - cobM: PP_3410 | Q88HF0 | Precorrin-4 C(11)-methyltransferase (EC 2.1.1.133)
    (EC 2.1.1.133; primary bucket kegg:ppu00860)

    - PP_3506: PP_3506 | Q88H59 | Magnesium chelatase, subunit ChII (primary bucket
    kegg:ppu00860)

    - cobN: PP_3507 | Q88H58 | Cobaltochelatase subunit CobN (EC 6.6.1.2) (EC 6.6.1.2;
    primary bucket kegg:ppu00860)

    - PP_3763: PP_3763 | Q88GG1 | CobF protein (primary bucket kegg:ppu00860)

    - cysG: PP_3999 | Q88FT3 | Siroheme synthase [Includes: Uroporphyrinogen-III C-methyltransferase
    (Urogen III methylase) (EC 2.1.1.107) (SUMT) (Uroporphyrinogen III methylase)
    (UROM); Precorrin-2 dehydrogenase (EC 1.3.1.76); Sirohydrochlorin ferrochelatase
    (EC 4.99.1.4)] (EC 1.3.1.76; 2.1.1.107; 4.99.1.4; primary bucket kegg:ppu00860)

    - hemN: PP_4264 | Q88F35 | Coproporphyrinogen-III oxidase (EC 1.3.98.3) (EC 1.3.98.3;
    primary bucket kegg:ppu00860)

    - hemL: PP_4784 | Q88DP0 | Glutamate-1-semialdehyde 2,1-aminomutase (GSA) (EC
    5.4.3.8) (Glutamate-1-semialdehyde aminotransferase) (GSA-AT) (EC 5.4.3.8; primary
    bucket kegg:ppu00860)

    - cobJ: PP_4826 | Q88DJ9 | Precorrin-3B C17-methyltransferase (primary bucket
    kegg:ppu00860)

    - cobI: PP_4827 | Q88DJ8 | Precorrin-2 C(20)-methyltransferase (EC 2.1.1.130)
    (EC 2.1.1.130; primary bucket kegg:ppu00860)

    - cobH: PP_4828 | Q88DJ7 | Precorrin-8X methylmutase (EC 5.4.99.61) (EC 5.4.99.61;
    primary bucket kegg:ppu00860)

    - cobG: PP_4829 | Q88DJ6 | Precorrin-3B synthase (EC 1.14.13.83) (EC 1.14.13.83;
    primary bucket kegg:ppu00860)

    - cobL: PP_4830 | Q88DJ5 | Precorrin-6Y C(5,15)-methyltransferase (EC 2.1.1.132)
    (EC 2.1.1.132; primary bucket kegg:ppu00860)

    - cbiD: PP_4831 | Q88DJ4 | Cobalt-precorrin-5B C(1)-methyltransferase (EC 2.1.1.195)
    (Cobalt-precorrin-6A synthase) (EC 2.1.1.195; primary bucket kegg:ppu00860)

    - cobK: PP_4832 | Q88DJ3 | Precorrin-6x reductase (primary bucket kegg:ppu00860)

    - PP_4856: PP_4856 | Q88DG9 | ferroxidase (EC 1.16.3.1) (EC 1.16.3.1; primary
    bucket kegg:ppu00860)

    - hemE: PP_5074 | Q88CV6 | Uroporphyrinogen decarboxylase (UPD) (URO-D) (EC 4.1.1.37)
    (EC 4.1.1.37; primary bucket kegg:ppu00860)'
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__heme_biosynthesis__ppu00860-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__heme_biosynthesis__ppu00860-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Heme B biosynthesis through alternative entry and oxidation routes in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00860
- Resolved ID: ppu00860
- Resolved name: Porphyrin metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00860 with 45 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 46

- hemF: PP_0073 | Q88RQ6 | Oxygen-dependent coproporphyrinogen-III oxidase (CPO) (Coprogen oxidase) (Coproporphyrinogenase) (EC 1.3.3.3) (EC 1.3.3.3; primary bucket kegg:ppu00860)
- PP_0109: PP_0109 | Q88RM0 | Cytochrome B (primary bucket kegg:ppu00860)
- cyoE1: PP_0110 | Q88RL9 | Protoheme IX farnesyltransferase 1 (EC 2.5.1.141) (Heme B farnesyltransferase 1) (Heme O synthase 1) (EC 2.5.1.141; primary bucket kegg:ppu00860)
- hemC: PP_0186 | Q88RE5 | Porphobilinogen deaminase (PBG) (EC 2.5.1.61) (Hydroxymethylbilane synthase) (HMBS) (Pre-uroporphyrinogen synthase) (EC 2.5.1.61; primary bucket kegg:ppu00860)
- hemD: PP_0187 | Q88RE4 | Uroporphyrinogen-III synthase (EC 4.2.1.75) (EC 4.2.1.75; primary bucket kegg:ppu00860)
- PP_0188: PP_0188 | Q88RE3 | Uroporphyrin-III C-methyltransferase (primary bucket kegg:ppu00860)
- PP_0431: PP_0431 | Q88QQ7 | Protoporphyrinogen IX oxidase (PPO) (EC 1.3.99.-) (EC 1.3.99.-; primary bucket kegg:ppu00860)
- bfr-I: PP_0482 | Q88QK8 | Bacterioferritin (EC 1.16.3.1) (EC 1.16.3.1; primary bucket kegg:ppu00860)
- hemA: PP_0732 | Q88PW6 | Glutamyl-tRNA reductase (GluTR) (EC 1.2.1.70) (EC 1.2.1.70; primary bucket kegg:ppu00860)
- hemH: PP_0744 | Q88PV4 | Ferrochelatase (EC 4.98.1.1) (Heme synthase) (Protoheme ferro-lyase) (EC 4.98.1.1; primary bucket kegg:ppu00860)
- cyoE2: PP_0816 | Q88PN3 | Protoheme IX farnesyltransferase 2 (EC 2.5.1.141) (Heme B farnesyltransferase 2) (Heme O synthase 2) (EC 2.5.1.141; primary bucket kegg:ppu00860)
- hemO: PP_1005 | Q88P48 | Heme oxygenase (primary bucket kegg:ppu00860)
- bfr-II: PP_1082 | Q88NX1 | Bacterioferritin (EC 1.16.3.1) (EC 1.16.3.1; primary bucket kegg:ppu00860)
- pduO: PP_1349 | Q88N66 | Corrinoid adenosyltransferase (EC 2.5.1.17) (Cob(II)alamin adenosyltransferase) (Cob(II)yrinic acid a,c-diamide adenosyltransferase) (Cobinamide/cobalamin adenosyltransferase) (EC 2.5.1.17; primary bucket kegg:ppu04980)
- PP_1358: PP_1358 | Q88N58 | Heme iron utilization protein (primary bucket kegg:ppu00860)
- cobO: PP_1672 | Q88MA2 | Corrinoid adenosyltransferase (EC 2.5.1.17) (Cob(II)alamin adenosyltransferase) (Cob(II)yrinic acid a,c-diamide adenosyltransferase) (EC 2.5.1.17; primary bucket kegg:ppu00860)
- cobB__Q88MA1: PP_1673 | Q88MA1 | Hydrogenobyrinate a,c-diamide synthase (EC 6.3.5.9) (Hydrogenobyrinic acid a,c-diamide synthase) (EC 6.3.5.9; primary bucket kegg:ppu00860)
- cobD: PP_1675 | Q88M99 | Cobalamin biosynthesis protein CobD (primary bucket kegg:ppu00860)
- cobC: PP_1676 | Q88M98 | threonine-phosphate decarboxylase (EC 4.1.1.81) (L-threonine-O-3-phosphate decarboxylase) (EC 4.1.1.81; primary bucket kegg:ppu00860)
- cobQ: PP_1677 | Q88M97 | Cobyric acid synthase (primary bucket kegg:ppu00860)
- cobP: PP_1678 | Q88M96 | Bifunctional adenosylcobalamin biosynthesis protein (EC 2.7.1.156) (EC 2.7.7.62) (EC 2.7.1.156; 2.7.7.62; primary bucket kegg:ppu00860)
- cobT: PP_1679 | Q88M95 | Nicotinate-nucleotide--dimethylbenzimidazole phosphoribosyltransferase (NN:DBI PRT) (EC 2.4.2.21) (N(1)-alpha-phosphoribosyltransferase) (EC 2.4.2.21; primary bucket kegg:ppu00860)
- PP_1680: PP_1680 | Q88M94 | Alpha-ribazole-5'-phosphate phosphatase (EC 3.1.3.73) (EC 3.1.3.73; primary bucket kegg:ppu00860)
- cobS: PP_1681 | Q88M93 | Adenosylcobinamide-GDP ribazoletransferase (EC 2.7.8.26) (Cobalamin synthase) (Cobalamin-5'-phosphate synthase) (EC 2.7.8.26; primary bucket kegg:ppu00860)
- gltX: PP_1977 | Q88LF6 | Glutamate--tRNA ligase (EC 6.1.1.17) (Glutamyl-tRNA synthetase) (GluRS) (EC 6.1.1.17; primary bucket kegg:ppu00860)
- cobA: PP_2090 | Q88L45 | uroporphyrinogen-III C-methyltransferase (EC 2.1.1.107) (EC 2.1.1.107; primary bucket kegg:ppu00860)
- PP_2582: PP_2582 | Q88JR7 | Heme oxygenase (primary bucket kegg:ppu00860)
- hemB: PP_2913 | Q88IT6 | Delta-aminolevulinic acid dehydratase (EC 4.2.1.24) (EC 4.2.1.24; primary bucket kegg:ppu00860)
- hemBB: PP_3322 | Q88HN1 | Delta-aminolevulinic acid dehydratase (EC 4.2.1.24) (EC 4.2.1.24; primary bucket kegg:ppu00860)
- PP_3409: PP_3409 | Q88HF1 | Cobalamin biosynthesis protein cobE (primary bucket kegg:ppu00860)
- cobM: PP_3410 | Q88HF0 | Precorrin-4 C(11)-methyltransferase (EC 2.1.1.133) (EC 2.1.1.133; primary bucket kegg:ppu00860)
- PP_3506: PP_3506 | Q88H59 | Magnesium chelatase, subunit ChII (primary bucket kegg:ppu00860)
- cobN: PP_3507 | Q88H58 | Cobaltochelatase subunit CobN (EC 6.6.1.2) (EC 6.6.1.2; primary bucket kegg:ppu00860)
- PP_3763: PP_3763 | Q88GG1 | CobF protein (primary bucket kegg:ppu00860)
- cysG: PP_3999 | Q88FT3 | Siroheme synthase [Includes: Uroporphyrinogen-III C-methyltransferase (Urogen III methylase) (EC 2.1.1.107) (SUMT) (Uroporphyrinogen III methylase) (UROM); Precorrin-2 dehydrogenase (EC 1.3.1.76); Sirohydrochlorin ferrochelatase (EC 4.99.1.4)] (EC 1.3.1.76; 2.1.1.107; 4.99.1.4; primary bucket kegg:ppu00860)
- hemN: PP_4264 | Q88F35 | Coproporphyrinogen-III oxidase (EC 1.3.98.3) (EC 1.3.98.3; primary bucket kegg:ppu00860)
- hemL: PP_4784 | Q88DP0 | Glutamate-1-semialdehyde 2,1-aminomutase (GSA) (EC 5.4.3.8) (Glutamate-1-semialdehyde aminotransferase) (GSA-AT) (EC 5.4.3.8; primary bucket kegg:ppu00860)
- cobJ: PP_4826 | Q88DJ9 | Precorrin-3B C17-methyltransferase (primary bucket kegg:ppu00860)
- cobI: PP_4827 | Q88DJ8 | Precorrin-2 C(20)-methyltransferase (EC 2.1.1.130) (EC 2.1.1.130; primary bucket kegg:ppu00860)
- cobH: PP_4828 | Q88DJ7 | Precorrin-8X methylmutase (EC 5.4.99.61) (EC 5.4.99.61; primary bucket kegg:ppu00860)
- cobG: PP_4829 | Q88DJ6 | Precorrin-3B synthase (EC 1.14.13.83) (EC 1.14.13.83; primary bucket kegg:ppu00860)
- cobL: PP_4830 | Q88DJ5 | Precorrin-6Y C(5,15)-methyltransferase (EC 2.1.1.132) (EC 2.1.1.132; primary bucket kegg:ppu00860)
- cbiD: PP_4831 | Q88DJ4 | Cobalt-precorrin-5B C(1)-methyltransferase (EC 2.1.1.195) (Cobalt-precorrin-6A synthase) (EC 2.1.1.195; primary bucket kegg:ppu00860)
- cobK: PP_4832 | Q88DJ3 | Precorrin-6x reductase (primary bucket kegg:ppu00860)
- PP_4856: PP_4856 | Q88DG9 | ferroxidase (EC 1.16.3.1) (EC 1.16.3.1; primary bucket kegg:ppu00860)
- hemE: PP_5074 | Q88CV6 | Uroporphyrinogen decarboxylase (UPD) (URO-D) (EC 4.1.1.37) (EC 4.1.1.37; primary bucket kegg:ppu00860)

## Generic Module Context

### Working Scope

A reusable cross-taxon model of protoporphyrin-dependent heme B biosynthesis. C5 glutamyl-tRNA and C4/Shemin reactions are alternative routes to 5-aminolevulinate (ALA). A shared tetrapyrrole trunk then feeds independently selected oxygen-dependent or oxygen-independent coproporphyrinogen oxidases and HemJ-, HemG-, or HemY/PPOX-family protoporphyrinogen oxidases. All realizations converge at protoporphyrin IX, which a species-neutral ferrochelatase reaction converts to heme B.

### Provisional Biological Outline

- Protoporphyrin-dependent heme B biosynthesis
  - 1. formation of protoporphyrin IX
  - Formation of protoporphyrin IX
    - 1. route-specific formation of 5-aminolevulinate
    - Alternative formation of 5-aminolevulinate
      - Alternative versions by precursor route: 5-Aminolevulinate entry chemistry
        - C5 glutamyl-tRNA formation of ALA
          - Glutamyl-tRNA reductase (molecular player: glutamyl-tRNA reductase family; activity or role: glutamyl-tRNA reductase (NADP+) activity)
          - Glutamate-1-semialdehyde 2,1-aminomutase (molecular player: glutamate-1-semialdehyde 2,1-aminomutase family; activity or role: glutamate-1-semialdehyde 2,1-aminomutase activity)
        - C4/Shemin ALA formation
          - 5-Aminolevulinate synthase (molecular player: 5-aminolevulinate synthase family; activity or role: 5-aminolevulinate synthase activity)
    - 2. shared ALA-to-coproporphyrinogen III trunk
    - Shared tetrapyrrole trunk
      - 1. condensation of ALA to porphobilinogen
      - ALA condensation
        - Porphobilinogen synthase (molecular player: delta-aminolevulinate dehydratase family; activity or role: porphobilinogen synthase activity)
      - 2. polymerization to hydroxymethylbilane
      - Hydroxymethylbilane formation
        - Hydroxymethylbilane synthase (molecular player: porphobilinogen deaminase family; activity or role: hydroxymethylbilane synthase activity)
      - 3. cyclization to uroporphyrinogen III
      - Uroporphyrinogen III formation
        - Uroporphyrinogen-III synthase (molecular player: uroporphyrinogen-III synthase family; activity or role: uroporphyrinogen-III synthase activity)
      - 4. decarboxylation to coproporphyrinogen III
      - Coproporphyrinogen III formation
        - Uroporphyrinogen decarboxylase (molecular player: uroporphyrinogen decarboxylase lineage; activity or role: uroporphyrinogen decarboxylase activity)
    - 3. formation of protoporphyrinogen IX
    - Coproporphyrinogen III oxidation
      - Alternative versions by oxygen dependence: Coproporphyrinogen oxidation chemistry
        - Oxygen-dependent HemF route
          - Oxygen-dependent coproporphyrinogen oxidase (molecular player: oxygen-dependent coproporphyrinogen oxidase lineage; activity or role: coproporphyrinogen oxidase activity)
        - Oxygen-independent HemN route
          - Oxygen-independent coproporphyrinogen dehydrogenase (molecular player: oxygen-independent coproporphyrinogen oxidase lineage; activity or role: coproporphyrinogen dehydrogenase activity)
    - 4. formation of protoporphyrin IX
    - Protoporphyrinogen IX oxidation
      - Alternative versions by enzyme family and terminal electron acceptor: Protoporphyrinogen oxidase chemistry
        - HemJ acceptor-dependent route
          - HemJ-family protoporphyrinogen oxidase (molecular player: HemJ protoporphyrinogen IX oxidase lineage; activity or role: protoporphyrinogen oxidase activity)
        - HemG quinone-acceptor route
          - HemG quinone-acceptor protoporphyrinogen dehydrogenase (molecular player: HemG quinone-acceptor protoporphyrinogen dehydrogenase lineage; activity or role: protoporphyrinogen oxidase activity, quinone as acceptor)
        - HemY oxygen-acceptor route
          - HemY/PgoX oxygen-dependent protoporphyrinogen oxidase (molecular player: HemY/PPOX protoporphyrinogen oxidase lineage; activity or role: protoporphyrinogen oxidase activity, oxygen as acceptor)
  - 2. insertion of ferrous iron to form heme B
  - Species-neutral ferrochelation of protoporphyrin IX
    - Protoporphyrin ferrochelatase (molecular player: ferrochelatase family; activity or role: protoporphyrin ferrochelatase activity)

### Known Relationships Among Steps

- Formation of protoporphyrin IX feeds into Species-neutral ferrochelation of protoporphyrin IX: Every valid combination of entry and late-step variants supplies protoporphyrin IX to ferrochelatase.
- Alternative formation of 5-aminolevulinate feeds into Shared tetrapyrrole trunk: Either entry route supplies 5-aminolevulinate to the shared trunk.
- Shared tetrapyrrole trunk feeds into Coproporphyrinogen III oxidation: Coproporphyrinogen III feeds an applicable oxygen-dependent or oxygen-independent oxidase.
- Coproporphyrinogen III oxidation feeds into Protoporphyrinogen IX oxidation: Protoporphyrinogen IX feeds an applicable HemJ-, HemG-, or HemY/PPOX-family oxidase.
- Glutamyl-tRNA reductase feeds into Glutamate-1-semialdehyde 2,1-aminomutase: HemA supplies glutamate-1-semialdehyde to HemL.
- ALA condensation feeds into Hydroxymethylbilane formation: Porphobilinogen feeds HemC.
- Hydroxymethylbilane formation feeds into Uroporphyrinogen III formation: Hydroxymethylbilane feeds HemD.
- Uroporphyrinogen III formation feeds into Coproporphyrinogen III formation: Uroporphyrinogen III feeds HemE.

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

# Heme B Biosynthesis in *Pseudomonas putida* KT2440 — Module/Pathway/Taxon Review

**Review topic:** Heme B biosynthesis through alternative entry and oxidation routes in *Pseudomonas putida* KT2440
**Target taxon:** PSEPK — *Pseudomonas putida* KT2440 (NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00860` "Porphyrin metabolism" (resolved local bucket, 45–46 primary candidate genes; module area *cofactors_vitamins_redox*)

---

## 1. Executive Summary

Heme B biosynthesis is **fully satisfiable** in *Pseudomonas putida* KT2440. Every catalytic step from 5-aminolevulinate (ALA) formation through ferrochelation of protoporphyrin IX to heme B is encoded in the proteome by a clearly identifiable candidate gene. The organism realizes one specific combination of the alternative routes that the generic module allows: it forms ALA exclusively via the **C5 / glutamyl-tRNA route** (`hemA`, `hemL`, with `gltX` supplying charged Glu-tRNA); it carries **both** the oxygen-dependent (`hemF`) and oxygen-independent (`hemN`) coproporphyrinogen III oxidases, giving aerobic/anaerobic flexibility; it uses a single **HemJ-type protoporphyrinogen IX oxidase** (`PP_0431`); and it converts protoporphyrin IX to heme B with a single-copy **ferrochelatase** (`hemH`). The Shemin/C4 ALA synthase and the HemG and HemY protoporphyrinogen-oxidase families are **not expected** in this organism, confirmed by a proteome-wide Pfam scan (HemJ PF03653 = 1 hit; true HemG PF01903 = 0; no HemY-fold protein is a protoporphyrinogen oxidase).

The single most important curation finding is one of **scope**, not gaps. The KEGG `ppu00860` "Porphyrin metabolism" bucket is an umbrella map: only ~13 of the 46 candidate genes belong to the heme B trunk. The remaining ~33 candidates route to neighboring tetrapyrrole branches that should be kept in separate modules — cobalamin (B₁₂) biosynthesis (the large `cob*`/`cbiD`/`pduO` block), siroheme synthesis (`cysG`, `cobA`/`PP_2090`, `PP_0188`), heme catabolism and iron storage/acquisition (`hemO`, `PP_2582`, `PP_1358`, bacterioferritins, ferroxidase), and downstream heme modification for terminal oxidase cofactors (`cyoE1`/`cyoE2` heme O synthases and `PP_0109`, which is a mislabeled CtaA/heme A synthase, **not** a "Cytochrome B").

The two curation actions that require follow-up at the gene level are: (i) two porphobilinogen-synthase (ALAD) paralogs, `hemB` (PP_2913) and `hemBB` (PP_3322), which are annotated identically and need metal-cofactor/subtype disambiguation; and (ii) the generically annotated `PP_0431`, which should be curated explicitly to the HemJ route. All conclusions rest on UniProt family/domain evidence for the target strain plus well-established biochemical literature for the pathway; direct genetic/enzymatic experiments in KT2440 itself remain the principal evidence gap.

---

## 2. Target-Organism Pathway Definition

### 2.1 What process is included

The module covers **protoporphyrin-dependent heme B biosynthesis**: the linear conversion of the universal tetrapyrrole precursor 5-aminolevulinate through the shared "trunk" (porphobilinogen → hydroxymethylbilane → uroporphyrinogen III → coproporphyrinogen III), then the two late oxidation steps (coproporphyrinogen III → protoporphyrinogen IX → protoporphyrin IX), and finally ferrous-iron insertion (ferrochelation) to yield heme B (protoheme IX). Upstream, the module includes the *route-specific* formation of ALA, for which two mutually exclusive entries exist across taxa: the C5 (glutamyl-tRNA) route and the C4 (Shemin, ALA synthase) route.

### 2.2 Neighboring pathways to keep separate

For curation, the following processes that co-occur in the KEGG `ppu00860` umbrella map should be **excluded** from the heme B module:

- **Cobalamin (vitamin B₁₂) biosynthesis** — the aerobic corrin ring pathway (`cobA`/SUMT, `cobI`, `cobG`, `cobJ`, `cobM`, `cobF`, `cobK`, `cobL`, `cbiD`, `cobH`, `cobB`, `cobN`, `cobO`, `cobQ`, `cobC`, `cobD`, `cobP`, `cobT`, `cobS`, `PP_1680`, `PP_3409`, `PP_3506`, `pduO`). These branch from uroporphyrinogen III via precorrin-2, sharing only the very earliest trunk with heme.
- **Siroheme biosynthesis** — `cysG` (multifunctional siroheme synthase), and the SUMT activities of `cobA`/`PP_2090` and `PP_0188`. Siroheme also branches at uroporphyrinogen III.
- **Heme catabolism / iron acquisition and storage** — heme oxygenases (`hemO`/PP_1005, `PP_2582`), heme iron utilization protein (`PP_1358`), bacterioferritins (`bfr-I`/PP_0482, `bfr-II`/PP_1082), and ferroxidase (`PP_4856`). These consume heme or store iron and are downstream/orthogonal to biosynthesis.
- **Heme O / heme A modification for terminal oxidases** — protoheme IX farnesyltransferases / heme O synthases `cyoE1` (PP_0110) and `cyoE2` (PP_0816), and the heme A synthase `PP_0109` (CtaA/COX15 family). These act *on* finished heme B to make oxidase cofactors and belong to a "heme modification for respiration" module, not heme B biosynthesis.

### 2.3 Alternate names / database definitions

The pathway is variously called "heme biosynthesis," "protoheme IX biosynthesis," "tetrapyrrole biosynthesis (heme branch)," and MetaCyc "heme *b* biosynthesis I (aerobic)/II (anaerobic)". KEGG collapses all tetrapyrrole end-products (heme, siroheme, cobalamin, and their catabolism) into the single map `00860` "Porphyrin metabolism" (historically "Porphyrin and chlorophyll metabolism"), which is why the local bucket is far broader than heme B proper.

---

## 3. Expected Step Model and Satisfiability

The table below maps each generic module step to the KT2440 gene(s) and a satisfiability call.

| Module step | Enzyme (EC) | KT2440 gene (locus \| UniProt) | Call |
|---|---|---|---|
| **ALA entry — C5** | Glutamyl-tRNA synthetase (6.1.1.17) | `gltX` (PP_1977 \| Q88LF6) | covered |
| | Glutamyl-tRNA reductase (1.2.1.70) | `hemA` (PP_0732 \| Q88PW6) | covered |
| | Glutamate-1-semialdehyde 2,1-aminomutase (5.4.3.8) | `hemL` (PP_4784 \| Q88DP0) | covered |
| **ALA entry — C4/Shemin** | 5-aminolevulinate synthase (2.3.1.37) | *absent* | not_expected_in_target_taxon |
| ALA condensation | Porphobilinogen synthase / ALAD (4.2.1.24) | `hemB` (PP_2913 \| Q88IT6) **and** `hemBB` (PP_3322 \| Q88HN1) | covered (paralog ambiguity) |
| Hydroxymethylbilane formation | Porphobilinogen deaminase / HMBS (2.5.1.61) | `hemC` (PP_0186 \| Q88RE5) | covered |
| Uroporphyrinogen III formation | Uroporphyrinogen-III synthase (4.2.1.75) | `hemD` (PP_0187 \| Q88RE4) | covered |
| Coproporphyrinogen III formation | Uroporphyrinogen decarboxylase (4.1.1.37) | `hemE` (PP_5074 \| Q88CV6) | covered |
| Coprogen oxidation — O₂-dependent | Coproporphyrinogen oxidase HemF (1.3.3.3) | `hemF` (PP_0073 \| Q88RQ6) | covered |
| Coprogen oxidation — O₂-independent | Coproporphyrinogen dehydrogenase HemN (1.3.98.3) | `hemN` (PP_4264 \| Q88F35) | covered |
| Protoporphyrinogen IX oxidation — HemJ | HemJ-family Protox | `PP_0431` (Q88QQ7) | covered (HemJ route) |
| Protoporphyrinogen IX oxidation — HemG | Quinone-acceptor Protox | *absent* | not_expected_in_target_taxon |
| Protoporphyrinogen IX oxidation — HemY | O₂-acceptor PPOX | *absent* | not_expected_in_target_taxon |
| Ferrochelation | Ferrochelatase HemH (4.98.1.1) | `hemH` (PP_0744 \| Q88PV4) | covered |

**Every trunk step is covered.** The only step-level uncertainties are the *choice of variant* at the ALA-entry, coprogen-oxidation, and protoporphyrinogen-oxidation nodes — which this review resolves — plus the ALAD paralog ambiguity.

---

## 4. Candidate Genes and Evidence

### 4.1 ALA entry: the C5 (glutamyl-tRNA) route (Finding F002)

*P. putida* KT2440 forms ALA via the **C5 route**, not the C4/Shemin route. The candidate list encodes glutamyl-tRNA reductase `hemA` (PP_0732, Q88PW6, EC 1.2.1.70), glutamate-1-semialdehyde 2,1-aminomutase `hemL` (PP_4784, Q88DP0, EC 5.4.3.8), and glutamate–tRNA ligase `gltX` (PP_1977, Q88LF6, EC 6.1.1.17). No 5-aminolevulinate synthase (ALAS, EC 2.3.1.37) gene is present anywhere in the bucket. This is the canonical bacterial arrangement: in the C5 pathway Glu-tRNA "is transformed to delta-aminolevulinic acid, the universal precursor of tetrapyrroles (e.g., heme and chlorophyll) by the action of Glu-tRNA reductase (GluTR) and glutamate semialdehyde aminotransferase" ([PMID: 17360620](https://pubmed.ncbi.nlm.nih.gov/17360620/)). Arabidopsis and *E. coli* work confirms ALA is derived from glutamate via the two-step C5 pathway (HemA/GluTR + GSA1/GSAM) ([PMID: 7908550](https://pubmed.ncbi.nlm.nih.gov/7908550/)). The C4/ALAS route is largely restricted to α-Proteobacteria, animals, and fungi, so its absence in this γ-proteobacterium is expected, not a gap.

Curation caveat: `gltX` is a **shared/dual-function** gene — the charged Glu-tRNA it produces feeds both protein synthesis and tetrapyrrole biosynthesis ([PMID: 17360620](https://pubmed.ncbi.nlm.nih.gov/17360620/)). It should be flagged as contributing to, but not exclusive to, the heme module.

### 4.2 Shared tetrapyrrole trunk (Findings F003, F004)

All shared-trunk enzymes are present as single, family-verified copies (except ALAD, below):

- `hemC` (Q88RE5) — porphobilinogen deaminase / HMBS family, dipyrromethane cofactor.
- `hemD` (Q88RE4) — uroporphyrinogen-III synthase family.
- `hemE` (Q88CV6) — uroporphyrinogen decarboxylase (URO-D) family.

The *B. subtilis* `hemAXCDBL` operon studies confirm these genes constitute the conserved glutamate-to-uroporphyrinogen-III core and that `hemA`, `hemB`, `hemC`, `hemD` have all been shown to be essential for heme synthesis ([PMID: 1672867](https://pubmed.ncbi.nlm.nih.gov/1672867/); [PMID: 2110138](https://pubmed.ncbi.nlm.nih.gov/2110138/)), supporting the expectation that their KT2440 orthologs are functional and required.

### 4.3 Two ALAD (porphobilinogen synthase) paralogs (Finding F005)

KT2440 carries **two** ALAD paralogs: `hemB` (PP_2913, Q88IT6, 324 aa) and `hemBB` (PP_3322, Q88HN1, 333 aa). Both belong to the ALAD family (Pfam PF00490, EC 4.2.1.24) and are annotated identically as delta-aminolevulinic acid dehydratase; UniProt lists no explicit metal cofactor for either. Bacterial ALADs split into **Zn²⁺-dependent** (cysteine-rich active-site motif) and **Mg²⁺-dependent** (aspartate motif) subtypes with distinct physiology. Most *Pseudomonas* genomes encode a single `hemB`, so this duplication is notable and biologically informative — the two paralogs may differ in metal use, expression condition, or physiological role. This is the clearest gene-level curation ambiguity in the module.

### 4.4 Coproporphyrinogen III oxidation: both HemF and HemN (Findings F003, F004)

KT2440 encodes **both** coproporphyrinogen III oxidases: the oxygen-dependent `hemF` (PP_0073, Q88RQ6, aerobic CPO, EC 1.3.3.3) and the oxygen-independent radical-SAM `hemN` (PP_4264, Q88F35, EC 1.3.98.3). Possessing both isozymes is the expected arrangement for a metabolically versatile soil pseudomonad, enabling heme synthesis across aerobic and microaerobic/anaerobic conditions. Both nodes of the "coproporphyrinogen oxidation chemistry" alternative are therefore realized.

### 4.5 Protoporphyrinogen IX oxidation: HemJ only (Findings F001, F004)

The penultimate step is catalyzed by a **HemJ-type** protoporphyrinogen IX oxidase, `PP_0431` (Q88QQ7). UniProt annotates it generically as "Protoporphyrinogen IX oxidase (EC 1.3.99.-)", but it carries Pfam **PF03653** and InterPro "HemJ-like" and is placed by UniProt in the HemJ family. A proteome-wide scan of UP000000556 found **PF03653 (HemJ) = 1 hit** (PP_0431), **PF01903 (true HemG) = 0 hits**, and while PF01593 (HemY/amine-oxidase fold) returned 5 hits, all are renalase/tryptophan-2-monooxygenase/amine oxidases — **none a protoporphyrinogen oxidase**. KT2440 therefore has no HemG or HemY redundancy at this step.

This is mechanistically notable. "Three nonhomologous isofunctional enzymes, HemG, HemJ, and HemY, for Protox have been identified" and most organisms possess only one type; "HemG is mostly limited to γ-Proteobacteria whereas HemJ may have originated within α-Proteobacteria and transferred to other Proteobacteria" ([PMID: 25108393](https://pubmed.ncbi.nlm.nih.gov/25108393/)). *Pseudomonas* is a γ-proteobacterium — the "expected" home of HemG — yet KT2440 uses HemJ, a clear example of the intricate, mosaic evolutionary distribution of these enzymes. Heterologous complementation work confirms that HemJ, HemY, and HemG homologs are genuinely interchangeable in function despite being unrelated in sequence ([PMID: 36357749](https://pubmed.ncbi.nlm.nih.gov/36357749/)), which validates assigning PP_0431 to the Protox step on family evidence.

### 4.6 Ferrochelation (Finding F004)

`hemH` (PP_0744, Q88PV4) is a **single-copy** ferrochelatase (family-verified, EC 4.98.1.1) that inserts Fe²⁺ into protoporphyrin IX to form heme B. This is the species-neutral convergence point of the module and is unambiguously covered.

### 4.7 Genes that belong to neighboring modules (over-scoped in the bucket)

| Candidate(s) | True branch | Recommended module |
|---|---|---|
| `cobA`/PP_2090, `cobI`, `cobG`, `cobJ`, `cobM`, `PP_3763`(CobF), `cobK`, `cobL`, `cbiD`, `cobH`, `cobB`, `cobN`, `PP_3506`, `cobO`, `cobQ`, `cobC`, `cobD`, `cobP`, `cobT`, `cobS`, `PP_1680`, `PP_3409`(CobE), `pduO` | Cobalamin (B₁₂) biosynthesis | separate cobalamin module |
| `cysG`, `PP_0188`, SUMT activity of `cobA` | Siroheme biosynthesis | separate siroheme module |
| `hemO`(PP_1005), `PP_2582`, `PP_1358` | Heme catabolism / iron utilization | heme-degradation module |
| `bfr-I`, `bfr-II`, `PP_4856` | Iron storage / ferroxidase | iron-homeostasis module |
| `cyoE1`(PP_0110), `cyoE2`(PP_0816) | Heme O synthase (EC 2.5.1.141) | heme-O/A modification module |
| `PP_0109` | Heme A synthase (CtaA/COX15 family) — **mislabeled** "Cytochrome B" | heme-O/A modification module |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

1. **`PP_0109` is mis-annotated.** It is labeled "Cytochrome B" in the metadata, but its InterPro/family signature (HemeA_synthase_prok; CtaA/COX15) identifies it as a **heme A synthase** that converts heme O to heme A. It is not a cytochrome b apoprotein and does not belong to the heme B trunk. **Correct this annotation and move it to the heme-modification module.**

2. **`PP_0431` carries an over-broad EC and generic name.** "Protoporphyrinogen IX oxidase (EC 1.3.99.-)" understates the specific, curatable assignment: it is a **HemJ-family** Protox. Promote to explicit HemJ annotation.

3. **ALAD paralog ambiguity (`hemB` vs `hemBB`).** Two identically annotated PF00490 proteins with no listed metal cofactor. Their Zn²⁺- vs Mg²⁺-dependence, conditional expression, and which (if either) is the housekeeping enzyme are unresolved.

4. **Broad/duplicated EC and GO mappings inflating the bucket.** Several `cob*` genes and `cysG` carry SUMT/uroporphyrinogen-III C-methyltransferase (EC 2.1.1.107) activity that overlaps the earliest trunk, which can cause over-propagation of "porphyrin metabolism" into heme B satisfiability checks. The bacterioferritins and `PP_4856` carry EC 1.16.3.1 (ferroxidase) unrelated to biosynthesis.

5. **`gltX` shared function.** Contributes charged Glu-tRNA to both translation and tetrapyrrole synthesis; should not be treated as a heme-exclusive gene.

6. **No genuine heme B trunk gaps were found.** The module is complete; there is no missing-step gap requiring a paralog search or a "not found" call for any trunk reaction.

---

## 6. Module and GO-Curation Recommendations

**Step-level calls for the heme B module in PSEPK:**

| Module step | Call |
|---|---|
| C5 ALA entry (`hemA`, `hemL`, `gltX`) | **covered** |
| C4/Shemin ALA entry (ALAS) | **not_expected_in_target_taxon** |
| ALA condensation (ALAD) | **covered** — flag paralog ambiguity (`hemB`/`hemBB`) → candidate_uncertain at gene level |
| HMBS (`hemC`), UROS (`hemD`), URO-D (`hemE`) | **covered** |
| Coprogen oxidation, HemF | **covered** |
| Coprogen oxidation, HemN | **covered** |
| Protox, HemJ (`PP_0431`) | **covered** |
| Protox, HemG | **not_expected_in_target_taxon** |
| Protox, HemY | **not_expected_in_target_taxon** |
| Ferrochelation (`hemH`) | **covered** |

**Module boundary:** The generic module boundaries are **correct for heme B**, but the *local KEGG bucket* `ppu00860` is too broad — it is an umbrella "Porphyrin metabolism" map. Recommend **splitting** the bucket so that only the ~13 trunk genes populate the heme B module, and creating (or linking to existing) separate modules for cobalamin, siroheme, heme catabolism, iron storage, and heme-O/A modification. Mark the bucket-level relationship as **module_needs_revision** with respect to scope.

**GO-term / annotation requests:**
- Re-annotate `PP_0109` from "Cytochrome B" to **heme A synthase** (CtaA/COX15).
- Add explicit **HemJ / protoporphyrinogen oxidase (GO:0004729)** assignment to `PP_0431`.
- No new GO term requests appear necessary; existing terms cover all realized steps.

---

## 7. Genes to Promote to Full Review (`fetch-gene`)

1. **`hemB` (PP_2913, Q88IT6)** and **`hemBB` (PP_3322, Q88HN1)** — disambiguate the two ALAD paralogs (metal-cofactor subtype, physiological role, which is housekeeping). Highest priority.
2. **`PP_0431` (Q88QQ7)** — confirm HemJ assignment and replace the generic EC 1.3.99.- annotation.
3. **`PP_0109` (Q88RM0)** — correct the "Cytochrome B" mislabel to heme A synthase and remove from the heme B trunk.
4. **`gltX` (PP_1977)** — annotate shared/dual role (translation + tetrapyrrole entry).
5. (Optional) **`hemN` (PP_4264)** vs **`hemF` (PP_0073)** — confirm both are functional and note the aerobic/anaerobic redundancy for module logic.

---

## 8. Evidence Base and Limitations

### 8.1 Key references

| PMID | Relevance |
|---|---|
| [25108393](https://pubmed.ncbi.nlm.nih.gov/25108393/) | Establishes HemG/HemJ/HemY as three nonhomologous isofunctional Protox enzymes; explains mosaic distribution (HemG mostly γ-Proteobacteria; HemJ from α-Proteobacteria) — underpins the HemJ assignment of PP_0431 (F001). |
| [36357749](https://pubmed.ncbi.nlm.nih.gov/36357749/) | Heterologous complementation verifies functional interchangeability of HemJ/HemY/HemG — validates assigning Protox by family. |
| [17360620](https://pubmed.ncbi.nlm.nih.gov/17360620/) | Defines C5-route enzymes (GluRS/`gltX`, GluTR/`hemA`, GSAM/`hemL`) and the dual role of Glu-tRNA — underpins F002. |
| [7908550](https://pubmed.ncbi.nlm.nih.gov/7908550/) | ALA as universal tetrapyrrole precursor via the two-step C5 pathway (HemA + GSA1) — supports C5 assignment. |
| [1672867](https://pubmed.ncbi.nlm.nih.gov/1672867/) | *B. subtilis* `hemAXCDBL` cluster; `hemA/B/C/D` essential for heme — supports trunk-gene functionality by homology. |
| [2110138](https://pubmed.ncbi.nlm.nih.gov/2110138/) | Characterization of `hemA` region; C5 GluTR conserved — supports trunk model. |
| [29164655](https://pubmed.ncbi.nlm.nih.gov/29164655/) | *Amycolatopsis* case with two divergent ALA pathways — cautionary context that some genomes carry dual ALA routes (not the case here). |

### 8.2 Limitations and species-transfer caveats

- **Evidence type is primarily homology/family-based.** All KT2440 assignments rest on UniProt Pfam/InterPro family membership and EC annotation for strain KT2440 proteins, combined with biochemical literature from *other* organisms (*E. coli*, *B. subtilis*, Arabidopsis, cyanobacteria). There are **no direct KT2440 gene-knockout or enzyme-assay data** cited here confirming in-vivo function. Transfer of the biochemical mechanism to KT2440 is **strong** for the highly conserved trunk enzymes and **strong** for the HemJ family assignment (the Pfam signature is diagnostic), but the *physiological* details (e.g., ALAD paralog roles, HemF/HemN condition-specificity) are **uncertain** without strain-specific experiments.
- The proteome scan is a snapshot of UniProt annotations; a novel or divergent Protox not captured by PF03653/PF01903/PF01593 would be missed, though this is unlikely given the complete trunk.
- The ALAD paralog metal-subtype inference is based on general bacterial ALAD biology, not on KT2440 sequence-motif analysis performed here — it should be verified at the sequence level in the `fetch-gene` step.

### 8.3 Proposed follow-up experiments / actions

1. **Sequence-motif analysis of `hemB` vs `hemBB`** to classify Zn²⁺- vs Mg²⁺-dependent ALAD subtypes (active-site Cys-rich vs Asp motif); ideally single/double knockouts to test which supports growth.
2. **Confirm PP_0431 HemJ function** by heterologous complementation of an *E. coli* Δ*hemG* strain (as in [PMID: 36357749](https://pubmed.ncbi.nlm.nih.gov/36357749/)).
3. **Correct annotations** for `PP_0109` (heme A synthase) and `PP_0431` (HemJ) in the reference proteome and downstream modules.
4. **Split the `ppu00860` bucket** into heme B, cobalamin, siroheme, heme-catabolism, iron-storage, and heme-modification modules for satisfiability tracking.
5. **Test HemF/HemN condition-dependence** (aerobic vs anaerobic growth of single mutants) to confirm the redundancy inferred here.

---

## 9. Mechanistic Model (Realized Route in KT2440)

```
        Glu  --gltX-->  Glu-tRNA
                            |
                         hemA (GluTR)
                            v
                 glutamate-1-semialdehyde
                            |
                         hemL (GSAM)
                            v
   [C5 route]        5-aminolevulinate (ALA)        [C4/ALAS: ABSENT]
                            |
                    hemB / hemBB (ALAD)   <-- two paralogs, disambiguate
                            v
                     porphobilinogen
                            |
                         hemC (HMBS)
                            v
                    hydroxymethylbilane
                            |
                         hemD (UROS)
                            v
                  uroporphyrinogen III  --> [siroheme: cysG; cobalamin: cobA...]
                            |
                         hemE (URO-D)
                            v
                 coproporphyrinogen III
                            |
              hemF (O2-dep)  +  hemN (O2-indep)   <-- both present
                            v
                  protoporphyrinogen IX
                            |
                    PP_0431 (HemJ)    [HemG: ABSENT; HemY: ABSENT]
                            v
                    protoporphyrin IX
                            |
                         hemH (ferrochelatase, single copy)
                            v
                         HEME B
                            |
              [cyoE1/cyoE2 -> heme O; PP_0109 -> heme A]  (separate module)
```

**Bottom line:** The heme B module is satisfiable and complete in *P. putida* KT2440 via C5 entry → shared trunk → HemF/HemN → HemJ → HemH. The work required is curatorial (bucket scoping, three annotation fixes, one paralog disambiguation), not a search for missing biosynthetic capability.


## Artifacts

- [OpenScientist final report](PSEPK__heme_biosynthesis__ppu00860-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__heme_biosynthesis__ppu00860-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17360620
2. PMID:7908550
3. PMID:1672867
4. PMID:2110138
5. PMID:25108393
6. PMID:36357749