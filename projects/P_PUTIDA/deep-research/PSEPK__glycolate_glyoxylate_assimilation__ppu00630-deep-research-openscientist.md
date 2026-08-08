---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T17:15:56.132527'
end_time: '2026-07-15T17:30:11.393192'
duration_seconds: 855.26
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial glycolate and glyoxylate assimilation
  module_summary: A reusable bacterial central-carbon module for conversion of glycolate
    and glyoxylate into metabolites that can re-enter core carbon metabolism. The
    module covers phosphoglycolate dephosphorylation to glycolate, multicomponent
    glycolate oxidation to glyoxylate, and the glyoxylate carboligase/tartronate semialdehyde
    branch that converts glyoxylate-derived carbon toward glycerate. Pseudomonas putida
    KT2440 provides local exemplars for the phosphoglycolate phosphatase, GlcDEF glycolate
    dehydrogenase, Gcl, Hyi, and GlxR roles, but the module boundary is the conserved
    bacterial pathway segment rather than a PSEPK-specific locus definition.
  module_outline: "- Bacterial glycolate and glyoxylate assimilation\n  - 1. phosphoglycolate\
    \ dephosphorylation to glycolate\n  - 2-phosphoglycolate to glycolate\n    - Phosphoglycolate\
    \ phosphatase (molecular player: bacterial phosphoglycolate phosphatase family;\
    \ activity or role: phosphoglycolate phosphatase activity)\n  - 2. glycolate oxidation\
    \ to glyoxylate\n  - GlcDEF glycolate dehydrogenase complex\n    - GlcD FAD-linked\
    \ glycolate dehydrogenase subunit (molecular player: GlcD glycolate oxidase/dehydrogenase\
    \ family; activity or role: glycolate dehydrogenase activity)\n    - GlcE FAD-binding\
    \ glycolate dehydrogenase subunit (molecular player: GlcE glycolate oxidase/dehydrogenase\
    \ family; activity or role: contributes to glycolate dehydrogenase activity)\n\
    \    - GlcF iron-sulfur glycolate dehydrogenase subunit (molecular player: GlcF\
    \ glycolate oxidase iron-sulfur subunit family; activity or role: contributes\
    \ to glycolate dehydrogenase activity)\n  - 3. glyoxylate condensation to tartronate\
    \ semialdehyde\n  - Glyoxylate to tartronate semialdehyde\n    - Glyoxylate carboligase\
    \ (molecular player: glyoxylate carboligase family; activity or role: tartronate-semialdehyde\
    \ synthase activity)\n  - 4. hydroxypyruvate and tartronate-semialdehyde interconversion\n\
    \  - Hydroxypyruvate isomerization\n    - Hydroxypyruvate isomerase (molecular\
    \ player: hydroxypyruvate isomerase family; activity or role: hydroxypyruvate\
    \ isomerase activity)\n  - 5. tartronate semialdehyde reduction to glycerate\n\
    \  - Tartronate semialdehyde to glycerate\n    - Tartronate semialdehyde reductase\
    \ (molecular player: tartronate semialdehyde reductase family; activity or role:\
    \ 2-hydroxy-3-oxopropionate reductase activity)"
  module_connections: '- 2-phosphoglycolate to glycolate feeds into GlcDEF glycolate
    dehydrogenase complex: Phosphoglycolate phosphatase produces glycolate, the substrate
    oxidized by the GlcDEF glycolate dehydrogenase complex.

    - GlcDEF glycolate dehydrogenase complex feeds into Glyoxylate to tartronate semialdehyde:
    GlcDEF oxidizes glycolate to glyoxylate, supplying the glyoxylate used by glyoxylate
    carboligase.

    - Glyoxylate to tartronate semialdehyde feeds into Tartronate semialdehyde to
    glycerate: Glyoxylate carboligase produces tartronate semialdehyde (2-hydroxy-3-oxopropanoate),
    the substrate reduced by GlxR.

    - Hydroxypyruvate isomerization feeds into Tartronate semialdehyde to glycerate:
    Hyi can provide the same tartronate-semialdehyde intermediate from hydroxypyruvate,
    connecting hydroxypyruvate metabolism to the GlxR reduction step.'
  pathway_query: ppu00630
  pathway_id: ppu00630
  pathway_name: Glyoxylate and dicarboxylate metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00630 with 9 primary genes; module
    area: central_carbon.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '62'
  candidate_genes: '- PP_0094: PP_0094 | Q88RN5 | 5''-nucleotidase (EC 3.1.3.5) (EC
    3.1.3.5; primary bucket kegg:ppu00630)

    - katE: PP_0115 | Q88RL4 | Catalase (EC 1.11.1.6) (EC 1.11.1.6; primary bucket
    kegg:ppu04146)

    - glyA1: PP_0322 | Q88R12 | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine
    methylase 1) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)

    - purU-I: PP_0327 | Q88R07 | Formyltetrahydrofolate deformylase (EC 3.5.1.10)
    (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)

    - glcB: PP_0356 | Q88QX8 | Malate synthase G (EC 2.3.3.9) (EC 2.3.3.9; primary
    bucket kegg:ppu00620)

    - PP_0416: PP_0416 | Q88QS2 | Phosphoglycolate phosphatase (PGP) (PGPase) (EC
    3.1.3.18) (EC 3.1.3.18; primary bucket kegg:ppu00630)

    - katA: PP_0481 | Q88QK9 | Catalase (EC 1.11.1.6) (EC 1.11.1.6; primary bucket
    kegg:ppu04146)

    - fdoG: PP_0489 | A0A140FVZ1 | Formate dehydrogenase-O major subunit (EC 1.2.1.2)
    (EC 1.2.1.2; primary bucket kegg:ppu00680)

    - fdoH: PP_0490 | Q88QK1 | Formate dehydrogenase iron-sulfur subunit (primary
    bucket kegg:ppu00680)

    - fdoI: PP_0491 | Q88QK0 | Formate dehydrogenase-O, gamma subunit (EC 1.2.1.2)
    (EC 1.2.1.2; primary bucket kegg:ppu00680)

    - PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)

    - mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37;
    primary bucket kegg:ppu00566)

    - glyA2: PP_0671 | Q88Q27 | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine
    methylase 2) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)

    - hprA: PP_0762 | Q88PT6 | Glycerate dehydrogenase (primary bucket kegg:ppu00680)

    - gcvT-I: PP_0986 | Q88P67 | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage
    system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)

    - gcvP1: PP_0988 | Q88P65 | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2)
    (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) (Glycine dehydrogenase
    (aminomethyl-transferring) 1) (EC 1.4.4.2; primary bucket kegg:ppu00785)

    - gcvH1: PP_0989 | Q88P64 | Glycine cleavage system H protein 1 (primary bucket
    kegg:ppu00785)

    - eda: PP_1024 | Q88P29 | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14)
    (EC 4.1.2.14; primary bucket kegg:ppu00030)

    - ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate
    reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81;
    primary bucket kegg:ppu00030)

    - purU-II: PP_1367 | Q88N49 | Formyltetrahydrofolate deformylase (EC 3.5.1.10)
    (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)

    - PP_1907: PP_1907 | Q88LM3 | Hydrolase, haloacid dehalogenase-like family (primary
    bucket kegg:ppu00630)

    - purU-III: PP_1943 | Q88LI9 | Formyltetrahydrofolate deformylase (EC 3.5.1.10)
    (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)

    - acnA-I: PP_2112 | Q88L24 | Aconitate hydratase (Aconitase) (EC 4.2.1.3) (EC
    4.2.1.3; primary bucket kegg:ppu00020)

    - puuA-I: PP_2178 | Q88KW1 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11;
    primary bucket kegg:ppu00910)

    - PP_2183: PP_2183 | Q88KV6 | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase
    I subunit E) (NDH-1 subunit E) (primary bucket kegg:ppu00680)

    - PP_2184: PP_2184 | Q88KV5 | NADH-quinone oxidoreductase subunit F (NADH dehydrogenase
    I subunit F) (NDH-1 subunit F) (primary bucket kegg:ppu00680)

    - PP_2185: PP_2185 | Q88KV4 | Formate dehydrogenase, alpha subunit (primary bucket
    kegg:ppu00680)

    - PP_2186: PP_2186 | Q88KV3 | Formate dehydrogenase, delta subunit (primary bucket
    kegg:ppu00680)

    - PP_2213: PP_2213 | Q88KS6 | Acyl-CoA synthetase (EC 6.2.1.-) (EC 6.2.1.-; primary
    bucket kegg:ppu00680)

    - PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - prpC: PP_2335 | Q88KF5 | Citrate synthase (primary bucket kegg:ppu00020)

    - acnB: PP_2339 | Q88KF1 | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate
    dehydratase) (EC 4.2.1.3; 4.2.1.99; primary bucket kegg:ppu00020)

    - PP_2887: PP_2887 | Q88IW2 | Catalase-related peroxidase (EC 1.11.1.-) (EC 1.11.1.-;
    primary bucket kegg:ppu04146)

    - PP_3148: PP_3148 | Q88I53 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - garK: PP_3178 | Q88I24 | Glycerate kinase (EC 2.7.1.165) (EC 2.7.1.165; primary
    bucket kegg:ppu00561)

    - PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)

    - glcD: PP_3745 | Q88GH8 | Glycolate oxidase, putative FAD-linked subunit (EC
    1.1.99.14) (EC 1.1.99.14; primary bucket kegg:ppu00630)

    - glcE: PP_3746 | Q88GH7 | Glycolate oxidase, putative FAD-binding subunit (EC
    1.1.99.14) (EC 1.1.99.14; primary bucket kegg:ppu00630)

    - glcF: PP_3747 | Q88GH6 | Glycolate oxidase iron-sulfur subunit (EC 1.1.99.14)
    (EC 1.1.99.14; primary bucket kegg:ppu00630)

    - bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC
    2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)

    - aceA: PP_4116 | Q88FI0 | Isocitrate lyase (EC 4.1.3.1) (EC 4.1.3.1; primary
    bucket kegg:ppu00640)

    - lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - gltA: PP_4194 | Q88FA4 | Citrate synthase (primary bucket kegg:ppu00020)

    - gcl: PP_4297 | Q88F03 | Glyoxylate carboligase (EC 4.1.1.47) (Tartronate-semialdehyde
    synthase) (EC 4.1.1.47; primary bucket kegg:ppu00630)

    - hyi: PP_4298 | Q88F02 | Hydroxypyruvate isomerase (EC 5.3.1.22) (EC 5.3.1.22;
    primary bucket kegg:ppu00630)

    - glxR: PP_4299 | Q88F01 | Tartronate semialdehyde reductase (EC 1.1.1.60) (EC
    1.1.1.60; primary bucket kegg:ppu00630)

    - ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81;
    primary bucket kegg:ppu00561)

    - PP_4399: PP_4399 | Q88EQ4 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - acsA1: PP_4487 | Q88EH6 | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1)
    (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme 1) (EC 6.2.1.1;
    primary bucket kegg:ppu00680)

    - PP_4547: PP_4547 | Q88EB9 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - acsA2: PP_4702 | Q88DW6 | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2)
    (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme 2) (EC 6.2.1.1;
    primary bucket kegg:ppu00680)

    - hutG: PP_5029 | Q88D00 | N-formylglutamate deformylase (EC 3.5.1.68) (EC 3.5.1.68;
    primary bucket kegg:ppu00340)

    - glnA: PP_5046 | Q88CY3 | Glutamine synthetase (EC 6.3.1.2) (EC 6.3.1.2; primary
    bucket kegg:ppu00910)

    - spuB: PP_5183 | Q88CJ7 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)

    - spuI: PP_5184 | Q88CJ6 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)

    - gcvP2: PP_5192 | Q88CI9 | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2)
    (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) (Glycine dehydrogenase
    (aminomethyl-transferring) 2) (EC 1.4.4.2; primary bucket kegg:ppu00785)

    - gcvH2: PP_5193 | Q88CI8 | Glycine cleavage system H protein 2 (primary bucket
    kegg:ppu00785)

    - gcvT: PP_5194 | Q88CI7 | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage
    system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)

    - puuA-II: PP_5299 | Q88C84 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11;
    primary bucket kegg:ppu00910)

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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__glycolate_glyoxylate_assimilation__ppu00630-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__glycolate_glyoxylate_assimilation__ppu00630-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial glycolate and glyoxylate assimilation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00630
- Resolved ID: ppu00630
- Resolved name: Glyoxylate and dicarboxylate metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00630 with 9 primary genes; module area: central_carbon.

