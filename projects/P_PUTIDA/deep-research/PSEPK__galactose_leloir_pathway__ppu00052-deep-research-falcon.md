---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T18:44:08.584214'
end_time: '2026-07-06T19:00:30.522720'
duration_seconds: 981.94
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Galactose catabolism (Leloir pathway)
  module_summary: The Leloir pathway converts D-galactose to glucose-1-phosphate through
    a conserved UDP-sugar cycle, allowing galactose carbon to enter central carbohydrate
    metabolism. In the canonical four-step route, galactose mutarotase (GALM/aldose
    1-epimerase) equilibrates the beta- and alpha-anomers of D-galactose, galactokinase
    (GALK) phosphorylates alpha-D-galactose to alpha-D-galactose 1-phosphate, galactose-1-phosphate
    uridylyltransferase transfers a UMP group from UDP-glucose to produce glucose-1-phosphate
    and UDP-galactose, and UDP-galactose 4-epimerase interconverts UDP-galactose and
    UDP-glucose. The epimerase step regenerates the UDP-glucose co-substrate used
    by the transferase and also links galactose handling to the UDP-galactose pool
    used in cell-surface and glycoconjugate biosynthesis. Some bacteria and individual
    genomes carry only part of this reference route, so organism-level pathway curation
    should distinguish the strict Leloir steps from side nodes such as phosphoglucomutase,
    UDP-glucose pyrophosphorylase, and polysaccharide/nucleotide-sugar metabolism.
  module_outline: "- Galactose catabolism (Leloir pathway)\n  - 1. anomer preparation\
    \ (mutarotation)\n  - beta-D-galactose to alpha-D-galactose\n    - GALM: galactose\
    \ mutarotase / aldose 1-epimerase (molecular player: Aldose 1-epimerase (mutarotase)\
    \ family (GALM); activity or role: aldose 1-epimerase activity)\n  - 2. phosphorylation\
    \ (committed step)\n  - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate\
    \ + ADP\n    - GALK1: galactokinase (molecular player: Galactokinase (GHMP kinase)\
    \ family (GALK1); activity or role: galactokinase activity)\n  - 3. uridylyl transfer\
    \ (central step)\n  - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate\
    \ + UDP-galactose\n    - GALT: galactose-1-phosphate uridylyltransferase (molecular\
    \ player: Galactose-1-phosphate uridylyltransferase family (GALT); activity or\
    \ role: UDP-glucose:hexose-1-phosphate uridylyltransferase activity)\n  - 4. UDP-sugar\
    \ recycling (regenerates UDP-glucose for GALT)\n  - UDP-galactose to UDP-glucose\
    \ (reversible)\n    - GALE: UDP-galactose-4-epimerase (molecular player: UDP-glucose\
    \ 4-epimerase family (GALE); activity or role: UDP-glucose 4-epimerase activity)"
  module_connections: '- beta-D-galactose to alpha-D-galactose feeds into alpha-D-galactose
    + ATP to alpha-D-galactose 1-phosphate + ADP: alpha-D-galactose from GALM is the
    substrate phosphorylated by GALK1.

    - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP feeds into alpha-D-galactose
    1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: alpha-D-galactose
    1-phosphate from GALK1 is the substrate of GALT.

    - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose
    feeds into UDP-galactose to UDP-glucose (reversible): UDP-galactose produced by
    GALT is epimerised by GALE to UDP-glucose.

    - UDP-galactose to UDP-glucose (reversible) feeds into alpha-D-galactose 1-phosphate
    + UDP-glucose to glucose-1-phosphate + UDP-galactose: UDP-glucose regenerated
    by GALE is the co-substrate GALT requires, closing the UDP-sugar recycling loop
    that makes the pathway catalytic in UDP-glucose.'
  pathway_query: ppu00052
  pathway_id: ppu00052
  pathway_name: Galactose metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00052 with 7 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '8'
  candidate_genes: '- PP_0501: PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase
    family protein (primary bucket kegg:ppu00052)

    - glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2;
    primary bucket kegg:ppu00052)

    - PP_1165: PP_1165 | Q88NP2 | Aldose 1-epimerase (primary bucket kegg:ppu00052)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - galE: PP_3129 | Q88I72 | UDP-glucose 4-epimerase (EC 5.1.3.2) (EC 5.1.3.2; primary
    bucket kegg:ppu00052)

    - pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary
    bucket kegg:ppu00052)

    - galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9)
    (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__galactose_leloir_pathway__ppu00052-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__galactose_leloir_pathway__ppu00052-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Galactose catabolism (Leloir pathway) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00052
- Resolved ID: ppu00052
- Resolved name: Galactose metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00052 with 7 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 8

- PP_0501: PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase family protein (primary bucket kegg:ppu00052)
- glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2; primary bucket kegg:ppu00052)
- PP_1165: PP_1165 | Q88NP2 | Aldose 1-epimerase (primary bucket kegg:ppu00052)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- galE: PP_3129 | Q88I72 | UDP-glucose 4-epimerase (EC 5.1.3.2) (EC 5.1.3.2; primary bucket kegg:ppu00052)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

## Generic Module Context

### Working Scope

The Leloir pathway converts D-galactose to glucose-1-phosphate through a conserved UDP-sugar cycle, allowing galactose carbon to enter central carbohydrate metabolism. In the canonical four-step route, galactose mutarotase (GALM/aldose 1-epimerase) equilibrates the beta- and alpha-anomers of D-galactose, galactokinase (GALK) phosphorylates alpha-D-galactose to alpha-D-galactose 1-phosphate, galactose-1-phosphate uridylyltransferase transfers a UMP group from UDP-glucose to produce glucose-1-phosphate and UDP-galactose, and UDP-galactose 4-epimerase interconverts UDP-galactose and UDP-glucose. The epimerase step regenerates the UDP-glucose co-substrate used by the transferase and also links galactose handling to the UDP-galactose pool used in cell-surface and glycoconjugate biosynthesis. Some bacteria and individual genomes carry only part of this reference route, so organism-level pathway curation should distinguish the strict Leloir steps from side nodes such as phosphoglucomutase, UDP-glucose pyrophosphorylase, and polysaccharide/nucleotide-sugar metabolism.

