---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T05:02:53.874879'
end_time: '2026-07-07T05:30:21.764352'
duration_seconds: 1647.89
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Pantothenate and CoA biosynthesis
  module_summary: A bacterial pantothenate and coenzyme A biosynthesis module covering
    formation of pantoate from 3-methyl-2-oxobutanoate, ligation with beta-alanine
    to form pantothenate, and conversion of pantothenate through phosphopantothenate,
    phosphopantothenoylcysteine, phosphopantetheine, and dephospho-CoA to CoA. In
    Pseudomonas putida KT2440, KEGG ppu00770 also includes branched-chain amino-acid
    precursor enzymes, pyrimidine/beta-alanine metabolism, ACP phosphopantetheine
    handling, and nucleotide hydrolase side nodes; these are tracked as precursor
    or boundary context unless they directly form pantothenate or CoA.
  module_outline: "- Pantothenate and CoA biosynthesis\n  - 1. pantoate branch of\
    \ pantothenate biosynthesis\n  - 3-methyl-2-oxobutanoate to pantoate\n    - PanB\
    \ ketopantoate hydroxymethyltransferase (molecular player: PSEPK panB; activity\
    \ or role: 3-methyl-2-oxobutanoate hydroxymethyltransferase activity)\n    - PanE\
    \ 2-dehydropantoate reductase (molecular player: PSEPK panE; activity or role:\
    \ 2-dehydropantoate 2-reductase activity)\n    - PP_2325 2-dehydropantoate reductase\
    \ candidate (molecular player: PSEPK PP_2325; activity or role: 2-dehydropantoate\
    \ 2-reductase activity)\n    - PP_2998 2-dehydropantoate reductase candidate (molecular\
    \ player: PSEPK PP_2998; activity or role: 2-dehydropantoate 2-reductase activity)\n\
    \    - PP_4452 2-dehydropantoate reductase candidate (molecular player: PSEPK\
    \ PP_4452; activity or role: 2-dehydropantoate 2-reductase activity)\n  - 2. pantothenate\
    \ synthetase\n  - Pantoate plus beta-alanine to pantothenate\n    - PanC pantothenate\
    \ synthetase (molecular player: PSEPK panC; activity or role: pantoate-beta-alanine\
    \ ligase activity)\n  - 3. pantothenate to coenzyme A\n  - Pantothenate to CoA\n\
    \    - CoaX type III pantothenate kinase (molecular player: PSEPK coaX; activity\
    \ or role: pantothenate kinase activity)\n    - Dfp/CoaBC phosphopantothenate--cysteine\
    \ ligase (molecular player: PSEPK dfp; activity or role: phosphopantothenate--cysteine\
    \ ligase activity)\n    - Dfp/CoaBC phosphopantothenoylcysteine decarboxylase\
    \ (molecular player: PSEPK dfp; activity or role: phosphopantothenoylcysteine\
    \ decarboxylase activity)\n    - CoaD phosphopantetheine adenylyltransferase (molecular\
    \ player: PSEPK coaD; activity or role: pantetheine-phosphate adenylyltransferase\
    \ activity)\n    - CoaE dephospho-CoA kinase (molecular player: PSEPK coaE; activity\
    \ or role: dephospho-CoA kinase activity)\n  - 4. beta-alanine supply context\n\
    \  - Beta-alanine metabolism context\n    - PydX/PydA dihydropyrimidine dehydrogenase\
    \ context (molecular player: dihydropyrimidine dehydrogenase (NAD+) activity;\
    \ activity or role: dihydropyrimidine dehydrogenase (NAD+) activity)\n    - PydB\
    \ dihydropyrimidinase context (molecular player: PSEPK pydB; activity or role:\
    \ dihydropyrimidinase activity)\n    - Beta-ureidopropionase context (molecular\
    \ player: beta-ureidopropionase activity; activity or role: beta-ureidopropionase\
    \ activity)\n  - 5. 3-methyl-2-oxobutanoate precursor context\n  - Branched-chain\
    \ amino-acid precursor context\n    - Acetolactate synthase context (molecular\
    \ player: acetolactate synthase activity; activity or role: acetolactate synthase\
    \ activity)\n    - IlvC ketol-acid reductoisomerase context (molecular player:\
    \ PSEPK ilvC; activity or role: ketol-acid reductoisomerase activity)\n    - IlvD\
    \ dihydroxy-acid dehydratase context (molecular player: PSEPK ilvD; activity or\
    \ role: dihydroxy-acid dehydratase activity)\n    - IlvE branched-chain amino-acid\
    \ transaminase context (molecular player: PSEPK ilvE; activity or role: L-valine:2-oxoglutarate\
    \ transaminase activity)\n  - 6. ACP phosphopantetheine and nucleotide boundary\
    \ context\n  - ACP and nucleotide side nodes\n    - PP_0922 ACP phosphodiesterase\
    \ boundary node (molecular player: PSEPK PP_0922; activity or role: [acyl-carrier-protein]\
    \ phosphodiesterase activity)\n    - PP_1183 phosphopantetheinyltransferase boundary\
    \ node (molecular player: PSEPK PP_1183; activity or role: holo-[acyl-carrier-protein]\
    \ synthase activity)\n    - MazG NTP pyrophosphohydrolase boundary node (molecular\
    \ player: PSEPK mazG)"
  module_connections: No explicit connections.
  pathway_query: ppu00770
  pathway_id: ppu00770
  pathway_name: Pantothenate and CoA biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00770 with 10 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '24'
  candidate_genes: '- coaX: PP_0438 | Q88QQ0 | Type III pantothenate kinase (EC 2.7.1.33)
    (PanK-III) (Pantothenic acid kinase) (EC 2.7.1.33; primary bucket kegg:ppu00770)

    - PP_0614: PP_0614 | Q88Q81 | N-carbamoyl-beta-alanine amidohydrolase/allantoine
    amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket
    kegg:ppu00410)

    - coaE: PP_0631 | Q88Q65 | Dephospho-CoA kinase (EC 2.7.1.24) (Dephosphocoenzyme
    A kinase) (EC 2.7.1.24; primary bucket kegg:ppu00770)

    - PP_0922: PP_0922 | Q88PC8 | ACP phosphodiesterase (primary bucket kegg:ppu00770)

    - PP_1157: PP_1157 | Q877U6 | Acetolactate synthase (primary bucket kegg:ppu00660)

    - PP_1183: PP_1183 | Q88NM4 | Enterobactin synthase component D (4''-phosphopantetheinyl
    transferase EntD) (Enterochelin synthase D) (primary bucket kegg:ppu00074)

    - panE: PP_1351 | Q88N64 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate
    reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)

    - PP_1394: PP_1394 | Q88N22 | Acetolactate synthase, large subunit (primary bucket
    kegg:ppu00660)

    - mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8)
    (EC 3.6.1.8; primary bucket kegg:ppu00770)

    - PP_2325: PP_2325 | Q88KG5 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate
    reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)

    - PP_2998: PP_2998 | Q88IK1 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate
    reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)

    - ilvE: PP_3511 | Q88H54 | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42)
    (EC 2.6.1.42; primary bucket kegg:ppu00290)

    - hyuC: PP_4034 | Q88FQ3 | N-carbamoyl-beta-alanine amidohydrolase/allantoine
    amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket
    kegg:ppu00410)

    - pydB: PP_4036 | A0A140FWK2 | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2)
    (EC 3.5.2.2; primary bucket kegg:ppu00410)

    - pydX: PP_4037 | Q88FQ1 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine
    dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)

    - pydA: PP_4038 | Q88FQ0 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine
    dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)

    - ilvC: PP_4678 | Q88DZ0 | Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86)
    (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta-hydroxylacyl reductoisomerase)
    (Ketol-acid reductoisomerase type 1) (Ketol-acid reductoisomerase type I) (EC
    1.1.1.86; primary bucket kegg:ppu00290)

    - ilvH: PP_4679 | Q88DY9 | Acetolactate synthase small subunit (AHAS) (ALS) (EC
    2.2.1.6) (Acetohydroxy-acid synthase small subunit) (EC 2.2.1.6; primary bucket
    kegg:ppu00660)

    - ilvI: PP_4680 | Q88DY8 | Acetolactate synthase (EC 2.2.1.6) (EC 2.2.1.6; primary
    bucket kegg:ppu00660)

    - panB: PP_4699 | Q88DW9 | 3-methyl-2-oxobutanoate hydroxymethyltransferase (EC
    2.1.2.11) (Ketopantoate hydroxymethyltransferase) (KPHMT) (EC 2.1.2.11; primary
    bucket kegg:ppu00770)

    - panC: PP_4700 | Q88DW8 | Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine
    ligase) (Pantoate-activating enzyme) (EC 6.3.2.1; primary bucket kegg:ppu00410)

    - coaD: PP_5123 | Q88CQ7 | Phosphopantetheine adenylyltransferase (EC 2.7.7.3)
    (Dephospho-CoA pyrophosphorylase) (Pantetheine-phosphate adenylyltransferase)
    (PPAT) (EC 2.7.7.3; primary bucket kegg:ppu00770)

    - ilvD: PP_5128 | Q88CQ2 | Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9) (EC 4.2.1.9;
    primary bucket kegg:ppu00290)

    - dfp: PP_5285 | Q88C96 | Coenzyme A biosynthesis bifunctional protein CoaBC (DNA/pantothenate
    metabolism flavoprotein) (Phosphopantothenoylcysteine synthetase/decarboxylase)
    (PPCS-PPCDC) [Includes: Phosphopantothenoylcysteine decarboxylase (PPC decarboxylase)
    (PPC-DC) (EC 4.1.1.36) (CoaC); Phosphopantothenate--cysteine ligase (EC 6.3.2.5)
    (CoaB) (Phosphopantothenoylcysteine synthetase) (PPC synthetase) (PPC-S)] (EC
    4.1.1.36; 6.3.2.5; primary bucket kegg:ppu00770)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__pantothenate_and_coa_biosynthesis__ppu00770-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__pantothenate_and_coa_biosynthesis__ppu00770-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Pantothenate and CoA biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00770
- Resolved ID: ppu00770
- Resolved name: Pantothenate and CoA biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00770 with 10 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 24

