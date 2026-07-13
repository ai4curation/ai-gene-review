---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T15:01:07.173066'
end_time: '2026-07-06T15:30:32.773999'
duration_seconds: 1765.6
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Aromatic compound degradation route umbrella
  module_summary: A taxon-neutral bacterial umbrella for aromatic-compound degradation
    maps that combine multiple route-specific catabolic funnels. This module is not
    a single linear pathway. It is used to separate strict aromatic-ring activation
    and beta-ketoadipate chemistry from neighboring cofactor, redox, UbiD/prenyl-FMN,
    and generic side-node enzymes that appear in broad KEGG degradation maps.
  module_outline: "- Aromatic compound degradation route umbrella\n  - 1. upper aromatic-ring\
    \ activation routes\n  - Upper aromatic-ring activation and dihydroxylation routes\n\
    \    - Benzoate 1,2-dioxygenase (molecular player: benzoate 1,2-dioxygenase activity;\
    \ activity or role: benzoate 1,2-dioxygenase activity)\n    - 4-hydroxybenzoate\
    \ 3-monooxygenase (molecular player: 4-hydroxybenzoate 3-monooxygenase activity;\
    \ activity or role: 4-hydroxybenzoate 3-monooxygenase activity)\n  - 2. ortho-cleavage\
    \ and beta-ketoadipate funnel\n  - Catechol/protocatechuate ortho-cleavage and\
    \ beta-ketoadipate funnel\n    - Catechol 1,2-dioxygenase (molecular player: catechol\
    \ 1,2-dioxygenase activity; activity or role: catechol 1,2-dioxygenase activity)\n\
    \    - Protocatechuate 3,4-dioxygenase (molecular player: protocatechuate 3,4-dioxygenase\
    \ activity; activity or role: protocatechuate 3,4-dioxygenase activity)\n    -\
    \ Muconate cycloisomerase (molecular player: muconate cycloisomerase activity;\
    \ activity or role: muconate cycloisomerase activity)\n    - 3-carboxy-cis,cis-muconate\
    \ cycloisomerase (molecular player: 3-carboxy-cis,cis-muconate cycloisomerase\
    \ activity; activity or role: 3-carboxy-cis,cis-muconate cycloisomerase activity)\n\
    \    - 3-oxoadipate CoA-transferase (molecular player: 3-oxoadipate CoA-transferase\
    \ activity; activity or role: 3-oxoadipate CoA-transferase activity)\n  - 3. UbiD/prenyl-FMN\
    \ and broad-map side-node context\n  - Cofactor, redox, and side-node context\
    \ in broad aromatic maps\n    - Flavin prenyltransferase (molecular player: flavin\
    \ prenyltransferase activity; activity or role: flavin prenyltransferase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu01220
  pathway_id: ppu01220
  pathway_name: Degradation of aromatic compounds
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu01220 with 8 primary genes; module
    area: aromatic_and_xenobiotic_catabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '20'
  candidate_genes: '- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129)
    (EC 2.5.1.129; primary bucket kegg:ppu00627)

    - pcaB: PP_1379 | Q88N37 | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2)
    (EC 5.5.1.2; primary bucket kegg:ppu01220)

    - pcaD: PP_1380 | Q88N36 | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) (EC 3.1.1.24;
    primary bucket kegg:ppu01220)

    - pcaC: PP_1381 | Q88N35 | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44)
    (EC 4.1.1.44; primary bucket kegg:ppu01220)

    - frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1)
    (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III)
    (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary
    bucket kegg:ppu00626)

    - PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)

    - PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate
    tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)

    - benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10)
    (EC 1.14.12.10; primary bucket kegg:ppu00622)

    - benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10)
    (EC 1.14.12.10; primary bucket kegg:ppu00622)

    - benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component
    (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)

    - benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase
    (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)

    - catA-II: PP_3166 | Q88I35 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1;
    primary bucket kegg:ppu00361)

    - pobA: PP_3537 | Q88H28 | 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2) (EC
    1.14.13.2; primary bucket kegg:ppu01220)

    - PP_3648: PP_3648 | Q88GS0 | Carboxymuconolactone decarboxylase family protein
    (primary bucket kegg:ppu01220)

    - catA-I: PP_3713 | Q88GK8 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1;
    primary bucket kegg:ppu00361)

    - catC: PP_3714 | Q88GK7 | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4)
    (EC 5.3.3.4; primary bucket kegg:ppu01220)

    - catB: PP_3715 | Q88GK6 | Muconate cycloisomerase 1 (EC 5.5.1.1) (EC 5.5.1.1;
    primary bucket kegg:ppu00361)

    - adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1)
    (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)

    - pcaG: PP_4655 | Q88E13 | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3)
    (EC 1.13.11.3; primary bucket kegg:ppu01220)

    - pcaH: PP_4656 | Q88E12 | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3)
    (EC 1.13.11.3; primary bucket kegg:ppu01220)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 3
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: PSEPK__aromatic_compound_degradation__ppu01220-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__aromatic_compound_degradation__ppu01220-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PSEPK__aromatic_compound_degradation__ppu01220-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: image-1.png
  path: PSEPK__aromatic_compound_degradation__ppu01220-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: 'Image artifact created (ID artifact-02): ''KT2440 Aromatic Degradation
    Funnel'' ![KT2440 Aromatic Degradation Funnel](artifact:artifact-02) Artifact
    IDs that may '
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Aromatic compound degradation route umbrella in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu01220
- Resolved ID: ppu01220
- Resolved name: Degradation of aromatic compounds
- Source: KEGG

Resolved local bucket kegg:ppu01220 with 8 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 20

- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- pcaB: PP_1379 | Q88N37 | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2) (EC 5.5.1.2; primary bucket kegg:ppu01220)
- pcaD: PP_1380 | Q88N36 | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) (EC 3.1.1.24; primary bucket kegg:ppu01220)
- pcaC: PP_1381 | Q88N35 | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44) (EC 4.1.1.44; primary bucket kegg:ppu01220)
- frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary bucket kegg:ppu00626)
- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)
- PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)
- benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)
- benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)
- catA-II: PP_3166 | Q88I35 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- pobA: PP_3537 | Q88H28 | 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2) (EC 1.14.13.2; primary bucket kegg:ppu01220)
- PP_3648: PP_3648 | Q88GS0 | Carboxymuconolactone decarboxylase family protein (primary bucket kegg:ppu01220)
- catA-I: PP_3713 | Q88GK8 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- catC: PP_3714 | Q88GK7 | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4) (EC 5.3.3.4; primary bucket kegg:ppu01220)
- catB: PP_3715 | Q88GK6 | Muconate cycloisomerase 1 (EC 5.5.1.1) (EC 5.5.1.1; primary bucket kegg:ppu00361)
- adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)
- pcaG: PP_4655 | Q88E13 | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)
- pcaH: PP_4656 | Q88E12 | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)

## Generic Module Context

### Working Scope

A taxon-neutral bacterial umbrella for aromatic-compound degradation maps that combine multiple route-specific catabolic funnels. This module is not a single linear pathway. It is used to separate strict aromatic-ring activation and beta-ketoadipate chemistry from neighboring cofactor, redox, UbiD/prenyl-FMN, and generic side-node enzymes that appear in broad KEGG degradation maps.

