---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T17:37:50.350799'
end_time: '2026-07-06T17:58:05.771664'
duration_seconds: 1215.42
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-histidine biosynthesis (microbial)
  module_summary: 'De novo biosynthesis of L-histidine from 5-phospho-alpha-D-ribose
    1-diphosphate (PRPP) and ATP. This is an ancient, largely linear pathway of ten
    enzymatic activities that is broadly conserved across bacteria, archaea, fungi,
    and plants, and is the canonical microbial route. The pathway is metabolically
    unusual in that its purine-like intermediates connect it to nucleotide metabolism:
    the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide
    ribonucleotide), a purine-biosynthesis intermediate, recycling the adenine ring
    of ATP back into the nucleotide pool. Several activities are commonly fused or
    bifunctional in microbes (e.g. the HisIE pyrophosphohydrolase/cyclohydrolase,
    and the HisB dehydratase fused to a histidinol-phosphate phosphatase domain in
    enteric bacteria), and the terminal HisD histidinol dehydrogenase performs two
    successive NAD+-dependent oxidations through a histidinal intermediate. The pathway
    is energetically expensive and is tightly regulated, classically by feedback inhibition
    of the first committed enzyme (ATP phosphoribosyltransferase, HisG) by L-histidine.'
  module_outline: "- L-histidine biosynthesis\n  - 1. PRPP supply (shared, not histidine-specific)\n\
    \  - Ribose-5-phosphate to PRPP\n    - prs: ribose-phosphate diphosphokinase (molecular\
    \ player: ribose phosphate diphosphokinase activity; activity or role: ribose\
    \ phosphate diphosphokinase activity)\n  - 2. first committed step\n  - PRPP to\
    \ phosphoribosyl-ATP\n    - hisG: ATP phosphoribosyltransferase (molecular player:\
    \ ATP phosphoribosyltransferase activity; activity or role: ATP phosphoribosyltransferase\
    \ activity)\n  - 3. pyrophosphohydrolase (often HisIE bifunctional)\n  - Phosphoribosyl-ATP\
    \ to phosphoribosyl-AMP\n    - hisE: phosphoribosyl-ATP diphosphatase (molecular\
    \ player: phosphoribosyl-ATP diphosphatase activity; activity or role: phosphoribosyl-ATP\
    \ diphosphatase activity)\n  - 4. cyclohydrolase (often HisIE bifunctional)\n\
    \  - Phosphoribosyl-AMP to ProFAR\n    - hisI: phosphoribosyl-AMP cyclohydrolase\
    \ (molecular player: phosphoribosyl-AMP cyclohydrolase (HisI / HisIE); activity\
    \ or role: phosphoribosyl-AMP cyclohydrolase activity)\n  - 5. amino-isomerase\n\
    \  - ProFAR to PRFAR\n    - hisA: ProFAR isomerase (molecular player: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide\
    \ isomerase activity; activity or role: ProFAR isomerase activity)\n  - 6. imidazole-glycerol-phosphate\
    \ synthase (glutamine amidotransferase)\n  - PRFAR to imidazole-glycerol-phosphate\
    \ + AICAR\n    - hisF: IGP synthase, cyclase subunit (molecular player: imidazole-glycerol-phosphate\
    \ synthase cyclase subunit HisF; activity or role: imidazoleglycerol-phosphate\
    \ synthase activity)\n    - hisH: IGP synthase, glutamine amidotransferase subunit\
    \ (molecular player: imidazole-glycerol-phosphate synthase amidotransferase subunit\
    \ HisH; activity or role: imidazoleglycerol-phosphate synthase activity)\n  -\
    \ 7. dehydratase\n  - IGP to imidazole-acetol phosphate\n    - hisB: imidazoleglycerol-phosphate\
    \ dehydratase (molecular player: imidazoleglycerol-phosphate dehydratase activity;\
    \ activity or role: imidazoleglycerol-phosphate dehydratase activity)\n  - 8.\
    \ transaminase\n  - Imidazole-acetol phosphate to L-histidinol phosphate\n   \
    \ - hisC: histidinol-phosphate aminotransferase (molecular player: histidinol-phosphate\
    \ aminotransferase activity; activity or role: histidinol-phosphate aminotransferase\
    \ activity)\n  - 9. phosphatase\n  - L-histidinol phosphate to L-histidinol\n\
    \    - hisN: histidinol-phosphate phosphatase (molecular player: histidinol-phosphatase\
    \ activity; activity or role: histidinol-phosphatase activity)\n  - 10. terminal\
    \ bifunctional dehydrogenase\n  - L-histidinol to L-histidine\n    - hisD: histidinol\
    \ dehydrogenase (molecular player: histidinol dehydrogenase activity; activity\
    \ or role: histidinol dehydrogenase activity)"
  module_connections: '- Ribose-5-phosphate to PRPP feeds into PRPP to phosphoribosyl-ATP:
    PRPP from the diphosphokinase feeds the first committed step.

    - PRPP to phosphoribosyl-ATP precedes Phosphoribosyl-ATP to phosphoribosyl-AMP

    - Phosphoribosyl-ATP to phosphoribosyl-AMP precedes Phosphoribosyl-AMP to ProFAR

    - Phosphoribosyl-AMP to ProFAR precedes ProFAR to PRFAR

    - ProFAR to PRFAR precedes PRFAR to imidazole-glycerol-phosphate + AICAR

    - PRFAR to imidazole-glycerol-phosphate + AICAR precedes IGP to imidazole-acetol
    phosphate

    - IGP to imidazole-acetol phosphate precedes Imidazole-acetol phosphate to L-histidinol
    phosphate

    - Imidazole-acetol phosphate to L-histidinol phosphate precedes L-histidinol phosphate
    to L-histidinol

    - L-histidinol phosphate to L-histidinol precedes L-histidinol to L-histidine'
  pathway_query: ppu00340
  pathway_id: ppu00340
  pathway_name: Histidine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00340 with 18 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '20'
  candidate_genes: '- gshA: PP_0243 | Q88R90 | Glutamate--cysteine ligase (EC 6.3.2.2)
    (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) (EC 6.3.2.2; primary bucket
    kegg:ppu00340)

    - hisB: PP_0289 | Q88R45 | Imidazoleglycerol-phosphate dehydratase (IGPD) (EC
    4.2.1.19) (EC 4.2.1.19; primary bucket kegg:ppu00340)

    - hisH: PP_0290 | Q88R44 | Imidazole glycerol phosphate synthase subunit HisH
    (EC 4.3.2.10) (IGP synthase glutaminase subunit) (EC 3.5.1.2) (IGP synthase subunit
    HisH) (ImGP synthase subunit HisH) (IGPS subunit HisH) (EC 3.5.1.2; 4.3.2.10;
    primary bucket kegg:ppu00340)

    - hisA: PP_0292 | Q88R42 | 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]
    imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosphoribosylformimino-5-aminoimidazole
    carboxamide ribotide isomerase) (EC 5.3.1.16; primary bucket kegg:ppu00340)

    - hisF: PP_0293 | Q88R41 | Imidazole glycerol phosphate synthase subunit HisF
    (EC 4.3.2.10) (IGP synthase cyclase subunit) (IGP synthase subunit HisF) (ImGP
    synthase subunit HisF) (IGPS subunit HisF) (EC 4.3.2.10; primary bucket kegg:ppu00340)

    - hisG: PP_0965 | Q88P87 | ATP phosphoribosyltransferase (ATP-PRT) (ATP-PRTase)
    (EC 2.4.2.17) (EC 2.4.2.17; primary bucket kegg:ppu00340)

    - hisD: PP_0966 | P59400 | Histidinol dehydrogenase (HDH) (EC 1.1.1.23) (EC 1.1.1.23;
    primary bucket kegg:ppu00340)

    - hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9)
    (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)

    - PP_1721: PP_1721 | Q88M53 | Phosphoserine phosphatase (EC 3.1.3.-) (EC 3.1.3.-;
    primary bucket kegg:ppu00340)

    - PP_3157: PP_3157 | Q88I44 | Histidinol-phosphatase (EC 3.1.3.15) (EC 3.1.3.15;
    primary bucket kegg:ppu00340)

    - hisZ: PP_4890 | Q88DD7 | ATP phosphoribosyltransferase regulatory subunit (primary
    bucket kegg:ppu00340)

    - PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3;
    primary bucket kegg:ppu00350)

    - hisI: PP_5014 | Q88D15 | Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19)
    (EC 3.5.4.19; primary bucket kegg:ppu00340)

    - hisE: PP_5015 | Q88D14 | Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31)
    (EC 3.6.1.31; primary bucket kegg:ppu00340)

    - hutG: PP_5029 | Q88D00 | N-formylglutamate deformylase (EC 3.5.1.68) (EC 3.5.1.68;
    primary bucket kegg:ppu00340)

    - hutI: PP_5030 | Q88CZ9 | Imidazolonepropionase (EC 3.5.2.7) (Imidazolone-5-propionate
    hydrolase) (EC 3.5.2.7; primary bucket kegg:ppu00340)

    - hutH: PP_5032 | Q88CZ7 | Histidine ammonia-lyase (Histidase) (EC 4.3.1.3) (EC
    4.3.1.3; primary bucket kegg:ppu00340)

    - hutU: PP_5033 | Q88CZ6 | Urocanate hydratase (Urocanase) (EC 4.2.1.49) (Imidazolonepropionate
    hydrolase) (EC 4.2.1.49; primary bucket kegg:ppu00340)

    - hutF: PP_5036 | Q88CZ3 | Formimidoylglutamate deiminase (EC 3.5.3.13) (EC 3.5.3.13;
    primary bucket kegg:ppu00340)

    - PP_5147: PP_5147 | Q88CN3 | Histidinol-phosphatase (EC 3.1.3.15) (Histidinol-phosphate
    phosphatase) (EC 3.1.3.15; primary bucket kegg:ppu00340)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__histidine_biosynthesis__ppu00340-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__histidine_biosynthesis__ppu00340-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-histidine biosynthesis (microbial) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00340