- coaX: PP_0438 | Q88QQ0 | Type III pantothenate kinase (EC 2.7.1.33) (PanK-III) (Pantothenic acid kinase) (EC 2.7.1.33; primary bucket kegg:ppu00770)
- PP_0614: PP_0614 | Q88Q81 | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket kegg:ppu00410)
- coaE: PP_0631 | Q88Q65 | Dephospho-CoA kinase (EC 2.7.1.24) (Dephosphocoenzyme A kinase) (EC 2.7.1.24; primary bucket kegg:ppu00770)
- PP_0922: PP_0922 | Q88PC8 | ACP phosphodiesterase (primary bucket kegg:ppu00770)
- PP_1157: PP_1157 | Q877U6 | Acetolactate synthase (primary bucket kegg:ppu00660)
- PP_1183: PP_1183 | Q88NM4 | Enterobactin synthase component D (4'-phosphopantetheinyl transferase EntD) (Enterochelin synthase D) (primary bucket kegg:ppu00074)
- panE: PP_1351 | Q88N64 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)
- PP_1394: PP_1394 | Q88N22 | Acetolactate synthase, large subunit (primary bucket kegg:ppu00660)
- mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) (EC 3.6.1.8; primary bucket kegg:ppu00770)
- PP_2325: PP_2325 | Q88KG5 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)
- PP_2998: PP_2998 | Q88IK1 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)
- ilvE: PP_3511 | Q88H54 | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42) (EC 2.6.1.42; primary bucket kegg:ppu00290)
- hyuC: PP_4034 | Q88FQ3 | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket kegg:ppu00410)
- pydB: PP_4036 | A0A140FWK2 | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2) (EC 3.5.2.2; primary bucket kegg:ppu00410)
- pydX: PP_4037 | Q88FQ1 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)
- pydA: PP_4038 | Q88FQ0 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)
- ilvC: PP_4678 | Q88DZ0 | Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86) (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta-hydroxylacyl reductoisomerase) (Ketol-acid reductoisomerase type 1) (Ketol-acid reductoisomerase type I) (EC 1.1.1.86; primary bucket kegg:ppu00290)
- ilvH: PP_4679 | Q88DY9 | Acetolactate synthase small subunit (AHAS) (ALS) (EC 2.2.1.6) (Acetohydroxy-acid synthase small subunit) (EC 2.2.1.6; primary bucket kegg:ppu00660)
- ilvI: PP_4680 | Q88DY8 | Acetolactate synthase (EC 2.2.1.6) (EC 2.2.1.6; primary bucket kegg:ppu00660)
- panB: PP_4699 | Q88DW9 | 3-methyl-2-oxobutanoate hydroxymethyltransferase (EC 2.1.2.11) (Ketopantoate hydroxymethyltransferase) (KPHMT) (EC 2.1.2.11; primary bucket kegg:ppu00770)
- panC: PP_4700 | Q88DW8 | Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine ligase) (Pantoate-activating enzyme) (EC 6.3.2.1; primary bucket kegg:ppu00410)
- coaD: PP_5123 | Q88CQ7 | Phosphopantetheine adenylyltransferase (EC 2.7.7.3) (Dephospho-CoA pyrophosphorylase) (Pantetheine-phosphate adenylyltransferase) (PPAT) (EC 2.7.7.3; primary bucket kegg:ppu00770)
- ilvD: PP_5128 | Q88CQ2 | Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9) (EC 4.2.1.9; primary bucket kegg:ppu00290)
- dfp: PP_5285 | Q88C96 | Coenzyme A biosynthesis bifunctional protein CoaBC (DNA/pantothenate metabolism flavoprotein) (Phosphopantothenoylcysteine synthetase/decarboxylase) (PPCS-PPCDC) [Includes: Phosphopantothenoylcysteine decarboxylase (PPC decarboxylase) (PPC-DC) (EC 4.1.1.36) (CoaC); Phosphopantothenate--cysteine ligase (EC 6.3.2.5) (CoaB) (Phosphopantothenoylcysteine synthetase) (PPC synthetase) (PPC-S)] (EC 4.1.1.36; 6.3.2.5; primary bucket kegg:ppu00770)

## Generic Module Context

### Working Scope

A bacterial pantothenate and coenzyme A biosynthesis module covering formation of pantoate from 3-methyl-2-oxobutanoate, ligation with beta-alanine to form pantothenate, and conversion of pantothenate through phosphopantothenate, phosphopantothenoylcysteine, phosphopantetheine, and dephospho-CoA to CoA. In Pseudomonas putida KT2440, KEGG ppu00770 also includes branched-chain amino-acid precursor enzymes, pyrimidine/beta-alanine metabolism, ACP phosphopantetheine handling, and nucleotide hydrolase side nodes; these are tracked as precursor or boundary context unless they directly form pantothenate or CoA.

### Provisional Biological Outline

- Pantothenate and CoA biosynthesis
  - 1. pantoate branch of pantothenate biosynthesis
  - 3-methyl-2-oxobutanoate to pantoate
    - PanB ketopantoate hydroxymethyltransferase (molecular player: PSEPK panB; activity or role: 3-methyl-2-oxobutanoate hydroxymethyltransferase activity)
    - PanE 2-dehydropantoate reductase (molecular player: PSEPK panE; activity or role: 2-dehydropantoate 2-reductase activity)
    - PP_2325 2-dehydropantoate reductase candidate (molecular player: PSEPK PP_2325; activity or role: 2-dehydropantoate 2-reductase activity)
    - PP_2998 2-dehydropantoate reductase candidate (molecular player: PSEPK PP_2998; activity or role: 2-dehydropantoate 2-reductase activity)
    - PP_4452 2-dehydropantoate reductase candidate (molecular player: PSEPK PP_4452; activity or role: 2-dehydropantoate 2-reductase activity)
  - 2. pantothenate synthetase
  - Pantoate plus beta-alanine to pantothenate
    - PanC pantothenate synthetase (molecular player: PSEPK panC; activity or role: pantoate-beta-alanine ligase activity)
  - 3. pantothenate to coenzyme A
  - Pantothenate to CoA
    - CoaX type III pantothenate kinase (molecular player: PSEPK coaX; activity or role: pantothenate kinase activity)
    - Dfp/CoaBC phosphopantothenate--cysteine ligase (molecular player: PSEPK dfp; activity or role: phosphopantothenate--cysteine ligase activity)
    - Dfp/CoaBC phosphopantothenoylcysteine decarboxylase (molecular player: PSEPK dfp; activity or role: phosphopantothenoylcysteine decarboxylase activity)
    - CoaD phosphopantetheine adenylyltransferase (molecular player: PSEPK coaD; activity or role: pantetheine-phosphate adenylyltransferase activity)
    - CoaE dephospho-CoA kinase (molecular player: PSEPK coaE; activity or role: dephospho-CoA kinase activity)
  - 4. beta-alanine supply context
  - Beta-alanine metabolism context
    - PydX/PydA dihydropyrimidine dehydrogenase context (molecular player: dihydropyrimidine dehydrogenase (NAD+) activity; activity or role: dihydropyrimidine dehydrogenase (NAD+) activity)
    - PydB dihydropyrimidinase context (molecular player: PSEPK pydB; activity or role: dihydropyrimidinase activity)
    - Beta-ureidopropionase context (molecular player: beta-ureidopropionase activity; activity or role: beta-ureidopropionase activity)
  - 5. 3-methyl-2-oxobutanoate precursor context
  - Branched-chain amino-acid precursor context
    - Acetolactate synthase context (molecular player: acetolactate synthase activity; activity or role: acetolactate synthase activity)
    - IlvC ketol-acid reductoisomerase context (molecular player: PSEPK ilvC; activity or role: ketol-acid reductoisomerase activity)
    - IlvD dihydroxy-acid dehydratase context (molecular player: PSEPK ilvD; activity or role: dihydroxy-acid dehydratase activity)
    - IlvE branched-chain amino-acid transaminase context (molecular player: PSEPK ilvE; activity or role: L-valine:2-oxoglutarate transaminase activity)
  - 6. ACP phosphopantetheine and nucleotide boundary context
  - ACP and nucleotide side nodes
    - PP_0922 ACP phosphodiesterase boundary node (molecular player: PSEPK PP_0922; activity or role: [acyl-carrier-protein] phosphodiesterase activity)
    - PP_1183 phosphopantetheinyltransferase boundary node (molecular player: PSEPK PP_1183; activity or role: holo-[acyl-carrier-protein] synthase activity)
    - MazG NTP pyrophosphohydrolase boundary node (molecular player: PSEPK mazG)

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

Pantothenate and CoA biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00770
- Resolved ID: ppu00770
- Resolved name: Pantothenate and CoA biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00770 with 10 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 24

- coaX: PP_0438 | Q88QQ0 | Type III pantothenate kinase (EC 2.7.1.33) (PanK-III) (Pantothenic acid kinase) (EC 2.7.1.33; primary bucket kegg:ppu00770)
- PP_0614: PP_0614 | Q88Q81 | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket kegg:ppu00410)
- coaE: PP_0631 | Q88Q65 | Dephospho-CoA kinase (EC 2.7.1.24) (Dephosphocoenzyme A kinase) (EC 2.7.1.24; primary bucket kegg:ppu00770)
- PP_0922: PP_0922 | Q88PC8 | ACP phosphodiesterase (primary bucket kegg:ppu00770)
- PP_1157: PP_1157 | Q877U6 | Acetolactate synthase (primary bucket kegg:ppu00660)
- PP_1183: PP_1183 | Q88NM4 | Enterobactin synthase component D (4'-phosphopantetheinyl transferase EntD) (Enterochelin synthase D) (primary bucket kegg:ppu00074)
- panE: PP_1351 | Q88N64 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)
- PP_1394: PP_1394 | Q88N22 | Acetolactate synthase, large subunit (primary bucket kegg:ppu00660)
- mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) (EC 3.6.1.8; primary bucket kegg:ppu00770)
- PP_2325: PP_2325 | Q88KG5 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)
- PP_2998: PP_2998 | Q88IK1 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)
- ilvE: PP_3511 | Q88H54 | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42) (EC 2.6.1.42; primary bucket kegg:ppu00290)
- hyuC: PP_4034 | Q88FQ3 | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket kegg:ppu00410)
- pydB: PP_4036 | A0A140FWK2 | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2) (EC 3.5.2.2; primary bucket kegg:ppu00410)
- pydX: PP_4037 | Q88FQ1 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)
- pydA: PP_4038 | Q88FQ0 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)
- ilvC: PP_4678 | Q88DZ0 | Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86) (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta-hydroxylacyl reductoisomerase) (Ketol-acid reductoisomerase type 1) (Ketol-acid reductoisomerase type I) (EC 1.1.1.86; primary bucket kegg:ppu00290)
- ilvH: PP_4679 | Q88DY9 | Acetolactate synthase small subunit (AHAS) (ALS) (EC 2.2.1.6) (Acetohydroxy-acid synthase small subunit) (EC 2.2.1.6; primary bucket kegg:ppu00660)
- ilvI: PP_4680 | Q88DY8 | Acetolactate synthase (EC 2.2.1.6) (EC 2.2.1.6; primary bucket kegg:ppu00660)
- panB: PP_4699 | Q88DW9 | 3-methyl-2-oxobutanoate hydroxymethyltransferase (EC 2.1.2.11) (Ketopantoate hydroxymethyltransferase) (KPHMT) (EC 2.1.2.11; primary bucket kegg:ppu00770)
- panC: PP_4700 | Q88DW8 | Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine ligase) (Pantoate-activating enzyme) (EC 6.3.2.1; primary bucket kegg:ppu00410)
- coaD: PP_5123 | Q88CQ7 | Phosphopantetheine adenylyltransferase (EC 2.7.7.3) (Dephospho-CoA pyrophosphorylase) (Pantetheine-phosphate adenylyltransferase) (PPAT) (EC 2.7.7.3; primary bucket kegg:ppu00770)
- ilvD: PP_5128 | Q88CQ2 | Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9) (EC 4.2.1.9; primary bucket kegg:ppu00290)
- dfp: PP_5285 | Q88C96 | Coenzyme A biosynthesis bifunctional protein CoaBC (DNA/pantothenate metabolism flavoprotein) (Phosphopantothenoylcysteine synthetase/decarboxylase) (PPCS-PPCDC) [Includes: Phosphopantothenoylcysteine decarboxylase (PPC decarboxylase) (PPC-DC) (EC 4.1.1.36) (CoaC); Phosphopantothenate--cysteine ligase (EC 6.3.2.5) (CoaB) (Phosphopantothenoylcysteine synthetase) (PPC synthetase) (PPC-S)] (EC 4.1.1.36; 6.3.2.5; primary bucket kegg:ppu00770)

