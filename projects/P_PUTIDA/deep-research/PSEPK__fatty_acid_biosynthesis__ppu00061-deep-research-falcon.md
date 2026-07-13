---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T21:40:46.784681'
end_time: '2026-07-06T21:59:42.328857'
duration_seconds: 1135.54
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Type-II fatty acid biosynthesis module
  module_summary: A bacterial type-II fatty acid synthesis boundary module covering
    formation of malonyl-CoA and malonyl-ACP, iterative acyl-ACP chain elongation,
    reduction and dehydration steps, enoyl-ACP reduction, and the unsaturated fatty-acid
    branch. For Pseudomonas putida KT2440, KEGG ppu00061 also pulls in acyl-CoA ligases
    and weak SDR/aromatic-catabolism side candidates that should be reviewed as boundary
    context rather than assumed core FAS-II enzymes.
  module_outline: "- Type-II fatty acid biosynthesis module\n  - 1. acetyl-CoA carboxylase\
    \ / malonyl-CoA formation\n  - Acetyl-CoA to malonyl-CoA\n    - Acetyl-CoA carboxylase\
    \ (molecular player: acetyl-CoA carboxylase activity; activity or role: acetyl-CoA\
    \ carboxylase activity)\n    - Biotin carboxylase (molecular player: biotin carboxylase\
    \ activity; activity or role: biotin carboxylase activity)\n  - 2. malonyl-ACP\
    \ formation\n  - Malonyl-CoA to malonyl-ACP\n    - Malonyl CoA-acyl carrier protein\
    \ transacylase (molecular player: [acyl-carrier-protein] S-malonyltransferase\
    \ activity; activity or role: [acyl-carrier-protein] S-malonyltransferase activity)\n\
    \  - 3. acyl-ACP condensation\n  - 3-oxoacyl-ACP synthesis\n    - 3-oxoacyl-[acyl-carrier-protein]\
    \ synthase (molecular player: 3-oxoacyl-[acyl-carrier-protein] synthase activity;\
    \ activity or role: 3-oxoacyl-[acyl-carrier-protein] synthase activity)\n  - 4.\
    \ beta-ketoacyl-ACP reduction\n  - 3-oxoacyl-ACP to 3-hydroxyacyl-ACP\n    - 3-oxoacyl-[acyl-carrier-protein]\
    \ reductase (NADPH) (molecular player: 3-oxoacyl-[acyl-carrier-protein] reductase\
    \ (NADPH) activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] reductase\
    \ (NADPH) activity)\n  - 5. beta-hydroxyacyl-ACP dehydration\n  - 3-hydroxyacyl-ACP\
    \ to enoyl-ACP\n    - 3-hydroxyacyl-[acyl-carrier-protein] dehydratase (molecular\
    \ player: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity; activity\
    \ or role: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity)\n  - 6.\
    \ enoyl-ACP reduction\n  - Enoyl-ACP to acyl-ACP\n    - Enoyl-[acyl-carrier-protein]\
    \ reductase (NADH) (molecular player: enoyl-[acyl-carrier-protein] reductase (NADH)\
    \ activity; activity or role: enoyl-[acyl-carrier-protein] reductase (NADH) activity)\n\
    \  - 7. unsaturated fatty acid branch\n  - Unsaturated fatty acid branch\n   \
    \ - Trans-2-decenoyl-acyl-carrier-protein isomerase (molecular player: trans-2-decenoyl-acyl-carrier-protein\
    \ isomerase activity; activity or role: trans-2-decenoyl-acyl-carrier-protein\
    \ isomerase activity)"
  module_connections: No explicit connections.
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
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__fatty_acid_biosynthesis__ppu00061-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__fatty_acid_biosynthesis__ppu00061-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Type-II fatty acid biosynthesis module in Pseudomonas putida KT2440

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

A bacterial type-II fatty acid synthesis boundary module covering formation of malonyl-CoA and malonyl-ACP, iterative acyl-ACP chain elongation, reduction and dehydration steps, enoyl-ACP reduction, and the unsaturated fatty-acid branch. For Pseudomonas putida KT2440, KEGG ppu00061 also pulls in acyl-CoA ligases and weak SDR/aromatic-catabolism side candidates that should be reviewed as boundary context rather than assumed core FAS-II enzymes.

### Provisional Biological Outline

- Type-II fatty acid biosynthesis module
  - 1. acetyl-CoA carboxylase / malonyl-CoA formation
  - Acetyl-CoA to malonyl-CoA
    - Acetyl-CoA carboxylase (molecular player: acetyl-CoA carboxylase activity; activity or role: acetyl-CoA carboxylase activity)
    - Biotin carboxylase (molecular player: biotin carboxylase activity; activity or role: biotin carboxylase activity)
  - 2. malonyl-ACP formation
  - Malonyl-CoA to malonyl-ACP
    - Malonyl CoA-acyl carrier protein transacylase (molecular player: [acyl-carrier-protein] S-malonyltransferase activity; activity or role: [acyl-carrier-protein] S-malonyltransferase activity)
  - 3. acyl-ACP condensation
  - 3-oxoacyl-ACP synthesis
    - 3-oxoacyl-[acyl-carrier-protein] synthase (molecular player: 3-oxoacyl-[acyl-carrier-protein] synthase activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] synthase activity)
  - 4. beta-ketoacyl-ACP reduction
  - 3-oxoacyl-ACP to 3-hydroxyacyl-ACP
    - 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) (molecular player: 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity)
  - 5. beta-hydroxyacyl-ACP dehydration
  - 3-hydroxyacyl-ACP to enoyl-ACP
    - 3-hydroxyacyl-[acyl-carrier-protein] dehydratase (molecular player: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity; activity or role: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity)
  - 6. enoyl-ACP reduction
  - Enoyl-ACP to acyl-ACP
    - Enoyl-[acyl-carrier-protein] reductase (NADH) (molecular player: enoyl-[acyl-carrier-protein] reductase (NADH) activity; activity or role: enoyl-[acyl-carrier-protein] reductase (NADH) activity)
  - 7. unsaturated fatty acid branch
  - Unsaturated fatty acid branch
    - Trans-2-decenoyl-acyl-carrier-protein isomerase (molecular player: trans-2-decenoyl-acyl-carrier-protein isomerase activity; activity or role: trans-2-decenoyl-acyl-carrier-protein isomerase activity)

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

Type-II fatty acid biosynthesis module in Pseudomonas putida KT2440

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

