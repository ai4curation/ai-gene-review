---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T15:35:37.249400'
end_time: '2026-07-06T15:54:57.674034'
duration_seconds: 1160.42
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Benzoate upper pathway to catechol
  module_summary: A taxon-neutral bacterial upper-pathway module for the conversion
    of benzoate to catechol by benzoate 1,2-dioxygenase and the cognate cis-dihydrodiol
    dehydrogenase. This module captures the entry branch that supplies catechol to
    downstream ortho-cleavage or meta-cleavage routes. Broad xylene/toluene degradation
    maps can include methylated-aromatic upper pathways and meta-cleavage enzymes;
    those are adjacent context unless the taxon encodes the corresponding substrate-specific
    route.
  module_outline: "- Benzoate upper pathway to catechol\n  - 1. benzoate hydroxylation\
    \ to the cis-dihydrodiol intermediate\n  - Benzoate 1,2-dioxygenase complex\n\
    \    - Benzoate 1,2-dioxygenase (molecular player: benzoate 1,2-dioxygenase activity;\
    \ activity or role: benzoate 1,2-dioxygenase activity)\n  - 2. benzoate cis-dihydrodiol\
    \ dehydrogenation to catechol\n  - Benzoate cis-dihydrodiol dehydrogenase\n  \
    \  - 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (molecular player:\
    \ 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity; activity\
    \ or role: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity)"
  module_connections: '- Benzoate 1,2-dioxygenase complex feeds into Benzoate cis-dihydrodiol
    dehydrogenase: The BenABC product is the substrate for BenD.'
  pathway_query: ppu00622
  pathway_id: ppu00622
  pathway_name: Xylene degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00622 with 4 primary genes; module
    area: aromatic_and_xenobiotic_catabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '6'
  candidate_genes: '- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket
    kegg:ppu00621)

    - PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate
    tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)

    - benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10)
    (EC 1.14.12.10; primary bucket kegg:ppu00622)

    - benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10)
    (EC 1.14.12.10; primary bucket kegg:ppu00622)

    - benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component
    (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)

    - benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase
    (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)'
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
  path: PSEPK__benzoate_upper_pathway__ppu00622-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__benzoate_upper_pathway__ppu00622-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Benzoate upper pathway to catechol in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00622
- Resolved ID: ppu00622
- Resolved name: Xylene degradation
- Source: KEGG

Resolved local bucket kegg:ppu00622 with 4 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 6

- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)
- PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)
- benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)
- benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)

## Generic Module Context

### Working Scope

A taxon-neutral bacterial upper-pathway module for the conversion of benzoate to catechol by benzoate 1,2-dioxygenase and the cognate cis-dihydrodiol dehydrogenase. This module captures the entry branch that supplies catechol to downstream ortho-cleavage or meta-cleavage routes. Broad xylene/toluene degradation maps can include methylated-aromatic upper pathways and meta-cleavage enzymes; those are adjacent context unless the taxon encodes the corresponding substrate-specific route.

### Provisional Biological Outline

- Benzoate upper pathway to catechol
  - 1. benzoate hydroxylation to the cis-dihydrodiol intermediate
  - Benzoate 1,2-dioxygenase complex
    - Benzoate 1,2-dioxygenase (molecular player: benzoate 1,2-dioxygenase activity; activity or role: benzoate 1,2-dioxygenase activity)
  - 2. benzoate cis-dihydrodiol dehydrogenation to catechol
  - Benzoate cis-dihydrodiol dehydrogenase
    - 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (molecular player: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity; activity or role: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity)

### Known Relationships Among Steps

- Benzoate 1,2-dioxygenase complex feeds into Benzoate cis-dihydrodiol dehydrogenase: The BenABC product is the substrate for BenD.

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

Benzoate upper pathway to catechol in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00622
- Resolved ID: ppu00622
- Resolved name: Xylene degradation
- Source: KEGG

Resolved local bucket kegg:ppu00622 with 4 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 6

- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)
- PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)
- benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)
- benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)

## Generic Module Context

### Working Scope

A taxon-neutral bacterial upper-pathway module for the conversion of benzoate to catechol by benzoate 1,2-dioxygenase and the cognate cis-dihydrodiol dehydrogenase. This module captures the entry branch that supplies catechol to downstream ortho-cleavage or meta-cleavage routes. Broad xylene/toluene degradation maps can include methylated-aromatic upper pathways and meta-cleavage enzymes; those are adjacent context unless the taxon encodes the corresponding substrate-specific route.

### Provisional Biological Outline

- Benzoate upper pathway to catechol
  - 1. benzoate hydroxylation to the cis-dihydrodiol intermediate
  - Benzoate 1,2-dioxygenase complex
    - Benzoate 1,2-dioxygenase (molecular player: benzoate 1,2-dioxygenase activity; activity or role: benzoate 1,2-dioxygenase activity)
  - 2. benzoate cis-dihydrodiol dehydrogenation to catechol
  - Benzoate cis-dihydrodiol dehydrogenase
    - 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (molecular player: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity; activity or role: 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity)

### Known Relationships Among Steps

- Benzoate 1,2-dioxygenase complex feeds into Benzoate cis-dihydrodiol dehydrogenase: The BenABC product is the substrate for BenD.

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

# Benzoate Upper Pathway to Catechol in *Pseudomonas putida* KT2440: Module/Pathway Review