### Provisional Biological Outline

- Galactose catabolism (Leloir pathway)
  - 1. anomer preparation (mutarotation)
  - beta-D-galactose to alpha-D-galactose
    - GALM: galactose mutarotase / aldose 1-epimerase (molecular player: Aldose 1-epimerase (mutarotase) family (GALM); activity or role: aldose 1-epimerase activity)
  - 2. phosphorylation (committed step)
  - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP
    - GALK1: galactokinase (molecular player: Galactokinase (GHMP kinase) family (GALK1); activity or role: galactokinase activity)
  - 3. uridylyl transfer (central step)
  - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose
    - GALT: galactose-1-phosphate uridylyltransferase (molecular player: Galactose-1-phosphate uridylyltransferase family (GALT); activity or role: UDP-glucose:hexose-1-phosphate uridylyltransferase activity)
  - 4. UDP-sugar recycling (regenerates UDP-glucose for GALT)
  - UDP-galactose to UDP-glucose (reversible)
    - GALE: UDP-galactose-4-epimerase (molecular player: UDP-glucose 4-epimerase family (GALE); activity or role: UDP-glucose 4-epimerase activity)

### Known Relationships Among Steps

- beta-D-galactose to alpha-D-galactose feeds into alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP: alpha-D-galactose from GALM is the substrate phosphorylated by GALK1.
- alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: alpha-D-galactose 1-phosphate from GALK1 is the substrate of GALT.
- alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose feeds into UDP-galactose to UDP-glucose (reversible): UDP-galactose produced by GALT is epimerised by GALE to UDP-glucose.
- UDP-galactose to UDP-glucose (reversible) feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: UDP-glucose regenerated by GALE is the co-substrate GALT requires, closing the UDP-sugar recycling loop that makes the pathway catalytic in UDP-glucose.

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

Galactose catabolism (Leloir pathway) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00052
- Resolved ID: ppu00052
- Resolved name: Galactose metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00052 with 7 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 8

- PP_0501: PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase family protein (primary bucket kegg:ppu00052)
- glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2; primary bucket kegg:ppu00052)
- PP_1165: PP_1165 | Q88NP2 | Aldose 1-epimerase (primary bucket kegg:ppu00052)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- galE: PP_3129 | Q88I72 | UDP-glucose 4-epimerase (EC 5.1.3.2) (EC 5.1.3.2; primary bucket kegg:ppu00052)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

## Generic Module Context

### Working Scope

The Leloir pathway converts D-galactose to glucose-1-phosphate through a conserved UDP-sugar cycle, allowing galactose carbon to enter central carbohydrate metabolism. In the canonical four-step route, galactose mutarotase (GALM/aldose 1-epimerase) equilibrates the beta- and alpha-anomers of D-galactose, galactokinase (GALK) phosphorylates alpha-D-galactose to alpha-D-galactose 1-phosphate, galactose-1-phosphate uridylyltransferase transfers a UMP group from UDP-glucose to produce glucose-1-phosphate and UDP-galactose, and UDP-galactose 4-epimerase interconverts UDP-galactose and UDP-glucose. The epimerase step regenerates the UDP-glucose co-substrate used by the transferase and also links galactose handling to the UDP-galactose pool used in cell-surface and glycoconjugate biosynthesis. Some bacteria and individual genomes carry only part of this reference route, so organism-level pathway curation should distinguish the strict Leloir steps from side nodes such as phosphoglucomutase, UDP-glucose pyrophosphorylase, and polysaccharide/nucleotide-sugar metabolism.

### Provisional Biological Outline

- Galactose catabolism (Leloir pathway)
  - 1. anomer preparation (mutarotation)
  - beta-D-galactose to alpha-D-galactose
    - GALM: galactose mutarotase / aldose 1-epimerase (molecular player: Aldose 1-epimerase (mutarotase) family (GALM); activity or role: aldose 1-epimerase activity)
  - 2. phosphorylation (committed step)
  - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP
    - GALK1: galactokinase (molecular player: Galactokinase (GHMP kinase) family (GALK1); activity or role: galactokinase activity)
  - 3. uridylyl transfer (central step)
  - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose
    - GALT: galactose-1-phosphate uridylyltransferase (molecular player: Galactose-1-phosphate uridylyltransferase family (GALT); activity or role: UDP-glucose:hexose-1-phosphate uridylyltransferase activity)
  - 4. UDP-sugar recycling (regenerates UDP-glucose for GALT)
  - UDP-galactose to UDP-glucose (reversible)
    - GALE: UDP-galactose-4-epimerase (molecular player: UDP-glucose 4-epimerase family (GALE); activity or role: UDP-glucose 4-epimerase activity)

### Known Relationships Among Steps

- beta-D-galactose to alpha-D-galactose feeds into alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP: alpha-D-galactose from GALM is the substrate phosphorylated by GALK1.
- alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: alpha-D-galactose 1-phosphate from GALK1 is the substrate of GALT.
- alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose feeds into UDP-galactose to UDP-glucose (reversible): UDP-galactose produced by GALT is epimerised by GALE to UDP-glucose.
- UDP-galactose to UDP-glucose (reversible) feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: UDP-glucose regenerated by GALE is the co-substrate GALT requires, closing the UDP-sugar recycling loop that makes the pathway catalytic in UDP-glucose.

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