## Generic Module Context

### Working Scope

A bacterial pantothenate and coenzyme A biosynthesis module covering formation of pantoate from 3-methyl-2-oxobutanoate, ligation with beta-alanine to form pantothenate, and conversion of pantothenate through phosphopantothenate, phosphopantothenoylcysteine, phosphopantetheine, and dephospho-CoA to CoA. In Pseudomonas putida KT2440, KEGG ppu00770 also includes branched-chain amino-acid precursor enzymes, pyrimidine/beta-alanine metabolism, ACP phosphopantetheine handling, and nucleotide hydrolase side nodes; these are tracked as precursor or boundary context unless they directly form pantothenate or CoA.

### Provisional Biological Outline

- Pantothenate and CoA biosynthesis
  - 1. pantoate branch of pantothenate biosynthesis
  - 3-methyl-2-oxobutanoate to pantoate
    - PanB ketopantoate hydroxymethyltransferase (molecular player: PSEPK panB; activity or role: 3-methyl-2-oxobutanoate hydroxymethyltransferase activity)
    - PanE 2-dehydropantoate reductase (molecular player: PSEPK panE; activity or role: 2-dehydropantoate 2-reductase activity)
    - PP_2325 2-dehydropantoate reductase candidate (molecular player: PSEPK PP_2325; activity or role: 2-dehydropantoate 2-reductase activity)
    - PP_2998 2-dehydropantoate reductase candidate (molecular player: PSEPK PP_2998; activity or role: 2-dehydropantoate 2-reductase activity)
    - PP_4452 2-dehydropantoate reductase candidate (molecular player: PSEPK PP_4452; activity or role: 2-dehydropantoate 2-reductase activity)
  - 2. pantothenate synthetase
  - Pantoate plus beta-alanine to pantothenate
    - PanC pantothenate synthetase (molecular player: PSEPK panC; activity or role: pantoate-beta-alanine ligase activity)
  - 3. pantothenate to coenzyme A
  - Pantothenate to CoA
    - CoaX type III pantothenate kinase (molecular player: PSEPK coaX; activity or role: pantothenate kinase activity)
    - Dfp/CoaBC phosphopantothenate--cysteine ligase (molecular player: PSEPK dfp; activity or role: phosphopantothenate--cysteine ligase activity)
    - Dfp/CoaBC phosphopantothenoylcysteine decarboxylase (molecular player: PSEPK dfp; activity or role: phosphopantothenoylcysteine decarboxylase activity)
    - CoaD phosphopantetheine adenylyltransferase (molecular player: PSEPK coaD; activity or role: pantetheine-phosphate adenylyltransferase activity)
    - CoaE dephospho-CoA kinase (molecular player: PSEPK coaE; activity or role: dephospho-CoA kinase activity)
  - 4. beta-alanine supply context
  - Beta-alanine metabolism context
    - PydX/PydA dihydropyrimidine dehydrogenase context (molecular player: dihydropyrimidine dehydrogenase (NAD+) activity; activity or role: dihydropyrimidine dehydrogenase (NAD+) activity)
    - PydB dihydropyrimidinase context (molecular player: PSEPK pydB; activity or role: dihydropyrimidinase activity)
    - Beta-ureidopropionase context (molecular player: beta-ureidopropionase activity; activity or role: beta-ureidopropionase activity)
  - 5. 3-methyl-2-oxobutanoate precursor context
  - Branched-chain amino-acid precursor context
    - Acetolactate synthase context (molecular player: acetolactate synthase activity; activity or role: acetolactate synthase activity)
    - IlvC ketol-acid reductoisomerase context (molecular player: PSEPK ilvC; activity or role: ketol-acid reductoisomerase activity)
    - IlvD dihydroxy-acid dehydratase context (molecular player: PSEPK ilvD; activity or role: dihydroxy-acid dehydratase activity)
    - IlvE branched-chain amino-acid transaminase context (molecular player: PSEPK ilvE; activity or role: L-valine:2-oxoglutarate transaminase activity)
  - 6. ACP phosphopantetheine and nucleotide boundary context
  - ACP and nucleotide side nodes
    - PP_0922 ACP phosphodiesterase boundary node (molecular player: PSEPK PP_0922; activity or role: [acyl-carrier-protein] phosphodiesterase activity)
    - PP_1183 phosphopantetheinyltransferase boundary node (molecular player: PSEPK PP_1183; activity or role: holo-[acyl-carrier-protein] synthase activity)
    - MazG NTP pyrophosphohydrolase boundary node (molecular player: PSEPK mazG)

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

# Pantothenate and CoA Biosynthesis in *Pseudomonas putida* KT2440: Species-Aware Module Review

## 1. Executive Summary

This review assesses the pantothenate and coenzyme A (CoA) biosynthesis module (KEGG ppu00770) in *Pseudomonas putida* KT2440 (NCBI taxon 160488, proteome UP000000556). The module encompasses the de novo synthesis of pantothenate (vitamin B5) from pantoate and β-alanine, followed by the five-step enzymatic conversion of pantothenate to CoA. Of the 24 candidate genes identified from local metadata, 7 map to the core pantothenate-to-CoA pathway, and a further 2 (panB, panC) catalyze pantothenate assembly. The remaining 15 candidates represent precursor-supply context (branched-chain amino acid pathway, pyrimidine reductive catabolism) or boundary nodes (ACP phosphopantetheine handling, nucleotide hydrolases) that should be tracked separately.

The strongest species-specific evidence exists for coaX/PpcoaA (PP_0438), whose gene product was cloned from KT2440 and shown to function as a type III pantothenate kinase when heterologously expressed (hou2019isolatingpromotersfrom pages 8-9, hou2019isolatingpromotersfrom pages 4-7). The five downstream CoA biosynthetic steps (CoaX → CoaBC/dfp → CoaD → CoaE) are all genetically encoded and annotated with high confidence by homology, though none has been biochemically characterized directly in KT2440. A notable finding is that *P. putida* KT2440 lacks the canonical panD (aspartate 1-decarboxylase) for β-alanine synthesis and instead relies on pyrimidine reductive catabolism (pydA, pydX, pydB, hyuC) to supply this precursor (schmidt2022nitrogenmetabolismin pages 12-15, perchat2022characterizationofa pages 1-2). This has implications for module boundary definitions. Additionally, the presence of multiple putative ketopantoate reductase paralogs (panE, PP_2325, PP_2998) and the established ability of IlvC to compensate for PanE function create paralog ambiguity that warrants attention (leonardi2007biosynthesisofpantothenic pages 2-4).

## 2. Target-Organism Pathway Definition

### 2.1 Pathway Boundaries

The pantothenate and CoA biosynthesis module in *P. putida* KT2440 includes:

**Core pantothenate synthesis:** Conversion of 3-methyl-2-oxobutanoate (α-ketoisovalerate) to pantoate via ketopantoate hydroxymethyltransferase (PanB, EC 2.1.2.11) and 2-dehydropantoate reductase (PanE, EC 1.1.1.169), followed by condensation with β-alanine to form pantothenate by pantothenate synthetase (PanC, EC 6.3.2.1) (leonardi2007biosynthesisofpantothenic pages 2-4).

**Core CoA biosynthesis (5 steps):** (i) Phosphorylation of pantothenate by type III pantothenate kinase CoaX (EC 2.7.1.33); (ii–iii) condensation with cysteine and decarboxylation by bifunctional CoaBC/Dfp (EC 6.3.2.5 and 4.1.1.36); (iv) adenylylation by CoaD/PPAT (EC 2.7.7.3); (v) phosphorylation by CoaE/DPCK (EC 2.7.1.24) (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 6-8, leonardi2007biosynthesisofpantothenic pages 1-2).

**Neighboring pathways to keep separate:** KEGG ppu00770 also maps branched-chain amino acid (BCAA) biosynthesis enzymes (ilvC, ilvD, ilvE, ilvH, ilvI, acetolactate synthases), pyrimidine degradation genes (pydA, pydX, pydB, hyuC), and ACP modification enzymes (PP_0922, PP_1183). These should be maintained as precursor-supply or boundary context rather than core module components.

### 2.2 Alternate Names and Database Definitions

The pathway is also known as "vitamin B5 biosynthesis" (pantothenate portion) and "CoA biosynthetic process" (GO:0015937). In KEGG, ppu00770 aggregates both pantothenate synthesis and CoA assembly; MetaCyc separates these into distinct pathways (PWY-4221 for pantothenate biosynthesis and PWY-5337 for the universal CoA pathway from pantothenate). The KEGG map's inclusion of BCAA and pyrimidine degradation genes reflects shared precursor nodes rather than unified pathway membership.