A bacterial type-II fatty acid synthesis boundary module covering formation of malonyl-CoA and malonyl-ACP, iterative acyl-ACP chain elongation, reduction and dehydration steps, enoyl-ACP reduction, and the unsaturated fatty-acid branch. For Pseudomonas putida KT2440, KEGG ppu00061 also pulls in acyl-CoA ligases and weak SDR/aromatic-catabolism side candidates that should be reviewed as boundary context rather than assumed core FAS-II enzymes.

### Provisional Biological Outline

- Type-II fatty acid biosynthesis module
  - 1. acetyl-CoA carboxylase / malonyl-CoA formation
  - Acetyl-CoA to malonyl-CoA
    - Acetyl-CoA carboxylase (molecular player: acetyl-CoA carboxylase activity; activity or role: acetyl-CoA carboxylase activity)
    - Biotin carboxylase (molecular player: biotin carboxylase activity; activity or role: biotin carboxylase activity)
  - 2. malonyl-ACP formation
  - Malonyl-CoA to malonyl-ACP
    - Malonyl CoA-acyl carrier protein transacylase (molecular player: [acyl-carrier-protein] S-malonyltransferase activity; activity or role: [acyl-carrier-protein] S-malonyltransferase activity)
  - 3. acyl-ACP condensation
  - 3-oxoacyl-ACP synthesis
    - 3-oxoacyl-[acyl-carrier-protein] synthase (molecular player: 3-oxoacyl-[acyl-carrier-protein] synthase activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] synthase activity)
  - 4. beta-ketoacyl-ACP reduction
  - 3-oxoacyl-ACP to 3-hydroxyacyl-ACP
    - 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) (molecular player: 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity; activity or role: 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity)
  - 5. beta-hydroxyacyl-ACP dehydration
  - 3-hydroxyacyl-ACP to enoyl-ACP
    - 3-hydroxyacyl-[acyl-carrier-protein] dehydratase (molecular player: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity; activity or role: 3-hydroxyacyl-[acyl-carrier-protein] dehydratase activity)
  - 6. enoyl-ACP reduction
  - Enoyl-ACP to acyl-ACP
    - Enoyl-[acyl-carrier-protein] reductase (NADH) (molecular player: enoyl-[acyl-carrier-protein] reductase (NADH) activity; activity or role: enoyl-[acyl-carrier-protein] reductase (NADH) activity)
  - 7. unsaturated fatty acid branch
  - Unsaturated fatty acid branch
    - Trans-2-decenoyl-acyl-carrier-protein isomerase (molecular player: trans-2-decenoyl-acyl-carrier-protein isomerase activity; activity or role: trans-2-decenoyl-acyl-carrier-protein isomerase activity)

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

# Type-II Fatty Acid Biosynthesis Module in *Pseudomonas putida* KT2440: Species-Aware Module Review

---

## 1. Executive Summary

*Pseudomonas putida* KT2440 encodes a complete type-II fatty acid synthesis (FAS-II) pathway, with all seven expected enzymatic steps represented by identifiable gene candidates. However, this review identifies several important curation issues: (i) the canonical FabH-only initiation model is likely too narrow for pseudomonads, as recent evidence from the closely related *P. putida* F1 demonstrates that FabB (KAS I) can initiate fatty acid synthesis independently of FabH (guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 6-8); (ii) the identity of the enoyl-ACP reductase was long unresolved, with FabV (PP_4635) now being the best core candidate rather than the earlier-flagged PP_1852 (mezzina2021engineeringnativeand pages 13-16); (iii) several SDR-family reductases (PP_0581, PP_2540, PP_2783) listed as putative FabG variants are likely over-propagated annotations; and (iv) FadD-I (PP_4549) and FadD-II (PP_4550) are β-oxidation acyl-CoA ligases, not FAS-II biosynthetic enzymes (thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 8-12). Of the 19 candidate genes, 11 are high-confidence core FAS-II enzymes, 2 are boundary/uncertain, 3 are likely over-annotations, and 2 are β-oxidation enzymes that should be assigned to a separate module. One gene (PP_3303) is a medium-confidence FabF paralog whose specific role remains unresolved.

---

## 2. Target-Organism Pathway Definition

### 2.1 Biochemical Scope

The FAS-II module covers de novo synthesis of long-chain acyl-ACP species (C14–C18) from acetyl-CoA and malonyl-CoA, using discrete soluble enzymes that act on acyl carrier protein (ACP)-tethered intermediates (mezzina2021engineeringnativeand pages 13-16). The pathway includes: (a) malonyl-CoA formation via the acetyl-CoA carboxylase (ACC) complex; (b) transfer of malonyl to ACP by FabD; (c) iterative condensation–reduction–dehydration–reduction elongation cycles; and (d) an unsaturated fatty acid (UFA) branch catalyzed by FabA isomerase and FabB elongase. In *P. putida* KT2440, the pathway is essential for providing precursors for membrane phospholipids, lipopolysaccharides, rhamnolipids, and medium-chain-length polyhydroxyalkanoates (mcl-PHA) (mezzina2021engineeringnativeand pages 13-16, mezzina2021engineeringnativeand pages 16-19).

### 2.2 Neighboring Pathways to Keep Separate

- **β-Oxidation (fatty acid degradation):** Catalyzed by FadD acyl-CoA ligases, FadE dehydrogenases, FadB hydratases, and FadA thiolases. FadD-I (PP_4549) and FadD-II (PP_4550) belong here, not in FAS-II (thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 8-12).
- **PHA biosynthesis:** Linked to FAS-II via PhaG transacylase/thioesterase (PP_1408) and AlkK (PP_0763), but these are PHA-specific connectors, not core FAS-II enzymes (mezzina2021engineeringnativeand pages 16-19).
- **Rhamnolipid biosynthesis:** Uses (R)-3-hydroxyacyl-ACP intermediates diverted from FAS-II by RhlA, but RhlA and downstream enzymes are separate.
- **Biotin synthesis:** ACC subunits are shared with biotin-dependent carboxylation but the biotin synthesis pathway itself is distinct.
- **Aromatic catabolism:** PP_2783 (dihydrodiol dehydrogenase) belongs here, not in FAS-II (mezzina2021engineeringnativeand pages 13-16).

### 2.3 Database Definitions

KEGG ppu00061 ("Fatty acid biosynthesis") resolves to 7 primary genes but pulls in additional candidates from ppu00780 ("Fatty acid metabolism") and ppu04146 ("Peroxisome/fatty acid degradation"). The KEGG boundary is broader than the core FAS-II module and includes β-oxidation activation enzymes that should be curated separately.

