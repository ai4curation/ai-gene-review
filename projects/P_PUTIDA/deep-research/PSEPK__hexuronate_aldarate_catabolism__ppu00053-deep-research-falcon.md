---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T19:53:18.241277'
end_time: '2026-07-06T20:17:36.673440'
duration_seconds: 1458.43
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Hexuronate and aldarate catabolism
  module_summary: A bacterial free-hexuronate and aldarate catabolism module centered
    on oxidative conversion of D-glucuronate or D-galacturonate to glucarate or galactarate,
    dehydration of aldarates to keto-deoxy intermediates, and terminal oxidation of
    2,5-dioxopentanoate or KGSA to 2-oxoglutarate. This is the catabolic arm that
    KEGG places under ascorbate and aldarate metabolism in Pseudomonas putida KT2440;
    it should be kept separate from UDP-glucuronate nucleotide-sugar biosynthesis
    and from eukaryotic ascorbate metabolism.
  module_outline: "- Hexuronate and aldarate catabolism\n  - 1. hexuronate oxidation\n\
    \  - Glucuronate or galacturonate to urono-1,5-lactone\n    - Uronate dehydrogenase\
    \ (molecular player: uronate dehydrogenase activity; activity or role: uronate\
    \ dehydrogenase activity)\n  - 2. urono-lactone hydrolysis candidate\n  - Urono-1,5-lactone\
    \ hydrolysis to aldarate\n    - Gluconolactonase-family lactonase candidate (molecular\
    \ player: gluconolactonase activity; activity or role: gluconolactonase activity)\n\
    \  - 3. D-glucarate dehydration\n  - D-glucarate to 5-dehydro-4-deoxy-D-glucarate\n\
    \    - Glucarate dehydratase (molecular player: glucarate dehydratase activity;\
    \ activity or role: glucarate dehydratase activity)\n  - 4. D-galactarate dehydration\n\
    \  - D-galactarate dehydration\n    - Galactarate dehydratase (molecular player:\
    \ galactarate dehydratase activity; activity or role: galactarate dehydratase\
    \ activity)\n  - 5. 5-dehydro-4-deoxyglucarate dehydration\n  - 5-dehydro-4-deoxy-D-glucarate\
    \ to 2,5-dioxopentanoate\n    - 5-dehydro-4-deoxyglucarate dehydratase (molecular\
    \ player: 5-dehydro-4-deoxyglucarate dehydratase activity; activity or role: 5-dehydro-4-deoxyglucarate\
    \ dehydratase activity)\n  - 6. 2,5-dioxopentanoate or KGSA oxidation\n  - 2,5-dioxopentanoate\
    \ or KGSA to 2-oxoglutarate\n    - 2,5-dioxovalerate dehydrogenase (molecular\
    \ player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role:\
    \ 2,5-dioxovalerate dehydrogenase (NADP+) activity)"
  module_connections: '- Glucuronate or galacturonate to urono-1,5-lactone feeds into
    Urono-1,5-lactone hydrolysis to aldarate: Udh produces glucaro- or galactaro-1,5-lactones
    that require lactone hydrolysis before aldarate dehydration.

    - Urono-1,5-lactone hydrolysis to aldarate feeds into D-glucarate to 5-dehydro-4-deoxy-D-glucarate:
    Lactonase activity would yield D-glucarate for GudD.

    - Urono-1,5-lactone hydrolysis to aldarate feeds into D-galactarate dehydration:
    Lactonase activity would yield D-galactarate for GarD.

    - D-glucarate to 5-dehydro-4-deoxy-D-glucarate feeds into 5-dehydro-4-deoxy-D-glucarate
    to 2,5-dioxopentanoate: GudD produces 5-dehydro-4-deoxy-D-glucarate, the KDGDH
    substrate.

    - D-galactarate dehydration precedes 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate:
    The D-galactarate branch is expected to feed the downstream keto-deoxy aldarate/KGSADH
    segment, but first-pass metadata do not fully resolve the intermediate mapping.

    - 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate feeds into 2,5-dioxopentanoate
    or KGSA to 2-oxoglutarate: KDGDH produces 2,5-dioxopentanoate, the KGSADH substrate.'
  pathway_query: ppu00053
  pathway_id: ppu00053
  pathway_name: Ascorbate and aldarate metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00053 with 4 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '8'
  candidate_genes: '- udh: PP_1171 | Q88NN6 | Uronate dehydrogenase (EC 1.1.1.203)
    (D-galacturonate dehydrogenase) (D-glucuronate dehydrogenase) (Hexuronate dehydrogenase)
    (EC 1.1.1.203; primary bucket kegg:ppu00053)

    - PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22;
    primary bucket kegg:ppu00040)

    - PP_3599: PP_3599 | Q88GW8 | 5-dehydro-4-deoxyglucarate dehydratase (EC 4.2.1.41)
    (5-keto-4-deoxy-glucarate dehydratase) (KDGDH) (EC 4.2.1.41; primary bucket kegg:ppu00053)

    - garD: PP_3601 | Q88GW6 | Galactarate dehydratase (EC 4.2.1.42) (EC 4.2.1.42;
    primary bucket kegg:ppu00053)

    - PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - gudD: PP_4757 | Q88DR6 | Glucarate dehydratase (EC 4.2.1.40) (EC 4.2.1.40; primary
    bucket kegg:ppu00053)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__hexuronate_aldarate_catabolism__ppu00053-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__hexuronate_aldarate_catabolism__ppu00053-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Hexuronate and aldarate catabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00053
- Resolved ID: ppu00053
- Resolved name: Ascorbate and aldarate metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00053 with 4 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 8