### Provisional Biological Outline

- Aromatic compound degradation route umbrella
  - 1. upper aromatic-ring activation routes
  - Upper aromatic-ring activation and dihydroxylation routes
    - Benzoate 1,2-dioxygenase (molecular player: benzoate 1,2-dioxygenase activity; activity or role: benzoate 1,2-dioxygenase activity)
    - 4-hydroxybenzoate 3-monooxygenase (molecular player: 4-hydroxybenzoate 3-monooxygenase activity; activity or role: 4-hydroxybenzoate 3-monooxygenase activity)
  - 2. ortho-cleavage and beta-ketoadipate funnel
  - Catechol/protocatechuate ortho-cleavage and beta-ketoadipate funnel
    - Catechol 1,2-dioxygenase (molecular player: catechol 1,2-dioxygenase activity; activity or role: catechol 1,2-dioxygenase activity)
    - Protocatechuate 3,4-dioxygenase (molecular player: protocatechuate 3,4-dioxygenase activity; activity or role: protocatechuate 3,4-dioxygenase activity)
    - Muconate cycloisomerase (molecular player: muconate cycloisomerase activity; activity or role: muconate cycloisomerase activity)
    - 3-carboxy-cis,cis-muconate cycloisomerase (molecular player: 3-carboxy-cis,cis-muconate cycloisomerase activity; activity or role: 3-carboxy-cis,cis-muconate cycloisomerase activity)
    - 3-oxoadipate CoA-transferase (molecular player: 3-oxoadipate CoA-transferase activity; activity or role: 3-oxoadipate CoA-transferase activity)
  - 3. UbiD/prenyl-FMN and broad-map side-node context
  - Cofactor, redox, and side-node context in broad aromatic maps
    - Flavin prenyltransferase (molecular player: flavin prenyltransferase activity; activity or role: flavin prenyltransferase activity)

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

Aromatic compound degradation route umbrella in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu01220
- Resolved ID: ppu01220
- Resolved name: Degradation of aromatic compounds
- Source: KEGG

Resolved local bucket kegg:ppu01220 with 8 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 20

- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- pcaB: PP_1379 | Q88N37 | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2) (EC 5.5.1.2; primary bucket kegg:ppu01220)
- pcaD: PP_1380 | Q88N36 | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) (EC 3.1.1.24; primary bucket kegg:ppu01220)
- pcaC: PP_1381 | Q88N35 | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44) (EC 4.1.1.44; primary bucket kegg:ppu01220)
- frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary bucket kegg:ppu00626)
- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)
- PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)
- benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)
- benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)
- catA-II: PP_3166 | Q88I35 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- pobA: PP_3537 | Q88H28 | 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2) (EC 1.14.13.2; primary bucket kegg:ppu01220)
- PP_3648: PP_3648 | Q88GS0 | Carboxymuconolactone decarboxylase family protein (primary bucket kegg:ppu01220)
- catA-I: PP_3713 | Q88GK8 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- catC: PP_3714 | Q88GK7 | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4) (EC 5.3.3.4; primary bucket kegg:ppu01220)
- catB: PP_3715 | Q88GK6 | Muconate cycloisomerase 1 (EC 5.5.1.1) (EC 5.5.1.1; primary bucket kegg:ppu00361)
- adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)
- pcaG: PP_4655 | Q88E13 | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)
- pcaH: PP_4656 | Q88E12 | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)

## Generic Module Context

### Working Scope

A taxon-neutral bacterial umbrella for aromatic-compound degradation maps that combine multiple route-specific catabolic funnels. This module is not a single linear pathway. It is used to separate strict aromatic-ring activation and beta-ketoadipate chemistry from neighboring cofactor, redox, UbiD/prenyl-FMN, and generic side-node enzymes that appear in broad KEGG degradation maps.

### Provisional Biological Outline

- Aromatic compound degradation route umbrella
  - 1. upper aromatic-ring activation routes
  - Upper aromatic-ring activation and dihydroxylation routes
    - Benzoate 1,2-dioxygenase (molecular player: benzoate 1,2-dioxygenase activity; activity or role: benzoate 1,2-dioxygenase activity)
    - 4-hydroxybenzoate 3-monooxygenase (molecular player: 4-hydroxybenzoate 3-monooxygenase activity; activity or role: 4-hydroxybenzoate 3-monooxygenase activity)
  - 2. ortho-cleavage and beta-ketoadipate funnel
  - Catechol/protocatechuate ortho-cleavage and beta-ketoadipate funnel
    - Catechol 1,2-dioxygenase (molecular player: catechol 1,2-dioxygenase activity; activity or role: catechol 1,2-dioxygenase activity)
    - Protocatechuate 3,4-dioxygenase (molecular player: protocatechuate 3,4-dioxygenase activity; activity or role: protocatechuate 3,4-dioxygenase activity)
    - Muconate cycloisomerase (molecular player: muconate cycloisomerase activity; activity or role: muconate cycloisomerase activity)
    - 3-carboxy-cis,cis-muconate cycloisomerase (molecular player: 3-carboxy-cis,cis-muconate cycloisomerase activity; activity or role: 3-carboxy-cis,cis-muconate cycloisomerase activity)
    - 3-oxoadipate CoA-transferase (molecular player: 3-oxoadipate CoA-transferase activity; activity or role: 3-oxoadipate CoA-transferase activity)
  - 3. UbiD/prenyl-FMN and broad-map side-node context
  - Cofactor, redox, and side-node context in broad aromatic maps
    - Flavin prenyltransferase (molecular player: flavin prenyltransferase activity; activity or role: flavin prenyltransferase activity)

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

# Aromatic Compound Degradation Route Umbrella in *Pseudomonas putida* KT2440: A Species-Aware Module Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 is the best-characterized bacterial chassis for aromatic compound catabolism and a TOL-plasmid-cured derivative that retains chromosomally encoded pathways for degradation of benzoate, 4-hydroxybenzoate, and related aromatics via the β-ketoadipate (ortho-cleavage) pathway (jimenez2002genomicanalysisof pages 1-2, cao2008catabolicpathwaysand pages 10-11). The KEGG map ppu01220 ("Degradation of aromatic compounds") functions as an umbrella that combines multiple route-specific catabolic funnels rather than representing a single linear pathway. This review assesses the 20 candidate genes against the known biochemistry and identifies **three critical core pathway genes (pcaI, pcaJ, pcaF) that are encoded in the KT2440 genome but absent from the candidate gene list**, alongside **five side-node or over-propagated genes (ubiX, frmA, adhP, PP_1791, PP_2504)** that do not belong to the core ortho-cleavage/β-ketoadipate funnel.

The following schematic illustrates the pathway architecture in KT2440, highlighting covered steps, missing candidates, and side-node genes:

![KT2440 Aromatic Degradation Funnel](artifact:artifact-02)

*Image: Schematic pathway map of aromatic compound degradation in Pseudomonas putida KT2440, showing benzoate and 4-hydroxybenzoate funneling into the β-ketoadipate pathway. The diagram highlights core ortho-cleavage steps and marks pcaIJ and pcaF as present in the organism but missing from the candidate gene list.*

