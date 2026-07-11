---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T20:52:57.894058'
end_time: '2026-07-06T21:14:06.867409'
duration_seconds: 1268.97
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Fructose and mannose metabolism boundary module
  module_summary: A bacterial carbohydrate boundary module that separates fructose
    PTS entry and fructose-1-phosphate phosphorylation from GDP-mannose and GDP-mannuronate
    precursor biosynthesis, alginate polymerization/modification/export, and fucose
    or rhamnose nucleotide-sugar side branches. KEGG ppu00051 groups these adjacent
    reactions under fructose and mannose metabolism in Pseudomonas putida KT2440,
    but species-level curation should distinguish soluble central-carbon entry reactions
    from alginate and envelope-polysaccharide biosynthesis.
  module_outline: "- Fructose and mannose metabolism boundary module\n  - 1. fructose\
    \ PTS import and phosphorylation\n  - Fructose PTS entry\n    - Fructose-specific\
    \ PTS permease activity (molecular player: protein-N(PI)-phosphohistidine-sugar\
    \ phosphotransferase activity; activity or role: protein-N(PI)-phosphohistidine-sugar\
    \ phosphotransferase activity)\n  - 2. fructose-1-phosphate phosphorylation\n\
    \  - Fructose 1-phosphate to fructose 1,6-bisphosphate\n    - 1-phosphofructokinase\
    \ (molecular player: 1-phosphofructokinase activity; activity or role: 1-phosphofructokinase\
    \ activity)\n  - 3. GDP-mannose precursor synthesis\n  - Fructose 6-phosphate\
    \ to GDP-mannose\n    - Mannose-6-phosphate isomerase (molecular player: mannose-6-phosphate\
    \ isomerase activity; activity or role: mannose-6-phosphate isomerase activity)\n\
    \    - Phosphomannomutase (molecular player: phosphomannomutase activity; activity\
    \ or role: phosphomannomutase activity)\n    - Mannose-1-phosphate guanylyltransferase\
    \ (molecular player: mannose-1-phosphate guanylyltransferase (GTP) activity; activity\
    \ or role: mannose-1-phosphate guanylyltransferase (GTP) activity)\n  - 4. GDP-mannuronate\
    \ formation\n  - GDP-mannose to GDP-mannuronate\n    - GDP-mannose 6-dehydrogenase\
    \ (molecular player: GDP-mannose 6-dehydrogenase activity; activity or role: GDP-mannose\
    \ 6-dehydrogenase activity)\n  - 5. alginate polymerization and envelope handling\n\
    \  - Alginate polymer synthesis, modification, and export\n    - Alginate synthase\
    \ (molecular player: alginate synthase activity; activity or role: alginate synthase\
    \ activity)\n    - Cyclic-di-GMP binding alginate polymerization regulator (molecular\
    \ player: cyclic-di-GMP binding; activity or role: cyclic-di-GMP binding)\n  \
    \  - Mannuronan C5 epimerase (molecular player: racemase and epimerase activity,\
    \ acting on carbohydrates and derivatives; activity or role: racemase and epimerase\
    \ activity, acting on carbohydrates and derivatives)\n    - Poly(beta-D-mannuronate)\
    \ lyase (molecular player: poly(beta-D-mannuronate) lyase activity; activity or\
    \ role: poly(beta-D-mannuronate) lyase activity)\n  - 6. deoxy-sugar side branches\n\
    \  - GDP-mannose-derived deoxy-sugar side reactions\n    - GDP-mannose 4,6-dehydratase\
    \ (molecular player: GDP-mannose 4,6-dehydratase activity; activity or role: GDP-mannose\
    \ 4,6-dehydratase activity)\n    - L-fuconate dehydratase (molecular player: L-fuconate\
    \ dehydratase activity; activity or role: L-fuconate dehydratase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00051
  pathway_id: ppu00051
  pathway_name: Fructose and mannose metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00051 with 8 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '18'
  candidate_genes: '- fruK: PP_0794 | Q88PQ4 | Phosphofructokinase (primary bucket
    kegg:ppu02060)

    - fruA: PP_0795 | Q88PQ3 | protein-N(pi)-phosphohistidine--D-fructose phosphotransferase
    (EC 2.7.1.202) (EC 2.7.1.202; primary bucket kegg:ppu02060)

    - algA: PP_1277 | Q88ND5 | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate
    isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate
    guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP)
    (GTP--mannose-1-phosphate guanylyltransferase)] (EC 2.7.7.13; 5.3.1.8; primary
    bucket kegg:ppu00051)

    - algL: PP_1281 | Q88ND1 | Alginate lyase (EC 4.2.2.3) (Poly(beta-D-mannuronate)
    lyase) (EC 4.2.2.3; primary bucket kegg:ppu00051)

    - algG: PP_1283 | Q88NC9 | Mannuronan C5-epimerase (EC 5.1.3.37) (Poly(beta-D-mannuronate)
    C5 epimerase) (EC 5.1.3.37; primary bucket kegg:ppu00051)

    - alg44: PP_1286 | Q88NC6 | Alginate biosynthesis protein Alg44 (primary bucket
    kegg:ppu00543)

    - alg8: PP_1287 | Q88NC5 | Glycosyltransferase alg8 (EC 2.4.-.-) (EC 2.4.-.-;
    primary bucket kegg:ppu00543)

    - algD: PP_1288 | Q88NC4 | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) (EC
    1.1.1.132; primary bucket kegg:ppu00051)

    - PP_1776: PP_1776 | Q88M00 | Alginate biosynthesis protein AlgA (EC 2.7.7.13)
    (EC 5.3.1.8) (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - gmd: PP_1799 | Q88LX8 | GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose
    dehydratase) (EC 4.2.1.47; primary bucket kegg:ppu00051)

    - rmd: PP_1800 | Q88LX7 | Oxidoreductase Rmd (primary bucket kegg:ppu00051)

    - PP_2037: PP_2037 | Q88L98 | Aldolase (primary bucket kegg:ppu00040)

    - fucD: PP_2831 | Q88J18 | L-fuconate dehydratase (EC 4.2.1.68) (EC 4.2.1.68;
    primary bucket kegg:ppu00051)

    - tpiA: PP_4715 | Q88DV4 | Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1)
    (Triose-phosphate isomerase) (EC 5.3.1.1; primary bucket kegg:ppu00562)

    - fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC
    4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)

    - fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1)
    (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11;
    primary bucket kegg:ppu00710)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__fructose_mannose_metabolism__ppu00051-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__fructose_mannose_metabolism__ppu00051-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Fructose and mannose metabolism boundary module in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00051
- Resolved ID: ppu00051
- Resolved name: Fructose and mannose metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00051 with 8 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 18

- fruK: PP_0794 | Q88PQ4 | Phosphofructokinase (primary bucket kegg:ppu02060)
- fruA: PP_0795 | Q88PQ3 | protein-N(pi)-phosphohistidine--D-fructose phosphotransferase (EC 2.7.1.202) (EC 2.7.1.202; primary bucket kegg:ppu02060)
- algA: PP_1277 | Q88ND5 | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP) (GTP--mannose-1-phosphate guanylyltransferase)] (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- algL: PP_1281 | Q88ND1 | Alginate lyase (EC 4.2.2.3) (Poly(beta-D-mannuronate) lyase) (EC 4.2.2.3; primary bucket kegg:ppu00051)
- algG: PP_1283 | Q88NC9 | Mannuronan C5-epimerase (EC 5.1.3.37) (Poly(beta-D-mannuronate) C5 epimerase) (EC 5.1.3.37; primary bucket kegg:ppu00051)
- alg44: PP_1286 | Q88NC6 | Alginate biosynthesis protein Alg44 (primary bucket kegg:ppu00543)
- alg8: PP_1287 | Q88NC5 | Glycosyltransferase alg8 (EC 2.4.-.-) (EC 2.4.-.-; primary bucket kegg:ppu00543)
- algD: PP_1288 | Q88NC4 | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) (EC 1.1.1.132; primary bucket kegg:ppu00051)
- PP_1776: PP_1776 | Q88M00 | Alginate biosynthesis protein AlgA (EC 2.7.7.13) (EC 5.3.1.8) (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- gmd: PP_1799 | Q88LX8 | GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose dehydratase) (EC 4.2.1.47; primary bucket kegg:ppu00051)
- rmd: PP_1800 | Q88LX7 | Oxidoreductase Rmd (primary bucket kegg:ppu00051)
- PP_2037: PP_2037 | Q88L98 | Aldolase (primary bucket kegg:ppu00040)
- fucD: PP_2831 | Q88J18 | L-fuconate dehydratase (EC 4.2.1.68) (EC 4.2.1.68; primary bucket kegg:ppu00051)
- tpiA: PP_4715 | Q88DV4 | Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1) (Triose-phosphate isomerase) (EC 5.3.1.1; primary bucket kegg:ppu00562)
- fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)
- fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11; primary bucket kegg:ppu00710)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

