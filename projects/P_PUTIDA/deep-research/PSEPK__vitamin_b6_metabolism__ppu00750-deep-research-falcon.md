---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T03:24:05.557825'
end_time: '2026-07-07T03:47:31.303971'
duration_seconds: 1405.75
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Vitamin B6 metabolism
  module_summary: A bacterial vitamin B6 metabolism module covering DXP-dependent
    de novo formation of pyridoxine 5'-phosphate, oxidation to pyridoxal 5'-phosphate,
    and salvage phosphorylation of B6 vitamers. In Pseudomonas putida KT2440, KEGG
    ppu00750 also includes shared precursor and amino-acid-metabolism nodes; those
    are treated as boundary context unless they directly make or salvage pyridoxal
    5'-phosphate.
  module_outline: "- Vitamin B6 metabolism\n  - 1. de novo pyridoxine 5'-phosphate\
    \ formation\n  - De novo pyridoxine phosphate formation\n    - PdxA 4-hydroxythreonine-4-phosphate\
    \ dehydrogenase (molecular player: PSEPK pdxA; activity or role: 4-hydroxythreonine-4-phosphate\
    \ dehydrogenase activity)\n    - PdxB 4-phosphoerythronate dehydrogenase (molecular\
    \ player: PSEPK pdxB; activity or role: 4-phosphoerythronate dehydrogenase activity)\n\
    \    - PdxJ pyridoxine 5'-phosphate synthase (molecular player: PSEPK pdxJ; activity\
    \ or role: pyridoxine 5'-phosphate synthase activity)\n  - 2. pyridoxal 5'-phosphate\
    \ formation\n  - Pyridoxine phosphate oxidation\n    - PdxH pyridoxamine phosphate\
    \ oxidase (molecular player: PSEPK pdxH; activity or role: pyridoxamine phosphate\
    \ oxidase activity)\n  - 3. vitamin B6 salvage phosphorylation\n  - Vitamin B6\
    \ salvage phosphorylation\n    - PdxY pyridoxal kinase (molecular player: PSEPK\
    \ pdxY; activity or role: pyridoxal kinase activity)\n  - 4. precursor and amino-acid\
    \ side context\n  - Precursor-side and PLP-enzyme context\n    - Epd erythrose-4-phosphate\
    \ dehydrogenase (molecular player: PSEPK epd; activity or role: erythrose-4-phosphate\
    \ dehydrogenase activity)\n    - SerC phosphoserine aminotransferase (molecular\
    \ player: PSEPK serC; activity or role: O-phospho-L-serine:2-oxoglutarate transaminase\
    \ activity)\n    - ThrC threonine synthase (molecular player: PSEPK thrC; activity\
    \ or role: threonine synthase activity)\n    - PP_0662 threonine synthase candidate\
    \ (molecular player: PSEPK PP_0662; activity or role: threonine synthase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00750
  pathway_id: ppu00750
  pathway_name: Vitamin B6 metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00750 with 9 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '9'
  candidate_genes: '- pdxA: PP_0402 | Q88QT5 | 4-hydroxythreonine-4-phosphate dehydrogenase
    (EC 1.1.1.262) (4-(phosphohydroxy)-L-threonine dehydrogenase) (EC 1.1.1.262; primary
    bucket kegg:ppu00750)

    - PP_0662: PP_0662 | Q88Q36 | Threonine synthase (primary bucket kegg:ppu00750)

    - pdxH: PP_1129 | Q88NS5 | Pyridoxine/pyridoxamine 5''-phosphate oxidase (EC 1.4.3.5)
    (PNP/PMP oxidase) (PNPOx) (Pyridoxal 5''-phosphate synthase) (EC 1.4.3.5; primary
    bucket kegg:ppu00750)

    - pdxJ: PP_1436 | Q88MY2 | Pyridoxine 5''-phosphate synthase (PNP synthase) (EC
    2.6.99.2) (EC 2.6.99.2; primary bucket kegg:ppu00750)

    - thrC: PP_1471 | Q88MU7 | Threonine synthase (EC 4.2.3.1) (EC 4.2.3.1; primary
    bucket kegg:ppu00750)

    - serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine
    aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)

    - pdxB: PP_2117 | Q88L20 | Erythronate-4-phosphate dehydrogenase (EC 1.1.1.290)
    (EC 1.1.1.290; primary bucket kegg:ppu00750)

    - epd: PP_4964 | Q88D63 | Erythrose-4-phosphate dehydrogenase (EC 1.2.1.72) (EC
    1.2.1.72; primary bucket kegg:ppu00750)

    - pdxY: PP_5357 | Q88C26 | Pyridoxal kinase PdxY (PL kinase) (EC 2.7.1.35) (EC
    2.7.1.35; primary bucket kegg:ppu00750)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__vitamin_b6_metabolism__ppu00750-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__vitamin_b6_metabolism__ppu00750-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Vitamin B6 metabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00750
- Resolved ID: ppu00750
- Resolved name: Vitamin B6 metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00750 with 9 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 9

- pdxA: PP_0402 | Q88QT5 | 4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262) (4-(phosphohydroxy)-L-threonine dehydrogenase) (EC 1.1.1.262; primary bucket kegg:ppu00750)
- PP_0662: PP_0662 | Q88Q36 | Threonine synthase (primary bucket kegg:ppu00750)
- pdxH: PP_1129 | Q88NS5 | Pyridoxine/pyridoxamine 5'-phosphate oxidase (EC 1.4.3.5) (PNP/PMP oxidase) (PNPOx) (Pyridoxal 5'-phosphate synthase) (EC 1.4.3.5; primary bucket kegg:ppu00750)
- pdxJ: PP_1436 | Q88MY2 | Pyridoxine 5'-phosphate synthase (PNP synthase) (EC 2.6.99.2) (EC 2.6.99.2; primary bucket kegg:ppu00750)
- thrC: PP_1471 | Q88MU7 | Threonine synthase (EC 4.2.3.1) (EC 4.2.3.1; primary bucket kegg:ppu00750)
- serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)
- pdxB: PP_2117 | Q88L20 | Erythronate-4-phosphate dehydrogenase (EC 1.1.1.290) (EC 1.1.1.290; primary bucket kegg:ppu00750)
- epd: PP_4964 | Q88D63 | Erythrose-4-phosphate dehydrogenase (EC 1.2.1.72) (EC 1.2.1.72; primary bucket kegg:ppu00750)
- pdxY: PP_5357 | Q88C26 | Pyridoxal kinase PdxY (PL kinase) (EC 2.7.1.35) (EC 2.7.1.35; primary bucket kegg:ppu00750)

## Generic Module Context

### Working Scope

A bacterial vitamin B6 metabolism module covering DXP-dependent de novo formation of pyridoxine 5'-phosphate, oxidation to pyridoxal 5'-phosphate, and salvage phosphorylation of B6 vitamers. In Pseudomonas putida KT2440, KEGG ppu00750 also includes shared precursor and amino-acid-metabolism nodes; those are treated as boundary context unless they directly make or salvage pyridoxal 5'-phosphate.

