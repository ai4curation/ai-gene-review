---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T19:11:34.735011'
end_time: '2026-07-06T19:33:03.818235'
duration_seconds: 1289.08
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Pentose and glucuronate interconversions
  module_summary: A boundary module for the sugar-acid and pentose interconversion
    reactions grouped by bacterial KEGG pentose/glucuronate maps. The map connects
    phosphorylated pentose metabolism, UDP-glucose/UDP-glucuronate generation, and
    uronate or aldarate degradation side chemistry. Organism-level curation should
    distinguish strict pentose-phosphate reactions, nucleotide-sugar biosynthesis,
    and candidate uronate-catabolic dehydratase/aldolase/dehydrogenase steps rather
    than treating every mapped enzyme as evidence for one complete linear pathway.
  module_outline: "- Pentose and glucuronate interconversions\n  - 1. pentose-phosphate\
    \ interconversion\n  - Ribulose 5-phosphate to xylulose 5-phosphate\n    - Ribulose-phosphate\
    \ 3-epimerase (molecular player: ribulose-phosphate 3-epimerase activity; activity\
    \ or role: ribulose-phosphate 3-epimerase activity)\n  - 2. UDP-glucose supply\n\
    \  - Glucose 1-phosphate to UDP-glucose\n    - UDP-glucose pyrophosphorylase (molecular\
    \ player: UTP:glucose-1-phosphate uridylyltransferase activity; activity or role:\
    \ UTP:glucose-1-phosphate uridylyltransferase activity)\n  - 3. UDP-glucuronate\
    \ formation\n  - UDP-glucose to UDP-glucuronate\n    - UDP-glucose 6-dehydrogenase\
    \ (molecular player: UDP-glucose 6-dehydrogenase activity; activity or role: UDP-glucose\
    \ 6-dehydrogenase activity)\n  - 4. 2,5-dioxovalerate oxidation\n  - 2,5-dioxovalerate\
    \ oxidation\n    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate\
    \ dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase\
    \ (NADP+) activity)"
  module_connections: '- Glucose 1-phosphate to UDP-glucose feeds into UDP-glucose
    to UDP-glucuronate: UDP-glucose is the substrate for UDP-glucose 6-dehydrogenase.'
  pathway_query: ppu00040
  pathway_id: ppu00040
  pathway_name: Pentose and glucuronate interconversions
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00040 with 8 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '8'
  candidate_genes: '- rpe: PP_0415 | Q88QS3 | Ribulose-phosphate 3-epimerase (EC 5.1.3.1)
    (EC 5.1.3.1; primary bucket kegg:ppu00040)

    - PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - PP_2037: PP_2037 | Q88L98 | Aldolase (primary bucket kegg:ppu00040)

    - PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - PP_2694: PP_2694 | Q88JF5 | Aldehyde dehydrogenase family protein (primary bucket
    kegg:ppu00040)

    - udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22;
    primary bucket kegg:ppu00040)

    - PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9)
    (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 46
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PSEPK__pentose_glucuronate_interconversions__ppu00040-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PSEPK__pentose_glucuronate_interconversions__ppu00040-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Pentose and glucuronate interconversions in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00040
- Resolved ID: ppu00040
- Resolved name: Pentose and glucuronate interconversions
- Source: KEGG

Resolved local bucket kegg:ppu00040 with 8 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 8

- rpe: PP_0415 | Q88QS3 | Ribulose-phosphate 3-epimerase (EC 5.1.3.1) (EC 5.1.3.1; primary bucket kegg:ppu00040)
- PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- PP_2037: PP_2037 | Q88L98 | Aldolase (primary bucket kegg:ppu00040)
- PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- PP_2694: PP_2694 | Q88JF5 | Aldehyde dehydrogenase family protein (primary bucket kegg:ppu00040)
- udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22; primary bucket kegg:ppu00040)
- PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)

## Generic Module Context

### Working Scope

A boundary module for the sugar-acid and pentose interconversion reactions grouped by bacterial KEGG pentose/glucuronate maps. The map connects phosphorylated pentose metabolism, UDP-glucose/UDP-glucuronate generation, and uronate or aldarate degradation side chemistry. Organism-level curation should distinguish strict pentose-phosphate reactions, nucleotide-sugar biosynthesis, and candidate uronate-catabolic dehydratase/aldolase/dehydrogenase steps rather than treating every mapped enzyme as evidence for one complete linear pathway.

### Provisional Biological Outline

- Pentose and glucuronate interconversions
  - 1. pentose-phosphate interconversion
  - Ribulose 5-phosphate to xylulose 5-phosphate
    - Ribulose-phosphate 3-epimerase (molecular player: ribulose-phosphate 3-epimerase activity; activity or role: ribulose-phosphate 3-epimerase activity)
  - 2. UDP-glucose supply
  - Glucose 1-phosphate to UDP-glucose
    - UDP-glucose pyrophosphorylase (molecular player: UTP:glucose-1-phosphate uridylyltransferase activity; activity or role: UTP:glucose-1-phosphate uridylyltransferase activity)
  - 3. UDP-glucuronate formation
  - UDP-glucose to UDP-glucuronate
    - UDP-glucose 6-dehydrogenase (molecular player: UDP-glucose 6-dehydrogenase activity; activity or role: UDP-glucose 6-dehydrogenase activity)
  - 4. 2,5-dioxovalerate oxidation
  - 2,5-dioxovalerate oxidation
    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+) activity)

### Known Relationships Among Steps

- Glucose 1-phosphate to UDP-glucose feeds into UDP-glucose to UDP-glucuronate: UDP-glucose is the substrate for UDP-glucose 6-dehydrogenase.

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

Pentose and glucuronate interconversions in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00040
- Resolved ID: ppu00040
- Resolved name: Pentose and glucuronate interconversions
- Source: KEGG

Resolved local bucket kegg:ppu00040 with 8 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 8

- rpe: PP_0415 | Q88QS3 | Ribulose-phosphate 3-epimerase (EC 5.1.3.1) (EC 5.1.3.1; primary bucket kegg:ppu00040)
- PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- PP_2037: PP_2037 | Q88L98 | Aldolase (primary bucket kegg:ppu00040)
- PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- PP_2694: PP_2694 | Q88JF5 | Aldehyde dehydrogenase family protein (primary bucket kegg:ppu00040)
- udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22; primary bucket kegg:ppu00040)
- PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)

## Generic Module Context

### Working Scope

A boundary module for the sugar-acid and pentose interconversion reactions grouped by bacterial KEGG pentose/glucuronate maps. The map connects phosphorylated pentose metabolism, UDP-glucose/UDP-glucuronate generation, and uronate or aldarate degradation side chemistry. Organism-level curation should distinguish strict pentose-phosphate reactions, nucleotide-sugar biosynthesis, and candidate uronate-catabolic dehydratase/aldolase/dehydrogenase steps rather than treating every mapped enzyme as evidence for one complete linear pathway.

### Provisional Biological Outline