# Galactose Catabolism (Leloir Pathway) in *Pseudomonas putida* KT2440: Species-Aware Module Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 **does not possess a functional Leloir pathway for galactose catabolism**. Wild-type KT2440 cannot grow on D-galactose as a sole carbon source (peabody2019engineeredpseudomonasputida pages 1-2, peabody2019engineeredpseudomonasputida pages 2-3). The KEGG pathway ppu00052 ("Galactose metabolism") maps eight candidate genes to this organism, but none of these genes encode the two committed catabolic enzymes of the Leloir pathway: galactokinase (GALK, EC 2.7.1.6) and galactose-1-phosphate uridylyltransferase (GALT, EC 2.7.7.12). Instead, the mapped genes function in glucose catabolism (glk, PP_1165), glycogen metabolism (pgm), and cell-envelope biosynthesis — including alginate, lipopolysaccharide (LPS), and rhamnolipid precursor pathways (algC, galU, galE) (santos2004insightsintothe pages 5-7, santos2004insightsintothe pages 4-5, king2009reviewlipopolysaccharidebiosynthesis pages 13-15, serrato2024bacterialalginatebiosynthesis pages 6-8). The KEGG annotation creates a misleading impression of partial Leloir pathway presence; in reality, the pathway is **not satisfied** in KT2440, and the module boundaries require revision for this taxon.

Two independent metabolic engineering studies confirm the absence of native galactose catabolism. Peabody et al. (2019) installed a heterologous De Ley–Doudoroff (DLD) pathway using *P. fluorescens* SBW25 dgoKAD genes (peabody2019engineeredpseudomonasputida pages 3-5, peabody2019engineeredpseudomonasputida pages 1-2, peabody2019engineeredpseudomonasputida pages 2-3), while Lim et al. (2021) introduced the *E. coli* K-12 MG1655 galETKM operon (encoding galE, galT, galK, and galM) followed by adaptive laboratory evolution (ALE) to achieve functional galactose utilization via the Leloir route (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 12-15, lim2021generationofpseudomonas pages 9-12). Both studies required introduction of heterologous genes because the native genome lacks the critical enzymatic steps.

## 2. Target-Organism Pathway Definition

**Pathway under review:** The canonical Leloir pathway converts D-galactose to glucose-1-phosphate through four enzymatic steps: (1) mutarotation (GALM), (2) phosphorylation (GALK), (3) uridylyl transfer (GALT), and (4) UDP-sugar recycling (GALE).

**Status in KT2440:** The Leloir pathway is not operative as a catabolic route. P. putida KT2440 metabolizes glucose primarily through direct oxidative (periplasmic glucose dehydrogenase Gcd) and phosphorylative (glucokinase Glk) routes feeding the Entner–Doudoroff (ED) pathway (santos2004insightsintothe pages 4-5). The organism's carbon source range does not include galactose, and engineering studies have confirmed that galactose utilization requires introduction of complete heterologous pathways (peabody2019engineeredpseudomonasputida pages 1-2, lim2021generationofpseudomonas pages 1-5).

**Neighboring pathways to keep separate:** The candidate genes belong to several distinct biological processes that should not be conflated with galactose catabolism: (a) upper glucose catabolism via ED pathway (glk, PP_1165); (b) glycogen metabolism (pgm); (c) LPS core oligosaccharide biosynthesis (galU, algC); (d) alginate biosynthesis (algC); (e) UDP-sugar nucleotide metabolism for cell-surface glycoconjugates (galE, cpsG, PP_0501). The KEGG "Galactose metabolism" reference map captures reactions involving galactose-related intermediates (e.g., UDP-galactose, glucose-1-phosphate) regardless of biological context, which causes these cell-envelope and central-metabolism genes to be mapped inappropriately to galactose catabolism.

**Database-specific naming:** KEGG ppu00052 is titled "Galactose metabolism" but functions as a broad overview of reactions involving galactose-related metabolites, not strictly galactose catabolism. This distinction is critical for module satisfiability assessment.

## 3. Expected Step Model

The following table summarizes the status of each canonical Leloir pathway step in *P. putida* KT2440:

| Step Number | Reaction | Required Enzyme | EC Number | KT2440 Gene Present | Module Status | Evidence |
|---|---|---|---|---|---|---|
| 1 | β-D-galactose → α-D-galactose | GALM (aldose 1-epimerase) | 5.1.3.3 | PP_1165 annotated as aldose 1-epimerase, but role in galactose catabolism is unproven and may instead reflect broader aldose/glucose mutarotation | candidate_uncertain | Annotation ambiguity; KT2440 lacks native galactose growth, so PP_1165 cannot be taken as sufficient evidence for a functional Leloir entry step (lim2021generationofpseudomonas pages 1-5, santos2004insightsintothe pages 4-5, lim2021generationofpseudomonas pages 9-12) |
| 2 | α-D-galactose + ATP → α-D-galactose-1-phosphate + ADP | GALK (galactokinase) | 2.7.1.6 | ABSENT | gap | No native galK identified; Lim et al. engineered KT2440 with heterologous *E. coli* galETKM, explicitly including **galK**, to enable Leloir-type galactose utilization (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12) |
| 3 | α-D-galactose-1-phosphate + UDP-glucose → glucose-1-phosphate + UDP-galactose | GALT (galactose-1-phosphate uridylyltransferase) | 2.7.7.12 | ABSENT | gap | No native galT identified; Lim et al. introduced heterologous **galT** as part of *E. coli* galETKM because KT2440 does not natively catabolize galactose (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12) |
| 4 | UDP-galactose ↔ UDP-glucose | GALE (UDP-glucose 4-epimerase) | 5.1.3.2 | PP_3129 (**galE**) present | not_expected_in_target_taxon | Although **galE** is present, KT2440 lacks the upstream committed Leloir steps and native galactose growth; the most plausible role is UDP-sugar/cell-envelope metabolism rather than catabolic Leloir recycling (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12, king2009reviewlipopolysaccharidebiosynthesis pages 13-15) |
| Overall pathway status | Canonical Leloir pathway in *Pseudomonas putida* KT2440 | — | — | Not satisfied | NOT SATISFIED | The two committed catabolic steps, **GALK** and **GALT**, are absent from the genome; wild-type KT2440 does not natively grow on galactose, and both DLD- and Leloir-based galactose utilization required heterologous pathway installation in engineering studies (peabody2019engineeredpseudomonasputida pages 1-2, lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12) |