- Resolved ID: ppu00340
- Resolved name: Histidine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00340 with 18 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 20

- gshA: PP_0243 | Q88R90 | Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) (EC 6.3.2.2; primary bucket kegg:ppu00340)
- hisB: PP_0289 | Q88R45 | Imidazoleglycerol-phosphate dehydratase (IGPD) (EC 4.2.1.19) (EC 4.2.1.19; primary bucket kegg:ppu00340)
- hisH: PP_0290 | Q88R44 | Imidazole glycerol phosphate synthase subunit HisH (EC 4.3.2.10) (IGP synthase glutaminase subunit) (EC 3.5.1.2) (IGP synthase subunit HisH) (ImGP synthase subunit HisH) (IGPS subunit HisH) (EC 3.5.1.2; 4.3.2.10; primary bucket kegg:ppu00340)
- hisA: PP_0292 | Q88R42 | 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase) (EC 5.3.1.16; primary bucket kegg:ppu00340)
- hisF: PP_0293 | Q88R41 | Imidazole glycerol phosphate synthase subunit HisF (EC 4.3.2.10) (IGP synthase cyclase subunit) (IGP synthase subunit HisF) (ImGP synthase subunit HisF) (IGPS subunit HisF) (EC 4.3.2.10; primary bucket kegg:ppu00340)
- hisG: PP_0965 | Q88P87 | ATP phosphoribosyltransferase (ATP-PRT) (ATP-PRTase) (EC 2.4.2.17) (EC 2.4.2.17; primary bucket kegg:ppu00340)
- hisD: PP_0966 | P59400 | Histidinol dehydrogenase (HDH) (EC 1.1.1.23) (EC 1.1.1.23; primary bucket kegg:ppu00340)
- hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)
- PP_1721: PP_1721 | Q88M53 | Phosphoserine phosphatase (EC 3.1.3.-) (EC 3.1.3.-; primary bucket kegg:ppu00340)
- PP_3157: PP_3157 | Q88I44 | Histidinol-phosphatase (EC 3.1.3.15) (EC 3.1.3.15; primary bucket kegg:ppu00340)
- hisZ: PP_4890 | Q88DD7 | ATP phosphoribosyltransferase regulatory subunit (primary bucket kegg:ppu00340)
- PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3; primary bucket kegg:ppu00350)
- hisI: PP_5014 | Q88D15 | Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19) (EC 3.5.4.19; primary bucket kegg:ppu00340)
- hisE: PP_5015 | Q88D14 | Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31) (EC 3.6.1.31; primary bucket kegg:ppu00340)
- hutG: PP_5029 | Q88D00 | N-formylglutamate deformylase (EC 3.5.1.68) (EC 3.5.1.68; primary bucket kegg:ppu00340)
- hutI: PP_5030 | Q88CZ9 | Imidazolonepropionase (EC 3.5.2.7) (Imidazolone-5-propionate hydrolase) (EC 3.5.2.7; primary bucket kegg:ppu00340)
- hutH: PP_5032 | Q88CZ7 | Histidine ammonia-lyase (Histidase) (EC 4.3.1.3) (EC 4.3.1.3; primary bucket kegg:ppu00340)
- hutU: PP_5033 | Q88CZ6 | Urocanate hydratase (Urocanase) (EC 4.2.1.49) (Imidazolonepropionate hydrolase) (EC 4.2.1.49; primary bucket kegg:ppu00340)
- hutF: PP_5036 | Q88CZ3 | Formimidoylglutamate deiminase (EC 3.5.3.13) (EC 3.5.3.13; primary bucket kegg:ppu00340)
- PP_5147: PP_5147 | Q88CN3 | Histidinol-phosphatase (EC 3.1.3.15) (Histidinol-phosphate phosphatase) (EC 3.1.3.15; primary bucket kegg:ppu00340)

## Generic Module Context

### Working Scope

De novo biosynthesis of L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) and ATP. This is an ancient, largely linear pathway of ten enzymatic activities that is broadly conserved across bacteria, archaea, fungi, and plants, and is the canonical microbial route. The pathway is metabolically unusual in that its purine-like intermediates connect it to nucleotide metabolism: the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide ribonucleotide), a purine-biosynthesis intermediate, recycling the adenine ring of ATP back into the nucleotide pool. Several activities are commonly fused or bifunctional in microbes (e.g. the HisIE pyrophosphohydrolase/cyclohydrolase, and the HisB dehydratase fused to a histidinol-phosphate phosphatase domain in enteric bacteria), and the terminal HisD histidinol dehydrogenase performs two successive NAD+-dependent oxidations through a histidinal intermediate. The pathway is energetically expensive and is tightly regulated, classically by feedback inhibition of the first committed enzyme (ATP phosphoribosyltransferase, HisG) by L-histidine.

### Provisional Biological Outline

- L-histidine biosynthesis
  - 1. PRPP supply (shared, not histidine-specific)
  - Ribose-5-phosphate to PRPP
    - prs: ribose-phosphate diphosphokinase (molecular player: ribose phosphate diphosphokinase activity; activity or role: ribose phosphate diphosphokinase activity)
  - 2. first committed step
  - PRPP to phosphoribosyl-ATP
    - hisG: ATP phosphoribosyltransferase (molecular player: ATP phosphoribosyltransferase activity; activity or role: ATP phosphoribosyltransferase activity)
  - 3. pyrophosphohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-ATP to phosphoribosyl-AMP
    - hisE: phosphoribosyl-ATP diphosphatase (molecular player: phosphoribosyl-ATP diphosphatase activity; activity or role: phosphoribosyl-ATP diphosphatase activity)
  - 4. cyclohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-AMP to ProFAR
    - hisI: phosphoribosyl-AMP cyclohydrolase (molecular player: phosphoribosyl-AMP cyclohydrolase (HisI / HisIE); activity or role: phosphoribosyl-AMP cyclohydrolase activity)
  - 5. amino-isomerase
  - ProFAR to PRFAR
    - hisA: ProFAR isomerase (molecular player: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity; activity or role: ProFAR isomerase activity)
  - 6. imidazole-glycerol-phosphate synthase (glutamine amidotransferase)
  - PRFAR to imidazole-glycerol-phosphate + AICAR
    - hisF: IGP synthase, cyclase subunit (molecular player: imidazole-glycerol-phosphate synthase cyclase subunit HisF; activity or role: imidazoleglycerol-phosphate synthase activity)
    - hisH: IGP synthase, glutamine amidotransferase subunit (molecular player: imidazole-glycerol-phosphate synthase amidotransferase subunit HisH; activity or role: imidazoleglycerol-phosphate synthase activity)
  - 7. dehydratase
  - IGP to imidazole-acetol phosphate
    - hisB: imidazoleglycerol-phosphate dehydratase (molecular player: imidazoleglycerol-phosphate dehydratase activity; activity or role: imidazoleglycerol-phosphate dehydratase activity)
  - 8. transaminase
  - Imidazole-acetol phosphate to L-histidinol phosphate
    - hisC: histidinol-phosphate aminotransferase (molecular player: histidinol-phosphate aminotransferase activity; activity or role: histidinol-phosphate aminotransferase activity)
  - 9. phosphatase
  - L-histidinol phosphate to L-histidinol
    - hisN: histidinol-phosphate phosphatase (molecular player: histidinol-phosphatase activity; activity or role: histidinol-phosphatase activity)
  - 10. terminal bifunctional dehydrogenase
  - L-histidinol to L-histidine
    - hisD: histidinol dehydrogenase (molecular player: histidinol dehydrogenase activity; activity or role: histidinol dehydrogenase activity)

### Known Relationships Among Steps

- Ribose-5-phosphate to PRPP feeds into PRPP to phosphoribosyl-ATP: PRPP from the diphosphokinase feeds the first committed step.
- PRPP to phosphoribosyl-ATP precedes Phosphoribosyl-ATP to phosphoribosyl-AMP
- Phosphoribosyl-ATP to phosphoribosyl-AMP precedes Phosphoribosyl-AMP to ProFAR
- Phosphoribosyl-AMP to ProFAR precedes ProFAR to PRFAR
- ProFAR to PRFAR precedes PRFAR to imidazole-glycerol-phosphate + AICAR
- PRFAR to imidazole-glycerol-phosphate + AICAR precedes IGP to imidazole-acetol phosphate
- IGP to imidazole-acetol phosphate precedes Imidazole-acetol phosphate to L-histidinol phosphate
- Imidazole-acetol phosphate to L-histidinol phosphate precedes L-histidinol phosphate to L-histidinol
- L-histidinol phosphate to L-histidinol precedes L-histidinol to L-histidine

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

L-histidine biosynthesis (microbial) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00340
- Resolved ID: ppu00340
- Resolved name: Histidine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00340 with 18 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 20