## Candidate Genes From Local Metadata

Candidate gene count: 62

- PP_0094: PP_0094 | Q88RN5 | 5'-nucleotidase (EC 3.1.3.5) (EC 3.1.3.5; primary bucket kegg:ppu00630)
- katE: PP_0115 | Q88RL4 | Catalase (EC 1.11.1.6) (EC 1.11.1.6; primary bucket kegg:ppu04146)
- glyA1: PP_0322 | Q88R12 | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)
- purU-I: PP_0327 | Q88R07 | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)
- glcB: PP_0356 | Q88QX8 | Malate synthase G (EC 2.3.3.9) (EC 2.3.3.9; primary bucket kegg:ppu00620)
- PP_0416: PP_0416 | Q88QS2 | Phosphoglycolate phosphatase (PGP) (PGPase) (EC 3.1.3.18) (EC 3.1.3.18; primary bucket kegg:ppu00630)
- katA: PP_0481 | Q88QK9 | Catalase (EC 1.11.1.6) (EC 1.11.1.6; primary bucket kegg:ppu04146)
- fdoG: PP_0489 | A0A140FVZ1 | Formate dehydrogenase-O major subunit (EC 1.2.1.2) (EC 1.2.1.2; primary bucket kegg:ppu00680)
- fdoH: PP_0490 | Q88QK1 | Formate dehydrogenase iron-sulfur subunit (primary bucket kegg:ppu00680)
- fdoI: PP_0491 | Q88QK0 | Formate dehydrogenase-O, gamma subunit (EC 1.2.1.2) (EC 1.2.1.2; primary bucket kegg:ppu00680)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37; primary bucket kegg:ppu00566)
- glyA2: PP_0671 | Q88Q27 | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)
- hprA: PP_0762 | Q88PT6 | Glycerate dehydrogenase (primary bucket kegg:ppu00680)
- gcvT-I: PP_0986 | Q88P67 | aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)
- gcvP1: PP_0988 | Q88P65 | Glycine dehydrogenase (decarboxylating) 1 (EC 1.4.4.2) (Glycine cleavage system P-protein 1) (Glycine decarboxylase 1) (Glycine dehydrogenase (aminomethyl-transferring) 1) (EC 1.4.4.2; primary bucket kegg:ppu00785)
- gcvH1: PP_0989 | Q88P64 | Glycine cleavage system H protein 1 (primary bucket kegg:ppu00785)
- eda: PP_1024 | Q88P29 | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14) (EC 4.1.2.14; primary bucket kegg:ppu00030)
- ghrB: PP_1261 | Q88NF1 | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) (EC 1.1.1.215; 1.1.1.79; 1.1.1.81; primary bucket kegg:ppu00030)
- purU-II: PP_1367 | Q88N49 | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)
- PP_1907: PP_1907 | Q88LM3 | Hydrolase, haloacid dehalogenase-like family (primary bucket kegg:ppu00630)
- purU-III: PP_1943 | Q88LI9 | Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase) (EC 3.5.1.10; primary bucket kegg:ppu00670)
- acnA-I: PP_2112 | Q88L24 | Aconitate hydratase (Aconitase) (EC 4.2.1.3) (EC 4.2.1.3; primary bucket kegg:ppu00020)
- puuA-I: PP_2178 | Q88KW1 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11; primary bucket kegg:ppu00910)
- PP_2183: PP_2183 | Q88KV6 | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase I subunit E) (NDH-1 subunit E) (primary bucket kegg:ppu00680)
- PP_2184: PP_2184 | Q88KV5 | NADH-quinone oxidoreductase subunit F (NADH dehydrogenase I subunit F) (NDH-1 subunit F) (primary bucket kegg:ppu00680)
- PP_2185: PP_2185 | Q88KV4 | Formate dehydrogenase, alpha subunit (primary bucket kegg:ppu00680)
- PP_2186: PP_2186 | Q88KV3 | Formate dehydrogenase, delta subunit (primary bucket kegg:ppu00680)
- PP_2213: PP_2213 | Q88KS6 | Acyl-CoA synthetase (EC 6.2.1.-) (EC 6.2.1.-; primary bucket kegg:ppu00680)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- prpC: PP_2335 | Q88KF5 | Citrate synthase (primary bucket kegg:ppu00020)
- acnB: PP_2339 | Q88KF1 | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate dehydratase) (EC 4.2.1.3; 4.2.1.99; primary bucket kegg:ppu00020)
- PP_2887: PP_2887 | Q88IW2 | Catalase-related peroxidase (EC 1.11.1.-) (EC 1.11.1.-; primary bucket kegg:ppu04146)
- PP_3148: PP_3148 | Q88I53 | Glutamine synthetase (primary bucket kegg:ppu00910)
- garK: PP_3178 | Q88I24 | Glycerate kinase (EC 2.7.1.165) (EC 2.7.1.165; primary bucket kegg:ppu00561)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- glcD: PP_3745 | Q88GH8 | Glycolate oxidase, putative FAD-linked subunit (EC 1.1.99.14) (EC 1.1.99.14; primary bucket kegg:ppu00630)
- glcE: PP_3746 | Q88GH7 | Glycolate oxidase, putative FAD-binding subunit (EC 1.1.99.14) (EC 1.1.99.14; primary bucket kegg:ppu00630)
- glcF: PP_3747 | Q88GH6 | Glycolate oxidase iron-sulfur subunit (EC 1.1.99.14) (EC 1.1.99.14; primary bucket kegg:ppu00630)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- aceA: PP_4116 | Q88FI0 | Isocitrate lyase (EC 4.1.3.1) (EC 4.1.3.1; primary bucket kegg:ppu00640)
- lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- gltA: PP_4194 | Q88FA4 | Citrate synthase (primary bucket kegg:ppu00020)
- gcl: PP_4297 | Q88F03 | Glyoxylate carboligase (EC 4.1.1.47) (Tartronate-semialdehyde synthase) (EC 4.1.1.47; primary bucket kegg:ppu00630)
- hyi: PP_4298 | Q88F02 | Hydroxypyruvate isomerase (EC 5.3.1.22) (EC 5.3.1.22; primary bucket kegg:ppu00630)
- glxR: PP_4299 | Q88F01 | Tartronate semialdehyde reductase (EC 1.1.1.60) (EC 1.1.1.60; primary bucket kegg:ppu00630)
- ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81; primary bucket kegg:ppu00561)
- PP_4399: PP_4399 | Q88EQ4 | Glutamine synthetase (primary bucket kegg:ppu00910)
- lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- acsA1: PP_4487 | Q88EH6 | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme 1) (EC 6.2.1.1; primary bucket kegg:ppu00680)
- PP_4547: PP_4547 | Q88EB9 | Glutamine synthetase (primary bucket kegg:ppu00910)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- acsA2: PP_4702 | Q88DW6 | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme 2) (EC 6.2.1.1; primary bucket kegg:ppu00680)
- hutG: PP_5029 | Q88D00 | N-formylglutamate deformylase (EC 3.5.1.68) (EC 3.5.1.68; primary bucket kegg:ppu00340)
- glnA: PP_5046 | Q88CY3 | Glutamine synthetase (EC 6.3.1.2) (EC 6.3.1.2; primary bucket kegg:ppu00910)
- spuB: PP_5183 | Q88CJ7 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)
- spuI: PP_5184 | Q88CJ6 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)
- gcvP2: PP_5192 | Q88CI9 | Glycine dehydrogenase (decarboxylating) 2 (EC 1.4.4.2) (Glycine cleavage system P-protein 2) (Glycine decarboxylase 2) (Glycine dehydrogenase (aminomethyl-transferring) 2) (EC 1.4.4.2; primary bucket kegg:ppu00785)
- gcvH2: PP_5193 | Q88CI8 | Glycine cleavage system H protein 2 (primary bucket kegg:ppu00785)
- gcvT: PP_5194 | Q88CI7 | Aminomethyltransferase (EC 2.1.2.10) (Glycine cleavage system T protein) (EC 2.1.2.10; primary bucket kegg:ppu00785)
- puuA-II: PP_5299 | Q88C84 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11; primary bucket kegg:ppu00910)
- lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)