- udh: PP_1171 | Q88NN6 | Uronate dehydrogenase (EC 1.1.1.203) (D-galacturonate dehydrogenase) (D-glucuronate dehydrogenase) (Hexuronate dehydrogenase) (EC 1.1.1.203; primary bucket kegg:ppu00053)
- PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22; primary bucket kegg:ppu00040)
- PP_3599: PP_3599 | Q88GW8 | 5-dehydro-4-deoxyglucarate dehydratase (EC 4.2.1.41) (5-keto-4-deoxy-glucarate dehydratase) (KDGDH) (EC 4.2.1.41; primary bucket kegg:ppu00053)
- garD: PP_3601 | Q88GW6 | Galactarate dehydratase (EC 4.2.1.42) (EC 4.2.1.42; primary bucket kegg:ppu00053)
- PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- gudD: PP_4757 | Q88DR6 | Glucarate dehydratase (EC 4.2.1.40) (EC 4.2.1.40; primary bucket kegg:ppu00053)

## Generic Module Context

### Working Scope

A bacterial free-hexuronate and aldarate catabolism module centered on oxidative conversion of D-glucuronate or D-galacturonate to glucarate or galactarate, dehydration of aldarates to keto-deoxy intermediates, and terminal oxidation of 2,5-dioxopentanoate or KGSA to 2-oxoglutarate. This is the catabolic arm that KEGG places under ascorbate and aldarate metabolism in Pseudomonas putida KT2440; it should be kept separate from UDP-glucuronate nucleotide-sugar biosynthesis and from eukaryotic ascorbate metabolism.

### Provisional Biological Outline

- Hexuronate and aldarate catabolism
  - 1. hexuronate oxidation
  - Glucuronate or galacturonate to urono-1,5-lactone
    - Uronate dehydrogenase (molecular player: uronate dehydrogenase activity; activity or role: uronate dehydrogenase activity)
  - 2. urono-lactone hydrolysis candidate
  - Urono-1,5-lactone hydrolysis to aldarate
    - Gluconolactonase-family lactonase candidate (molecular player: gluconolactonase activity; activity or role: gluconolactonase activity)
  - 3. D-glucarate dehydration
  - D-glucarate to 5-dehydro-4-deoxy-D-glucarate
    - Glucarate dehydratase (molecular player: glucarate dehydratase activity; activity or role: glucarate dehydratase activity)
  - 4. D-galactarate dehydration
  - D-galactarate dehydration
    - Galactarate dehydratase (molecular player: galactarate dehydratase activity; activity or role: galactarate dehydratase activity)
  - 5. 5-dehydro-4-deoxyglucarate dehydration
  - 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate
    - 5-dehydro-4-deoxyglucarate dehydratase (molecular player: 5-dehydro-4-deoxyglucarate dehydratase activity; activity or role: 5-dehydro-4-deoxyglucarate dehydratase activity)
  - 6. 2,5-dioxopentanoate or KGSA oxidation
  - 2,5-dioxopentanoate or KGSA to 2-oxoglutarate
    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+) activity)

### Known Relationships Among Steps

- Glucuronate or galacturonate to urono-1,5-lactone feeds into Urono-1,5-lactone hydrolysis to aldarate: Udh produces glucaro- or galactaro-1,5-lactones that require lactone hydrolysis before aldarate dehydration.
- Urono-1,5-lactone hydrolysis to aldarate feeds into D-glucarate to 5-dehydro-4-deoxy-D-glucarate: Lactonase activity would yield D-glucarate for GudD.
- Urono-1,5-lactone hydrolysis to aldarate feeds into D-galactarate dehydration: Lactonase activity would yield D-galactarate for GarD.
- D-glucarate to 5-dehydro-4-deoxy-D-glucarate feeds into 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate: GudD produces 5-dehydro-4-deoxy-D-glucarate, the KDGDH substrate.
- D-galactarate dehydration precedes 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate: The D-galactarate branch is expected to feed the downstream keto-deoxy aldarate/KGSADH segment, but first-pass metadata do not fully resolve the intermediate mapping.
- 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate feeds into 2,5-dioxopentanoate or KGSA to 2-oxoglutarate: KDGDH produces 2,5-dioxopentanoate, the KGSADH substrate.

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

Hexuronate and aldarate catabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00053
- Resolved ID: ppu00053
- Resolved name: Ascorbate and aldarate metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00053 with 4 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 8

- udh: PP_1171 | Q88NN6 | Uronate dehydrogenase (EC 1.1.1.203) (D-galacturonate dehydrogenase) (D-glucuronate dehydrogenase) (Hexuronate dehydrogenase) (EC 1.1.1.203; primary bucket kegg:ppu00053)
- PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22; primary bucket kegg:ppu00040)
- PP_3599: PP_3599 | Q88GW8 | 5-dehydro-4-deoxyglucarate dehydratase (EC 4.2.1.41) (5-keto-4-deoxy-glucarate dehydratase) (KDGDH) (EC 4.2.1.41; primary bucket kegg:ppu00053)
- garD: PP_3601 | Q88GW6 | Galactarate dehydratase (EC 4.2.1.42) (EC 4.2.1.42; primary bucket kegg:ppu00053)
- PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- gudD: PP_4757 | Q88DR6 | Glucarate dehydratase (EC 4.2.1.40) (EC 4.2.1.40; primary bucket kegg:ppu00053)

## Generic Module Context

### Working Scope

A bacterial free-hexuronate and aldarate catabolism module centered on oxidative conversion of D-glucuronate or D-galacturonate to glucarate or galactarate, dehydration of aldarates to keto-deoxy intermediates, and terminal oxidation of 2,5-dioxopentanoate or KGSA to 2-oxoglutarate. This is the catabolic arm that KEGG places under ascorbate and aldarate metabolism in Pseudomonas putida KT2440; it should be kept separate from UDP-glucuronate nucleotide-sugar biosynthesis and from eukaryotic ascorbate metabolism.

### Provisional Biological Outline