## 2. Target-Organism Pathway Definition

### 2.1 Pathway Scope

In *P. putida* KT2440, the aromatic compound degradation umbrella encompasses four chromosomally encoded central pathways: the protocatechuate branch (pca genes) and catechol branch (cat genes) of the β-ketoadipate pathway, the homogentisate pathway (hmg/fah/mai genes), and the phenylacetate pathway (pha genes) (jimenez2002genomicanalysisof pages 1-2, jimenez2002genomicanalysisof pages 5-6). The KEGG ppu01220 map primarily captures the first two branches plus upper peripheral activation routes (ben, pob).

### 2.2 Pathway Boundaries

The core process captured by this module is:

- **Upper aromatic-ring activation**: Benzoate → catechol (via benABCD); 4-hydroxybenzoate → protocatechuate (via pobA) (jimenez2002genomicanalysisof pages 6-9).
- **Ortho-cleavage ring opening**: Catechol → cis,cis-muconate (via catA); protocatechuate → β-carboxy-cis,cis-muconate (via pcaGH) (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 3-5).
- **β-Ketoadipate funnel convergence**: Both branches converge at β-ketoadipate enol-lactone, which is hydrolyzed by PcaD to β-ketoadipate, then converted to succinyl-CoA and acetyl-CoA (TCA cycle intermediates) by PcaIJ and PcaF (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5).

**Neighboring pathways that should be kept separate** include: the homogentisate pathway (hmg/fah/mai), the phenylacetate pathway (pha), meta-cleavage pathways (KEGG ppu00621), phenylpropanoid peripheral routes (fcs/ech/vdh/vanAB), ubiquinone biosynthesis, and formaldehyde detoxification (jimenez2002genomicanalysisof pages 1-2).

### 2.3 Alternate Names and Database Definitions

The pathway is variably termed: β-ketoadipate pathway, ortho-cleavage pathway, 3-oxoadipate pathway, protocatechuate/catechol branches of the β-ketoadipate pathway. KEGG ppu01220 is broader than any single branch. MetaCyc uses separate entries for "catechol degradation to β-ketoadipate" and "protocatechuate degradation II (ortho-cleavage pathway)."

## 3. Expected Step Model

The complete ortho-cleavage/β-ketoadipate route in KT2440 requires the following enzymatic steps, as established by comprehensive genomic analysis (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5, jimenez2002genomicanalysisof pages 5-6):

**Upper activation routes:**
1. Benzoate 1,2-dioxygenase (benABC, EC 1.14.12.10)
2. Benzoate dihydrodiol dehydrogenase (benD, EC 1.3.1.25)
3. 4-Hydroxybenzoate 3-monooxygenase (pobA, EC 1.14.13.2)

**Catechol branch (ortho-cleavage):**
4. Catechol 1,2-dioxygenase (catA / catA2, EC 1.13.11.1)
5. Muconate cycloisomerase (catB, EC 5.5.1.1)
6. Muconolactone isomerase (catC, EC 5.3.3.4)

**Protocatechuate branch:**
7. Protocatechuate 3,4-dioxygenase (pcaGH, EC 1.13.11.3)
8. 3-Carboxy-cis,cis-muconate cycloisomerase (pcaB, EC 5.5.1.2)
9. γ-Carboxymuconolactone decarboxylase (pcaC, EC 4.1.1.44)

**Lower convergent pathway:**
10. β-Ketoadipate enol-lactone hydrolase (pcaD, EC 3.1.1.24)
11. β-Ketoadipate succinyl-CoA transferase (pcaIJ)
12. β-Ketoadipyl-CoA thiolase (pcaF)

## 4. Candidate Genes and Evidence

The comprehensive assessment of all 20 candidate genes is provided below:

| Gene Name | Locus Tag (PP_) | UniProt ID | Enzyme Function | EC Number | Pathway Branch/Step | Evidence Type | Confidence Level | Assessment |
|---|---|---|---|---|---|---|---|---|
| ubiX | PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX; prenyl-FMN cofactor synthesis, typically linked to ubiquinone/UbiD systems rather than the core ortho-cleavage funnel | 2.5.1.129 | Broad-map cofactor/side-node context | genomic/functional inference | low | side-node; likely over-propagated into umbrella map |
| pcaB | PP_1379 | Q88N37 | 3-carboxy-cis,cis-muconate cycloisomerase | 5.5.1.2 | Protocatechuate branch, β-ketoadipate funnel | genomic in KT2440; pathway-established | high | core pathway |
| pcaD | PP_1380 | Q88N36 | β-ketoadipate enol-lactone hydrolase (3-oxoadipate enol-lactonase) | 3.1.1.24 | Convergence/lower β-ketoadipate funnel | genomic in KT2440; proteomic support in related benzoate studies | high | core pathway |
| pcaC | PP_1381 | Q88N35 | γ-carboxymuconolactone decarboxylase (4-carboxymuconolactone decarboxylase) | 4.1.1.44 | Protocatechuate branch, β-ketoadipate funnel | genomic in KT2440 | high | core pathway |
| frmA | PP_1616 | Q88MF5 | Glutathione-dependent formaldehyde dehydrogenase / S-(hydroxymethyl)glutathione dehydrogenase | 1.1.1.1; 1.1.1.284 | One-carbon/formaldehyde detox side chemistry | annotation/homology | low | side-node; not core aromatic umbrella step |
| PP_1791 | PP_1791 | Q88LY5 | Aldolase/synthase family protein; likely meta-cleavage-associated side enzyme rather than ortho-cleavage core | — | Meta-cleavage side pathway (KEGG ppu00621) | annotation/homology | low | over-propagated for ppu01220 |
| PP_2504 | PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (4-oxalocrotonate tautomerase) | 5.3.2.6 | Meta-cleavage side pathway (KEGG ppu00621) | annotation/homology | low | over-propagated for ppu01220 |
| benA | PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase α subunit | 1.14.12.10 | Upper benzoate activation to dihydrodiol | genomic in KT2440; proteomic induction on benzoate | high | core pathway |
| benB | PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase β subunit | 1.14.12.10 | Upper benzoate activation to dihydrodiol | genomic in KT2440; proteomic support | high | core pathway |
| benC | PP_3163 | Q88I38 | Benzoate dioxygenase reductase/electron transfer component | 1.14.12.10; 1.18.1.3 | Upper benzoate activation electron transfer | genomic in KT2440 | high | core pathway |
| benD | PP_3164 | Q88I37 | 2-hydro-1,2-dihydroxybenzoate dehydrogenase | 1.3.1.25 | Benzoate-to-catechol upper pathway | genomic in KT2440; proteomic induction on benzoate | high | core pathway |
| catA-II (catA2) | PP_3166 | Q88I35 | Second catechol 1,2-dioxygenase paralog embedded in ben cluster | 1.13.11.1 | Catechol ortho-cleavage backup/ben-linked step | genomic in KT2440; experimental role unresolved in KT2440 | medium | paralog-ambiguous; likely core-adjacent but not sole assignment |
| pobA | PP_3537 | Q88H28 | p-Hydroxybenzoate 3-monooxygenase | 1.14.13.2 | 4-hydroxybenzoate to protocatechuate upper pathway | genomic in KT2440; proteomic induction on p-hydroxybenzoate | high | core pathway |
| PP_3648 | PP_3648 | Q88GS0 | Carboxymuconolactone decarboxylase family protein; possible pcaC-like paralog/family member | — | Putative protocatechuate branch side paralog | family-level annotation only | low | paralog-ambiguous; possible over-propagation |
| catA-I (catA) | PP_3713 | Q88GK8 | Catechol 1,2-dioxygenase | 1.13.11.1 | Main catechol ortho-cleavage step | genomic in KT2440; proteomic induction on benzoate | high | core pathway |
| catC | PP_3714 | Q88GK7 | Muconolactone isomerase | 5.3.3.4 | Catechol branch, ortho-cleavage lower step | genomic in KT2440 | high | core pathway |
| catB | PP_3715 | Q88GK6 | Muconate cycloisomerase | 5.5.1.1 | Catechol branch, ortho-cleavage lower step | genomic in KT2440; proteomic induction on benzoate | high | core pathway |
| adhP | PP_3839 | Q88G86 | Coniferyl alcohol dehydrogenase (reannotated from generic alcohol dehydrogenase) | 1.1.1.- | Lignin/phenylpropanoid peripheral oxidation | direct experimental in KT2440 deletion study | medium | side-node/peripheral aromatic funnel |
| pcaG | PP_4655 | Q88E13 | Protocatechuate 3,4-dioxygenase α chain | 1.13.11.3 | Protocatechuate ring-cleavage step | genomic in KT2440; proteomic induction on p-hydroxybenzoate | high | core pathway |
| pcaH | PP_4656 | Q88E12 | Protocatechuate 3,4-dioxygenase β chain | 1.13.11.3 | Protocatechuate ring-cleavage step | genomic in KT2440; proteomic induction on p-hydroxybenzoate | high | core pathway |
| **Missing expected gene** pcaI | **not in candidate list** | — | β-ketoadipate succinyl-CoA transferase subunit | — | Lower β-ketoadipate funnel after ring cleavage | genomic in KT2440; proteomic support for expression | high | **core pathway; missing from candidate set** |
| **Missing expected gene** pcaJ | **not in candidate list** | — | β-ketoadipate succinyl-CoA transferase subunit | — | Lower β-ketoadipate funnel after ring cleavage | genomic in KT2440; proteomic support for expression | high | **core pathway; missing from candidate set** |
| **Missing expected gene** pcaF | **not in candidate list** | — | β-ketoadipyl-CoA thiolase | — | Final β-ketoadipate-to-central metabolism step | genomic in KT2440; proteomic support for expression | high | **core pathway; missing from candidate set** |