- gshA: PP_0243 | Q88R90 | Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) (EC 6.3.2.2; primary bucket kegg:ppu00340)
- hisB: PP_0289 | Q88R45 | Imidazoleglycerol-phosphate dehydratase (IGPD) (EC 4.2.1.19) (EC 4.2.1.19; primary bucket kegg:ppu00340)
- hisH: PP_0290 | Q88R44 | Imidazole glycerol phosphate synthase subunit HisH (EC 4.3.2.10) (IGP synthase glutaminase subunit) (EC 3.5.1.2) (IGP synthase subunit HisH) (ImGP synthase subunit HisH) (IGPS subunit HisH) (EC 3.5.1.2; 4.3.2.10; primary bucket kegg:ppu00340)
- hisA: PP_0292 | Q88R42 | 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase) (EC 5.3.1.16; primary bucket kegg:ppu00340)
- hisF: PP_0293 | Q88R41 | Imidazole glycerol phosphate synthase subunit HisF (EC 4.3.2.10) (IGP synthase cyclase subunit) (IGP synthase subunit HisF) (ImGP synthase subunit HisF) (IGPS subunit HisF) (EC 4.3.2.10; primary bucket kegg:ppu00340)
- hisG: PP_0965 | Q88P87 | ATP phosphoribosyltransferase (ATP-PRT) (ATP-PRTase) (EC 2.4.2.17) (EC 2.4.2.17; primary bucket kegg:ppu00340)
- hisD: PP_0966 | P59400 | Histidinol dehydrogenase (HDH) (EC 1.1.1.23) (EC 1.1.1.23; primary bucket kegg:ppu00340)
- hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)
- PP_1721: PP_1721 | Q88M53 | Phosphoserine phosphatase (EC 3.1.3.-) (EC 3.1.3.-; primary bucket kegg:ppu00340)
- PP_3157: PP_3157 | Q88I44 | Histidinol-phosphatase (EC 3.1.3.15) (EC 3.1.3.15; primary bucket kegg:ppu00340)
- hisZ: PP_4890 | Q88DD7 | ATP phosphoribosyltransferase regulatory subunit (primary bucket kegg:ppu00340)
- PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3; primary bucket kegg:ppu00350)
- hisI: PP_5014 | Q88D15 | Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19) (EC 3.5.4.19; primary bucket kegg:ppu00340)
- hisE: PP_5015 | Q88D14 | Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31) (EC 3.6.1.31; primary bucket kegg:ppu00340)
- hutG: PP_5029 | Q88D00 | N-formylglutamate deformylase (EC 3.5.1.68) (EC 3.5.1.68; primary bucket kegg:ppu00340)
- hutI: PP_5030 | Q88CZ9 | Imidazolonepropionase (EC 3.5.2.7) (Imidazolone-5-propionate hydrolase) (EC 3.5.2.7; primary bucket kegg:ppu00340)
- hutH: PP_5032 | Q88CZ7 | Histidine ammonia-lyase (Histidase) (EC 4.3.1.3) (EC 4.3.1.3; primary bucket kegg:ppu00340)
- hutU: PP_5033 | Q88CZ6 | Urocanate hydratase (Urocanase) (EC 4.2.1.49) (Imidazolonepropionate hydrolase) (EC 4.2.1.49; primary bucket kegg:ppu00340)
- hutF: PP_5036 | Q88CZ3 | Formimidoylglutamate deiminase (EC 3.5.3.13) (EC 3.5.3.13; primary bucket kegg:ppu00340)
- PP_5147: PP_5147 | Q88CN3 | Histidinol-phosphatase (EC 3.1.3.15) (Histidinol-phosphate phosphatase) (EC 3.1.3.15; primary bucket kegg:ppu00340)

## Generic Module Context

### Working Scope

De novo biosynthesis of L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) and ATP. This is an ancient, largely linear pathway of ten enzymatic activities that is broadly conserved across bacteria, archaea, fungi, and plants, and is the canonical microbial route. The pathway is metabolically unusual in that its purine-like intermediates connect it to nucleotide metabolism: the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide ribonucleotide), a purine-biosynthesis intermediate, recycling the adenine ring of ATP back into the nucleotide pool. Several activities are commonly fused or bifunctional in microbes (e.g. the HisIE pyrophosphohydrolase/cyclohydrolase, and the HisB dehydratase fused to a histidinol-phosphate phosphatase domain in enteric bacteria), and the terminal HisD histidinol dehydrogenase performs two successive NAD+-dependent oxidations through a histidinal intermediate. The pathway is energetically expensive and is tightly regulated, classically by feedback inhibition of the first committed enzyme (ATP phosphoribosyltransferase, HisG) by L-histidine.

### Provisional Biological Outline

- L-histidine biosynthesis
  - 1. PRPP supply (shared, not histidine-specific)
  - Ribose-5-phosphate to PRPP
    - prs: ribose-phosphate diphosphokinase (molecular player: ribose phosphate diphosphokinase activity; activity or role: ribose phosphate diphosphokinase activity)
  - 2. first committed step
  - PRPP to phosphoribosyl-ATP
    - hisG: ATP phosphoribosyltransferase (molecular player: ATP phosphoribosyltransferase activity; activity or role: ATP phosphoribosyltransferase activity)
  - 3. pyrophosphohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-ATP to phosphoribosyl-AMP
    - hisE: phosphoribosyl-ATP diphosphatase (molecular player: phosphoribosyl-ATP diphosphatase activity; activity or role: phosphoribosyl-ATP diphosphatase activity)
  - 4. cyclohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-AMP to ProFAR
    - hisI: phosphoribosyl-AMP cyclohydrolase (molecular player: phosphoribosyl-AMP cyclohydrolase (HisI / HisIE); activity or role: phosphoribosyl-AMP cyclohydrolase activity)
  - 5. amino-isomerase
  - ProFAR to PRFAR
    - hisA: ProFAR isomerase (molecular player: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity; activity or role: ProFAR isomerase activity)
  - 6. imidazole-glycerol-phosphate synthase (glutamine amidotransferase)
  - PRFAR to imidazole-glycerol-phosphate + AICAR
    - hisF: IGP synthase, cyclase subunit (molecular player: imidazole-glycerol-phosphate synthase cyclase subunit HisF; activity or role: imidazoleglycerol-phosphate synthase activity)
    - hisH: IGP synthase, glutamine amidotransferase subunit (molecular player: imidazole-glycerol-phosphate synthase amidotransferase subunit HisH; activity or role: imidazoleglycerol-phosphate synthase activity)
  - 7. dehydratase
  - IGP to imidazole-acetol phosphate
    - hisB: imidazoleglycerol-phosphate dehydratase (molecular player: imidazoleglycerol-phosphate dehydratase activity; activity or role: imidazoleglycerol-phosphate dehydratase activity)
  - 8. transaminase
  - Imidazole-acetol phosphate to L-histidinol phosphate
    - hisC: histidinol-phosphate aminotransferase (molecular player: histidinol-phosphate aminotransferase activity; activity or role: histidinol-phosphate aminotransferase activity)
  - 9. phosphatase
  - L-histidinol phosphate to L-histidinol
    - hisN: histidinol-phosphate phosphatase (molecular player: histidinol-phosphatase activity; activity or role: histidinol-phosphatase activity)
  - 10. terminal bifunctional dehydrogenase
  - L-histidinol to L-histidine
    - hisD: histidinol dehydrogenase (molecular player: histidinol dehydrogenase activity; activity or role: histidinol dehydrogenase activity)

### Known Relationships Among Steps

- Ribose-5-phosphate to PRPP feeds into PRPP to phosphoribosyl-ATP: PRPP from the diphosphokinase feeds the first committed step.
- PRPP to phosphoribosyl-ATP precedes Phosphoribosyl-ATP to phosphoribosyl-AMP
- Phosphoribosyl-ATP to phosphoribosyl-AMP precedes Phosphoribosyl-AMP to ProFAR
- Phosphoribosyl-AMP to ProFAR precedes ProFAR to PRFAR
- ProFAR to PRFAR precedes PRFAR to imidazole-glycerol-phosphate + AICAR
- PRFAR to imidazole-glycerol-phosphate + AICAR precedes IGP to imidazole-acetol phosphate
- IGP to imidazole-acetol phosphate precedes Imidazole-acetol phosphate to L-histidinol phosphate
- Imidazole-acetol phosphate to L-histidinol phosphate precedes L-histidinol phosphate to L-histidinol
- L-histidinol phosphate to L-histidinol precedes L-histidinol to L-histidine

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

# L-Histidine Biosynthesis in *Pseudomonas putida* KT2440: Species-Aware Module Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 (NCBI taxon 160488) encodes a complete de novo L-histidine biosynthesis pathway, as expected for a prototroph capable of growth on glucose minimal medium (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 2-3). The pathway is dispersed across four chromosomal loci rather than a single compact operon as seen in enterobacteria: (i) the hisB-hisH-PP0291-hisA-hisF cluster (PP_0289–PP_0293), (ii) the hisG-hisD-hisC cluster (PP_0965–PP_0967), (iii) the hisI-hisE cluster (PP_5014–PP_5015), and (iv) the monocistronic hisZ (PP_4890) (molina‐henares2010identificationofconditionally pages 7-9). Of the ten canonical enzymatic steps, nine can be assigned with medium-to-high confidence to specific KT2440 locus tags. The one remaining ambiguity is the histidinol-phosphate phosphatase (step 9), for which two candidate genes (PP_3157 and PP_5147) are annotated but neither has been directly validated in KT2440 (kulishorn2017sequencebasedidentificationof pages 1-2, kinateder2023evolutionaryanalysisand pages 1-9). Direct experimental evidence from KT2440 (transposon mutagenesis, BarSeq fitness profiling) exists for four biosynthetic genes: hisB, hisH, hisF, and hisZ, all of which confer histidine auxotrophy when disrupted (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7, molina‐henares2010identificationofconditionally pages 2-3).