- Pentose and glucuronate interconversions
  - 1. pentose-phosphate interconversion
  - Ribulose 5-phosphate to xylulose 5-phosphate
    - Ribulose-phosphate 3-epimerase (molecular player: ribulose-phosphate 3-epimerase activity; activity or role: ribulose-phosphate 3-epimerase activity)
  - 2. UDP-glucose supply
  - Glucose 1-phosphate to UDP-glucose
    - UDP-glucose pyrophosphorylase (molecular player: UTP:glucose-1-phosphate uridylyltransferase activity; activity or role: UTP:glucose-1-phosphate uridylyltransferase activity)
  - 3. UDP-glucuronate formation
  - UDP-glucose to UDP-glucuronate
    - UDP-glucose 6-dehydrogenase (molecular player: UDP-glucose 6-dehydrogenase activity; activity or role: UDP-glucose 6-dehydrogenase activity)
  - 4. 2,5-dioxovalerate oxidation
  - 2,5-dioxovalerate oxidation
    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+) activity)

### Known Relationships Among Steps

- Glucose 1-phosphate to UDP-glucose feeds into UDP-glucose to UDP-glucuronate: UDP-glucose is the substrate for UDP-glucose 6-dehydrogenase.

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

# Pentose and Glucuronate Interconversions in *Pseudomonas putida* KT2440: Species-Aware Module Review

## 1. Executive Summary

The KEGG map ppu00040 ("Pentose and glucuronate interconversions") in *Pseudomonas putida* KT2440 is a composite boundary module that conflates three biologically distinct processes: (i) pentose-phosphate interconversion within the non-oxidative pentose phosphate pathway (PPP), (ii) nucleotide-sugar (UDP-glucose/UDP-glucuronate) biosynthesis for cell-envelope polysaccharides, and (iii) oxidative hexuronate/aldarate catabolism. Of the eight candidate genes retrieved from local metadata, three (rpe, galU, udg) are well-supported and high-confidence, while the remaining five (three KGSADH paralogs annotated as EC 1.2.1.26, one aldolase, and one broad aldehyde dehydrogenase) are ambiguous due to paralog multiplicity, broad EC mapping, and likely annotation over-propagation. Critically, the metadata set is missing key genes for the oxidative hexuronate catabolic arm—particularly uronate dehydrogenase (PP_1171/Udh) and lactonase (PP_1170)—that have direct experimental support from fitness assays in KT2440. The module boundaries should be revised to separate these three functional arms, and several candidate genes should be reassigned or flagged for deeper curation.

## 2. Target-Organism Pathway Definition

### 2.1 Pathway scope in *P. putida* KT2440

*P. putida* KT2440 processes glucose primarily through the Entner-Doudoroff (ED) pathway, with a distinctive cyclic metabolism termed the EDEMP cycle that integrates elements of the ED pathway, gluconeogenic reactions of the Embden-Meyerhof-Parnas (EMP) pathway, and the pentose phosphate (PP) pathway (nikel2015pseudomonasputidakt2440 pages 9-11, nikel2015pseudomonasputidakt2440 pages 8-9, nikel2016fromdirtto pages 3-5, nikel2015pseudomonasputidakt2440 pages 1-2). In this cycle, approximately 10% of triose phosphates are recycled back to hexose phosphates through gluconeogenic reactions (G3P → DHAP → FBP → F6P → G6P), and ribulose-phosphate 3-epimerase (Rpe) plays a standard role in the non-oxidative branch of the PPP (dvorak2024syntheticallyprimedadaptationof pages 3-4, nikel2015pseudomonasputidakt2440 pages 6-7).

The nucleotide-sugar branch (galU → udg) serves LPS core oligosaccharide biosynthesis and alginate/exopolysaccharide precursor supply rather than free-sugar catabolism. *P. putida* produces alginate under water-limiting conditions via the algD-dependent biosynthetic pathway, which requires UDP-glucuronate as a precursor (chang2007alginateproductionby pages 2-3, chang2007alginateproductionby pages 7-8, chang2007alginateproductionby pages 1-2, chang2007alginateproductionby pages 3-4). The galU product (UDP-glucose) is also essential for LPS biosynthesis (costagutierrez2020plantgrowthpromotion pages 13-14, costagutierrez2020plantgrowthpromotion pages 6-8).

The hexuronate catabolic arm uses an oxidative (non-isomerase) pathway: hexuronates (D-glucuronate, D-galacturonate) are oxidized by uronate dehydrogenase (Udh) to glucaro- or galactaro-1,5-lactone, hydrolyzed by a lactonase to the corresponding aldarate, dehydrated by aldarate dehydratases (GudD/GarD family), and ultimately converted through α-ketoglutaric semialdehyde (KGSA) to α-ketoglutarate by KGSADH (EC 1.2.1.26) (avci2025metabolicengineeringfor pages 7-9, bouvier2019novelmetabolicpathways pages 1-2, bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 14-15, bouvier2019novelmetabolicpathways pages 7-9, yoon2009cloningandcharacterization pages 6-8).

### 2.2 Neighboring pathways to keep separate

- **Pentose phosphate pathway (ppu00030):** Rpe belongs properly to the non-oxidative branch of the PPP/EDEMP cycle rather than to uronate catabolism.
- **Amino sugar and nucleotide sugar metabolism (ppu00520):** The galU → udg branch feeds nucleotide-sugar pools for LPS/EPS and is better placed in nucleotide-sugar biosynthesis.
- **Ascorbate/aldarate metabolism (ppu00053):** Aldarate processing overlaps substantially.
- **Weimberg/Dahms pentose oxidation pathways:** *P. putida* KT2440 has endogenous genes for oxidative xylose processing (e.g., PP_2836 encoding a 2-keto-3-deoxy-xylonate dehydratase homolog), which connect to the same KGSA → α-ketoglutarate terminal step but are not part of the classical pentose/glucuronate interconversion map (bator2020comparisonofthree pages 7-9, bator2020comparisonofthree pages 13-14, meijnen2009establishmentofoxidative pages 6-7).

## 3. Expected Step Model

The pathway can be decomposed into the following functional steps relevant to *P. putida* KT2440:

**Step 1. Pentose-phosphate interconversion (Ru5P ↔ Xu5P):** Core non-oxidative PPP reaction catalyzed by Rpe. Well established in KT2440 via flux analysis and the EDEMP cycle (dvorak2024syntheticallyprimedadaptationof pages 3-4, nikel2015pseudomonasputidakt2440 pages 9-11).

**Step 2. UDP-glucose supply (G1P + UTP → UDP-glucose + PPi):** Catalyzed by GalU (PP_3821). Essential for LPS/EPS biosynthesis. In *P. aeruginosa*, galU mutants lack O-antigen and show truncated LPS core oligosaccharide (king2009reviewlipopolysaccharidebiosynthesis pages 13-15, ruhal2015amultivariateapproach pages 4-5). In *P. putida* KT2440, galU is required for LPS and EPS synthesis and competitive colonization of plant surfaces (costagutierrez2020plantgrowthpromotion pages 13-14, costagutierrez2020plantgrowthpromotion pages 6-8).

**Step 3. UDP-glucuronate formation (UDP-glucose → UDP-glucuronate):** Catalyzed by UDP-glucose 6-dehydrogenase (Udg, PP_2926). Provides UDP-glucuronate for alginate biosynthesis; alginate production in *P. putida* is well documented and regulated by water-limiting stress (chang2007alginateproductionby pages 2-3, chang2007alginateproductionby pages 7-8, chang2007alginateproductionby pages 3-4).