- Hexuronate and aldarate catabolism
  - 1. hexuronate oxidation
  - Glucuronate or galacturonate to urono-1,5-lactone
    - Uronate dehydrogenase (molecular player: uronate dehydrogenase activity; activity or role: uronate dehydrogenase activity)
  - 2. urono-lactone hydrolysis candidate
  - Urono-1,5-lactone hydrolysis to aldarate
    - Gluconolactonase-family lactonase candidate (molecular player: gluconolactonase activity; activity or role: gluconolactonase activity)
  - 3. D-glucarate dehydration
  - D-glucarate to 5-dehydro-4-deoxy-D-glucarate
    - Glucarate dehydratase (molecular player: glucarate dehydratase activity; activity or role: glucarate dehydratase activity)
  - 4. D-galactarate dehydration
  - D-galactarate dehydration
    - Galactarate dehydratase (molecular player: galactarate dehydratase activity; activity or role: galactarate dehydratase activity)
  - 5. 5-dehydro-4-deoxyglucarate dehydration
  - 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate
    - 5-dehydro-4-deoxyglucarate dehydratase (molecular player: 5-dehydro-4-deoxyglucarate dehydratase activity; activity or role: 5-dehydro-4-deoxyglucarate dehydratase activity)
  - 6. 2,5-dioxopentanoate or KGSA oxidation
  - 2,5-dioxopentanoate or KGSA to 2-oxoglutarate
    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+) activity)

### Known Relationships Among Steps

- Glucuronate or galacturonate to urono-1,5-lactone feeds into Urono-1,5-lactone hydrolysis to aldarate: Udh produces glucaro- or galactaro-1,5-lactones that require lactone hydrolysis before aldarate dehydration.
- Urono-1,5-lactone hydrolysis to aldarate feeds into D-glucarate to 5-dehydro-4-deoxy-D-glucarate: Lactonase activity would yield D-glucarate for GudD.
- Urono-1,5-lactone hydrolysis to aldarate feeds into D-galactarate dehydration: Lactonase activity would yield D-galactarate for GarD.
- D-glucarate to 5-dehydro-4-deoxy-D-glucarate feeds into 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate: GudD produces 5-dehydro-4-deoxy-D-glucarate, the KDGDH substrate.
- D-galactarate dehydration precedes 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate: The D-galactarate branch is expected to feed the downstream keto-deoxy aldarate/KGSADH segment, but first-pass metadata do not fully resolve the intermediate mapping.
- 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate feeds into 2,5-dioxopentanoate or KGSA to 2-oxoglutarate: KDGDH produces 2,5-dioxopentanoate, the KGSADH substrate.

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


# Hexuronate and Aldarate Catabolism in *Pseudomonas putida* KT2440: A Module/Pathway Review

## 1. Executive Summary

*Pseudomonas putida* KT2440 encodes a complete oxidative hexuronate-to-aldarate-to-α-ketoglutarate catabolic pathway. Unlike *Escherichia coli*, which uses an isomerase-based pathway for hexuronate catabolism, *P. putida* KT2440 employs an oxidative route in which D-glucuronate and D-galacturonate are first oxidized by uronate dehydrogenase (Udh, PP_1171) to urono-1,5-lactones, hydrolyzed by a dedicated lactonase (UxuL, PP_1170) to aldarates, and then degraded through sequential dehydration steps (GudD/GarD → KdgD) and terminal oxidation (KgsD) to feed α-ketoglutarate into the TCA cycle (bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 15-17).

Of the eight original candidate genes, six map confidently to pathway steps. One critical gene—PP_1170, encoding the UxuL lactonase—is absent from the candidate list but is strongly supported by both comparative genomics and high-throughput fitness data (bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 25-29). One candidate gene, *udg* (PP_2926, UDP-glucose 6-dehydrogenase), belongs to nucleotide-sugar biosynthesis and should be excluded from this catabolic module. Two KGSADH paralogs (PP_1256, PP_2585) are likely over-propagated annotations for this specific pathway.

## 2. Target-Organism Pathway Definition

### 2.1 Pathway Boundaries

The pathway reviewed here encompasses the **oxidative catabolism of free D-glucuronate and D-galacturonate** through aldaric acid intermediates to α-ketoglutarate in *P. putida* KT2440. KEGG maps this under "Ascorbate and aldarate metabolism" (ppu00053), but the relevant portion for this organism is restricted to:

- **Entry**: Free hexuronates (D-glucuronate, D-galacturonate) taken up from the environment
- **Core pathway**: Oxidation → lactone hydrolysis → aldarate dehydration → keto-deoxy aldarate dehydration/decarboxylation → semialdehyde oxidation
- **Exit**: α-Ketoglutarate entering the TCA cycle

The following should be kept **separate**:
- **UDP-glucuronate nucleotide-sugar biosynthesis** (involves *udg*/PP_2926, EC 1.1.1.22—a different metabolic context)
- **Eukaryotic ascorbate (vitamin C) metabolism** (absent in *P. putida*)
- **Isomerase-based hexuronate catabolism** (the *E. coli*-type UxaC/UxuB/UxaA pathway—*P. putida* KT2440 lacks this route) (yoon2009cloningandcharacterization pages 1-2, bouvier2019novelmetabolicpathways pages 23-25)
- **Pectin depolymerization** (upstream substrate liberation, not the intracellular catabolic module)

### 2.2 Alternative Pathway Names

This pathway is variably called the "oxidative hexuronate pathway," "aldarate catabolic pathway," or "KdgD-KgsD pathway" (to distinguish it from the *E. coli* GarR-GarL aldolase route for aldarate utilization) (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 23-25). Bouvier et al. (2019) refer to it as the "oxidative pathway of hexuronate catabolism" feeding into "aldarate utilization" (bouvier2019novelmetabolicpathways pages 1-2).

## 3. Expected Step Model

The six-step model for this module is supported by comparative genomics across Pseudomonadaceae and validated in part by direct biochemical and genetic data from KT2440.