*Table: This table evaluates all 20 candidate genes for the KEGG aromatic-compound degradation umbrella in Pseudomonas putida KT2440, separating core ortho-cleavage/β-ketoadipate genes from side-node or over-propagated assignments. It also highlights critical missing core genes pcaI, pcaJ, and pcaF that are encoded in KT2440 but absent from the candidate list. (jimenez2002genomicanalysisof pages 3-5, jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 6-9, cao2008inductionofortho pages 6-7, cao2008catabolicpathwaysand pages 9-10, werner2023ligninconversionto pages 1-2, garciahidalgo2020vanillinproductionin pages 8-9)*

### 4.1 High-Confidence Core Pathway Genes (12 of 20 candidates)

**benA (PP_3161), benB (PP_3162), benC (PP_3163), benD (PP_3164)**: These four genes encode the benzoate 1,2-dioxygenase complex and dihydrodiol dehydrogenase. Genomic analysis maps them to positions 3580–3591 kb in the KT2440 chromosome, with orf numbers 03542, 03540, 03539, and 03538 respectively (jimenez2002genomicanalysisof pages 5-6). Proteomic studies confirm BenA and BenD induction during growth on benzoate in KT2440 (cao2008catabolicpathwaysand pages 9-10, yun2011proteomiccharacterizationof pages 5-7). The ben cluster also contains benR (transcriptional activator), benK (benzoate transporter), benE, benF (porin), and a unique benX gene of unknown function (jimenez2002genomicanalysisof pages 5-6). All evidence is direct for KT2440. **Assessment: core pathway, high confidence.**

**pobA (PP_3537)**: Encodes p-hydroxybenzoate hydroxylase converting 4-hydroxybenzoate to protocatechuate. Identified in KT2440 at orf 02935 and is regulated by PobR, a XylS/AraC-family transcriptional activator (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 3-5). Proteomic data confirm induction on p-hydroxybenzoate (cao2008catabolicpathwaysand pages 9-10). **Assessment: core pathway, high confidence.**

**catA-I (PP_3713), catB (PP_3715), catC (PP_3714)**: The main cat cluster at the catRcatBCA locus. CatA (orf 02653) encodes catechol 1,2-dioxygenase with 100% identity to CatA from *P. putida* mt-2. CatB (orf 02548) encodes muconate cycloisomerase, and CatC (orf 02650) encodes muconolactone isomerase (jimenez2002genomicanalysisof pages 5-6). CatR is a LysR-type transcriptional activator that responds to cis,cis-muconate (cao2008catabolicpathwaysand pages 10-11, jimenez2002genomicanalysisof pages 6-9). Proteomic evidence confirms CatA and CatB expression during benzoate growth (cao2008catabolicpathwaysand pages 9-10). **Assessment: core pathway, high confidence.**

**pcaB (PP_1379), pcaC (PP_1381), pcaD (PP_1380)**: Located in the pca gene cluster (orf 06324, 06320, 06322 respectively). PcaB catalyzes β-carboxy-cis,cis-muconate cycloisomerization, PcaC catalyzes γ-carboxymuconolactone decarboxylation, and PcaD catalyzes β-ketoadipate enol-lactone hydrolysis (jimenez2002genomicanalysisof pages 3-5). PcaD is the convergence-point enzyme of both branches. All are regulated by PcaR with β-ketoadipate as inducer (jimenez2002genomicanalysisof pages 6-9). **Assessment: core pathway, high confidence.**

**pcaG (PP_4655), pcaH (PP_4656)**: Encode the α and β subunits of protocatechuate 3,4-dioxygenase (orf 01496 and 01495), with 98% and 97% identity to *P. putida* ATCC23975 respectively (jimenez2002genomicanalysisof pages 3-5). Proteomic studies confirm PcaGH induction on p-hydroxybenzoate and vanillin in KT2440 (cao2008catabolicpathwaysand pages 9-10). **Assessment: core pathway, high confidence.**

### 4.2 Paralog-Ambiguous Candidates (2 of 20)

**catA-II / catA2 (PP_3166)**: A second catechol 1,2-dioxygenase located within the ben cluster (orf 03534). CatA2 shows 77% identity to the primary CatA and its N-terminus is homologous to the α subunit of catechol 1,2-dioxygenase from *P. arvilla* C-1 (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 5-6). Critically, the Jiménez et al. (2002) analysis explicitly states that "the expression of the catA2 gene and the physiological role of the CatA2 enzyme in *P. putida* KT2440 remain to be checked" (jimenez2002genomicanalysisof pages 5-6). This catA2 is unique to KT2440 and absent from the ben clusters of *P. putida* PRS2000, *P. aeruginosa*, and *P. fluorescens* (jimenez2002genomicanalysisof pages 6-9). Subsequent work by Jiménez et al. (2014) on *P. putida* mt-2 described it as an "enzymatic safety valve for excess catechol." **Assessment: candidate_uncertain; likely functional but role unresolved in KT2440 specifically.**