**Step 4. Hexuronate oxidation (glucuronate → glucaro-1,5-lactone → glucarate):** Catalyzed by uronate dehydrogenase (Udh, PP_1171) and a lactonase (PP_1170). These genes are NOT in the candidate list but are present in the KT2440 genome and have strong fitness support: PP_1170 shows fitness values less than −2 during growth on D-glucuronate and D-galacturonate (price2022fillinggapsin pages 16-17, price2021gapmindforcarbon pages 17-19). PP_1170 is 72% identical to the experimentally validated glucurono-1,5-lactonase PSPTO_1052 from *P. syringae* (price2022fillinggapsin pages 16-17). The Udh enzyme from *P. putida* KT2440 has been cloned and biochemically characterized (yoon2009cloningandcharacterization pages 1-2, yoon2009cloningandcharacterization pages 6-8).

**Step 5. Aldarate dehydration (glucarate → 5-dehydro-4-deoxy-glucarate):** Catalyzed by D-glucarate dehydratase (GudD) or D-galactarate dehydratase (GarD). These genes are part of the GguR regulon in Pseudomonadaceae but are absent from the current candidate list (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 14-15, bouvier2019novelmetabolicpathways pages 9-10).

**Step 6. KGSA oxidation (α-ketoglutaric semialdehyde → α-ketoglutarate):** The terminal oxidation step is catalyzed by KGSADH (EC 1.2.1.26). *P. putida* is known to possess four KGSADH isozymes, three inducible (by hydroxy-L-proline, D-glucarate, and L-lysine) and one constitutive (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2). Three candidate genes (PP_1256, PP_2585, PP_3602) annotated as EC 1.2.1.26 correspond to these isozymes but cannot be unambiguously assigned to the hexuronate/aldarate branch without locus-specific experimental data.

## 4. Candidate Genes and Evidence

The following table summarizes the assessment of each candidate gene:

| Gene name | Locus tag | UniProt ID | EC number | Annotated function | Proposed actual role in *P. putida* KT2440 | Evidence type | Confidence level | Module step assignment |
|---|---|---|---|---|---|---|---|---|
| rpe | PP_0415 | Q88QS3 | 5.1.3.1 | Ribulose-phosphate 3-epimerase | Core non-oxidative pentose-phosphate/EDEMP-cycle enzyme interconverting Ru5P and Xu5P; relevant to pentose-phosphate interconversion rather than uronate catabolism (dvorak2024syntheticallyprimedadaptationof pages 3-4, nikel2015pseudomonasputidakt2440 pages 9-11, nikel2015pseudomonasputidakt2440 pages 1-2) | Direct experimental flux analysis; computational/metabolic modeling | High | covered |
| PP_1256 | PP_1256 | Q88NF5 | 1.2.1.26 | 2,5-dioxovalerate dehydrogenase | One of several α-ketoglutaric semialdehyde dehydrogenase (KGSADH) isozymes likely oxidizing 2,5-dioxopentanoate/KGSA to 2-oxoglutarate in one or more oxidative sugar-acid or related catabolic routes; specific substrate context in KT2440 unresolved (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, ren2022structureandfunction pages 13-15, bouvier2019novelmetabolicpathways pages 15-17) | Homology; comparative biochemistry; computational pathway reconstruction | Medium | candidate_uncertain |
| PP_2037 | PP_2037 | Q88L98 | — | Aldolase | Current KEGG placement is weakly supported; no direct evidence found that this protein carries a pentose/glucuronate-specific aldolase step in KT2440. Likely over-propagated broad aldolase assignment unless linked to a distinct non-phosphorylative sugar-acid route by future evidence | Computational annotation only | Low | candidate_uncertain |
| PP_2585 | PP_2585 | Q88JR4 | 1.2.1.26 | 2,5-dioxovalerate dehydrogenase | Additional KGSADH paralog; likely participates in oxidation of KGSA/2,5-dioxopentanoate to 2-oxoglutarate in a pathway-specific context (e.g., glucarate/galactarate, hydroxyproline, lysine, or constitutive background activity), but exact assignment to hexuronate catabolism is unresolved (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9, bouvier2019novelmetabolicpathways pages 9-10) | Homology; comparative enzymology; computational regulon/pathway reconstruction | Medium | candidate_uncertain |
| PP_2694 | PP_2694 | Q88JF5 | — | Aldehyde dehydrogenase family protein | Broad ALDH-family annotation; could represent one of the multiple KGSADH-like activities known in *P. putida*, but no direct evidence ties this locus specifically to pentose/glucuronate interconversions in KT2440. Should not be accepted as a pathway step solely from family annotation (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) | Homology/family-level inference; computational annotation | Low | candidate_uncertain |
| udg | PP_2926 | Q88IS3 | 1.1.1.22 | UDP-glucose 6-dehydrogenase | High-confidence UDP-glucuronate-forming enzyme supplying nucleotide-sugar precursors for alginate and other envelope/exopolysaccharide functions; belongs to the nucleotide-sugar biosynthesis branch that KEGG groups with this map, not to hexuronate catabolism proper (chang2007alginateproductionby pages 2-3, chang2007alginateproductionby pages 7-8, chang2007alginateproductionby pages 3-4) | Direct physiological/biological role inferred from species alginate biology; pathway biochemistry | High | covered |
| PP_3602 | PP_3602 | Q88GW5 | 1.2.1.26 | 2,5-dioxovalerate dehydrogenase | Third candidate KGSADH paralog in this KEGG bucket; likely one member of the multi-isozyme KGSA oxidation capacity known for *P. putida*. Exact induction pattern and pathway placement in KT2440 remain unresolved, so it should not be treated as unique proof of the glucuronate branch (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, bouvier2019novelmetabolicpathways pages 15-17) | Homology; comparative enzymology; computational pathway reconstruction | Medium | candidate_uncertain |
| galU | PP_3821 | Q88GA4 | 2.7.7.9 | UTP--glucose-1-phosphate uridylyltransferase | High-confidence UDP-glucose pyrophosphorylase supplying UDP-glucose for LPS/EPS biosynthesis and upstream substrate for UDP-glucose dehydrogenase; function belongs to envelope/nucleotide-sugar metabolism rather than uronate degradation (costagutierrez2020plantgrowthpromotion pages 13-14, costagutierrez2020plantgrowthpromotion pages 6-8) | Direct species-specific phenotype/physiology; biochemical function inference | High | covered |


*Table: This table summarizes the likely roles and curation status of the eight KEGG ppu00040 candidate genes in *Pseudomonas putida* KT2440. It distinguishes well-supported core/nucleotide-sugar steps from uncertain paralogous aldehyde dehydrogenase assignments and likely over-annotations.*

### Detailed gene-by-gene assessment:

**rpe (PP_0415, Q88QS3, EC 5.1.3.1):** High confidence. This enzyme catalyzes the interconversion of ribulose-5-phosphate and xylulose-5-phosphate in the non-oxidative branch of the PPP. In *P. putida* KT2440, the Rpe reaction operates as part of the EDEMP cycle during glucose growth and plays a key role in xylose assimilation when the heterologous xylose isomerase pathway is expressed (dvorak2024syntheticallyprimedadaptationof pages 3-4). Flux analysis in xylose-adapted strains reveals that the Rpe reaction can be rate-limiting, necessitating compensatory carbon cycling through the non-oxidative PPP (dvorak2024syntheticallyprimedadaptationof pages 3-4). This is a bona fide pentose-phosphate step and its placement in ppu00040 is appropriate for the "pentose interconversion" component of the map.