*Table: This table summarizes the four canonical Leloir pathway steps and evaluates whether each is encoded and biologically supported in *Pseudomonas putida* KT2440. It is useful for module curation because it shows that the pathway is not satisfied despite the presence of some overlapping UDP-sugar and mutarotase annotations.*

## 4. Candidate Genes and Evidence

The eight candidate genes from KEGG ppu00052 metadata are assessed individually below, with evidence type and curation recommendations:

| Gene (locus tag) | Gene Name | EC Number | Proposed Leloir Step | Actual Biological Role in KT2440 | Evidence Type | Confidence Level | Curation Recommendation |
|---|---|---|---|---|---|---|---|
| PP_0501 | NAD-dependent epimerase/dehydratase family protein | Unclear / broad family assignment | Sometimes over-mapped to UDP-sugar epimerization side chemistry | Likely general sugar-nucleotide or carbohydrate-modifying enzyme; no direct evidence for galactose catabolism or any canonical Leloir step in KT2440 | Inference from broad family annotation; absence of supporting physiological evidence for native galactose use in KT2440 (peabody2019engineeredpseudomonasputida pages 1-2, peabody2019engineeredpseudomonasputida pages 2-3, lim2021generationofpseudomonas pages 9-12) | Low | Keep as candidate_uncertain outside strict Leloir module; likely annotation over-propagation; promote only if synteny/biochemistry suggests a specific UDP-sugar role |
| glk (PP_1011) | Glucokinase | EC 2.7.1.2 | Misassigned as galactose phosphorylation analog of GALK | Cytosolic glucose kinase in the phosphorylative glucose route; clustered with edd and upper glucose catabolic genes, supporting glucose-to-G6P metabolism rather than galactose-1-phosphate formation (santos2004insightsintothe pages 4-5) | Direct genome/context evidence in KT2440; physiological literature on glucose catabolism (santos2004insightsintothe pages 4-5) | High | Remove from strict Leloir coverage; mark misplaced in galactose module |
| PP_1165 | Aldose 1-epimerase | EC 5.1.3.3 | Galactose mutarotation (GALM) | Best interpreted as an aldose mutarotase supporting upper sugar/glucose handling in KT2440; GALM-like annotation is ambiguous, but KT2440 still lacks native galactose catabolism and required downstream Leloir enzymes (santos2004insightsintothe pages 4-5, lim2021generationofpseudomonas pages 9-12) | Annotation plus indirect physiological/genetic evidence from absence of native galactose growth and need for heterologous galETKM (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12) | Medium | Keep only as ambiguous mutarotase candidate; do not count as pathway-satisfying GALM for galactose catabolism without direct biochemical evidence |
| cpsG (PP_1777) | Phosphomannomutase | EC 5.4.2.8 | None in core Leloir; side node sometimes linked through sugar-nucleotide metabolism | Mannose/phosphosugar interconversion for polysaccharide and cell-envelope precursor metabolism, not galactose catabolism | Functional inference from enzyme class and pathway context; no evidence tying it to native galactose growth in KT2440 (peabody2019engineeredpseudomonasputida pages 1-2, lim2021generationofpseudomonas pages 9-12) | Medium | Treat as side node; exclude from strict Leloir module |
| galE (PP_3129) | UDP-glucose 4-epimerase | EC 5.1.3.2 | UDP-galactose ↔ UDP-glucose epimerization (GALE) | UDP-sugar interconversion likely used for LPS/EPS/cell-surface carbohydrate biosynthesis; although biochemically GALE-like, KT2440 lacks the core catabolic entry enzymes galK and galT, so this does not establish a functional Leloir catabolic cycle (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12, king2009reviewlipopolysaccharidebiosynthesis pages 13-15) | Strong indirect evidence: heterologous galETKM was required to build Leloir pathway in KT2440; comparative Pseudomonas UDP-sugar/LPS literature (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12, king2009reviewlipopolysaccharidebiosynthesis pages 13-15) | High | Retain as bona fide GALE/UDP-sugar gene, but annotate as cell-surface/UDP-sugar metabolism rather than galactose catabolic recycling |
| pgm (PP_3578) | Phosphoglucomutase | EC 5.4.2.2 | Downstream side node from glucose-1-phosphate | Phosphoglucomutase associated with glycogen/carbohydrate metabolism; not part of the defining Leloir core and not evidence for galactose catabolism in KT2440 (santos2004insightsintothe pages 5-7) | Direct genome-context evidence in KT2440 showing pgm outside glycogen cluster but clearly assigned to phosphoglucomutase function (santos2004insightsintothe pages 5-7) | High | Treat as side node only; exclude from module satisfiability |
| galU (PP_3821) | UTP--glucose-1-phosphate uridylyltransferase | EC 2.7.7.9 | Side node supplying UDP-glucose | UDP-glucose pyrophosphorylase for LPS core and other UDP-glucose-dependent envelope/glycoconjugate pathways; not the galactose-1-phosphate uridylyltransferase (GALT) step of the Leloir pathway (king2009reviewlipopolysaccharidebiosynthesis pages 13-15) | Comparative functional evidence from Pseudomonas LPS biosynthesis and distinction from missing galT in KT2440 (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12, king2009reviewlipopolysaccharidebiosynthesis pages 13-15) | High | Keep as side node; explicitly distinguish from GALT to avoid over-annotation |
| algC (PP_5288) | Phosphomannomutase/phosphoglucomutase | EC 5.4.2.2 / 5.4.2.8 | Side node sometimes linked through Glc1P/Man1P metabolism | Bifunctional PMM/PGM supporting alginate, LPS, and related exopolysaccharide/rhamnolipid precursor metabolism; conserved Pseudomonas envelope-biosynthesis role, not galactose catabolism (muhammadi2007geneticsofbacterial pages 4-5, king2009reviewlipopolysaccharidebiosynthesis pages 13-15, serrato2024bacterialalginatebiosynthesis pages 6-8) | Strong comparative evidence across Pseudomonas/Azotobacter lineages; consistent with absence of native galactose pathway in KT2440 (peabody2019engineeredpseudomonasputida pages 1-2, lim2021generationofpseudomonas pages 9-12) | High | Treat as side node for cell-envelope polysaccharide biosynthesis; exclude from strict Leloir coverage |
| — | **Missing core enzymes** | **GALK: EC 2.7.1.6; GALT: EC 2.7.7.12** | **Core Leloir committed and uridylyltransfer steps** | **Native KT2440 lacks galactokinase and galactose-1-phosphate uridylyltransferase; heterologous galETKM from E. coli had to be introduced to construct a Leloir pathway, and wild-type KT2440 does not natively grow on galactose** (peabody2019engineeredpseudomonasputida pages 1-2, lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12) | Direct experimental evidence from engineering studies in KT2440 (peabody2019engineeredpseudomonasputida pages 1-2, lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12) | **Very high** | **Mark core Leloir pathway as gap/not satisfied in KT2440; revise KEGG-derived module boundaries accordingly** |