## 1. Executive Summary

The benzoate upper pathway to catechol in *Pseudomonas putida* KT2440 (NCBI taxon 160488, proteome UP000000556) is a well-characterized, chromosomally encoded two-step conversion catalyzed by the products of the *ben* operon. The pathway converts benzoate to catechol via a *cis*-dihydrodiol intermediate, supplying catechol to the downstream ortho-cleavage (β-ketoadipate) pathway. All four core enzymatic genes—*benA* (PP_3161), *benB* (PP_3162), *benC* (PP_3163), and *benD* (PP_3164)—are present in the KT2440 genome and supported by direct proteomic, transcriptomic, and enzyme-activity evidence (kim2006analysisofaromatic pages 6-7, cowles2000benraxyls pages 4-5, duuren2011optimizationofpseudomonas pages 15-16). The module is fully satisfiable in this organism.

Two additional candidate genes from the local metadata—PP_1791 (aldolase/synthase) and PP_2504 (2-hydroxymuconate tautomerase, EC 5.3.2.6)—are meta-cleavage pathway enzymes that do not belong to the benzoate upper pathway. KT2440 degrades benzoate exclusively via the ortho-cleavage route; direct enzyme activity assays detected catechol 1,2-dioxygenase activity (1.26 U/mg) but no catechol 2,3-dioxygenase activity under benzoate growth conditions (kim2006analysisofaromatic pages 6-7). These two genes represent over-propagated annotations from the broader KEGG xylene/benzoate degradation maps and should be excluded from this module.

## 2. Target-Organism Pathway Definition

### 2.1 Biochemical Scope

The module encompasses precisely two enzymatic steps:

1. **Benzoate hydroxylation**: Benzoate + O₂ + NADH + H⁺ → *cis*-1,2-dihydroxy-1,2-dihydrobenzoate (benzoate *cis*-dihydrodiol) + NAD⁺, catalyzed by the three-component benzoate 1,2-dioxygenase (BenABC; EC 1.14.12.10) (cowles2000benraxyls pages 4-5, duuren2011optimizationofpseudomonas pages 24-27).
2. **Dihydrodiol dehydrogenation**: *cis*-1,2-dihydroxy-1,2-dihydrobenzoate + NAD⁺ → catechol + CO₂ + NADH, catalyzed by 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (BenD; EC 1.3.1.25) (cowles2000benraxyls pages 4-5, duuren2011optimizationofpseudomonas pages 15-16).

Notably, the NADH consumed in step 1 is regenerated in step 2, resulting in no net cofactor consumption for the overall benzoate → catechol conversion (duuren2011optimizationofpseudomonas pages 15-16).

### 2.2 Pathway Boundaries

**Included**: The two enzymatic conversions above (benzoate → *cis*-dihydrodiol → catechol), corresponding to the *benABCD* gene products.

**Excluded (adjacent context)**:
- **Upstream**: Benzoate transport (*benK*, *benE*, *benF*) and transcriptional regulation (*benR*). While genomically linked to the *ben* operon, transport and regulation are outside the core biochemical module boundary (choudhary2017benzoatetransportin pages 4-6).
- **Downstream**: Catechol ortho-cleavage via catechol 1,2-dioxygenase (*catA*, *catA2*/PP_3166), the *catBCA* operon, and the *pca* operon (β-ketoadipate pathway). These constitute a separate module (duuren2011optimizationofpseudomonas pages 15-16, duuren2011optimizationofpseudomonas pages 24-27).
- **Meta-cleavage**: Catechol 2,3-dioxygenase and associated meta-cleavage enzymes (e.g., 4-oxalocrotonate tautomerase, hydroxymuconate semialdehyde dehydrogenase). KT2440 does not possess a functional chromosomal meta-cleavage pathway for catechol; meta-cleavage capability requires the TOL plasmid pWW0, which is absent from KT2440 (duuren2011optimizationofpseudomonas pages 15-16, tsipa2015connectingtranscriptionalregulation pages 27-32, panke1998engineeringofquasinatural pages 2-3).

### 2.3 Alternate Names and Database Definitions

- KEGG map ppu00622 ("Xylene degradation") is an overview map that includes methylated-aromatic upper pathways, meta-cleavage enzymes, and the benzoate upper pathway. The benzoate-to-catechol conversion is only a small subset of this broad map.
- KEGG map ppu00362 ("Benzoate degradation") also captures these steps.
- MetaCyc pathway: "benzoate degradation I (aerobic)" or "superpathway of benzoate degradation (aerobic)."
- The working scope as defined—"benzoate upper pathway to catechol"—is the most precise and unambiguous designation for this module.

## 3. Expected Step Model

The module requires exactly two catalytic steps, carried by four genes:

| Step | Reaction | Enzyme complex | Genes | EC |
|------|----------|---------------|-------|-----|
| 1 | Benzoate → *cis*-1,2-dihydroxy-1,2-dihydrobenzoate | Benzoate 1,2-dioxygenase (3-component Rieske dioxygenase) | *benA* (α-subunit), *benB* (β-subunit), *benC* (electron transfer/reductase) | 1.14.12.10 (+ 1.18.1.3 for BenC reductase domain) |
| 2 | *cis*-1,2-dihydroxy-1,2-dihydrobenzoate → catechol + CO₂ | *cis*-diol dehydrogenase | *benD* | 1.3.1.25 |

