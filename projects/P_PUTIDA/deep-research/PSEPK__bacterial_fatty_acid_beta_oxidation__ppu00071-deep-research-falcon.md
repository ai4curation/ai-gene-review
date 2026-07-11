---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T22:31:12.173026'
end_time: '2026-07-06T22:46:10.666963'
duration_seconds: 898.49
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial fatty acid beta-oxidation and acyl-CoA activation
  module_summary: A bacterial fatty-acid degradation boundary module covering activation
    of free fatty acids to acyl-CoA thioesters, the FAD-dependent acyl-CoA dehydrogenase
    step, hydration and oxidation of enoyl/hydroxyacyl-CoA intermediates, and thiolytic
    cleavage to acetyl-CoA plus a shortened acyl-CoA. For Pseudomonas putida KT2440,
    KEGG ppu00071 also includes alkane/rubredoxin electron-transfer nodes and specialized
    CoA-thioester dehydrogenase paralogs; those should be treated as boundary context
    until module-level evidence resolves their role in fatty-acid degradation.
  module_outline: "- Bacterial fatty acid beta-oxidation and acyl-CoA activation\n\
    \  - 1. fatty-acid activation to acyl-CoA\n  - Fatty acid to fatty acyl-CoA\n\
    \    - Long-chain fatty acid-CoA ligase (molecular player: long-chain fatty acid-CoA\
    \ ligase activity; activity or role: long-chain fatty acid-CoA ligase activity)\n\
    \  - 2. FAD-dependent acyl-CoA dehydrogenation\n  - Fatty acyl-CoA to trans-2-enoyl-CoA\n\
    \    - Long-chain fatty acyl-CoA dehydrogenase (molecular player: long-chain fatty\
    \ acyl-CoA dehydrogenase activity; activity or role: long-chain fatty acyl-CoA\
    \ dehydrogenase activity)\n    - Medium-chain fatty acyl-CoA dehydrogenase (molecular\
    \ player: medium-chain fatty acyl-CoA dehydrogenase activity; activity or role:\
    \ medium-chain fatty acyl-CoA dehydrogenase activity)\n    - Acyl-CoA dehydrogenase-family\
    \ activity (molecular player: acyl-CoA dehydrogenase activity; activity or role:\
    \ acyl-CoA dehydrogenase activity)\n  - 3. enoyl-CoA hydration\n  - trans-2-enoyl-CoA\
    \ to 3-hydroxyacyl-CoA\n    - Enoyl-CoA hydratase (molecular player: enoyl-CoA\
    \ hydratase activity; activity or role: enoyl-CoA hydratase activity)\n  - 4.\
    \ 3-hydroxyacyl-CoA oxidation\n  - 3-hydroxyacyl-CoA to 3-ketoacyl-CoA\n    -\
    \ 3-hydroxyacyl-CoA dehydrogenase (molecular player: (3S)-3-hydroxyacyl-CoA dehydrogenase\
    \ (NAD+) activity; activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+)\
    \ activity)\n    - Long-chain 3-hydroxyacyl-CoA dehydrogenase (molecular player:\
    \ long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or\
    \ role: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)\n  -\
    \ 5. thiolytic cleavage to acetyl-CoA\n  - 3-ketoacyl-CoA to acetyl-CoA plus shortened\
    \ acyl-CoA\n    - Acetyl-CoA C-acyltransferase / beta-ketothiolase (molecular\
    \ player: acetyl-CoA C-acyltransferase activity; activity or role: acetyl-CoA\
    \ C-acyltransferase activity)\n  - 6. boundary alkane/rubredoxin electron transfer\n\
    \  - Alkane oxidation electron-transfer side nodes\n    - Rubredoxin-NAD+ reductase\
    \ (molecular player: rubredoxin-NAD+ reductase activity; activity or role: rubredoxin-NAD+\
    \ reductase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00071
  pathway_id: ppu00071
  pathway_name: Fatty acid degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00071 with 6 primary genes; module
    area: lipid_cell_envelope_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '22'
  candidate_genes: '- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC
    1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)

    - PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)

    - frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1)
    (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III)
    (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary
    bucket kegg:ppu00626)

    - fadE: PP_1893 | Q88LN6 | Acyl-coenzyme A dehydrogenase (EC 1.3.8.7) (EC 1.3.8.8)
    (EC 1.3.8.7; 1.3.8.8; primary bucket kegg:ppu00071)

    - fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16)
    (EC 2.3.1.16; primary bucket kegg:ppu00592)

    - fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes:
    Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA
    epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase
    (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)

    - fadA__Q88L01: PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA
    acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta)
    (EC 2.3.1.16; primary bucket kegg:ppu00592)

    - PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - acd: PP_2216 | Q88KS3 | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC
    3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane-1-carbonyl-CoA
    dehydrogenase) (EC 1.3.8.11; 3.13.1.4; primary bucket kegg:ppu00410)

    - PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_2437: PP_2437 | Q88K54 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC
    1.3.8.8; primary bucket kegg:ppu00071)

    - PP_2793: PP_2793 | Q88J56 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC
    1.3.8.8; primary bucket kegg:ppu00071)

    - paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)

    - PP_3725: PP_3725 | Q88GJ7 | Acyl-CoA dehydrogenase (primary bucket kegg:ppu00071)

    - bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC
    2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)

    - adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1)
    (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)

    - fadD-I: PP_4549 | Q88EB7 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain
    acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)

    - fadD-II: PP_4550 | Q88EB6 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain
    acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)

    - yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - alkT: PP_5314 | Q88C69 | Rubredoxin-NAD(+) reductase (EC 1.18.1.1) (EC 1.18.1.1;
    primary bucket kegg:ppu00071)

    - PP_5371: PP_5371 | Q88C12 | Rubredoxin/rubredoxin reductase (primary bucket
    kegg:ppu00071)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__bacterial_fatty_acid_beta_oxidation__ppu00071-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__bacterial_fatty_acid_beta_oxidation__ppu00071-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial fatty acid beta-oxidation and acyl-CoA activation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00071
- Resolved ID: ppu00071
- Resolved name: Fatty acid degradation
- Source: KEGG

Resolved local bucket kegg:ppu00071 with 6 primary genes; module area: lipid_cell_envelope_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 22

- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary bucket kegg:ppu00626)
- fadE: PP_1893 | Q88LN6 | Acyl-coenzyme A dehydrogenase (EC 1.3.8.7) (EC 1.3.8.8) (EC 1.3.8.7; 1.3.8.8; primary bucket kegg:ppu00071)
- fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)
- fadA__Q88L01: PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- acd: PP_2216 | Q88KS3 | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane-1-carbonyl-CoA dehydrogenase) (EC 1.3.8.11; 3.13.1.4; primary bucket kegg:ppu00410)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_2437: PP_2437 | Q88K54 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC 1.3.8.8; primary bucket kegg:ppu00071)
- PP_2793: PP_2793 | Q88J56 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC 1.3.8.8; primary bucket kegg:ppu00071)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- PP_3725: PP_3725 | Q88GJ7 | Acyl-CoA dehydrogenase (primary bucket kegg:ppu00071)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)
- fadD-I: PP_4549 | Q88EB7 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)
- fadD-II: PP_4550 | Q88EB6 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- alkT: PP_5314 | Q88C69 | Rubredoxin-NAD(+) reductase (EC 1.18.1.1) (EC 1.18.1.1; primary bucket kegg:ppu00071)
- PP_5371: PP_5371 | Q88C12 | Rubredoxin/rubredoxin reductase (primary bucket kegg:ppu00071)