### Provisional Biological Outline

- Vitamin B6 metabolism
  - 1. de novo pyridoxine 5'-phosphate formation
  - De novo pyridoxine phosphate formation
    - PdxA 4-hydroxythreonine-4-phosphate dehydrogenase (molecular player: PSEPK pdxA; activity or role: 4-hydroxythreonine-4-phosphate dehydrogenase activity)
    - PdxB 4-phosphoerythronate dehydrogenase (molecular player: PSEPK pdxB; activity or role: 4-phosphoerythronate dehydrogenase activity)
    - PdxJ pyridoxine 5'-phosphate synthase (molecular player: PSEPK pdxJ; activity or role: pyridoxine 5'-phosphate synthase activity)
  - 2. pyridoxal 5'-phosphate formation
  - Pyridoxine phosphate oxidation
    - PdxH pyridoxamine phosphate oxidase (molecular player: PSEPK pdxH; activity or role: pyridoxamine phosphate oxidase activity)
  - 3. vitamin B6 salvage phosphorylation
  - Vitamin B6 salvage phosphorylation
    - PdxY pyridoxal kinase (molecular player: PSEPK pdxY; activity or role: pyridoxal kinase activity)
  - 4. precursor and amino-acid side context
  - Precursor-side and PLP-enzyme context
    - Epd erythrose-4-phosphate dehydrogenase (molecular player: PSEPK epd; activity or role: erythrose-4-phosphate dehydrogenase activity)
    - SerC phosphoserine aminotransferase (molecular player: PSEPK serC; activity or role: O-phospho-L-serine:2-oxoglutarate transaminase activity)
    - ThrC threonine synthase (molecular player: PSEPK thrC; activity or role: threonine synthase activity)
    - PP_0662 threonine synthase candidate (molecular player: PSEPK PP_0662; activity or role: threonine synthase activity)

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

Vitamin B6 metabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00750
- Resolved ID: ppu00750
- Resolved name: Vitamin B6 metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00750 with 9 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 9

- pdxA: PP_0402 | Q88QT5 | 4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262) (4-(phosphohydroxy)-L-threonine dehydrogenase) (EC 1.1.1.262; primary bucket kegg:ppu00750)
- PP_0662: PP_0662 | Q88Q36 | Threonine synthase (primary bucket kegg:ppu00750)
- pdxH: PP_1129 | Q88NS5 | Pyridoxine/pyridoxamine 5'-phosphate oxidase (EC 1.4.3.5) (PNP/PMP oxidase) (PNPOx) (Pyridoxal 5'-phosphate synthase) (EC 1.4.3.5; primary bucket kegg:ppu00750)
- pdxJ: PP_1436 | Q88MY2 | Pyridoxine 5'-phosphate synthase (PNP synthase) (EC 2.6.99.2) (EC 2.6.99.2; primary bucket kegg:ppu00750)
- thrC: PP_1471 | Q88MU7 | Threonine synthase (EC 4.2.3.1) (EC 4.2.3.1; primary bucket kegg:ppu00750)
- serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)
- pdxB: PP_2117 | Q88L20 | Erythronate-4-phosphate dehydrogenase (EC 1.1.1.290) (EC 1.1.1.290; primary bucket kegg:ppu00750)
- epd: PP_4964 | Q88D63 | Erythrose-4-phosphate dehydrogenase (EC 1.2.1.72) (EC 1.2.1.72; primary bucket kegg:ppu00750)
- pdxY: PP_5357 | Q88C26 | Pyridoxal kinase PdxY (PL kinase) (EC 2.7.1.35) (EC 2.7.1.35; primary bucket kegg:ppu00750)

## Generic Module Context

### Working Scope

A bacterial vitamin B6 metabolism module covering DXP-dependent de novo formation of pyridoxine 5'-phosphate, oxidation to pyridoxal 5'-phosphate, and salvage phosphorylation of B6 vitamers. In Pseudomonas putida KT2440, KEGG ppu00750 also includes shared precursor and amino-acid-metabolism nodes; those are treated as boundary context unless they directly make or salvage pyridoxal 5'-phosphate.

### Provisional Biological Outline

- Vitamin B6 metabolism
  - 1. de novo pyridoxine 5'-phosphate formation
  - De novo pyridoxine phosphate formation
    - PdxA 4-hydroxythreonine-4-phosphate dehydrogenase (molecular player: PSEPK pdxA; activity or role: 4-hydroxythreonine-4-phosphate dehydrogenase activity)
    - PdxB 4-phosphoerythronate dehydrogenase (molecular player: PSEPK pdxB; activity or role: 4-phosphoerythronate dehydrogenase activity)
    - PdxJ pyridoxine 5'-phosphate synthase (molecular player: PSEPK pdxJ; activity or role: pyridoxine 5'-phosphate synthase activity)
  - 2. pyridoxal 5'-phosphate formation
  - Pyridoxine phosphate oxidation
    - PdxH pyridoxamine phosphate oxidase (molecular player: PSEPK pdxH; activity or role: pyridoxamine phosphate oxidase activity)
  - 3. vitamin B6 salvage phosphorylation
  - Vitamin B6 salvage phosphorylation
    - PdxY pyridoxal kinase (molecular player: PSEPK pdxY; activity or role: pyridoxal kinase activity)
  - 4. precursor and amino-acid side context
  - Precursor-side and PLP-enzyme context
    - Epd erythrose-4-phosphate dehydrogenase (molecular player: PSEPK epd; activity or role: erythrose-4-phosphate dehydrogenase activity)
    - SerC phosphoserine aminotransferase (molecular player: PSEPK serC; activity or role: O-phospho-L-serine:2-oxoglutarate transaminase activity)
    - ThrC threonine synthase (molecular player: PSEPK thrC; activity or role: threonine synthase activity)
    - PP_0662 threonine synthase candidate (molecular player: PSEPK PP_0662; activity or role: threonine synthase activity)

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