**galU (PP_3821, Q88GA4, EC 2.7.7.9):** High confidence. Encodes UDP-glucose pyrophosphorylase, converting glucose-1-phosphate and UTP to UDP-glucose. In *P. putida* KT2440, galU is required for both LPS and EPS synthesis (costagutierrez2020plantgrowthpromotion pages 6-8). Mutant phenotype data from the closely related *P. aeruginosa* show that galU disruption causes loss of O-polysaccharide, truncated LPS core, and absence of glucose and rhamnose residues in the core oligosaccharide (king2009reviewlipopolysaccharidebiosynthesis pages 13-15, ruhal2015amultivariateapproach pages 4-5). The gene has been directly cited in *P. putida* KT2440 colonization studies (costagutierrez2020plantgrowthpromotion pages 13-14). **Caveat:** This enzyme serves envelope biosynthesis, not uronate catabolism; its inclusion in ppu00040 reflects KEGG's map-boundary convention rather than a linear catabolic pathway role.

**udg (PP_2926, Q88IS3, EC 1.1.1.22):** High confidence. Encodes UDP-glucose 6-dehydrogenase, oxidizing UDP-glucose to UDP-glucuronate. The product UDP-glucuronate serves as a precursor for alginate biosynthesis, which is well documented in *P. putida* (chang2007alginateproductionby pages 2-3, chang2007alginateproductionby pages 7-8, chang2007alginateproductionby pages 1-2, chang2007alginateproductionby pages 3-4). In *P. putida* mt-2, alginate production increases dramatically under water-limiting conditions and the algD mutant shows severely reduced uronic acid EPS content (chang2007alginateproductionby pages 3-4). **Caveat:** Like galU, this is a nucleotide-sugar biosynthetic enzyme, not a uronate degradation enzyme.

**PP_1256 (Q88NF5, EC 1.2.1.26), PP_2585 (Q88JR4, EC 1.2.1.26), PP_3602 (Q88GW5, EC 1.2.1.26):** Medium confidence as a group, with significant paralog ambiguity. All three are annotated as 2,5-dioxovalerate dehydrogenase (KGSADH). The name "2,5-dioxovalerate" is synonymous with α-ketoglutaric semialdehyde (KGSA), and EC 1.2.1.26 covers the NAD(P)+-dependent oxidation of KGSA to α-ketoglutarate (ren2022structureandfunction pages 13-15). Classical enzymology in *P. putida* has demonstrated four KGSADH isozymes with distinct induction profiles: hydroxy-L-proline-inducible, D-glucarate-inducible, L-lysine-inducible, and constitutive (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2). Phylogenetically, these isozymes represent convergent evolution within the ALDH superfamily, with type II KGSADHs being dimeric and type III KGSADHs being tetrameric (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 10-11). Only one of the four isozymes (the glucarate-induced form) properly belongs to the hexuronate/aldarate branch of ppu00040; the others serve hydroxyproline, lysine, or pentose oxidation pathways. Without locus-specific induction data or genomic-context analysis for each of PP_1256, PP_2585, and PP_3602 in KT2440, all three should remain as `candidate_uncertain` for this specific module.

**PP_2037 (Q88L98, aldolase):** Low confidence. No direct experimental or genomic-context evidence links this protein to a specific step in pentose/glucuronate interconversions in *P. putida* KT2440. The KEGG mapping may reflect broad EC family grouping rather than pathway-specific function. In the non-phosphorylative sugar acid pathways of *P. putida*, aldolase-type cleavage (Dahms pathway) produces pyruvate + glycolaldehyde from 2-keto-3-deoxy-pentonate, but this step is typically associated with PP_4283-regulated pathways and requires deletion of PP_2836 for isolation (bator2020comparisonofthree pages 13-14). Without further evidence, PP_2037 should be treated as likely over-propagated annotation.

**PP_2694 (Q88JF5, aldehyde dehydrogenase family protein):** Low confidence. Annotated only at the family level (ALDH superfamily), which is too broad for pathway assignment. While *P. putida* KT2440 encodes multiple ALDH family proteins with KGSA-related activities, this locus has no direct evidence connecting it to hexuronate catabolism. The annotation may represent over-propagation from superfamily membership.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Missing genes (gaps in metadata)

The most significant gap is the absence from the candidate list of the oxidative hexuronate catabolic enzymes that are genuinely present in *P. putida* KT2440 and have direct experimental support:

- **PP_1171 (Udh, uronate dehydrogenase):** Biochemically characterized from *P. putida* KT2440; catalyzes oxidation of glucuronate and galacturonate (yoon2009cloningandcharacterization pages 1-2, yoon2009cloningandcharacterization pages 6-8). This is the entry enzyme for the oxidative hexuronate pathway.
- **PP_1170 (putative lactonase):** Shows fitness values < −2 specifically during growth on D-glucuronate and D-galacturonate, is 72% identical to the validated lactonase PSPTO_1052 from *P. syringae* (price2022fillinggapsin pages 16-17, price2021gapmindforcarbon pages 17-19). This is among the strongest pieces of direct species-specific evidence available.
- **GudD/GarD-type aldarate dehydratases:** Part of the GguR regulon in Pseudomonadaceae (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 14-15, bouvier2019novelmetabolicpathways pages 9-10); specific KT2440 loci should be identified.
- **Hexuronate/aldarate transporters (UxuPQM TRAP system, ExuT-type MFS):** Identified in the GguR regulon in *P. putida* (bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 10-12).

### 5.2 Paralog ambiguity

The three EC 1.2.1.26 entries (PP_1256, PP_2585, PP_3602) represent a classic case of paralog ambiguity. Classical enzymology demonstrates that *P. putida* uses different KGSADH isozymes for different catabolic inputs (glucarate, hydroxyproline, lysine, arabinose) (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2). Mapping all three to ppu00040 overstates the pathway coverage; ideally, only the glucarate-inducible isozyme should be assigned to this module, with the others mapped to their respective catabolic routes.

### 5.3 Likely over-annotations

- **PP_2037 (aldolase):** No pathway-specific evidence; likely inherited from broad KEGG EC-family mapping.
- **PP_2694 (ALDH family protein):** Family-level annotation without locus-specific functional data; should not be counted as satisfying a specific pathway step.

## 6. Module and GO-Curation Recommendations

The following table summarizes recommended module-step status calls:

| Step number | Step name | Expected enzyme/reaction | Candidate gene(s) from metadata | Missing genes that should be considered | Module status recommendation | Key notes |
|---|---|---|---|---|---|---|
| 1 | Pentose-phosphate interconversion | Ribulose-5-phosphate 3-epimerase; Ru5P ↔ Xu5P | rpe / PP_0415 | None obvious | covered | Strong species-specific support as a core non-oxidative PPP/EDEMP-cycle step in *P. putida* KT2440; this is central carbon metabolism rather than uronate catabolism proper (dvorak2024syntheticallyprimedadaptationof pages 3-4, nikel2015pseudomonasputidakt2440 pages 9-11, nikel2015pseudomonasputidakt2440 pages 1-2) |
| 2 | UDP-glucose supply | UTP-glucose-1-phosphate uridylyltransferase; G1P → UDP-glucose | galU / PP_3821 | None obvious | covered | High-confidence nucleotide-sugar step supplying LPS/EPS biosynthesis; pathway-map inclusion is valid, but biologically this belongs to envelope/nucleotide-sugar metabolism rather than a linear glucuronate degradation route (costagutierrez2020plantgrowthpromotion pages 13-14, costagutierrez2020plantgrowthpromotion pages 6-8) |
| 3 | UDP-glucuronate formation | UDP-glucose 6-dehydrogenase; UDP-glucose → UDP-glucuronate | udg / PP_2926 | None obvious | covered | High-confidence upstream source of UDP-glucuronate, likely relevant to alginate/exopolysaccharide precursor supply in *Pseudomonas*; should be kept distinct from free hexuronate catabolism (chang2007alginateproductionby pages 2-3, chang2007alginateproductionby pages 7-8, chang2007alginateproductionby pages 3-4) |
| 4 | Hexuronate oxidation | Uronate dehydrogenase + lactonase; glucuronate/galacturonate → glucaro-/galactaro-lactone → aldarate | None in candidate list | PP_1171 (Udh), PP_1170 (putative lactonase/UxuL-like) | gap | This is a real missing arm in local metadata: fitness data strongly support PP_1170 in glucuronate/galacturonate utilization, and comparative genomics place Udh plus lactonase in the oxidative hexuronate pathway of *P. putida* (price2022fillinggapsin pages 16-17, price2021gapmindforcarbon pages 17-19, bouvier2019novelmetabolicpathways pages 7-9, yoon2009cloningandcharacterization pages 6-8) |
| 5 | Aldarate dehydration | Aldarate dehydratase; glucarate → 5-dehydro-4-deoxy-glucarate | None in candidate list | gudD-like dehydratase(s), possibly garD-linked enzymes in GguR regulon | gap | Oxidative hexuronate degradation in pseudomonads is reconstructed to proceed through GudD/GarD-family dehydratases, but the specific KT2440 locus was not recovered in the local candidate set; metadata likely undercalls this pathway segment (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 14-15, bouvier2019novelmetabolicpathways pages 9-10) |
| 6 | KGSA oxidation | α-Ketoglutaric semialdehyde dehydrogenase (EC 1.2.1.26); KGSA/2,5-dioxovalerate → 2-oxoglutarate | PP_1256, PP_2585, PP_3602 | Additional KGSADH paralog(s) may exist | candidate_uncertain | KT2440 is reported to encode multiple KGSADH isozymes with distinct induction patterns; three metadata genes are plausible paralogs, but exact assignment to the hexuronate/aldarate branch is unresolved, so none should be treated as uniquely sufficient evidence on its own (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, ren2022structureandfunction pages 13-15, bouvier2019novelmetabolicpathways pages 15-17) |
| 7 | Aldolase step | Putative aldolase step on KEGG boundary map | PP_2037 | None confidently identified | candidate_uncertain | Evidence for PP_2037 participating in ppu00040-specific chemistry is weak; likely an over-propagated broad aldolase mapping unless future gene-context or experimental data support a defined non-phosphorylative sugar-acid step (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 9-10) |
| 8 | Aldehyde dehydrogenase | Broad aldehyde dehydrogenase-family reaction | PP_2694 | Other ALDH-family paralogs may be more relevant | candidate_uncertain | Family-level ALDH annotation is too broad for direct pathway satisfaction. Because *P. putida* carries multiple KGSA/semialdehyde dehydrogenases, PP_2694 should remain provisional pending locus-specific evidence (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) |


*Table: This table summarizes recommended module-step calls for KEGG ppu00040 in *Pseudomonas putida* KT2440, separating well-supported core and nucleotide-sugar steps from missing oxidative hexuronate genes and ambiguous paralog assignments. It is useful for deciding which steps are covered, which are metadata gaps, and which require deeper curation.*

### 6.1 Summary of module-step status calls

| Status | Steps |
|---|---|
| **Covered** | Pentose-phosphate interconversion (rpe); UDP-glucose supply (galU); UDP-glucuronate formation (udg) |
| **Candidate_uncertain** | KGSA oxidation (PP_1256, PP_2585, PP_3602); Aldolase step (PP_2037); ALDH step (PP_2694) |
| **Gap** | Hexuronate oxidation (Udh + lactonase, PP_1171 + PP_1170); Aldarate dehydration (GudD/GarD) |

### 6.2 Module boundary recommendations

The current KEGG ppu00040 map conflates three biologically and regulatorily distinct processes. For *P. putida* KT2440, the following restructuring is recommended:

1. **Pentose-phosphate interconversion sub-module:** rpe (PP_0415). This belongs primarily to the PPP/EDEMP cycle and should cross-reference ppu00030.
2. **Nucleotide-sugar biosynthesis sub-module:** galU (PP_3821) → udg (PP_2926). This feeds LPS/EPS/alginate biosynthesis and should cross-reference ppu00520.
3. **Oxidative hexuronate catabolism sub-module:** This arm (hexuronate → aldarate → KGSA → α-KG) requires its own module document, incorporating PP_1171 (Udh), PP_1170 (lactonase), GudD/GarD (dehydratases), and the appropriate KGSADH isozyme. The GguR regulon reconstruction (bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 14-15, bouvier2019novelmetabolicpathways pages 9-10) provides the biological framework for this sub-module.

### 6.3 GO term considerations

- Rpe: GO:0004750 (ribulose-phosphate 3-epimerase activity) is appropriate.
- GalU: GO:0003983 (UTP:glucose-1-phosphate uridylyltransferase activity) is appropriate.
- Udg: GO:0003979 (UDP-glucose 6-dehydrogenase activity) is appropriate.
- For PP_1256/PP_2585/PP_3602: The EC 1.2.1.26 mapping to GO:0004491 (methylmalonate-semialdehyde dehydrogenase activity) should be reviewed; the correct GO term is GO:0004491 only if the primary substrate is confirmed. The specific 2,5-dioxovalerate dehydrogenase activity should be distinguished from other ALDH activities.

## 7. Genes to Promote to Full Review

The following genes should be prioritized for deeper (`fetch-gene`) curation:

1. **PP_1170 (putative lactonase):** Not currently in the candidate list, but has the strongest direct fitness evidence for glucuronate/galacturonate utilization in KT2440 (fitness < −2). It should be added to the module and assessed for its specific lactonase activity via biochemical characterization or structural homology modeling (price2022fillinggapsin pages 16-17, price2021gapmindforcarbon pages 17-19).

2. **PP_1171 (Udh, uronate dehydrogenase):** Biochemically characterized from *P. putida* KT2440 with demonstrated activity on both glucuronate and galacturonate (yoon2009cloningandcharacterization pages 1-2, yoon2009cloningandcharacterization pages 6-8). Should be the anchor gene for the hexuronate catabolic arm.

3. **PP_1256, PP_2585, PP_3602 (KGSADH isozymes):** A comparative analysis is needed to determine which isozyme corresponds to which catabolic pathway (glucarate vs. hydroxyproline vs. lysine vs. constitutive). Genomic context analysis, induction studies, or regulon membership (GguR vs. other regulators) would resolve the assignments (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, bouvier2019novelmetabolicpathways pages 15-17).

4. **PP_2037 (aldolase):** Requires genomic context review to determine whether this gene has any role in sugar-acid catabolism or is a mis-annotation for this pathway.