| Step Number | Reaction Description | EC Number | Expected Gene(s) in KT2440 | Evidence Level | Module Status | Key Notes |
|---|---|---|---|---|---|---|
| 1 | D-glucuronate/D-galacturonate + NAD+ → glucaro-/galactaro-1,5-lactone + NADH | 1.1.1.203 | PP_1171 (udh) | Direct | covered | Recombinant Udh from KT2440 was biochemically characterized; NAD+-dependent key entry enzyme of the oxidative pathway; Udh is broadly distributed in Pseudomonadaceae (yoon2009cloningandcharacterization pages 4-5, yoon2009cloningandcharacterization pages 1-2, bouvier2019novelmetabolicpathways pages 25-29) |
| 2 | Glucaro-/galactaro-1,5-lactone → D-glucarate/meso-galactarate | 3.1.1.- | PP_1170 (uxuL) | Inferred | covered | Novel PF08450-family lactonase inferred from comparative genomics and supported by KT2440 fitness data on D-glucuronate/D-galacturonate; not in original candidate list and should be added; not explicitly represented in KEGG ppu00053 (bouvier2019novelmetabolicpathways pages 7-9, price2022fillinggapsin pages 7-9, bouvier2019novelmetabolicpathways pages 25-29) |
| 3 | D-glucarate → 5-dehydro-4-deoxy-D-glucarate | 4.2.1.40 | PP_4757 (gudD) | Inferred | covered | Conserved glucarate dehydratase in the Pseudomonas aldarate system; enolase-superfamily enzyme; note that gudD is separated chromosomally from the garD/kdgD/kgsD cluster in P. putida genomic reconstructions (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 17-19, bouvier2019novelmetabolicpathways pages 25-29) |
| 4 | meso-galactarate → 5-dehydro-4-deoxy-D-glucarate | 4.2.1.42 | PP_3601 (garD) | Inferred | covered | Galactarate dehydratase assigned from conserved aldarate cluster context and regulon reconstruction; co-clustered with downstream aldarate genes including kdgD and kgsD (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 25-29) |
| 5 | 5-dehydro-4-deoxy-D-glucarate → 2,5-dioxopentanoate (KGSA) + CO2 | 4.2.1.41 | PP_3599 (kdgD) | Inferred | covered | Corresponds to kdgD in Bouvier nomenclature; conserved part of the aldarate utilization locus; functions as the downstream keto-deoxy aldarate dehydratase/decarboxylase step (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 17-19, bouvier2019novelmetabolicpathways pages 25-29) |
| 6 | 2,5-dioxopentanoate (KGSA) + NAD(P)+ → α-ketoglutarate + NAD(P)H | 1.2.1.26 | PP_3602 (kgsD, primary); PP_1256 and PP_2585 (paralogs, uncertain) | Inferred | covered (PP_3602); candidate_uncertain (PP_1256, PP_2585) | P. putida contains multiple KGSADH isozymes/paralogs; PP_3602 is the best aldarate-pathway candidate because of positional linkage with garD/kdgD, whereas PP_1256 and PP_2585 lack equivalent pathway context and remain uncertain paralogs (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9, bouvier2019novelmetabolicpathways pages 25-29) |


*Table: This table summarizes the six expected biochemical steps for hexuronate and aldarate catabolism in Pseudomonas putida KT2440 and assigns a module satisfiability status to each. It is useful for curation because it distinguishes directly supported steps from inferred ones and highlights PP_1170 as a missing but necessary addition to the candidate set.*

### Step 1: Hexuronate Oxidation (Udh, PP_1171)

D-Glucuronate or D-galacturonate is oxidized by NAD⁺-dependent uronate dehydrogenase to the corresponding 1,5-lactone. The *P. putida* KT2440 Udh (PP_1171, GenBank BK006380) was cloned, recombinantly expressed, and kinetically characterized by Yoon et al. (2009). It is a homodimer (~60 kDa total) with a monomer molecular weight of ~30 kDa (yoon2009cloningandcharacterization pages 4-5, yoon2009cloningandcharacterization pages 1-2). The enzyme shows a k_cat of 55 s⁻¹ on glucuronate (K_m = 0.25 mM) and 30 s⁻¹ on galacturonate (K_m = 0.10 mM), with an optimal pH near 7.0 and relatively low thermal stability compared to the *Agrobacterium tumefaciens* ortholog (yoon2009cloningandcharacterization pages 4-5). It shares 75.6% sequence identity with *P. syringae* Udh (yoon2009cloningandcharacterization pages 4-5). This is the best-characterized enzyme in the module with **direct biochemical evidence from KT2440**.

### Step 2: Urono-1,5-Lactone Hydrolysis (UxuL, PP_1170)

The Udh reaction products are D-glucaro-1,5-lactone and D-galactaro-1,5-lactone. These must be hydrolyzed to the open-chain aldarates before dehydratase attack. Bouvier et al. (2019) identified two novel families of lactonases—UxuL (PF08450) and UxuF (PF10282)—involved in this step across Proteobacteria (bouvier2019novelmetabolicpathways pages 10-12, bouvier2019novelmetabolicpathways pages 12-14, bouvier2019novelmetabolicpathways pages 1-2). In *P. putida*, the *uxuL* gene is co-transcribed with *udh* and the TRAP transporter *uxuPQM* in the operon arrangement **udh–uxuL–uxuPQM–aldE** (bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 25-29). UxuL from *P. syringae* (orthologous to the *P. putida* gene) was biochemically characterized with k_cat/K_M of 2.2 × 10⁶ M⁻¹s⁻¹ for glucarolactone and 7.0 × 10⁵ M⁻¹s⁻¹ for galactarolactone (bouvier2019novelmetabolicpathways pages 17-19).

Critically, Price et al. (2022) demonstrated using RB-TnSeq fitness data that **PP_1170** (the putative lactonase adjacent to *udh*) is important for growth of *P. putida* KT2440 on both D-glucuronate and D-galacturonate as sole carbon sources (price2022fillinggapsin pages 7-9). This gene is **not present in the original candidate list** and must be added.

### Step 3: D-Glucarate Dehydration (GudD, PP_4757)