# Vitamin B6 Metabolism in *Pseudomonas putida* KT2440: Module/Pathway Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 (NCBI TaxID 160488; proteome UP000000556) employs the DXP-dependent (DXP-D) de novo pathway for pyridoxal 5′-phosphate (PLP) biosynthesis, consistent with its phylogenetic position as a diderm Gammaproteobacterium (denise2023pyridoxal5’phosphatesynthesis pages 6-9, denise2023pyridoxal5’phosphatesynthesis pages 4-6). The KEGG pathway ppu00750 assigns nine candidate genes to this module. Of these, six (epd, pdxB, serC, pdxA, pdxJ, pdxH) represent core de novo PLP biosynthesis steps with high-confidence orthology-based assignments supported by extensive biochemical characterization in *Escherichia coli* (denise2023pyridoxal5’phosphatesynthesis pages 1-3, tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 7-10). One gene (pdxY) covers the vitamin B6 salvage phosphorylation step with medium-high confidence (tramonti2021knownsandunknowns pages 12-13, yang1998identificationandfunction pages 5-7). Two genes (thrC/PP_1471 and PP_0662) represent threonine synthase activities that are boundary/precursor context rather than committed PLP biosynthesis enzymes and likely represent map-context over-propagation. Notably, the DXP-supplying enzyme Dxs and a broader-substrate salvage kinase PdxK are absent from the candidate list but are expected to be present in the KT2440 genome. No direct biochemical studies of vitamin B6 metabolism specific to *P. putida* KT2440 were identified; all gene assignments rest on homology transfer from model Gammaproteobacteria, primarily *E. coli*, which is a strong but not experimentally validated basis in this organism.

## 2. Target-Organism Pathway Definition

### 2.1 Pathway Boundaries

The vitamin B6 metabolism module (KEGG ppu00750) encompasses three functional blocks:

**De novo DXP-dependent PLP biosynthesis.** This pathway converts erythrose-4-phosphate (from the pentose phosphate pathway) and 1-deoxyxylulose-5-phosphate (DXP, from condensation of pyruvate and glyceraldehyde-3-phosphate) into pyridoxine 5′-phosphate (PNP), which is then oxidized to pyridoxal 5′-phosphate (PLP) (tramonti2021knownsandunknowns pages 4-5, tramonti2021knownsandunknowns pages 10-12, tramonti2021knownsandunknowns pages 5-7). The DXP-dependent route is one of two known bacterial PLP synthesis pathways; the alternative DXP-independent pathway (found mainly in monoderm bacteria) uses PLP synthase (Pdx1/Pdx2) to directly produce PLP from ribose 5-phosphate, glyceraldehyde 3-phosphate, and glutamine (denise2023pyridoxal5’phosphatesynthesis pages 6-9, denise2023pyridoxal5’phosphatesynthesis pages 4-6). The DXP-D pathway is found almost exclusively in Gracilicutes (Gram-negative bacteria) and correlates with diderm cell envelope structure (denise2023pyridoxal5’phosphatesynthesis pages 6-9).

**PLP salvage.** Exogenous or recycled B6 vitamers (pyridoxal, pyridoxamine, pyridoxine) are phosphorylated by kinases (PdxK, PdxY) and interconverted by PdxH (PNP/PMP oxidase) to regenerate PLP (tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 4-5).

**Boundary context.** KEGG ppu00750 also includes threonine synthase (ThrC) and a second threonine synthase candidate (PP_0662), which provide precursors (4-phospho-hydroxy-L-threonine derives from threonine-pathway intermediates) but are not committed PLP biosynthesis enzymes. SerC is a bona fide dual-function enzyme shared between serine biosynthesis and PLP biosynthesis (tramonti2021knownsandunknowns pages 12-13).

### 2.2 Neighboring Pathways to Keep Separate

- **Isoprenoid biosynthesis (MEP/DOXP pathway):** Shares DXP as a substrate via Dxs; should remain in terpenoid backbone biosynthesis modules.
- **Thiamine biosynthesis:** Also uses DXP; PdxK in *E. coli* additionally functions as hydroxymethylpyrimidine kinase (yang1998identificationandfunction pages 5-7).
- **Serine biosynthesis:** Shares SerC; should be tracked as an overlapping node.
- **Threonine biosynthesis:** ThrC (PP_1471) and PP_0662 belong primarily to amino acid metabolism, not to committed PLP synthesis.

### 2.3 Alternate Names and Database Definitions

The pathway is variously referred to as "vitamin B6 metabolism," "pyridoxine biosynthesis," "PLP biosynthesis," and "DXP-dependent PLP pathway." MetaCyc designates the de novo portion as the "pyridoxal 5′-phosphate biosynthesis I (DXP-dependent)" pathway.

## 3. Expected Step Model

The DXP-dependent de novo pathway in *P. putida* KT2440 is expected to comprise the following enzymatic steps, based on the well-characterized *E. coli* paradigm and comparative genomics across 5,840 bacterial and archaeal genomes (denise2023pyridoxal5’phosphatesynthesis pages 1-3):

**Branch 1 (4-amino-hydroxyacetone phosphate arm):**
1. **Epd** (EC 1.2.1.72): D-erythrose-4-phosphate → 4-phosphoerythronate (NAD⁺-dependent, nonphosphorylating oxidation) (tramonti2021knownsandunknowns pages 5-7, he2024adaptivelaboratoryevolution pages 2-3)
2. **PdxB** (EC 1.1.1.290): 4-phosphoerythronate → 2-oxo-3-hydroxy-4-phosphobutanoate (NAD⁺-dependent oxidation) (tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 7-10)
3. **SerC** (EC 2.6.1.52): 2-oxo-3-hydroxy-4-phosphobutanoate → 4-phospho-hydroxy-L-threonine (aminotransferase, using L-glutamate) (tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 7-10)
4. **PdxA** (EC 1.1.1.262): 4-phospho-hydroxy-L-threonine → 3-amino-1-hydroxyacetone 1-phosphate (NAD⁺-dependent oxidative decarboxylation) (denise2023pyridoxal5’phosphatesynthesis pages 1-3, tramonti2021knownsandunknowns pages 7-10)

**Branch 2 (DXP arm):**
5. **Dxs** (EC 2.2.1.7): Pyruvate + D-glyceraldehyde-3-phosphate → 1-deoxyxylulose-5-phosphate (DXP) (tramonti2021knownsandunknowns pages 10-12)

**Condensation and final oxidation:**
6. **PdxJ** (EC 2.6.99.2): DXP + 3-amino-1-hydroxyacetone 1-phosphate → pyridoxine 5′-phosphate (PNP) (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 6-9)
7. **PdxH** (EC 1.4.3.5): PNP (and PMP) → PLP (FMN-dependent oxidase) (tramonti2021knownsandunknowns pages 10-12, tramonti2021knownsandunknowns pages 5-7)

**Salvage:**
8. **PdxY** (EC 2.7.1.35): Pyridoxal → PLP (ATP-dependent kinase, PL-specific) (tramonti2021knownsandunknowns pages 12-13, yang1998identificationandfunction pages 5-7)
9. **PdxK** (EC 2.7.1.35): PL/PM/PN → PLP/PMP/PNP (broader-substrate kinase; not in candidate list) (yang1998identificationandfunction pages 5-7, denise2023pyridoxal5’phosphatesynthesis pages 1-3)

## 4. Candidate Genes and Evidence

The following table provides a detailed assessment of all nine candidate genes from the local KEGG metadata:

| Gene name | Locus tag | UniProt ID | Proposed function | Pathway step | Evidence type | Confidence level | Curation notes |
|---|---|---|---|---|---|---|---|
| pdxA | PP_0402 | Q88QT5 | 4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262) | De novo DXP-dependent branch: 4-phosphohydroxy-L-threonine → 3-amino-1-hydroxyacetone phosphate | Homology/biochemical transfer from *E. coli* DXP-dependent PLP pathway; KEGG assignment (denise2023pyridoxal5’phosphatesynthesis pages 1-3, tramonti2021knownsandunknowns pages 7-10) | High | Strong fit to canonical DXP-dependent B6 pathway; no direct KT2440 experiment found in retrieved sources; should be treated as core pathway gene, not boundary context. |
| PP_0662 | PP_0662 | Q88Q36 | Threonine synthase-like protein | Boundary/precursor context rather than core B6 step | Computational/KEGG annotation only | Low | Likely over-propagated from overview map context; no evidence that threonine synthase is a committed vitamin B6 enzyme in KT2440; possible paralog/functional redundancy with thrC; keep separate from core PLP satisfiability pending review. |
| pdxH | PP_1129 | Q88NS5 | Pyridoxine/pyridoxamine 5'-phosphate oxidase (PNP/PMP oxidase; EC 1.4.3.5) | Final PLP-forming step: PNP/PMP → PLP; functions in de novo completion and salvage | Homology/biochemical transfer from *E. coli*; KEGG assignment; pathway role well established broadly (tramonti2021knownsandunknowns pages 10-12, tramonti2021knownsandunknowns pages 5-7) | High | Core PLP-forming enzyme; appropriate to mark covered. Retrieved KT2440-specific functional proof was not found, but role is strongly conserved. |
| pdxJ | PP_1436 | Q88MY2 | Pyridoxine 5'-phosphate synthase (PNP synthase; EC 2.6.99.2) | De novo DXP-dependent condensation step: DXP + 3-amino-1-hydroxyacetone phosphate → PNP | Homology/biochemical transfer from *E. coli*; comparative genomics identifies PdxJ as a signature DXP-D protein; KEGG assignment (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 6-9, tramonti2021knownsandunknowns pages 5-7) | High | Signature enzyme for DXP-dependent pathway; strong evidence pathway type is correct for diderm gammaproteobacteria such as *Pseudomonas*. |
| thrC | PP_1471 | Q88MU7 | Threonine synthase (EC 4.2.3.1) | Boundary/precursor amino-acid metabolism context | Direct experimental evidence in *P. putida* supports threonine biosynthesis role/auxotrophy, not core B6 role; KEGG inclusion likely map-context effect (molina‐henares2010identificationofconditionally pages 12-13) | Medium | Valid threonine synthase annotation, but probably not a vitamin B6 pathway gene. Recommend not counting as core module coverage; keep as neighboring precursor context only. |
| serC | PP_1768 | Q88M07 | Phosphoserine aminotransferase / phosphohydroxythreonine aminotransferase (EC 2.6.1.52) | De novo DXP-dependent branch: 2-oxo-3-hydroxy-4-phosphobutanoate → 4-phosphohydroxy-L-threonine | Homology/biochemical transfer from *E. coli*; shared serine/B6 pathway enzyme described in literature; KEGG assignment (tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 7-10) | High | Dual-function/shared enzyme between serine biosynthesis and PLP biosynthesis; curation should capture shared-function caveat rather than treating as B6-specific enzyme family. |
| pdxB | PP_2117 | Q88L20 | Erythronate-4-phosphate dehydrogenase / 4-phosphoerythronate dehydrogenase (EC 1.1.1.290) | De novo DXP-dependent branch: 4-phosphoerythronate → 2-oxo-3-hydroxy-4-phosphobutanoate | Homology/biochemical transfer from *E. coli*; KEGG assignment; comparative genomics support (denise2023pyridoxal5’phosphatesynthesis pages 1-3, tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 7-10) | High | Core DXP-dependent PLP enzyme. No direct KT2440 knockout/biochemistry found in retrieved sources; nonetheless strong orthology-based assignment. |
| epd | PP_4964 | Q88D63 | Erythrose-4-phosphate dehydrogenase (EC 1.2.1.72) | First de novo DXP-dependent branch step: erythrose-4-phosphate → 4-phosphoerythronate | Homology/biochemical transfer from *E. coli*; KEGG assignment; comparative genomics support (denise2023pyridoxal5’phosphatesynthesis pages 1-3, tramonti2021knownsandunknowns pages 5-7) | High | Core pathway enzyme but with caveat: in *E. coli*, GapA shows limited overlapping activity and alternative bypasses can evolve (tramonti2021knownsandunknowns pages 5-7, he2024adaptivelaboratoryevolution pages 2-3, tramonti2021knownsandunknowns pages 15-16). In KT2440 this gene should still be treated as the primary canonical step. |
| pdxY | PP_5357 | Q88C26 | Pyridoxal kinase PdxY (EC 2.7.1.35) | Salvage phosphorylation of B6 vitamers, especially PL → PLP | Homology from *E. coli* PdxY/PdxK salvage system; KEGG assignment (tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 4-5, yang1998identificationandfunction pages 5-7, denise2023pyridoxal5’phosphatesynthesis pages 1-3) | Medium-High | Strong salvage-pathway candidate. Important caveat: PdxY is often PL-specific, whereas a broader PdxK kinase may also exist and is not in the local candidate list; KT2440 salvage annotation should therefore be reviewed for possible missing pdxK-like function. |


*Table: This table summarizes the nine KEGG ppu00750 candidate genes for vitamin B6 metabolism in *Pseudomonas putida* KT2440, distinguishing core DXP-dependent PLP biosynthesis and salvage functions from likely boundary-context annotations. It is useful for module satisfiability review because it highlights which genes are high-confidence pathway components versus probable over-annotations or paralog-related ambiguities.*

### Key observations per gene:

**pdxA (PP_0402, Q88QT5).** Assigned as 4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262). This is a core DXP-dependent pathway enzyme catalyzing the oxidative decarboxylation of 4-phospho-hydroxy-L-threonine to produce 3-amino-1-hydroxyacetone 1-phosphate (denise2023pyridoxal5’phosphatesynthesis pages 1-3, tramonti2021knownsandunknowns pages 7-10). Evidence is by strong orthology from *E. coli*; no direct *P. putida* experiment was retrieved. The annotation is high confidence and appropriate for module coverage.

**PP_0662 (Q88Q36).** Annotated as a threonine synthase. This gene is not a committed vitamin B6 pathway enzyme. Its inclusion in KEGG ppu00750 likely reflects shared precursor-map context. It may be a paralog of thrC (PP_1471) providing functional redundancy in threonine biosynthesis. Confidence for B6 pathway relevance is low; this gene should be treated as boundary context only.