The relationship between steps is strictly sequential: the BenABC product is the sole substrate for BenD (cowles2000benraxyls pages 4-5, duuren2011optimizationofpseudomonas pages 24-27).

## 4. Candidate Genes and Evidence

The following table provides detailed assessment of all six candidate genes:

| Gene name | Locus tag (PP_number) | UniProt ID | Encoded protein | EC number | Module step | Evidence type | Confidence level | Module status recommendation | Key notes |
|---|---|---|---|---|---|---|---|---|---|
| benA | PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (large oxygenase subunit) | 1.14.12.10 | Step 1: benzoate → cis-1,2-dihydrodiol intermediate | direct | high | covered | Direct KT2440 proteomics identified BenA as benzoate-induced; part of chromosomal ben operon activated by BenR in response to benzoate. Core upper-pathway gene and should be retained in this module. (kim2006analysisofaromatic pages 6-7, cowles2000benraxyls pages 3-4, moreno2008thetargetfor pages 1-2) |
| benB | PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (small oxygenase subunit) | 1.14.12.10 | Step 1: benzoate → cis-1,2-dihydrodiol intermediate | inferred/direct-operon | high | covered | BenB is part of the BenABC dioxygenase complex and is cotranscribed with benA/benC under BenR control; direct KT2440 operon/regulatory evidence strongly supports assignment even if proteomic detection is less explicit than for BenA. (cowles2000benraxyls pages 4-5, moreno2008thetargetfor pages 1-2) |
| benC | PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component | 1.14.12.10; 1.18.1.3 | Step 1: electron transfer to BenAB dioxygenase during benzoate oxidation | inferred/direct-operon | high | covered | BenC is the electron transfer component of the BenABC multicomponent dioxygenase; direct KT2440 pathway/regulatory evidence supports inclusion as an essential part of step 1. Broad EC mappings should be curated cautiously, but role in benzoate upper pathway is secure. (cowles2000benraxyls pages 4-5, moreno2008thetargetfor pages 1-2) |
| benD | PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (cis-diol dehydrogenase) | 1.3.1.25 | Step 2: cis-dihydrodiol → catechol | direct | high | covered | Direct KT2440 proteomics identified BenD as benzoate-induced; biochemically assigned as the dehydrogenase converting the BenABC product to catechol. This is the canonical second step of the upper pathway. (kim2006analysisofaromatic pages 6-7, cowles2000benraxyls pages 4-5, duuren2011optimizationofpseudomonas pages 15-16) |
| PP_1791 | PP_1791 | Q88LY5 | Aldolase/synthase | not specific for this module | None in benzoate upper pathway | inferred negative | low | over-annotation | No evidence links PP_1791 to benzoate-to-catechol conversion in KT2440. The organism primarily uses the ortho-cleavage route after catechol, and this gene is not part of benABCD or the defined upper pathway boundary; likely belongs to adjacent/meta-cleavage context or another pathway bucket and should not satisfy this module. (duuren2011optimizationofpseudomonas pages 15-16, panke1998engineeringofquasinatural pages 2-3) |
| PP_2504 | PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase / 4-oxalocrotonate tautomerase | 5.3.2.6 | None in benzoate upper pathway | inferred negative | medium | over-annotation | EC 5.3.2.6 is a meta-cleavage-pathway enzyme acting downstream of catechol 2,3-dioxygenase, not in benzoate upper conversion to catechol. KT2440 benzoate metabolism is supported by catechol 1,2-dioxygenase activity and no detectable catechol 2,3-dioxygenase activity under benzoate growth, so this gene should be excluded from the upper module. (kim2006analysisofaromatic pages 6-7, duuren2011optimizationofpseudomonas pages 15-16, choudhary2017benzoatetransportin pages 4-6) |


*Table: This table evaluates all six candidate genes against the benzoate upper pathway to catechol in Pseudomonas putida KT2440, distinguishing core covered genes from likely over-annotated adjacent-pathway genes. It is useful for module satisfiability decisions and targeted gene curation.*

### 4.1 High-Confidence Core Genes

**benA (PP_3161, Q88I40)**: Encodes the α (large) oxygenase subunit of benzoate 1,2-dioxygenase. This Rieske non-heme iron dioxygenase contains the [2Fe-2S] cluster and catalytic iron center. Direct KT2440 evidence: identified as a benzoate-induced protein by 2-DE/MS proteomics (kim2006analysisofaromatic pages 6-7). Expression is activated by BenR in response to benzoate (cowles2000benraxyls pages 3-4) and subject to Crc-mediated carbon catabolite repression at the translational level of BenR (moreno2008thetargetfor pages 2-2, moreno2008thetargetfor pages 1-2). **Confidence: high. Status: covered.**

**benB (PP_3162, Q88I39)**: Encodes the β (small) oxygenase subunit. BenB forms the α₃β₃ heterohexameric oxygenase component with BenA. Co-transcribed with *benA* and *benC* in the *benABCD* operon (cowles2000benraxyls pages 4-5). While direct proteomic detection of BenB alone is less explicitly documented than BenA, its inclusion in the co-transcribed operon and conserved role across all characterized Rieske benzoate dioxygenases provides strong evidence. **Confidence: high. Status: covered.**