## Generic Module Context

### Working Scope

A reusable bacterial central-carbon module for conversion of glycolate and glyoxylate into metabolites that can re-enter core carbon metabolism. The module covers phosphoglycolate dephosphorylation to glycolate, multicomponent glycolate oxidation to glyoxylate, and the glyoxylate carboligase/tartronate semialdehyde branch that converts glyoxylate-derived carbon toward glycerate. Pseudomonas putida KT2440 provides local exemplars for the phosphoglycolate phosphatase, GlcDEF glycolate dehydrogenase, Gcl, Hyi, and GlxR roles, but the module boundary is the conserved bacterial pathway segment rather than a PSEPK-specific locus definition.

### Provisional Biological Outline

- Bacterial glycolate and glyoxylate assimilation
  - 1. phosphoglycolate dephosphorylation to glycolate
  - 2-phosphoglycolate to glycolate
    - Phosphoglycolate phosphatase (molecular player: bacterial phosphoglycolate phosphatase family; activity or role: phosphoglycolate phosphatase activity)
  - 2. glycolate oxidation to glyoxylate
  - GlcDEF glycolate dehydrogenase complex
    - GlcD FAD-linked glycolate dehydrogenase subunit (molecular player: GlcD glycolate oxidase/dehydrogenase family; activity or role: glycolate dehydrogenase activity)
    - GlcE FAD-binding glycolate dehydrogenase subunit (molecular player: GlcE glycolate oxidase/dehydrogenase family; activity or role: contributes to glycolate dehydrogenase activity)
    - GlcF iron-sulfur glycolate dehydrogenase subunit (molecular player: GlcF glycolate oxidase iron-sulfur subunit family; activity or role: contributes to glycolate dehydrogenase activity)
  - 3. glyoxylate condensation to tartronate semialdehyde
  - Glyoxylate to tartronate semialdehyde
    - Glyoxylate carboligase (molecular player: glyoxylate carboligase family; activity or role: tartronate-semialdehyde synthase activity)
  - 4. hydroxypyruvate and tartronate-semialdehyde interconversion
  - Hydroxypyruvate isomerization
    - Hydroxypyruvate isomerase (molecular player: hydroxypyruvate isomerase family; activity or role: hydroxypyruvate isomerase activity)
  - 5. tartronate semialdehyde reduction to glycerate
  - Tartronate semialdehyde to glycerate
    - Tartronate semialdehyde reductase (molecular player: tartronate semialdehyde reductase family; activity or role: 2-hydroxy-3-oxopropionate reductase activity)