## Generic Module Context

### Working Scope

A bacterial carbohydrate boundary module that separates fructose PTS entry and fructose-1-phosphate phosphorylation from GDP-mannose and GDP-mannuronate precursor biosynthesis, alginate polymerization/modification/export, and fucose or rhamnose nucleotide-sugar side branches. KEGG ppu00051 groups these adjacent reactions under fructose and mannose metabolism in Pseudomonas putida KT2440, but species-level curation should distinguish soluble central-carbon entry reactions from alginate and envelope-polysaccharide biosynthesis.

### Provisional Biological Outline

- Fructose and mannose metabolism boundary module
  - 1. fructose PTS import and phosphorylation
  - Fructose PTS entry
    - Fructose-specific PTS permease activity (molecular player: protein-N(PI)-phosphohistidine-sugar phosphotransferase activity; activity or role: protein-N(PI)-phosphohistidine-sugar phosphotransferase activity)
  - 2. fructose-1-phosphate phosphorylation
  - Fructose 1-phosphate to fructose 1,6-bisphosphate
    - 1-phosphofructokinase (molecular player: 1-phosphofructokinase activity; activity or role: 1-phosphofructokinase activity)
  - 3. GDP-mannose precursor synthesis
  - Fructose 6-phosphate to GDP-mannose
    - Mannose-6-phosphate isomerase (molecular player: mannose-6-phosphate isomerase activity; activity or role: mannose-6-phosphate isomerase activity)
    - Phosphomannomutase (molecular player: phosphomannomutase activity; activity or role: phosphomannomutase activity)
    - Mannose-1-phosphate guanylyltransferase (molecular player: mannose-1-phosphate guanylyltransferase (GTP) activity; activity or role: mannose-1-phosphate guanylyltransferase (GTP) activity)
  - 4. GDP-mannuronate formation
  - GDP-mannose to GDP-mannuronate
    - GDP-mannose 6-dehydrogenase (molecular player: GDP-mannose 6-dehydrogenase activity; activity or role: GDP-mannose 6-dehydrogenase activity)
  - 5. alginate polymerization and envelope handling
  - Alginate polymer synthesis, modification, and export
    - Alginate synthase (molecular player: alginate synthase activity; activity or role: alginate synthase activity)
    - Cyclic-di-GMP binding alginate polymerization regulator (molecular player: cyclic-di-GMP binding; activity or role: cyclic-di-GMP binding)
    - Mannuronan C5 epimerase (molecular player: racemase and epimerase activity, acting on carbohydrates and derivatives; activity or role: racemase and epimerase activity, acting on carbohydrates and derivatives)
    - Poly(beta-D-mannuronate) lyase (molecular player: poly(beta-D-mannuronate) lyase activity; activity or role: poly(beta-D-mannuronate) lyase activity)
  - 6. deoxy-sugar side branches
  - GDP-mannose-derived deoxy-sugar side reactions
    - GDP-mannose 4,6-dehydratase (molecular player: GDP-mannose 4,6-dehydratase activity; activity or role: GDP-mannose 4,6-dehydratase activity)
    - L-fuconate dehydratase (molecular player: L-fuconate dehydratase activity; activity or role: L-fuconate dehydratase activity)

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

Fructose and mannose metabolism boundary module in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00051
- Resolved ID: ppu00051
- Resolved name: Fructose and mannose metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00051 with 8 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 18

- fruK: PP_0794 | Q88PQ4 | Phosphofructokinase (primary bucket kegg:ppu02060)
- fruA: PP_0795 | Q88PQ3 | protein-N(pi)-phosphohistidine--D-fructose phosphotransferase (EC 2.7.1.202) (EC 2.7.1.202; primary bucket kegg:ppu02060)
- algA: PP_1277 | Q88ND5 | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP) (GTP--mannose-1-phosphate guanylyltransferase)] (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- algL: PP_1281 | Q88ND1 | Alginate lyase (EC 4.2.2.3) (Poly(beta-D-mannuronate) lyase) (EC 4.2.2.3; primary bucket kegg:ppu00051)
- algG: PP_1283 | Q88NC9 | Mannuronan C5-epimerase (EC 5.1.3.37) (Poly(beta-D-mannuronate) C5 epimerase) (EC 5.1.3.37; primary bucket kegg:ppu00051)
- alg44: PP_1286 | Q88NC6 | Alginate biosynthesis protein Alg44 (primary bucket kegg:ppu00543)
- alg8: PP_1287 | Q88NC5 | Glycosyltransferase alg8 (EC 2.4.-.-) (EC 2.4.-.-; primary bucket kegg:ppu00543)
- algD: PP_1288 | Q88NC4 | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) (EC 1.1.1.132; primary bucket kegg:ppu00051)
- PP_1776: PP_1776 | Q88M00 | Alginate biosynthesis protein AlgA (EC 2.7.7.13) (EC 5.3.1.8) (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- gmd: PP_1799 | Q88LX8 | GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose dehydratase) (EC 4.2.1.47; primary bucket kegg:ppu00051)
- rmd: PP_1800 | Q88LX7 | Oxidoreductase Rmd (primary bucket kegg:ppu00051)
- PP_2037: PP_2037 | Q88L98 | Aldolase (primary bucket kegg:ppu00040)
- fucD: PP_2831 | Q88J18 | L-fuconate dehydratase (EC 4.2.1.68) (EC 4.2.1.68; primary bucket kegg:ppu00051)
- tpiA: PP_4715 | Q88DV4 | Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1) (Triose-phosphate isomerase) (EC 5.3.1.1; primary bucket kegg:ppu00562)
- fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)
- fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11; primary bucket kegg:ppu00710)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

## Generic Module Context

### Working Scope

A bacterial carbohydrate boundary module that separates fructose PTS entry and fructose-1-phosphate phosphorylation from GDP-mannose and GDP-mannuronate precursor biosynthesis, alginate polymerization/modification/export, and fucose or rhamnose nucleotide-sugar side branches. KEGG ppu00051 groups these adjacent reactions under fructose and mannose metabolism in Pseudomonas putida KT2440, but species-level curation should distinguish soluble central-carbon entry reactions from alginate and envelope-polysaccharide biosynthesis.

### Provisional Biological Outline

- Fructose and mannose metabolism boundary module
  - 1. fructose PTS import and phosphorylation
  - Fructose PTS entry
    - Fructose-specific PTS permease activity (molecular player: protein-N(PI)-phosphohistidine-sugar phosphotransferase activity; activity or role: protein-N(PI)-phosphohistidine-sugar phosphotransferase activity)
  - 2. fructose-1-phosphate phosphorylation
  - Fructose 1-phosphate to fructose 1,6-bisphosphate
    - 1-phosphofructokinase (molecular player: 1-phosphofructokinase activity; activity or role: 1-phosphofructokinase activity)
  - 3. GDP-mannose precursor synthesis
  - Fructose 6-phosphate to GDP-mannose
    - Mannose-6-phosphate isomerase (molecular player: mannose-6-phosphate isomerase activity; activity or role: mannose-6-phosphate isomerase activity)
    - Phosphomannomutase (molecular player: phosphomannomutase activity; activity or role: phosphomannomutase activity)
    - Mannose-1-phosphate guanylyltransferase (molecular player: mannose-1-phosphate guanylyltransferase (GTP) activity; activity or role: mannose-1-phosphate guanylyltransferase (GTP) activity)
  - 4. GDP-mannuronate formation
  - GDP-mannose to GDP-mannuronate
    - GDP-mannose 6-dehydrogenase (molecular player: GDP-mannose 6-dehydrogenase activity; activity or role: GDP-mannose 6-dehydrogenase activity)
  - 5. alginate polymerization and envelope handling
  - Alginate polymer synthesis, modification, and export
    - Alginate synthase (molecular player: alginate synthase activity; activity or role: alginate synthase activity)
    - Cyclic-di-GMP binding alginate polymerization regulator (molecular player: cyclic-di-GMP binding; activity or role: cyclic-di-GMP binding)
    - Mannuronan C5 epimerase (molecular player: racemase and epimerase activity, acting on carbohydrates and derivatives; activity or role: racemase and epimerase activity, acting on carbohydrates and derivatives)
    - Poly(beta-D-mannuronate) lyase (molecular player: poly(beta-D-mannuronate) lyase activity; activity or role: poly(beta-D-mannuronate) lyase activity)
  - 6. deoxy-sugar side branches
  - GDP-mannose-derived deoxy-sugar side reactions
    - GDP-mannose 4,6-dehydratase (molecular player: GDP-mannose 4,6-dehydratase activity; activity or role: GDP-mannose 4,6-dehydratase activity)
    - L-fuconate dehydratase (molecular player: L-fuconate dehydratase activity; activity or role: L-fuconate dehydratase activity)

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