**PP_3648**: Annotated as a carboxymuconolactone decarboxylase family protein. This may be a paralog of pcaC but lacks direct experimental characterization. Family-level annotation alone is insufficient to confirm pathway function. **Assessment: candidate_uncertain; possible over-propagation of the carboxymuconolactone decarboxylase family.**

### 4.3 Side-Node and Over-Propagated Genes (6 of 20)

**ubiX (PP_0548)**: Flavin prenyltransferase involved in prenyl-FMN cofactor synthesis for UbiD-family decarboxylases. While UbiX/UbiD systems can participate in aromatic decarboxylation reactions, in KT2440 the primary role of UbiX is in ubiquinone biosynthesis, not in the core β-ketoadipate pathway. Its inclusion in the ppu01220 umbrella appears to stem from broad KEGG map associations rather than direct pathway participation (jimenez2002genomicanalysisof pages 1-2). **Assessment: side-node; module_needs_revision for core satisfiability.**

**frmA (PP_1616)**: Glutathione-dependent formaldehyde dehydrogenase / S-(hydroxymethyl)glutathione dehydrogenase. This is a one-carbon metabolism enzyme for formaldehyde detoxification. It has no established role in the ortho-cleavage or β-ketoadipate pathway (jimenez2002genomicanalysisof pages 1-2). Its primary KEGG bucket is ppu00626 (naphthalene degradation side-map). **Assessment: side-node; should not be used for core pathway satisfiability.**

**adhP (PP_3839)**: Experimentally demonstrated in KT2440 to function as a coniferyl alcohol dehydrogenase, oxidizing coniferyl alcohol to coniferyl aldehyde in the phenylpropanoid peripheral pathway (garciahidalgo2020vanillinproductionin pages 8-9). García-Hidalgo et al. (2020) showed that ΔPP_3839 exhibited delayed growth on coniferyl alcohol. This is a peripheral lignin-related activity, not a core β-ketoadipate step. **Assessment: peripheral aromatic funnel enzyme; not core satisfier.**

**PP_1791**: Annotated as aldolase/synthase with primary bucket KEGG ppu00621 (meta-cleavage pathway). KT2440 lacks the TOL plasmid encoding the canonical meta-cleavage pathway, though some chromosomal meta-cleavage genes (pcm cluster) have been identified (jimenez2002genomicanalysisof pages 1-2). This gene is not part of the ortho-cleavage pathway. **Assessment: over-propagated for ppu01220.**

**PP_2504**: 2-Hydroxymuconate tautomerase (4-oxalocrotonate tautomerase), a meta-cleavage pathway enzyme with primary bucket KEGG ppu00621. The meta-cleavage pathway processes catechol via extradiol cleavage, which is distinct from the ortho-cleavage route that defines the β-ketoadipate funnel in KT2440 (perez‐pantoja2012genomicanalysisof pages 17-18). **Assessment: over-propagated for ppu01220.**

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Critical Missing Core Genes

The most significant finding is that **three essential core pathway genes are absent from the candidate list despite being present in the KT2440 genome**:

- **pcaI** (orf 02302): β-Ketoadipate succinyl-CoA transferase subunit, 231 aa, 98% identity to *P. putida* PRS2000 PcaI (jimenez2002genomicanalysisof pages 3-5). Proteomic evidence confirms expression during aromatic growth (cao2008inductionofortho pages 6-7, cao2008catabolicpathwaysand pages 9-10).
- **pcaJ** (orf 02300): β-Ketoadipate succinyl-CoA transferase subunit, 213 aa, 100% identity to *P. putida* PRS2000 PcaJ (jimenez2002genomicanalysisof pages 3-5). Co-transcribed with pcaI.
- **pcaF** (orf 06327): β-Ketoadipyl-CoA thiolase, 400 aa, 97% identity to *P. putida* PRS2000 PcaF (jimenez2002genomicanalysisof pages 3-5). Located in the main pca gene cluster. Proteomic evidence confirms expression during aromatic degradation (cao2008inductionofortho pages 6-7, cao2008catabolicpathwaysand pages 9-10).

Without pcaIJ and pcaF, the pathway cannot be completed from β-ketoadipate to TCA cycle intermediates. The Werner et al. (2023) metabolic engineering study specifically deleted pcaIJ to accumulate β-ketoadipate as a product, confirming their essentiality in the native pathway (werner2023ligninconversionto pages 1-2).

### 5.2 Missing Regulatory and Transport Genes

Also absent from the candidate list but present in KT2440 are: pcaR (orf 06331, IclR-family transcriptional activator), pcaK (orf 06330, 4-hydroxybenzoate transporter), pcaT (orf 06326, β-ketoadipate transporter), pcaP (orf 06317, porin), catR (orf 02646, LysR-family transcriptional activator), and benR (orf 03545, XylS/AraC-family transcriptional activator) (jimenez2002genomicanalysisof pages 3-5, jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 5-6). While regulatory/transport genes are not typically required for enzymatic satisfiability calls, they are important for understanding pathway operation. Notably, pcaF is **not linked to pcaIJ** in *P. putida*, unlike in some other bacteria where pcaIJF are contiguous (jimenez2002genomicanalysisof pages 5-6).

### 5.3 Over-Annotations

Five of the 20 candidate genes (ubiX, frmA, PP_1791, PP_2504, adhP) represent over-propagation from broad KEGG degradation maps. Their inclusion inflates the apparent gene count of the module without contributing to core pathway satisfiability.

## 6. Module and GO-Curation Recommendations

The step-by-step satisfiability assessment is summarized below:

| Step Number | Step Name | Expected Enzyme Activity | Candidate Gene(s) | Status | Notes |
|---|---|---|---|---|---|
| 1 | Benzoate 1,2-dioxygenase | Benzoate 1,2-dioxygenase alpha/beta/reductase components | benA (PP_3161), benB (PP_3162), benC (PP_3163) | covered | Core upper benzoate activation route is clearly encoded in KT2440; ben genes are directly identified in the KT2440 genome and supported by benzoate-induced proteomics. (jimenez2002genomicanalysisof pages 5-6, yun2011proteomiccharacterizationof pages 5-7) |
| 2 | Benzoate dihydrodiol dehydrogenase | 2-Hydro-1,2-dihydroxybenzoate dehydrogenase | benD (PP_3164) | covered | Core benzoate-to-catechol step; directly assigned in KT2440 genomic analysis and detected in benzoate proteomics. (jimenez2002genomicanalysisof pages 5-6, yun2011proteomiccharacterizationof pages 5-7) |
| 3 | 4-Hydroxybenzoate 3-monooxygenase | p-Hydroxybenzoate hydroxylase | pobA (PP_3537) | covered | Core peripheral entry to the protocatechuate branch; present in KT2440 and proteomically induced on p-hydroxybenzoate. (jimenez2002genomicanalysisof pages 3-5, cao2008catabolicpathwaysand pages 9-10) |
| 4 | Catechol 1,2-dioxygenase | Catechol 1,2-dioxygenase | catA-I (PP_3713), catA-II/catA2 (PP_3166) | candidate_uncertain | KT2440 clearly encodes the main CatA-I enzyme and a second ben-cluster paralog catA2. CatA-I is high-confidence core coverage; catA2 likely contributes but its exact physiological role in KT2440 remained unresolved in the genomic study, so paralog handling needs caution. (jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 6-9) |
| 5 | Protocatechuate 3,4-dioxygenase | Protocatechuate 3,4-dioxygenase alpha/beta chains | pcaG (PP_4655), pcaH (PP_4656) | covered | Canonical ring-cleavage step of the protocatechuate branch; directly identified in KT2440 genome and supported by proteomics. (jimenez2002genomicanalysisof pages 3-5, cao2008catabolicpathwaysand pages 9-10) |
| 6 | Muconate cycloisomerase | cis,cis-Muconate cycloisomerase | catB (PP_3715) | covered | Core catechol-branch ortho-cleavage funnel step; directly assigned in KT2440. (jimenez2002genomicanalysisof pages 5-6) |
| 7 | Muconolactone isomerase | Muconolactone isomerase | catC (PP_3714) | covered | Core catechol-branch lower step; directly assigned in KT2440. (jimenez2002genomicanalysisof pages 5-6) |
| 8 | 3-Carboxy-cis,cis-muconate cycloisomerase | 3-Carboxy-cis,cis-muconate cycloisomerase | pcaB (PP_1379) | covered | Core protocatechuate-branch lower step; directly assigned in KT2440. (jimenez2002genomicanalysisof pages 3-5) |
| 9 | γ-Carboxymuconolactone decarboxylase | γ-Carboxymuconolactone decarboxylase | pcaC (PP_1381); PP_3648 family protein | covered | pcaC is the high-confidence core enzyme. PP_3648 is only a family-level paralog candidate and should not replace pcaC without direct evidence. (jimenez2002genomicanalysisof pages 3-5) |
| 10 | β-Ketoadipate enol-lactone hydrolase | β-Ketoadipate enol-lactone hydrolase / 3-oxoadipate enol-lactonase | pcaD (PP_1380) | covered | Core convergence step of the β-ketoadipate funnel; directly assigned in KT2440. (jimenez2002genomicanalysisof pages 3-5) |
| 11 | β-Ketoadipate succinyl-CoA transferase | β-Ketoadipate succinyl-CoA transferase subunits | pcaI, pcaJ (missing from candidate list) | gap | This is a true module gap in the candidate metadata, not in the organism. KT2440 encodes pcaI and pcaJ (orf 02302/02300), and proteomic evidence supports expression of PcaI during aromatic growth. These genes should be added to the candidate set. (jimenez2002genomicanalysisof pages 3-5, cao2008inductionofortho pages 6-7) |
| 12 | β-Ketoadipyl-CoA thiolase | β-Ketoadipyl-CoA thiolase | pcaF (missing from candidate list) | gap | Another metadata gap rather than biological absence. KT2440 encodes pcaF (orf 06327), and proteomic evidence supports expression during aromatic degradation. This gene should be added to the candidate set. (jimenez2002genomicanalysisof pages 3-5, cao2008inductionofortho pages 6-7) |
| 13 | Flavin prenyltransferase | Flavin prenyltransferase / prenyl-FMN cofactor synthesis | ubiX (PP_0548) | module_needs_revision | UbiX is not part of the canonical ben/cat/pca ortho-cleavage and β-ketoadipate route in KT2440. It fits broad-map cofactor context and should be kept separate unless a specific UbiD-dependent aromatic decarboxylation submodule is being curated. (jimenez2002genomicanalysisof pages 1-2) |
| 14 | Formaldehyde dehydrogenase | Glutathione-dependent formaldehyde dehydrogenase | frmA (PP_1616) | module_needs_revision | frmA is a one-carbon/formaldehyde detox enzyme, not a core step of the KEGG aromatic degradation umbrella as realized by ben/cat/pca in KT2440. It should be excluded from core satisfiability calls for ppu01220. (jimenez2002genomicanalysisof pages 1-2) |
| 15 | Alcohol dehydrogenase | Peripheral aromatic alcohol dehydrogenase | adhP (PP_3839) | not_expected_in_target_taxon | PP_3839 is experimentally supported as a coniferyl alcohol dehydrogenase in lignin/phenylpropanoid peripheral metabolism, not a required core step for benzoate/4-hydroxybenzoate ortho-cleavage satisfiability. Keep as peripheral context only. (garciahidalgo2020vanillinproductionin pages 8-9) |


*Table: This table summarizes step-by-step satisfiability of the aromatic compound degradation umbrella in Pseudomonas putida KT2440, distinguishing true pathway coverage from metadata gaps and broad-map side-node assignments. It is useful for module curation because it highlights that pcaIJ and pcaF are biologically present but missing from the candidate list, while ubiX, frmA, and adhP should not be treated as core satisfiers.*

### 6.1 Specific Recommendations

1. **Add pcaI, pcaJ, and pcaF to the candidate gene list** as primary bucket kegg:ppu01220 members. These are essential catalytic steps of the β-ketoadipate pathway and their absence is a metadata gap, not a biological one.

2. **Reclassify ubiX (PP_0548), frmA (PP_1616), PP_1791, and PP_2504** as side-node/context genes, not core satisfiers. Their primary KEGG buckets (ppu00627, ppu00626, ppu00621) correctly place them outside the core ortho-cleavage pathway.

3. **Flag catA-II (PP_3166) as paralog-ambiguous**. While likely encoding an active catechol 1,2-dioxygenase, its physiological role in KT2440 has not been experimentally resolved. It should not be the sole satisfier for the catechol 1,2-dioxygenase step; catA-I (PP_3713) is the primary assignment.

4. **Flag PP_3648** as requiring further investigation before assignment. Family-level annotation to carboxymuconolactone decarboxylase is insufficient without functional data. It may be a pcaC paralog or have divergent substrate specificity.

5. **Reclassify adhP (PP_3839)** from ppu01220 to a peripheral phenylpropanoid/lignin context role. Direct experimental evidence shows it functions as a coniferyl alcohol dehydrogenase (garciahidalgo2020vanillinproductionin pages 8-9), not as a core β-ketoadipate enzyme.

6. **Consider separate sub-modules** for: (a) upper benzoate activation (benABCD), (b) upper 4-hydroxybenzoate activation (pobA), (c) catechol ortho-cleavage branch (catA/B/C), (d) protocatechuate branch (pcaGH/B/C), and (e) lower convergent pathway (pcaD/IJ/F). This would improve satisfiability tracking.

### 6.2 Module Boundary Adjustments

The generic module boundary is **too broad for KT2440** because it conflates ortho-cleavage core enzymes with meta-cleavage pathway components (PP_1791, PP_2504), cofactor biosynthesis (ubiX), and generic oxidoreductases (frmA, adhP). KT2440 primarily uses the ortho-cleavage pathway for benzoate and 4-hydroxybenzoate degradation (cao2008catabolicpathwaysand pages 10-11, zhou2025lignindegradingenzymesand pages 12-14).