**benC (PP_3163, Q88I38)**: Encodes the electron transfer component (ferredoxin-NADH reductase) that channels electrons from NADH to the BenAB oxygenase. The dual EC assignment (1.14.12.10 for the overall reaction; 1.18.1.3 for the reductase activity) reflects its role within the multi-component system (cowles2000benraxyls pages 4-5, papadopoulou2018metabolicandevolutionary pages 4-6). Co-transcribed with *benA/benB/benD* (cowles2000benraxyls pages 4-5). **Confidence: high. Status: covered.**

**benD (PP_3164, Q88I37)**: Encodes the NAD⁺-dependent *cis*-diol dehydrogenase converting the dihydrodiol to catechol with concomitant CO₂ release. Directly identified as a benzoate-induced protein in KT2440 proteomics, including in cells grown on *p*-hydroxybenzoate (suggesting some cross-induction) (kim2006analysisofaromatic pages 6-7). The enzyme regenerates NADH consumed by BenABC (duuren2011optimizationofpseudomonas pages 15-16). **Confidence: high. Status: covered.**

### 4.2 Non-Core Candidate Genes (Excluded)

**PP_1791 (Q88LY5, aldolase/synthase)**: This gene is annotated from KEGG ppu00621 (degradation of aromatic compounds) rather than the benzoate upper pathway. Its aldolase/synthase annotation is consistent with a meta-cleavage lower pathway role (e.g., 4-hydroxy-2-oxovalerate aldolase in the meta-cleavage route). There is no evidence linking PP_1791 to the benzoate → catechol conversion. **Confidence for this module: low. Status: over-annotation.** This gene should not be used to satisfy this module.

**PP_2504 (Q88JY9, 2-hydroxymuconate tautomerase / 4-oxalocrotonate tautomerase, EC 5.3.2.6)**: EC 5.3.2.6 is exclusively a meta-cleavage pathway enzyme acting downstream of catechol 2,3-dioxygenase. KT2440 has no detectable catechol 2,3-dioxygenase activity under benzoate growth (kim2006analysisofaromatic pages 6-7) and processes catechol via ortho-cleavage (duuren2011optimizationofpseudomonas pages 15-16, cao2008catabolicpathwaysand pages 10-11). The gene may encode a functional tautomerase in another metabolic context, but it has no role in the benzoate upper pathway. **Confidence for this module: low. Status: over-annotation.** This gene should not be used to satisfy this module.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 No Gaps in the Core Module

Both enzymatic steps are fully covered by *benA*, *benB*, *benC*, and *benD*. No missing genes are expected for the biochemical conversion of benzoate to catechol.

### 5.2 Over-Annotations from KEGG Map Context

The inclusion of PP_1791 and PP_2504 as candidates for this module stems from KEGG's broad "Xylene degradation" (ppu00622) and "Benzoate degradation via hydroxylation" (ppu00621) overview maps. These maps conflate the benzoate upper pathway with downstream meta-cleavage routes that are not physiologically relevant in KT2440. This represents a clear case of annotation over-propagation from generic pathway maps to a specific organism that lacks the meta-cleavage route for catechol.

### 5.3 catA2 (PP_3166): A Notable Ambiguity

The *ben* operon in KT2440 uniquely contains a second catechol 1,2-dioxygenase gene (*catA2*/PP_3166) embedded within the *ben* gene cluster. This gene encodes a catechol 1,2-dioxygenase that is functionally redundant with *catA* (on the *cat* operon located ~760 kbp away) (duuren2011optimizationofpseudomonas pages 24-27, duuren2011optimizationofpseudomonas pages 15-16). The expression and physiological role of *catA2* have not been fully confirmed experimentally, though it was shown to be functional in the *catR*-deficient mutant KT2440-JD1, where it enabled conversion of catechol to *cis,cis*-muconate when the *cat* operon was not induced (duuren2011optimizationofpseudomonas pages 24-27). This gene is downstream of the benzoate upper pathway boundary (it acts on catechol, the product of BenD) and should **not** be included in this module, but it is noteworthy for adjacent module curation.

### 5.4 Genomic Organization Note

In KT2440, the extended *ben* region is organized as two probable transcription units: *benABCDK-catA2-benE* and *benF*, with the divergently transcribed regulator *benR* upstream of *benA* (choudhary2017benzoatetransportin pages 4-6). The *catBCA* operon is located ~760 kbp downstream on the complementary strand (choudhary2017benzoatetransportin pages 4-6). This physical separation is important for module boundary definition: the ben and cat operons are regulated independently despite being functionally connected.

## 6. Module and GO-Curation Recommendations

The following table summarizes the module step satisfiability assessment:

| Module Step | Step Description | Expected gene(s) | Status | Evidence strength | Notes |
|---|---|---|---|---|---|
| 1 | Benzoate hydroxylation to cis-dihydrodiol intermediate by benzoate 1,2-dioxygenase | benA (PP_3161), benB (PP_3162), benC (PP_3163) | covered | High, direct in KT2440 | BenA and BenD were detected as benzoate-induced proteins in KT2440 proteomics; benABCD is the chromosomal ben operon under BenR control, and BenABC is the canonical multicomponent dioxygenase for this step (EC 1.14.12.10) (kim2006analysisofaromatic pages 6-7, cowles2000benraxyls pages 4-5, cowles2000benraxyls pages 3-4) |
| 2 | Dehydrogenation of benzoate cis-dihydrodiol to catechol | benD (PP_3164) | covered | High, direct in KT2440 | BenD is the cognate cis-diol dehydrogenase (EC 1.3.1.25) acting immediately downstream of BenABC; proteomics in KT2440 identified BenD under benzoate growth, matching the expected upper-pathway second step (kim2006analysisofaromatic pages 6-7, cowles2000benraxyls pages 4-5, duuren2011optimizationofpseudomonas pages 15-16) |
| Boundary-adjacent downstream element | Catechol ortho-cleavage after the upper pathway product catechol is formed | catA (cat operon), catA2 / PP_3166 (ben operon) | not_expected_in_target_taxon | High for boundary exclusion; medium for catA2 role | This is downstream of the target module, not part of benzoate-to-catechol conversion. KT2440 uses ortho-cleavage natively; catA2 is a second catechol 1,2-dioxygenase encoded in the ben region and may act as a safety valve/redundant downstream function, but it should be kept outside the upper module boundary (duuren2011optimizationofpseudomonas pages 15-16, duuren2011optimizationofpseudomonas pages 24-27) |
| Boundary-adjacent transport | Benzoate uptake and outer-membrane entry associated with benzoate utilization | benK, benE, benF | not_expected_in_target_taxon | Medium | Transport strongly supports pathway operation in KT2440 and the genes are genomically linked to the ben region, but transport is not part of the core biochemical conversion from benzoate to catechol unless the module is intentionally expanded to include uptake (choudhary2017benzoatetransportin pages 4-6, cowles2000benraxyls pages 5-6) |
| Adjacent overview-map/meta-cleavage context | Catechol meta-cleavage/xylene-degradation overview-map functions | PP_2504, PP_1791, other meta-pathway genes | not_expected_in_target_taxon | Medium | These genes belong to adjacent meta-cleavage/xylene-degradation map context rather than the benzoate upper pathway. KT2440 benzoate metabolism showed catechol 1,2-dioxygenase activity and no detectable catechol 2,3-dioxygenase activity under benzoate growth, supporting exclusion from this module (kim2006analysisofaromatic pages 6-7, duuren2011optimizationofpseudomonas pages 15-16) |
| Module boundary check | Whether the current generic module should extend beyond catechol into ortho/meta cleavage | benABCD only for core; cat/pca and meta-cleavage separate | covered | High | For KT2440, the core benzoate upper pathway is satisfiable with benABCD alone. Downstream cat/pca genes are biologically connected but belong to the catechol ortho-cleavage/β-ketoadipate route; meta-cleavage functions should remain separate and not be used to satisfy this module (duuren2011optimizationofpseudomonas pages 15-16, cao2008catabolicpathwaysand pages 10-11, tsipa2015connectingtranscriptionalregulation pages 27-32) |


*Table: This table summarizes whether each expected step of the benzoate upper pathway to catechol is satisfied in Pseudomonas putida KT2440, and distinguishes core covered steps from boundary-adjacent transport and downstream functions that should remain outside the module.*

### 6.1 Module Step Status

- **Step 1 (benzoate hydroxylation)**: **Covered** — *benA*, *benB*, *benC* (PP_3161–PP_3163).
- **Step 2 (dihydrodiol dehydrogenation)**: **Covered** — *benD* (PP_3164).

### 6.2 Candidate Gene Dispositions

- **benA, benB, benC, benD**: Retain as primary genes for this module. High confidence.
- **PP_1791**: Remove from candidate list. This is a meta-cleavage pathway enzyme with no role in the benzoate upper pathway in KT2440.
- **PP_2504**: Remove from candidate list. EC 5.3.2.6 (4-oxalocrotonate tautomerase) is a meta-cleavage enzyme; KT2440 does not use meta-cleavage for catechol derived from benzoate.

### 6.3 Module Boundary Recommendations

The current generic module boundaries (benzoate → catechol) are **correct** for KT2440. No revision is needed. However:

1. The module should be explicitly delimited to exclude *catA2*/PP_3166 and downstream catechol cleavage steps, which belong to a separate ortho-cleavage/β-ketoadipate module.
2. Transport genes (*benK*, *benE*, *benF*) and the regulator (*benR*) are genomically linked and physiologically essential for pathway operation, but they are outside the core biochemical module scope. If a broader "benzoate utilization" module is desired, these should be captured in a separate or expanded module document.
3. The KEGG source map ppu00622 ("Xylene degradation") is too broad for this module. The resolved module should be anchored to the benzoate upper pathway specifically, not the xylene degradation overview.

### 6.4 GO Term Considerations

- GO:0018623 (benzoate 1,2-dioxygenase activity) is appropriate for BenA, BenB, BenC.
- GO:0018580 (1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity) or equivalent is appropriate for BenD.
- No new GO term requests appear to be needed for the core module.

## 7. Genes to Promote to Full Review

1. **benA (PP_3161)**: Recommended for full `fetch-gene` review as the primary catalytic subunit. It has direct proteomic evidence and is the key diagnostic gene for this pathway.
2. **benD (PP_3164)**: Recommended for full review as the sole gene for step 2, with direct proteomic evidence.
3. **catA2 (PP_3166)**: While outside this module's boundary, this gene merits full review in the context of the adjacent catechol ortho-cleavage module, as its expression and physiological role remain partially uncharacterized and it is uniquely present in the KT2440 *ben* locus (duuren2011optimizationofpseudomonas pages 15-16, duuren2011optimizationofpseudomonas pages 24-27).