# Fructose and Mannose Metabolism Boundary Module in *Pseudomonas putida* KT2440: A Species-Aware Curation Review

## 1. Executive Summary

KEGG pathway ppu00051 ("Fructose and mannose metabolism") in *Pseudomonas putida* KT2440 conflates at least four biochemically and regulatorily distinct processes under a single pathway identifier: (i) fructose PTS-dependent import and initial phosphorylation (fruBKA operon), (ii) GDP-mannose precursor synthesis feeding alginate biosynthesis (algA, algC, algD), (iii) alginate polymerization, modification, and export (alg8, alg44, algG, algL and additional operon members), and (iv) GDP-rhamnose/LPS O-antigen nucleotide-sugar biosynthesis (PP_1776, gmd, rmd, and associated glycosyltransferases). Several additional candidate genes (tpiA, fba, fbp, PP_2037, fucD) are peripheral central-carbon-metabolism enzymes or weakly linked deoxy-sugar catabolic activities that do not properly belong to a coherent fructose/mannose entry module. A critical gap in the candidate gene list is the absence of **fruB** (the EI-HPr-EIIAFru fusion protein essential for fructose PTS function), which must be added. For species-level curation, this KEGG bucket should be decomposed into at least three separate module documents: (a) fructose PTS entry and phosphorylation, (b) GDP-mannose/alginate precursor biosynthesis, and (c) LPS/O-antigen nucleotide-sugar side branches.

## 2. Target-Organism Pathway Definition

### 2.1 Pathway boundaries

**Fructose entry.** In *P. putida* KT2440, fructose is the only sugar imported via a PEP-dependent phosphotransferase system (PTSFru). The fruBKA operon encodes FruB (a multi-domain EI-HPr-EIIAFru fusion protein), FruK (1-phosphofructokinase), and FruA (EIIBCFru permease) (chavarria2012regulatorytasksof pages 1-2, chavarria2012regulatorytasksof pages 2-2, chavarria2016ametabolicwidget pages 6-8). Fructose is phosphorylated to fructose-1-phosphate during transport, then converted to fructose-1,6-bisphosphate (FBP) by FruK. Unlike *E. coli*, KT2440 lacks 6-phosphofructokinase and routes most FBP through fructose-1,6-bisphosphatase (Fbp) back to fructose-6-phosphate, which then enters the Entner-Doudoroff (ED) pathway (santos2004genomicfeaturesof pages 8-11, sudarsan2014thefunctionalstructure pages 7-8). Approximately 52% of fructose carbon flows through the ED pathway, 34% through the EMP route, and 14% through the pentose phosphate pathway (chavarria2012regulatorytasksof pages 4-4).

**GDP-mannose/alginate precursor synthesis.** Fructose-6-phosphate is the branch point for GDP-mannose biosynthesis via AlgA (phosphomannose isomerase/GDP-mannose pyrophosphorylase; PP_1277), AlgC (phosphomannomutase/phosphoglucomutase; PP_5288), and AlgD (GDP-mannose dehydrogenase; PP_1288) (ertesvag2017identificationofgenes pages 1-2, serrato2024bacterialalginatebiosynthesis pages 6-8, rehman2013insightsintothe pages 1-2). These enzymes produce the activated precursor GDP-mannuronate for alginate polymerization.

**Alginate polymerization and export.** The 12-gene alginate structural operon (algD-alg8-alg44-algK-algE-algG-algX-algL-algI-algJ-algF-algA, spanning PP_1277–PP_1288) encodes the complete machinery for alginate synthesis, epimerization, acetylation, and secretion (muhammadi2007geneticsofbacterial pages 2-3, gulez2014colonymorphologyand pages 6-8). KT2440 produces alginate primarily under water-limitation stress and in biofilms (gulez2014colonymorphologyand pages 1-2).

**LPS O-antigen nucleotide-sugar branch.** A separate gene cluster (PP_1797–PP_1806) encodes enzymes for A-band LPS O-antigen biosynthesis, including PP_1776 (WbpW, an AlgA paralog for GDP-mannose synthesis), PP_1799/gmd (GDP-mannose 4,6-dehydratase), and PP_1800/rmd (GDP-rhamnose synthetic oxidoreductase), along with glycosyltransferases wbpL, wbpY, wbpZ, and wbpX (santos2004insightsintothe pages 11-12).

### 2.2 Neighboring pathways to keep separate

- **Glycolysis/Gluconeogenesis (ppu00010):** tpiA, fba, and fbp belong to core EMP/gluconeogenic metabolism, not fructose-specific entry.
- **Pentose and glucuronate interconversions (ppu00040):** PP_2037 aldolase is a spillover from this pathway.
- **Alginate biosynthesis (ppu00543):** alg44 and alg8 are already primarily assigned there; the full alginate polymerization/export machinery should reside in a dedicated alginate/EPS module.
- **Starch and sucrose metabolism (ppu00052):** cpsG/PP_1777 is primarily assigned there.

### 2.3 Alternate names and database definitions

KEGG ppu00051 corresponds broadly to MetaCyc pathways for GDP-mannose biosynthesis, fructose degradation, and mannose degradation. In *P. putida*, no canonical mannose catabolic pathway (mannose → fructose-6-phosphate via phosphomannose isomerase for carbon assimilation) has been demonstrated as a physiologically important route, though fructose-to-mannose isomerization has been observed under bioelectrochemical conditions (nguyen2021theanoxicelectrode‐driven pages 1-2, nguyen2021theanoxicelectrode‐driven pages 5-7).

## 3. Expected Step Model

The six provisional steps and their satisfiability in KT2440 are assessed in the following table:

| Step number | Step name | Status | Genes covering the step | Missing genes/gaps | Species-specific notes |
|---|---|---|---|---|---|
| 1 | Fructose PTS import and phosphorylation | candidate_uncertain | **fruA / PP_0795** (EIIBC fructose permease); **fruB** (EI-HPr-EIIA fusion, required but absent from candidate list) | **fruB missing from metadata candidate set** | In *P. putida* KT2440, fructose uptake is via the dedicated **fruBKA** operon; FruA alone is insufficient for satisfiability because FruB provides the phosphorelay needed to generate fructose-1-phosphate. This is a strong case for promoting **fruB** into review and correcting module completeness logic (chavarria2012regulatorytasksof pages 2-2, chavarria2016ametabolicwidget pages 6-8). |
| 2 | Fructose-1-phosphate phosphorylation | covered | **fruK / PP_0794** | No clear gap once fruK is accepted | FruK is the expected kinase downstream of the fructose PTS, converting fructose-1-phosphate to fructose-1,6-bisphosphate in KT2440 fructose catabolism. Annotation should prefer **1-phosphofructokinase/fructose-1-phosphate kinase** over generic phosphofructokinase wording (chavarria2012regulatorytasksof pages 2-2, sudarsan2014thefunctionalstructure pages 7-8). |
| 3 | GDP-mannose precursor synthesis | covered | **algA / PP_1277**, **algC / PP_5288**; likely branch paralogs **PP_1776** and possibly **cpsG / PP_1777** for LPS-linked nucleotide-sugar synthesis | No obligate gap for alginate branch; **PP_1777** remains branch-specific uncertainty | In KT2440 this step is present, but it is primarily an **alginate/EPS precursor** function rather than soluble mannose catabolism. **algA** and **algC** support alginate precursor synthesis, whereas **PP_1776-PP_1777** likely serve a neighboring LPS/O-antigen branch and should not be collapsed into the same biological step without note (muhammadi2007geneticsofbacterial pages 2-3, serrato2024bacterialalginatebiosynthesis pages 6-8, santos2004insightsintothe pages 11-12, gulez2014colonymorphologyand pages 6-8). |
| 4 | GDP-mannuronate formation | covered | **algD / PP_1288** | No gap | **algD** is the committed alginate-precursor step, converting GDP-mannose to GDP-mannuronate. In KT2440 this belongs to the alginate structural operon and should be curated as **EPS biosynthesis boundary metabolism**, not core fructose assimilation (muhammadi2007geneticsofbacterial pages 2-3, rehman2013insightsintothe pages 1-2, gulez2014colonymorphologyand pages 6-8). |
| 5 | Alginate polymerization and envelope handling | module_needs_revision | **alg8 / PP_1287**, **alg44 / PP_1286**, **algG / PP_1283**, **algL / PP_1281** | Additional non-candidate alginate-envelope genes likely relevant in the full operon/context (e.g., algK/algE/algX etc.) | This step is clearly encoded in KT2440, but it belongs to the **neighboring alginate biosynthesis/export pathway**, not core fructose/mannose metabolism. The KEGG bucket is over-broad here; for module satisfiability this section should be split into a separate alginate/EPS document or explicitly marked boundary-only (muhammadi2007geneticsofbacterial pages 2-3, rehman2013insightsintothe pages 1-2, gulez2014colonymorphologyand pages 6-8, martinezgarcia2020thenakedbacterium pages 2-3). |
| 6 | Deoxy-sugar side branches | module_needs_revision | **gmd / PP_1799**, **rmd / PP_1800**, **PP_1776**; **cpsG / PP_1777** candidate branch enzyme; **fucD / PP_2831** only weakly linked | **fucD pathway support unresolved**; branch specificity of **PP_1777** needs direct review | In KT2440, **PP_1776-PP_1800** are best interpreted as part of **GDP-rhamnose/A-band LPS O-antigen biosynthesis**, not mannose central metabolism. **fucD** is a low-confidence spill-in from broader deoxy-sugar metabolism and should not be used to satisfy the module without additional locus/phenotype evidence. This whole step should be separated from the core fructose module (santos2004insightsintothe pages 11-12, nguyen2021theanoxicelectrode‐driven pages 5-7). |