5. **PP_2836 (2-keto-3-deoxy-xylonate dehydratase homolog):** While not in the candidate list for ppu00040, this gene is involved in the endogenous Weimberg-like xylose oxidation pathway in KT2440 (57% identity to *C. crescentus* XylX) and connects to the same KGSA → α-KG terminal oxidation step (bator2020comparisonofthree pages 7-9, meijnen2009establishmentofoxidative pages 6-7). Its relationship to the hexuronate pathway genes should be clarified.

## 8. Key References

- Nikel PI, Chavarría M, Fuhrer T, Sauer U, de Lorenzo V. *Pseudomonas putida* KT2440 strain metabolizes glucose through a cycle formed by enzymes of the Entner-Doudoroff, Embden-Meyerhof-Parnas, and Pentose Phosphate Pathways. *J Biol Chem*. 2015;290:25920–25932. DOI: 10.1074/jbc.M115.687749 (nikel2015pseudomonasputidakt2440 pages 9-11, nikel2015pseudomonasputidakt2440 pages 8-9, nikel2015pseudomonasputidakt2440 pages 1-2)

- Dvořák P, Burýšková B, Popelářová B, et al. Synthetically-primed adaptation of *Pseudomonas putida* to a non-native substrate D-xylose. *Nat Commun*. 2024;15:2666. DOI: 10.1038/s41467-024-46812-9 (dvorak2024syntheticallyprimedadaptationof pages 3-4, dvorak2024syntheticallyprimedadaptationof pages 2-3)

- Price MN, Deutschbauer AM, Arkin AP. Filling gaps in bacterial catabolic pathways with computation and high-throughput genetics. *PLoS Genet*. 2022;18:e1010156. DOI: 10.1371/journal.pgen.1010156 (price2022fillinggapsin pages 16-17)

- Bouvier JT, Sernova NV, Ghasempur S, et al. Novel metabolic pathways and regulons for hexuronate utilization in Proteobacteria. *J Bacteriol*. 2019;201:e00431-18. DOI: 10.1128/JB.00431-18 (bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 15-17, bouvier2019novelmetabolicpathways pages 14-15, bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 1-2, bouvier2019novelmetabolicpathways pages 17-19, bouvier2019novelmetabolicpathways pages 10-12)

- Yoon S-H, Moon TS, Iranpour P, Lanza AM, Prather KJ. Cloning and characterization of uronate dehydrogenases from two Pseudomonads and *Agrobacterium tumefaciens* strain C58. *J Bacteriol*. 2009;191:1565–1573. DOI: 10.1128/JB.00586-08 (yoon2009cloningandcharacterization pages 1-2, yoon2009cloningandcharacterization pages 6-8)

- Watanabe S, Yamada M, Ohtsu I, Makino K. α-Ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of D-glucarate, D-galactarate, and hydroxy-L-proline. *J Biol Chem*. 2007;282:6685–6695. DOI: 10.1074/jbc.M611057200 (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 10-11)

- Chang W-S, van de Mortel M, Nielsen L, et al. Alginate production by *Pseudomonas putida* creates a hydrated microenvironment and contributes to biofilm architecture and stress tolerance under water-limiting conditions. *J Bacteriol*. 2007;189:8290–8299. DOI: 10.1128/JB.00727-07 (chang2007alginateproductionby pages 2-3, chang2007alginateproductionby pages 7-8, chang2007alginateproductionby pages 1-2, chang2007alginateproductionby pages 3-4)

- Costa-Gutierrez SB, Lami MJ, Caram-Di Santo MC, et al. Plant growth promotion by *Pseudomonas putida* KT2440 under saline stress: role of eptA. *Appl Microbiol Biotechnol*. 2020;104:4577–4592. DOI: 10.1007/s00253-020-10516-z (costagutierrez2020plantgrowthpromotion pages 13-14, costagutierrez2020plantgrowthpromotion pages 6-8)

- Bator I, Wittgens A, Rosenau F, Tiso T, Blank LM. Comparison of three xylose pathways in *Pseudomonas putida* KT2440 for the synthesis of valuable products. *Front Bioeng Biotechnol*. 2020;7:480. DOI: 10.3389/fbioe.2019.00480 (bator2020comparisonofthree pages 7-9, bator2020comparisonofthree pages 13-14, bator2020comparisonofthree pages 1-2)

- Meijnen J-P, de Winde JH, Ruijssenaars HJ. Establishment of oxidative D-xylose metabolism in *Pseudomonas putida* S12. *Appl Environ Microbiol*. 2009;75:2784–2791. DOI: 10.1128/AEM.02713-08 (meijnen2009establishmentofoxidative pages 5-6, meijnen2009establishmentofoxidative pages 1-1, meijnen2009establishmentofoxidative pages 6-7)

- Ren Y, Eronen V, Andberg MB, Koivula A, Hakulinen N. Structure and function of aldopentose catabolism enzymes involved in oxidative non-phosphorylative pathways. *Biotechnol Biofuels Bioprod*. 2022;15:147. DOI: 10.1186/s13068-022-02252-5 (ren2022structureandfunction pages 13-15)

- King JD, Kocíncová D, Westman EL, Lam JS. Review: Lipopolysaccharide biosynthesis in *Pseudomonas aeruginosa*. *Innate Immun*. 2009;15:261–312. DOI: 10.1177/1753425909106436 (king2009reviewlipopolysaccharidebiosynthesis pages 13-15)

References

1. (nikel2015pseudomonasputidakt2440 pages 9-11): Pablo I. Nikel, Max Chavarría, Tobias Fuhrer, Uwe Sauer, and Víctor de Lorenzo. Pseudomonas putida kt2440 strain metabolizes glucose through a cycle formed by enzymes of the entner-doudoroff, embden-meyerhof-parnas, and pentose phosphate pathways. Journal of Biological Chemistry, 290:25920-25932, Oct 2015. URL: https://doi.org/10.1074/jbc.m115.687749, doi:10.1074/jbc.m115.687749. This article has 446 citations and is from a domain leading peer-reviewed journal.

2. (nikel2015pseudomonasputidakt2440 pages 8-9): Pablo I. Nikel, Max Chavarría, Tobias Fuhrer, Uwe Sauer, and Víctor de Lorenzo. Pseudomonas putida kt2440 strain metabolizes glucose through a cycle formed by enzymes of the entner-doudoroff, embden-meyerhof-parnas, and pentose phosphate pathways. Journal of Biological Chemistry, 290:25920-25932, Oct 2015. URL: https://doi.org/10.1074/jbc.m115.687749, doi:10.1074/jbc.m115.687749. This article has 446 citations and is from a domain leading peer-reviewed journal.

3. (nikel2016fromdirtto pages 3-5): Pablo I Nikel, Max Chavarría, Antoine Danchin, and Víctor de Lorenzo. From dirt to industrial applications: pseudomonas putida as a synthetic biology chassis for hosting harsh biochemical reactions. Current opinion in chemical biology, 34:20-29, Oct 2016. URL: https://doi.org/10.1016/j.cbpa.2016.05.011, doi:10.1016/j.cbpa.2016.05.011. This article has 270 citations and is from a peer-reviewed journal.

4. (nikel2015pseudomonasputidakt2440 pages 1-2): Pablo I. Nikel, Max Chavarría, Tobias Fuhrer, Uwe Sauer, and Víctor de Lorenzo. Pseudomonas putida kt2440 strain metabolizes glucose through a cycle formed by enzymes of the entner-doudoroff, embden-meyerhof-parnas, and pentose phosphate pathways. Journal of Biological Chemistry, 290:25920-25932, Oct 2015. URL: https://doi.org/10.1074/jbc.m115.687749, doi:10.1074/jbc.m115.687749. This article has 446 citations and is from a domain leading peer-reviewed journal.