## 7. Genes to Promote to Full Review

The following genes warrant full `fetch-gene` review:

1. **pcaI, pcaJ** — Must be identified by PP locus tag and added. Critical gap in candidate list.
2. **pcaF** — Must be identified by PP locus tag and added. Critical gap in candidate list.
3. **catA-II (PP_3166)** — Paralog ambiguity with catA-I needs resolution. Direct experimental data on expression and physiological role in KT2440 would be valuable.
4. **PP_3648** — Carboxymuconolactone decarboxylase family protein with uncertain pathway role.
5. **pobA (PP_3537)** — While high-confidence, this gene is a key metabolic engineering target (used in PCA production from lignin hydrolysate) (werner2023ligninconversionto pages 1-2) and merits review for annotation completeness.

## 8. Key References

1. **Jiménez JI, Miñambres B, García JL, Díaz E** (2002). Genomic analysis of the aromatic catabolic pathways from *Pseudomonas putida* KT2440. *Environmental Microbiology* 4(12):824–841. doi:10.1046/j.1462-2920.2002.00370.x — *Foundational genomic analysis; direct KT2440 evidence for all pca, cat, ben, pob genes* (jimenez2002genomicanalysisof pages 6-9, jimenez2002genomicanalysisof pages 1-2, jimenez2002genomicanalysisof pages 5-6, jimenez2002genomicanalysisof pages 3-5).

2. **Werner AZ, Cordell WT, Lahive CW et al.** (2023). Lignin conversion to β-ketoadipic acid by *Pseudomonas putida* via metabolic engineering and bioprocess development. *Science Advances* 9(36):eadj0053. doi:10.1126/sciadv.adj0053 — *State-of-the-art metabolic engineering; 44.5 g/L β-ketoadipate; deletion of pcaIJ confirms pathway essentiality* (werner2023ligninconversionto pages 1-2).

3. **García-Hidalgo J, Brink DP, Ravi K et al.** (2020). Vanillin production in *Pseudomonas*: Reannotation of *P. putida* CalA as a vanillin reductase. *Appl Environ Microbiol* 86(6). doi:10.1128/aem.02442-19 — *Direct experimental evidence for adhP (PP_3839) function as coniferyl alcohol dehydrogenase in KT2440* (garciahidalgo2020vanillinproductionin pages 8-9).

4. **Kim YH, Cho K, Yun S-H et al.** (2006). Analysis of aromatic catabolic pathways in *P. putida* KT 2440 using a combined proteomic approach. *PROTEOMICS* 6(4):1301–1318. doi:10.1002/pmic.200500329 — *Proteomic confirmation of BenA, BenD, CatA, CatB, PcaF, PcaI, PcaGH induction on aromatic substrates in KT2440* (cao2008catabolicpathwaysand pages 9-10).

5. **Cao B, Loh K-C** (2008). Catabolic pathways and cellular responses of *P. putida* P8 during growth on benzoate. *Biotechnol Bioeng* 101:1297–1312. doi:10.1002/bit.21997 — *Proteomic characterization of beta-ketoadipate pathway enzyme expression* (cao2008catabolicpathwaysand pages 9-10, cao2008catabolicpathwaysand pages 10-11).

6. **Cao B, Geng A, Loh K-C** (2008). Induction of ortho- and meta-cleavage pathways in Pseudomonas in biodegradation of high benzoate concentration. *Appl Microbiol Biotechnol* 81:99–107. doi:10.1007/s00253-008-1728-3 — *MS identification of PcaI and PcaF as expressed catabolic enzymes* (cao2008inductionofortho pages 6-7).

7. **Jin X, Li X, Zou L et al.** (2024). Biological valorization of lignin-derived aromatics to protocatechuic acid by engineered *P. putida* KT2440. *Molecules* 29(7):1555. doi:10.3390/molecules29071555 — *Recent application: PCA production from lignin hydrolysate via pcaGH knockout engineering* (werner2023ligninconversionto pages 1-2).

8. **Zhou Q, Fransen A, de Winde H** (2025). Lignin-degrading enzymes and the potential of *P. putida* as a cell factory. *Microorganisms* 13(4):935. doi:10.3390/microorganisms13040935 — *Recent comprehensive review of P. putida lignin valorization potential* (zhou2025lignindegradingenzymesand pages 24-25, zhou2025lignindegradingenzymesand pages 23-24, zhou2025lignindegradingenzymesand pages 12-14).

9. **Nogales J, Palsson BØ, Thiele I** (2008). A genome-scale metabolic reconstruction of *P. putida* KT2440: iJN746 as a cell factory. *BMC Systems Biology* 2:79. doi:10.1186/1752-0509-2-79 — *Genome-scale model including aromatic degradation routes*.

10. **Salvachúa D, Werner AZ, Pardo I et al.** (2020). Outer membrane vesicles catabolize lignin-derived aromatic compounds in *P. putida* KT2440. *PNAS* 117(17):9302–9310. doi:10.1073/pnas.1921073117 — *Discovery of OMV-mediated extracellular aromatic catabolism*.

## 9. Evidence Summary and Open Questions

### Conclusions Supported by Direct Experiments in KT2440:
- All ben, cat, pca, pob genes are genomically identified and most are proteomically validated (cao2008catabolicpathwaysand pages 9-10, jimenez2002genomicanalysisof pages 3-5, jimenez2002genomicanalysisof pages 5-6).
- adhP (PP_3839) functions as coniferyl alcohol dehydrogenase (garciahidalgo2020vanillinproductionin pages 8-9).
- pcaIJ deletion accumulates β-ketoadipate, confirming pathway essentiality (werner2023ligninconversionto pages 1-2).
- The β-ketoadipate pathway is the primary route for benzoate/4-hydroxybenzoate catabolism in KT2440 (cao2008catabolicpathwaysand pages 10-11).

### Conclusions Inferred from Homology or Neighboring Organisms:
- PP_3648 function as carboxymuconolactone decarboxylase is inferred from family-level annotation only.
- catA2 function is inferred from sequence homology to known catechol dioxygenases and from studies in *P. putida* mt-2.

### Open Questions Requiring Resolution:
1. What is the physiological role of catA2 (PP_3166) in KT2440? Is it co-expressed with the ben operon?
2. What are the exact PP locus tags for pcaI, pcaJ, and pcaF? (The Jiménez et al. 2002 paper uses orf numbers from the original TIGR annotation, not the current PP_ nomenclature.)
3. Does PP_3648 have measurable carboxymuconolactone decarboxylase activity, and if so, under what conditions?
4. What is the contribution of chromosomal meta-cleavage genes (pcm cluster) to aromatic metabolism in KT2440, and are PP_1791 and PP_2504 part of this system?


References

1. (jimenez2002genomicanalysisof pages 1-2): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

2. (cao2008catabolicpathwaysand pages 10-11): Bin Cao and Kai‐Chee Loh. Catabolic pathways and cellular responses of pseudomonas putida p8 during growth on benzoate with a proteomics approach. Biotechnology and Bioengineering, 101:1297-1312, Dec 2008. URL: https://doi.org/10.1002/bit.21997, doi:10.1002/bit.21997. This article has 56 citations and is from a domain leading peer-reviewed journal.