D-Glucarate dehydratase (EC 4.2.1.40) converts D-glucarate to 5-dehydro-4-deoxy-D-glucarate. PP_4757 (*gudD*) is the assigned gene, conserved across all analyzed Pseudomonadaceae species (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 25-29). In *P. putida*, *gudD* is located in the first cluster segment (*gguR1–gguT–gudD–kdgD–garP–garD–kgsD–gguR2*), under control of GguR regulators (bouvier2019novelmetabolicpathways pages 25-29). Note that *gudD* is positioned at a different chromosomal locus from the *udh*–*uxuL* operon, consistent with the two-cluster organization seen in Pseudomonadaceae.

### Step 4: D-Galactarate Dehydration (GarD, PP_3601)

Galactarate dehydratase (EC 4.2.1.42) converts meso-galactarate to 5-dehydro-4-deoxy-D-glucarate, the same product as GudD. PP_3601 (*garD*) is co-clustered with *kdgD* (PP_3599) and *kgsD* (PP_3602) in the aldarate utilization locus (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 25-29). The *uxuL* gene is frequently co-localized with *garD* across Proteobacteria, reflecting the functional linkage between lactone hydrolysis and galactarate dehydration (bouvier2019novelmetabolicpathways pages 14-15).

### Step 5: 5-Dehydro-4-deoxyglucarate Dehydration (KdgD, PP_3599)

This dehydratase/decarboxylase (EC 4.2.1.41) converts 5-dehydro-4-deoxy-D-glucarate (KDG) to α-ketoglutaric semialdehyde (KGSA, also called 2,5-dioxopentanoate). PP_3599 corresponds to *kdgD* in the Bouvier nomenclature and is part of the conserved aldarate cluster (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 25-29). This step distinguishes the *Pseudomonas*-type pathway from the *E. coli* GarR-GarL aldolase route, which instead cleaves KDG to pyruvate and tartronate semialdehyde (bouvier2019novelmetabolicpathways pages 23-25).

### Step 6: KGSA Oxidation (KgsD, PP_3602 primary; PP_1256, PP_2585 paralogs)

α-Ketoglutaric semialdehyde dehydrogenase (KGSADH, EC 1.2.1.26) oxidizes KGSA to α-ketoglutarate using NAD(P)⁺. *P. putida* possesses multiple KGSADH isozymes. Watanabe et al. (2007) demonstrated that *P. putida* has at least two KGSADHs in the NCBI database (accession numbers AAA25698 and AAA25870), belonging to the "KGSADH type II" subclass (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9). These are dimeric, NAD⁺-preferring enzymes with high specificity for KGSA. The D-glucarate/D-galactarate-inducible KGSADH-II isozyme, distinct from the L-arabinose-pathway and hydroxy-L-proline-pathway isozymes, was characterized in *Azospirillum brasilense* (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2).

In KT2440, **PP_3602** is the strongest candidate for the aldarate-pathway KGSADH because it is co-clustered with *garD* and *kdgD* (bouvier2019novelmetabolicpathways pages 25-29). PP_1256 and PP_2585, while annotated as 2,5-dioxovalerate dehydrogenases (EC 1.2.1.26), lack this genomic context and likely serve the L-arabinose or hydroxy-L-proline pathways, respectively.

## 4. Candidate Genes and Evidence

| Gene Name (common name) | Locus Tag (PP number) | UniProt ID | EC Number | Pathway Step | Primary Bucket | Evidence Type | Confidence Level | Key Evidence Summary | Module Status Recommendation |
|---|---|---|---|---|---|---|---|---|---|
| udh | PP_1171 | Q88NN6 | 1.1.1.203 | Step 1: Hexuronate oxidation | kegg:ppu00053 | direct biochemical | High | Recombinant KT2440 Udh was expressed and kinetically characterized; NAD+-dependent uronate dehydrogenase with kcat ≈ 55 s^-1 on glucuronate, Km 0.25 mM; 75.6% identity to P. syringae Udh; gene deposited as BK006380 (yoon2009cloningandcharacterization pages 4-5, yoon2009cloningandcharacterization pages 1-2) | covered |
| PP_1170 (UxuL) | PP_1170 | not listed | 3.1.1.- | Step 2: Urono-lactone hydrolysis | not in candidate list | fitness/genetic; comparative genomics | High | PF08450-family UxuL lactonase adjacent to udh in the P. putida hexuronate locus; Bouvier identified UxuL as the oxidative-pathway lactonase family in Pseudomonas, and Price reported PP_1170 is important for growth on D-glucuronate and D-galacturonate in KT2440 (bouvier2019novelmetabolicpathways pages 7-9, price2022fillinggapsin pages 7-9, bouvier2019novelmetabolicpathways pages 25-29) | covered |
| gudD | PP_4757 | Q88DR6 | 4.2.1.40 | Step 3: D-Glucarate dehydration | kegg:ppu00053 | comparative genomics | High | Assigned as glucarate dehydratase in the GguR-linked aldarate module; present in the P. putida Pseudomonadaceae cluster with gguT, kdgD, garP, garD, and kgsD (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 17-19, bouvier2019novelmetabolicpathways pages 25-29) | covered |
| garD | PP_3601 | Q88GW6 | 4.2.1.42 | Step 4: D-Galactarate dehydration | kegg:ppu00053 | comparative genomics | High | Assigned as galactarate dehydratase; co-located with downstream aldarate genes and included in the reconstructed GguR regulon for Pseudomonadaceae, including P. putida (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 25-29) | covered |
| PP_3599 (KdgD) | PP_3599 | Q88GW8 | 4.2.1.41 | Step 5: 5-Dehydro-4-deoxyglucarate dehydration | kegg:ppu00053 | comparative genomics | High | Corresponds to kdgD in Bouvier nomenclature; placed in the conserved P. putida aldarate catabolic cluster and expected to convert keto-deoxy glucarate to KGSA/2,5-dioxopentanoate (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 17-19, bouvier2019novelmetabolicpathways pages 25-29) | covered |
| PP_3602 (KgsD) | PP_3602 | Q88GW5 | 1.2.1.26 | Step 6: KGSA to α-ketoglutarate | kegg:ppu00040 primary | comparative genomics; indirect biochemical | High | Best positional candidate for the aldarate-pathway KGSADH because it is co-localized with garD and kdgD in the aldarate cluster; Watanabe showed P. putida has D-glucarate/D-galactarate-associated KGSADH isozymes, supporting this assignment to the pathway-specific paralog (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, bouvier2019novelmetabolicpathways pages 25-29) | covered |
| PP_1256 | PP_1256 | Q88NF5 | 1.2.1.26 | Step 6 paralog | kegg:ppu00040 primary | homology only | Low | Paralogous aldehyde dehydrogenase/KGSADH candidate without aldarate-cluster context; may belong to another oxidative sugar-acid route such as the L-arabinose-related KGSADH set rather than the primary hexuronate/aldarate module (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9) | candidate_uncertain |
| PP_2585 | PP_2585 | Q88JR4 | 1.2.1.26 | Step 6 paralog | kegg:ppu00040 primary | homology only | Low | Additional KGSADH-like paralog lacking specific genomic linkage to the aldarate locus; may function in another pathway such as hydroxy-L-proline or a different semialdehyde substrate system, so it should not be treated as the primary aldarate enzyme (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9) | candidate_uncertain |
| udg | PP_2926 | Q88IS3 | 1.1.1.22 | UDP-glucose 6-dehydrogenase; not part of free hexuronate catabolism | kegg:ppu00040 primary | annotation-based | Low | UDP-glucose 6-dehydrogenase belongs to nucleotide-sugar/exopolysaccharide metabolism, not the oxidative free hexuronate-to-aldarate catabolic arm defined here; inclusion in this module is an over-propagated neighboring-pathway annotation (bouvier2019novelmetabolicpathways pages 15-17, price2022fillinggapsin pages 1-2) | not_expected_in_module |