## 3. Expected Step Model

The following table summarizes the step-by-step satisfiability assessment for pantothenate and CoA biosynthesis in *P. putida* KT2440:

| Step number | Pathway step name | EC number | Expected gene(s) | Coverage status | Notes |
|---|---|---|---|---|---|
| 1 | 3-methyl-2-oxobutanoate to 2-dehydropantoate | 2.1.2.11 | panB (PP_4699) | covered | Canonical ketopantoate hydroxymethyltransferase assignment is strong in KT2440 by annotation and pathway conservation; no direct KT2440 biochemistry found, but this is the best-supported core gene for the step (leonardi2007biosynthesisofpantothenic pages 2-4, belda2016therevisitedgenome pages 1-2) |
| 2 | 2-dehydropantoate to pantoate | 1.1.1.169 | panE (PP_1351); possible backup by ilvC (PP_4678); PP_2325/PP_2998 uncertain | candidate_uncertain | PanE is the expected assignment, but ketopantoate reduction is often redundant in bacteria and IlvC can substitute for PanE chemistry; multiple PanE-like annotations in KT2440 create paralog ambiguity (leonardi2007biosynthesisofpantothenic pages 2-4, nitschel2020engineeringpseudomonasputida pages 1-2, batianis2023atunablemetabolic pages 6-7) |
| 3 | Beta-alanine supply | — | Not PanD; pyrimidine degradation genes pydA/pydX (PP_4038/PP_4037), pydB (PP_4036), hyuC (PP_4034), possibly PP_0614 | module_needs_revision | KT2440 appears to use pyrimidine reductive catabolism rather than the canonical PanD aspartate decarboxylase route. This feeder function is present, but the generic module should not expect PanD here; beta-alanine supply should be represented as species-specific context or alternative step (schmidt2022nitrogenmetabolismin pages 12-15, perchat2022characterizationofa pages 1-2) |
| 4 | Pantoate + beta-alanine to pantothenate | 6.3.2.1 | panC (PP_4700) | covered | PanC is the canonical pantothenate synthetase. However, a KT2440 panC mutant reportedly was not auxotrophic on minimal medium, indicating physiological redundancy, salvage, or a boundary problem in the mutant assay rather than clear absence of the step (molina‐henares2010identificationofconditionally pages 4-6, molina‐henares2010identificationofconditionally pages 12-13) |
| 5 | Pantothenate to 4'-phosphopantothenate | 2.7.1.33 | coaX / PpcoaA (PP_0438) | covered | Strongest species-linked core step: KT2440 PpcoaA was cloned and overexpressed heterologously, increasing CoA production about 4.1-4.4-fold; assignment to type III PanK is also consistent with broader structural literature on CoaX enzymes (hou2019isolatingpromotersfrom pages 8-9, hou2019isolatingpromotersfrom pages 4-7, leonardi2007biosynthesisofpantothenic pages 8-9) |
| 6 | 4'-phosphopantothenate to 4'-phosphopantothenoylcysteine | 6.3.2.5 | dfp / coaBC (PP_5285), CoaB domain | covered | Standard bacterial CoaBC architecture fits the KT2440 annotation well; no species-specific biochemical paper found, but homology support is strong (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 8-9) |
| 7 | 4'-phosphopantothenoylcysteine to 4'-phosphopantetheine | 4.1.1.36 | dfp / coaBC (PP_5285), CoaC domain | covered | Same bifunctional Dfp/CoaBC protein is expected to catalyze this decarboxylation step; strong conserved-pathway inference (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 8-9) |
| 8 | 4'-phosphopantetheine to dephospho-CoA | 2.7.7.3 | coaD (PP_5123) | covered | Canonical phosphopantetheine adenylyltransferase assignment; no direct KT2440 enzyme study found, but this is a routine conserved CoA-pathway step (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 6-8) |
| 9 | Dephospho-CoA to CoA | 2.7.1.24 | coaE (PP_0631) | covered | Canonical dephospho-CoA kinase assignment; conserved and well aligned with bacterial pathway expectations (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 6-8) |
| 10 | ACP phosphopantetheine transfer (boundary) | 2.7.8.- / PPTase class | PP_1183 (EntD-like phosphopantetheinyl transferase) | not_expected_in_target_taxon | This is a boundary/side-node process involving transfer of the 4'-phosphopantetheine moiety onto carrier proteins, not a de novo pantothenate/CoA biosynthesis step; should be excluded from core satisfiability (leonardi2007biosynthesisofpantothenic pages 9-10) |
| 11 | ACP phosphopantetheine removal (boundary) | 3.1.4.- | PP_0922 (AcpH-like ACP phosphodiesterase) | not_expected_in_target_taxon | ACP phosphodiesterase belongs to phosphopantetheine recycling or ACP remodeling, not de novo pantothenate/CoA synthesis; inclusion on KEGG map is boundary noise for this module (leonardi2007biosynthesisofpantothenic pages 9-10) |


*Table: This table summarizes step-by-step coverage for pantothenate and CoA biosynthesis in Pseudomonas putida KT2440, distinguishing core covered reactions from uncertain or boundary steps. It is useful for module satisfiability decisions and for identifying where the generic pathway model needs species-aware revision.*

### 3.1 Key Observations on the Step Model

**Type III PanK replaces Type I:** Unlike *Escherichia coli*, which uses a type I pantothenate kinase (CoaA) subject to competitive feedback inhibition by CoA, *P. putida* KT2440 encodes a type III pantothenate kinase (CoaX/PP_0438). Type III PanK enzymes belong to the ASKHA (Acetate and Sugar Kinase/Hsc70/Actin) superfamily and are structurally distinct from type I enzymes (nicely2007structureofthe pages 1-2, nicely2007structureofthe pages 5-7). Crucially, type III PanKs are refractory to feedback inhibition by free CoA or CoA thioesters, which allows organisms to accumulate higher intracellular CoA levels (leonardi2007biosynthesisofpantothenic pages 8-9, nicely2007structureofthe pages 9-10). This property has been exploited in metabolic engineering: the PpcoaA gene from KT2440, when overexpressed under a strong promoter in *Corynebacterium ammoniagenes*, increased CoA production approximately 4.1–4.4-fold (hou2019isolatingpromotersfrom pages 4-7).

**β-Alanine supply via pyrimidine degradation:** *P. putida* KT2440 lacks panD, the canonical aspartate 1-decarboxylase used for β-alanine synthesis in *E. coli* and *Salmonella* (perchat2022characterizationofa pages 1-2). Instead, β-alanine is derived from the reductive pyrimidine degradation pathway: uracil → dihydrouracil (pydA/pydX, PP_4038/PP_4037) → N-carbamoyl-β-alanine (pydB, PP_4036) → β-alanine (hyuC, PP_4034 or PP_0614) (schmidt2022nitrogenmetabolismin pages 12-15). RB-TnSeq fitness data in *P. putida* KT2440 have confirmed the functional involvement of PP_4036, PP_4037-4038, and PP_4034 in pyrimidine degradation under nitrogen-limiting conditions (schmidt2022nitrogenmetabolismin pages 12-15).

**Pantothenate pathway redundancy:** Genome-wide mutant library screening of *P. putida* KT2440 found that neither panB (PP_4699) nor panC (PP_4700) knockout mutants displayed pantothenate auxotrophy on minimal medium, despite *in silico* model predictions that these genes should be conditionally essential (molina‐henares2010identificationofconditionally pages 4-6, molina‐henares2010identificationofconditionally pages 12-13). This suggests either metabolic bypass, salvage of pantothenate from complex medium contaminants, or functional redundancy at the pantoate/β-alanine supply level.

## 4. Candidate Genes and Evidence

The comprehensive assessment of all 24 candidate genes is presented below:

| Pathway section | Gene | Locus tag | UniProt ID | Assigned pathway step | Evidence type | Confidence | Module status | Key caveats |
|---|---|---|---|---|---|---|---|---|
| Pantoate branch | panB | PP_4699 | Q88DW9 | Ketopantoate hydroxymethyltransferase; 3-methyl-2-oxobutanoate → 2-dehydropantoate | Computational prediction in KT2440; pathway-consistent homology inference | High | covered | Strong canonical assignment, but direct biochemical validation in KT2440 not found; panB mutants were predicted auxotrophic yet not recovered as pantothenate auxotrophs in a mutant screen, suggesting pathway redundancy or bypass at module level (molina‐henares2010identificationofconditionally pages 4-6, molina‐henares2010identificationofconditionally pages 2-3, belda2016therevisitedgenome pages 1-2) |
| Pantoate branch | panE | PP_1351 | Q88N64 | 2-dehydropantoate reductase; 2-dehydropantoate → pantoate | Computational prediction; homology inference | Medium | candidate_uncertain | Canonical enzyme assignment is plausible, but PanE can be functionally replaced by IlvC in bacteria; lack of pantothenate auxotrophy in KT2440 panC/panB-related analyses argues caution about assigning sole responsibility (leonardi2007biosynthesisofpantothenic pages 2-4, molina‐henares2010identificationofconditionally pages 4-6) |
| Pantoate branch | PP_2325 | PP_2325 | Q88KG5 | Alternative 2-dehydropantoate reductase candidate | Computational prediction only | Low | candidate_uncertain | Annotated as PanE-like, but no species-specific evidence located; may represent over-propagated oxidoreductase annotation rather than bona fide pantothenate synthesis enzyme (belda2016therevisitedgenome pages 1-2) |
| Pantoate branch | PP_2998 | PP_2998 | Q88IK1 | Alternative 2-dehydropantoate reductase candidate | Computational prediction only | Low | candidate_uncertain | Same caveat as PP_2325; no direct evidence for role in pantothenate synthesis in KT2440 (belda2016therevisitedgenome pages 1-2) |
| Pantothenate synthetase | panC | PP_4700 | Q88DW8 | Pantothenate synthetase; pantoate + β-alanine → pantothenate | Computational prediction in KT2440; mutant phenotype tested in P. putida | High | covered | panC is the canonical enzyme, but a KT2440 panC knockout was reported as not auxotrophic on minimal medium, implying metabolic redundancy, scavenging, or model/annotation issues; pathway step likely present but biological implementation may be non-canonical in vivo (molina‐henares2010identificationofconditionally pages 4-6, molina‐henares2010identificationofconditionally pages 12-13) |
| CoA biosynthesis steps | coaX | PP_0438 | Q88QQ0 | Type III pantothenate kinase; pantothenate → 4′-phosphopantothenate | Heterologous expression of KT2440 gene; strong homology to type III PanK family | High | covered | Best-supported core step in KT2440 candidate set: PpcoaA from KT2440 increased CoA production ~4.1-4.4-fold when overexpressed in C. ammoniagenes; assignment to type III PanK also fits broader bacterial structural literature (hou2019isolatingpromotersfrom pages 8-9, hou2019isolatingpromotersfrom pages 4-7, leonardi2007biosynthesisofpantothenic pages 8-9) |
| CoA biosynthesis steps | dfp (CoaBC) | PP_5285 | Q88C96 | Bifunctional phosphopantothenoylcysteine synthetase/decarboxylase; 4′-phosphopantothenate → 4′-phosphopantetheine | Homology inference; canonical bacterial pathway logic | High | covered | No direct KT2440 experiment found, but bifunctional coaBC/dfp architecture is standard in bacteria and matches annotation well (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 8-9) |
| CoA biosynthesis steps | coaD | PP_5123 | Q88CQ7 | Phosphopantetheine adenylyltransferase; 4′-phosphopantetheine → dephospho-CoA | Homology inference; canonical bacterial pathway logic | High | covered | No KT2440-specific biochemical study found; annotation matches conserved essential CoA pathway step (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 6-8) |
| CoA biosynthesis steps | coaE | PP_0631 | Q88Q65 | Dephospho-CoA kinase; dephospho-CoA → CoA | Homology inference; canonical bacterial pathway logic | High | covered | No KT2440 direct assay located, but function is highly conserved and annotation is straightforward (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 6-8) |
| Beta-alanine supply context | hyuC | PP_4034 | Q88FQ3 | β-ureidopropionase/allantoinase-like amidase; downstream pyrimidine reductive catabolism feeding β-alanine | Direct functional genomics in KT2440 (RB-TnSeq) for pyrimidine degradation context | Medium | not_core | Strongly supported as pyrimidine catabolism context gene, but exact β-alanine-producing step assignment remains somewhat broad because PP_0614 is a paralog and pathway naming varies (schmidt2022nitrogenmetabolismin pages 12-15) |
| Beta-alanine supply context | PP_0614 | PP_0614 | Q88Q81 | Paralogue amidase candidate in pyrimidine reductive catabolism | Computational prediction plus indirect functional inference from paralogy | Low | not_core | Likely redundant with hyuC rather than core pantothenate gene; no direct KT2440 evidence for this paralog in β-alanine supply (schmidt2022nitrogenmetabolismin pages 12-15) |
| Beta-alanine supply context | pydB | PP_4036 | A0A140FWK2 | Dihydropyrimidinase; ring opening in pyrimidine reductive catabolism feeding β-alanine | Direct functional genomics in KT2440 (RB-TnSeq) | High | not_core | Well supported as pyrimidine degradation enzyme in KT2440; important for β-alanine supply context because KT2440 appears to rely on uracil degradation rather than PanD-type aspartate decarboxylase (schmidt2022nitrogenmetabolismin pages 12-15, perchat2022characterizationofa pages 1-2) |
| Beta-alanine supply context | pydX | PP_4037 | Q88FQ1 | Dihydropyrimidine dehydrogenase subunit/candidate; uracil → dihydrouracil | Direct functional genomics in KT2440 (RB-TnSeq) | Medium | not_core | RB-TnSeq supports PP_4037-4038 locus in pyrimidine degradation, but exact subunit naming/order remains annotation-sensitive (schmidt2022nitrogenmetabolismin pages 12-15) |
| Beta-alanine supply context | pydA | PP_4038 | Q88FQ0 | Dihydropyrimidine dehydrogenase subunit/candidate; uracil → dihydrouracil | Direct functional genomics in KT2440 (RB-TnSeq) | Medium | not_core | As with PP_4037, likely part of pyrimidine reductive catabolism supplying β-alanine indirectly; not a core pantothenate enzyme (schmidt2022nitrogenmetabolismin pages 12-15) |
| BCAA precursor context | PP_1157 | PP_1157 | Q877U6 | Acetolactate synthase candidate; upstream provision of 3-methyl-2-oxobutanoate | Computational prediction only | Low | not_core | Candidate is less compelling than ilvHI/ilvI system; likely peripheral or condition-specific paralog (belda2016therevisitedgenome pages 1-2) |
| BCAA precursor context | PP_1394 | PP_1394 | Q88N22 | Acetolactate synthase large subunit candidate; upstream provision of 3-methyl-2-oxobutanoate | Computational prediction only | Low | not_core | Similar caveat as PP_1157; no direct evidence tying this paralog to pantothenate precursor supply in KT2440 (belda2016therevisitedgenome pages 1-2) |
| BCAA precursor context | ilvC | PP_4678 | Q88DZ0 | Ketol-acid reductoisomerase in BCAA synthesis; can substitute for PanE-like chemistry | Direct experimental support in KT2440 via engineering studies; broad biochemical literature | High | not_core | Definitely functional in KT2440 BCAA/2-KIV metabolism; may partially compensate pantoate branch reduction, which complicates PanE curation; should not replace panE automatically as primary pantothenate annotation without direct test (nitschel2020engineeringpseudomonasputida pages 1-2, nitschel2020engineeringpseudomonasputida pages 7-8, batianis2023atunablemetabolic pages 6-7, leonardi2007biosynthesisofpantothenic pages 2-4) |
| BCAA precursor context | ilvH | PP_4679 | Q88DY9 | Acetolactate synthase small subunit; upstream provision of 3-methyl-2-oxobutanoate | Direct/indirect support from KT2440 metabolic engineering context | Medium | not_core | Included as precursor-supply context only; KEGG placement near pantothenate reflects shared precursor chemistry rather than pathway membership (batianis2023atunablemetabolic pages 6-7) |
| BCAA precursor context | ilvI | PP_4680 | Q88DY8 | Acetolactate synthase catalytic subunit; upstream provision of 3-methyl-2-oxobutanoate | Homology inference with KT2440 pathway context | Medium | not_core | Likely the main native acetolactate synthase route feeding valine/2-KIV, but evidence gathered was stronger for pathway-level function than gene-specific biochemical proof (batianis2023atunablemetabolic pages 6-7) |
| BCAA precursor context | ilvD | PP_5128 | Q88CQ2 | Dihydroxy-acid dehydratase in BCAA synthesis; supplies 2-ketoisovalerate precursor pool | Direct experimental support in KT2440 via engineering studies | High | not_core | Strong support for native BCAA precursor function in KT2440; not a pantothenate enzyme per se (nitschel2020engineeringpseudomonasputida pages 1-2, nitschel2020engineeringpseudomonasputida pages 7-8, batianis2023atunablemetabolic pages 6-7) |
| BCAA precursor context | ilvE | PP_3511 | Q88H54 | Branched-chain amino acid aminotransferase; consumes 2-ketoisovalerate to valine | Homology inference; pathway context from related Pseudomonas engineering | Medium | not_core | Context gene only; mechanistically adjacent because it competes for 2-KIV, but not part of pantothenate/CoA biosynthesis proper (lang2014metabolicengineeringof pages 6-7) |
| ACP/nucleotide boundary nodes | PP_0922 | PP_0922 | Q88PC8 | ACP phosphodiesterase (AcpH-like); holo-ACP phosphopantetheine removal/recycling boundary | Computational prediction only | Low | boundary | Relevant to phosphopantetheine handling, not de novo pantothenate/CoA synthesis; should be excluded from core module satisfiability (leonardi2007biosynthesisofpantothenic pages 9-10) |
| ACP/nucleotide boundary nodes | PP_1183 | PP_1183 | Q88NM4 | Phosphopantetheinyl transferase (EntD-like); transfers 4′-phosphopantetheine to carrier proteins | Computational prediction; broad family knowledge | Low | boundary | Carrier-protein modification enzyme, not a CoA biosynthetic step; inclusion in KEGG map is a side-node/boundary issue (leonardi2007biosynthesisofpantothenic pages 9-10) |
| ACP/nucleotide boundary nodes | mazG | PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase | Computational prediction only | Low | boundary | No clear direct role in pantothenate or CoA biosynthesis; likely KEGG neighborhood/overview-map artifact rather than pathway member (belda2016therevisitedgenome pages 1-2) |


*Table: This table summarizes the 24 candidate genes associated with KEGG ppu00770 in Pseudomonas putida KT2440, organizing them by core steps, feeder pathways, and boundary nodes. It highlights which genes are strongly supported core pathway components versus contextual or likely over-propagated annotations, with evidence type, confidence, and curation-oriented status for each.*

### 4.1 High-Confidence Core Genes

**coaX (PP_0438):** This is the best-supported gene in the module for *P. putida* KT2440. The type III pantothenate kinase (PpcoaA) was cloned from KT2440 genomic DNA, and its heterologous expression in *C. ammoniagenes* ATCC 6871 led to a ~4.4-fold increase in CoA production, demonstrating functional activity (hou2019isolatingpromotersfrom pages 8-9, hou2019isolatingpromotersfrom pages 4-7). Structural studies of type III PanKs from related organisms (*Bacillus anthracis*, *Pseudomonas aeruginosa*) confirm that these enzymes share 25–37% sequence identity with the *P. putida* enzyme and lack the hydrophobic dome that mediates CoA feedback inhibition in type I/II enzymes (nicely2007structureofthe pages 1-2, nicely2007structureofthe pages 9-10, leonardi2007biosynthesisofpantothenic pages 8-9). Additionally, recent work on enhanced PHB biosynthesis in *P. putida* notes that PHA production can be enhanced by boosting flux through the CoA biosynthetic pathway via introduction of a type III pantothenate kinase gene and supplementation with pantothenate or β-alanine (favoino2024enhancedbiosynthesisof pages 2-4).

**panB (PP_4699):** Ketopantoate hydroxymethyltransferase. Annotation is consistent with the canonical pantoate branch. Though no direct KT2440 biochemistry has been published, the annotation is well supported by homology and pathway context (leonardi2007biosynthesisofpantothenic pages 2-4, belda2016therevisitedgenome pages 1-2).

**panC (PP_4700):** Pantothenate synthetase. Similarly well annotated. The non-auxotrophic phenotype of a panC knockout (molina‐henares2010identificationofconditionally pages 4-6) does not invalidate the gene assignment but suggests in vivo physiological context is more complex than simple single-gene essentiality would indicate.