5. (dvorak2024syntheticallyprimedadaptationof pages 3-4): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Elisabeth Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Synthetically-primed adaptation of pseudomonas putida to a non-native substrate d-xylose. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46812-9, doi:10.1038/s41467-024-46812-9. This article has 36 citations and is from a highest quality peer-reviewed journal.

6. (nikel2015pseudomonasputidakt2440 pages 6-7): Pablo I. Nikel, Max Chavarría, Tobias Fuhrer, Uwe Sauer, and Víctor de Lorenzo. Pseudomonas putida kt2440 strain metabolizes glucose through a cycle formed by enzymes of the entner-doudoroff, embden-meyerhof-parnas, and pentose phosphate pathways. Journal of Biological Chemistry, 290:25920-25932, Oct 2015. URL: https://doi.org/10.1074/jbc.m115.687749, doi:10.1074/jbc.m115.687749. This article has 446 citations and is from a domain leading peer-reviewed journal.

7. (chang2007alginateproductionby pages 2-3): Woo-Suk Chang, Martijn van de Mortel, Lindsey Nielsen, Gabriela Nino de Guzman, Xiaohong Li, and Larry J. Halverson. Alginate production by <i>pseudomonas putida</i> creates a hydrated microenvironment and contributes to biofilm architecture and stress tolerance under water-limiting conditions. Nov 2007. URL: https://doi.org/10.1128/jb.00727-07, doi:10.1128/jb.00727-07. This article has 444 citations and is from a peer-reviewed journal.

8. (chang2007alginateproductionby pages 7-8): Woo-Suk Chang, Martijn van de Mortel, Lindsey Nielsen, Gabriela Nino de Guzman, Xiaohong Li, and Larry J. Halverson. Alginate production by <i>pseudomonas putida</i> creates a hydrated microenvironment and contributes to biofilm architecture and stress tolerance under water-limiting conditions. Nov 2007. URL: https://doi.org/10.1128/jb.00727-07, doi:10.1128/jb.00727-07. This article has 444 citations and is from a peer-reviewed journal.

9. (chang2007alginateproductionby pages 1-2): Woo-Suk Chang, Martijn van de Mortel, Lindsey Nielsen, Gabriela Nino de Guzman, Xiaohong Li, and Larry J. Halverson. Alginate production by <i>pseudomonas putida</i> creates a hydrated microenvironment and contributes to biofilm architecture and stress tolerance under water-limiting conditions. Nov 2007. URL: https://doi.org/10.1128/jb.00727-07, doi:10.1128/jb.00727-07. This article has 444 citations and is from a peer-reviewed journal.

10. (chang2007alginateproductionby pages 3-4): Woo-Suk Chang, Martijn van de Mortel, Lindsey Nielsen, Gabriela Nino de Guzman, Xiaohong Li, and Larry J. Halverson. Alginate production by <i>pseudomonas putida</i> creates a hydrated microenvironment and contributes to biofilm architecture and stress tolerance under water-limiting conditions. Nov 2007. URL: https://doi.org/10.1128/jb.00727-07, doi:10.1128/jb.00727-07. This article has 444 citations and is from a peer-reviewed journal.

11. (costagutierrez2020plantgrowthpromotion pages 13-14): Stefanie B. Costa-Gutierrez, María Jesús Lami, María Carolina Caram-Di Santo, Ana M. Zenoff, Paula A. Vincent, María Antonia Molina-Henares, Manuel Espinosa-Urgel, and Ricardo E. de Cristóbal. Plant growth promotion by pseudomonas putida kt2440 under saline stress: role of epta. Applied Microbiology and Biotechnology, 104:4577-4592, Mar 2020. URL: https://doi.org/10.1007/s00253-020-10516-z, doi:10.1007/s00253-020-10516-z. This article has 102 citations and is from a domain leading peer-reviewed journal.

12. (costagutierrez2020plantgrowthpromotion pages 6-8): Stefanie B. Costa-Gutierrez, María Jesús Lami, María Carolina Caram-Di Santo, Ana M. Zenoff, Paula A. Vincent, María Antonia Molina-Henares, Manuel Espinosa-Urgel, and Ricardo E. de Cristóbal. Plant growth promotion by pseudomonas putida kt2440 under saline stress: role of epta. Applied Microbiology and Biotechnology, 104:4577-4592, Mar 2020. URL: https://doi.org/10.1007/s00253-020-10516-z, doi:10.1007/s00253-020-10516-z. This article has 102 citations and is from a domain leading peer-reviewed journal.

13. (avci2025metabolicengineeringfor pages 7-9): Fatma Gizem Avci, Tim Prasun, and Volker F. Wendisch. Metabolic engineering for microbial production of sugar acids. BMC Biotechnology, May 2025. URL: https://doi.org/10.1186/s12896-025-00973-7, doi:10.1186/s12896-025-00973-7. This article has 11 citations and is from a peer-reviewed journal.

14. (bouvier2019novelmetabolicpathways pages 1-2): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

15. (bouvier2019novelmetabolicpathways pages 15-17): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

16. (bouvier2019novelmetabolicpathways pages 14-15): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

17. (bouvier2019novelmetabolicpathways pages 7-9): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

18. (yoon2009cloningandcharacterization pages 6-8): Sang-Hwal Yoon, Tae Seok Moon, Pooya Iranpour, Amanda M. Lanza, and Kristala Jones Prather. Cloning and characterization of uronate dehydrogenases from two pseudomonads and<i>agrobacterium tumefaciens</i>strain c58. Mar 2009. URL: https://doi.org/10.1128/jb.00586-08, doi:10.1128/jb.00586-08. This article has 64 citations and is from a peer-reviewed journal.

19. (bator2020comparisonofthree pages 7-9): Isabel Bator, Andreas Wittgens, Frank Rosenau, Till Tiso, and Lars M. Blank. Comparison of three xylose pathways in pseudomonas putida kt2440 for the synthesis of valuable products. Frontiers in Bioengineering and Biotechnology, Jan 2020. URL: https://doi.org/10.3389/fbioe.2019.00480, doi:10.3389/fbioe.2019.00480. This article has 134 citations.

20. (bator2020comparisonofthree pages 13-14): Isabel Bator, Andreas Wittgens, Frank Rosenau, Till Tiso, and Lars M. Blank. Comparison of three xylose pathways in pseudomonas putida kt2440 for the synthesis of valuable products. Frontiers in Bioengineering and Biotechnology, Jan 2020. URL: https://doi.org/10.3389/fbioe.2019.00480, doi:10.3389/fbioe.2019.00480. This article has 134 citations.

21. (meijnen2009establishmentofoxidative pages 6-7): Jean-Paul Meijnen, Johannes H. de Winde, and Harald J. Ruijssenaars. Establishment of oxidative <scp>d</scp> -xylose metabolism in <i>pseudomonas putida</i> s12. May 2009. URL: https://doi.org/10.1128/aem.02713-08, doi:10.1128/aem.02713-08. This article has 109 citations and is from a peer-reviewed journal.