Critically, the KEGG map ppu00340 ("Histidine metabolism") conflates biosynthesis and degradation. Five of the 20 candidate genes (hutH, hutU, hutI, hutF, hutG) belong to the histidine utilization (hut) catabolic pathway and should be excluded from a biosynthesis-focused module. Two additional genes (gshA, PP_4983) are misassigned to this pathway entirely (bender2012regulationofthe pages 10-11, bender2012regulationofthe pages 3-4, wirtz2021huttfunctionsas pages 1-2, bender2012regulationofthe pages 2-3).

## 2. Target-Organism Pathway Definition

### Pathway Scope
The L-histidine biosynthesis pathway comprises ten enzymatic activities converting PRPP + ATP to L-histidine in a largely linear fashion. The pathway is metabolically connected to purine biosynthesis through the release of AICAR at the IGP synthase step, recycling the adenine ring of ATP back into the nucleotide pool (kulis‐horn2014histidinebiosynthesisits pages 4-5). PRPP supply (via ribose-phosphate diphosphokinase, Prs) is a shared precursor step and not histidine-specific.

### Pathway Boundaries
The following should be kept **separate** from the de novo biosynthesis module:
- **Histidine utilization (hut) pathway**: L-histidine → urocanate → imidazolone propionate → formiminoglutamate → formylglutamate → glutamate + formate. This is a catabolic pathway regulated by HutC and the CbrAB/NtrBC systems (bender2012regulationofthe pages 10-11, bender2012regulationofthe pages 3-4, bender2012regulationofthe pages 2-3).
- **Glutathione biosynthesis**: gshA (PP_0243) is a glutamate–cysteine ligase involved in glutathione metabolism, not histidine.
- **Tryptophan catabolism**: PP_4983 (tryptophan 2-monooxygenase) belongs to indoleacetic acid/tryptophan metabolism.
- **PRPP supply**: Shared with purine, pyrimidine, tryptophan, and NAD biosynthesis.

### Alternate Names
KEGG ppu00340 = "Histidine metabolism" (includes both biosynthesis and degradation). MetaCyc pathway: "L-histidine biosynthesis" (PWY-6326 or equivalent). The de novo biosynthesis module corresponds to KEGG Module M00026.

## 3. Expected Step Model

The canonical ten-step pathway and its gene assignments in KT2440 are summarized below.

| Step Number | Reaction (substrate to product) | Enzyme Name | EC Number | Gene Name | Locus Tag (PP_xxxx) | UniProt ID | Evidence Type | Module Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Ribose-5-phosphate + ATP -> PRPP + AMP | Ribose-phosphate diphosphokinase (shared PRPP supply; not histidine-specific) | 2.7.6.1 | prs | not provided | not provided | genome annotation; shared precursor-supply step, not pathway-specific in reviewed metadata (molina‐henares2010identificationofconditionally pages 7-9) | covered |
| 2 | PRPP + ATP -> N1-(5-phosphoribosyl)-ATP + PPi | ATP phosphoribosyltransferase, short-form catalytic/regulatory complex | 2.4.2.17 | hisG + hisZ | PP_0965 + PP_4890 | Q88P87 + Q88DD7 | hisZ direct experimental in KT2440 mutant screen; short-form HisG/HisZ architecture and regulation by homology/biochemical literature (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7, alphey2018catalyticandanticatalytic pages 1-5, read2021allostericinhibitionof pages 6-11) | covered |
| 3 | N1-(5-phosphoribosyl)-ATP -> N1-(5-phosphoribosyl)-AMP + PPi | Phosphoribosyl-ATP pyrophosphatase | 3.6.1.31 | hisE | PP_5015 | Q88D14 | genome annotation; placement in KT2440 hisIE cluster supports assignment (molina‐henares2010identificationofconditionally pages 7-9) | covered |
| 4 | N1-(5-phosphoribosyl)-AMP -> ProFAR | Phosphoribosyl-AMP cyclohydrolase | 3.5.4.19 | hisI | PP_5014 | Q88D15 | genome annotation; placement in KT2440 hisIE cluster supports assignment (molina‐henares2010identificationofconditionally pages 7-9) | covered |
| 5 | ProFAR -> PRFAR | ProFAR isomerase | 5.3.1.16 | hisA | PP_0292 | Q88R42 | genome annotation; placement in KT2440 his cluster supports assignment (molina‐henares2010identificationofconditionally pages 7-9) | covered |
| 6 | PRFAR + glutamine -> imidazole glycerol phosphate + AICAR + glutamate | Imidazole glycerol phosphate synthase (cyclase + glutaminase subunits) | 4.3.2.10 / 3.5.1.2 | hisF + hisH | PP_0293 + PP_0290 | Q88R41 + Q88R44 | direct experimental in KT2440 mutant screen (hisF, hisH auxotrophy); cluster assignment supports pathway role (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7) | covered |
| 7 | Imidazole glycerol phosphate -> imidazole acetol phosphate + H2O | Imidazoleglycerol-phosphate dehydratase | 4.2.1.19 | hisB | PP_0289 | Q88R45 | direct experimental in KT2440 mutant screen; monofunctional dehydratase assignment favored over enterobacterial bifunctional HisB model (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7, kulis‐horn2014histidinebiosynthesisits pages 6-7) | covered |
| 8 | Imidazole acetol phosphate + glutamate -> L-histidinol-phosphate + 2-oxoglutarate | Histidinol-phosphate aminotransferase | 2.6.1.9 | hisC | PP_0967 | Q88P86 | genome annotation plus functional genetics in KT2440/BarSeq indicating essential biosynthetic role but likely broad aminotransferase specificity (schmidt2022nitrogenmetabolismin pages 10-12) | covered |
| 9 | L-histidinol-phosphate -> L-histidinol + Pi | Histidinol-phosphate phosphatase (HAD-type candidate[s]) | 3.1.3.15 | unknown canonical name; candidates PP_3157 and/or PP_5147 | PP_3157 and/or PP_5147 | Q88I44 and/or Q88CN3 | homology-based and genome annotation only; Pseudomonas expected to use a separate HAD-type HolPase/HisN-like enzyme, but direct KT2440 assignment unresolved (kulishorn2017sequencebasedidentificationof pages 1-2, kinateder2023evolutionaryanalysisand pages 1-9, ingle2011histidinebiosynthesis pages 4-5) | candidate_uncertain |
| 10 | L-histidinol + 2 NAD+ + H2O -> L-histidine + 2 NADH + 2 H+ | Histidinol dehydrogenase | 1.1.1.23 | hisD | PP_0966 | P59400 | genome annotation; placement in KT2440 hisGDC cluster supports assignment (molina‐henares2010identificationofconditionally pages 7-9) | covered |


*Table: This table maps the canonical 10-step microbial L-histidine biosynthesis pathway onto candidate genes in Pseudomonas putida KT2440, highlighting which steps are well supported versus still uncertain. It is useful for module satisfiability and annotation curation, especially for the unresolved histidinol-phosphatase step.*

### Key Organism-Specific Features

**Short-form ATP phosphoribosyltransferase (HisG/HisZ).** *P. putida* KT2440 utilizes the short-form (HisGS) architecture for step 2, in which the catalytic subunit HisG (PP_0965, ~30 kDa) lacks the C-terminal ACT regulatory domain found in long-form enzymes (e.g., *E. coli* HisG) (khajeaian2022exploringtheevolution pages 25-32). Instead, a separate regulatory protein HisZ (PP_4890), a paralog of histidyl-tRNA synthetase, assembles with HisG to form a hetero-octameric complex (4×HisGS + 4×HisZ) (alphey2018catalyticandanticatalytic pages 1-5, khajeaian2022exploringtheevolution pages 82-85). HisZ serves dual functions: it activates HisG catalysis in the absence of histidine and mediates allosteric feedback inhibition when histidine is present (read2021allostericinhibitionof pages 6-11, khajeaian2022exploringtheevolution pages 95-100). Disruption of hisZ in KT2440 produces histidine auxotrophy, confirming that HisG requires HisZ for adequate catalytic activity in vivo (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 2-3).

**Monofunctional HisB.** Unlike the bifunctional HisB of *E. coli* and *S. typhimurium* (which carries both imidazoleglycerol-phosphate dehydratase and histidinol-phosphate phosphatase activities), KT2440 HisB (PP_0289) is a monofunctional dehydratase (step 7 only). The phosphatase activity required for step 9 must be supplied by a separate gene product (kulis‐horn2014histidinebiosynthesisits pages 7-9, kulis‐horn2014histidinebiosynthesisits pages 6-7).

**Separate hisI and hisE.** In many bacteria, steps 3 and 4 are fused in a bifunctional HisIE protein. In KT2440, hisI (PP_5014) and hisE (PP_5015) are co-located but encoded as distinct open reading frames, consistent with the Pseudomonas lineage pattern (molina‐henares2010identificationofconditionally pages 7-9).