## Generic Module Context

### Working Scope

A bacterial fatty-acid degradation boundary module covering activation of free fatty acids to acyl-CoA thioesters, the FAD-dependent acyl-CoA dehydrogenase step, hydration and oxidation of enoyl/hydroxyacyl-CoA intermediates, and thiolytic cleavage to acetyl-CoA plus a shortened acyl-CoA. For Pseudomonas putida KT2440, KEGG ppu00071 also includes alkane/rubredoxin electron-transfer nodes and specialized CoA-thioester dehydrogenase paralogs; those should be treated as boundary context until module-level evidence resolves their role in fatty-acid degradation.

### Provisional Biological Outline

- Bacterial fatty acid beta-oxidation and acyl-CoA activation
  - 1. fatty-acid activation to acyl-CoA
  - Fatty acid to fatty acyl-CoA
    - Long-chain fatty acid-CoA ligase (molecular player: long-chain fatty acid-CoA ligase activity; activity or role: long-chain fatty acid-CoA ligase activity)
  - 2. FAD-dependent acyl-CoA dehydrogenation
  - Fatty acyl-CoA to trans-2-enoyl-CoA
    - Long-chain fatty acyl-CoA dehydrogenase (molecular player: long-chain fatty acyl-CoA dehydrogenase activity; activity or role: long-chain fatty acyl-CoA dehydrogenase activity)
    - Medium-chain fatty acyl-CoA dehydrogenase (molecular player: medium-chain fatty acyl-CoA dehydrogenase activity; activity or role: medium-chain fatty acyl-CoA dehydrogenase activity)
    - Acyl-CoA dehydrogenase-family activity (molecular player: acyl-CoA dehydrogenase activity; activity or role: acyl-CoA dehydrogenase activity)
  - 3. enoyl-CoA hydration
  - trans-2-enoyl-CoA to 3-hydroxyacyl-CoA
    - Enoyl-CoA hydratase (molecular player: enoyl-CoA hydratase activity; activity or role: enoyl-CoA hydratase activity)
  - 4. 3-hydroxyacyl-CoA oxidation
  - 3-hydroxyacyl-CoA to 3-ketoacyl-CoA
    - 3-hydroxyacyl-CoA dehydrogenase (molecular player: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
    - Long-chain 3-hydroxyacyl-CoA dehydrogenase (molecular player: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or role: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
  - 5. thiolytic cleavage to acetyl-CoA
  - 3-ketoacyl-CoA to acetyl-CoA plus shortened acyl-CoA
    - Acetyl-CoA C-acyltransferase / beta-ketothiolase (molecular player: acetyl-CoA C-acyltransferase activity; activity or role: acetyl-CoA C-acyltransferase activity)
  - 6. boundary alkane/rubredoxin electron transfer
  - Alkane oxidation electron-transfer side nodes
    - Rubredoxin-NAD+ reductase (molecular player: rubredoxin-NAD+ reductase activity; activity or role: rubredoxin-NAD+ reductase activity)

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

Bacterial fatty acid beta-oxidation and acyl-CoA activation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00071
- Resolved ID: ppu00071
- Resolved name: Fatty acid degradation
- Source: KEGG

Resolved local bucket kegg:ppu00071 with 6 primary genes; module area: lipid_cell_envelope_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 22

- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary bucket kegg:ppu00626)
- fadE: PP_1893 | Q88LN6 | Acyl-coenzyme A dehydrogenase (EC 1.3.8.7) (EC 1.3.8.8) (EC 1.3.8.7; 1.3.8.8; primary bucket kegg:ppu00071)
- fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)
- fadA__Q88L01: PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- acd: PP_2216 | Q88KS3 | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane-1-carbonyl-CoA dehydrogenase) (EC 1.3.8.11; 3.13.1.4; primary bucket kegg:ppu00410)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_2437: PP_2437 | Q88K54 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC 1.3.8.8; primary bucket kegg:ppu00071)
- PP_2793: PP_2793 | Q88J56 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC 1.3.8.8; primary bucket kegg:ppu00071)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- PP_3725: PP_3725 | Q88GJ7 | Acyl-CoA dehydrogenase (primary bucket kegg:ppu00071)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)
- fadD-I: PP_4549 | Q88EB7 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)
- fadD-II: PP_4550 | Q88EB6 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- alkT: PP_5314 | Q88C69 | Rubredoxin-NAD(+) reductase (EC 1.18.1.1) (EC 1.18.1.1; primary bucket kegg:ppu00071)
- PP_5371: PP_5371 | Q88C12 | Rubredoxin/rubredoxin reductase (primary bucket kegg:ppu00071)

## Generic Module Context

### Working Scope

A bacterial fatty-acid degradation boundary module covering activation of free fatty acids to acyl-CoA thioesters, the FAD-dependent acyl-CoA dehydrogenase step, hydration and oxidation of enoyl/hydroxyacyl-CoA intermediates, and thiolytic cleavage to acetyl-CoA plus a shortened acyl-CoA. For Pseudomonas putida KT2440, KEGG ppu00071 also includes alkane/rubredoxin electron-transfer nodes and specialized CoA-thioester dehydrogenase paralogs; those should be treated as boundary context until module-level evidence resolves their role in fatty-acid degradation.

### Provisional Biological Outline