*benB* and *benC* are high-confidence by operon context but have less individual experimental characterization; they can be reviewed at a lower priority if needed.

## 8. Key References

- **Cowles CE, Nichols NN, Harwood CS** (2000). BenR, a XylS homologue, regulates three different pathways of aromatic acid degradation in *Pseudomonas putida*. *J Bacteriol* 182:6339–6346. doi:10.1128/jb.182.22.6339-6346.2000. [Direct *P. putida* evidence for BenR regulation of *benABC*, characterization of BenK/BenE/BenF] (cowles2000benraxyls pages 4-5, cowles2000benraxyls pages 5-6, cowles2000benraxyls pages 6-7, cowles2000benraxyls pages 3-4).

- **Moreno R, Rojo F** (2008). The target for the *Pseudomonas putida* Crc global regulator in the benzoate degradation pathway is the BenR transcriptional regulator. *J Bacteriol* 190:1539–1545. doi:10.1128/jb.01604-07. [Direct KT2440 evidence for Crc-mediated catabolite repression of *benABCD*] (moreno2008thetargetfor pages 3-4, moreno2008thetargetfor pages 2-2, moreno2008thetargetfor pages 1-2, moreno2008thetargetfor pages 6-7, moreno2008thetargetfor pages 4-5).

- **Kim YH et al.** (2006). Analysis of aromatic catabolic pathways in *Pseudomonas putida* KT2440 using a combined proteomic approach. *Proteomics* 6:1301–1318. doi:10.1002/pmic.200500329. [Direct KT2440 proteomics and enzyme activity data; BenA, BenD identified; catechol 1,2-dioxygenase activity confirmed, no catechol 2,3-dioxygenase detected] (kim2006analysisofaromatic pages 6-7).

- **van Duuren JBJH** (2011). Optimization of *Pseudomonas putida* KT2440 as host for the production of *cis,cis*-muconate from benzoate. PhD thesis, Wageningen University. doi:10.18174/176647. [KT2440-specific pathway diagram, catA2/PP_3166 characterization, ben operon structure] (duuren2011optimizationofpseudomonas pages 24-27, duuren2011optimizationofpseudomonas pages 15-16).

- **Choudhary A, Purohit H, Phale PS** (2017). Benzoate transport in *Pseudomonas putida* CSV86. *FEMS Microbiol Lett* 364:fnx118. doi:10.1093/femsle/fnx118. [Comparative analysis of benzoate transporters in KT2440 and CSV86; ben operon organization] (choudhary2017benzoatetransportin pages 4-6, choudhary2017benzoatetransportin pages 6-8).

- **Moreno R et al.** (2024). Inactivation of *Pseudomonas putida* KT2440 pyruvate dehydrogenase relieves catabolite repression. *Microb Biotechnol* 17:e14514. doi:10.1111/1751-7915.14514. [Recent KT2440 work confirming ben pathway in catabolite repression context].

- **de Lorenzo V, Pérez-Pantoja D, Nikel PI** (2024). *Pseudomonas putida* KT2440: the long journey of a soil-dweller to become a synthetic biology chassis. *J Bacteriol* 206:e00136-24. doi:10.1128/jb.00136-24. [Authoritative 2024 review of KT2440 as model organism for aromatic catabolism].

- **Jiménez JI, Miñambres B, García JL, Díaz E** (2002). Genomic analysis of the aromatic catabolic pathways from *Pseudomonas putida* KT2440. *Environ Microbiol* 4:824–841. doi:10.1046/j.1462-2920.2002.00370.x. [Foundational genomic analysis of aromatic pathways in KT2440; referenced by multiple sources but not directly available for full-text search].

## 9. Evidence and Open Questions

### 9.1 Supported by Direct Experiments in KT2440

- BenA and BenD are benzoate-induced proteins (proteomics) (kim2006analysisofaromatic pages 6-7).
- Catechol 1,2-dioxygenase activity is 1.26 U/mg under benzoate growth; no catechol 2,3-dioxygenase activity detected (kim2006analysisofaromatic pages 6-7).
- BenR activates *benA* promoter ~15-fold in response to benzoate (cowles2000benraxyls pages 3-4).
- Crc represses *benABCD* expression ~70-fold during exponential growth in rich medium by inhibiting BenR translation (moreno2008thetargetfor pages 3-4, moreno2008thetargetfor pages 2-2).
- The benzoate → catechol → *cis,cis*-muconate pathway is functional in KT2440, as demonstrated by muconate production in engineered strains (duuren2011optimizationofpseudomonas pages 15-16).

### 9.2 Inferred from Homology or Operon Context

- BenB and BenC roles are inferred from operon co-transcription with *benA* and conserved function across all characterized Rieske benzoate dioxygenases.
- The precise subunit stoichiometry of the BenABC complex in KT2440 has not been directly determined but is assumed to follow the α₃β₃ oxygenase + reductase architecture typical of class III Rieske dioxygenases.

### 9.3 Open Questions

1. **catA2 (PP_3166) physiological role**: The expression conditions and functional significance of this second catechol 1,2-dioxygenase in wild-type KT2440 remain incompletely characterized (duuren2011optimizationofpseudomonas pages 15-16). Its role as a "safety valve" against catechol accumulation is hypothesized but not directly demonstrated.
2. **BenB/BenC individual contributions**: While essential for complex function, individual subunit characterization (e.g., by single-gene knockouts) has not been explicitly reported for KT2440.
3. **PP_1791 and PP_2504 actual functions**: While excluded from this module, the physiological roles of these annotated meta-cleavage enzymes in KT2440 (an organism without a canonical meta-cleavage pathway) remain unclear. They may be orphan genes, involved in other metabolic contexts, or represent evolutionary relics.