### Known Relationships Among Steps

- 2-phosphoglycolate to glycolate feeds into GlcDEF glycolate dehydrogenase complex: Phosphoglycolate phosphatase produces glycolate, the substrate oxidized by the GlcDEF glycolate dehydrogenase complex.
- GlcDEF glycolate dehydrogenase complex feeds into Glyoxylate to tartronate semialdehyde: GlcDEF oxidizes glycolate to glyoxylate, supplying the glyoxylate used by glyoxylate carboligase.
- Glyoxylate to tartronate semialdehyde feeds into Tartronate semialdehyde to glycerate: Glyoxylate carboligase produces tartronate semialdehyde (2-hydroxy-3-oxopropanoate), the substrate reduced by GlxR.
- Hydroxypyruvate isomerization feeds into Tartronate semialdehyde to glycerate: Hyi can provide the same tartronate-semialdehyde intermediate from hydroxypyruvate, connecting hydroxypyruvate metabolism to the GlxR reduction step.

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

# Module/Pathway/Taxon Review: Bacterial Glycolate and Glyoxylate Assimilation in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00630` — *Glyoxylate and dicarboxylate metabolism*
**Module area:** central_carbon
**Scope reviewed:** glycolate → glyoxylate → glycerate assimilation module (phosphoglycolate dephosphorylation; multicomponent glycolate oxidation; glyoxylate carboligase / tartronate-semialdehyde branch)

---

## 1. Executive Summary