- Bacterial fatty acid beta-oxidation and acyl-CoA activation
  - 1. fatty-acid activation to acyl-CoA
  - Fatty acid to fatty acyl-CoA
    - Long-chain fatty acid-CoA ligase (molecular player: long-chain fatty acid-CoA ligase activity; activity or role: long-chain fatty acid-CoA ligase activity)
  - 2. FAD-dependent acyl-CoA dehydrogenation
  - Fatty acyl-CoA to trans-2-enoyl-CoA
    - Long-chain fatty acyl-CoA dehydrogenase (molecular player: long-chain fatty acyl-CoA dehydrogenase activity; activity or role: long-chain fatty acyl-CoA dehydrogenase activity)
    - Medium-chain fatty acyl-CoA dehydrogenase (molecular player: medium-chain fatty acyl-CoA dehydrogenase activity; activity or role: medium-chain fatty acyl-CoA dehydrogenase activity)
    - Acyl-CoA dehydrogenase-family activity (molecular player: acyl-CoA dehydrogenase activity; activity or role: acyl-CoA dehydrogenase activity)
  - 3. enoyl-CoA hydration
  - trans-2-enoyl-CoA to 3-hydroxyacyl-CoA
    - Enoyl-CoA hydratase (molecular player: enoyl-CoA hydratase activity; activity or role: enoyl-CoA hydratase activity)
  - 4. 3-hydroxyacyl-CoA oxidation
  - 3-hydroxyacyl-CoA to 3-ketoacyl-CoA
    - 3-hydroxyacyl-CoA dehydrogenase (molecular player: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
    - Long-chain 3-hydroxyacyl-CoA dehydrogenase (molecular player: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity; activity or role: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
  - 5. thiolytic cleavage to acetyl-CoA
  - 3-ketoacyl-CoA to acetyl-CoA plus shortened acyl-CoA
    - Acetyl-CoA C-acyltransferase / beta-ketothiolase (molecular player: acetyl-CoA C-acyltransferase activity; activity or role: acetyl-CoA C-acyltransferase activity)
  - 6. boundary alkane/rubredoxin electron transfer
  - Alkane oxidation electron-transfer side nodes
    - Rubredoxin-NAD+ reductase (molecular player: rubredoxin-NAD+ reductase activity; activity or role: rubredoxin-NAD+ reductase activity)

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

# Module Review: Bacterial Fatty Acid Beta-Oxidation and Acyl-CoA Activation in *Pseudomonas putida* KT2440

## 1. Executive Summary

The fatty acid β-oxidation pathway in *Pseudomonas putida* KT2440 (KEGG ppu00071) is fully satisfiable — all five core enzymatic steps (activation, dehydrogenation, hydration, oxidation, and thiolysis) are encoded in the genome and supported by direct experimental evidence. However, the current candidate gene list has significant gaps and over-annotations. Most critically, the two best-supported primary acyl-CoA dehydrogenases for fatty acid catabolism — PP_0368 (C10+ substrates) and PP_0370 (C6–C8 substrates) — are absent from the 22-gene candidate list, as are auxiliary CoA ligases PP_0763 and PP_4559, and the short-chain 3-hydroxyacyl-CoA dehydrogenase PP_3755 (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 12-15). Meanwhile, several candidates (gcdH/PP_0158, frmA/PP_1616, adhP/PP_3839, paaF/PP_3284) belong to unrelated pathways (lysine catabolism, formaldehyde metabolism, alcohol oxidation, phenylacetate degradation) and should be removed from the core ppu00071 module. The rubredoxin/rubredoxin reductase pair (alkT/PP_5314, PP_5371) is correctly flagged as a boundary component: these genes supply electrons for alkane monooxygenase systems but are not part of the β-oxidation cycle itself (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4, duque2022providingoctanedegradation pages 1-1).

A defining feature of *P. putida* KT2440 β-oxidation is extensive paralog redundancy, with genome-wide RB-TnSeq fitness profiling revealing chain-length-specialized enzymes at nearly every step (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7). This redundancy complicates homology-based annotation and means that the "primary" enzyme for each step depends on the chain length of the substrate being metabolized.

## 2. Target-Organism Pathway Definition

**Biochemical scope.** The core pathway converts free fatty acids (C4–C18) to acetyl-CoA through iterative cycles consisting of: (i) CoA thioester activation by acyl-CoA synthetases/ligases (EC 6.2.1.3); (ii) FAD-dependent dehydrogenation by acyl-CoA dehydrogenases (EC 1.3.8.7, 1.3.8.8); (iii) hydration by enoyl-CoA hydratases (EC 4.2.1.17); (iv) NAD⁺-dependent oxidation by 3-hydroxyacyl-CoA dehydrogenases (EC 1.1.1.35); and (v) thiolytic cleavage by 3-ketoacyl-CoA thiolases (EC 2.3.1.16) (mezzina2021engineeringnativeand pages 10-13).

**Neighboring pathways to exclude.** The following should be kept separate: (a) phenylacetate catabolism (paa pathway), which shares enoyl-CoA hydratase-family enzymes but operates on aromatic CoA-thioester intermediates; (b) the PHA biosynthesis cycle, which diverts β-oxidation intermediates via PhaJ (R-specific enoyl-CoA hydratases) and PhaC (PHA synthases); (c) glutaryl-CoA dehydrogenation (lysine degradation, kegg:ppu00380); (d) alkane/alkanol terminal oxidation, which feeds fatty acids into the β-oxidation cycle but is mechanistically distinct (williams2022anoverviewof pages 1-2, duque2022providingoctanedegradation pages 1-1).

**Database equivalents.** KEGG ppu00071 ("Fatty acid degradation") is the primary reference. MetaCyc pathway "fatty acid β-oxidation I" and GO:0006635 ("fatty acid beta-oxidation") are equivalent core definitions.

## 3. Expected Step Model

The following table summarizes the satisfiability assessment for each of the six provisional pathway steps in KT2440:

| Step Number | Step Name | Reaction | Status | Primary Gene(s) | Supporting Paralog(s) | Notes |
|---|---|---|---|---|---|---|
| 1 | Fatty-acid activation to acyl-CoA | Fatty acid + CoA + ATP -> fatty acyl-CoA + AMP + PPi | covered | fadD-I/PP_4549; fadD-II/PP_4550 | PP_0763; PP_4559 | Core step is clearly present in KT2440. PP_4549 is the major ligase for C7-C18 (likely also C6), while PP_4550 contributes especially on C6-C12/C8-C10 substrates. PP_0763 and PP_4559 support short-chain activation but are missing from the candidate metadata, so candidate-gene completeness for this step is incomplete despite pathway satisfiability being covered (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 12-15, mezzina2021engineeringnativeand pages 10-13, valencia2022engineeringpseudomonasputida pages 1-3) |
| 2 | FAD-dependent acyl-CoA dehydrogenation | Fatty acyl-CoA -> trans-2-enoyl-CoA | covered | PP_0368; PP_0370; PP_2437 | fadE/PP_1893; acd/PP_2216; PP_2793?; PP_3725? | This step is encoded, but the candidate list misses the best-supported primary ACADs PP_0368 (C10+) and PP_0370 (C6-C8), making the local metadata critically incomplete. PP_2437 is directly supported for C10-C14. PP_1893 is a bona fide ACAD candidate but appears secondary to PP_0368/PP_0370 in RB-TnSeq data; PP_2216 is more short-chain/specialized. PP_2793 and PP_3725 remain candidate_uncertain family members (mezzina2021engineeringnativeand pages 10-13, thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 12-15, guzik2014identificationandcharacterization pages 5-6, guzik2014identificationandcharacterization pages 1-2) |
| 3 | Enoyl-CoA hydration | trans-2-enoyl-CoA -> 3-hydroxyacyl-CoA | covered | fadB/PP_2136 | PP_2217 | PP_2136 is the main multifunctional FadB for C6+ substrates and covers the canonical hydration step. PP_2217 likely supports short-chain beta-oxidation, especially butyrate/hexanoate catabolism, rather than replacing PP_2136 as the main long-chain enzyme (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 12-15, mezzina2021engineeringnativeand pages 10-13) |
| 4 | 3-hydroxyacyl-CoA oxidation | 3-hydroxyacyl-CoA -> 3-ketoacyl-CoA | covered | fadB/PP_2136 | PP_3755; PP_2214? | PP_2136 also catalyzes the dehydrogenase step for the main cycle. A short-chain-biased dehydrogenase role is supported for PP_3755, which is missing from the candidate list. PP_2214 is discussed in the literature as an alternative/backup hydroxyacyl-CoA dehydrogenase-like component in the fadBAx region, but its exact contribution is less certain (thompson2020functionalanalysisof pages 12-15, mezzina2021engineeringnativeand pages 13-16, mezzina2021engineeringnativeand pages 10-13) |
| 5 | Thiolytic cleavage to acetyl-CoA plus shortened acyl-CoA | 3-ketoacyl-CoA + CoA -> acetyl-CoA + shortened acyl-CoA | covered | fadA/PP_2137; bktB/PP_3754 | PP_2215; PP_2051?; PP_0582?; PP_3355?; PP_4636? | PP_2137 is the primary long-chain thiolase, especially for C8+ substrates. PP_3754 is important for shorter-chain substrates (C5-C7, including butyrate branch behavior). PP_2215 likely acts as a backup/alternative thiolase in the fadBAx cluster. Other thiolase-family candidates in the metadata are weakly supported and should not be treated as primary without further evidence (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 13-16, thompson2020functionalanalysisof pages 12-15, mezzina2021engineeringnativeand pages 10-13) |
| 6 | Boundary alkane/rubredoxin electron transfer | NADH -> rubredoxin reductase -> rubredoxin -> alkane hydroxylase electron flow | not_expected_in_target_taxon | none for core beta-oxidation | alkT/PP_5314; PP_5371 | These genes are not part of the core fatty-acid beta-oxidation cycle. Instead, they belong to upstream alkane oxidation electron transfer. KT2440 does not natively encode the full alkane hydroxylase pathway for alkane growth, but native rubredoxin/reductase can support acquired alkane monooxygenase systems. For ppu00071 module curation, this row should be treated as boundary context rather than a required beta-oxidation step (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4, duque2022providingoctanedegradation pages 1-1) |


*Table: This table summarizes satisfiability of the six provisional fatty-acid degradation steps in Pseudomonas putida KT2440 and highlights important genes missing from the candidate metadata. It is useful for deciding which steps are genuinely covered versus where the local candidate list needs revision.*

### Key observations on step coverage

**Step 1 (Fatty acid activation):** FadD-I (PP_4549) is the dominant long-chain-fatty-acid–CoA ligase, catalyzing CoA ligation of C7–C18 (and likely C6) fatty acids with severe fitness defects observed upon its disruption. FadD-II (PP_4550) plays a secondary but important role, particularly on C6–C12 substrates and especially C8–C10 (thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 10-13, valencia2022engineeringpseudomonasputida pages 1-3). Valencia et al. (2022) exploited the differential substrate preferences of these two tandem ligases to engineer strains producing medium-chain free fatty acids (valencia2022engineeringpseudomonasputida pages 1-3). Two additional CoA ligases, PP_0763 and PP_4559, are required specifically for short-chain fatty acid activation (valerate, hexanoate) but are absent from the candidate list (thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 12-15).

**Step 2 (Acyl-CoA dehydrogenation):** This is the most paralog-rich step. The genome encodes at least 21 putative acyl-CoA dehydrogenases (ACADs) (guzik2014identificationandcharacterization pages 1-2). RB-TnSeq data identified PP_0368 as the primary ACAD for C10+ fatty acids and PP_0370 as preferred for C6–C8, with both showing roughly equal contribution on C9 (nonanoate) (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7). PP_2437 was characterized by Guzik et al. (2014) as an ACAD with preference for medium-to-long-chain (C10–C14) substrates (guzik2014identificationandcharacterization pages 5-6, guzik2014identificationandcharacterization pages 1-2). The annotated fadE (PP_1893) contains fadE multi-domains but appears to be secondary to PP_0368/PP_0370 in the RB-TnSeq fitness data (guzik2014identificationandcharacterization pages 5-6). Acd (PP_2216) handles short-chain acyl-CoAs (C4–C8) but showed no fitness defects as a single mutant, indicating redundancy (mezzina2021engineeringnativeand pages 10-13, thompson2020functionalanalysisof pages 12-15).

**Steps 3–4 (Enoyl-CoA hydration and 3-hydroxyacyl-CoA oxidation):** These two reactions are primarily catalyzed by the multifunctional FadB complex. PP_2136 (FadB) encodes four enzymatic activities: enoyl-CoA hydratase (EC 4.2.1.17), Δ³-cis-Δ²-trans-enoyl-CoA isomerase (EC 5.3.3.8), 3-hydroxyacyl-CoA epimerase (EC 5.1.2.3), and 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35) (mezzina2021engineeringnativeand pages 10-13). RB-TnSeq confirmed PP_2136 as the primary enzyme for C6+ substrates at both steps (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7). The alternative FadBx (PP_2214) and short-chain enoyl-CoA hydratase PP_2217 become important for shorter-chain substrates, particularly butyrate and hexanoate catabolism (thompson2020functionalanalysisof pages 12-15, mezzina2021engineeringnativeand pages 13-16). PP_3755 (3-hydroxybutyryl-CoA dehydrogenase) shows a preference for butyrate metabolism and is missing from the candidate list (thompson2020functionalanalysisof pages 12-15).

**Step 5 (Thiolytic cleavage):** FadA (PP_2137) is the primary 3-ketoacyl-CoA thiolase for long-chain substrates (C8+), while BktB (PP_3754) is important for short-chain substrates including C5–C7 (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 13-16). The alternative thiolase PP_2215 in the fadBAx cluster can partially compensate when the primary fadBA is deleted but is not the main enzyme under wild-type conditions (thompson2020functionalanalysisof pages 12-15, mezzina2021engineeringnativeand pages 10-13).

**Step 6 (Boundary alkane electron transfer):** AlkT (PP_5314) and the rubredoxin PP_5371 are not part of the β-oxidation cycle. They participate in alkane terminal oxidation electron transfer (NADH → rubredoxin reductase → rubredoxin → alkane monooxygenase). KT2440 does not natively encode an alkane monooxygenase (AlkB) and cannot grow on alkanes without acquisition of additional genes, although its native rubredoxin/reductase system can support horizontally acquired alkane hydroxylase function (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4, duque2022providingoctanedegradation pages 1-1).

## 4. Candidate Genes and Evidence

The detailed assessment of all 22 candidate genes is presented below:

| Gene Name | Locus Tag | UniProt | Pathway Step | Evidence Type | Confidence (High/Medium/Low) | Primary Bucket Correct? | Curation Notes |
|---|---|---|---|---|---|---|---|
| gcdH | PP_0158 | Q88RH2 | Not in core FA β-oxidation | Direct target-species genetics/biochemistry for lysine/glutarate catabolism | Low | No | Glutaryl-CoA dehydrogenase in lysine/glutarate degradation, not fatty-acid β-oxidation; remove from ppu00071 core set (thompson2020functionalanalysisof pages 12-15) |
| PP_0582 | PP_0582 | Q88QB2 | Candidate Step 5 thiolase only | Annotation only; no direct KT2440 β-oxidation evidence found | Low | Unclear/likely no | Generic thiolase family protein; likely over-propagated into ppu00071; prioritize other thiolases first |
| frmA | PP_1616 | Q88MF5 | Not in core FA β-oxidation | Annotation only | Low | No | Formaldehyde/alcohol dehydrogenase family protein; no evidence for acyl-CoA activation or β-oxidation role |
| fadE | PP_1893 | Q88LN6 | Step 2: acyl-CoA dehydrogenation | Direct target-species mutagenesis/fitness and ACAD study | Medium | Yes | Annotated fadE, but RB-TnSeq indicates PP_0368 and PP_0370 are the principal chain-length-specialized ACADs for many fatty acids; retain as ppu00071-associated but not primary core dehydrogenase for most substrates (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, guzik2014identificationandcharacterization pages 5-6) |
| fadA__Q88L84 | PP_2051 | Q88L84 | Candidate Step 5 thiolysis | Annotation only; locus-name discrepancy | Low | Likely no | Listed as fadA-like thiolase, but evidence favors PP_2137 as the primary long-chain β-ketothiolase; PP_2051 should not be treated as the main fadA without targeted review |
| fadB | PP_2136 | Q88L02 | Steps 3-4: enoyl-CoA hydration + 3-hydroxyacyl-CoA oxidation | Direct target-species fitness/genetic evidence | High | No | Primary FadB for C6+ substrates; multifunctional β-oxidation enzyme. Current primary bucket ppu00930 is too generic; should be promoted into ppu00071 core coverage (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 10-13) |
| fadA__Q88L01 | PP_2137 | Q88L01 | Step 5: thiolytic cleavage | Direct target-species fitness/genetic evidence | High | No | Primary long-chain 3-ketoacyl-CoA thiolase, especially C8+; current primary bucket ppu00592 is too broad, should map to ppu00071 core (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 10-13) |
| PP_2215 | PP_2215 | Q88KS4 | Step 5: alternative thiolase/FadAx complex | Direct target-species fitness/genetic evidence, but indirect role assignment | Medium | Unclear | Part of alternative fadBAx-like cluster (with PP_2217/PP_2216); likely backup/short-chain-associated thiolase activity rather than primary long-chain FadA (thompson2020functionalanalysisof pages 12-15, mezzina2021engineeringnativeand pages 10-13) |
| acd | PP_2216 | Q88KS3 | Step 2: short-chain acyl-CoA dehydrogenation | Direct target-species fitness/genetic evidence | Medium | No | Short-chain ACAD activity on ~C4-C8 acyl-CoAs; not major long-chain fadE equivalent. Current primary bucket ppu00410 reflects specialized role; include as ppu00071 short-chain branch/boundary candidate (mezzina2021engineeringnativeand pages 10-13, thompson2020functionalanalysisof pages 12-15) |
| PP_2217 | PP_2217 | Q88KS2 | Step 3: enoyl-CoA hydratase | Direct target-species fitness/genetic evidence | Medium | Yes | Part of fadBAx-like cluster; shows strongest phenotype in butyrate/hexanoate use, suggesting role in short-chain β-oxidation rather than main long-chain cycle (thompson2020functionalanalysisof pages 12-15) |
| PP_2437 | PP_2437 | Q88K54 | Step 2: medium/long-chain acyl-CoA dehydrogenation | Direct target-species mutagenesis/characterization | High | Yes | Functionally characterized ACAD with fadE2 domain; supports growth/PHA phenotypes on C10-C14 substrates and is a strong ppu00071 component (guzik2014identificationandcharacterization pages 5-6, guzik2014identificationandcharacterization pages 1-2) |
| PP_2793 | PP_2793 | Q88J56 | Candidate Step 2: ACAD | Annotation only | Low | Unclear | Annotated long-chain ACAD but no direct KT2440 evidence retrieved; candidate_uncertain for ppu00071 |
| paaF | PP_3284 | Q88HR9 | Not core FA β-oxidation | Annotation/homology to phenylacetate catabolism | Low | No | Enoyl-CoA hydratase-isomerase more plausibly belongs to phenylacetate/aromatic CoA catabolism than canonical fatty-acid degradation; likely over-annotated in ppu00071 |
| PP_3355 | PP_3355 | Q88HK1 | Candidate Step 5 thiolase | Annotation only | Low | Likely no | Generic beta-ketothiolase; no direct evidence for KT2440 fatty-acid β-oxidation role |
| PP_3725 | PP_3725 | Q88GJ7 | Candidate Step 2: ACAD | Annotation only | Low | Unclear | Acyl-CoA dehydrogenase family member with no direct KT2440 substrate evidence retrieved; candidate_uncertain |
| bktB | PP_3754 | Q88GH0 | Step 5: short-chain thiolytic cleavage | Direct target-species fitness/genetic evidence | High | No | Important thiolase for C5-C7/short-chain β-oxidation; particularly relevant in butyrate/hexanoate branch. Primary bucket ppu00900 is too generic; should be recognized in ppu00071 coverage (thompson2020functionalanalysisof pages 8-12, mezzina2021engineeringnativeand pages 13-16, thompson2020functionalanalysisof pages 12-15) |
| adhP | PP_3839 | Q88G86 | Not in core FA β-oxidation | Annotation only | Low | No | Short-chain alcohol dehydrogenase; no evidence for acyl-CoA pathway role |
| fadD-I | PP_4549 | Q88EB7 | Step 1: fatty-acid activation to acyl-CoA | Direct target-species fitness/genetics and recent engineering evidence | High | No | Major acyl-CoA ligase for C7-C18, likely also C6; current primary bucket ppu04146 is too narrow/off-target for module purposes and should also cover ppu00071 core activation step (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 10-13, valencia2022engineeringpseudomonasputida pages 1-3) |
| fadD-II | PP_4550 | Q88EB6 | Step 1: fatty-acid activation to acyl-CoA | Direct target-species fitness/genetics and recent engineering evidence | High | No | Secondary/chain-length-biased acyl-CoA ligase, strongest evidence for C6-C12 and especially C8-C10; should be included in ppu00071 activation coverage despite current ppu04146 assignment (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 10-13, valencia2022engineeringpseudomonasputida pages 1-3) |
| yqeF | PP_4636 | Q88E32 | Candidate Step 5 thiolase/acetyltransferase | Limited indirect target-species evidence | Low | Unclear | Acetyl-CoA acetyltransferase with weak/indirect association only; no strong evidence for canonical fatty-acid β-oxidation role in KT2440 (thompson2020functionalanalysisof pages 12-15) |
| alkT | PP_5314 | Q88C69 | Boundary alkane electron transfer, not β-oxidation core | Indirect/related-system evidence plus KT2440 transfer | Low | No | Rubredoxin-NAD+ reductase used for electron delivery to alkane monooxygenase systems; KT2440 uses native rubredoxin/reductase to support acquired octane oxidation, but this is upstream alkane activation, not fatty-acid β-oxidation proper (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4, duque2022providingoctanedegradation pages 1-1) |
| PP_5371 | PP_5371 | Q88C12 | Boundary alkane electron transfer, not β-oxidation core | Indirect/related-system evidence plus KT2440 transfer | Low | No | Rubredoxin/rubredoxin-reductase-like boundary component; likely relevant to alkane hydroxylation electron transfer rather than core ppu00071 β-oxidation steps (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4, duque2022providingoctanedegradation pages 1-1) |


*Table: This table summarizes the 22 candidate genes associated with KEGG ppu00071 in Pseudomonas putida KT2440, indicating which genes are high-confidence core beta-oxidation components, which are short-chain or backup functions, and which are likely boundary or over-propagated annotations.*

### High-confidence core β-oxidation genes (direct KT2440 evidence)

- **fadD-I / PP_4549** (Step 1): Major acyl-CoA ligase, C7–C18. Supported by RB-TnSeq fitness data and metabolic engineering studies (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 10-13, valencia2022engineeringpseudomonasputida pages 1-3).
- **fadD-II / PP_4550** (Step 1): Secondary ligase, strongest phenotype on C8–C10. Both fadD genes are currently mapped to ppu04146 (peroxisome) rather than ppu00071, which is inappropriate for a bacterial system (thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 10-13, valencia2022engineeringpseudomonasputida pages 1-3).
- **PP_2437** (Step 2): ACAD with fadE2 domain, characterized by direct mutagenesis and enzymatic assay in KT2440. Preference for C10–C14 substrates including dodecanoyl-CoA (C12) (guzik2014identificationandcharacterization pages 5-6, guzik2014identificationandcharacterization pages 1-2).
- **fadB / PP_2136** (Steps 3–4): Primary multifunctional β-oxidation complex subunit α for C6+ substrates. Currently mapped to ppu00930, which is too generic; should be promoted to ppu00071 core (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 10-13).
- **fadA / PP_2137** (Step 5): Primary long-chain 3-ketoacyl-CoA thiolase, especially C8+. Currently mapped to ppu00592; should be recognized in ppu00071 (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, mezzina2021engineeringnativeand pages 10-13).
- **bktB / PP_3754** (Step 5): Important short-chain thiolase for C5–C7, particularly butyrate catabolism. Currently mapped to ppu00900; should also be in ppu00071 (thompson2020functionalanalysisof pages 8-12, mezzina2021engineeringnativeand pages 13-16, thompson2020functionalanalysisof pages 12-15).

### Medium-confidence / secondary role genes

- **fadE / PP_1893** (Step 2): Annotated fadE with correct ACAD domains, but RB-TnSeq evidence places PP_0368 and PP_0370 as the primary chain-length-specialized ACADs. PP_1893 may have a role under specific conditions or substrates not fully tested (thompson2020functionalanalysisof pages 8-12, guzik2014identificationandcharacterization pages 5-6).
- **acd / PP_2216** (Step 2): Short-chain ACAD (C4–C8), part of the alternative fadBAx cluster (PP_2213–PP_2217). No single-mutant fitness defect observed, indicating redundancy (mezzina2021engineeringnativeand pages 10-13, thompson2020functionalanalysisof pages 12-15).
- **PP_2215** (Step 5): Alternative thiolase (FadAx) that becomes active when primary fadBA is deleted. Backup function (thompson2020functionalanalysisof pages 12-15, mezzina2021engineeringnativeand pages 10-13).
- **PP_2217** (Step 3): Enoyl-CoA hydratase in the fadBAx cluster; shows fitness defects on butyrate and hexanoate, suggesting short-chain specificity (thompson2020functionalanalysisof pages 12-15).

### Low-confidence / over-propagated annotations (should be removed or flagged)

- **gcdH / PP_0158**: Glutaryl-CoA dehydrogenase in lysine/tryptophan catabolism. Not fatty acid β-oxidation. Well-characterized in KT2440 as part of the glutarate degradation pathway (thompson2020functionalanalysisof pages 12-15).
- **frmA / PP_1616**: S-(hydroxymethyl)glutathione dehydrogenase / alcohol dehydrogenase class III. No role in β-oxidation.
- **adhP / PP_3839**: Short-chain alcohol dehydrogenase. Not acyl-CoA pathway.
- **paaF / PP_3284**: Enoyl-CoA hydratase-isomerase belonging to phenylacetate catabolism, not fatty acid β-oxidation.
- **PP_0582, PP_3355, PP_4636 (yqeF)**: Generic thiolase/acetyltransferase family members with no direct evidence for canonical fatty acid β-oxidation role in KT2440. Likely annotation over-propagation from broad EC/GO family assignments.
- **fadA (PP_2051 / Q88L84)**: Listed as a second fadA but evidence strongly favors PP_2137 as the primary long-chain thiolase. PP_2051's specific role in β-oxidation vs. other CoA-thioester pathways is unclear.
- **alkT / PP_5314, PP_5371**: Rubredoxin-NAD⁺ reductase and rubredoxin, respectively. These are alkane hydroxylase electron-transfer components, not β-oxidation enzymes. KT2440 natively encodes these but lacks AlkB; they support acquired alkane oxidation systems (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4, duque2022providingoctanedegradation pages 1-1).

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### Critical gaps in the candidate list

The most significant omission is the absence of **PP_0368** and **PP_0370**, which are the best-supported primary acyl-CoA dehydrogenases for fatty acid catabolism in KT2440 based on RB-TnSeq fitness data. PP_0368 is the primary ACAD for long-chain (C10+) fatty acids, while PP_0370 is preferred for medium-chain (C6–C8) substrates (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7). Additional missing genes include:
- **PP_0763**: CoA ligase required for both valerate (C5) and hexanoate (C6) activation (thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 12-15).
- **PP_4559**: CoA ligase required specifically for hexanoate (C6) activation (thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 12-15).
- **PP_3755**: 3-Hydroxybutyryl-CoA dehydrogenase with preference for butyrate metabolism (thompson2020functionalanalysisof pages 12-15).
- **PP_0767**: Transcription factor regulating expression of fatty acid catabolic genes; not an enzyme but functionally important (thompson2020fattyacidand pages 5-7).

### Over-annotations

At least 7 of the 22 candidate genes (gcdH, frmA, adhP, paaF, PP_0582, PP_3355, alkT) have primary roles outside fatty acid β-oxidation. Their inclusion in the ppu00071 candidate set likely reflects broad EC number propagation or the KEGG overview map including neighboring/boundary pathways. PP_5371 is similarly a boundary component.

### Paralog ambiguity

The *P. putida* KT2440 genome encodes extensive paralog families at every β-oxidation step: ~6 acyl-CoA ligases, 7+ acyl-CoA dehydrogenases, multiple enoyl-CoA hydratases, and 5+ thiolases contribute to fatty acid catabolism with chain-length-dependent substrate partitioning (mezzina2021engineeringnativeand pages 10-13, sharma2014genomefeaturesof pages 8-10). This redundancy means that single-gene deletions often show mild or no phenotype, making functional assignment via homology alone unreliable.

## 6. Module and GO-Curation Recommendations

### Step status recommendations

| Step | Recommended Status | Action Required |
|------|-------------------|-----------------|
| 1. Fatty acid activation | **covered** | Add PP_0763 and PP_4559 to candidate list; correct fadD-I/fadD-II primary bucket from ppu04146 to ppu00071 |
| 2. Acyl-CoA dehydrogenation | **covered** but candidate list critically incomplete | Add PP_0368 and PP_0370 as primary candidates; retain PP_2437; downgrade fadE/PP_1893 to secondary |
| 3. Enoyl-CoA hydration | **covered** | Correct fadB/PP_2136 primary bucket from ppu00930 to ppu00071 |
| 4. 3-Hydroxyacyl-CoA oxidation | **covered** | Same as Step 3 (both activities in FadB); add PP_3755 for short-chain branch |
| 5. Thiolytic cleavage | **covered** | Correct fadA/PP_2137 from ppu00592 and bktB/PP_3754 from ppu00900 to include ppu00071 |
| 6. Boundary alkane electron transfer | **not_expected_in_target_taxon** (for β-oxidation module) | Remove alkT/PP_5314 and PP_5371 from core module; retain as boundary context only |

### Genes to remove from ppu00071 core

gcdH (PP_0158), frmA (PP_1616), adhP (PP_3839), paaF (PP_3284). These belong definitively to other pathways.

### Module boundary revision

The current KEGG ppu00071 map includes alkane/rubredoxin electron-transfer nodes that are not part of β-oxidation *sensu stricto*. For a curated module definition, these should be separated into a distinct alkane terminal oxidation module or kept as clearly labeled boundary context. The β-oxidation module should terminate at the fatty acid → acyl-CoA activation step and should not extend upstream to alkane hydroxylation.

### GO term considerations

The existing GO term GO:0006635 ("fatty acid beta-oxidation") is appropriate for the core pathway. However, the chain-length specialization observed in KT2440 (with different enzyme sets handling C4–C8 vs. C10–C18) may warrant sub-annotation. GO:0033539 ("fatty acid beta-oxidation using acyl-CoA dehydrogenase") is the appropriate child term.

## 7. Genes to Promote to Full Review

The following genes warrant detailed `fetch-gene` review:

1. **PP_0368** — Primary long-chain acyl-CoA dehydrogenase (C10+). Not in current candidate list but has the strongest RB-TnSeq phenotype for this step. Critical for module completeness.
2. **PP_0370** — Primary medium-chain acyl-CoA dehydrogenase (C6–C8). Same justification as PP_0368.
3. **fadD-I / PP_4549** — Primary fatty acid–CoA ligase. Well characterized but currently assigned to wrong primary bucket (ppu04146). Needs bucket correction.
4. **fadD-II / PP_4550** — Secondary CoA ligase. Same bucket correction needed; tandem arrangement with fadD-I is biologically significant.
5. **PP_2437** — Directly characterized ACAD with fadE2 domain. Confirmed medium-to-long-chain preference. Good candidate for detailed review to distinguish from PP_0368.
6. **fadB / PP_2136** — Multifunctional complex subunit. Needs primary bucket reassignment from ppu00930 to ppu00071.
7. **fadA / PP_2137** — Primary long-chain thiolase. Needs primary bucket reassignment from ppu00592 to ppu00071.

## 8. Key References

The principal evidence base for this review derives from:

- **Thompson et al. (2020)** — RB-TnSeq fitness profiling of *P. putida* KT2440 grown on 13 fatty acids and 10 alcohols. This is the single most informative study for functional assignment of β-oxidation paralogs, providing genome-wide fitness data with chain-length resolution (thompson2020functionalanalysisof pages 8-12, thompson2020fattyacidand pages 5-7, thompson2020functionalanalysisof pages 12-15). Published in *Applied and Environmental Microbiology* 86:e01665-20 (DOI: 10.1128/aem.01665-20).

- **Mezzina et al. (2021)** — Comprehensive review of native and synthetic pathways for PHA production in *P. putida*, including detailed discussion of all β-oxidation enzyme paralogs (mezzina2021engineeringnativeand pages 10-13, mezzina2021engineeringnativeand pages 13-16). Published in *Biotechnology Journal* 16:2000165 (DOI: 10.1002/biot.202000165).

- **Guzik et al. (2014)** — Direct biochemical characterization of ACADs in KT2440, identifying four putative ACADs (PP_1893, PP_2039, PP_2048, PP_2437) and demonstrating PP_2437 preference for medium-to-long-chain substrates (guzik2014identificationandcharacterization pages 5-6, guzik2014identificationandcharacterization pages 1-2). Published in *Microbiology* 160:1760-71 (DOI: 10.1099/mic.0.078758-0).

- **Valencia et al. (2022)** — Engineering of KT2440 for free fatty acid and oleochemical production, exploiting differential FadD substrate preferences (valencia2022engineeringpseudomonasputida pages 1-3). Published in *Communications Biology* 5:1 (DOI: 10.1038/s42003-022-04336-2).

- **Liu et al. (2023)** — Revisited β-oxidation–PHA synthesis relationship in KT2440, characterizing PhaJ hydratases and their role in diverting β-oxidation intermediates to PHA. Published in *Applied Microbiology and Biotechnology* 107:1863-1874 (DOI: 10.1007/s00253-023-12413-7).

- **Duque et al. (2022)** — Demonstrated that KT2440 requires horizontal acquisition of alkane monooxygenase genes for octane degradation, with native rubredoxin/reductase supporting electron transfer (duque2022providingoctanedegradation pages 1-1). Published in *Environmental Microbiology Reports* 14:934-946 (DOI: 10.1111/1758-2229.13097).

- **Williams & Austin (2022)** — Review of electron-transfer proteins activating AlkB alkane monooxygenase, clarifying the AlkT/AlkG system relevant to boundary assessment (williams2022anoverviewof pages 1-2, williams2022anoverviewof pages 2-4). Published in *Frontiers in Microbiology* 13:845551 (DOI: 10.3389/fmicb.2022.845551).

- **Sharma et al. (2014)** — Comparative genomics of *P. putida* strains showing conservation of fad gene families across the species, with 4–7 paralogs per step (sharma2014genomefeaturesof pages 8-10). Published in *AMB Express* 4:37 (DOI: 10.1186/s13568-014-0037-8).

- **Salvachúa et al. (2020)** — Metabolic engineering for PHA production from lignin, including fadBA1 and fadBA2 deletion studies demonstrating their role in β-oxidation flux control. Published in *Microbial Biotechnology* 13:290-298 (DOI: 10.1111/1751-7915.13481).

---

**Summary of uncertainty.** The strongest evidence comes from direct *P. putida* KT2440 experiments (RB-TnSeq, gene knockouts, enzyme characterization). Where evidence is from other *P. putida* strains (e.g., LS46, U, GPo1), transfer to KT2440 is generally strong due to >86% genome identity and highly conserved fad gene families across strains (sharma2014genomefeaturesof pages 8-10). Evidence from *E. coli* or *P. aeruginosa* β-oxidation should be transferred with caution, as these organisms have simpler, less redundant fad systems. The principal open question remains the precise substrate range and relative contribution of the many paralogous ACADs (especially PP_0368, PP_0370, PP_1893, PP_2437, PP_2793, PP_3725) under physiological conditions, which would benefit from systematic in vitro kinetic characterization.

References

1. (thompson2020functionalanalysisof pages 8-12): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Functional analysis of the fatty acid and alcohol metabolism of pseudomonas putida using rb-tnseq. bioRxiv, Jul 2020. URL: https://doi.org/10.1101/2020.07.04.188060, doi:10.1101/2020.07.04.188060. This article has 3 citations.

2. (thompson2020fattyacidand pages 5-7): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Fatty acid and alcohol metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Oct 2020. URL: https://doi.org/10.1128/aem.01665-20, doi:10.1128/aem.01665-20. This article has 116 citations and is from a peer-reviewed journal.

3. (thompson2020functionalanalysisof pages 12-15): Mitchell G. Thompson, Matthew R. Incha, Allison N. Pearson, Matthias Schmidt, William A. Sharpless, Christopher B. Eiben, Pablo Cruz-Morales, Jacquelyn M. Blake-Hedges, Yuzhong Liu, Catharine A. Adams, Robert W. Haushalter, Rohith N. Krishna, Patrick Lichtner, Lars M. Blank, Aindrila Mukhopadhyay, Adam M. Deutschbauer, Patrick M. Shih, and Jay D. Keasling. Functional analysis of the fatty acid and alcohol metabolism of pseudomonas putida using rb-tnseq. bioRxiv, Jul 2020. URL: https://doi.org/10.1101/2020.07.04.188060, doi:10.1101/2020.07.04.188060. This article has 3 citations.

4. (williams2022anoverviewof pages 1-2): Shoshana C. Williams and Rachel Narehood Austin. An overview of the electron-transfer proteins that activate alkane monooxygenase (alkb). Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2022.845551, doi:10.3389/fmicb.2022.845551. This article has 43 citations and is from a peer-reviewed journal.

5. (williams2022anoverviewof pages 2-4): Shoshana C. Williams and Rachel Narehood Austin. An overview of the electron-transfer proteins that activate alkane monooxygenase (alkb). Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2022.845551, doi:10.3389/fmicb.2022.845551. This article has 43 citations and is from a peer-reviewed journal.

6. (duque2022providingoctanedegradation pages 1-1): Estrella Duque, Zulema Udaondo, Lázaro Molina, Jesús de la Torre, Patricia Godoy, and Juan L. Ramos. Providing octane degradation capability to pseudomonas putida kt2440 through the horizontal acquisition of oct genes located on an integrative and conjugative element. Environmental Microbiology Reports, 14:934-946, Jun 2022. URL: https://doi.org/10.1111/1758-2229.13097, doi:10.1111/1758-2229.13097. This article has 19 citations and is from a peer-reviewed journal.

7. (mezzina2021engineeringnativeand pages 10-13): Mariela P. Mezzina, María Tsampika Manoli, M. Auxiliadora Prieto, and Pablo I. Nikel. Engineering native and synthetic pathways in <i>pseudomonas putida</i> for the production of tailored polyhydroxyalkanoates. Biotechnology Journal, Nov 2021. URL: https://doi.org/10.1002/biot.202000165, doi:10.1002/biot.202000165. This article has 150 citations and is from a peer-reviewed journal.

8. (valencia2022engineeringpseudomonasputida pages 1-3): Luis E. Valencia, Matthew R. Incha, Matthias Schmidt, Allison N. Pearson, Mitchell G. Thompson, Jacob B. Roberts, Marina Mehling, Kevin Yin, Ning Sun, Asun Oka, Patrick M. Shih, Lars M. Blank, John Gladden, and Jay D. Keasling. Engineering pseudomonas putida kt2440 for chain length tailored free fatty acid and oleochemical production. Communications Biology, Dec 2022. URL: https://doi.org/10.1038/s42003-022-04336-2, doi:10.1038/s42003-022-04336-2. This article has 23 citations and is from a peer-reviewed journal.

9. (guzik2014identificationandcharacterization pages 5-6): Maciej W. Guzik, Tanja Narancic, Tatjana Ilic-Tomic, Sandra Vojnovic, Shane T. Kenny, William T. Casey, Gearoid F. Duane, Eoin Casey, Trevor Woods, Ramesh Padamati Babu, Jasmina Nikodinovic-Runic, and Kevin E. O’Connor. Identification and characterization of an acyl-coa dehydrogenase from pseudomonas putida kt2440 that shows preference towards medium to long chain length fatty acids. Microbiology, 160 Pt 8:1760-71, Aug 2014. URL: https://doi.org/10.1099/mic.0.078758-0, doi:10.1099/mic.0.078758-0. This article has 32 citations and is from a peer-reviewed journal.

10. (guzik2014identificationandcharacterization pages 1-2): Maciej W. Guzik, Tanja Narancic, Tatjana Ilic-Tomic, Sandra Vojnovic, Shane T. Kenny, William T. Casey, Gearoid F. Duane, Eoin Casey, Trevor Woods, Ramesh Padamati Babu, Jasmina Nikodinovic-Runic, and Kevin E. O’Connor. Identification and characterization of an acyl-coa dehydrogenase from pseudomonas putida kt2440 that shows preference towards medium to long chain length fatty acids. Microbiology, 160 Pt 8:1760-71, Aug 2014. URL: https://doi.org/10.1099/mic.0.078758-0, doi:10.1099/mic.0.078758-0. This article has 32 citations and is from a peer-reviewed journal.

11. (mezzina2021engineeringnativeand pages 13-16): Mariela P. Mezzina, María Tsampika Manoli, M. Auxiliadora Prieto, and Pablo I. Nikel. Engineering native and synthetic pathways in <i>pseudomonas putida</i> for the production of tailored polyhydroxyalkanoates. Biotechnology Journal, Nov 2021. URL: https://doi.org/10.1002/biot.202000165, doi:10.1002/biot.202000165. This article has 150 citations and is from a peer-reviewed journal.

12. (sharma2014genomefeaturesof pages 8-10): Parveen K Sharma, Jilagamazhi Fu, Xiangli Zhang, Brian Fristensky, Richard Sparling, and David B Levin. Genome features of pseudomonas putida ls46, a novel polyhydroxyalkanoate producer and its comparison with other p. putida strains. AMB Express, May 2014. URL: https://doi.org/10.1186/s13568-014-0037-8, doi:10.1186/s13568-014-0037-8. This article has 32 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__bacterial_fatty_acid_beta_oxidation__ppu00071-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__bacterial_fatty_acid_beta_oxidation__ppu00071-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. mezzina2021engineeringnativeand pages 10-13
2. valencia2022engineeringpseudomonasputida pages 1-3
3. guzik2014identificationandcharacterization pages 1-2
4. guzik2014identificationandcharacterization pages 5-6
5. thompson2020functionalanalysisof pages 12-15
6. thompson2020fattyacidand pages 5-7
7. duque2022providingoctanedegradation pages 1-1
8. sharma2014genomefeaturesof pages 8-10
9. thompson2020functionalanalysisof pages 8-12
10. williams2022anoverviewof pages 1-2
11. williams2022anoverviewof pages 2-4
12. mezzina2021engineeringnativeand pages 13-16
13. Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)
14. https://doi.org/10.1101/2020.07.04.188060,
15. https://doi.org/10.1128/aem.01665-20,
16. https://doi.org/10.3389/fmicb.2022.845551,
17. https://doi.org/10.1111/1758-2229.13097,
18. https://doi.org/10.1002/biot.202000165,
19. https://doi.org/10.1038/s42003-022-04336-2,
20. https://doi.org/10.1099/mic.0.078758-0,
21. https://doi.org/10.1186/s13568-014-0037-8,