*Table: This table evaluates the eight KEGG ppu00052 candidate genes against the strict Leloir pathway in Pseudomonas putida KT2440. It highlights that none of the listed genes establish native galactose catabolism, because the core galK and galT steps are absent and the mapped genes mainly belong to glucose, glycogen, or cell-envelope UDP-sugar metabolism.*

### Detailed Gene Assessments

**PP_0501 (NAD-dependent epimerase/dehydratase family protein):** This gene belongs to a large enzyme superfamily with broad substrate specificity. No experimental data link it to galactose catabolism in KT2440. Its annotation to galactose metabolism likely results from over-propagation of family-level EC assignments. The actual biological role is uncertain but most likely relates to general nucleotide-sugar or carbohydrate modification.

**glk / PP_1011 (Glucokinase, EC 2.7.1.2):** This gene encodes the well-characterized cytosolic glucokinase that phosphorylates glucose to glucose-6-phosphate as part of the phosphorylative glucose uptake route in KT2440 (santos2004insightsintothe pages 4-5). It is clustered with edd (6-phosphogluconate dehydratase, PP_1010), the response regulator gltR (PP_1012), and the sugar ABC transport system gct (santos2004insightsintothe pages 4-5). Glucokinase has no known activity on galactose and is clearly part of glucose metabolism, not galactose catabolism. Its presence in KEGG ppu00052 reflects EC-number mapping to the broad "hexose kinase" node in the galactose metabolism reference map.

**PP_1165 (Aldose 1-epimerase):** This gene is annotated as an aldose 1-epimerase (galM family), which catalyzes mutarotation between alpha and beta anomers of aldoses. In KT2440, Santos et al. (2004) describe this gene in the context of glucose metabolism pathways, where it assists in equilibrating glucose anomers for efficient entry into the phosphorylative ED pathway (santos2004insightsintothe pages 4-5). While aldose 1-epimerases can in principle act on galactose, the absence of downstream Leloir enzymes (GALK, GALT) means this activity has no catabolic relevance for galactose in KT2440. Notably, when Lim et al. (2021) engineered the Leloir pathway in KT2440, they included galM from *E. coli* as part of the galETKM operon, suggesting the native PP_1165 was either insufficient or not recognized as functionally equivalent for galactose mutarotation (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12).

**cpsG / PP_1777 (Phosphomannomutase, EC 5.4.2.8):** This gene encodes a phosphomannomutase that interconverts mannose-6-phosphate and mannose-1-phosphate. Its primary role is in providing precursors for polysaccharide biosynthesis (capsular polysaccharide, LPS). It is a side node in the KEGG galactose map and has no direct role in galactose catabolism.

**galE / PP_3129 (UDP-glucose 4-epimerase, EC 5.1.3.2):** This is a genuine galE ortholog encoding UDP-glucose 4-epimerase activity. However, in KT2440, this enzyme functions in UDP-sugar interconversion for cell-envelope biosynthesis (LPS, exopolysaccharides) rather than as the recycling step of a Leloir catabolic cycle (king2009reviewlipopolysaccharidebiosynthesis pages 13-15). The enzyme is essential for interconverting UDP-glucose and UDP-galactose for glycoconjugate assembly, a biosynthetic (anabolic) role shared across Gram-negative bacteria regardless of galactose catabolic capacity. In the LPS biosynthetic context in *Pseudomonas aeruginosa*, this enzyme provides UDP-galactose for O-antigen synthesis (king2009reviewlipopolysaccharidebiosynthesis pages 13-15). The presence of galE alone does not establish a functional Leloir pathway.

**pgm / PP_3578 (Phosphoglucomutase, EC 5.4.2.2):** This gene encodes phosphoglucomutase, which interconverts glucose-1-phosphate and glucose-6-phosphate. In KT2440, pgm is located near genes involved in glycogen metabolism but outside the main glycogen cluster (santos2004insightsintothe pages 5-7). Its role is in glycogen turnover and general hexose-phosphate interconversion, serving as a housekeeping metabolic enzyme. It is a side node in the galactose metabolism map and has no specific role in galactose catabolism.

**galU / PP_3821 (UTP–glucose-1-phosphate uridylyltransferase, EC 2.7.7.9):** GalU synthesizes UDP-glucose from glucose-1-phosphate and UTP. In *P. aeruginosa*, a galU mutant showed truncated LPS core lacking glucose and rhamnose residues (king2009reviewlipopolysaccharidebiosynthesis pages 13-15). This enzyme is essential for LPS core biosynthesis and rhamnolipid precursor supply. It is distinct from GALT (galactose-1-phosphate uridylyltransferase, EC 2.7.7.12), which catalyzes the exchange reaction central to the Leloir cycle. The galU/GALT confusion is a common source of annotation over-propagation.