References

1. (kim2006analysisofaromatic pages 6-7): Young Hwan Kim, Kun Cho, Sung‐Ho Yun, Jin Young Kim, Kyung‐Hoon Kwon, Jong Shin Yoo, and Seung Il Kim. Analysis of aromatic catabolic pathways in pseudomonas putida kt 2440 using a combined proteomic approach: 2‐de/ms and cleavable isotope‐coded affinity tag analysis. PROTEOMICS, 6:1301-1318, Feb 2006. URL: https://doi.org/10.1002/pmic.200500329, doi:10.1002/pmic.200500329. This article has 210 citations and is from a peer-reviewed journal.

2. (cowles2000benraxyls pages 4-5): Charles E. Cowles, Nancy N. Nichols, and Caroline S. Harwood. Benr, a xyls homologue, regulates three different pathways of aromatic acid degradation in pseudomonas putida. Journal of Bacteriology, 182:6339-6346, Nov 2000. URL: https://doi.org/10.1128/jb.182.22.6339-6346.2000, doi:10.1128/jb.182.22.6339-6346.2000. This article has 195 citations and is from a peer-reviewed journal.

3. (duuren2011optimizationofpseudomonas pages 15-16): J.B.J.H. van Duuren. Optimization of pseudomonas putida kt2440 as host for the production of cis, cis-muconate from benzoate. ArXiv, 2011. URL: https://doi.org/10.18174/176647, doi:10.18174/176647. This article has 4 citations.

4. (duuren2011optimizationofpseudomonas pages 24-27): J.B.J.H. van Duuren. Optimization of pseudomonas putida kt2440 as host for the production of cis, cis-muconate from benzoate. ArXiv, 2011. URL: https://doi.org/10.18174/176647, doi:10.18174/176647. This article has 4 citations.

5. (choudhary2017benzoatetransportin pages 4-6): Alpa Choudhary, Hemant Purohit, and Prashant S. Phale. Benzoate transport in pseudomonas putida csv86. FEMS Microbiology Letters, 364:fnx118, Jul 2017. URL: https://doi.org/10.1093/femsle/fnx118, doi:10.1093/femsle/fnx118. This article has 46 citations and is from a peer-reviewed journal.

6. (tsipa2015connectingtranscriptionalregulation pages 27-32): Argyro Tsipa. Connecting transcriptional regulation and microbial growth kinetics in cultures of pseudomonas putida. ArXiv, Sep 2015. URL: https://doi.org/10.25560/52631, doi:10.25560/52631. This article has 1 citations.

7. (panke1998engineeringofquasinatural pages 2-3): Sven Panke, Juan M. Sánchez-Romero, and Víctor de Lorenzo. Engineering of quasi-natural pseudomonas putida strains for toluene metabolism through anortho-cleavage degradation pathway. Applied and Environmental Microbiology, 64:748-751, Feb 1998. URL: https://doi.org/10.1128/aem.64.2.748-751.1998, doi:10.1128/aem.64.2.748-751.1998. This article has 84 citations and is from a peer-reviewed journal.

8. (cowles2000benraxyls pages 3-4): Charles E. Cowles, Nancy N. Nichols, and Caroline S. Harwood. Benr, a xyls homologue, regulates three different pathways of aromatic acid degradation in pseudomonas putida. Journal of Bacteriology, 182:6339-6346, Nov 2000. URL: https://doi.org/10.1128/jb.182.22.6339-6346.2000, doi:10.1128/jb.182.22.6339-6346.2000. This article has 195 citations and is from a peer-reviewed journal.

9. (moreno2008thetargetfor pages 1-2): Renata Moreno and Fernando Rojo. The target for the <i>pseudomonas putida</i> crc global regulator in the benzoate degradation pathway is the benr transcriptional regulator. Mar 2008. URL: https://doi.org/10.1128/jb.01604-07, doi:10.1128/jb.01604-07. This article has 122 citations and is from a peer-reviewed journal.

10. (moreno2008thetargetfor pages 2-2): Renata Moreno and Fernando Rojo. The target for the <i>pseudomonas putida</i> crc global regulator in the benzoate degradation pathway is the benr transcriptional regulator. Mar 2008. URL: https://doi.org/10.1128/jb.01604-07, doi:10.1128/jb.01604-07. This article has 122 citations and is from a peer-reviewed journal.

11. (papadopoulou2018metabolicandevolutionary pages 4-6): Evangelia S. Papadopoulou, Chiara Perruchon, Sotirios Vasileiadis, Constantina Rousidou, Georgia Tanou, Martina Samiotaki, Athanassios Molassiotis, and Dimitrios G. Karpouzas. Metabolic and evolutionary insights in the transformation of diphenylamine by a pseudomonas putida strain unravelled by genomic, proteomic, and transcription analysis. Frontiers in Microbiology, Apr 2018. URL: https://doi.org/10.3389/fmicb.2018.00676, doi:10.3389/fmicb.2018.00676. This article has 15 citations and is from a peer-reviewed journal.