The core bacterial glycolate/glyoxylate-assimilation module is **genomically present and experimentally validated** in *P. putida* KT2440, but it is **conditionally active** because the key branch is transcriptionally repressed in the wild-type strain. Direct KT2440 evidence establishes that the GlcDEF glycolate dehydrogenase (PP_3745–PP_3747) oxidizes glycolate to glyoxylate, and that a co-transcribed operon — *gcl-hyi-glxR-ttuD-pykF* — carries glyoxylate to glycerate via glyoxylate carboligase Gcl (PP_4297) and tartronate-semialdehyde reductase GlxR (PP_4299). Overexpression of only *gcl* plus *glxR* is sufficient to confer growth on ethylene glycol, demonstrating that module steps 2, 3, and 5 are functionally covered. Consequently these steps should be marked **covered**, with the important caveat that the entire *gcl* branch is repressed by the regulator **GclR** in wild-type KT2440 and becomes active only upon regulatory de-repression (e.g., loss-of-function *gclR* mutations selected during adaptive laboratory evolution).

Two curation corrections are required. First, the generic **"step 1" 2-phosphoglycolate phosphatase** (candidate PP_0416 / PP_1907) does **not** represent the physiological entry to glycolate assimilation in this organism. 2-Phosphoglycolate salvage is biochemically tied to the RuBisCO oxygenase reaction and the Calvin-Benson-Bassham (CBB) cycle / oxygenic photorespiration, which KT2440 — a chemoheterotroph — lacks. In the experimentally characterized KT2440 route, glycolate arises from oxidation of ethylene-glycol-derived glycolaldehyde, not from 2-phosphoglycolate. This step should be flagged **module_needs_revision / not_expected_in_target_taxon** as the physiological entry, retaining PP_0416 only as a housekeeping/detoxification phosphatase.

Second, the **62-gene candidate list is dominated by neighboring-pathway "bucket noise."** KEGG map 00630 is a broad hub map that overlaps the glyoxylate shunt, TCA cycle, glycine/serine and C1 metabolism, nitrogen assimilation, and thiolase chemistry. Only ~9 candidates are true `ppu00630`-primary, and only ~7 genes form the actual glycolate→glyoxylate→glycerate module core (*glcDEF*, *gcl*, *hyi*, *glxR*, plus the PGP step). Reductase paralogs *ttuD*, *ghrB*, and *hprA* carry broad EC mappings and are likely over-annotated for this module; PP_0094 (5′-nucleotidase) is a clear map artifact with no role in glycolate/glyoxylate assimilation. No dedicated glycolate/glyoxylate permease is present among the candidates, consistent with an intracellular substrate-supply mode.

---

## 2. Target-Organism Pathway Definition

**Process included.** The reviewed module is the conserved bacterial pathway segment that converts glycolate and glyoxylate into glycerate, a metabolite that re-enters lower glycolysis/gluconeogenesis. In *P. putida* KT2440 the physiologically relevant sequence is:

```
ethylene glycol ─▶ glycolaldehyde ─▶ glycolate ─▶ glyoxylate ─▶ tartronate semialdehyde ─▶ glycerate ─▶ 2-phosphoglycerate
                     (Ped ADH/ALDH)     (GlcDEF)      (Gcl)             (GlxR)          (GarK)
                                                                                   └─(Hyi auxiliary; hydroxypyruvate)
```

- **Step 2 — glycolate oxidation:** GlcDEF (PP_3745/3746/3747), a three-subunit FAD/Fe-S glycolate dehydrogenase.
- **Step 3 — glyoxylate condensation:** Gcl (PP_4297), glyoxylate carboligase / tartronate-semialdehyde synthase (EC 4.1.1.47).
- **Step 4 — hydroxypyruvate/tartronate-semialdehyde interconversion:** Hyi (PP_4298), hydroxypyruvate isomerase (EC 5.3.1.22) — auxiliary.
- **Step 5 — tartronate-semialdehyde reduction:** GlxR (PP_4299), tartronate-semialdehyde reductase (EC 1.1.1.60).
- Downstream re-entry: glycerate → 2-phosphoglycerate by glycerate kinase GarK (PP_3178).

**Neighboring pathways to keep separate.** KEGG `ppu00630` is a broad "overview-adjacent" map. The following overlapping processes should be curated as **distinct** modules and not merged into the glycolate/glyoxylate-assimilation module:

- **Glyoxylate shunt** (isocitrate lyase AceA / malate synthase GlcB; KEGG ppu00620/ppu00640) — a distinct anaplerotic route that *consumes* glyoxylate but is not part of the glycolate→glycerate branch.
- **Glycine/serine and C1 metabolism** (glyA1/glyA2, glycine cleavage system gcv, purU deformylases; ppu00785/ppu00670/ppu04981).
- **TCA cycle / aconitase / citrate synthase** (acnA, acnB, gltA, prpC; ppu00020).
- **Nitrogen assimilation / glutamine synthetase family** (glnA, PP_3148, PP_4399, PP_4547, puuA, spuB/spuI; ppu00910).
- **Formate/methane metabolism** (fdoGHI, formate dehydrogenase subunits; ppu00680).
- **Thiolase / acetyl-CoA acetyltransferase family** (bktB, yqeF, PP_0582, PP_2215, PP_3355; ppu00900).

**Alternate names / database definitions.** The reviewed segment is variously described as "glycolate utilization" (glc genes), the "glyoxylate carboligase (tartronate-semialdehyde) pathway," and the "glycerate pathway." KEGG folds these into map 00630 (Glyoxylate and dicarboxylate metabolism); MetaCyc represents the glycerate branch as the *glycolate and glyoxylate degradation* pathway. The step-1 phosphatase (EC 3.1.3.18) belongs biochemically to **photorespiration** in phototrophs, which is a database-driven inclusion, not a KT2440 physiological reality.

---

## 3. Expected Step Model and Satisfiability