**dfp/coaBC (PP_5285), coaD (PP_5123), coaE (PP_0631):** These encode the three remaining CoA pathway steps. All are assigned by high-confidence homology to the universal bacterial CoA pathway. The bifunctional CoaBC architecture (phosphopantothenoylcysteine synthetase + decarboxylase, encoded by dfp) is the standard arrangement in bacteria (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 8-9). CoaD (PPAT) and CoaE (DPCK) annotations are straightforward and consistent with conserved essential functions in all bacteria (leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 6-8, leonardi2007biosynthesisofpantothenic pages 10-12).

### 4.2 Moderate-Confidence and Context Genes

**panE (PP_1351):** The primary ketopantoate reductase candidate, but confidence is moderated by the known ability of IlvC (acetohydroxy acid isomeroreductase, EC 1.1.1.86) to catalyze the same α-ketopantoate reduction reaction both in vitro and in vivo. In *C. glutamicum*, IlvC is the sole enzyme for this step (leonardi2007biosynthesisofpantothenic pages 2-4). The presence of multiple PanE-annotated paralogs (PP_2325, PP_2998) further complicates assignment.

**ilvC (PP_4678), ilvD (PP_5128):** Both are experimentally confirmed as functional in KT2440 through multiple metabolic engineering studies involving isobutanol and 2-ketoisovalerate production (nitschel2020engineeringpseudomonasputida pages 1-2, nitschel2020engineeringpseudomonasputida pages 2-4, nitschel2020engineeringpseudomonasputida pages 7-8, batianis2023atunablemetabolic pages 6-7). While they are not pantothenate/CoA pathway enzymes per se, ilvC provides the precursor 3-methyl-2-oxobutanoate and may serve as a backup ketopantoate reductase. These should be classified as precursor-supply context.

**pydB (PP_4036), pydA/pydX (PP_4038/PP_4037), hyuC (PP_4034):** Functional genomics (RB-TnSeq) in KT2440 provides direct evidence for their roles in pyrimidine degradation (schmidt2022nitrogenmetabolismin pages 12-15). Their relevance to pantothenate biosynthesis is indirect—they supply β-alanine in the absence of PanD—and they should be treated as context genes rather than core module members.

### 4.3 Low-Confidence and Boundary Genes

**PP_2325, PP_2998:** These carry 2-dehydropantoate reductase (EC 1.1.1.169) annotations but have no species-specific experimental support. They likely represent over-propagated annotations based on broad oxidoreductase similarity rather than verified pantothenate biosynthesis roles.

**PP_0922 (AcpH-like), PP_1183 (EntD-like):** These are phosphopantetheine-handling enzymes that function in ACP modification (phosphopantetheinyl transfer and removal), not in de novo CoA biosynthesis. They appear in KEGG ppu00770 as side nodes and should be excluded from core module satisfiability.

**mazG (PP_1657):** NTP pyrophosphohydrolase. Its inclusion in ppu00770 appears to be a KEGG overview-map artifact with no clear mechanistic connection to pantothenate or CoA biosynthesis.

**PP_1157, PP_1394, ilvH (PP_4679), ilvI (PP_4680), ilvE (PP_3511):** These are BCAA pathway enzymes providing or consuming the 3-methyl-2-oxobutanoate precursor. They are important metabolic context but not pantothenate/CoA pathway members.

**PP_0614:** Paralog of hyuC. No direct evidence links it to β-alanine supply specifically; likely redundant with hyuC (schmidt2022nitrogenmetabolismin pages 12-15).

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Gaps

**panD absence:** *P. putida* KT2440 does not encode the canonical aspartate 1-decarboxylase (panD) for β-alanine supply. The pyrimidine reductive catabolism route (pydA/pydX → pydB → hyuC) compensates but is classified under a different KEGG pathway (ppu00410). This creates a genuine gap in the standard module definition that requires species-aware revision (schmidt2022nitrogenmetabolismin pages 12-15, perchat2022characterizationofa pages 1-2).

**No direct biochemistry for most CoA pathway enzymes:** While coaX has heterologous expression data, the remaining core genes (panB, panC, panE, dfp, coaD, coaE) are annotated solely by homology. No KT2440-specific enzyme kinetics, crystal structures, or complementation assays have been published for these genes.

### 5.2 Ambiguities

**Ketopantoate reductase paralog assignment:** The annotation of PP_1351 (panE), PP_2325, and PP_2998 all as EC 1.1.1.169 creates significant paralog ambiguity. It is unclear whether all three genuinely catalyze 2-dehydropantoate reduction in vivo, or whether PP_2325 and PP_2998 represent over-propagated annotations for general-purpose oxidoreductases. The ability of IlvC (PP_4678) to substitute for PanE adds another layer of redundancy (leonardi2007biosynthesisofpantothenic pages 2-4).

**Non-auxotrophic panC mutant:** The failure to observe pantothenate auxotrophy in a panC (PP_4700) knockout on minimal medium (molina‐henares2010identificationofconditionally pages 4-6, molina‐henares2010identificationofconditionally pages 12-13) is unexplained. Possible explanations include: (a) trace pantothenate contamination in the medium; (b) an alternative pantothenate synthesis route; (c) pantothenate salvage from cell lysis; or (d) library screening limitations. This issue is not resolved and warrants targeted validation.

### 5.3 Likely Over-Annotations

**PP_2325 and PP_2998** as bona fide 2-dehydropantoate reductases are suspect without experimental evidence. Broad EC number propagation from sequence similarity to genuine PanE enzymes is the most parsimonious explanation.

**mazG (PP_1657)** inclusion in ppu00770 is likely an artifact of KEGG overview-map construction rather than genuine pathway membership.

**PP_0922 and PP_1183** are correctly annotated for their respective functions (AcpH phosphodiesterase and EntD-type phosphopantetheinyl transferase) but are not CoA biosynthetic enzymes. Their presence in the KEGG map reflects downstream utilization of the phosphopantetheine moiety derived from CoA, not participation in CoA synthesis.

## 6. Module and GO-Curation Recommendations

### 6.1 Module Step Status Assignments