*Table: This table assesses whether each provisional step in the KT2440 fructose/mannose boundary module is actually satisfied, missing, or misplaced. It is useful for curation because it distinguishes true fructose-entry reactions from adjacent alginate and LPS/O-antigen branches that KEGG groups together.*

## 4. Candidate Genes and Evidence

A comprehensive assessment of all 18 candidate genes is provided below:

| Gene name | Locus tag | UniProt ID | EC number | Assigned module step | Primary biological function | Evidence type (direct/inferred) | Evidence quality | Curation status recommendation | Key caveats |
|---|---|---|---|---|---|---|---|---|---|
| fruK | PP_0794 | Q88PQ4 | 2.7.1.- (candidate 1-phosphofructokinase; local metadata labels phosphofructokinase) | Fructose-1-phosphate phosphorylation | Likely converts fructose-1-phosphate to fructose-1,6-bisphosphate downstream of fructose PTS uptake in the fruBKA system | Direct for pathway role in KT2440 fructose catabolism; exact EC assignment inferred | High | covered | Strong pathway placement from KT2440 fructose studies, but the local annotation as generic phosphofructokinase should be curated carefully because KT2440 lacks canonical 6-phosphofructokinase-driven EMP glycolysis and fructose entry is via fructose-1-phosphate (chavarria2012regulatorytasksof pages 2-2, santos2004genomicfeaturesof pages 8-11, sudarsan2014thefunctionalstructure pages 7-8) |
| fruA | PP_0795 | Q88PQ3 | 2.7.1.202 | Fructose PTS import and phosphorylation | EIIBC fructose-specific PTS permease importing fructose and phosphorylating it to fructose-1-phosphate | Direct | High | covered | High-confidence KT2440 assignment; should be curated together with missing operon partner fruB, which is essential to the complete transport phosphorelay but absent from the candidate list (chavarria2012regulatorytasksof pages 2-2, chavarria2016ametabolicwidget pages 6-8) |
| algA | PP_1277 | Q88ND5 | 5.3.1.8; 2.7.7.13 | GDP-mannose precursor synthesis / alginate precursor branch | Bifunctional phosphomannose isomerase and mannose-1-phosphate guanylyltransferase for GDP-mannose precursor formation feeding alginate biosynthesis | Inferred to KT2440 from conserved alginate structural operon and KT2440 operon maps | High | covered | This is alginate/EPS precursor synthesis, not soluble mannose catabolism; keep separate from central fructose uptake during module curation (rehman2013insightsintothe pages 1-2, gulez2014colonymorphologyand pages 6-8, martinezgarcia2020thenakedbacterium pages 2-3) |
| algL | PP_1281 | Q88ND1 | 4.2.2.3 | Alginate polymerization / periplasmic handling | Alginate lyase involved in periplasmic editing/turnover and integrity of the alginate biosynthetic complex | Inferred to KT2440 from conserved operon structure; alginate importance shown in KT2440 EPS studies | Medium | covered | Relevant to alginate export/editing rather than fructose or mannose catabolism; inclusion in this KEGG bucket reflects pathway overbreadth (rehman2013insightsintothe pages 1-2, gulez2014colonymorphologyand pages 6-8) |
| algG | PP_1283 | Q88NC9 | 5.1.3.37 | Alginate polymer modification | Mannuronan C5-epimerase converting mannuronate residues to guluronate in polymeric alginate | Inferred to KT2440 from conserved operon structure; alginate operon directly present in KT2440 | Medium | covered | Polymer-level EPS modification, not central mannose metabolism; should likely stay in alginate-focused curation rather than a narrow carbohydrate-entry module (muhammadi2007geneticsofbacterial pages 2-3, rehman2013insightsintothe pages 1-2, gulez2014colonymorphologyand pages 6-8) |
| alg44 | PP_1286 | Q88NC6 | 2.4.-.- (polymerase-associated copolymerase/regulator; no complete EC) | Alginate polymerization | c-di-GMP-responsive copolymerase/regulatory subunit of alginate synthase complex acting with Alg8 | Inferred to KT2440 from conserved alginate operon; KT2440 structural cluster confirmed | Medium | covered | Better curated as alginate biosynthesis/export component than as fructose/mannose metabolic enzyme; avoid over-specific EC propagation (muhammadi2007geneticsofbacterial pages 2-3, rehman2013insightsintothe pages 1-2, gulez2014colonymorphologyand pages 6-8) |
| alg8 | PP_1287 | Q88NC5 | 2.4.-.- | Alginate polymerization | Inner-membrane glycosyltransferase/polymerase catalytic subunit for alginate synthesis | Inferred to KT2440 from conserved operon structure | Medium | covered | Polymerase in EPS branch; should be separated from central carbohydrate entry in module boundary definition (muhammadi2007geneticsofbacterial pages 2-3, rehman2013insightsintothe pages 1-2, gulez2014colonymorphologyand pages 6-8) |
| algD | PP_1288 | Q88NC4 | 1.1.1.132 | GDP-mannuronate formation | GDP-mannose dehydrogenase forming GDP-mannuronate, the committed alginate precursor | Direct for operon presence/regulation in KT2440; function inferred from conserved enzyme identity | High | covered | Core alginate precursor enzyme; well supported in KT2440 transcriptome/EPS studies, but belongs to EPS biosynthesis rather than mannose catabolism sensu stricto (gulez2014colonymorphologyand pages 6-8, martinezgarcia2020thenakedbacterium pages 2-3) |
| PP_1776 | PP_1776 | Q88M00 | 5.3.1.8; 2.7.7.13 | GDP-mannose-derived deoxy-sugar side branch | WbpW/AlgA-like bifunctional enzyme generating GDP-mannose precursor for GDP-rhamnose and A-band LPS O-antigen biosynthesis | Direct for KT2440 genome-based pathway assignment | High | covered | Despite AlgA-like annotation, this paralog is not the alginate operon algA; it belongs to LPS/O-antigen sugar-nucleotide biosynthesis and should not be merged with alginate precursor step without noting branch specificity (santos2004insightsintothe pages 11-12) |
| cpsG | PP_1777 | Q88LZ9 | 5.4.2.8 | GDP-mannose-derived deoxy-sugar side branch | Likely phosphomannomutase supplying mannose-1-phosphate for LPS/O-antigen nucleotide-sugar synthesis near the wbp/gmd/rmd cluster | Inferred from genomic context in KT2440 | Medium | candidate_uncertain | Plausible branch-specific PMM, but direct functional evidence in KT2440 was not retrieved; possible redundancy/overlap with broad-specificity AlgC should be reviewed in detail (santos2004insightsintothe pages 11-12) |
| gmd | PP_1799 | Q88LX8 | 4.2.1.47 | GDP-mannose-derived deoxy-sugar side branch | GDP-mannose 4,6-dehydratase for GDP-rhamnose precursor formation used in A-band LPS O-antigen biosynthesis | Direct | High | covered | Local metadata ties this to fructose/mannose metabolism, but direct KT2440 genomic evidence places it in LPS O-antigen/rhamnose biosynthesis, not alginate or central mannose assimilation (santos2004insightsintothe pages 11-12) |
| rmd | PP_1800 | Q88LX7 | not assigned in local metadata | GDP-mannose-derived deoxy-sugar side branch | Rhamnose-pathway oxidoreductase acting downstream of Gmd in GDP-rhamnose formation for A-band LPS O-antigen | Direct for branch assignment; exact enzymology inferred | High | covered | Annotation should emphasize LPS O-antigen/GDP-rhamnose branch; avoid vague placement under generic fructose/mannose metabolism (santos2004insightsintothe pages 11-12) |
| PP_2037 | PP_2037 | Q88L98 | not assigned | Central carbon interconversion (overview-map spillover) | Aldolase family protein in broader central carbon metabolism | Inferred only | Low | not_expected_in_target_taxon | No retrieved evidence links PP_2037 specifically to the fructose/mannose boundary module in KT2440; likely included because KEGG overview maps spill central-carbon enzymes into multiple pathways (sudarsan2014thefunctionalstructure pages 6-7, santos2004insightsintothe pages 4-5) |
| fucD | PP_2831 | Q88J18 | 4.2.1.68 | Deoxy-sugar catabolic side branch | Putative L-fuconate dehydratase in a non-phosphorylative fucose degradation route | Inferred only | Low | candidate_uncertain | Retrieved evidence supports the enzyme class generally but not a resolved KT2440 pathway or growth phenotype on L-fucose; should not be counted for module satisfiability without additional locus-context or phenotype evidence (nguyen2021theanoxicelectrode‐driven pages 5-7) |
| tpiA | PP_4715 | Q88DV4 | 5.3.1.1 | Lower central-carbon metabolism / overview-map spillover | Triosephosphate isomerase interconverting GAP and DHAP in central metabolism | Direct for general CCM role in KT2440 | Medium | not_expected_in_target_taxon | KT2440 central metabolism contains TpiA, but flux analysis during fructose growth found no detectable flux through TpiA in the relevant route; not an essential defining step of the boundary module (sudarsan2014thefunctionalstructure pages 7-8, santos2004insightsintothe pages 4-5) |
| fba | PP_4960 | Q88D67 | 4.1.2.13 | Central carbon interconversion / overview-map spillover | Fructose-1,6-bisphosphate aldolase in EMP-like interconversions | Direct for general CCM role in KT2440 | Medium | not_expected_in_target_taxon | Present in KT2440, but fructose fluxomics indicated no detectable flux through Fba during fructose catabolism; should not be used to satisfy fructose-entry steps in this organism (sudarsan2014thefunctionalstructure pages 7-8, santos2004insightsintothe pages 4-5) |
| fbp | PP_5040 | Q88CY9 | 3.1.3.11 | Fructose-to-F6P gluconeogenic recycling connected to ED routing | Fructose-1,6-bisphosphatase class 1 functioning in the unusual fructose catabolic/gluconeogenic loop of KT2440 | Direct | High | covered | Unlike fba/tpiA, Fbp carries major flux during fructose metabolism in KT2440 and is important for the species-specific rerouting of FBP toward F6P and the ED pathway; this step is central to organism-aware module interpretation (sudarsan2014thefunctionalstructure pages 7-8, sudarsan2014thefunctionalstructure pages 8-10) |
| algC | PP_5288 | Q88C93 | 5.4.2.2; 5.4.2.8 | Mannose-1-phosphate formation for GDP-mannose precursor synthesis | Bifunctional phosphomannomutase/phosphoglucomutase linking mannose-6-phosphate to mannose-1-phosphate and also supporting other envelope polysaccharides/LPS | Inferred to KT2440 from conserved alginate pathway plus broad pseudomonad evidence | High | covered | Key caveat: multifunctional enzyme participates in alginate, LPS, and other envelope polysaccharide pathways; do not overassign it as alginate-specific, and note possible functional overlap with cpsG/PP_1777 (muhammadi2007geneticsofbacterial pages 2-3, serrato2024bacterialalginatebiosynthesis pages 6-8, gulez2014colonymorphologyand pages 6-8) |