12. (cao2008catabolicpathwaysand pages 10-11): Bin Cao and Kai‐Chee Loh. Catabolic pathways and cellular responses of pseudomonas putida p8 during growth on benzoate with a proteomics approach. Biotechnology and Bioengineering, 101:1297-1312, Dec 2008. URL: https://doi.org/10.1002/bit.21997, doi:10.1002/bit.21997. This article has 56 citations and is from a domain leading peer-reviewed journal.

13. (cowles2000benraxyls pages 5-6): Charles E. Cowles, Nancy N. Nichols, and Caroline S. Harwood. Benr, a xyls homologue, regulates three different pathways of aromatic acid degradation in pseudomonas putida. Journal of Bacteriology, 182:6339-6346, Nov 2000. URL: https://doi.org/10.1128/jb.182.22.6339-6346.2000, doi:10.1128/jb.182.22.6339-6346.2000. This article has 195 citations and is from a peer-reviewed journal.

14. (cowles2000benraxyls pages 6-7): Charles E. Cowles, Nancy N. Nichols, and Caroline S. Harwood. Benr, a xyls homologue, regulates three different pathways of aromatic acid degradation in pseudomonas putida. Journal of Bacteriology, 182:6339-6346, Nov 2000. URL: https://doi.org/10.1128/jb.182.22.6339-6346.2000, doi:10.1128/jb.182.22.6339-6346.2000. This article has 195 citations and is from a peer-reviewed journal.

15. (moreno2008thetargetfor pages 3-4): Renata Moreno and Fernando Rojo. The target for the <i>pseudomonas putida</i> crc global regulator in the benzoate degradation pathway is the benr transcriptional regulator. Mar 2008. URL: https://doi.org/10.1128/jb.01604-07, doi:10.1128/jb.01604-07. This article has 122 citations and is from a peer-reviewed journal.

16. (moreno2008thetargetfor pages 6-7): Renata Moreno and Fernando Rojo. The target for the <i>pseudomonas putida</i> crc global regulator in the benzoate degradation pathway is the benr transcriptional regulator. Mar 2008. URL: https://doi.org/10.1128/jb.01604-07, doi:10.1128/jb.01604-07. This article has 122 citations and is from a peer-reviewed journal.

17. (moreno2008thetargetfor pages 4-5): Renata Moreno and Fernando Rojo. The target for the <i>pseudomonas putida</i> crc global regulator in the benzoate degradation pathway is the benr transcriptional regulator. Mar 2008. URL: https://doi.org/10.1128/jb.01604-07, doi:10.1128/jb.01604-07. This article has 122 citations and is from a peer-reviewed journal.

18. (choudhary2017benzoatetransportin pages 6-8): Alpa Choudhary, Hemant Purohit, and Prashant S. Phale. Benzoate transport in pseudomonas putida csv86. FEMS Microbiology Letters, 364:fnx118, Jul 2017. URL: https://doi.org/10.1093/femsle/fnx118, doi:10.1093/femsle/fnx118. This article has 46 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__benzoate_upper_pathway__ppu00622-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__benzoate_upper_pathway__ppu00622-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. kim2006analysisofaromatic pages 6-7
2. duuren2011optimizationofpseudomonas pages 15-16
3. choudhary2017benzoatetransportin pages 4-6
4. cowles2000benraxyls pages 3-4
5. cowles2000benraxyls pages 4-5
6. duuren2011optimizationofpseudomonas pages 24-27
7. tsipa2015connectingtranscriptionalregulation pages 27-32
8. panke1998engineeringofquasinatural pages 2-3
9. moreno2008thetargetfor pages 1-2
10. moreno2008thetargetfor pages 2-2
11. papadopoulou2018metabolicandevolutionary pages 4-6
12. cao2008catabolicpathwaysand pages 10-11
13. cowles2000benraxyls pages 5-6
14. cowles2000benraxyls pages 6-7
15. moreno2008thetargetfor pages 3-4
16. moreno2008thetargetfor pages 6-7
17. moreno2008thetargetfor pages 4-5
18. choudhary2017benzoatetransportin pages 6-8
19. 2Fe-2S
20. Direct *P. putida* evidence for BenR regulation of *benABC*, characterization of BenK/BenE/BenF
21. Direct KT2440 evidence for Crc-mediated catabolite repression of *benABCD*
22. Direct KT2440 proteomics and enzyme activity data; BenA, BenD identified; catechol 1,2-dioxygenase activity confirmed, no catechol 2,3-dioxygenase detected
23. KT2440-specific pathway diagram, catA2/PP_3166 characterization, ben operon structure
24. Comparative analysis of benzoate transporters in KT2440 and CSV86; ben operon organization
25. Recent KT2440 work confirming ben pathway in catabolite repression context
26. Authoritative 2024 review of KT2440 as model organism for aromatic catabolism
27. Foundational genomic analysis of aromatic pathways in KT2440; referenced by multiple sources but not directly available for full-text search
28. https://doi.org/10.1002/pmic.200500329,
29. https://doi.org/10.1128/jb.182.22.6339-6346.2000,
30. https://doi.org/10.18174/176647,
31. https://doi.org/10.1093/femsle/fnx118,
32. https://doi.org/10.25560/52631,
33. https://doi.org/10.1128/aem.64.2.748-751.1998,
34. https://doi.org/10.1128/jb.01604-07,
35. https://doi.org/10.3389/fmicb.2018.00676,
36. https://doi.org/10.1002/bit.21997,