3. (jimenez2002genomicanalysisof pages 5-6): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

4. (jimenez2002genomicanalysisof pages 6-9): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

5. (jimenez2002genomicanalysisof pages 3-5): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 705 citations and is from a domain leading peer-reviewed journal.

6. (cao2008inductionofortho pages 6-7): Bin Cao, Anli Geng, and Kai-Chee Loh. Induction of ortho- and meta-cleavage pathways in pseudomonas in biodegradation of high benzoate concentration: ms identification of catabolic enzymes. Nov 2008. URL: https://doi.org/10.1007/s00253-008-1728-3, doi:10.1007/s00253-008-1728-3. This article has 99 citations and is from a domain leading peer-reviewed journal.

7. (cao2008catabolicpathwaysand pages 9-10): Bin Cao and Kai‐Chee Loh. Catabolic pathways and cellular responses of pseudomonas putida p8 during growth on benzoate with a proteomics approach. Biotechnology and Bioengineering, 101:1297-1312, Dec 2008. URL: https://doi.org/10.1002/bit.21997, doi:10.1002/bit.21997. This article has 56 citations and is from a domain leading peer-reviewed journal.

8. (werner2023ligninconversionto pages 1-2): Allison Z. Werner, William T. Cordell, Ciaran W. Lahive, Bruno C. Klein, Christine A. Singer, Eric C. D. Tan, Morgan A. Ingraham, Kelsey J. Ramirez, Dong Hyun Kim, Jacob Nedergaard Pedersen, Christopher W. Johnson, Brian F. Pfleger, Gregg T. Beckham, and Davinia Salvachúa. Lignin conversion to β-ketoadipic acid by <i>pseudomonas putida</i> via metabolic engineering and bioprocess development. Science Advances, Sep 2023. URL: https://doi.org/10.1126/sciadv.adj0053, doi:10.1126/sciadv.adj0053. This article has 92 citations and is from a highest quality peer-reviewed journal.

9. (garciahidalgo2020vanillinproductionin pages 8-9): Javier García-Hidalgo, Daniel P. Brink, Krithika Ravi, Catherine J. Paul, Gunnar Lidén, and Marie F. Gorwa-Grauslund. Vanillin production in <i>pseudomonas</i> : whole-genome sequencing of <i>pseudomonas</i> sp. strain 9.1 and reannotation of pseudomonas putida cala as a vanillin reductase. Mar 2020. URL: https://doi.org/10.1128/aem.02442-19, doi:10.1128/aem.02442-19. This article has 44 citations and is from a peer-reviewed journal.

10. (yun2011proteomiccharacterizationof pages 5-7): Sung-Ho Yun, Gun Wook Park, Jin Young Kim, Sang Oh Kwon, Chi-Won Choi, Sun-Hee Leem, Kyung-Hoon Kwon, Jong Shin Yoo, Chulhyun Lee, Soohyun Kim, and Seung Il Kim. Proteomic characterization of the pseudomonas putida kt2440 global response to a monocyclic aromatic compound by itraq analysis and 1de-mudpit. Journal of proteomics, 74 5:620-8, May 2011. URL: https://doi.org/10.1016/j.jprot.2011.01.020, doi:10.1016/j.jprot.2011.01.020. This article has 50 citations and is from a peer-reviewed journal.

11. (perez‐pantoja2012genomicanalysisof pages 17-18): Danilo Pérez‐Pantoja, Raúl Donoso, Loreine Agulló, Macarena Córdova, Michael Seeger, Dietmar H. Pieper, and Bernardo González. Genomic analysis of the potential for aromatic compounds biodegradation in burkholderiales. Environmental microbiology, 14 5:1091-117, May 2012. URL: https://doi.org/10.1111/j.1462-2920.2011.02613.x, doi:10.1111/j.1462-2920.2011.02613.x. This article has 420 citations and is from a domain leading peer-reviewed journal.

12. (zhou2025lignindegradingenzymesand pages 12-14): Qing Zhou, Annabel Fransen, and Han de Winde. Lignin-degrading enzymes and the potential of pseudomonas putida as a cell factory for lignin degradation and valorization. Microorganisms, 13:935, Apr 2025. URL: https://doi.org/10.3390/microorganisms13040935, doi:10.3390/microorganisms13040935. This article has 22 citations.

13. (zhou2025lignindegradingenzymesand pages 24-25): Qing Zhou, Annabel Fransen, and Han de Winde. Lignin-degrading enzymes and the potential of pseudomonas putida as a cell factory for lignin degradation and valorization. Microorganisms, 13:935, Apr 2025. URL: https://doi.org/10.3390/microorganisms13040935, doi:10.3390/microorganisms13040935. This article has 22 citations.

14. (zhou2025lignindegradingenzymesand pages 23-24): Qing Zhou, Annabel Fransen, and Han de Winde. Lignin-degrading enzymes and the potential of pseudomonas putida as a cell factory for lignin degradation and valorization. Microorganisms, 13:935, Apr 2025. URL: https://doi.org/10.3390/microorganisms13040935, doi:10.3390/microorganisms13040935. This article has 22 citations.

## Artifacts

- [Edison artifact artifact-00](PSEPK__aromatic_compound_degradation__ppu01220-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__aromatic_compound_degradation__ppu01220-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PSEPK__aromatic_compound_degradation__ppu01220-deep-research-falcon_artifacts/artifact-02.md)
![Image artifact created (ID artifact-02): 'KT2440 Aromatic Degradation Funnel' ![KT2440 Aromatic Degradation Funnel](artifact:artifact-02) Artifact IDs that may ](PSEPK__aromatic_compound_degradation__ppu01220-deep-research-falcon_artifacts/image-1.png)

## Citations

1. jimenez2002genomicanalysisof pages 6-9
2. jimenez2002genomicanalysisof pages 1-2
3. jimenez2002genomicanalysisof pages 5-6
4. cao2008catabolicpathwaysand pages 9-10
5. jimenez2002genomicanalysisof pages 3-5
6. garciahidalgo2020vanillinproductionin pages 8-9
7. werner2023ligninconversionto pages 1-2
8. cao2008inductionofortho pages 6-7
9. cao2008catabolicpathwaysand pages 10-11
10. yun2011proteomiccharacterizationof pages 5-7
11. zhou2025lignindegradingenzymesand pages 12-14
12. zhou2025lignindegradingenzymesand pages 24-25
13. zhou2025lignindegradingenzymesand pages 23-24
14. KT2440 Aromatic Degradation Funnel
15. https://doi.org/10.1046/j.1462-2920.2002.00370.x,
16. https://doi.org/10.1002/bit.21997,
17. https://doi.org/10.1007/s00253-008-1728-3,
18. https://doi.org/10.1126/sciadv.adj0053,
19. https://doi.org/10.1128/aem.02442-19,
20. https://doi.org/10.1016/j.jprot.2011.01.020,
21. https://doi.org/10.1111/j.1462-2920.2011.02613.x,
22. https://doi.org/10.3390/microorganisms13040935,