*Table: This table summarizes all 18 candidate genes for the Pseudomonas putida KT2440 fructose and mannose metabolism boundary module, mapping each gene to a module step, evidence strength, and a curation recommendation. It is useful for deciding which genes truly satisfy the module, which belong to neighboring alginate or LPS pathways, and which candidates are likely over-annotations.*

### 4.1 High-confidence genes with direct KT2440 evidence

**fruA (PP_0795) and fruK (PP_0794).** These are part of the well-characterized fruBKA operon. FruA is the EIIBCFru membrane permease that imports fructose with concomitant phosphorylation to fructose-1-phosphate (chavarria2012regulatorytasksof pages 2-2). FruK converts fructose-1-phosphate to FBP (chavarria2012regulatorytasksof pages 2-2, sudarsan2014thefunctionalstructure pages 7-8). Expression of fruBKA is repressed by the Cra regulator and derepressed by intracellular fructose-1-phosphate (chavarria2012regulatorytasksof pages 7-7, chavarria2016ametabolicwidget pages 1-2).

**algD (PP_1288).** GDP-mannose 6-dehydrogenase, the first gene in the alginate structural operon and the committed step for GDP-mannuronate formation. Its regulation and presence in KT2440 are confirmed by transcriptome and EPS studies (gulez2014colonymorphologyand pages 6-8).

**algA (PP_1277).** Bifunctional phosphomannose isomerase/GDP-mannose pyrophosphorylase at the terminal end of the alginate operon. Converts fructose-6-phosphate to mannose-6-phosphate and mannose-1-phosphate to GDP-mannose (ertesvag2017identificationofgenes pages 1-2, rehman2013insightsintothe pages 1-2).

**algC (PP_5288).** Bifunctional phosphomannomutase/phosphoglucomutase encoded at a separate chromosomal locus. This is the only gene in the alginate precursor pathway not located within the alginate operon. AlgC participates in alginate, LPS, and other polysaccharide biosynthesis pathways (serrato2024bacterialalginatebiosynthesis pages 6-8, gaona2004characterizationofthe pages 7-8).

**fbp (PP_5040).** Fructose-1,6-bisphosphatase class 1. ¹³C flux analysis in KT2440 demonstrated that during fructose growth, FBP is predominantly recycled through Fbp to fructose-6-phosphate for ED pathway entry, making this a functionally essential enzyme in the species-specific fructose catabolic route (sudarsan2014thefunctionalstructure pages 7-8).

**gmd (PP_1799) and rmd (PP_1800).** GDP-mannose 4,6-dehydratase and the downstream oxidoreductase for GDP-rhamnose biosynthesis. These are part of the LPS A-band O-antigen gene cluster (PP_1797–PP_1806) and serve envelope polysaccharide biosynthesis, not mannose catabolism (santos2004insightsintothe pages 11-12).

**PP_1776 (WbpW).** An AlgA paralog providing GDP-mannose for the LPS/O-antigen biosynthetic branch, not for alginate (santos2004insightsintothe pages 11-12).

### 4.2 Medium-confidence genes

**algG (PP_1283), algL (PP_1281), alg44 (PP_1286), alg8 (PP_1287).** These alginate operon components are present in KT2440 (the structural operon PP_1277–PP_1288 is confirmed) (gulez2014colonymorphologyand pages 6-8, martinezgarcia2020thenakedbacterium pages 2-3). Their specific enzymatic roles (epimerase, lyase, copolymerase, polymerase) are well characterized in *P. aeruginosa* and *P. fluorescens* and are conserved in *P. putida* by operon synteny, though direct biochemical characterization in KT2440 is limited (muhammadi2007geneticsofbacterial pages 5-7, rehman2013insightsintothe pages 1-2, serrato2024bacterialalginatebiosynthesis pages 3-6).

**cpsG (PP_1777).** Annotated as phosphomannomutase. Located near the LPS O-antigen gene cluster, this may serve as a branch-specific PMM for LPS precursor synthesis, potentially redundant with AlgC. Direct functional evidence in KT2440 is lacking (santos2004insightsintothe pages 11-12).

### 4.3 Low-confidence or misplaced genes

**tpiA (PP_4715) and fba (PP_4960).** Triosephosphate isomerase and fructose-1,6-bisphosphate aldolase are core central-carbon-metabolism enzymes. ¹³C flux analysis in KT2440 growing on fructose found no detectable flux through either enzyme in the fructose catabolic direction (sudarsan2014thefunctionalstructure pages 7-8). Their inclusion in this module reflects KEGG overview-map spillover and should be disregarded for module satisfiability.