---

## 3. Expected Step Model

The following table summarizes the satisfiability of each expected FAS-II step in *P. putida* KT2440:

| Step Number | Step Name | Reaction | Covering Gene(s) | Status | Key Caveats |
|---|---|---|---|---|---|
| 1 | Malonyl-CoA formation | Acetyl-CoA + HCO3- + ATP -> malonyl-CoA | accC/PP_0558, accB/PP_0559, accA/PP_1607, accD/PP_1996 | covered | Core 4-subunit ACC complex is well supported in KT2440 pathway reconstructions and reviews; no major ambiguity at the step level (mezzina2021engineeringnativeand pages 13-16). |
| 2 | Malonyl-ACP formation | Malonyl-CoA -> malonyl-ACP | fabD/PP_1913 | covered | Canonical FabD assignment; no strong competing candidates identified (mezzina2021engineeringnativeand pages 13-16). |
| 3 | Acyl-ACP condensation / initiation | Acetyl primer + malonyl-ACP -> acetoacetyl-ACP; subsequent elongating condensations with malonyl-ACP | PP_4379 (FabH-like KAS III), fabB/PP_4175; elongation also includes fabF/PP_1916 and PP_3303 | module_needs_revision | KT2440 reviews assign FabH to initiation, but recent P. putida F1 experiments show FabB can initiate FAS and FabH can be non-essential, so a generic "FabH-only initiation" boundary is likely too narrow for Pseudomonas. Transfer to KT2440 is strong but indirect (mezzina2021engineeringnativeand pages 13-16, guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 6-8, dong2021acrypticlongchain pages 1-2). |
| 4 | Beta-ketoacyl-ACP reduction | 3-oxoacyl-ACP -> 3-hydroxyacyl-ACP | fabG/PP_1914 | covered | PP_1914 is the best core assignment; PP_0581, PP_2540, and PP_2783 are weak SDR-family side candidates and should not be needed to satisfy the core step (mezzina2021engineeringnativeand pages 13-16). |
| 5 | Beta-hydroxyacyl-ACP dehydration | 3-hydroxyacyl-ACP -> trans-2-enoyl-ACP | fabZ/PP_1602, fabA/PP_4174 | covered | FabZ is the canonical dehydratase; FabA also dehydrates but is additionally important for the UFA branch via isomerase activity (mezzina2021engineeringnativeand pages 13-16, dong2021acrypticlongchain pages 8-10). |
| 6 | Enoyl-ACP reduction | trans-2-enoyl-ACP -> acyl-ACP | fabV/PP_4635 | covered | Older KT2440 reviews left ENR identity unresolved and mentioned PP_1852 as a putative ENR, but current candidate set supports fabV/PP_4635 as the best core assignment; PP_1852 should be treated as secondary/uncertain (mezzina2021engineeringnativeand pages 13-16, hopf2022bacterialenoylreductasesthe pages 8-10). |
| 7 | Unsaturated fatty acid branch | trans-2-decenoyl-ACP -> cis-3-decenoyl-ACP -> elongated unsaturated acyl-ACP | fabA/PP_4174, fabB/PP_4175 | covered | FabA provides the trans-2 to cis-3 isomerase activity and FabB performs the key elongation step in the anaerobic/oxygen-independent UFA branch. In related P. putida F1, a DesA-dependent aerobic route also exists, so FabAB is not necessarily the only UFA route in the lineage; presence and contribution of DesA/DesB in KT2440 should be reviewed separately from the core FAS-II module (dong2021acrypticlongchain pages 8-10, dong2021acrypticlongchain pages 4-6). |


*Table: This table summarizes satisfiability of the seven expected FAS-II steps in Pseudomonas putida KT2440 and highlights the major curation issue: initiation may not be FabH-only in pseudomonads. It is useful for deciding which steps are covered versus where the module definition likely needs revision.*

---

## 4. Candidate Genes and Evidence

The complete assessment of all 19 candidate genes is presented below:

| Gene Name | Locus Tag | UniProt | Assigned Pathway Step | Evidence Type (direct/homology/annotation) | Confidence | Core FAS-II? | Notes |
|---|---|---|---|---|---|---|---|
| accC | PP_0558 | Q88QD6 | Acetyl-CoA carboxylase, biotin carboxylase subunit; malonyl-CoA formation | homology/curated pathway in KT2440 review | High | Yes | Part of 4-subunit ACC complex with AccB/AccA/AccD; repeatedly described as core FAS-II initiation in KT2440 (mezzina2021engineeringnativeand pages 13-16). |
| accB | PP_0559 | Q88QD5 | Acetyl-CoA carboxylase, biotin carboxyl carrier protein; malonyl-CoA formation | homology/curated pathway in KT2440 review | High | Yes | Core ACC carrier subunit in KT2440; grouped with accC/accA/accD in FAS entry step (mezzina2021engineeringnativeand pages 13-16). |
| PP_0581 | PP_0581 | Q88QB3 | Putative 3-oxoacyl-ACP reductase variant | annotation only | Low | Boundary | Listed in KT2440 reviews as a possible FabG-like paralog, but no direct species-specific functional validation for core FAS-II found; likely broad SDR over-propagation (mezzina2021engineeringnativeand pages 13-16). |
| fabZ | PP_1602 | Q88MG9 | 3-hydroxyacyl-ACP dehydratase; dehydration step | homology plus pathway logic from Pseudomonas studies | High | Yes | Canonical FabZ dehydratase; in pseudomonads FabZ performs dehydration but lacks FabA isomerase function (mezzina2021engineeringnativeand pages 13-16, dong2021acrypticlongchain pages 8-10). |
| accA | PP_1607 | Q88MG4 | Acetyl-CoA carboxylase carboxyltransferase alpha; malonyl-CoA formation | homology/curated pathway in KT2440 review | High | Yes | Core ACC alpha subunit in KT2440 FAS-II (mezzina2021engineeringnativeand pages 13-16). |
| PP_1852 | PP_1852 | Q88LS6 | Putative enoyl-ACP reductase or SDR reductase | annotation only | Low | Boundary | Earlier KT2440 review flagged PP_1852 as a putative ENR based on motifs, but gene identity remained unresolved there; now likely displaced by fabV as better ENR candidate in metadata, so PP_1852 should be treated cautiously (mezzina2021engineeringnativeand pages 13-16). |
| fabD | PP_1913 | Q88LL7 | Malonyl-CoA:ACP transacylase; malonyl-ACP formation | homology/curated pathway in KT2440 review | High | Yes | Canonical FabD assignment in KT2440; activates malonyl-CoA onto ACP before condensation (mezzina2021engineeringnativeand pages 13-16). |
| fabG | PP_1914 | Q88LL6 | 3-oxoacyl-ACP reductase; beta-keto reduction step | homology/curated pathway in KT2440 review | High | Yes | Best-supported core beta-ketoacyl-ACP reductase in KT2440; paralogous SDRs exist but are less convincing (mezzina2021engineeringnativeand pages 13-16). |
| fabF | PP_1916 | Q88LL4 | 3-oxoacyl-ACP synthase II; elongation condensation | homology plus transfer from P. putida F1 paralog studies | High | Yes | Core elongation KAS. In related P. putida F1, FabF1 is major long-chain elongase including cis-vaccenate production; transfer to KT2440 is strong but indirect (dong2021acrypticlongchain pages 2-4, dong2021acrypticlongchain pages 1-2). |
| accD | PP_1996 | Q88LD9 | Acetyl-CoA carboxylase carboxyltransferase beta; malonyl-CoA formation | homology/curated pathway in KT2440 review | High | Yes | Core ACC beta subunit in KT2440 (mezzina2021engineeringnativeand pages 13-16). |
| PP_2540 | PP_2540 | Q88JV7 | Putative SDR/FabG-like reductase variant | annotation only | Low | Boundary | Included in KT2440 review as one of several putative FabG variants, but no direct evidence ties it to housekeeping FAS-II; likely non-core SDR family member (mezzina2021engineeringnativeand pages 13-16). |
| PP_2783 | PP_2783 | Q88J66 | Annotated aromatic-diol dehydrogenase; weakly suggested FabG-like variant in overview review | annotation/conflicting | Over-annotation | No | Specific annotation is 2,3-dihydroxy-2,3-dihydro-p-cumate dehydrogenase, arguing for aromatic catabolism rather than core FAS-II; mention as FabG variant in broad review is likely overreach (mezzina2021engineeringnativeand pages 13-16). |
| PP_3303 | PP_3303 | Q88HQ0 | 3-oxoacyl-ACP synthase II paralog; elongation KAS | homology/paralog inference | Medium | Yes | Likely second FabF-like KAS. P. putida F1 contains multiple FabF-family proteins, with only some active in FAS/UFA synthesis; KT2440 paralog-specific role remains unresolved (dong2021acrypticlongchain pages 2-4, dong2021acrypticlongchain pages 1-2). |
| fabA | PP_4174 | Q88FC4 | 3-hydroxyacyl-ACP dehydratase/isomerase; dehydration and unsaturated-FA branch | homology plus direct evidence in related P. putida F1 | High | Yes | Strong assignment: FabA has dual dehydratase and trans-2 to cis-3 isomerase activity required for anaerobic UFA branch; transfer from P. putida F1 to KT2440 is strong (dong2021acrypticlongchain pages 8-10, mezzina2021engineeringnativeand pages 13-16). |
| fabB | PP_4175 | Q88FC3 | 3-oxoacyl-ACP synthase I; elongation and unsaturated-FA branch, possibly initiation | homology plus strong related-species experiments | High | Yes | Core UFA-branch KAS. In P. putida F1, FabB is essential for UFA synthesis and can even initiate FAS in vivo/in vitro; this raises a major curation caveat that generic KT2440 modules assigning initiation only to FabH may be incomplete (guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 6-8, dong2021acrypticlongchain pages 1-2). |
| PP_4379 | PP_4379 | Q88ES4 | FabH/KAS III-like initiation condensing enzyme | annotation plus KT2440 pathway review | Medium | Yes | KT2440 review assigns PP_4379 as FabH for first condensation, but recent Pseudomonas work suggests FabH may be non-essential or secondary to FabB/FabY-like initiation in some strains; keep as candidate core initiator with caveat (mezzina2021engineeringnativeand pages 13-16, guo2024diversityinfatty pages 2-4, yuan2012fattyacidbiosynthesis pages 5-9). |
| fadD-I | PP_4549 | Q88EB7 | Long-chain fatty acyl-CoA ligase for beta-oxidation entry | direct fitness evidence in KT2440 | High | No | Strongly supported catabolic acyl-CoA ligase for C7-C18 fatty acids; not part of ACP-based FAS-II, though relevant as neighboring fatty-acid metabolism boundary gene (thompson2020fattyacidand pages 5-7, valencia2022engineeringpseudomonasputida pages 1-3). |
| fadD-II | PP_4550 | Q88EB6 | Fatty acyl-CoA ligase for beta-oxidation entry | direct fitness evidence in KT2440 | High | No | Catabolic ligase with narrower contribution, especially C8-C10; not a FAS-II biosynthetic enzyme (thompson2020fattyacidand pages 5-7, valencia2022engineeringpseudomonasputida pages 1-3). |
| fabV | PP_4635 | Q88E33 | Enoyl-ACP reductase (ENR); enoyl reduction step | homology/annotation with family-level support | High | Yes | Best current core ENR candidate in KT2440 metadata. FabV is a recognized triclosan-resistant ENR family widespread in Gram-negatives and pseudomonads; older KT2440 review had unresolved ENR identity, so PP_4635 should be promoted over PP_1852 for focused review (hopf2022bacterialenoylreductasesthe pages 8-10, mezzina2021engineeringnativeand pages 13-16). |


*Table: This table summarizes all 19 candidate genes associated with the Pseudomonas putida KT2440 FAS-II module, assigning each to a pathway step and indicating whether it is a core biosynthetic enzyme, a boundary gene, or a likely over-annotation. It is useful for module satisfiability review and for prioritizing genes that need deeper curation.*

### 4.1 High-Confidence Core FAS-II Genes

**AccABCD (PP_1607, PP_0559, PP_0558, PP_1996):** The four-subunit acetyl-CoA carboxylase complex is well-established in *P. putida* KT2440. AccC (PP_0558) is the biotin carboxylase, AccB (PP_0559) is the biotin carboxyl carrier protein, AccA (PP_1607) and AccD (PP_1996) are the carboxyltransferase α and β subunits, respectively. Together, they catalyze the ATP-dependent carboxylation of acetyl-CoA to malonyl-CoA (mezzina2021engineeringnativeand pages 13-16). Evidence type: curated pathway annotation with strong homology support. No curation concerns.

**FabD (PP_1913):** Malonyl-CoA:ACP transacylase, converting malonyl-CoA to malonyl-ACP. Canonical assignment supported by genomic context (co-located with fabG and fabF in the fab gene cluster) (mezzina2021engineeringnativeand pages 13-16). Evidence type: homology and genomic context. No curation concerns.