**Dispersed gene organization.** The histidine biosynthesis genes are distributed across four chromosomal locations forming at least three operons, rather than a single compact operon (molina‐henares2010identificationofconditionally pages 7-9). This is similar to the dispersed organization seen in *Corynebacterium glutamicum* (kulis‐horn2014histidinebiosynthesisits pages 9-11) and contrasts with the single his operon of enterobacteria.

## 4. Candidate Genes and Evidence

| Gene Name | Locus Tag | UniProt | Annotated Function | True Pathway Assignment | Evidence Quality | Curation Notes |
|---|---|---|---|---|---|---|
| gshA | PP_0243 | Q88R90 | Glutamate--cysteine ligase | glutathione | low | Over-propagated from broad KEGG map; no evidence this is part of histidine metabolism in KT2440. Should be removed from histidine pathway review set. |
| hisB | PP_0289 | Q88R45 | Imidazoleglycerol-phosphate dehydratase | biosynthesis | high | Canonical histidine biosynthesis step 7. Direct KT2440 mutant evidence supports histidine auxotrophy when disrupted; in Pseudomonas this is monofunctional dehydratase, not the enterobacterial bifunctional HisB model (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7, kulis‐horn2014histidinebiosynthesisits pages 6-7). |
| hisH | PP_0290 | Q88R44 | Imidazole glycerol phosphate synthase subunit HisH | biosynthesis | high | Canonical biosynthesis step 6 glutaminase subunit. Direct KT2440 mutant evidence supports histidine auxotrophy (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7). |
| hisA | PP_0292 | Q88R42 | ProFAR isomerase | biosynthesis | medium | Canonical biosynthesis step 5. Strong pathway fit and cluster context in KT2440, but no direct mutant phenotype cited here (molina‐henares2010identificationofconditionally pages 7-9). |
| hisF | PP_0293 | Q88R41 | Imidazole glycerol phosphate synthase subunit HisF | biosynthesis | high | Canonical biosynthesis step 6 cyclase subunit. Direct KT2440 mutant evidence supports histidine auxotrophy (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7). |
| hisG | PP_0965 | Q88P87 | ATP phosphoribosyltransferase | biosynthesis | medium | First committed step (step 2). Expected catalytic subunit of short-form HisG/HisZ ATP-PRT. Not recovered in KT2440 auxotroph screen, but cluster context and conserved short-form system support assignment (molina‐henares2010identificationofconditionally pages 7-9, alphey2018catalyticandanticatalytic pages 1-5, read2021allostericinhibitionof pages 6-11). |
| hisD | PP_0966 | P59400 | Histidinol dehydrogenase | biosynthesis | medium | Canonical terminal biosynthesis step 10. Strong annotation and cluster context; not directly validated in KT2440 in the cited screen (molina‐henares2010identificationofconditionally pages 7-9). |
| hisC | PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase | biosynthesis | medium | Canonical step 8, but likely broad-substrate aminotransferase rather than strictly histidine-specific. BarSeq evidence indicates PP_0967 has broader aromatic/amino acid aminotransferase behavior, so annotate with caution (schmidt2022nitrogenmetabolismin pages 10-12). |
| PP_1721 | PP_1721 | Q88M53 | Phosphoserine phosphatase | other | low | Likely serine-pathway phosphatase rather than histidinol-phosphatase. No direct evidence linking to histidine biosynthesis in KT2440; probable KEGG over-assignment. |
| PP_3157 | PP_3157 | Q88I44 | Histidinol-phosphatase | ambiguous | medium | Plausible candidate for histidine biosynthesis step 9. Pseudomonads are expected to use a separate HAD-type HolPase/HisN-like enzyme, but direct KT2440 assignment remains unresolved between PP_3157 and PP_5147 (kulishorn2017sequencebasedidentificationof pages 1-2, kinateder2023evolutionaryanalysisand pages 1-9, ingle2011histidinebiosynthesis pages 4-5). |
| hisZ | PP_4890 | Q88DD7 | ATP phosphoribosyltransferase regulatory subunit | biosynthesis | high | Regulatory subunit of short-form ATP-PRT for step 2. Direct KT2440 mutant evidence supports histidine auxotrophy; should be retained as core biosynthesis component even though noncatalytic (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7, alphey2018catalyticandanticatalytic pages 1-5, read2021allostericinhibitionof pages 6-11). |
| PP_4983 | PP_4983 | Q88D45 | Tryptophan 2-monooxygenase | other | low | Not part of histidine metabolism; likely misplaced by broad map linkage. Should be removed from histidine curation set. |
| hisI | PP_5014 | Q88D15 | Phosphoribosyl-AMP cyclohydrolase | biosynthesis | medium | Canonical biosynthesis step 4. Strong pathway fit in the KT2440 hisIE cluster, but no direct mutant evidence cited here (molina‐henares2010identificationofconditionally pages 7-9). |
| hisE | PP_5015 | Q88D14 | Phosphoribosyl-ATP pyrophosphatase | biosynthesis | medium | Canonical biosynthesis step 3. Strong pathway fit in the KT2440 hisIE cluster, but no direct mutant evidence cited here (molina‐henares2010identificationofconditionally pages 7-9). |
| hutG | PP_5029 | Q88D00 | N-formylglutamate deformylase | catabolism-hut | high | Histidine utilization, not biosynthesis. Part of hut degradative branch converting FIG derivatives to glutamate/formate products; keep separate from biosynthetic module (bender2012regulationofthe pages 3-4). |
| hutI | PP_5030 | Q88CZ9 | Imidazolonepropionase | catabolism-hut | high | Histidine utilization enzyme in the hut pathway, downstream of urocanate. Catabolic, not biosynthetic (bender2012regulationofthe pages 2-3). |
| hutH | PP_5032 | Q88CZ7 | Histidine ammonia-lyase (histidase) | catabolism-hut | high | First committed histidine degradation enzyme generating urocanate. Definitively hut catabolism, not biosynthesis (bender2012regulationofthe pages 2-3). |
| hutU | PP_5033 | Q88CZ6 | Urocanate hydratase | catabolism-hut | high | Histidine utilization enzyme acting on urocanate. Catabolic, not biosynthetic (bender2012regulationofthe pages 10-11, bender2012regulationofthe pages 2-3). |
| hutF | PP_5036 | Q88CZ3 | Formimidoylglutamate deiminase | catabolism-hut | high | Hut pathway enzyme in histidine degradation. Should be excluded from de novo histidine biosynthesis module (bender2012regulationofthe pages 3-4). |
| PP_5147 | PP_5147 | Q88CN3 | Histidinol-phosphatase | ambiguous | medium | Second plausible candidate for biosynthesis step 9. Competes with PP_3157 for assignment; requires targeted review or experiment to distinguish true HolPase from over-annotation (kulishorn2017sequencebasedidentificationof pages 1-2, kinateder2023evolutionaryanalysisand pages 1-9, ingle2011histidinebiosynthesis pages 4-5). |


*Table: This table evaluates all 20 KEGG ppu00340 candidate genes for Pseudomonas putida KT2440 and separates true histidine biosynthesis genes from hut catabolic genes and likely over-annotations. It is useful for module satisfiability decisions and prioritizing genes for manual curation.*

### Detailed Assessment of Key Genes

**High-confidence biosynthetic genes (direct KT2440 evidence):**
- **hisB (PP_0289)**, **hisH (PP_0290)**, **hisF (PP_0293)**, **hisZ (PP_4890)**: All four were recovered as histidine auxotrophs in a genome-wide miniTn5 mutagenesis screen of KT2440 grown on M9 glucose minimal medium. Growth was restored by supplementation with L-histidine but not D-histidine (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7, molina‐henares2010identificationofconditionally pages 2-3).

**Medium-confidence biosynthetic genes (cluster context, no direct mutant phenotype reported):**
- **hisA (PP_0292)**, **hisG (PP_0965)**, **hisD (PP_0966)**, **hisI (PP_5014)**, **hisE (PP_5015)**: These were not recovered in the transposon screen, potentially because (a) mutants may accumulate toxic intermediates, (b) the screen was not saturating, or (c) intermediates may be supplied by cross-feeding in the library (molina‐henares2010identificationofconditionally pages 7-9). Their annotation is supported by sequence homology and genomic context.
- **hisC (PP_0967)**: Annotated as histidinol-phosphate aminotransferase (EC 2.6.1.9) but BarSeq fitness data from Schmidt et al. (2022) indicate broad substrate specificity including aromatic amino acid transamination. PP_0967 showed fitness defects across multiple nitrogen and amino acid conditions, not exclusively histidine-related, and has been used heterologously to catalyze phenylalanine deamination (schmidt2022nitrogenmetabolismin pages 10-12). Despite this promiscuity, its essentiality for histidine biosynthesis on minimal medium is supported by its genomic context in the hisGDC cluster.