**PP_2037.** An aldolase-family protein with no retrieved evidence linking it specifically to fructose or mannose metabolism in KT2440. Likely a KEGG map artifact.

**fucD (PP_2831).** Annotated as L-fuconate dehydratase (EC 4.2.1.68). No evidence was found for L-fucose growth or a complete non-phosphorylative fucose degradation pathway in KT2440. The gene annotation is based on sequence homology to characterized enzymes from *Xanthomonas campestris* and related organisms; its physiological role in KT2440 remains uncertain.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Critical gap: fruB missing from candidate list

The most significant gap is the absence of **fruB** from the 18-candidate gene set. FruB (EI-HPr-EIIAFru fusion protein) is essential for the fructose PTS phosphorelay cascade—without it, FruA cannot phosphorylate fructose during import (chavarria2012regulatorytasksof pages 1-2, chavarria2012regulatorytasksof pages 2-2, chavarria2016ametabolicwidget pages 6-8). FruB is encoded in the same fruBKA operon and must be added to the candidate gene list.

### 5.2 Over-broad KEGG grouping

The inclusion of alginate polymerization/modification enzymes (alg8, alg44, algG, algL) and LPS O-antigen biosynthetic enzymes (gmd, rmd, PP_1776) under "fructose and mannose metabolism" is a recognized weakness of the KEGG ppu00051 map. These represent fundamentally different biological processes:
- Alginate biosynthesis is an exopolysaccharide pathway induced under water stress (gulez2014colonymorphologyand pages 6-8, gulez2014colonymorphologyand pages 1-2).
- LPS O-antigen assembly is a constitutive envelope biosynthesis process (santos2004insightsintothe pages 11-12).
- Fructose PTS entry is a catabolic carbon-source utilization pathway (chavarria2012regulatorytasksof pages 2-2).

### 5.3 Annotation ambiguities

- **fruK** is annotated as "phosphofructokinase," which in most organisms implies 6-phosphofructokinase (PFK-1). In KT2440, which lacks PFK-1, fruK should be annotated specifically as **1-phosphofructokinase** (EC 2.7.1.56) acting on fructose-1-phosphate, not fructose-6-phosphate (santos2004genomicfeaturesof pages 8-11, sudarsan2014thefunctionalstructure pages 7-8).
- **PP_1776** is annotated as "AlgA" but functions as **WbpW** in LPS O-antigen biosynthesis, not in the alginate operon. The gene name should be disambiguated from the true alginate operon algA (PP_1277) (santos2004insightsintothe pages 11-12).
- **algC** (PP_5288) has dual phosphomannomutase/phosphoglucomutase activity and participates in multiple pathways (alginate, LPS, rhamnolipids). Over-assigning it solely to alginate is incorrect (serrato2024bacterialalginatebiosynthesis pages 6-8, gaona2004characterizationofthe pages 7-8).

### 5.4 Likely over-propagated annotations

- **tpiA**, **fba**, and **PP_2037** are generic central-metabolism enzymes included via KEGG overview-map overlap. They do not define the fructose/mannose boundary module.
- **fucD** annotation as L-fuconate dehydratase is sequence-based; no functional validation in KT2440 exists, and P. putida is not known to grow on L-fucose.

## 6. Module and GO-Curation Recommendations

### 6.1 Module step statuses

| Step | Recommended status |
|---|---|
| 1. Fructose PTS import | **candidate_uncertain** (fruB missing from candidate list) |
| 2. Fructose-1-P phosphorylation | **covered** (fruK) |
| 3. GDP-mannose precursor synthesis | **covered** (algA, algC; with branch-specific paralogs PP_1776, cpsG) |
| 4. GDP-mannuronate formation | **covered** (algD) |
| 5. Alginate polymerization/export | **module_needs_revision** (belongs to separate alginate/EPS module) |
| 6. Deoxy-sugar side branches | **module_needs_revision** (belongs to LPS/O-antigen module) |

### 6.2 Recommended module boundary revisions

The current KEGG ppu00051 bucket should be decomposed for species-level curation:

1. **Fructose PTS entry module:** fruB, fruK, fruA, and fbp (for the species-specific FBP→F6P recycling step).
2. **GDP-mannose/alginate precursor module:** algA (PP_1277), algC (PP_5288), algD (PP_1288). This can serve as a precursor sub-module for the alginate biosynthesis pathway (ppu00543).
3. **LPS O-antigen nucleotide-sugar module:** PP_1776, cpsG (PP_1777), gmd (PP_1799), rmd (PP_1800). This should link to LPS biosynthesis pathway curation.
4. **Alginate polymerization/export** (alg8, alg44, algG, algL and remaining operon genes) should remain under ppu00543 or a dedicated alginate/EPS document.

### 6.3 GO term considerations

- A GO annotation for **1-phosphofructokinase activity** (GO:0008662) should be confirmed for fruK/PP_0794 rather than generic phosphofructokinase activity.
- The GO term **protein-N(pi)-phosphohistidine-sugar phosphotransferase activity** is appropriate for fruA but the complete PTS function requires fruB, which should carry the upstream EI/HPr/EIIA GO annotations.

## 7. Genes to Promote to Full Review

1. **fruB (PP_0793 or adjacent locus):** Essential component of the fructose PTS absent from the candidate list. Must be identified, confirmed, and added. This is the highest-priority gap.
2. **cpsG (PP_1777):** Ambiguous phosphomannomutase that may be branch-specific for LPS vs. redundant with AlgC. Direct biochemical or genetic evidence in KT2440 would resolve this.
3. **fucD (PP_2831):** L-fuconate dehydratase with no demonstrated physiological role in KT2440. Needs locus-context analysis and growth phenotype testing to determine whether a fucose degradation pathway is functional.
4. **PP_2037:** Aldolase with no clear assignment to this module. Brief review to confirm it is a KEGG artifact and should be excluded.

## 8. Key References

- Chavarría M, Kleijn RJ, Sauer U, Pflüger-Grau K, de Lorenzo V. Regulatory tasks of the phosphoenolpyruvate-phosphotransferase system of *Pseudomonas putida* in central carbon metabolism. *mBio*. 2012;3(2):e00028-12. doi:10.1128/mbio.00028-12 (chavarria2012regulatorytasksof pages 1-2, chavarria2012regulatorytasksof pages 2-2, chavarria2012regulatorytasksof pages 7-7, chavarria2012regulatorytasksof pages 4-4)
- Chavarría M, Goñi-Moreno Á, de Lorenzo V, Nikel PI. A metabolic widget adjusts the phosphoenolpyruvate-dependent fructose influx in *Pseudomonas putida*. *mSystems*. 2016;1(6). doi:10.1128/msystems.00154-16 (chavarria2016ametabolicwidget pages 6-8, chavarria2016ametabolicwidget pages 1-2)
- Sudarsan S, Dethlefsen S, Blank LM, Siemann-Herzberg M, Schmid A. The functional structure of central carbon metabolism in *Pseudomonas putida* KT2440. *Appl Environ Microbiol*. 2014;80(17):5292-5303. doi:10.1128/aem.01643-14 (sudarsan2014thefunctionalstructure pages 7-8, sudarsan2014thefunctionalstructure pages 6-7, sudarsan2014thefunctionalstructure pages 8-10)
- Martins dos Santos VAP, Heim S, Moore ERB, Strätz M, Timmis KN. Insights into the genomic basis of niche specificity of *Pseudomonas putida* KT2440. *Environ Microbiol*. 2004;6(12):1264-1286. doi:10.1111/j.1462-2920.2004.00734.x (santos2004insightsintothe pages 11-12, santos2004insightsintothe pages 4-5, santos2004insightsintothe pages 5-7)
- Gulez G, Altıntaş A, Fazli M, et al. Colony morphology and transcriptome profiling of *Pseudomonas putida* KT2440 and its mutants deficient in alginate or all EPS synthesis. *MicrobiologyOpen*. 2014;3(4):457-469. doi:10.1002/mbo3.180 (gulez2014colonymorphologyand pages 6-8, gulez2014colonymorphologyand pages 1-2)
- Muhammadi, Ahmed N. Genetics of bacterial alginate: alginate genes distribution, organization and biosynthesis in bacteria. *Curr Genomics*. 2007;8(3):191-202. doi:10.2174/138920207780833810 (muhammadi2007geneticsofbacterial pages 2-3, muhammadi2007geneticsofbacterial pages 5-7, muhammadi2007geneticsofbacterial pages 1-2)
- Rehman ZU, Wang Y, Moradali MF, Hay ID, Rehm BHA. Insights into the assembly of the alginate biosynthesis machinery in *Pseudomonas aeruginosa*. *Appl Environ Microbiol*. 2013;79(10):3264-3272. doi:10.1128/aem.00460-13 (rehman2013insightsintothe pages 1-2)
- Serrato RV. Bacterial alginate biosynthesis and metabolism. *Biochemistry*. 2024. doi:10.5772/intechopen.109295 (serrato2024bacterialalginatebiosynthesis pages 6-8, serrato2024bacterialalginatebiosynthesis pages 3-6)
- Ertesvåg H, Sletta H, Senneset M, et al. Identification of genes affecting alginate biosynthesis in *Pseudomonas fluorescens*. *BMC Genomics*. 2017;18:82. doi:10.1186/s12864-016-3467-7 (ertesvag2017identificationofgenes pages 1-2)
- Nguyen AV, Lai B, Adrian L, Krömer JO. The anoxic electrode-driven fructose catabolism of *Pseudomonas putida* KT2440. *Microb Biotechnol*. 2021;14(4):1784-1796. doi:10.1111/1751-7915.13862 (nguyen2021theanoxicelectrode‐driven pages 1-2, nguyen2021theanoxicelectrode‐driven pages 5-7)
- Martínez-García E, Fraile S, Rodríguez Espeso D, et al. The naked bacterium: emerging properties of a surfome-streamlined *Pseudomonas putida* strain. *ACS Synth Biol*. 2020;9(9):2477-2492. doi:10.1021/acssynbio.0c00272 (martinezgarcia2020thenakedbacterium pages 2-3)
- Gaona G, Núñez C, Goldberg JB, et al. Characterization of the *Azotobacter vinelandii* algC gene involved in alginate and lipopolysaccharide production. *FEMS Microbiol Lett*. 2004;238(1):199-206. doi:10.1111/j.1574-6968.2004.tb09756.x (gaona2004characterizationofthe pages 7-8)
- Martins dos Santos VAP, Timmis KN, Tümmler B, Weinel C. Genomic features of *Pseudomonas putida* strain KT2440. In: *Pseudomonas*. Springer; 2004:77-112. doi:10.1007/978-1-4419-9086-0_3 (santos2004genomicfeaturesof pages 8-11)