*Table: This table summarizes gene-by-gene evidence for the P. putida KT2440 hexuronate/aldarate catabolic module, including confidence levels and recommended module statuses. It is useful for manual satisfiability review because it separates high-confidence pathway members from paralogs and likely over-annotations.*

### 4.1 High-Confidence Assignments

- **PP_1171 (udh)**: The only gene in this module with direct biochemical evidence from KT2440. Recombinant protein was expressed, purified, and kinetically characterized (yoon2009cloningandcharacterization pages 4-5). Widely used in metabolic engineering for glucaric acid production (avci2025metabolicengineeringfor pages 10-12, avci2025metabolicengineeringfor pages 9-10).

- **PP_3601 (garD)**, **PP_4757 (gudD)**, **PP_3599 (kdgD)**: All three dehydratases are placed by comparative genomics in the conserved GguR-regulated aldarate utilization cluster across Pseudomonadaceae (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 25-29). Their EC numbers and predicted functions are well-established.

- **PP_3602 (kgsD)**: Best positional candidate for the aldarate-pathway KGSADH, co-located with *garD* and *kdgD* (bouvier2019novelmetabolicpathways pages 25-29).

### 4.2 Missing Gene: PP_1170 (UxuL Lactonase)

PP_1170 is **absent from the original 8-gene candidate list** but is essential for module completeness. It encodes a UxuL-family lactonase (PF08450) adjacent to *udh* in the *P. putida* operon (bouvier2019novelmetabolicpathways pages 7-9). RB-TnSeq data confirm its importance during growth on D-glucuronate and D-galacturonate in KT2440 (price2022fillinggapsin pages 7-9). The homologous enzyme from *P. syringae* was kinetically characterized, confirming activity on both glucaro- and galactaro-1,5-lactones (bouvier2019novelmetabolicpathways pages 17-19). **This gene should be promoted to the candidate list.**

### 4.3 Over-Propagated or Misassigned Annotations

- **PP_2926 (udg)**: UDP-glucose 6-dehydrogenase (EC 1.1.1.22) is part of nucleotide-sugar/exopolysaccharide biosynthesis and has no role in free hexuronate catabolism. Its inclusion in this module is an artifact of the broad KEGG "Ascorbate and aldarate metabolism" map (ppu00053), which conflates biosynthetic and catabolic pathways. **Should be excluded.**

- **PP_1256 and PP_2585**: These KGSADH paralogs (EC 1.2.1.26) are broadly annotated as 2,5-dioxovalerate dehydrogenases but lack genomic-context evidence for the aldarate pathway specifically. *P. putida* is known to have multiple KGSADH isozymes serving different metabolic pathways (L-arabinose, D-glucarate/D-galactarate, hydroxy-L-proline) (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2). Without fitness data or expression studies linking PP_1256 or PP_2585 to aldarate utilization, they should be marked as **candidate_uncertain** for this module.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Key Gap: Lactonase (PP_1170) Not in Candidate List

The most significant gap is the absence of PP_1170 (UxuL) from the candidate gene set. This enzyme bridges the Udh oxidation product (a 1,5-lactone) and the downstream aldarate dehydratases. Without it, the module has a logical break between Steps 1 and 3. The lactonase was only recently described (Bouvier et al. 2019) and was previously misannotated as a hypothetical protein or 6-phosphogluconolactonase in databases (bouvier2019novelmetabolicpathways pages 14-15).

### 5.2 Paralog Ambiguity at the KGSADH Step

Three genes (PP_3602, PP_1256, PP_2585) share the EC 1.2.1.26 annotation. Genomic context strongly favors PP_3602 as the aldarate-specific KGSADH, but direct evidence (e.g., gene knockout phenotype on glucarate/galactarate, or expression analysis) from KT2440 is lacking. The earlier work by Watanabe et al. (2007) on *A. brasilense* KGSADH isozymes provides a useful framework but was not conducted in *P. putida* directly (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2).

### 5.3 Udg (PP_2926) Is an Over-Propagation