**Candidate-uncertain: histidinol-phosphate phosphatase (step 9):**
- **PP_3157** and **PP_5147** are both annotated as histidinol-phosphatases (EC 3.1.3.15) in UniProt. In *P. aeruginosa*, the histidinol-phosphate phosphatase (HisN) has been confirmed as a HAD-type enzyme by AlphaFold structural prediction, with a distinct cap structure compared to the *E. coli* bifunctional HisB N-terminal domain (kinateder2023evolutionaryanalysisand pages 1-9). The Gammaproteobacteria generally use HAD-type (DDDD superfamily) HolPases, as distinct from the PHP-type found in Firmicutes/yeasts and the IMPase-like type found in Actinobacteria (kulishorn2017sequencebasedidentificationof pages 1-2, duca2021thehistidinebiosynthetic pages 6-8, ingle2011histidinebiosynthesis pages 4-5). Neither PP_3157 nor PP_5147 has been directly validated as the functional HolPase in KT2440.

**Genes to exclude from biosynthesis module:**
- **hutH (PP_5032)**, **hutU (PP_5033)**, **hutI (PP_5030)**, **hutF (PP_5036)**, **hutG (PP_5029)**: All belong to the histidine utilization (hut) catabolic pathway. In pseudomonads, histidine is degraded through a five-step pathway (histidase → urocanase → imidazolonepropionase → formimidoylglutamate deiminase → N-formylglutamate deformylase) to yield glutamate and formate (bender2012regulationofthe pages 10-11, bender2012regulationofthe pages 3-4, wirtz2021huttfunctionsas pages 1-2, bender2012regulationofthe pages 2-3). The hut genes are regulated by the repressor HutC (responsive to urocanate) and activated under nitrogen-limiting conditions via NtrBC and CbrAB (bender2012regulationofthe pages 10-11). HutT (PP_5031) functions as the major high-affinity L-histidine:proton symporter in KT2440 (wirtz2021huttfunctionsas pages 1-2).
- **gshA (PP_0243)**: Glutamate–cysteine ligase for glutathione biosynthesis. No connection to histidine metabolism.
- **PP_4983**: Tryptophan 2-monooxygenase. Belongs to tryptophan catabolism (KEGG ppu00350), not histidine metabolism.
- **PP_1721**: Annotated as phosphoserine phosphatase (EC 3.1.3.-). Likely involved in serine biosynthesis rather than histidine.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### Key Gap: Step 9 (histidinol-phosphate phosphatase)
The identity of the functional histidinol-phosphate phosphatase in KT2440 remains the principal gap. Two candidates exist (PP_3157, PP_5147), both annotated as EC 3.1.3.15. Based on the broader Pseudomonas lineage pattern (HAD-type HolPase confirmed in *P. aeruginosa*) (kinateder2023evolutionaryanalysisand pages 1-9), both are plausible. However, the presence of two paralogs raises the possibility of functional redundancy, which would explain why neither appeared in the Molina-Henares (2010) auxotroph screen (molina‐henares2010identificationofconditionally pages 7-9). Alternatively, one may represent a broader-specificity phosphatase recruited to histidine metabolism. Resolution requires: (i) individual and double gene deletions in KT2440, (ii) in vitro enzymatic characterization with histidinol-phosphate substrate, and/or (iii) structural comparison with the validated *P. aeruginosa* HisN.

### PP_0291: Uncharacterized ORF in the first his cluster
The first histidine biosynthetic cluster spans PP_0289–PP_0293 (hisB-hisH-PP_0291-hisA-hisF) (molina‐henares2010identificationofconditionally pages 7-9). PP_0291 is located between hisH and hisA and may encode an ORF of unknown or accessory function. It is not among the 20 candidate genes in the KEGG list and was not recovered as an auxotroph. Its role, if any, in histidine biosynthesis should be reviewed.

### Over-annotations in KEGG ppu00340
The KEGG "Histidine metabolism" map (ppu00340) conflates three distinct biological processes: de novo biosynthesis, histidine degradation (hut), and tangentially related reactions (glutathione biosynthesis, tryptophan oxidation). Three genes (gshA, PP_4983, PP_1721) have no meaningful connection to histidine metabolism and were likely included due to broad EC/reaction linkages in the KEGG overview map. The five hut genes belong to a separate catabolic module.

### HisC (PP_0967) promiscuity
HisC is annotated in the hisGDC biosynthetic cluster but the gene product has demonstrated broad aminotransferase activity beyond histidinol-phosphate. BarSeq data show that PP_0967 contributes to fitness across multiple amino acid conditions and has been used for heterologous phenylalanine-to-phenylpyruvate conversion (schmidt2022nitrogenmetabolismin pages 10-12). This promiscuity does not invalidate its role in histidine biosynthesis but suggests it should be annotated with broader GO terms (e.g., GO:0004400 for histidinol-phosphate transaminase activity, plus broader aminotransferase activity annotations).

## 6. Module and GO-Curation Recommendations

### Module Step Status Assignments

| Step | Status | Rationale |
|------|--------|-----------|
| 1 (PRPP supply) | **not_expected_in_module** | Shared precursor step; should be handled by a separate PRPP supply module |
| 2 (HisG + HisZ) | **covered** | Both subunits present; hisZ validated experimentally |
| 3 (HisE) | **covered** | Gene present in hisIE cluster |
| 4 (HisI) | **covered** | Gene present in hisIE cluster |
| 5 (HisA) | **covered** | Gene present in first his cluster |
| 6 (HisF + HisH) | **covered** | Both subunits validated experimentally |
| 7 (HisB) | **covered** | Validated experimentally; monofunctional dehydratase |
| 8 (HisC) | **covered** | Gene in hisGDC cluster; BarSeq confirms essential role in amino acid biosynthesis |
| 9 (HolPase) | **candidate_uncertain** | Two candidates (PP_3157, PP_5147); no direct validation |
| 10 (HisD) | **covered** | Gene in hisGDC cluster |

### Recommendations for Module Boundary Revision
1. **Separate biosynthesis from catabolism**: The current KEGG map ppu00340 should be split into two distinct modules for annotation purposes: (a) L-histidine de novo biosynthesis (steps 2–10) and (b) histidine utilization/hut catabolism (hutH → hutU → hutI → hutF → hutG).
2. **Remove non-histidine genes**: gshA, PP_4983, and PP_1721 should be excluded from the histidine module.
3. **Add hisZ to the biosynthesis module**: HisZ (PP_4890) is essential for the short-form ATP-PRT and must be included as a core component of step 2, not just a regulatory accessory.
4. **GO term request**: For PP_3157 and PP_5147, if validated as HAD-type HolPases, appropriate GO annotations should include GO:0004401 (histidinol-phosphatase activity) and, if applicable, GO:0000105 (histidine biosynthetic process).

## 7. Genes to Promote to Full Review

| Priority | Gene | Locus Tag | Rationale |
|----------|------|-----------|-----------|
| **High** | HolPase candidate 1 | PP_3157 | Unresolved step 9; requires experimental validation (deletion, in vitro assay) |
| **High** | HolPase candidate 2 | PP_5147 | Same as above; possible redundancy with PP_3157 |
| **Medium** | hisC | PP_0967 | Broad aminotransferase activity; may warrant revised GO terms |
| **Low** | PP_0291 | PP_0291 | Uncharacterized ORF in the first his cluster; role unclear |
| **Low** | hisG | PP_0965 | No direct KT2440 mutant phenotype reported; confirm short-form activity |

## 8. Key References

1. **Molina-Henares et al. (2010)** — Genome-wide mutant library screen identifying hisB, hisH, hisF, hisZ as conditionally essential for histidine prototrophy in *P. putida* KT2440. *Environmental Microbiology* 12:1468–1485. DOI: 10.1111/j.1462-2920.2010.02166.x (molina‐henares2010identificationofconditionally pages 7-9, molina‐henares2010identificationofconditionally pages 6-7, molina‐henares2010identificationofconditionally pages 2-3)

2. **Nelson et al. (2002)** — Complete genome sequence of *P. putida* KT2440. *Environmental Microbiology* 4(12):799–808. DOI: 10.1046/j.1462-2920.2002.00366.x

3. **Belda et al. (2016)** — Revisited genome annotation of KT2440 with 242 new genes and 1548 re-annotated genes. *Environmental Microbiology* 18(10):3403–3424. DOI: 10.1111/1462-2920.13230 (belda2016therevisitedgenome pages 4-5, belda2016therevisitedgenome pages 13-14, belda2016therevisitedgenome pages 1-2)

4. **Schmidt et al. (2022)** — Nitrogen metabolism RB-TnSeq fitness profiling; PP_0967 (hisC) functional data across 52 nitrogen conditions. *Applied and Environmental Microbiology* 88(7). DOI: 10.1128/aem.02430-21 (schmidt2022nitrogenmetabolismin pages 10-12)

5. **Wirtz et al. (2021)** — HutT as the major L-histidine transporter in KT2440. *FEBS Letters* 595:2113–2126. DOI: 10.1002/1873-3468.14159 (wirtz2021huttfunctionsas pages 1-2)

6. **Wirtz et al. (2020)** — CbrA as a L-histidine transporter and sensor kinase in KT2440. *Scientific Reports* 10. DOI: 10.1038/s41598-020-62337-9

7. **Bender (2012)** — Comprehensive review of hut system regulation in bacteria, including *Pseudomonas*. *Microbiology and Molecular Biology Reviews* 76:565–584. DOI: 10.1128/mmbr.00014-12 (bender2012regulationofthe pages 10-11, bender2012regulationofthe pages 3-4, bender2012regulationofthe pages 2-3)