References

1. (chavarria2012regulatorytasksof pages 1-2): Max Chavarría, Roelco J. Kleijn, Uwe Sauer, Katharina Pflüger-Grau, and Víctor de Lorenzo. Regulatory tasks of the phosphoenolpyruvate-phosphotransferase system of pseudomonas putida in central carbon metabolism. May 2012. URL: https://doi.org/10.1128/mbio.00028-12, doi:10.1128/mbio.00028-12. This article has 97 citations and is from a domain leading peer-reviewed journal.

2. (chavarria2012regulatorytasksof pages 2-2): Max Chavarría, Roelco J. Kleijn, Uwe Sauer, Katharina Pflüger-Grau, and Víctor de Lorenzo. Regulatory tasks of the phosphoenolpyruvate-phosphotransferase system of pseudomonas putida in central carbon metabolism. May 2012. URL: https://doi.org/10.1128/mbio.00028-12, doi:10.1128/mbio.00028-12. This article has 97 citations and is from a domain leading peer-reviewed journal.

3. (chavarria2016ametabolicwidget pages 6-8): Max Chavarría, Ángel Goñi-Moreno, Víctor de Lorenzo, and Pablo I. Nikel. A metabolic widget adjusts the phosphoenolpyruvate-dependent fructose influx in pseudomonas putida. mSystems, Dec 2016. URL: https://doi.org/10.1128/msystems.00154-16, doi:10.1128/msystems.00154-16. This article has 42 citations and is from a peer-reviewed journal.

4. (santos2004genomicfeaturesof pages 8-11): Vitor A. P. Martins dos Santos, Kenneth N. Timmis, Burkhard Tümmler, and Christian Weinel. Genomic features of pseudomonas putida strain kt2440. ArXiv, pages 77-112, Jan 2004. URL: https://doi.org/10.1007/978-1-4419-9086-0\_3, doi:10.1007/978-1-4419-9086-0\_3. This article has 19 citations.

5. (sudarsan2014thefunctionalstructure pages 7-8): Suresh Sudarsan, Sarah Dethlefsen, Lars M. Blank, Martin Siemann-Herzberg, and Andreas Schmid. The functional structure of central carbon metabolism in pseudomonas putida kt2440. Applied and Environmental Microbiology, 80:5292-5303, Sep 2014. URL: https://doi.org/10.1128/aem.01643-14, doi:10.1128/aem.01643-14. This article has 155 citations and is from a peer-reviewed journal.

6. (chavarria2012regulatorytasksof pages 4-4): Max Chavarría, Roelco J. Kleijn, Uwe Sauer, Katharina Pflüger-Grau, and Víctor de Lorenzo. Regulatory tasks of the phosphoenolpyruvate-phosphotransferase system of pseudomonas putida in central carbon metabolism. May 2012. URL: https://doi.org/10.1128/mbio.00028-12, doi:10.1128/mbio.00028-12. This article has 97 citations and is from a domain leading peer-reviewed journal.

7. (ertesvag2017identificationofgenes pages 1-2): Helga Ertesvåg, Håvard Sletta, Mona Senneset, Yi-Qian Sun, Geir Klinkenberg, Therese Aursand Konradsen, Trond E. Ellingsen, and Svein Valla. Identification of genes affecting alginate biosynthesis in pseudomonas fluorescens by screening a transposon insertion library. BMC Genomics, Jan 2017. URL: https://doi.org/10.1186/s12864-016-3467-7, doi:10.1186/s12864-016-3467-7. This article has 35 citations and is from a peer-reviewed journal.

8. (serrato2024bacterialalginatebiosynthesis pages 6-8): Rodrigo Vassoler Serrato. Bacterial alginate biosynthesis and metabolism. Biochemistry, May 2024. URL: https://doi.org/10.5772/intechopen.109295, doi:10.5772/intechopen.109295. This article has 6 citations and is from a peer-reviewed journal.

9. (rehman2013insightsintothe pages 1-2): Zahid U. Rehman, Yajie Wang, M. Fata Moradali, Iain D. Hay, and Bernd H. A. Rehm. Insights into the assembly of the alginate biosynthesis machinery in pseudomonas aeruginosa. Applied and Environmental Microbiology, 79:3264-3272, May 2013. URL: https://doi.org/10.1128/aem.00460-13, doi:10.1128/aem.00460-13. This article has 73 citations and is from a peer-reviewed journal.

10. (muhammadi2007geneticsofbacterial pages 2-3): Muhammadi and Nuzhat Ahmed. Genetics of bacterial alginate: alginate genes distribution, organization and biosynthesis in bacteria. Current Genomics, 8:191-202, May 2007. URL: https://doi.org/10.2174/138920207780833810, doi:10.2174/138920207780833810. This article has 80 citations and is from a peer-reviewed journal.

11. (gulez2014colonymorphologyand pages 6-8): Gamze Gulez, Ali Altıntaş, Mustafa Fazli, Arnaud Dechesne, Christopher T. Workman, Tim Tolker‐Nielsen, and Barth F. Smets. Colony morphology and transcriptome profiling of pseudomonas putida kt2440 and its mutants deficient in alginate or all eps synthesis under controlled matric potentials. MicrobiologyOpen, 3:457-469, Jun 2014. URL: https://doi.org/10.1002/mbo3.180, doi:10.1002/mbo3.180. This article has 33 citations and is from a peer-reviewed journal.

12. (gulez2014colonymorphologyand pages 1-2): Gamze Gulez, Ali Altıntaş, Mustafa Fazli, Arnaud Dechesne, Christopher T. Workman, Tim Tolker‐Nielsen, and Barth F. Smets. Colony morphology and transcriptome profiling of pseudomonas putida kt2440 and its mutants deficient in alginate or all eps synthesis under controlled matric potentials. MicrobiologyOpen, 3:457-469, Jun 2014. URL: https://doi.org/10.1002/mbo3.180, doi:10.1002/mbo3.180. This article has 33 citations and is from a peer-reviewed journal.

13. (santos2004insightsintothe pages 11-12): V. A. P. Martins Dos Santos, S. Heim, E. R. B. Moore, M. Strätz, and K. N. Timmis. Insights into the genomic basis of niche specificity of pseudomonas putida kt2440. Environmental microbiology, 6 12:1264-86, Dec 2004. URL: https://doi.org/10.1111/j.1462-2920.2004.00734.x, doi:10.1111/j.1462-2920.2004.00734.x. This article has 343 citations and is from a domain leading peer-reviewed journal.