| Step | Recommended Status |
|---|---|
| PanB (3-methyl-2-oxobutanoate → 2-dehydropantoate) | **covered** |
| PanE (2-dehydropantoate → pantoate) | **candidate_uncertain** (paralog ambiguity with PP_2325, PP_2998, and IlvC) |
| β-Alanine supply | **module_needs_revision** (panD absent; pyrimidine catabolism route substitutes) |
| PanC (pantoate + β-alanine → pantothenate) | **covered** (despite non-auxotrophy caveat) |
| CoaX (pantothenate → 4'-phosphopantothenate) | **covered** (strongest evidence) |
| CoaBC/Dfp (4'-phosphopantothenate → 4'-phosphopantetheine) | **covered** |
| CoaD (4'-phosphopantetheine → dephospho-CoA) | **covered** |
| CoaE (dephospho-CoA → CoA) | **covered** |
| ACP boundary nodes (PP_0922, PP_1183) | **not_expected_in_target_taxon** (boundary) |
| mazG (PP_1657) | **not_expected_in_target_taxon** (boundary artifact) |

### 6.2 Recommended Module Boundary Revisions

1. **Add a species-aware β-alanine supply note:** The generic module should flag that organisms lacking panD (including *Pseudomonas* spp.) may derive β-alanine from pyrimidine reductive catabolism, polyamine degradation, or other non-canonical routes (perchat2022characterizationofa pages 1-2).

2. **Separate BCAA precursor context:** Acetolactate synthase, IlvC, IlvD, and IlvE genes should be tracked under BCAA biosynthesis (ppu00290/ppu00660) rather than ppu00770. Their inclusion in the pantothenate module conflates precursor supply with pathway membership.

3. **Remove boundary nodes from core satisfiability:** PP_0922, PP_1183, and mazG should be excluded from core module satisfiability assessments. They represent downstream CoA utilization or unrelated nucleotide metabolism.

### 6.3 GO Term Considerations

- The GO term "pantothenate kinase activity" (GO:0004594) is correctly applicable to coaX (PP_0438). However, the qualifier should specify "type III pantothenate kinase" to distinguish it from type I and type II activities.
- Consider requesting or verifying that IlvC (PP_4678) carries an annotation note for possible "2-dehydropantoate 2-reductase activity" (GO:0008677) as a secondary activity.

## 7. Genes to Promote to Full Review

The following genes merit full `fetch-gene` review:

1. **coaX / PP_0438:** Highest priority. The only gene with direct heterologous expression evidence from KT2440. Full review should include structural alignment to the *B. anthracis* and *P. aeruginosa* type III PanK crystal structures, complete kinetic characterization, and assessment of CoA-insensitive regulation (nicely2007structureofthe pages 1-2, hou2019isolatingpromotersfrom pages 4-7).

2. **panE / PP_1351:** Needs resolution of paralog ambiguity. Full review should address whether PP_1351 is the physiologically relevant 2-dehydropantoate reductase or whether IlvC (PP_4678) is the primary enzyme in KT2440, as in *C. glutamicum* (leonardi2007biosynthesisofpantothenic pages 2-4).

3. **panC / PP_4700:** The non-auxotrophic panC knockout phenotype (molina‐henares2010identificationofconditionally pages 4-6) warrants targeted investigation. Full review should examine whether pantothenate salvage or an alternative synthetase exists.

4. **dfp / PP_5285:** CoaBC bifunctional enzyme. Important for module completeness; full review should confirm bifunctional domain architecture and examine whether pantethine rescue is possible in *Pseudomonas* as it is in *E. coli* but reportedly not in *P. aeruginosa*.

5. **PP_2325 and PP_2998:** These should be evaluated for possible annotation over-propagation. A targeted review should determine whether their PanE-like annotation is justified or should be revised to a more general oxidoreductase classification.

## 8. Key References

1. **Leonardi R, Jackowski S.** Biosynthesis of pantothenic acid and coenzyme A. *EcoSal Plus*. 2007;2(2). doi:10.1128/ecosalplus.3.6.3.4 — Comprehensive review of bacterial pantothenate and CoA biosynthesis pathway enzymology (leonardi2007biosynthesisofpantothenic pages 2-4, leonardi2007biosynthesisofpantothenic pages 9-10, leonardi2007biosynthesisofpantothenic pages 6-8, leonardi2007biosynthesisofpantothenic pages 8-9, leonardi2007biosynthesisofpantothenic pages 10-12, leonardi2007biosynthesisofpantothenic pages 1-2).

2. **Nicely NI, Parsonage D, Paige C, et al.** Structure of the type III pantothenate kinase from *Bacillus anthracis* at 2.0 Å resolution. *Biochemistry*. 2007;46(11):3234-45. doi:10.1021/bi062299p — Crystal structure and functional characterization of type III PanK, ASKHA superfamily classification, and absence of CoA feedback inhibition (nicely2007structureofthe pages 1-2, nicely2007structureofthe pages 5-7, nicely2007structureofthe pages 9-10, nicely2007structureofthe pages 4-5, nicely2007structureofthe pages 3-4).

3. **Hou Y, Chen S, Wang J, et al.** Isolating promoters from *Corynebacterium ammoniagenes* ATCC 6871 and application in CoA synthesis. *BMC Biotechnology*. 2019;19(1):76. doi:10.1186/s12896-019-0568-9 — Heterologous expression of PpcoaA (type III PanK from *P. putida* KT2440) increasing CoA yield ~4.4-fold (hou2019isolatingpromotersfrom pages 8-9, hou2019isolatingpromotersfrom pages 4-7).

4. **Molina-Henares MA, De La Torre J, García-Salamanca A, et al.** Identification of conditionally essential genes for growth of *P. putida* KT2440 on minimal medium. *Environmental Microbiology*. 2010;12(6):1468-85. doi:10.1111/j.1462-2920.2010.02166.x — Genome-wide mutant library screening; panB/panC mutants not auxotrophic for pantothenate (molina‐henares2010identificationofconditionally pages 4-6, molina‐henares2010identificationofconditionally pages 2-3, molina‐henares2010identificationofconditionally pages 12-13, molina‐henares2010identificationofconditionally pages 11-12, molina‐henares2010identificationofconditionally pages 1-2).

5. **Schmidt M, Pearson AN, Incha MR, et al.** Nitrogen metabolism in *Pseudomonas putida*: functional analysis using random barcode transposon sequencing. *Applied and Environmental Microbiology*. 2022;88(7). doi:10.1128/aem.02430-21 — RB-TnSeq fitness data for pyrimidine degradation genes (PP_4036-4038, PP_4034) in KT2440 (schmidt2022nitrogenmetabolismin pages 12-15).

6. **Borchert AJ, Bleem AC, Lim HG, et al.** Machine learning analysis of RB-TnSeq fitness data predicts functional gene modules in *Pseudomonas putida* KT2440. *mSystems*. 2024;9(3). doi:10.1128/msystems.00942-23 — ICA-based functional module prediction integrating fitness data for KT2440 (borchert2024machinelearninganalysis pages 15-17).

7. **Belda E, van Heck RGA, Lopez-Sanchez MJ, et al.** The revisited genome of *Pseudomonas putida* KT2440 enlightens its value as a robust metabolic chassis. *Environmental Microbiology*. 2016;18(10):3403-3424. doi:10.1111/1462-2920.13230 — Comprehensive genome re-annotation with 242 new genes and 1,548 re-annotated functions (belda2016therevisitedgenome pages 1-2).

8. **Nitschel R, Ankenbauer A, Welsch I, et al.** Engineering *Pseudomonas putida* KT2440 for the production of isobutanol. *Engineering in Life Sciences*. 2020;20(5-6):148-159. doi:10.1002/elsc.201900151 — Functional demonstration of native ilvC, ilvD, and heterologous alsS in KT2440 BCAA pathway (nitschel2020engineeringpseudomonasputida pages 1-2, nitschel2020engineeringpseudomonasputida pages 2-4, nitschel2020engineeringpseudomonasputida pages 7-8).

9. **Favoino G, Krink N, Schwanemann T, et al.** Enhanced biosynthesis of poly(3-hydroxybutyrate) in engineered strains of *Pseudomonas putida* via increased malonyl-CoA availability. *Microbial Biotechnology*. 2024;17(11). doi:10.1111/1751-7915.70044 — CoA pathway flux enhancement via type III PanK for PHA production (favoino2024enhancedbiosynthesisof pages 2-4, favoino2024enhancedbiosynthesisof pages 1-2).

10. **Perchat N, Dubois C, Mor-Gautier R, et al.** Characterization of a novel β-alanine biosynthetic pathway consisting of promiscuous metabolic enzymes. *Journal of Biological Chemistry*. 2022;298(7):102067. doi:10.1016/j.jbc.2022.102067 — Alternative β-alanine biosynthesis routes in bacteria lacking panD (perchat2022characterizationofa pages 1-2).

11. **Böttcher J, Sibon OCM, El Aidy S.** Coenzyme A metabolism: a key driver of gut microbiota dynamics and metabolic profiles. *FEMS Microbiology Reviews*. 2025;49. doi:10.1093/femsre/fuaf051 — Recent review of bacterial CoA metabolism and type III PanK prevalence (bottcher2025coenzymeametabolism pages 1-2).

References

1. (hou2019isolatingpromotersfrom pages 8-9): Yingshuo Hou, Siyu Chen, Jianjun Wang, Guizhen Liu, Sheng Wu, and Yong Tao. Isolating promoters from corynebacterium ammoniagenes atcc 6871 and application in coa synthesis. BMC Biotechnology, Nov 2019. URL: https://doi.org/10.1186/s12896-019-0568-9, doi:10.1186/s12896-019-0568-9. This article has 8 citations and is from a peer-reviewed journal.

2. (hou2019isolatingpromotersfrom pages 4-7): Yingshuo Hou, Siyu Chen, Jianjun Wang, Guizhen Liu, Sheng Wu, and Yong Tao. Isolating promoters from corynebacterium ammoniagenes atcc 6871 and application in coa synthesis. BMC Biotechnology, Nov 2019. URL: https://doi.org/10.1186/s12896-019-0568-9, doi:10.1186/s12896-019-0568-9. This article has 8 citations and is from a peer-reviewed journal.

3. (schmidt2022nitrogenmetabolismin pages 12-15): Matthias Schmidt, Allison N. Pearson, Matthew R. Incha, Mitchell G. Thompson, Edward E. K. Baidoo, Ramu Kakumanu, Aindrila Mukhopadhyay, Patrick M. Shih, Adam M. Deutschbauer, Lars M. Blank, and Jay D. Keasling. Nitrogen metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Applied and Environmental Microbiology, Apr 2022. URL: https://doi.org/10.1128/aem.02430-21, doi:10.1128/aem.02430-21. This article has 36 citations and is from a peer-reviewed journal.

4. (perchat2022characterizationofa pages 1-2): Nadia Perchat, Christelle Dubois, Rémi Mor-Gautier, Sophie Duquesne, Christophe Lechaplais, David Roche, Stéphanie Fouteau, Ekaterina Darii, and Alain Perret. Characterization of a novel β-alanine biosynthetic pathway consisting of promiscuous metabolic enzymes. Journal of Biological Chemistry, 298:102067, Jul 2022. URL: https://doi.org/10.1016/j.jbc.2022.102067, doi:10.1016/j.jbc.2022.102067. This article has 13 citations and is from a domain leading peer-reviewed journal.

5. (leonardi2007biosynthesisofpantothenic pages 2-4): Roberta Leonardi and Suzanne Jackowski. Biosynthesis of pantothenic acid and coenzyme a. EcoSal Plus, Dec 2007. URL: https://doi.org/10.1128/ecosalplus.3.6.3.4, doi:10.1128/ecosalplus.3.6.3.4. This article has 448 citations.

6. (leonardi2007biosynthesisofpantothenic pages 9-10): Roberta Leonardi and Suzanne Jackowski. Biosynthesis of pantothenic acid and coenzyme a. EcoSal Plus, Dec 2007. URL: https://doi.org/10.1128/ecosalplus.3.6.3.4, doi:10.1128/ecosalplus.3.6.3.4. This article has 448 citations.

7. (leonardi2007biosynthesisofpantothenic pages 6-8): Roberta Leonardi and Suzanne Jackowski. Biosynthesis of pantothenic acid and coenzyme a. EcoSal Plus, Dec 2007. URL: https://doi.org/10.1128/ecosalplus.3.6.3.4, doi:10.1128/ecosalplus.3.6.3.4. This article has 448 citations.

8. (leonardi2007biosynthesisofpantothenic pages 1-2): Roberta Leonardi and Suzanne Jackowski. Biosynthesis of pantothenic acid and coenzyme a. EcoSal Plus, Dec 2007. URL: https://doi.org/10.1128/ecosalplus.3.6.3.4, doi:10.1128/ecosalplus.3.6.3.4. This article has 448 citations.

9. (belda2016therevisitedgenome pages 1-2): Eugeni Belda, Ruben G. A. van Heck, Maria José Lopez‐Sanchez, Stéphane Cruveiller, Valérie Barbe, Claire Fraser, Hans‐Peter Klenk, Jörn Petersen, Anne Morgat, Pablo I. Nikel, David Vallenet, Zoé Rouy, Agnieszka Sekowska, Vitor A. P. Martins dos Santos, Víctor de Lorenzo, Antoine Danchin, and Claudine Médigue. The revisited genome of pseudomonas putida kt2440 enlightens its value as a robust metabolic chassis. Environmental microbiology, 18 10:3403-3424, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13230, doi:10.1111/1462-2920.13230. This article has 376 citations and is from a domain leading peer-reviewed journal.

10. (nitschel2020engineeringpseudomonasputida pages 1-2): Robert Nitschel, Andreas Ankenbauer, Ilona Welsch, Nicolas T. Wirth, Christoph Massner, Naveed Ahmad, Stephen McColm, Frédéric Borges, Ian Fotheringham, Ralf Takors, and Bastian Blombach. Engineering pseudomonas putida kt2440 for the production of isobutanol. Engineering in Life Sciences, 20:148-159, Feb 2020. URL: https://doi.org/10.1002/elsc.201900151, doi:10.1002/elsc.201900151. This article has 32 citations and is from a peer-reviewed journal.

11. (batianis2023atunablemetabolic pages 6-7): Christos Batianis, Rik P. van Rosmalen, Monika Major, Cheyenne van Ee, Alexandros Kasiotakis, Ruud A. Weusthuis, and Vitor A.P. Martins dos Santos. A tunable metabolic valve for precise growth control and increased product formation in pseudomonas putida. Metabolic Engineering, 75:47-57, Jan 2023. URL: https://doi.org/10.1016/j.ymben.2022.10.002, doi:10.1016/j.ymben.2022.10.002. This article has 19 citations and is from a domain leading peer-reviewed journal.

12. (molina‐henares2010identificationofconditionally pages 4-6): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

13. (molina‐henares2010identificationofconditionally pages 12-13): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

14. (leonardi2007biosynthesisofpantothenic pages 8-9): Roberta Leonardi and Suzanne Jackowski. Biosynthesis of pantothenic acid and coenzyme a. EcoSal Plus, Dec 2007. URL: https://doi.org/10.1128/ecosalplus.3.6.3.4, doi:10.1128/ecosalplus.3.6.3.4. This article has 448 citations.

15. (nicely2007structureofthe pages 1-2): Nathan I. Nicely, Derek Parsonage, Carleitta Paige, Gerald L. Newton, Robert C. Fahey, Roberta Leonardi, Suzanne Jackowski, T. Conn Mallett, and Al Claiborne. Structure of the type iii pantothenate kinase from bacillus anthracis at 2.0 a resolution: implications for coenzyme a-dependent redox biology. Biochemistry, 46 11:3234-45, Mar 2007. URL: https://doi.org/10.1021/bi062299p, doi:10.1021/bi062299p. This article has 79 citations and is from a peer-reviewed journal.

16. (nicely2007structureofthe pages 5-7): Nathan I. Nicely, Derek Parsonage, Carleitta Paige, Gerald L. Newton, Robert C. Fahey, Roberta Leonardi, Suzanne Jackowski, T. Conn Mallett, and Al Claiborne. Structure of the type iii pantothenate kinase from bacillus anthracis at 2.0 a resolution: implications for coenzyme a-dependent redox biology. Biochemistry, 46 11:3234-45, Mar 2007. URL: https://doi.org/10.1021/bi062299p, doi:10.1021/bi062299p. This article has 79 citations and is from a peer-reviewed journal.

17. (nicely2007structureofthe pages 9-10): Nathan I. Nicely, Derek Parsonage, Carleitta Paige, Gerald L. Newton, Robert C. Fahey, Roberta Leonardi, Suzanne Jackowski, T. Conn Mallett, and Al Claiborne. Structure of the type iii pantothenate kinase from bacillus anthracis at 2.0 a resolution: implications for coenzyme a-dependent redox biology. Biochemistry, 46 11:3234-45, Mar 2007. URL: https://doi.org/10.1021/bi062299p, doi:10.1021/bi062299p. This article has 79 citations and is from a peer-reviewed journal.

18. (molina‐henares2010identificationofconditionally pages 2-3): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

19. (nitschel2020engineeringpseudomonasputida pages 7-8): Robert Nitschel, Andreas Ankenbauer, Ilona Welsch, Nicolas T. Wirth, Christoph Massner, Naveed Ahmad, Stephen McColm, Frédéric Borges, Ian Fotheringham, Ralf Takors, and Bastian Blombach. Engineering pseudomonas putida kt2440 for the production of isobutanol. Engineering in Life Sciences, 20:148-159, Feb 2020. URL: https://doi.org/10.1002/elsc.201900151, doi:10.1002/elsc.201900151. This article has 32 citations and is from a peer-reviewed journal.

20. (lang2014metabolicengineeringof pages 6-7): Karsten Lang, Jessica Zierow, Katja Buehler, and Andreas Schmid. Metabolic engineering of pseudomonas sp. strain vlb120 as platform biocatalyst for the production of isobutyric acid and other secondary metabolites. Microbial Cell Factories, 13:2-2, Jan 2014. URL: https://doi.org/10.1186/1475-2859-13-2, doi:10.1186/1475-2859-13-2. This article has 92 citations and is from a peer-reviewed journal.

21. (favoino2024enhancedbiosynthesisof pages 2-4): Giusi Favoino, Nicolas Krink, Tobias Schwanemann, Nick Wierckx, and Pablo I. Nikel. Enhanced biosynthesis of poly(3‐hydroxybutyrate) in engineered strains of pseudomonas putida via increased malonyl‐coa availability. Microbial Biotechnology, Nov 2024. URL: https://doi.org/10.1111/1751-7915.70044, doi:10.1111/1751-7915.70044. This article has 11 citations and is from a peer-reviewed journal.

22. (leonardi2007biosynthesisofpantothenic pages 10-12): Roberta Leonardi and Suzanne Jackowski. Biosynthesis of pantothenic acid and coenzyme a. EcoSal Plus, Dec 2007. URL: https://doi.org/10.1128/ecosalplus.3.6.3.4, doi:10.1128/ecosalplus.3.6.3.4. This article has 448 citations.

23. (nitschel2020engineeringpseudomonasputida pages 2-4): Robert Nitschel, Andreas Ankenbauer, Ilona Welsch, Nicolas T. Wirth, Christoph Massner, Naveed Ahmad, Stephen McColm, Frédéric Borges, Ian Fotheringham, Ralf Takors, and Bastian Blombach. Engineering pseudomonas putida kt2440 for the production of isobutanol. Engineering in Life Sciences, 20:148-159, Feb 2020. URL: https://doi.org/10.1002/elsc.201900151, doi:10.1002/elsc.201900151. This article has 32 citations and is from a peer-reviewed journal.

24. (nicely2007structureofthe pages 4-5): Nathan I. Nicely, Derek Parsonage, Carleitta Paige, Gerald L. Newton, Robert C. Fahey, Roberta Leonardi, Suzanne Jackowski, T. Conn Mallett, and Al Claiborne. Structure of the type iii pantothenate kinase from bacillus anthracis at 2.0 a resolution: implications for coenzyme a-dependent redox biology. Biochemistry, 46 11:3234-45, Mar 2007. URL: https://doi.org/10.1021/bi062299p, doi:10.1021/bi062299p. This article has 79 citations and is from a peer-reviewed journal.

25. (nicely2007structureofthe pages 3-4): Nathan I. Nicely, Derek Parsonage, Carleitta Paige, Gerald L. Newton, Robert C. Fahey, Roberta Leonardi, Suzanne Jackowski, T. Conn Mallett, and Al Claiborne. Structure of the type iii pantothenate kinase from bacillus anthracis at 2.0 a resolution: implications for coenzyme a-dependent redox biology. Biochemistry, 46 11:3234-45, Mar 2007. URL: https://doi.org/10.1021/bi062299p, doi:10.1021/bi062299p. This article has 79 citations and is from a peer-reviewed journal.

26. (molina‐henares2010identificationofconditionally pages 11-12): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

27. (molina‐henares2010identificationofconditionally pages 1-2): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

28. (borchert2024machinelearninganalysis pages 15-17): Andrew J. Borchert, Alissa C. Bleem, Hyun Gyu Lim, Kevin Rychel, Keven D. Dooley, Zoe A. Kellermyer, Tracy L. Hodges, Bernhard O. Palsson, and Gregg T. Beckham. Machine learning analysis of rb-tnseq fitness data predicts functional gene modules in <i>pseudomonas putida</i> kt2440. Mar 2024. URL: https://doi.org/10.1128/msystems.00942-23, doi:10.1128/msystems.00942-23. This article has 13 citations and is from a peer-reviewed journal.

29. (favoino2024enhancedbiosynthesisof pages 1-2): Giusi Favoino, Nicolas Krink, Tobias Schwanemann, Nick Wierckx, and Pablo I. Nikel. Enhanced biosynthesis of poly(3‐hydroxybutyrate) in engineered strains of pseudomonas putida via increased malonyl‐coa availability. Microbial Biotechnology, Nov 2024. URL: https://doi.org/10.1111/1751-7915.70044, doi:10.1111/1751-7915.70044. This article has 11 citations and is from a peer-reviewed journal.

30. (bottcher2025coenzymeametabolism pages 1-2): Johanna Böttcher, Ody C M Sibon, and Sahar El Aidy. Coenzyme a metabolism: a key driver of gut microbiota dynamics and metabolic profiles. FEMS Microbiology Reviews, Oct 2025. URL: https://doi.org/10.1093/femsre/fuaf051, doi:10.1093/femsre/fuaf051. This article has 10 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__pantothenate_and_coa_biosynthesis__ppu00770-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__pantothenate_and_coa_biosynthesis__ppu00770-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. leonardi2007biosynthesisofpantothenic pages 2-4
2. leonardi2007biosynthesisofpantothenic pages 9-10
3. hou2019isolatingpromotersfrom pages 4-7
4. perchat2022characterizationofa pages 1-2
5. schmidt2022nitrogenmetabolismin pages 12-15
6. belda2016therevisitedgenome pages 1-2
7. batianis2023atunablemetabolic pages 6-7
8. lang2014metabolicengineeringof pages 6-7
9. favoino2024enhancedbiosynthesisof pages 2-4
10. borchert2024machinelearninganalysis pages 15-17
11. bottcher2025coenzymeametabolism pages 1-2
12. hou2019isolatingpromotersfrom pages 8-9
13. leonardi2007biosynthesisofpantothenic pages 6-8
14. leonardi2007biosynthesisofpantothenic pages 1-2
15. nitschel2020engineeringpseudomonasputida pages 1-2
16. leonardi2007biosynthesisofpantothenic pages 8-9
17. nicely2007structureofthe pages 1-2
18. nicely2007structureofthe pages 5-7
19. nicely2007structureofthe pages 9-10
20. nitschel2020engineeringpseudomonasputida pages 7-8
21. leonardi2007biosynthesisofpantothenic pages 10-12
22. nitschel2020engineeringpseudomonasputida pages 2-4
23. nicely2007structureofthe pages 4-5
24. nicely2007structureofthe pages 3-4
25. favoino2024enhancedbiosynthesisof pages 1-2
26. Includes: Phosphopantothenoylcysteine decarboxylase (PPC decarboxylase) (PPC-DC) (EC 4.1.1.36) (CoaC); Phosphopantothenate--cysteine ligase (EC 6.3.2.5) (CoaB) (Phosphopantothenoylcysteine synthetase) (PPC synthetase) (PPC-S)
27. acyl-carrier-protein
28. https://doi.org/10.1186/s12896-019-0568-9,
29. https://doi.org/10.1128/aem.02430-21,
30. https://doi.org/10.1016/j.jbc.2022.102067,
31. https://doi.org/10.1128/ecosalplus.3.6.3.4,
32. https://doi.org/10.1111/1462-2920.13230,
33. https://doi.org/10.1002/elsc.201900151,
34. https://doi.org/10.1016/j.ymben.2022.10.002,
35. https://doi.org/10.1111/j.1462-2920.2010.02166.x,
36. https://doi.org/10.1021/bi062299p,
37. https://doi.org/10.1186/1475-2859-13-2,
38. https://doi.org/10.1111/1751-7915.70044,
39. https://doi.org/10.1128/msystems.00942-23,
40. https://doi.org/10.1093/femsre/fuaf051,