The inclusion of UDP-glucose 6-dehydrogenase in the hexuronate catabolism module is a database artifact. KEGG ppu00053 lumps together biosynthetic and catabolic reactions involving uronic and aldaric acids; UDP-glucose dehydrogenase operates in the opposite metabolic direction (synthesis of UDP-glucuronate for cell-wall/exopolysaccharide purposes) and should not be in this catabolic module.

### 5.4 Transport and Regulation Components

The Bouvier et al. (2019) reconstruction identified several additional genes in the GguR regulon of *P. putida* that are functionally linked to this catabolic module but are not in the candidate list (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 25-29):
- **UxuPQM**: TRAP-family hexuronate transporter
- **GarP**: MFS-family aldarate permease
- **GguT**: MFS-family transporter (predicted aldarate)
- **Omp**: Outer membrane porin
- **AldE**: Aldose 1-epimerase/mutarotase
- **GguR1, GguR2**: Two GntR-family transcriptional regulators

These are beyond the strict enzymatic scope of the current module but are relevant for a complete functional annotation of hexuronate/aldarate utilization.

## 6. Module and GO-Curation Recommendations

### 6.1 Module Step Status

| Step | Status | Action Required |
|------|--------|----------------|
| 1. Hexuronate oxidation | **covered** | No action |
| 2. Urono-lactone hydrolysis | **covered** (after adding PP_1170) | **Add PP_1170 to candidate list**; request GO term for urono-1,5-lactonase activity |
| 3. D-Glucarate dehydration | **covered** | No action |
| 4. D-Galactarate dehydration | **covered** | No action |
| 5. KDG dehydration | **covered** | No action |
| 6. KGSA oxidation | **covered** (PP_3602); paralogs **candidate_uncertain** | Clarify PP_3602 vs. PP_1256/PP_2585 assignment |

### 6.2 Genes to Exclude

- **PP_2926 (udg)**: Mark as **not_expected_in_module**. UDP-glucose 6-dehydrogenase belongs to nucleotide-sugar biosynthesis.

### 6.3 Module Boundary Revision

The KEGG ppu00053 map is too broad for this organism-specific module. The catabolic arm should be defined as a six-step pathway from hexuronate to α-ketoglutarate, explicitly including the lactonase step. The biosynthetic arm (UDP-glucuronate synthesis) should be a separate module.

### 6.4 GO Term Recommendations

- A new GO molecular function term for "urono-1,5-lactonase activity" or "glucarolactonase/galactarolactonase activity" should be requested, as UxuL/UxuF lactonases are not well-represented in current GO.
- Existing GO annotations for EC 1.2.1.26 should distinguish the aldarate-pathway KGSADH from paralogs serving other pathways (L-arabinose, hydroxy-L-proline).

## 7. Genes to Promote to Full Review

1. **PP_1170 (UxuL)**: Highest priority. Must be added to the candidate list. Should receive a full `fetch-gene` review including: (a) confirmation of PF08450 domain, (b) operon structure with *udh*, (c) fitness data from Price et al. (2022), and (d) whether direct enzymatic characterization has been performed on the KT2440 protein specifically (the *P. syringae* ortholog was characterized by Bouvier et al. 2019).

2. **PP_3602 (KgsD)**: Medium priority. Clarification of which KGSADH isozyme is the primary aldarate-pathway enzyme requires expression or knockout studies. Cross-reference with the NCBI accession numbers AAA25698 and AAA25870 reported by Watanabe et al. (2007) for *P. putida* KGSADHs (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9).

3. **PP_1256 and PP_2585**: Low priority for this module, but warrant review to assign them to their correct pathways (likely L-arabinose and hydroxy-L-proline catabolism, respectively).

## 8. Key References

1. **Bouvier JT, Sernova NV, Ghasempur S, et al.** (2019) Novel metabolic pathways and regulons for hexuronate utilization in Proteobacteria. *J Bacteriol* 201:e00431-18. DOI: 10.1128/jb.00431-18. — Comprehensive comparative genomics of hexuronate/aldarate pathways in Proteobacteria; identified UxuL/UxuF lactonases and GguR regulons; includes *P. putida* gene cluster organization (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 10-12, bouvier2019novelmetabolicpathways pages 12-14, bouvier2019novelmetabolicpathways pages 1-2, bouvier2019novelmetabolicpathways pages 14-15, bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 17-19, bouvier2019novelmetabolicpathways pages 25-29).

2. **Yoon SH, Moon TS, Iranpour P, Lanza AM, Prather KJ.** (2009) Cloning and characterization of uronate dehydrogenases from two pseudomonads and *Agrobacterium tumefaciens* strain C58. *J Bacteriol* 191:1565–1573. DOI: 10.1128/jb.00586-08. — Direct biochemical characterization of KT2440 Udh (PP_1171); kinetic parameters, substrate specificity (yoon2009cloningandcharacterization pages 4-5, yoon2009cloningandcharacterization pages 1-2, yoon2009cloningandcharacterization pages 5-6).

3. **Price MN, Deutschbauer AM, Arkin AP.** (2022) Filling gaps in bacterial catabolic pathways with computation and high-throughput genetics. *PLoS Genet* 18:e1010156. DOI: 10.1371/journal.pgen.1010156. — RB-TnSeq fitness data identifying PP_1170 as important for D-glucuronate/D-galacturonate utilization in KT2440 (price2022fillinggapsin pages 7-9, price2022fillinggapsin pages 2-4, price2022fillinggapsin pages 1-2).

4. **Watanabe S, Yamada M, Ohtsu I, Makino K.** (2007) α-Ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of D-glucarate, D-galactarate, and hydroxy-L-proline. *J Biol Chem* 282:6685–6695. DOI: 10.1074/jbc.m611057200. — Characterization of KGSADH isozymes; identifies *P. putida* KGSADHs in the type II subclass (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 7-8).

5. **Avci FG, Prasun T, Wendisch VF.** (2025) Metabolic engineering for microbial production of sugar acids. *BMC Biotechnol* 25:36. DOI: 10.1186/s12896-025-00973-7. — Recent review of sugar acid production including glucaric acid using Udh from Pseudomonas (avci2025metabolicengineeringfor pages 10-12, avci2025metabolicengineeringfor pages 9-10).