14. (nguyen2021theanoxicelectrode‐driven pages 1-2): Anh Vu Nguyen, Bin Lai, Lorenz Adrian, and Jens O. Krömer. The anoxic electrode‐driven fructose catabolism of pseudomonas putida kt2440. Microbial Biotechnology, 14:1784-1796, Jun 2021. URL: https://doi.org/10.1111/1751-7915.13862, doi:10.1111/1751-7915.13862. This article has 13 citations and is from a peer-reviewed journal.

15. (nguyen2021theanoxicelectrode‐driven pages 5-7): Anh Vu Nguyen, Bin Lai, Lorenz Adrian, and Jens O. Krömer. The anoxic electrode‐driven fructose catabolism of pseudomonas putida kt2440. Microbial Biotechnology, 14:1784-1796, Jun 2021. URL: https://doi.org/10.1111/1751-7915.13862, doi:10.1111/1751-7915.13862. This article has 13 citations and is from a peer-reviewed journal.

16. (martinezgarcia2020thenakedbacterium pages 2-3): Esteban Martínez-García, Sofía Fraile, David Rodríguez Espeso, Davide Vecchietti, Giovanni Bertoni, and Víctor de Lorenzo. The naked bacterium: emerging properties of a surfome-streamlined pseudomonas putida strain. ACS synthetic biology, 9:2477-2492, Jul 2020. URL: https://doi.org/10.1021/acssynbio.0c00272, doi:10.1021/acssynbio.0c00272. This article has 31 citations and is from a domain leading peer-reviewed journal.

17. (sudarsan2014thefunctionalstructure pages 6-7): Suresh Sudarsan, Sarah Dethlefsen, Lars M. Blank, Martin Siemann-Herzberg, and Andreas Schmid. The functional structure of central carbon metabolism in pseudomonas putida kt2440. Applied and Environmental Microbiology, 80:5292-5303, Sep 2014. URL: https://doi.org/10.1128/aem.01643-14, doi:10.1128/aem.01643-14. This article has 155 citations and is from a peer-reviewed journal.

18. (santos2004insightsintothe pages 4-5): V. A. P. Martins Dos Santos, S. Heim, E. R. B. Moore, M. Strätz, and K. N. Timmis. Insights into the genomic basis of niche specificity of pseudomonas putida kt2440. Environmental microbiology, 6 12:1264-86, Dec 2004. URL: https://doi.org/10.1111/j.1462-2920.2004.00734.x, doi:10.1111/j.1462-2920.2004.00734.x. This article has 343 citations and is from a domain leading peer-reviewed journal.

19. (sudarsan2014thefunctionalstructure pages 8-10): Suresh Sudarsan, Sarah Dethlefsen, Lars M. Blank, Martin Siemann-Herzberg, and Andreas Schmid. The functional structure of central carbon metabolism in pseudomonas putida kt2440. Applied and Environmental Microbiology, 80:5292-5303, Sep 2014. URL: https://doi.org/10.1128/aem.01643-14, doi:10.1128/aem.01643-14. This article has 155 citations and is from a peer-reviewed journal.

20. (chavarria2012regulatorytasksof pages 7-7): Max Chavarría, Roelco J. Kleijn, Uwe Sauer, Katharina Pflüger-Grau, and Víctor de Lorenzo. Regulatory tasks of the phosphoenolpyruvate-phosphotransferase system of pseudomonas putida in central carbon metabolism. May 2012. URL: https://doi.org/10.1128/mbio.00028-12, doi:10.1128/mbio.00028-12. This article has 97 citations and is from a domain leading peer-reviewed journal.

21. (chavarria2016ametabolicwidget pages 1-2): Max Chavarría, Ángel Goñi-Moreno, Víctor de Lorenzo, and Pablo I. Nikel. A metabolic widget adjusts the phosphoenolpyruvate-dependent fructose influx in pseudomonas putida. mSystems, Dec 2016. URL: https://doi.org/10.1128/msystems.00154-16, doi:10.1128/msystems.00154-16. This article has 42 citations and is from a peer-reviewed journal.

22. (gaona2004characterizationofthe pages 7-8): Gerardo Gaona, Cinthia NÃºÃ±ez, Joanna B. Goldberg, Alicia S. Linford, Rebeca NÃ¡jera, Miguel CastaÃ±eda, Josefina GuzmÃ¡n, Guadalupe EspÃ­n, and Gloria SoberÃ³n-ChÃ¡vez. Characterization of the azotobacter vinelandii algc gene involved in alginate and lipopolysaccharide production. FEMS microbiology letters, 238 1:199-206, Sep 2004. URL: https://doi.org/10.1111/j.1574-6968.2004.tb09756.x, doi:10.1111/j.1574-6968.2004.tb09756.x. This article has 46 citations and is from a peer-reviewed journal.

23. (muhammadi2007geneticsofbacterial pages 5-7): Muhammadi and Nuzhat Ahmed. Genetics of bacterial alginate: alginate genes distribution, organization and biosynthesis in bacteria. Current Genomics, 8:191-202, May 2007. URL: https://doi.org/10.2174/138920207780833810, doi:10.2174/138920207780833810. This article has 80 citations and is from a peer-reviewed journal.

24. (serrato2024bacterialalginatebiosynthesis pages 3-6): Rodrigo Vassoler Serrato. Bacterial alginate biosynthesis and metabolism. Biochemistry, May 2024. URL: https://doi.org/10.5772/intechopen.109295, doi:10.5772/intechopen.109295. This article has 6 citations and is from a peer-reviewed journal.

25. (santos2004insightsintothe pages 5-7): V. A. P. Martins Dos Santos, S. Heim, E. R. B. Moore, M. Strätz, and K. N. Timmis. Insights into the genomic basis of niche specificity of pseudomonas putida kt2440. Environmental microbiology, 6 12:1264-86, Dec 2004. URL: https://doi.org/10.1111/j.1462-2920.2004.00734.x, doi:10.1111/j.1462-2920.2004.00734.x. This article has 343 citations and is from a domain leading peer-reviewed journal.

26. (muhammadi2007geneticsofbacterial pages 1-2): Muhammadi and Nuzhat Ahmed. Genetics of bacterial alginate: alginate genes distribution, organization and biosynthesis in bacteria. Current Genomics, 8:191-202, May 2007. URL: https://doi.org/10.2174/138920207780833810, doi:10.2174/138920207780833810. This article has 80 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__fructose_mannose_metabolism__ppu00051-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__fructose_mannose_metabolism__ppu00051-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. chavarria2012regulatorytasksof pages 4-4
2. gulez2014colonymorphologyand pages 1-2
3. santos2004insightsintothe pages 11-12
4. chavarria2012regulatorytasksof pages 2-2
5. gulez2014colonymorphologyand pages 6-8
6. sudarsan2014thefunctionalstructure pages 7-8
7. rehman2013insightsintothe pages 1-2
8. ertesvag2017identificationofgenes pages 1-2
9. martinezgarcia2020thenakedbacterium pages 2-3
10. gaona2004characterizationofthe pages 7-8
11. santos2004genomicfeaturesof pages 8-11
12. chavarria2012regulatorytasksof pages 1-2
13. chavarria2016ametabolicwidget pages 6-8
14. serrato2024bacterialalginatebiosynthesis pages 6-8
15. muhammadi2007geneticsofbacterial pages 2-3
16. sudarsan2014thefunctionalstructure pages 6-7
17. santos2004insightsintothe pages 4-5
18. sudarsan2014thefunctionalstructure pages 8-10
19. chavarria2012regulatorytasksof pages 7-7
20. chavarria2016ametabolicwidget pages 1-2
21. muhammadi2007geneticsofbacterial pages 5-7
22. serrato2024bacterialalginatebiosynthesis pages 3-6
23. santos2004insightsintothe pages 5-7
24. muhammadi2007geneticsofbacterial pages 1-2
25. Includes: Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP) (GTP--mannose-1-phosphate guanylyltransferase)
26. https://doi.org/10.1128/mbio.00028-12,
27. https://doi.org/10.1128/msystems.00154-16,
28. https://doi.org/10.1007/978-1-4419-9086-0\_3,
29. https://doi.org/10.1128/aem.01643-14,
30. https://doi.org/10.1186/s12864-016-3467-7,
31. https://doi.org/10.5772/intechopen.109295,
32. https://doi.org/10.1128/aem.00460-13,
33. https://doi.org/10.2174/138920207780833810,
34. https://doi.org/10.1002/mbo3.180,
35. https://doi.org/10.1111/j.1462-2920.2004.00734.x,
36. https://doi.org/10.1111/1751-7915.13862,
37. https://doi.org/10.1021/acssynbio.0c00272,
38. https://doi.org/10.1111/j.1574-6968.2004.tb09756.x,