8. **Kulis-Horn et al. (2014)** — Histidine biosynthesis in *C. glutamicum*; describes IMPase-like HisN and comparison with HAD/PHP-type HolPases. *Microbial Biotechnology* 7:5–25. DOI: 10.1111/1751-7915.12055 (kulis‐horn2014histidinebiosynthesisits pages 7-9, kulis‐horn2014histidinebiosynthesisits pages 6-7, kulis‐horn2014histidinebiosynthesisits pages 4-5, kulis‐horn2014histidinebiosynthesisits pages 13-14)

9. **Kulis-Horn et al. (2017)** — Sequence-based identification of IMPase-like HolPases; HAD-type predominance in Gammaproteobacteria. *BMC Microbiology* 17. DOI: 10.1186/s12866-017-1069-4 (kulishorn2017sequencebasedidentificationof pages 1-2, kulishorn2017sequencebasedidentificationof pages 15-16)

10. **Kinateder (2023)** — Evolutionary analysis of HolPases; confirms HAD-type HisN in *P. aeruginosa* by AlphaFold. DOI: 10.5283/epub.54797 (kinateder2023evolutionaryanalysisand pages 1-9)

11. **Alphey et al. (2018)** — Structural characterization of short-form ATP-PRT catalytic and anticatalytic states. *ACS Catalysis* 8:5601–5610. DOI: 10.1021/acscatal.8b00867 (alphey2018catalyticandanticatalytic pages 1-5, alphey2018catalyticandanticatalytic pages 22-26, alphey2018catalyticandanticatalytic pages 15-19)

12. **Khajeaian (2022)** — Thesis on ATP-PRT evolution and function including short-form HisG/HisZ architecture. DOI: 10.26686/wgtn.19709419 (khajeaian2022exploringtheevolution pages 82-85, khajeaian2022exploringtheevolution pages 192-194, khajeaian2022exploringtheevolution pages 95-100, khajeaian2022exploringtheevolution pages 25-32)

13. **Borchert et al. (2024)** — Machine learning analysis of RB-TnSeq fitness data in KT2440 identifying functional gene modules. *mSystems* 9(3). DOI: 10.1128/msystems.00942-23

14. **Nogales et al. (2008)** — Genome-scale metabolic reconstruction of KT2440 (iJN746). *BMC Systems Biology* 2:79. DOI: 10.1186/1752-0509-2-79

### Summary of Evidence Strength

| Evidence Category | Source Organism | Strength |
|---|---|---|
| Transposon mutagenesis auxotrophy (hisB, hisH, hisF, hisZ) | *P. putida* KT2440 | **Direct, strong** |
| RB-TnSeq/BarSeq fitness profiling (hisC/PP_0967 and others) | *P. putida* KT2440 | **Direct, medium** |
| Genome annotation and cluster context (hisG, hisD, hisA, hisI, hisE) | *P. putida* KT2440 | **Annotation-based, medium** |
| HisG/HisZ short-form architecture and kinetics | *Psychrobacter arcticus*, *A. baumannii*, *L. lactis* | **Homology transfer, strong** |
| HAD-type HolPase identity for Pseudomonas | *P. aeruginosa* (AlphaFold) | **Homology transfer, moderate** |
| Hut pathway enzymology and regulation | *P. putida*, *P. fluorescens*, *Klebsiella* | **Cross-species, strong** |
| HolPase enzyme family classification | *E. coli*, *C. glutamicum*, *B. subtilis* | **Comparative genomics, strong** |

The principal open question for this module is the unambiguous identification of the step 9 histidinol-phosphate phosphatase. Targeted gene deletion of PP_3157 and PP_5147 (individually and in combination) on minimal medium, coupled with in vitro enzymatic characterization using histidinol-phosphate as substrate, would definitively resolve this gap.

References

1. (molina‐henares2010identificationofconditionally pages 7-9): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

2. (molina‐henares2010identificationofconditionally pages 2-3): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

3. (kulishorn2017sequencebasedidentificationof pages 1-2): Robert Kasimir Kulis-Horn, Christian Rückert, Jörn Kalinowski, and Marcus Persicke. Sequence-based identification of inositol monophosphatase-like histidinol-phosphate phosphatases (hisn) in corynebacterium glutamicum, actinobacteria, and beyond. BMC Microbiology, Jul 2017. URL: https://doi.org/10.1186/s12866-017-1069-4, doi:10.1186/s12866-017-1069-4. This article has 11 citations and is from a peer-reviewed journal.

4. (kinateder2023evolutionaryanalysisand pages 1-9): Thomas Kinateder. Evolutionary analysis and functional characterization of different histidinol phosphate phosphatases. Text, Jan 2023. URL: https://doi.org/10.5283/epub.54797, doi:10.5283/epub.54797. This article has 0 citations and is from a peer-reviewed journal.

5. (molina‐henares2010identificationofconditionally pages 6-7): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

6. (bender2012regulationofthe pages 10-11): Robert A. Bender. Regulation of the histidine utilization (hut) system in bacteria. Microbiology and Molecular Biology Reviews, 76:565-584, Sep 2012. URL: https://doi.org/10.1128/mmbr.00014-12, doi:10.1128/mmbr.00014-12. This article has 198 citations and is from a domain leading peer-reviewed journal.

7. (bender2012regulationofthe pages 3-4): Robert A. Bender. Regulation of the histidine utilization (hut) system in bacteria. Microbiology and Molecular Biology Reviews, 76:565-584, Sep 2012. URL: https://doi.org/10.1128/mmbr.00014-12, doi:10.1128/mmbr.00014-12. This article has 198 citations and is from a domain leading peer-reviewed journal.

8. (wirtz2021huttfunctionsas pages 1-2): Larissa Wirtz, Michelle Eder, Anna‐Katharina Brand, and Heinrich Jung. Hutt functions as the major l‐histidine transporter in <i>pseudomonas putida</i> kt2440. Jul 2021. URL: https://doi.org/10.1002/1873-3468.14159, doi:10.1002/1873-3468.14159. This article has 11 citations and is from a peer-reviewed journal.

9. (bender2012regulationofthe pages 2-3): Robert A. Bender. Regulation of the histidine utilization (hut) system in bacteria. Microbiology and Molecular Biology Reviews, 76:565-584, Sep 2012. URL: https://doi.org/10.1128/mmbr.00014-12, doi:10.1128/mmbr.00014-12. This article has 198 citations and is from a domain leading peer-reviewed journal.

10. (kulis‐horn2014histidinebiosynthesisits pages 4-5): Robert K. Kulis‐Horn, Marcus Persicke, and Jörn Kalinowski. Histidine biosynthesis, its regulation and biotechnological application in corynebacterium glutamicum. Microbial Biotechnology, 7:5-25, Apr 2014. URL: https://doi.org/10.1111/1751-7915.12055, doi:10.1111/1751-7915.12055. This article has 157 citations and is from a peer-reviewed journal.

11. (alphey2018catalyticandanticatalytic pages 1-5): Magnus S. Alphey, Gemma Fisher, Ying Ge, Eoin R. Gould, Teresa F. G. Machado, Huanting Liu, Gordon J. Florence, James H. Naismith, and Rafael G. da Silva. Catalytic and anticatalytic snapshots of a short-form atp phosphoribosyltransferase. ACS Catalysis, 8:5601-5610, May 2018. URL: https://doi.org/10.1021/acscatal.8b00867, doi:10.1021/acscatal.8b00867. This article has 19 citations and is from a highest quality peer-reviewed journal.

12. (read2021allostericinhibitionof pages 6-11): Benjamin J. Read, Gemma Fisher, Oliver L. R. Wissett, Teresa F. G. Machado, John Nicholson, John B. O. Mitchell, and Rafael G. da Silva. Allosteric inhibition of acinetobacter baumannii atp phosphoribosyltransferase by protein:dipeptide and protein:protein interactions. ACS infectious diseases, 8:197-209, Dec 2021. URL: https://doi.org/10.1021/acsinfecdis.1c00539, doi:10.1021/acsinfecdis.1c00539. This article has 7 citations and is from a peer-reviewed journal.

13. (kulis‐horn2014histidinebiosynthesisits pages 6-7): Robert K. Kulis‐Horn, Marcus Persicke, and Jörn Kalinowski. Histidine biosynthesis, its regulation and biotechnological application in corynebacterium glutamicum. Microbial Biotechnology, 7:5-25, Apr 2014. URL: https://doi.org/10.1111/1751-7915.12055, doi:10.1111/1751-7915.12055. This article has 157 citations and is from a peer-reviewed journal.

14. (schmidt2022nitrogenmetabolismin pages 10-12): Matthias Schmidt, Allison N. Pearson, Matthew R. Incha, Mitchell G. Thompson, Edward E. K. Baidoo, Ramu Kakumanu, Aindrila Mukhopadhyay, Patrick M. Shih, Adam M. Deutschbauer, Lars M. Blank, and Jay D. Keasling. Nitrogen metabolism in pseudomonas putida: functional analysis using random barcode transposon sequencing. Applied and Environmental Microbiology, Apr 2022. URL: https://doi.org/10.1128/aem.02430-21, doi:10.1128/aem.02430-21. This article has 36 citations and is from a peer-reviewed journal.

15. (ingle2011histidinebiosynthesis pages 4-5): Robert A. Ingle. Histidine biosynthesis. The Arabidopsis Book, 2011:e0141, Jan 2011. URL: https://doi.org/10.1199/tab.0141, doi:10.1199/tab.0141. This article has 142 citations and is from a peer-reviewed journal.