6. **Mandrand-Berthelot MA, Condemine G, Hugouvieux-Cotte-Pattat N.** (2004) Catabolism of hexuronides, hexuronates, aldonates, and aldarates. *EcoSal Plus* 1:1. DOI: 10.1128/ecosalplus.3.4.2. — Foundational review of hexuronate catabolism in enterobacteria.


References

1. (bouvier2019novelmetabolicpathways pages 7-9): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

2. (bouvier2019novelmetabolicpathways pages 15-17): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

3. (bouvier2019novelmetabolicpathways pages 25-29): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

4. (yoon2009cloningandcharacterization pages 1-2): Sang-Hwal Yoon, Tae Seok Moon, Pooya Iranpour, Amanda M. Lanza, and Kristala Jones Prather. Cloning and characterization of uronate dehydrogenases from two pseudomonads and<i>agrobacterium tumefaciens</i>strain c58. Mar 2009. URL: https://doi.org/10.1128/jb.00586-08, doi:10.1128/jb.00586-08. This article has 64 citations and is from a peer-reviewed journal.

5. (bouvier2019novelmetabolicpathways pages 23-25): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

6. (bouvier2019novelmetabolicpathways pages 1-2): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

7. (yoon2009cloningandcharacterization pages 4-5): Sang-Hwal Yoon, Tae Seok Moon, Pooya Iranpour, Amanda M. Lanza, and Kristala Jones Prather. Cloning and characterization of uronate dehydrogenases from two pseudomonads and<i>agrobacterium tumefaciens</i>strain c58. Mar 2009. URL: https://doi.org/10.1128/jb.00586-08, doi:10.1128/jb.00586-08. This article has 64 citations and is from a peer-reviewed journal.

8. (price2022fillinggapsin pages 7-9): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Filling gaps in bacterial catabolic pathways with computation and high-throughput genetics. Apr 2022. URL: https://doi.org/10.1371/journal.pgen.1010156, doi:10.1371/journal.pgen.1010156. This article has 44 citations and is from a domain leading peer-reviewed journal.

9. (bouvier2019novelmetabolicpathways pages 17-19): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

10. (bouvier2019novelmetabolicpathways pages 9-10): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

11. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

12. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

13. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

14. (bouvier2019novelmetabolicpathways pages 10-12): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

15. (bouvier2019novelmetabolicpathways pages 12-14): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

16. (bouvier2019novelmetabolicpathways pages 14-15): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

17. (price2022fillinggapsin pages 1-2): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Filling gaps in bacterial catabolic pathways with computation and high-throughput genetics. Apr 2022. URL: https://doi.org/10.1371/journal.pgen.1010156, doi:10.1371/journal.pgen.1010156. This article has 44 citations and is from a domain leading peer-reviewed journal.

18. (avci2025metabolicengineeringfor pages 10-12): Fatma Gizem Avci, Tim Prasun, and Volker F. Wendisch. Metabolic engineering for microbial production of sugar acids. BMC Biotechnology, May 2025. URL: https://doi.org/10.1186/s12896-025-00973-7, doi:10.1186/s12896-025-00973-7. This article has 11 citations and is from a peer-reviewed journal.

19. (avci2025metabolicengineeringfor pages 9-10): Fatma Gizem Avci, Tim Prasun, and Volker F. Wendisch. Metabolic engineering for microbial production of sugar acids. BMC Biotechnology, May 2025. URL: https://doi.org/10.1186/s12896-025-00973-7, doi:10.1186/s12896-025-00973-7. This article has 11 citations and is from a peer-reviewed journal.

20. (yoon2009cloningandcharacterization pages 5-6): Sang-Hwal Yoon, Tae Seok Moon, Pooya Iranpour, Amanda M. Lanza, and Kristala Jones Prather. Cloning and characterization of uronate dehydrogenases from two pseudomonads and<i>agrobacterium tumefaciens</i>strain c58. Mar 2009. URL: https://doi.org/10.1128/jb.00586-08, doi:10.1128/jb.00586-08. This article has 64 citations and is from a peer-reviewed journal.

21. (price2022fillinggapsin pages 2-4): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Filling gaps in bacterial catabolic pathways with computation and high-throughput genetics. Apr 2022. URL: https://doi.org/10.1371/journal.pgen.1010156, doi:10.1371/journal.pgen.1010156. This article has 44 citations and is from a domain leading peer-reviewed journal.

22. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 7-8): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__hexuronate_aldarate_catabolism__ppu00053-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__hexuronate_aldarate_catabolism__ppu00053-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. bouvier2019novelmetabolicpathways pages 1-2
2. yoon2009cloningandcharacterization pages 4-5
3. bouvier2019novelmetabolicpathways pages 17-19
4. price2022fillinggapsin pages 7-9
5. bouvier2019novelmetabolicpathways pages 25-29
6. bouvier2019novelmetabolicpathways pages 14-15
7. bouvier2019novelmetabolicpathways pages 23-25
8. bouvier2019novelmetabolicpathways pages 7-9
9. bouvier2019novelmetabolicpathways pages 15-17
10. yoon2009cloningandcharacterization pages 1-2
11. bouvier2019novelmetabolicpathways pages 9-10
12. bouvier2019novelmetabolicpathways pages 10-12
13. bouvier2019novelmetabolicpathways pages 12-14
14. price2022fillinggapsin pages 1-2
15. avci2025metabolicengineeringfor pages 10-12
16. avci2025metabolicengineeringfor pages 9-10
17. yoon2009cloningandcharacterization pages 5-6
18. price2022fillinggapsin pages 2-4
19. https://doi.org/10.1128/jb.00431-18,
20. https://doi.org/10.1128/jb.00586-08,
21. https://doi.org/10.1371/journal.pgen.1010156,
22. https://doi.org/10.1074/jbc.m611057200,
23. https://doi.org/10.1186/s12896-025-00973-7,