| Module step | Expected enzyme | KT2440 candidate | Status | Confidence / evidence type |
|---|---|---|---|---|
| 1. 2-phosphoglycolate → glycolate | Phosphoglycolate phosphatase (EC 3.1.3.18) | PP_0416, PP_1907 | **module_needs_revision** / not physiological entry | Homology + biochemical context; direct absence of CBB/RuBisCO |
| 2. glycolate → glyoxylate | GlcDEF glycolate dehydrogenase (EC 1.1.99.14) | PP_3745/3746/3747 | **covered** | Direct KT2440 experiment (overexpression relieves bottleneck) |
| 3. glyoxylate → tartronate semialdehyde | Glyoxylate carboligase Gcl (EC 4.1.1.47) | PP_4297 | **covered** (GclR-gated) | Direct KT2440 experiment (gcl+glxR sufficient) |
| 4. hydroxypyruvate ⇌ tartronate semialdehyde | Hydroxypyruvate isomerase Hyi (EC 5.3.1.22) | PP_4298 | **covered / auxiliary** | Operon co-transcription; not strictly required |
| 5. tartronate semialdehyde → glycerate | Tartronate-semialdehyde reductase GlxR (EC 1.1.1.60) | PP_4299 | **covered** | Direct KT2440 experiment (gcl+glxR sufficient) |
| (downstream) glycerate → 2-P-glycerate | Glycerate kinase GarK (EC 2.7.1.165) | PP_3178 | covered (re-entry) | Homology + pathway logic |
| (transport) glycolate/glyoxylate import | GlcA-type permease | — none in candidates | **gap** | Absence in candidate set; intracellular supply route |

**Steps encoded by candidate genes:** 2, 3, 4, 5, plus glycerate re-entry (GarK). These constitute a satisfiable core.

**Steps missing from metadata but likely present under other names:** none of the core catalytic steps are missing; the reductase step has *extra* paralogs rather than a gap. Transport is the genuine unfilled slot (see §5).

**Steps probably not expected in this organism:** the physiological version of step 1 (2-phosphoglycolate salvage as the glycolate source) is not expected in this RuBisCO-lacking heterotroph.

---

## 4. Candidate Genes and Evidence

### High-confidence core module genes

**GlcDEF — PP_3745 (glcD), PP_3746 (glcE), PP_3747 (glcF); EC 1.1.99.14 (Finding F002).**
This three-subunit FAD-linked / FAD-binding / iron-sulfur glycolate dehydrogenase performs the committed glycolate→glyoxylate oxidation. Franden et al. 2018 showed by direct engineering in KT2440 that overexpression of the *glcDEF* operon **removes the glycolate bottleneck** during ethylene-glycol metabolism and minimizes accumulation of toxic glycolaldehyde/glyoxal intermediates ([PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/)). Mückschel et al. 2012 independently documented temporal accumulation of glycolic and glyoxylic acid in KT2440, consistent with GlcDEF being the flux-controlling glycolate-oxidizing activity ([PMID: 23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/)). **Evidence type: direct KT2440 experiment. Curation: mark step 2 covered.** No paralog ambiguity; these three loci are the unambiguous complex.

**Gcl — PP_4297; glyoxylate carboligase / tartronate-semialdehyde synthase; EC 4.1.1.47 (Findings F001, F003).**
Gcl condenses two glyoxylate molecules to tartronate semialdehyde, committing glyoxylate carbon to the glycerate branch. Franden et al. 2018 demonstrated by directed overexpression that expressing **only *gcl* plus *glxR* was sufficient to confer growth on ethylene glycol**, with full-operon expression improving growth ([PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/)). **Evidence type: direct KT2440 experiment. Curation: covered, but GclR-gated.**

**GlxR — PP_4299; tartronate-semialdehyde reductase; EC 1.1.1.60 (Findings F001, F005).**
GlxR reduces tartronate semialdehyde to glycerate, the module's exit metabolite. Validated as the functional reductase in the same *gcl*+*glxR* sufficiency experiment ([PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/)). **Evidence type: direct KT2440 experiment. Curation: covered.** This is the validated reductase; do not let the broad-EC paralogs (below) dilute the assignment.

**Hyi — PP_4298; hydroxypyruvate isomerase; EC 5.3.1.22 (Finding F001).**
Co-transcribed within the *gcl* operon. Provides tartronate-semialdehyde/hydroxypyruvate interconversion, linking hydroxypyruvate metabolism to the GlxR reduction step. It is **auxiliary** — not strictly required for growth (gcl+glxR alone suffice) — but part of the physiological operon. **Curation: covered / auxiliary.**

**Operon architecture (Finding F001).** Franden et al. 2018 established by qRT-PCR that the four genes genomically proximal to *gcl* (*hyi, glxR, ttuD, pykF*) are **co-transcribed as a single operon** with *gcl* ([PMID: 29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/)). This operon structure is the strongest single piece of KT2440-specific evidence for the module and should anchor its curation.

**GarK — PP_3178; glycerate kinase; EC 2.7.1.165 (Finding F005).**
Downstream re-entry step: phosphorylates glycerate to 2-phosphoglycerate, feeding lower glycolysis. Evidence is homology + pathway logic; not directly tested here but mechanistically required.

### Regulatory context (not a catalytic candidate but curation-critical)

**GclR — represses the gcl/glyoxylate-carboligase branch (Finding F003).**
Li et al. 2019 identified the transcriptional regulator **GclR** as the repressor of the glyoxylate carboligase pathway; **loss-of-function *gclR* mutations were required** to enable growth on ethylene glycol as sole carbon source in adaptive laboratory evolution ([PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)). Mückschel et al. 2012 corroborated the regulatory state at the pathway level: in *P. putida* JM37, Gcl, malate synthase (GlcB), and isocitrate lyase (AceA) were all induced by ethylene glycol/glyoxylate, whereas **KT2440 showed induction of AceA only** — the *gcl* branch was transcriptionally silent in wild-type KT2440 ([PMID: 23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/)). This explains the apparent paradox: the genes are present and functional, but the wild-type pathway is off. **Curation: annotate the module as "covered but conditionally active / GclR-repressed."**

### Lower-confidence / over-annotated candidates