**FabG (PP_1914):** NADPH-dependent 3-oxoacyl-ACP reductase. The primary β-ketoacyl-ACP reductase in FAS-II, co-located with fabD and fabF. While four additional putative SDR-family variants are mentioned in pathway overviews (PP_0581, PP_1852, PP_2540, PP_2783), PP_1914 is the best-supported core assignment (mezzina2021engineeringnativeand pages 13-16). Evidence type: homology and genomic context.

**FabZ (PP_1602):** 3-Hydroxyacyl-ACP dehydratase. Catalyzes dehydration of (R)-3-hydroxyacyl-ACP to trans-2-enoyl-ACP. In pseudomonads, FabZ performs the general dehydration step, while FabA additionally carries out the isomerization needed for UFA synthesis (mezzina2021engineeringnativeand pages 13-16, dong2021acrypticlongchain pages 8-10). Evidence type: homology.

**FabA (PP_4174):** Bifunctional 3-hydroxydecanoyl-ACP dehydratase and trans-2-decenoyl-ACP isomerase. In *P. putida* F1, FabA deletion results in UFA auxotrophy, confirming its essential role in the oxygen-independent UFA branch (dong2021acrypticlongchain pages 8-10, dong2021acrypticlongchain pages 4-6, dong2021acrypticlongchain pages 1-2). The isomerase activity (trans-2 → cis-3-decenoyl-ACP) is unique to FabA and cannot be performed by FabZ. Evidence type: direct genetic evidence in *P. putida* F1, with strong transfer to KT2440.

**FabB (PP_4175):** 3-Oxoacyl-ACP synthase I (KAS I). Essential for UFA synthesis, as it elongates cis-3-decenoyl-ACP to longer unsaturated acyl-ACP species. Critically, recent work by Guo et al. (2024) demonstrated that *P. putida* F1 FabB can also initiate fatty acid synthesis by decarboxylating malonyl-ACP and condensing the resulting acetyl-ACP with another malonyl-ACP, a function traditionally attributed to FabH (guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 6-8). Deletion of both FabH paralogs in *P. putida* F1 did not abolish growth, indicating FabB-mediated initiation can substitute for FabH (guo2024diversityinfatty pages 1-2). Evidence type: direct in vivo and in vitro evidence in *P. putida* F1. Transfer to KT2440 is strong.

**FabF (PP_1916):** 3-Oxoacyl-ACP synthase II (KAS II). Responsible for elongation of saturated and unsaturated acyl-ACP chains, including the conversion of palmitoleoyl-ACP (C16:1) to cis-vaccenoyl-ACP (C18:1). In *P. putida* F1, the orthologous FabF1 is confirmed as the major enzyme for cis-vaccenate production, and its deletion leads to near-complete loss of C18:1 (dong2021acrypticlongchain pages 2-4, dong2021acrypticlongchain pages 1-2). Evidence type: direct evidence in *P. putida* F1.

**FabV (PP_4635):** Enoyl-ACP reductase (ENR), NADH-dependent. FabV represents a distinct class of ENR that is larger than FabI (~400 residues vs. ~260) and is intrinsically resistant to triclosan (hopf2022bacterialenoylreductasesthe pages 8-10). The identity of the ENR in *P. putida* KT2440 was noted as unresolved in an earlier comprehensive review, which flagged PP_1852 as a putative ENR based on conserved motifs (mezzina2021engineeringnativeand pages 13-16). However, PP_4635 is annotated as FabV (EC 1.3.1.9) in the current KEGG assignment and is the strongest candidate based on the FabV enzyme class being widespread in γ-proteobacteria including *Pseudomonas* species (hopf2022bacterialenoylreductasesthe pages 8-10). *P. aeruginosa* encodes both FabI and FabV, and the same architecture may apply in *P. putida* KT2440, though this requires direct experimental confirmation.

### 4.2 Medium-Confidence Genes

**PP_4379 (FabH-like, KAS III):** Annotated as the initiation condensing enzyme in KT2440 reviews, catalyzing the condensation of acetyl-CoA with malonyl-ACP to form acetoacetyl-ACP (mezzina2021engineeringnativeand pages 13-16). A second FabH paralog, PP_4545, was also identified. However, as noted above, recent *P. putida* F1 work shows that FabH is not essential for initiation, as FabB can substitute (guo2024diversityinfatty pages 2-4). Whether PP_4379 is the primary initiation enzyme in KT2440, or whether FabB plays the dominant role, remains an open question. In *P. aeruginosa*, a different enzyme entirely (FabY, PA5174) was identified as the primary initiation KAS (yuan2012fattyacidbiosynthesis pages 1-5, yuan2012fattyacidbiosynthesis pages 5-9). *P. putida* does not encode a clear FabY homolog, adding further complexity. Evidence type: annotation plus indirect evidence.

**PP_3303 (FabF paralog):** Annotated as a second 3-oxoacyl-ACP synthase II (KAS II). In *P. putida* F1, the genome encodes multiple FabF-family proteins, but only FabF1 and FabF2 showed clear in vivo activity; FabF3 and FabF4 lacked detectable KAS activity when expressed in *E. coli* (dong2021acrypticlongchain pages 2-4, dong2021acrypticlongchain pages 1-2). The role of PP_3303 in KT2440 is uncertain and may represent a specialized or cryptic elongase. Evidence type: paralog inference.

### 4.3 Boundary and Over-Annotation Candidates

**PP_1852:** Listed as a putative enoyl-ACP reductase (EC 1.3.1.10, NADPH B-specific) in the primary KEGG bucket ppu00780. An earlier pathway review mentioned PP_1852 as a possible ENR candidate based on conserved motifs but also listed it among putative FabG variants (mezzina2021engineeringnativeand pages 13-16). With FabV (PP_4635) now assigned as the primary ENR, PP_1852 should be treated as a secondary candidate with uncertain function. It may be an SDR-family reductase with substrate specificity distinct from core FAS-II.

**PP_0581:** Annotated as 3-oxoacyl-ACP reductase and listed among putative FabG variants, but no direct functional evidence supports its role in housekeeping FAS-II in *P. putida* KT2440 (mezzina2021engineeringnativeand pages 13-16). Likely an over-propagation from broad EC/SDR family classification.

**PP_2540:** Short-chain dehydrogenase/reductase family protein. Included as a putative FabG variant but lacks specific evidence for FAS-II function (mezzina2021engineeringnativeand pages 13-16). Likely over-annotation.