22. (king2009reviewlipopolysaccharidebiosynthesis pages 13-15): Jerry D. King, Dana Kocíncová, Erin L. Westman, and Joseph S. Lam. Review: lipopolysaccharide biosynthesis in pseudomonas aeruginosa. Innate Immunity, 15:261-312, Aug 2009. URL: https://doi.org/10.1177/1753425909106436, doi:10.1177/1753425909106436. This article has 451 citations and is from a peer-reviewed journal.

23. (ruhal2015amultivariateapproach pages 4-5): Rohit Ruhal, Henrik Antti, Olena Rzhepishevska, Nicolas Boulanger, David R. Barbero, Sun Nyunt Wai, Bernt Eric Uhlin, and Madeleine Ramstedt. A multivariate approach to correlate bacterial surface properties to biofilm formation by lipopolysaccharide mutants of pseudomonas aeruginosa. Colloids and surfaces. B, Biointerfaces, 127:182-91, Mar 2015. URL: https://doi.org/10.1016/j.colsurfb.2015.01.030, doi:10.1016/j.colsurfb.2015.01.030. This article has 52 citations.

24. (price2022fillinggapsin pages 16-17): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Filling gaps in bacterial catabolic pathways with computation and high-throughput genetics. PLOS Genetics, 18:e1010156, Apr 2022. URL: https://doi.org/10.1371/journal.pgen.1010156, doi:10.1371/journal.pgen.1010156. This article has 44 citations and is from a domain leading peer-reviewed journal.

25. (price2021gapmindforcarbon pages 17-19): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Gapmind for carbon sources: automated annotations of catabolic pathways. bioRxiv, Nov 2021. URL: https://doi.org/10.1101/2021.11.02.466981, doi:10.1101/2021.11.02.466981. This article has 4 citations.

26. (yoon2009cloningandcharacterization pages 1-2): Sang-Hwal Yoon, Tae Seok Moon, Pooya Iranpour, Amanda M. Lanza, and Kristala Jones Prather. Cloning and characterization of uronate dehydrogenases from two pseudomonads and<i>agrobacterium tumefaciens</i>strain c58. Mar 2009. URL: https://doi.org/10.1128/jb.00586-08, doi:10.1128/jb.00586-08. This article has 64 citations and is from a peer-reviewed journal.

27. (bouvier2019novelmetabolicpathways pages 9-10): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

28. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

29. (ren2022structureandfunction pages 13-15): Yaxin Ren, Veikko Eronen, Martina Blomster Andberg, Anu Koivula, and Nina Hakulinen. Structure and function of aldopentose catabolism enzymes involved in oxidative non-phosphorylative pathways. Biotechnology for Biofuels and Bioproducts, Dec 2022. URL: https://doi.org/10.1186/s13068-022-02252-5, doi:10.1186/s13068-022-02252-5. This article has 11 citations and is from a domain leading peer-reviewed journal.

30. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 8-9): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

31. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 10-11): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

32. (bouvier2019novelmetabolicpathways pages 10-12): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

33. (dvorak2024syntheticallyprimedadaptationof pages 2-3): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Elisabeth Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Synthetically-primed adaptation of pseudomonas putida to a non-native substrate d-xylose. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46812-9, doi:10.1038/s41467-024-46812-9. This article has 36 citations and is from a highest quality peer-reviewed journal.

34. (bouvier2019novelmetabolicpathways pages 17-19): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

35. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

36. (bator2020comparisonofthree pages 1-2): Isabel Bator, Andreas Wittgens, Frank Rosenau, Till Tiso, and Lars M. Blank. Comparison of three xylose pathways in pseudomonas putida kt2440 for the synthesis of valuable products. Frontiers in Bioengineering and Biotechnology, Jan 2020. URL: https://doi.org/10.3389/fbioe.2019.00480, doi:10.3389/fbioe.2019.00480. This article has 134 citations.

37. (meijnen2009establishmentofoxidative pages 5-6): Jean-Paul Meijnen, Johannes H. de Winde, and Harald J. Ruijssenaars. Establishment of oxidative <scp>d</scp> -xylose metabolism in <i>pseudomonas putida</i> s12. May 2009. URL: https://doi.org/10.1128/aem.02713-08, doi:10.1128/aem.02713-08. This article has 109 citations and is from a peer-reviewed journal.

38. (meijnen2009establishmentofoxidative pages 1-1): Jean-Paul Meijnen, Johannes H. de Winde, and Harald J. Ruijssenaars. Establishment of oxidative <scp>d</scp> -xylose metabolism in <i>pseudomonas putida</i> s12. May 2009. URL: https://doi.org/10.1128/aem.02713-08, doi:10.1128/aem.02713-08. This article has 109 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PSEPK__pentose_glucuronate_interconversions__ppu00040-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PSEPK__pentose_glucuronate_interconversions__ppu00040-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. price2022fillinggapsin pages 16-17
2. dvorak2024syntheticallyprimedadaptationof pages 3-4
3. costagutierrez2020plantgrowthpromotion pages 6-8
4. costagutierrez2020plantgrowthpromotion pages 13-14
5. chang2007alginateproductionby pages 3-4
6. ren2022structureandfunction pages 13-15
7. bator2020comparisonofthree pages 13-14
8. king2009reviewlipopolysaccharidebiosynthesis pages 13-15
9. nikel2016fromdirtto pages 3-5
10. chang2007alginateproductionby pages 2-3
11. chang2007alginateproductionby pages 7-8
12. chang2007alginateproductionby pages 1-2
13. avci2025metabolicengineeringfor pages 7-9
14. bouvier2019novelmetabolicpathways pages 1-2
15. bouvier2019novelmetabolicpathways pages 15-17
16. bouvier2019novelmetabolicpathways pages 14-15
17. bouvier2019novelmetabolicpathways pages 7-9
18. yoon2009cloningandcharacterization pages 6-8
19. bator2020comparisonofthree pages 7-9
20. meijnen2009establishmentofoxidative pages 6-7
21. ruhal2015amultivariateapproach pages 4-5
22. price2021gapmindforcarbon pages 17-19
23. yoon2009cloningandcharacterization pages 1-2
24. bouvier2019novelmetabolicpathways pages 9-10
25. bouvier2019novelmetabolicpathways pages 10-12
26. dvorak2024syntheticallyprimedadaptationof pages 2-3
27. bouvier2019novelmetabolicpathways pages 17-19
28. bator2020comparisonofthree pages 1-2
29. meijnen2009establishmentofoxidative pages 5-6
30. meijnen2009establishmentofoxidative pages 1-1
31. https://doi.org/10.1074/jbc.m115.687749,
32. https://doi.org/10.1016/j.cbpa.2016.05.011,
33. https://doi.org/10.1038/s41467-024-46812-9,
34. https://doi.org/10.1128/jb.00727-07,
35. https://doi.org/10.1007/s00253-020-10516-z,
36. https://doi.org/10.1186/s12896-025-00973-7,
37. https://doi.org/10.1128/jb.00431-18,
38. https://doi.org/10.1128/jb.00586-08,
39. https://doi.org/10.3389/fbioe.2019.00480,
40. https://doi.org/10.1128/aem.02713-08,
41. https://doi.org/10.1177/1753425909106436,
42. https://doi.org/10.1016/j.colsurfb.2015.01.030,
43. https://doi.org/10.1371/journal.pgen.1010156,
44. https://doi.org/10.1101/2021.11.02.466981,
45. https://doi.org/10.1074/jbc.m611057200,
46. https://doi.org/10.1186/s13068-022-02252-5,