**algC / PP_5288 (Phosphomannomutase/phosphoglucomutase, EC 5.4.2.2 and 5.4.2.8):** AlgC is a well-characterized bifunctional enzyme with both phosphomannomutase (PMM) and phosphoglucomutase (PGM) activities (muhammadi2007geneticsofbacterial pages 4-5, serrato2024bacterialalginatebiosynthesis pages 6-8). In Pseudomonas species, AlgC is a key node linking central carbon metabolism to alginate biosynthesis (through mannose-6-phosphate → mannose-1-phosphate conversion), LPS core assembly (through glucose-6-phosphate → glucose-1-phosphate), and rhamnolipid biosynthesis (king2009reviewlipopolysaccharidebiosynthesis pages 13-15, serrato2024bacterialalginatebiosynthesis pages 6-8). Its dual activity makes it appear in multiple KEGG pathway maps, but its primary biological context is cell-envelope polysaccharide precursor supply, not galactose catabolism.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### Critical Gaps

The **two defining catabolic steps** of the Leloir pathway are absent from the KT2440 genome:
- **Galactokinase (GALK, EC 2.7.1.6):** No gene encoding this activity has been identified. Lim et al. (2021) explicitly introduced galK from *E. coli* K-12 MG1655 to construct a functional Leloir pathway (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12).
- **Galactose-1-phosphate uridylyltransferase (GALT, EC 2.7.7.12):** No gene encoding this activity has been identified. Lim et al. (2021) introduced galT from *E. coli* as part of the same engineering effort (lim2021generationofpseudomonas pages 1-5, lim2021generationofpseudomonas pages 9-12).

### Over-Annotations and Ambiguities

1. **KEGG ppu00052 creates a false impression** of partial galactose metabolism by mapping housekeeping enzymes (PGM, UDP-glucose pyrophosphorylase, epimerase) that happen to handle metabolites shared with the galactose map. These enzymes function in LPS, alginate, glycogen, and central glucose metabolism.

2. **galU (PP_3821) vs. galT confusion:** GalU (EC 2.7.7.9) and GALT (EC 2.7.7.12) catalyze chemically distinct reactions. GalU synthesizes UDP-glucose de novo; GALT exchanges UMP between UDP-glucose and galactose-1-phosphate. These must not be conflated in module curation.

3. **PP_1165 (aldose 1-epimerase) ambiguity:** While this gene could theoretically catalyze galactose mutarotation, its biological context in KT2440 is glucose handling. The Lim et al. (2021) study included heterologous galM from *E. coli*, suggesting PP_1165 was not considered functionally equivalent for the Leloir pathway (lim2021generationofpseudomonas pages 1-5).

4. **Native periplasmic galactose oxidation:** The broad-substrate glucose dehydrogenase Gcd (PP_1444) can oxidize galactose to galactonate in the periplasm (peabody2019engineeredpseudomonasputida pages 2-3, nguyen2021theanoxicelectrode‐driven pages 5-7). However, this activity does not support growth and represents promiscuous side activity, not a dedicated galactose catabolic pathway. Peabody et al. (2019) exploited this activity by introducing only the dgoKAD galactonate catabolic genes, but noted that growth was very slow without additional engineering of dedicated transport and galactose-to-galactonate conversion genes (peabody2019engineeredpseudomonasputida pages 3-5, peabody2019engineeredpseudomonasputida pages 2-3).

### Organism Context: Galactose Metabolism in Pseudomonas

*P. putida* KT2440 is representative of many fluorescent pseudomonads that lack native galactose catabolism. When pseudomonads do catabolize galactose, they typically use the oxidative De Ley–Doudoroff (DLD) pathway rather than the Leloir pathway, as the DLD route produces the same intermediates (glyceraldehyde-3-phosphate and pyruvate) as the Entner–Doudoroff glucose pathway natively used by these organisms (peabody2019engineeredpseudomonasputida pages 1-2, peabody2019engineeredpseudomonasputida pages 2-3). Some pseudomonads (e.g., *P. fluorescens* SBW25) carry dgoKAD genes for galactonate catabolism, but KT2440 does not (peabody2019engineeredpseudomonasputida pages 3-5, peabody2019engineeredpseudomonasputida pages 2-3).

## 6. Module and GO-Curation Recommendations

### Module Satisfiability Verdict

| Step | Status |
|------|--------|
| Step 1: Mutarotation (GALM) | **candidate_uncertain** — PP_1165 is annotated but biologically ambiguous for galactose |
| Step 2: Phosphorylation (GALK) | **gap** — gene absent from genome |
| Step 3: Uridylyl transfer (GALT) | **gap** — gene absent from genome |
| Step 4: UDP-sugar recycling (GALE) | **not_expected_in_target_taxon** (for catabolic role) — galE is present but serves cell-envelope biosynthesis |
| Overall Leloir catabolic module | **NOT SATISFIED** |

### Recommendations

1. **Mark the Leloir galactose catabolism module as not_expected_in_target_taxon** for *P. putida* KT2440. The organism does not natively catabolize galactose via any pathway (Leloir or DLD), and the two committed Leloir steps (GALK, GALT) are genuinely absent from the genome.

2. **Reclassify the eight candidate genes** out of the galactose catabolism module. Assign them to their proper functional contexts:
   - glk → glucose catabolism (ED pathway)
   - PP_1165 → aldose mutarotation (glucose handling)
   - galE, galU, algC → cell-envelope polysaccharide/LPS/alginate biosynthesis
   - pgm → glycogen/central carbohydrate metabolism
   - cpsG → polysaccharide biosynthesis (phosphomannomutase)
   - PP_0501 → general UDP-sugar/nucleotide-sugar metabolism