**PP_2783:** Annotated as 2,3-dihydroxy-2,3-dihydro-p-cumate dehydrogenase (EC 1.3.1.58), an enzyme involved in aromatic catabolism. Its inclusion in the FAS-II candidate list appears to be an over-propagation based on SDR family membership (mezzina2021engineeringnativeand pages 13-16). This gene should be removed from the FAS-II module and assigned to aromatic degradation pathways.

**FadD-I (PP_4549) and FadD-II (PP_4550):** Long-chain fatty-acid–CoA ligases involved in the activation step of β-oxidation (fatty acid degradation), not biosynthesis. RB-TnSeq fitness data in KT2440 demonstrated that FadD1 is required for catabolism of C7–C18 fatty acids, while FadD2 has a narrower role primarily on C8–C10 substrates (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7). Engineering studies confirmed that knocking out these ligases blocks fatty acid degradation and enables free fatty acid accumulation (valencia2022engineeringpseudomonasputida pages 1-3). These genes should be assigned to the β-oxidation module, not FAS-II.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Critical Ambiguity: FAS Initiation Step

The most significant curation issue is the initiation condensation step. The generic FAS-II module model assigns this step to FabH (KAS III, EC 2.3.1.180). However, multiple lines of evidence indicate this model is too simple for pseudomonads:

- In *P. aeruginosa*, FabY (PA5174), a divergent KAS I/II-domain protein unrelated to FabH, is the primary initiation enzyme. Deletion of all four KAS III genes in *P. aeruginosa* produced a wild-type growth phenotype (yuan2012fattyacidbiosynthesis pages 1-5, yuan2012fattyacidbiosynthesis pages 5-9).
- In *P. putida* F1, FabB can initiate FAS by decarboxylating malonyl-ACP and catalyzing the first condensation, and FabH double-deletion does not prevent growth (guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 6-8).
- A related study (McNaught et al., 2023, doi:10.1016/j.ymben.2023.02.006, paper unobtainable) specifically addressed initiation of fatty acid biosynthesis in *P. putida* KT2440 and may provide direct KT2440-specific evidence; this paper should be consulted for definitive curation.

**Recommendation:** The module definition should be revised to allow FabB as an alternative or primary initiation enzyme in pseudomonads. PP_4379 should remain as a candidate initiator, but its essentiality should not be assumed.

### 5.2 Enoyl-ACP Reductase Identity

Earlier KT2440 reviews noted the ENR identity as unresolved (mezzina2021engineeringnativeand pages 13-16). The current KEGG assignment places FabV (PP_4635, EC 1.3.1.9) in the pathway, which is well-supported by FabV biology in other γ-proteobacteria (hopf2022bacterialenoylreductasesthe pages 8-10). However, direct biochemical or genetic characterization of PP_4635 in KT2440 has not been confirmed from the literature obtained here. Whether KT2440 also encodes a functional FabI, as seen in *P. aeruginosa* (which has both FabI and FabV), remains an open question.

### 5.3 Over-Annotations

Three genes (PP_0581, PP_2540, PP_2783) are listed as putative FabG variants based on SDR family membership, but there is no direct evidence for their role in core FAS-II. PP_2783 is a clear over-annotation, as its primary function is in aromatic catabolism (mezzina2021engineeringnativeand pages 13-16). PP_1852 occupies an ambiguous position between a FabG-like reductase and a putative ENR; with FabV (PP_4635) now assigned, PP_1852's role becomes even more uncertain.

### 5.4 Aerobic UFA Pathway

*P. putida* F1 encodes a DesA desaturase (Pput_0232, 84% identity to *P. aeruginosa* DesA) that provides an aerobic alternative to the FabA–FabB UFA pathway (dong2021acrypticlongchain pages 4-6). Whether KT2440 retains a functional DesA remains to be confirmed from its genome annotation. If present, the FAS-II module boundary should note that the UFA branch is not solely dependent on FabA–FabB under aerobic conditions. *P. aeruginosa* additionally encodes DesB; the presence of DesB in *P. putida* KT2440 is uncertain (dong2023suppressormutantsdemonstrate pages 1-2).

---

## 6. Module and GO-Curation Recommendations

### 6.1 Step Status Summary

| Step | Recommended Status |
|------|-------------------|
| 1. Malonyl-CoA formation | **Covered** (accABCD) |
| 2. Malonyl-ACP formation | **Covered** (fabD) |
| 3. Initiation condensation | **Module_needs_revision** (FabH assigned but FabB may be primary; FabY absent) |
| 4. β-Ketoacyl-ACP reduction | **Covered** (fabG/PP_1914) |
| 5. β-Hydroxyacyl-ACP dehydration | **Covered** (fabZ + fabA) |
| 6. Enoyl-ACP reduction | **Covered** (fabV/PP_4635) |
| 7. UFA branch | **Covered** (fabA + fabB), with note that aerobic DesA route may also exist |

### 6.2 Module Boundary Revisions Needed

1. **Initiation step:** The generic module should be revised for pseudomonads to include FabB as an alternative initiation enzyme, or the initiation step definition should be broadened to "β-ketoacyl-ACP synthase (KAS III or KAS I)" rather than "FabH only."
2. **Boundary exclusions:** FadD-I (PP_4549) and FadD-II (PP_4550) should be formally excluded from FAS-II and assigned to β-oxidation. PP_2783 should be excluded and assigned to aromatic catabolism.
3. **SDR candidates:** PP_0581, PP_2540, and PP_1852 should be flagged as "candidate_uncertain" rather than core FAS-II, pending direct functional evidence.
4. **DesA desaturase:** If present in KT2440, consider adding an optional aerobic UFA branch to the module definition.

### 6.3 GO Term Considerations

- FabB in pseudomonads may warrant the addition of a GO term or qualifier for "fatty acid biosynthesis initiation" in addition to the existing "3-oxoacyl-ACP synthase activity" and "unsaturated fatty acid biosynthesis."
- PP_4635 (FabV) should carry GO:0004318 (enoyl-[acyl-carrier-protein] reductase activity) with NADH specificity qualifier (EC 1.3.1.9), distinct from the NADPH-specific EC 1.3.1.10 sometimes assigned to PP_1852.

---

## 7. Genes to Promote to Full Review

The following genes should be prioritized for detailed `fetch-gene` review based on curation significance:

1. **FabB (PP_4175):** Requires full review to document its dual role as elongation KAS I and potential initiation enzyme in KT2440, a major departure from *E. coli* paradigm.
2. **FabV (PP_4635):** Requires full review to resolve whether it is the sole ENR, whether a FabI is also present, and to obtain direct KT2440 experimental evidence.
3. **PP_4379 (FabH-like):** Requires full review to determine whether it is essential or dispensable for FAS initiation in KT2440.
4. **PP_3303 (FabF paralog):** Requires review to determine if it is a functional KAS II or a cryptic/inactive paralog, informed by *P. putida* F1 evidence that some FabF paralogs lack detectable activity.
5. **PP_1852:** Requires review to determine whether it is an ENR, a FabG-like reductase, or has a non-FAS-II function.

---

## 8. Key References

- Mezzina et al. (2021), *Biotechnol. J.*, 16:2000165. doi:10.1002/biot.202000165. Comprehensive review of PHA metabolism in *P. putida* KT2440 with detailed FAS-II pathway description (mezzina2021engineeringnativeand pages 13-16).
- Guo et al. (2024), *J. Biol. Chem.*, 300:105600. doi:10.1016/j.jbc.2023.105600. Key paper demonstrating FabB-mediated FAS initiation in *P. putida* F1 (guo2024diversityinfatty pages 1-2, guo2024diversityinfatty pages 2-4, guo2024diversityinfatty pages 6-8).
- Dong et al. (2021), *J. Biol. Chem.*, 297:100920. doi:10.1016/j.jbc.2021.100920. Discovery of cryptic FabF2 3-ketoacyl-ACP synthase in *P. putida* F1 UFA pathway (dong2021acrypticlongchain pages 8-10, dong2021acrypticlongchain pages 2-4, dong2021acrypticlongchain pages 1-2, dong2021acrypticlongchain pages 4-6).
- Thompson et al. (2020), *Appl. Environ. Microbiol.*, 86:e01665-20. doi:10.1128/aem.01665-20. RB-TnSeq functional genomics of fatty acid catabolism in *P. putida* KT2440 (thompson2020fattyacidand pages 5-7).
- Valencia et al. (2022), *Commun. Biol.*, 5:1363. doi:10.1038/s42003-022-04336-2. Engineering *P. putida* KT2440 for free fatty acid production, clarifying CoA ligase roles (valencia2022engineeringpseudomonasputida pages 1-3).
- Yuan et al. (2012), *J. Bacteriol.*, 194:5171-5184. doi:10.1128/jb.00792-12. Discovery of FabY initiation enzyme in *P. aeruginosa* (yuan2012fattyacidbiosynthesis pages 1-5, yuan2012fattyacidbiosynthesis pages 5-9).
- Dong and Cronan (2023), *Microbiology*, 169:001400. doi:10.1099/mic.0.001400. Suppressor mutants revealing UFA synthesis plasticity in *P. aeruginosa*, with implications for *P. putida* DesA function (dong2023suppressormutantsdemonstrate pages 1-2).
- Hopf et al. (2022), *Front. Microbiol.*, 13:891610. doi:10.3389/fmicb.2022.891610. Review of bacterial enoyl-ACP reductase diversity including FabV (hopf2022bacterialenoylreductasesthe pages 8-10).
- Massengo-Tiassé and Cronan (2008), *J. Biol. Chem.*, 283:1308-1316. doi:10.1074/jbc.m708171200. Original characterization of FabV as a new ENR class.
- McNaught et al. (2023), *Metab. Eng.*, doi:10.1016/j.ymben.2023.02.006. Directly addresses FAS initiation in *P. putida* KT2440 (unobtainable; should be consulted for definitive curation).

---

### Note on Evidence Quality

Most gene assignments rely on a combination of (a) curated KT2440 pathway reviews (Mezzina et al., 2021), (b) direct experimental evidence from the closely related strain *P. putida* F1 (Guo et al., 2024; Dong et al., 2021), and (c) RB-TnSeq fitness data from KT2440 (Thompson et al., 2020). Transfer from *P. putida* F1 to KT2440 is generally strong, as the two strains share >95% amino acid identity for most FAS-II enzymes (guo2024diversityinfatty pages 1-2). Transfer from *P. aeruginosa* is weaker but informative, particularly for understanding the diversity of initiation and UFA synthesis strategies in the genus. Direct biochemical characterization of individual FAS-II enzymes in KT2440 remains limited, and the McNaught et al. (2023) study appears to be the most directly relevant KT2440-specific FAS initiation paper available.

References

1. (guo2024diversityinfatty pages 2-4): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

2. (guo2024diversityinfatty pages 6-8): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

3. (mezzina2021engineeringnativeand pages 13-16): Mariela P. Mezzina, María Tsampika Manoli, M. Auxiliadora Prieto, and Pablo I. Nikel. Engineering native and synthetic pathways in <i>pseudomonas putida</i> for the production of tailored polyhydroxyalkanoates. Biotechnology Journal, Nov 2021. URL: https://doi.org/10.1002/biot.202000165, doi:10.1002/biot.202000165. This article has 150 citations and is from a peer-reviewed journal.

4. (thompson2020fattyacidand pages 5-7): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

5. (thompson2020functionalanalysisof pages 8-12): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Functional analysis of the fatty acid and alcohol metabolism of pseudomonas putida using rb-tnseq. bioRxiv, Jul 2020. URL: https://doi.org/10.1101/2020.07.04.188060, doi:10.1101/2020.07.04.188060. This article has 3 citations.

6. (mezzina2021engineeringnativeand pages 16-19): Mariela P. Mezzina, María Tsampika Manoli, M. Auxiliadora Prieto, and Pablo I. Nikel. Engineering native and synthetic pathways in <i>pseudomonas putida</i> for the production of tailored polyhydroxyalkanoates. Biotechnology Journal, Nov 2021. URL: https://doi.org/10.1002/biot.202000165, doi:10.1002/biot.202000165. This article has 150 citations and is from a peer-reviewed journal.

7. (dong2021acrypticlongchain pages 1-2): Huijuan Dong, Jincheng Ma, Qunyi Chen, Bo Chen, Lujie Liang, Yuling Liao, Yulu Song, Haihong Wang, and John E. Cronan. A cryptic long-chain 3-ketoacyl-acp synthase in the pseudomonas putida f1 unsaturated fatty acid synthesis pathway. Aug 2021. URL: https://doi.org/10.1016/j.jbc.2021.100920, doi:10.1016/j.jbc.2021.100920. This article has 18 citations and is from a domain leading peer-reviewed journal.