16. (khajeaian2022exploringtheevolution pages 25-32): Parastoo Khajeaian. Exploring the evolution and function of the first enzyme in histidine biosynthesis. ArXiv, 2022. URL: https://doi.org/10.26686/wgtn.19709419, doi:10.26686/wgtn.19709419. This article has 1 citations.

17. (khajeaian2022exploringtheevolution pages 82-85): Parastoo Khajeaian. Exploring the evolution and function of the first enzyme in histidine biosynthesis. ArXiv, 2022. URL: https://doi.org/10.26686/wgtn.19709419, doi:10.26686/wgtn.19709419. This article has 1 citations.

18. (khajeaian2022exploringtheevolution pages 95-100): Parastoo Khajeaian. Exploring the evolution and function of the first enzyme in histidine biosynthesis. ArXiv, 2022. URL: https://doi.org/10.26686/wgtn.19709419, doi:10.26686/wgtn.19709419. This article has 1 citations.

19. (kulis‐horn2014histidinebiosynthesisits pages 7-9): Robert K. Kulis‐Horn, Marcus Persicke, and Jörn Kalinowski. Histidine biosynthesis, its regulation and biotechnological application in corynebacterium glutamicum. Microbial Biotechnology, 7:5-25, Apr 2014. URL: https://doi.org/10.1111/1751-7915.12055, doi:10.1111/1751-7915.12055. This article has 157 citations and is from a peer-reviewed journal.

20. (kulis‐horn2014histidinebiosynthesisits pages 9-11): Robert K. Kulis‐Horn, Marcus Persicke, and Jörn Kalinowski. Histidine biosynthesis, its regulation and biotechnological application in corynebacterium glutamicum. Microbial Biotechnology, 7:5-25, Apr 2014. URL: https://doi.org/10.1111/1751-7915.12055, doi:10.1111/1751-7915.12055. This article has 157 citations and is from a peer-reviewed journal.

21. (duca2021thehistidinebiosynthetic pages 6-8): Sara Del Duca, Christopher Riccardi, Alberto Vassallo, Giulia Fontana, Lara Mitia Castronovo, Sofia Chioccioli, and Renato Fani. The histidine biosynthetic genes in the superphylum bacteroidota-rhodothermota-balneolota-chlorobiota: insights into the evolution of gene structure and organization. Microorganisms, 9:1439, Jul 2021. URL: https://doi.org/10.3390/microorganisms9071439, doi:10.3390/microorganisms9071439. This article has 8 citations.

22. (belda2016therevisitedgenome pages 4-5): Eugeni Belda, Ruben G. A. van Heck, Maria José Lopez‐Sanchez, Stéphane Cruveiller, Valérie Barbe, Claire Fraser, Hans‐Peter Klenk, Jörn Petersen, Anne Morgat, Pablo I. Nikel, David Vallenet, Zoé Rouy, Agnieszka Sekowska, Vitor A. P. Martins dos Santos, Víctor de Lorenzo, Antoine Danchin, and Claudine Médigue. The revisited genome of pseudomonas putida kt2440 enlightens its value as a robust metabolic chassis. Environmental microbiology, 18 10:3403-3424, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13230, doi:10.1111/1462-2920.13230. This article has 375 citations and is from a domain leading peer-reviewed journal.

23. (belda2016therevisitedgenome pages 13-14): Eugeni Belda, Ruben G. A. van Heck, Maria José Lopez‐Sanchez, Stéphane Cruveiller, Valérie Barbe, Claire Fraser, Hans‐Peter Klenk, Jörn Petersen, Anne Morgat, Pablo I. Nikel, David Vallenet, Zoé Rouy, Agnieszka Sekowska, Vitor A. P. Martins dos Santos, Víctor de Lorenzo, Antoine Danchin, and Claudine Médigue. The revisited genome of pseudomonas putida kt2440 enlightens its value as a robust metabolic chassis. Environmental microbiology, 18 10:3403-3424, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13230, doi:10.1111/1462-2920.13230. This article has 375 citations and is from a domain leading peer-reviewed journal.

24. (belda2016therevisitedgenome pages 1-2): Eugeni Belda, Ruben G. A. van Heck, Maria José Lopez‐Sanchez, Stéphane Cruveiller, Valérie Barbe, Claire Fraser, Hans‐Peter Klenk, Jörn Petersen, Anne Morgat, Pablo I. Nikel, David Vallenet, Zoé Rouy, Agnieszka Sekowska, Vitor A. P. Martins dos Santos, Víctor de Lorenzo, Antoine Danchin, and Claudine Médigue. The revisited genome of pseudomonas putida kt2440 enlightens its value as a robust metabolic chassis. Environmental microbiology, 18 10:3403-3424, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13230, doi:10.1111/1462-2920.13230. This article has 375 citations and is from a domain leading peer-reviewed journal.

25. (kulis‐horn2014histidinebiosynthesisits pages 13-14): Robert K. Kulis‐Horn, Marcus Persicke, and Jörn Kalinowski. Histidine biosynthesis, its regulation and biotechnological application in corynebacterium glutamicum. Microbial Biotechnology, 7:5-25, Apr 2014. URL: https://doi.org/10.1111/1751-7915.12055, doi:10.1111/1751-7915.12055. This article has 157 citations and is from a peer-reviewed journal.

26. (kulishorn2017sequencebasedidentificationof pages 15-16): Robert Kasimir Kulis-Horn, Christian Rückert, Jörn Kalinowski, and Marcus Persicke. Sequence-based identification of inositol monophosphatase-like histidinol-phosphate phosphatases (hisn) in corynebacterium glutamicum, actinobacteria, and beyond. BMC Microbiology, Jul 2017. URL: https://doi.org/10.1186/s12866-017-1069-4, doi:10.1186/s12866-017-1069-4. This article has 11 citations and is from a peer-reviewed journal.

27. (alphey2018catalyticandanticatalytic pages 22-26): Magnus S. Alphey, Gemma Fisher, Ying Ge, Eoin R. Gould, Teresa F. G. Machado, Huanting Liu, Gordon J. Florence, James H. Naismith, and Rafael G. da Silva. Catalytic and anticatalytic snapshots of a short-form atp phosphoribosyltransferase. ACS Catalysis, 8:5601-5610, May 2018. URL: https://doi.org/10.1021/acscatal.8b00867, doi:10.1021/acscatal.8b00867. This article has 19 citations and is from a highest quality peer-reviewed journal.

28. (alphey2018catalyticandanticatalytic pages 15-19): Magnus S. Alphey, Gemma Fisher, Ying Ge, Eoin R. Gould, Teresa F. G. Machado, Huanting Liu, Gordon J. Florence, James H. Naismith, and Rafael G. da Silva. Catalytic and anticatalytic snapshots of a short-form atp phosphoribosyltransferase. ACS Catalysis, 8:5601-5610, May 2018. URL: https://doi.org/10.1021/acscatal.8b00867, doi:10.1021/acscatal.8b00867. This article has 19 citations and is from a highest quality peer-reviewed journal.

29. (khajeaian2022exploringtheevolution pages 192-194): Parastoo Khajeaian. Exploring the evolution and function of the first enzyme in histidine biosynthesis. ArXiv, 2022. URL: https://doi.org/10.26686/wgtn.19709419, doi:10.26686/wgtn.19709419. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](PSEPK__histidine_biosynthesis__ppu00340-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__histidine_biosynthesis__ppu00340-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. schmidt2022nitrogenmetabolismin pages 10-12
2. khajeaian2022exploringtheevolution pages 25-32
3. bender2012regulationofthe pages 3-4
4. bender2012regulationofthe pages 2-3
5. kinateder2023evolutionaryanalysisand pages 1-9
6. bender2012regulationofthe pages 10-11
7. wirtz2021huttfunctionsas pages 1-2
8. kulishorn2017sequencebasedidentificationof pages 1-2
9. alphey2018catalyticandanticatalytic pages 1-5
10. read2021allostericinhibitionof pages 6-11
11. ingle2011histidinebiosynthesis pages 4-5
12. khajeaian2022exploringtheevolution pages 82-85
13. khajeaian2022exploringtheevolution pages 95-100
14. duca2021thehistidinebiosynthetic pages 6-8
15. belda2016therevisitedgenome pages 4-5
16. belda2016therevisitedgenome pages 13-14
17. belda2016therevisitedgenome pages 1-2
18. kulishorn2017sequencebasedidentificationof pages 15-16
19. alphey2018catalyticandanticatalytic pages 22-26
20. alphey2018catalyticandanticatalytic pages 15-19
21. khajeaian2022exploringtheevolution pages 192-194
22. (5-phosphoribosylamino)methylideneamino
23. s
24. https://doi.org/10.1111/j.1462-2920.2010.02166.x,
25. https://doi.org/10.1186/s12866-017-1069-4,
26. https://doi.org/10.5283/epub.54797,
27. https://doi.org/10.1128/mmbr.00014-12,
28. https://doi.org/10.1002/1873-3468.14159,
29. https://doi.org/10.1111/1751-7915.12055,
30. https://doi.org/10.1021/acscatal.8b00867,
31. https://doi.org/10.1021/acsinfecdis.1c00539,
32. https://doi.org/10.1128/aem.02430-21,
33. https://doi.org/10.1199/tab.0141,
34. https://doi.org/10.26686/wgtn.19709419,
35. https://doi.org/10.3390/microorganisms9071439,
36. https://doi.org/10.1111/1462-2920.13230,