3. **Revise KEGG-derived module boundaries** for this taxon. The ppu00052 map should be annotated to distinguish between "galactose metabolism — reference reactions present as side nodes in other pathways" and "galactose catabolism — not present."

4. **No new GO term requests** are needed, but existing GO annotations should be reviewed to ensure that galE (PP_3129), galU (PP_3821), and algC (PP_5288) are annotated with appropriate biological process terms (LPS biosynthesis, alginate biosynthesis, exopolysaccharide metabolism) rather than "galactose catabolic process."

## 7. Genes to Promote to Full Review

1. **galE (PP_3129):** Merits full review to clarify its role in LPS O-antigen and exopolysaccharide assembly in KT2440. The enzyme is genuinely important for cell-envelope biology but should be curated away from galactose catabolism.

2. **algC (PP_5288):** A well-studied gene in *P. aeruginosa* with clear relevance to alginate and LPS biosynthesis (muhammadi2007geneticsofbacterial pages 4-5, king2009reviewlipopolysaccharidebiosynthesis pages 13-15, serrato2024bacterialalginatebiosynthesis pages 6-8). A full review in the KT2440 context would benefit alginate/LPS module curation.

3. **galU (PP_3821):** Essential for LPS core biosynthesis across *Pseudomonas* species (king2009reviewlipopolysaccharidebiosynthesis pages 13-15). Full review recommended for the nucleotide-sugar/LPS module.

4. **PP_1165 (aldose 1-epimerase):** Warrants biochemical characterization to determine substrate specificity (glucose vs. galactose vs. broad aldose) and clarify whether it should be annotated as galM.

## 8. Key References

- Peabody GL, Elmore JR, Martinez-Baird J, Guss AM. Engineered *Pseudomonas putida* KT2440 co-utilizes galactose and glucose. *Biotechnology for Biofuels* 12:295 (2019). DOI: 10.1186/s13068-019-1627-0 — Direct evidence that wild-type KT2440 does not grow on galactose; engineering of DLD pathway.

- Lim HG, Eng T, Banerjee D, et al. Generation of *Pseudomonas putida* KT2440 strains with efficient utilization of xylose and galactose via adaptive laboratory evolution. *ACS Sustainable Chemistry & Engineering* 9:11512–11523 (2021). DOI: 10.1021/acssuschemeng.1c03765 — Introduction of heterologous *E. coli* galETKM Leloir genes; ALE optimization; identification of gtsABCD transporter mutations as galactose uptake bottleneck.

- Santos VAPM dos, Heim S, Moore ERB, Strätz M, Timmis KN. Insights into the genomic basis of niche specificity of *Pseudomonas putida* KT2440. *Environmental Microbiology* 6(12):1264–1286 (2004). DOI: 10.1111/j.1462-2920.2004.00734.x — Comprehensive genome analysis describing glucose metabolism including glk, pgm, and aldose 1-epimerase roles.

- King JD, Kocíncová D, Westman EL, Lam JS. Review: Lipopolysaccharide biosynthesis in *Pseudomonas aeruginosa*. *Innate Immunity* 15:261–312 (2009). DOI: 10.1177/1753425909106436 — AlgC and GalU roles in LPS core biosynthesis.

- Serrato RV. Bacterial alginate biosynthesis and metabolism. *Biochemistry* (2024). DOI: 10.5772/intechopen.109295 — AlgC function in alginate precursor synthesis.

- Muhammadi, Ahmed N. Genetics of bacterial alginate: alginate genes distribution, organization and biosynthesis in bacteria. *Current Genomics* 8:191–202 (2007). DOI: 10.2174/138920207780833810 — AlgC bifunctional enzyme characterization.

- Nguyen AV, Lai B, Adrian L, Krömer JO. The anoxic electrode-driven fructose catabolism of *Pseudomonas putida* KT2440. *Microbial Biotechnology* 14:1784–1796 (2021). DOI: 10.1111/1751-7915.13862 — Gcd broad substrate range including galactose oxidation.

- Nogales J, Mueller J, Gudmundsson S, et al. High-quality genome-scale metabolic modelling of *Pseudomonas putida* highlights its broad metabolic capabilities. *Environmental Microbiology* 22:255–269 (2020). DOI: 10.1111/1462-2920.14843 — iJN1462 metabolic model confirming carbon source range.

References

1. (peabody2019engineeredpseudomonasputida pages 1-2): George L. Peabody, Joshua R. Elmore, Jessica Martinez-Baird, and Adam M. Guss. Engineered pseudomonas putida kt2440 co-utilizes galactose and glucose. Biotechnology for Biofuels, Dec 2019. URL: https://doi.org/10.1186/s13068-019-1627-0, doi:10.1186/s13068-019-1627-0. This article has 32 citations.

2. (peabody2019engineeredpseudomonasputida pages 2-3): George L. Peabody, Joshua R. Elmore, Jessica Martinez-Baird, and Adam M. Guss. Engineered pseudomonas putida kt2440 co-utilizes galactose and glucose. Biotechnology for Biofuels, Dec 2019. URL: https://doi.org/10.1186/s13068-019-1627-0, doi:10.1186/s13068-019-1627-0. This article has 32 citations.

3. (santos2004insightsintothe pages 5-7): V. A. P. Martins Dos Santos, S. Heim, E. R. B. Moore, M. Strätz, and K. N. Timmis. Insights into the genomic basis of niche specificity of pseudomonas putida kt2440. Environmental microbiology, 6 12:1264-86, Dec 2004. URL: https://doi.org/10.1111/j.1462-2920.2004.00734.x, doi:10.1111/j.1462-2920.2004.00734.x. This article has 343 citations and is from a domain leading peer-reviewed journal.