8. (dong2021acrypticlongchain pages 8-10): Huijuan Dong, Jincheng Ma, Qunyi Chen, Bo Chen, Lujie Liang, Yuling Liao, Yulu Song, Haihong Wang, and John E. Cronan. A cryptic long-chain 3-ketoacyl-acp synthase in the pseudomonas putida f1 unsaturated fatty acid synthesis pathway. Aug 2021. URL: https://doi.org/10.1016/j.jbc.2021.100920, doi:10.1016/j.jbc.2021.100920. This article has 18 citations and is from a domain leading peer-reviewed journal.

9. (hopf2022bacterialenoylreductasesthe pages 8-10): Fernanda S. M. Hopf, Candida D. Roth, Eduardo V. de Souza, Luiza Galina, Alexia M. Czeczot, Pablo Machado, Luiz A. Basso, and Cristiano V. Bizarro. Bacterial enoyl-reductases: the ever-growing list of fabs, their mechanisms and inhibition. Frontiers in Microbiology, Jun 2022. URL: https://doi.org/10.3389/fmicb.2022.891610, doi:10.3389/fmicb.2022.891610. This article has 28 citations and is from a peer-reviewed journal.

10. (dong2021acrypticlongchain pages 4-6): Huijuan Dong, Jincheng Ma, Qunyi Chen, Bo Chen, Lujie Liang, Yuling Liao, Yulu Song, Haihong Wang, and John E. Cronan. A cryptic long-chain 3-ketoacyl-acp synthase in the pseudomonas putida f1 unsaturated fatty acid synthesis pathway. Aug 2021. URL: https://doi.org/10.1016/j.jbc.2021.100920, doi:10.1016/j.jbc.2021.100920. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (dong2021acrypticlongchain pages 2-4): Huijuan Dong, Jincheng Ma, Qunyi Chen, Bo Chen, Lujie Liang, Yuling Liao, Yulu Song, Haihong Wang, and John E. Cronan. A cryptic long-chain 3-ketoacyl-acp synthase in the pseudomonas putida f1 unsaturated fatty acid synthesis pathway. Aug 2021. URL: https://doi.org/10.1016/j.jbc.2021.100920, doi:10.1016/j.jbc.2021.100920. This article has 18 citations and is from a domain leading peer-reviewed journal.

12. (yuan2012fattyacidbiosynthesis pages 5-9): Yanqiu Yuan, Meena Sachdeva, Jennifer A. Leeds, and Timothy C. Meredith. Fatty acid biosynthesis in pseudomonas aeruginosa is initiated by the faby class of β-ketoacyl acyl carrier protein synthases. Journal of Bacteriology, 194:5171-5184, Oct 2012. URL: https://doi.org/10.1128/jb.00792-12, doi:10.1128/jb.00792-12. This article has 91 citations and is from a peer-reviewed journal.

13. (valencia2022engineeringpseudomonasputida pages 1-3): Luis E. Valencia, Matthew R. Incha, Matthias Schmidt, Allison N. Pearson, Mitchell G. Thompson, Jacob B. Roberts, Marina Mehling, Kevin Yin, Ning Sun, Asun Oka, Patrick M. Shih, Lars M. Blank, John Gladden, and Jay D. Keasling. Engineering pseudomonas putida kt2440 for chain length tailored free fatty acid and oleochemical production. Communications Biology, Dec 2022. URL: https://doi.org/10.1038/s42003-022-04336-2, doi:10.1038/s42003-022-04336-2. This article has 23 citations and is from a peer-reviewed journal.

14. (guo2024diversityinfatty pages 1-2): Qiaoqiao Guo, Canyao Zhong, Huijuan Dong, John E. Cronan, and Haihong Wang. Diversity in fatty acid elongation enzymes: the fabb long-chain β-ketoacyl-acp synthase i initiates fatty acid synthesis in pseudomonas putida f1. The Journal of Biological Chemistry, 300:105600, Feb 2024. URL: https://doi.org/10.1016/j.jbc.2023.105600, doi:10.1016/j.jbc.2023.105600. This article has 10 citations.

15. (yuan2012fattyacidbiosynthesis pages 1-5): Yanqiu Yuan, Meena Sachdeva, Jennifer A. Leeds, and Timothy C. Meredith. Fatty acid biosynthesis in pseudomonas aeruginosa is initiated by the faby class of β-ketoacyl acyl carrier protein synthases. Journal of Bacteriology, 194:5171-5184, Oct 2012. URL: https://doi.org/10.1128/jb.00792-12, doi:10.1128/jb.00792-12. This article has 91 citations and is from a peer-reviewed journal.

16. (dong2023suppressormutantsdemonstrate pages 1-2): Huijuan Dong and John E. Cronan. Suppressor mutants demonstrate the metabolic plasticity of unsaturated fatty acid synthesis in pseudomonas aeruginosa pao1. Oct 2023. URL: https://doi.org/10.1099/mic.0.001400, doi:10.1099/mic.0.001400. This article has 2 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__fatty_acid_biosynthesis__ppu00061-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__fatty_acid_biosynthesis__ppu00061-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. mezzina2021engineeringnativeand pages 13-16
2. mezzina2021engineeringnativeand pages 16-19
3. guo2024diversityinfatty pages 1-2
4. hopf2022bacterialenoylreductasesthe pages 8-10
5. guo2024diversityinfatty pages 2-4
6. valencia2022engineeringpseudomonasputida pages 1-3
7. dong2021acrypticlongchain pages 4-6
8. dong2023suppressormutantsdemonstrate pages 1-2
9. thompson2020fattyacidand pages 5-7
10. guo2024diversityinfatty pages 6-8
11. thompson2020functionalanalysisof pages 8-12
12. dong2021acrypticlongchain pages 1-2
13. dong2021acrypticlongchain pages 8-10
14. dong2021acrypticlongchain pages 2-4
15. yuan2012fattyacidbiosynthesis pages 5-9
16. yuan2012fattyacidbiosynthesis pages 1-5
17. acyl-carrier-protein
18. NADH
19. https://doi.org/10.1016/j.jbc.2023.105600,
20. https://doi.org/10.1002/biot.202000165,
21. https://doi.org/10.1128/aem.01665-20,
22. https://doi.org/10.1101/2020.07.04.188060,
23. https://doi.org/10.1016/j.jbc.2021.100920,
24. https://doi.org/10.3389/fmicb.2022.891610,
25. https://doi.org/10.1128/jb.00792-12,
26. https://doi.org/10.1038/s42003-022-04336-2,
27. https://doi.org/10.1099/mic.0.001400,