**Step-1 phosphatases — PP_0416 (phosphoglycolate phosphatase, EC 3.1.3.18), PP_1907 (HAD hydrolase) (Finding F004).**
PGP dephosphorylates 2-phosphoglycolate to glycolate ([PMID: 38861076](https://pubmed.ncbi.nlm.nih.gov/38861076/)), but 2-phosphoglycolate is generated primarily by the RuBisCO oxygenase reaction in CBB-cycle / photorespiratory organisms ([PMID: 38593075](https://pubmed.ncbi.nlm.nih.gov/38593075/)). KT2440 lacks RuBisCO and the CBB cycle; its only endogenous 2-phosphoglycolate is the minor DNA-repair-derived pool. In the characterized KT2440 route glycolate comes from glycolaldehyde oxidation, not from 2-phosphoglycolate. **Curation: PP_0416 retained as housekeeping/detoxification phosphatase; step 1 flagged not the physiological entry.**

**Reductase paralogs — ghrB (PP_1261), hprA (PP_0762), ttuD (PP_4300) (Finding F005).**
These three carry broad or overlapping EC annotations (ghrB: EC 1.1.1.215/1.1.1.79/1.1.1.81, primary bucket ppu00030; hprA: glycerate dehydrogenase, ppu00680; ttuD: hydroxypyruvate reductase EC 1.1.1.81, ppu00561) that could *nominally* satisfy the tartronate-semialdehyde/hydroxypyruvate reduction step. GlxR is the validated reductase; these paralogs are **likely over-annotated** for this module. Note the specific conflict in **ttuD (PP_4300)**: it is co-transcribed in the *gcl* operon and named for the tartrate-utilization glycerate *kinase*, yet the metadata annotates it as hydroxypyruvate *reductase* — an unresolved name/function conflict warranting individual review.

**Clear map artifacts.** PP_0094 (5′-nucleotidase, EC 3.1.3.5) has **no role** in glycolate/glyoxylate assimilation and is a KEGG-map artifact. The bulk of the remaining 53 candidates (glyoxylate-shunt, TCA, C1, nitrogen, thiolase enzymes) are neighboring-bucket noise (Finding F006).

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**Candidate-list composition (Finding F006).** Of 62 candidates, only **9 are `ppu00630`-primary** (PP_0094, PP_0416, PP_1907, glcD/E/F, gcl, hyi, glxR), and only **~7 form the true module core** (glcDEF, gcl, hyi, glxR + PGP step). The other 53 belong to other primary KEGG buckets and are pulled in because map 00630 is a broad hub overlapping glycine/serine, TCA, the glyoxylate shunt, C1, nitrogen, and thiolase metabolism. Curators should down-weight the list to the core seven and treat the rest as cross-map contamination.

**Transport gap (Finding F007).** The *E. coli* *glc* system includes a glycolate permease (GlcA, part of the *glcDEFGBA* cluster). In KT2440 there is **no annotated glycolate/glyoxylate permease among the candidates**; the *glcDEF* operon lacks an adjacent transporter and malate-synthase gene (KT2440 *glcB*, PP_0356, is a separate ppu00620 locus). Because glycolate is generated **intracellularly** from ethylene-glycol-derived glycolaldehyde, a dedicated import step is not strictly required for that carbon-entry mode. Whether exogenous glycolate uptake occurs, and via which transporter, is **unresolved** for KT2440 and is the module's genuine open gap.

**Regulatory conditionality.** The module is satisfiable but **off in the wild type**. Any "covered" call must carry the GclR-repression caveat; the module is fully active only in *gclR* de-repressed backgrounds.

**Step-1 mismatch.** The generic module boundary that places a 2-phosphoglycolate phosphatase as the glycolate entry is **wrong for this organism** and reflects a phototroph-centric definition.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|---|---|---|
| Step 1 — phosphoglycolate → glycolate | **module_needs_revision** (not_expected_in_target_taxon as physiological entry) | No RuBisCO/CBB in KT2440; PP_0416 is housekeeping only |
| Step 2 — glycolate → glyoxylate (GlcDEF) | **covered** | Direct KT2440 experiment |
| Step 3 — glyoxylate → tartronate semialdehyde (Gcl) | **covered** (flag GclR-repressed) | Direct KT2440 experiment |
| Step 4 — hydroxypyruvate isomerization (Hyi) | **covered / auxiliary** | Operon member; non-essential for growth |
| Step 5 — tartronate semialdehyde → glycerate (GlxR) | **covered** | Direct KT2440 experiment |
| Transport (glycolate import) | **gap** (candidate_uncertain) | No GlcA-type permease in candidate set |
| Reductase paralogs (ghrB/hprA/ttuD) | **candidate_uncertain / likely over-annotated** | Broad EC mappings; GlxR is validated reductase |

**Module boundary revisions.** (1) Redefine the module entry for heterotrophic Pseudomonads so that glycolate originates from glycolaldehyde oxidation rather than 2-phosphoglycolate dephosphorylation, or explicitly mark the phosphatase step as lineage-conditional (present only in CBB/photorespiratory organisms). (2) Add a **regulatory annotation node (GclR)** to capture the conditional-activity state, since satisfiability here is regulatory, not genetic. (3) Add a **transport slot** marked as an open gap.

**GO-curation notes.** GlcDEF, Gcl, and GlxR have strong experimental support for specific GO molecular-function and biological-process terms (glycolate catabolic process; tartronate-semialdehyde synthase activity; 2-hydroxy-3-oxopropionate reductase activity). Avoid propagating the broad multi-EC reductase GO terms from ghrB to the module reductase role. No new GO term requests appear strictly necessary, but a **GO annotation extension** capturing GclR regulation (or a "conditionally active/repressed" qualifier) would improve fidelity.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **PP_4300 (ttuD)** — resolve the name/function conflict (tartrate-utilization glycerate kinase vs. annotated hydroxypyruvate reductase EC 1.1.1.81); it is a *gcl*-operon member and its true role affects module wiring.
2. **PP_0416 (PGP, EC 3.1.3.18)** — confirm housekeeping/detoxification role and formally decouple it from the physiological glycolate-entry annotation.
3. **PP_1261 (ghrB)** and **PP_0762 (hprA)** — assess whether their broad EC/GO mappings should be trimmed to avoid over-propagation onto the module reductase step.
4. **GlcA-type permease search** — a targeted genome-wide review to determine whether a glycolate/glyoxylate transporter exists outside the candidate set (the module's real gap).
5. **GclR regulator locus** — promote for annotation as the repressor controlling module activity (curation-critical even though non-catalytic).

The validated core (glcDEF, gcl, glxR, hyi) does not require further gene-level review beyond confirming loci — the experimental evidence is direct and sufficient.

---

## 8. Evidence Base

| Paper | PMID | Contribution | Evidence strength for KT2440 |
|---|---|---|---|
| *Engineering P. putida KT2440 for efficient ethylene glycol utilization* (Franden et al. 2018) | [29885475](https://pubmed.ncbi.nlm.nih.gov/29885475/) | Operon structure of *gcl-hyi-glxR-ttuD-pykF*; gcl+glxR sufficiency for growth; glcDEF overexpression relieves glycolate bottleneck | **Direct, strain-specific** |
| *Laboratory evolution reveals the metabolic and regulatory basis of ethylene glycol metabolism by P. putida KT2440* (Li et al. 2019) | [31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/) | GclR identified as repressor of the glyoxylate carboligase pathway; gclR loss-of-function required for growth | **Direct, strain-specific** |
| *Ethylene glycol metabolism by Pseudomonas putida* (Mückschel et al. 2012) | [23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/) | Temporal glycolate/glyoxylate accumulation; KT2440 induces AceA only (gcl branch silent) | **Direct, strain-specific** |
| *Determination of Phosphoglycolate Phosphatase Activity…* | [38861076](https://pubmed.ncbi.nlm.nih.gov/38861076/) | PGP dephosphorylates 2-phosphoglycolate to glycolate (photorespiratory context) | Biochemical context (not KT2440) |
| *Removal of phosphoglycolate in hyperthermophilic archaea* | [38593075](https://pubmed.ncbi.nlm.nih.gov/38593075/) | 2-Phosphoglycolate salvage linked to CBB cycle / oxygenic photosynthesis | Contextual (supports step-1 exclusion) |
| *Ethylene glycol metabolism in Ideonella sakaiensis* | [36289066](https://pubmed.ncbi.nlm.nih.gov/36289066/) | I. sakaiensis EG enzymes are homologs of KT2440 Ped enzymes — confirms upstream glycolaldehyde route | Related organism, supports upstream supply |

**How the evidence coheres.** The three KT2440-specific papers converge on a single narrative: the module is genetically complete and biochemically functional (Franden 2018), the wild-type pathway is regulated off (Mückschel 2012; Li 2019), and de-repression via *gclR* unlocks growth on glycolate-generating substrates (Li 2019). The photorespiration/phosphatase literature (38861076, 38593075) supports the *exclusion* of step 1 as a physiological entry in this heterotroph.

---

## 9. Mechanistic Model

```
                            ┌────────────────── GclR repression (wild-type OFF) ───────────────┐
                            │                                                                   │
 ethylene glycol            ▼                                                                   ▼
      │  (Ped ADH/ALDH)   ┌──────────── gcl operon: gcl — hyi — glxR — ttuD — pykF ───────────┐
      ▼                   │                                                                    │
 glycolaldehyde           │   glyoxylate ──Gcl(PP_4297)──▶ tartronate semialdehyde            │
      │                   │       ▲                              │                             │
      ▼                   │       │                       GlxR(PP_4299)                        │
   GLYCOLATE ──GlcDEF────▶ glyoxylate                            ▼                             │
             (PP_3745-47)         │  Hyi(PP_4298)          GLYCERATE ──GarK(PP_3178)──▶ 2-P-glycerate
                                  │  hydroxypyruvate ⇌ TSA        │                             │
                                  ▼                              (lower glycolysis)            │
                            glyoxylate shunt (AceA/GlcB)  ◀── separate module ─────────────────┘

 [NOT physiological entry in KT2440]:  2-phosphoglycolate ──PGP(PP_0416)──▶ glycolate   (CBB/photorespiration-linked; no RuBisCO here)
```

The module is a **regulatory switch on top of a complete enzymatic path**: all catalytic parts exist and work, but flux through the *gcl* branch is gated by GclR. Glyoxylate sits at a branch point — it can be routed either to the glycerate pathway (this module, GclR-repressed) or through the glyoxylate shunt (AceA/GlcB, a separate module induced in KT2440).

---

## 10. Limitations and Knowledge Gaps

- **No direct enzymology performed here** — conclusions rest on published KT2440 genetics/physiology plus annotation reasoning, not new wet-lab data.
- **Transporter identity unknown** — whether KT2440 imports exogenous glycolate/glyoxylate, and via which permease, is unresolved.
- **ttuD name/function conflict unresolved** — kinase vs. reductase annotation needs experimental disambiguation.
- **Reductase paralog specificities** (ghrB, hprA) toward tartronate semialdehyde have not been kinetically compared with GlxR in KT2440.
- **Quantitative regulatory thresholds** — the exact GclR effector/derepression conditions in the wild type are only partly defined.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Genome-wide permease search** (targeted `fetch-gene`) for a GlcA/glyoxylate-transporter candidate outside the current bucket; test exogenous glycolate/glyoxylate uptake in KT2440.
2. **Disambiguate PP_4300 (ttuD)** by enzymatic assay (glycerate kinase vs. hydroxypyruvate reductase) and by phenotyping a clean deletion in a *gclR*-derepressed background.
3. **Reductase paralog comparison** — kinetically test GlxR vs. ghrB/hprA on tartronate semialdehyde to confirm GlxR is the physiological module reductase and trim over-propagated EC/GO terms.
4. **Confirm PP_0416 housekeeping role** — assess phenotype on glycolate/EG to verify it is dispensable for assimilation (detoxification-only).
5. **Curator actions:** mark steps 2/3/5 covered (GclR caveat), step 4 auxiliary-covered, step 1 module_needs_revision, transport gap; add a GclR regulatory node; down-weight the 53 non-core candidates as cross-map noise.

---

*Prepared as a species-aware curation review. Direct KT2440 evidence is available for the core oxidation and glyoxylate-to-glycerate steps; step-1 exclusion and transport/paralog calls are inferences from pathway logic, comparative genomics, and biochemical context and are flagged accordingly.*


## Artifacts

- [OpenScientist final report](PSEPK__glycolate_glyoxylate_assimilation__ppu00630-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__glycolate_glyoxylate_assimilation__ppu00630-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:29885475
2. PMID:23023748
3. PMID:31166064
4. PMID:38861076
5. PMID:38593075