4. (santos2004insightsintothe pages 4-5): V. A. P. Martins Dos Santos, S. Heim, E. R. B. Moore, M. Strätz, and K. N. Timmis. Insights into the genomic basis of niche specificity of pseudomonas putida kt2440. Environmental microbiology, 6 12:1264-86, Dec 2004. URL: https://doi.org/10.1111/j.1462-2920.2004.00734.x, doi:10.1111/j.1462-2920.2004.00734.x. This article has 343 citations and is from a domain leading peer-reviewed journal.

5. (king2009reviewlipopolysaccharidebiosynthesis pages 13-15): Jerry D. King, Dana Kocíncová, Erin L. Westman, and Joseph S. Lam. Review: lipopolysaccharide biosynthesis in pseudomonas aeruginosa. Innate Immunity, 15:261-312, Aug 2009. URL: https://doi.org/10.1177/1753425909106436, doi:10.1177/1753425909106436. This article has 451 citations and is from a peer-reviewed journal.

6. (serrato2024bacterialalginatebiosynthesis pages 6-8): Rodrigo Vassoler Serrato. Bacterial alginate biosynthesis and metabolism. Biochemistry, May 2024. URL: https://doi.org/10.5772/intechopen.109295, doi:10.5772/intechopen.109295. This article has 6 citations and is from a peer-reviewed journal.

7. (peabody2019engineeredpseudomonasputida pages 3-5): George L. Peabody, Joshua R. Elmore, Jessica Martinez-Baird, and Adam M. Guss. Engineered pseudomonas putida kt2440 co-utilizes galactose and glucose. Biotechnology for Biofuels, Dec 2019. URL: https://doi.org/10.1186/s13068-019-1627-0, doi:10.1186/s13068-019-1627-0. This article has 32 citations.

8. (lim2021generationofpseudomonas pages 1-5): Hyun Gyu Lim, Thomas Eng, Deepanwita Banerjee, Geovanni Alarcon, Andrew K. Lau, Mee-Rye Park, Blake A. Simmons, Bernhard O. Palsson, Steven W. Singer, Aindrila Mukhopadhyay, and Adam M. Feist. Generation of pseudomonas putida kt2440 strains with efficient utilization of xylose and galactose via adaptive laboratory evolution. ACS Sustainable Chemistry & Engineering, 9:11512-11523, Aug 2021. URL: https://doi.org/10.1021/acssuschemeng.1c03765, doi:10.1021/acssuschemeng.1c03765. This article has 59 citations and is from a peer-reviewed journal.

9. (lim2021generationofpseudomonas pages 12-15): Hyun Gyu Lim, Thomas Eng, Deepanwita Banerjee, Geovanni Alarcon, Andrew K. Lau, Mee-Rye Park, Blake A. Simmons, Bernhard O. Palsson, Steven W. Singer, Aindrila Mukhopadhyay, and Adam M. Feist. Generation of pseudomonas putida kt2440 strains with efficient utilization of xylose and galactose via adaptive laboratory evolution. ACS Sustainable Chemistry & Engineering, 9:11512-11523, Aug 2021. URL: https://doi.org/10.1021/acssuschemeng.1c03765, doi:10.1021/acssuschemeng.1c03765. This article has 59 citations and is from a peer-reviewed journal.

10. (lim2021generationofpseudomonas pages 9-12): Hyun Gyu Lim, Thomas Eng, Deepanwita Banerjee, Geovanni Alarcon, Andrew K. Lau, Mee-Rye Park, Blake A. Simmons, Bernhard O. Palsson, Steven W. Singer, Aindrila Mukhopadhyay, and Adam M. Feist. Generation of pseudomonas putida kt2440 strains with efficient utilization of xylose and galactose via adaptive laboratory evolution. ACS Sustainable Chemistry & Engineering, 9:11512-11523, Aug 2021. URL: https://doi.org/10.1021/acssuschemeng.1c03765, doi:10.1021/acssuschemeng.1c03765. This article has 59 citations and is from a peer-reviewed journal.

11. (muhammadi2007geneticsofbacterial pages 4-5): Muhammadi and Nuzhat Ahmed. Genetics of bacterial alginate: alginate genes distribution, organization and biosynthesis in bacteria. Current Genomics, 8:191-202, May 2007. URL: https://doi.org/10.2174/138920207780833810, doi:10.2174/138920207780833810. This article has 80 citations and is from a peer-reviewed journal.

12. (nguyen2021theanoxicelectrode‐driven pages 5-7): Anh Vu Nguyen, Bin Lai, Lorenz Adrian, and Jens O. Krömer. The anoxic electrode‐driven fructose catabolism of pseudomonas putida kt2440. Microbial Biotechnology, 14:1784-1796, Jun 2021. URL: https://doi.org/10.1111/1751-7915.13862, doi:10.1111/1751-7915.13862. This article has 13 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__galactose_leloir_pathway__ppu00052-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__galactose_leloir_pathway__ppu00052-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. santos2004insightsintothe pages 4-5
2. santos2004insightsintothe pages 5-7
3. king2009reviewlipopolysaccharidebiosynthesis pages 13-15
4. lim2021generationofpseudomonas pages 1-5
5. peabody2019engineeredpseudomonasputida pages 1-2
6. peabody2019engineeredpseudomonasputida pages 2-3
7. serrato2024bacterialalginatebiosynthesis pages 6-8
8. peabody2019engineeredpseudomonasputida pages 3-5
9. lim2021generationofpseudomonas pages 12-15
10. lim2021generationofpseudomonas pages 9-12
11. muhammadi2007geneticsofbacterial pages 4-5
12. https://doi.org/10.1186/s13068-019-1627-0,
13. https://doi.org/10.1111/j.1462-2920.2004.00734.x,
14. https://doi.org/10.1177/1753425909106436,
15. https://doi.org/10.5772/intechopen.109295,
16. https://doi.org/10.1021/acssuschemeng.1c03765,
17. https://doi.org/10.2174/138920207780833810,
18. https://doi.org/10.1111/1751-7915.13862,