**pdxH (PP_1129, Q88NS5).** Pyridoxine/pyridoxamine 5′-phosphate oxidase (EC 1.4.3.5). This FMN-dependent enzyme catalyzes the final step converting PNP to PLP and also interconverts PMP to PLP in the salvage pathway (tramonti2021knownsandunknowns pages 10-12, tramonti2021knownsandunknowns pages 5-7). High confidence; core to both de novo and salvage PLP metabolism.

**pdxJ (PP_1436, Q88MY2).** PNP synthase (EC 2.6.99.2). A signature enzyme of the DXP-dependent pathway, PdxJ catalyzes the condensation of DXP and 3-amino-1-hydroxyacetone 1-phosphate to form pyridoxine 5′-phosphate (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 6-9). Its presence in the *P. putida* genome, together with the absence of PLP synthase (Pdx1/Pdx2), confirms use of the DXP-D route. High confidence.

**thrC (PP_1471, Q88MU7).** Threonine synthase (EC 4.2.3.1). This gene was identified as conditionally essential for *P. putida* KT2440 growth on minimal medium, producing a threonine auxotroph (molina‐henares2010identificationofconditionally pages 12-13). However, threonine synthase is not a committed vitamin B6 enzyme. Its KEGG inclusion reflects that threonine pathway intermediates feed into the 4-phospho-hydroxy-L-threonine branch, but the connection is indirect. Medium confidence for amino acid function; not appropriate for core B6 module coverage.

**serC (PP_1768, Q88M07).** Phosphoserine aminotransferase (EC 2.6.1.52). SerC is a dual-function enzyme shared between serine biosynthesis and PLP de novo synthesis (tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 7-10). In the B6 context, it catalyzes the transamination of 2-oxo-3-hydroxy-4-phosphobutanoate to 4-phospho-hydroxy-L-threonine. The genes pdxB and serA are homologous, reflecting the evolutionary derivation of the PLP pathway from serine biosynthesis (tramonti2021knownsandunknowns pages 12-13). High confidence, but curation should note shared function.

**pdxB (PP_2117, Q88L20).** Erythronate-4-phosphate dehydrogenase (EC 1.1.1.290). Catalyzes the NAD⁺-dependent oxidation of 4-phosphoerythronate in the second step of the de novo pathway (tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 7-10). In *E. coli*, alternative bypass pathways can compensate when PdxB is absent (tramonti2021knownsandunknowns pages 12-13), but PdxB is the canonical primary enzyme. High confidence.

**epd (PP_4964, Q88D63).** Erythrose-4-phosphate dehydrogenase (EC 1.2.1.72). Catalyzes the first committed step of de novo PLP biosynthesis through NAD⁺-dependent nonphosphorylating oxidation of erythrose-4-phosphate (tramonti2021knownsandunknowns pages 5-7). Epd shares >40% sequence identity with GapA (glyceraldehyde-3-phosphate dehydrogenase) but has distinct substrate specificity (tramonti2021knownsandunknowns pages 5-7). In *E. coli*, GapA can replace Epd at low efficiency, and adaptive laboratory evolution can recruit other enzymes such as succinate semialdehyde dehydrogenase to compensate for epd loss (he2024adaptivelaboratoryevolution pages 2-3). High confidence for primary assignment; the partial functional redundancy with GapA means epd deletion may not always be lethal.

**pdxY (PP_5357, Q88C26).** Pyridoxal kinase (EC 2.7.1.35). In *E. coli*, PdxY is a PL-specific kinase with only ~1% of PdxK's activity when assayed in vitro (tramonti2021knownsandunknowns pages 12-13). PdxK, by contrast, is the primary broader-substrate kinase capable of phosphorylating PL, PM, and PN (yang1998identificationandfunction pages 5-7). The *P. putida* KT2440 candidate list includes pdxY but not pdxK, raising the question of whether the salvage pathway is fully represented. It is possible that a PdxK homolog is present elsewhere in the genome but not captured in the ppu00750 annotation. Medium-high confidence for PdxY; potential gap for PdxK.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Missing Genes

**Dxs (1-deoxyxylulose-5-phosphate synthase, EC 2.2.1.7).** The DXP-D pathway absolutely requires DXP as a substrate for PdxJ (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 6-9). The Dxs enzyme is expected to be encoded in the *P. putida* KT2440 genome (likely as PP_4457 based on KEGG annotations of terpenoid backbone biosynthesis). Its absence from the ppu00750 candidate list reflects KEGG's pathway boundary decision to assign Dxs to isoprenoid/thiamine metabolism rather than B6 metabolism. This is a boundary annotation issue, not a true genomic gap.

**PdxK (broader B6 salvage kinase).** In *E. coli*, PdxK is the primary salvage kinase with activity toward PL, PM, and PN, while PdxY is PL-specific and has much lower activity (tramonti2021knownsandunknowns pages 12-13, yang1998identificationandfunction pages 5-7). The KT2440 candidate list includes only PdxY. A PdxK homolog should be searched in the genome; its absence from the module would leave the salvage pathway incompletely covered for PM and PN phosphorylation.

### 5.2 Likely Over-Annotations

**PP_0662 (threonine synthase candidate).** This gene's inclusion in ppu00750 is almost certainly map-context propagation from the overview KEGG map that links threonine intermediates to B6 precursors. PP_0662 should not be counted toward B6 module satisfiability.

**thrC (PP_1471).** Similarly, while thrC is a valid threonine synthase and was experimentally confirmed as conditionally essential for growth on minimal medium in *P. putida* KT2440 (molina‐henares2010identificationofconditionally pages 12-13), it is not a committed PLP biosynthesis enzyme. Its KEGG placement in ppu00750 is boundary context.

### 5.3 Paralog Ambiguity

PP_0662 and thrC (PP_1471) are both annotated as threonine synthases. Whether they are true paralogs with overlapping function or one is misannotated requires further investigation. For the purpose of B6 module curation, neither is relevant.

### 5.4 Dual-Function Concerns

SerC (PP_1768) genuinely participates in both serine biosynthesis and PLP biosynthesis (tramonti2021knownsandunknowns pages 12-13). Module curation should flag this shared function so that serC is not treated as exclusively a B6-pathway gene.

## 6. Module Step Satisfiability Assessment

The following table provides the step-level satisfiability assessment:

| Module Step | Reaction Description | Expected Enzyme | Candidate Gene(s) | Status | Notes |
|---|---|---|---|---|---|
| 1. Erythrose-4-phosphate oxidation | Erythrose-4-phosphate → 4-phosphoerythronate | Epd (EC 1.2.1.72) | PP_4964 (*epd*) | covered | Canonical first step of the DXP-dependent PLP pathway; strong homology-based support. In *E. coli*, GapA can show limited overlapping activity, so partial backup is plausible but does not replace *epd* as the primary assignment (tramonti2021knownsandunknowns pages 5-7, he2024adaptivelaboratoryevolution pages 2-3, denise2023pyridoxal5’phosphatesynthesis pages 1-3). |
| 2. 4-phosphoerythronate oxidation | 4-phosphoerythronate → 2-oxo-3-hydroxy-4-phosphobutanoate | PdxB (EC 1.1.1.290) | PP_2117 (*pdxB*) | covered | Core DXP-dependent de novo step; strongly conserved in Gram-negative PLP synthesis pathways and included in comparative genomics pathway models (denise2023pyridoxal5’phosphatesynthesis pages 1-3, tramonti2021knownsandunknowns pages 5-7). |
| 3. Transamination to 4-phospho-hydroxy-L-threonine | 2-oxo-3-hydroxy-4-phosphobutanoate → 4-phospho-hydroxy-L-threonine | SerC (EC 2.6.1.52) | PP_1768 (*serC*) | covered | Shared enzyme between serine biosynthesis and PLP biosynthesis; should be curated as a dual-function step rather than B6-specific only (tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 7-10). |
| 4. 4-Phosphohydroxythreonine oxidation | 4-phospho-hydroxy-L-threonine → 3-amino-1-hydroxyacetone 1-phosphate | PdxA (EC 1.1.1.262) | PP_0402 (*pdxA*) | covered | Canonical DXP-dependent B6 pathway enzyme; strong orthology-based assignment, though direct KT2440 biochemical validation was not retrieved (denise2023pyridoxal5’phosphatesynthesis pages 1-3, tramonti2021knownsandunknowns pages 7-10). |
| 5. PNP synthesis | DXP + 3-amino-1-hydroxyacetone 1-phosphate → pyridoxine 5'-phosphate (PNP) | PdxJ (EC 2.6.99.2) | PP_1436 (*pdxJ*) | covered | Signature enzyme of the DXP-dependent pathway; strong evidence that *Pseudomonas* should use this route as a diderm gammaproteobacterium (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 6-9). |
| 6. DXP supply | Pyruvate + glyceraldehyde-3-phosphate → DXP | Dxs (EC 2.2.1.7) | Not in candidate list; likely genomic gene such as PP_4457/*dxs* | gap | Biochemically required for the de novo pathway because PdxJ consumes DXP; likely omitted because KEGG ppu00750 boundary centers on vitamin B6 steps while DXP is shared with thiamine/isoprenoid metabolism (tramonti2021knownsandunknowns pages 10-12, denise2023pyridoxal5’phosphatesynthesis pages 6-9, denise2023pyridoxal5’phosphatesynthesis pages 1-3). |
| 7. PNP/PMP oxidation to PLP | PNP (and PMP) → PLP | PdxH (EC 1.4.3.5) | PP_1129 (*pdxH*) | covered | Final PLP-forming step; functions at the interface of de novo synthesis and salvage, with strong conserved assignment (tramonti2021knownsandunknowns pages 10-12, tramonti2021knownsandunknowns pages 5-7). |
| 8. B6 salvage phosphorylation | Pyridoxal (PL) → PLP | PdxY (EC 2.7.1.35) | PP_5357 (*pdxY*) | covered | Good salvage assignment. In model bacteria, PdxY is usually PL-specific; broader salvage may additionally require PdxK-like kinase activity not represented in the local candidate set (tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 4-5, yang1998identificationandfunction pages 5-7, denise2023pyridoxal5’phosphatesynthesis pages 1-3). |
| 9. Threonine biosynthesis (boundary context) | O-phosphohomoserine → threonine | ThrC (EC 4.2.3.1) | PP_1471 (*thrC*), PP_0662 | module_needs_revision | These are plausible threonine synthase annotations, but not core vitamin B6 pathway steps. Their presence in KEGG ppu00750 likely reflects shared precursor/amino-acid map context rather than committed PLP synthesis; treat as boundary context and revise module boundary accordingly (molina‐henares2010identificationofconditionally pages 12-13). |
| 10. Broader B6 salvage kinase | PL/PM/PN → PLP/PMP/PNP | PdxK | Not in candidate list | candidate_uncertain | In model bacteria, PdxK often complements or exceeds PdxY substrate scope. A KT2440 PdxK homolog may be present but was not retrieved from the local candidate list; this is a targeted review item rather than proof of absence (tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 4-5, yang1998identificationandfunction pages 5-7, denise2023pyridoxal5’phosphatesynthesis pages 1-3). |


*Table: This table summarizes step-level satisfiability for vitamin B6 metabolism in *Pseudomonas putida* KT2440, separating well-supported core DXP-dependent PLP synthesis steps from boundary-context or uncertain salvage annotations. It is useful for deciding which module steps are covered, missing from the candidate list, or in need of boundary revision.*

### Summary of satisfiability status:

- **Covered (high confidence):** Steps 1–5 and 7 (Epd → PdxB → SerC → PdxA → PdxJ → PdxH) represent the complete de novo DXP-dependent PLP biosynthesis from erythrose-4-phosphate to PLP. All six required genes are present in the candidate list.
- **Covered (medium-high confidence):** Step 8 (PdxY salvage phosphorylation) is covered but may be incomplete without PdxK.
- **Gap (boundary issue):** Step 6 (Dxs/DXP supply) is biochemically required but excluded from the module boundary by KEGG's assignment to isoprenoid metabolism.
- **Candidate_uncertain:** Step 10 (PdxK broader salvage kinase) — not in candidate list; may or may not be present in genome.
- **Module_needs_revision:** Step 9 (ThrC/PP_0662 threonine synthase context) — these should be removed from core B6 module coverage or explicitly flagged as boundary-only nodes.

## 7. Module and GO-Curation Recommendations

1. **Core module is satisfiable.** The six de novo DXP-dependent pathway steps (Epd → PdxB → SerC → PdxA → PdxJ → PdxH) plus the PdxY salvage kinase provide a functionally complete PLP biosynthesis and salvage module, assuming Dxs is supplied from the adjacent isoprenoid/thiamine module.

2. **Revise module boundaries.** ThrC (PP_1471) and PP_0662 should be excluded from the core vitamin B6 module or explicitly tagged as "boundary context—amino acid precursor supply." Their inclusion inflates apparent module complexity without contributing to PLP satisfiability.

3. **Flag SerC as shared-function.** Curation should annotate SerC with both GO:0004648 (O-phospho-L-serine:2-oxoglutarate aminotransferase activity) and the B6-specific transaminase function, with a note that it operates at the intersection of two pathways (tramonti2021knownsandunknowns pages 12-13).

4. **Search for PdxK.** The absence of a PdxK-like gene from the candidate list should be investigated. If a PdxK homolog (COG0351/ThiD2 family or COG2240) exists in the KT2440 genome, it should be added to the salvage module (denise2023pyridoxal5’phosphatesynthesis pages 1-3).

5. **Consider adding Dxs as a boundary node.** While properly belonging to isoprenoid/thiamine metabolism, Dxs (likely PP_4457) is essential for PdxJ function. A cross-reference or boundary link would strengthen module documentation.

6. **Vitamin B6 essentiality under anaerobic conditions.** Metabolic modeling and design studies for anaerobic *P. putida* engineering indicate that PLP cannot be synthesized under anoxic conditions, requiring exogenous supplementation (kampers2020arationaldesign pages 13-15). This implies that one or more de novo pathway steps (possibly PdxH, which requires O₂-dependent FMN) are oxygen-dependent, which is relevant to module annotation under different growth conditions.

7. **Gene essentiality context.** A genome-wide transposon mutant library screen of *P. putida* KT2440 identified 48 conditionally essential genes for minimal-medium growth, including auxotrophs for threonine (thrC) and serine (serA/serB) but not specifically for vitamin B6 (molina‐henares2010identificationofconditionally pages 2-3, molina‐henares2010identificationofconditionally pages 1-2, molina‐henares2010identificationofconditionally pages 12-13). The absence of B6 auxotrophs from this screen could indicate either (a) transposon insertions in B6 genes are truly essential (lethal) rather than conditionally essential, or (b) functional redundancy (e.g., GapA partially compensating for Epd) prevents simple auxotrophy. This remains an open question.

## 8. Genes to Promote to Full Review

1. **pdxJ (PP_1436)** — Signature DXP-D pathway enzyme. A full review would confirm that *P. putida* lacks PLP synthase (Pdx1/Pdx2) and definitively uses the DXP-D route.
2. **pdxH (PP_1129)** — Dual de novo/salvage function; potential oxygen dependence relevant to anaerobic engineering efforts.
3. **pdxY (PP_5357)** — Needs clarification of substrate scope in *P. putida* and whether PdxK function is present elsewhere in the genome.
4. **epd (PP_4964)** — Investigate whether GapA-mediated backup is physiologically relevant in KT2440; explore whether adaptive evolution studies (he2024adaptivelaboratoryevolution pages 2-3) are transferable.

## 9. Evidence and Open Questions

### Conclusions supported by direct experiments:
- *P. putida* KT2440 is a PLP prototroph under aerobic conditions (grows on minimal medium without B6 supplementation) (molina‐henares2010identificationofconditionally pages 2-3, molina‐henares2010identificationofconditionally pages 1-2).
- ThrC (PP_1471) knockout produces a threonine auxotroph in KT2440 (molina‐henares2010identificationofconditionally pages 12-13).
- Under anoxic conditions, PLP biosynthesis is disrupted and requires supplementation (kampers2020arationaldesign pages 13-15).

### Conclusions inferred from homology and pathway databases:
- All gene function assignments for the DXP-D pathway enzymes are based on *E. coli* orthology and KEGG/UniProt propagation, not on direct biochemistry in *P. putida* KT2440 (denise2023pyridoxal5’phosphatesynthesis pages 1-3).
- The DXP-D pathway assignment to *Pseudomonas* rests on phylogenetic distribution analysis showing that diderm Gammaproteobacteria predominantly use DXP-D (denise2023pyridoxal5’phosphatesynthesis pages 6-9, denise2023pyridoxal5’phosphatesynthesis pages 4-6).

### Open questions requiring experiments or expert review:
1. Does KT2440 encode a PdxK-type kinase, and if so, under what locus tag?
2. What is the true essentiality status of individual B6 pathway genes (pdxA, pdxB, pdxJ, pdxH, epd) in KT2440 — are they unconditionally essential?
3. Does PP_0662 have genuine threonine synthase activity, or is it a pseudogene/misannotation?
4. Is PdxH the oxygen-dependent step limiting anaerobic PLP synthesis?
5. Are any non-orthologous displacements present for early pathway steps (Epd, PdxB, SerC) in *P. putida*, as observed in some other Gammaproteobacteria (denise2023pyridoxal5’phosphatesynthesis pages 6-9)?

## 10. Key References

- Denise R, Babor J, Gerlt JA, de Crécy-Lagard V. "Pyridoxal 5'-phosphate synthesis and salvage in Bacteria and Archaea: predicting pathway variant distributions and holes." *Microbial Genomics* 9(2), 2023. DOI: 10.1099/mgen.0.000926 (denise2023pyridoxal5’phosphatesynthesis pages 1-3, denise2023pyridoxal5’phosphatesynthesis pages 6-9, denise2023pyridoxal5’phosphatesynthesis pages 4-6).
- Tramonti A, et al. "Knowns and Unknowns of Vitamin B₆ Metabolism in *Escherichia coli*." *EcoSal Plus* 9(2), 2021. DOI: 10.1128/ecosalplus.esp-0004-2021 (tramonti2021knownsandunknowns pages 5-7, tramonti2021knownsandunknowns pages 10-12, tramonti2021knownsandunknowns pages 4-5, tramonti2021knownsandunknowns pages 12-13, tramonti2021knownsandunknowns pages 15-16, tramonti2021knownsandunknowns pages 7-10).
- Yang Y, Tsui HCT, Man TK, Winkler ME. "Identification and Function of the pdxY Gene, Which Encodes a Novel Pyridoxal Kinase Involved in the Salvage Pathway of Pyridoxal 5′-Phosphate Biosynthesis in *Escherichia coli* K-12." *Journal of Bacteriology* 180:1814–1821, 1998. DOI: 10.1128/jb.180.7.1814-1821.1998 (yang1998identificationandfunction pages 5-7).
- Molina-Henares MA, et al. "Identification of conditionally essential genes for growth of *Pseudomonas putida* KT2440 on minimal medium through the screening of a genome-wide mutant library." *Environmental Microbiology* 12:1468–1485, 2010. DOI: 10.1111/j.1462-2920.2010.02166.x (molina‐henares2010identificationofconditionally pages 2-3, molina‐henares2010identificationofconditionally pages 1-2, molina‐henares2010identificationofconditionally pages 3-4, molina‐henares2010identificationofconditionally pages 12-13, molina‐henares2010identificationofconditionally pages 4-6).
- He H, et al. "Adaptive laboratory evolution recruits the promiscuity of succinate semialdehyde dehydrogenase to repair different metabolic deficiencies." *Nature Communications* 15, 2024. DOI: 10.1038/s41467-024-53156-x (he2024adaptivelaboratoryevolution pages 2-3).
- Kampers LFC, et al. "A metabolic and physiological design study of *Pseudomonas putida* KT2440 capable of anaerobic respiration." *BMC Microbiology* 21, 2021. DOI: 10.1186/s12866-020-02058-1 (kampers2020arationaldesign pages 13-15).
- Belda E, et al. "The revisited genome of *Pseudomonas putida* KT2440 enlightens its value as a robust metabolic chassis." *Environmental Microbiology* 18(10):3403–3424, 2016. DOI: 10.1111/1462-2920.13230 (belda2016therevisitedgenome pages 10-12).
- Nogales J, et al. "High-quality genome-scale metabolic modelling of *Pseudomonas putida* highlights its broad metabolic capabilities." *Environmental Microbiology* 22:255–269, 2020. DOI: 10.1111/1462-2920.14843.

References

1. (denise2023pyridoxal5’phosphatesynthesis pages 6-9): Rémi Denise, Jill Babor, John A. Gerlt, and Valérie de Crécy-Lagard. Pyridoxal 5’-phosphate synthesis and salvage in bacteria and archaea: predicting pathway variant distributions and holes. Feb 2023. URL: https://doi.org/10.1099/mgen.0.000926, doi:10.1099/mgen.0.000926. This article has 22 citations and is from a peer-reviewed journal.

2. (denise2023pyridoxal5’phosphatesynthesis pages 4-6): Rémi Denise, Jill Babor, John A. Gerlt, and Valérie de Crécy-Lagard. Pyridoxal 5’-phosphate synthesis and salvage in bacteria and archaea: predicting pathway variant distributions and holes. Feb 2023. URL: https://doi.org/10.1099/mgen.0.000926, doi:10.1099/mgen.0.000926. This article has 22 citations and is from a peer-reviewed journal.

3. (denise2023pyridoxal5’phosphatesynthesis pages 1-3): Rémi Denise, Jill Babor, John A. Gerlt, and Valérie de Crécy-Lagard. Pyridoxal 5’-phosphate synthesis and salvage in bacteria and archaea: predicting pathway variant distributions and holes. Feb 2023. URL: https://doi.org/10.1099/mgen.0.000926, doi:10.1099/mgen.0.000926. This article has 22 citations and is from a peer-reviewed journal.

4. (tramonti2021knownsandunknowns pages 5-7): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

5. (tramonti2021knownsandunknowns pages 7-10): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

6. (tramonti2021knownsandunknowns pages 12-13): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

7. (yang1998identificationandfunction pages 5-7): Yong Yang, Ho-Ching Tiffany Tsui, Tsz-Kwong Man, and Malcolm E. Winkler. Identification and function of the pdxy gene, which encodes a novel pyridoxal kinase involved in the salvage pathway of pyridoxal 5′-phosphate biosynthesis in escherichia coli k-12. Journal of Bacteriology, 180:1814-1821, Apr 1998. URL: https://doi.org/10.1128/jb.180.7.1814-1821.1998, doi:10.1128/jb.180.7.1814-1821.1998. This article has 141 citations and is from a peer-reviewed journal.

8. (tramonti2021knownsandunknowns pages 4-5): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

9. (tramonti2021knownsandunknowns pages 10-12): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

10. (he2024adaptivelaboratoryevolution pages 2-3): Hai He, Paul A. Gómez-Coronado, Jan Zarzycki, Sebastian Barthel, Jörg Kahnt, Peter Claus, Moritz Klein, Melanie Klose, Valérie de Crécy-Lagard, Daniel Schindler, Nicole Paczia, Timo Glatter, and Tobias J. Erb. Adaptive laboratory evolution recruits the promiscuity of succinate semialdehyde dehydrogenase to repair different metabolic deficiencies. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53156-x, doi:10.1038/s41467-024-53156-x. This article has 19 citations and is from a highest quality peer-reviewed journal.

11. (molina‐henares2010identificationofconditionally pages 12-13): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

12. (tramonti2021knownsandunknowns pages 15-16): Angela Tramonti, Caterina Nardella, Martino L. di Salvo, Anna Barile, Federico D’Alessio, Valérie de Crécy-Lagard, and Roberto Contestabile. Knowns and unknowns of vitamin b <sub>6</sub> metabolism in escherichia coli. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0004-2021, doi:10.1128/ecosalplus.esp-0004-2021. This article has 64 citations.

13. (kampers2020arationaldesign pages 13-15): Linde F. C. Kampers, Jasper J. Koehorst, Ruben G. A. van Heck, Maria Suarez-Diez, Alfons J. M. Stams, and Peter J. Schaap. A rational design of pseudomonas putida kt2440 capable of anaerobic respiration. ArXiv, Apr 2020. URL: https://doi.org/10.21203/rs.3.rs-21150/v1, doi:10.21203/rs.3.rs-21150/v1. This article has 1 citations.

14. (molina‐henares2010identificationofconditionally pages 2-3): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

15. (molina‐henares2010identificationofconditionally pages 1-2): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

16. (molina‐henares2010identificationofconditionally pages 3-4): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

17. (molina‐henares2010identificationofconditionally pages 4-6): M. Antonia Molina‐Henares, Jesús De La Torre, Adela García‐Salamanca, A. Jesús Molina‐Henares, M. Carmen Herrera, Juan L. Ramos, and Estrella Duque. Identification of conditionally essential genes for growth of <i>pseudomonas putida</i> kt2440 on minimal medium through the screening of a genome‐wide mutant library. Environmental Microbiology, 12:1468-1485, Jun 2010. URL: https://doi.org/10.1111/j.1462-2920.2010.02166.x, doi:10.1111/j.1462-2920.2010.02166.x. This article has 90 citations and is from a domain leading peer-reviewed journal.

18. (belda2016therevisitedgenome pages 10-12): Eugeni Belda, Ruben G. A. van Heck, Maria José Lopez‐Sanchez, Stéphane Cruveiller, Valérie Barbe, Claire Fraser, Hans‐Peter Klenk, Jörn Petersen, Anne Morgat, Pablo I. Nikel, David Vallenet, Zoé Rouy, Agnieszka Sekowska, Vitor A. P. Martins dos Santos, Víctor de Lorenzo, Antoine Danchin, and Claudine Médigue. The revisited genome of pseudomonas putida kt2440 enlightens its value as a robust metabolic chassis. Environmental microbiology, 18 10:3403-3424, Oct 2016. URL: https://doi.org/10.1111/1462-2920.13230, doi:10.1111/1462-2920.13230. This article has 376 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__vitamin_b6_metabolism__ppu00750-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__vitamin_b6_metabolism__ppu00750-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. tramonti2021knownsandunknowns pages 12-13
2. yang1998identificationandfunction pages 5-7
3. tramonti2021knownsandunknowns pages 10-12
4. tramonti2021knownsandunknowns pages 5-7
5. he2024adaptivelaboratoryevolution pages 2-3
6. kampers2020arationaldesign pages 13-15
7. belda2016therevisitedgenome pages 10-12
8. tramonti2021knownsandunknowns pages 7-10
9. tramonti2021knownsandunknowns pages 4-5
10. tramonti2021knownsandunknowns pages 15-16
11. https://doi.org/10.1099/mgen.0.000926,
12. https://doi.org/10.1128/ecosalplus.esp-0004-2021,
13. https://doi.org/10.1128/jb.180.7.1814-1821.1998,
14. https://doi.org/10.1038/s41467-024-53156-x,
15. https://doi.org/10.1111/j.1462-2920.2010.02166.x,
16. https://doi.org/10.21203/rs.3.rs-21150/v1,
17. https://doi.org/10.1111/1462-2920.13230,