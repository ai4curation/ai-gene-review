---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T09:26:04.634095'
end_time: '2026-09-01T09:40:40.633053'
duration_seconds: 876.0
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Histidine catabolism to glutamate
  module_summary: A reusable pathway for degradation of L-histidine to L-glutamate.
    Three conserved reactions convert histidine through trans-urocanate and 4-imidazolone-5-propanoate
    to N-formimidoyl-L-glutamate. Terminal processing then differs among organisms.
    One bacterial route uses HutF and HutG to release ammonium and formate; a second
    bacterial route uses a formimidoylglutamase to release formamide directly. The
    folate-coupled route instead transfers the formimino group to tetrahydrofolate
    and feeds it into one-carbon metabolism.
  module_outline: "- Histidine catabolism to glutamate\n  - 1. histidine deamination\n\
    \  - Histidine ammonia-lyase reaction\n    - HutH/HAL histidine ammonia-lyase\
    \ activity (molecular player: histidine ammonia-lyase family; activity or role:\
    \ histidine ammonia-lyase activity)\n  - 2. urocanate hydration\n  - Urocanate\
    \ hydratase reaction\n    - HutU/UROC1 urocanate hydratase activity (molecular\
    \ player: urocanate hydratase family; activity or role: urocanate hydratase activity)\n\
    \  - 3. imidazolone ring opening\n  - Imidazolonepropionase reaction\n    - HutI/AMDHD1\
    \ imidazolonepropionase activity (molecular player: imidazolonepropionase family;\
    \ activity or role: imidazolonepropionase activity)\n  - 4. terminal FIGLU processing\
    \ to L-glutamate\n  - Alternative terminal processing of N-formimidoyl-L-glutamate\n\
    \    - Alternative versions by formimino-group disposal: FIGLU terminal-processing\
    \ routes\n      - HutF/HutG formate route\n        - 1. FIGLU deimination\n  \
    \      - HutF-dependent N-formyl-L-glutamate formation\n          - HutF formimidoylglutamate\
    \ deiminase activity (molecular player: HutF formimidoylglutamate deiminase family;\
    \ activity or role: formimidoylglutamate deiminase activity)\n        - 2. N-formyl-L-glutamate\
    \ deformylation\n        - HutG-dependent L-glutamate and formate formation\n\
    \          - HutG N-formylglutamate deformylase activity (molecular player: HutG\
    \ N-formylglutamate deformylase family; activity or role: N-formylglutamate deformylase\
    \ activity)\n      - Bacillus-type formimidoylglutamase route\n        - Bacillus-type\
    \ HutG formimidoylglutamase activity (molecular player: bacterial HutG formiminoglutamase\
    \ family; activity or role: formimidoylglutamase activity)\n      - Folate-coupled\
    \ FTCD route\n        - 1. formimino transfer to tetrahydrofolate\n        - FTCD\
    \ glutamate formimidoyltransferase reaction\n          - FTCD glutamate formimidoyltransferase\
    \ activity (molecular player: formimidoyltransferase-cyclodeaminase family; activity\
    \ or role: glutamate formimidoyltransferase activity)\n        - 2. formimino-folate\
    \ cyclodeamination\n        - FTCD formimidoyltetrahydrofolate cyclodeaminase\
    \ reaction\n          - FTCD formimidoyltetrahydrofolate cyclodeaminase activity\
    \ (molecular player: formimidoyltransferase-cyclodeaminase family; activity or\
    \ role: formimidoyltetrahydrofolate cyclodeaminase activity)"
  module_connections: '- Histidine ammonia-lyase reaction feeds into Urocanate hydratase
    reaction: The urocanate produced by HutH/HAL is consumed by HutU/UROC1.

    - Urocanate hydratase reaction feeds into Imidazolonepropionase reaction: The
    imidazolone intermediate produced by HutU/UROC1 is consumed by HutI/AMDHD1.

    - Imidazolonepropionase reaction feeds into Alternative terminal processing of
    N-formimidoyl-L-glutamate: N-formimidoyl-L-glutamate produced by HutI/AMDHD1 enters
    one of the terminal processing routes.

    - HutF-dependent N-formyl-L-glutamate formation feeds into HutG-dependent L-glutamate
    and formate formation: HutF produces the N-formyl-L-glutamate consumed by HutG.

    - FTCD glutamate formimidoyltransferase reaction feeds into FTCD formimidoyltetrahydrofolate
    cyclodeaminase reaction: The 5-formimidoyltetrahydrofolate produced by the transferase
    reaction is consumed by cyclodeamination.'
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
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__histidine_catabolism__ppu00340-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__histidine_catabolism__ppu00340-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Histidine catabolism to glutamate in Pseudomonas putida KT2440

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

A reusable pathway for degradation of L-histidine to L-glutamate. Three conserved reactions convert histidine through trans-urocanate and 4-imidazolone-5-propanoate to N-formimidoyl-L-glutamate. Terminal processing then differs among organisms. One bacterial route uses HutF and HutG to release ammonium and formate; a second bacterial route uses a formimidoylglutamase to release formamide directly. The folate-coupled route instead transfers the formimino group to tetrahydrofolate and feeds it into one-carbon metabolism.

### Provisional Biological Outline

- Histidine catabolism to glutamate
  - 1. histidine deamination
  - Histidine ammonia-lyase reaction
    - HutH/HAL histidine ammonia-lyase activity (molecular player: histidine ammonia-lyase family; activity or role: histidine ammonia-lyase activity)
  - 2. urocanate hydration
  - Urocanate hydratase reaction
    - HutU/UROC1 urocanate hydratase activity (molecular player: urocanate hydratase family; activity or role: urocanate hydratase activity)
  - 3. imidazolone ring opening
  - Imidazolonepropionase reaction
    - HutI/AMDHD1 imidazolonepropionase activity (molecular player: imidazolonepropionase family; activity or role: imidazolonepropionase activity)
  - 4. terminal FIGLU processing to L-glutamate
  - Alternative terminal processing of N-formimidoyl-L-glutamate
    - Alternative versions by formimino-group disposal: FIGLU terminal-processing routes
      - HutF/HutG formate route
        - 1. FIGLU deimination
        - HutF-dependent N-formyl-L-glutamate formation
          - HutF formimidoylglutamate deiminase activity (molecular player: HutF formimidoylglutamate deiminase family; activity or role: formimidoylglutamate deiminase activity)
        - 2. N-formyl-L-glutamate deformylation
        - HutG-dependent L-glutamate and formate formation
          - HutG N-formylglutamate deformylase activity (molecular player: HutG N-formylglutamate deformylase family; activity or role: N-formylglutamate deformylase activity)
      - Bacillus-type formimidoylglutamase route
        - Bacillus-type HutG formimidoylglutamase activity (molecular player: bacterial HutG formiminoglutamase family; activity or role: formimidoylglutamase activity)
      - Folate-coupled FTCD route
        - 1. formimino transfer to tetrahydrofolate
        - FTCD glutamate formimidoyltransferase reaction
          - FTCD glutamate formimidoyltransferase activity (molecular player: formimidoyltransferase-cyclodeaminase family; activity or role: glutamate formimidoyltransferase activity)
        - 2. formimino-folate cyclodeamination
        - FTCD formimidoyltetrahydrofolate cyclodeaminase reaction
          - FTCD formimidoyltetrahydrofolate cyclodeaminase activity (molecular player: formimidoyltransferase-cyclodeaminase family; activity or role: formimidoyltetrahydrofolate cyclodeaminase activity)

### Known Relationships Among Steps

- Histidine ammonia-lyase reaction feeds into Urocanate hydratase reaction: The urocanate produced by HutH/HAL is consumed by HutU/UROC1.
- Urocanate hydratase reaction feeds into Imidazolonepropionase reaction: The imidazolone intermediate produced by HutU/UROC1 is consumed by HutI/AMDHD1.
- Imidazolonepropionase reaction feeds into Alternative terminal processing of N-formimidoyl-L-glutamate: N-formimidoyl-L-glutamate produced by HutI/AMDHD1 enters one of the terminal processing routes.
- HutF-dependent N-formyl-L-glutamate formation feeds into HutG-dependent L-glutamate and formate formation: HutF produces the N-formyl-L-glutamate consumed by HutG.
- FTCD glutamate formimidoyltransferase reaction feeds into FTCD formimidoyltetrahydrofolate cyclodeaminase reaction: The 5-formimidoyltetrahydrofolate produced by the transferase reaction is consumed by cyclodeamination.

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

# Histidine Catabolism to Glutamate in *Pseudomonas putida* KT2440 — Module/Pathway/Taxon Review

**Target taxon:** *Pseudomonas putida* KT2440 (organism code PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00340 "Histidine metabolism" (resolved local bucket kegg:ppu00340; module area: amino acid metabolism)
**Module reviewed:** Histidine catabolism to L-glutamate (generic reusable module; His → urocanate → imidazolone-propionate → N-formimidoyl-glutamate → L-glutamate)

---

## 1. Executive Summary

The histidine-catabolism-to-glutamate module is **fully satisfiable (COVERED)** in *Pseudomonas putida* KT2440. The organism uses the classical bacterial **five-step Hut "formate" route**, encoded in a single contiguous, single-copy gene cluster spanning **PP_5029–PP_5036**. The core catabolic reactions are: **HutH** (histidase, PP_5032, EC 4.3.1.3) → **HutU** (urocanase, PP_5033, EC 4.2.1.49) → **HutI** (imidazolonepropionase, PP_5030, EC 3.5.2.7) → **HutF** (formimidoylglutamate deiminase, PP_5036, EC 3.5.3.13) → **HutG** (N-formylglutamate deformylase, PP_5029, EC 3.5.1.68). The cluster additionally encodes the ancillary functions **HutT** (histidine transporter, PP_5031), **HutC** (pathway repressor, PP_5035), and **HutD** (PP_5034, Pfam PF05962). Every core enzyme is present in exactly one copy, and there are no genuine enzymatic gaps in the pathway.

The two lineage-specific terminal alternatives described by the generic module — the **Bacillus-type formimidoylglutamase route** (EC 3.5.3.8) and the **folate-coupled FTCD route** (glutamate formimidoyltransferase EC 2.1.2.5 + formimidoyltetrahydrofolate cyclodeaminase EC 4.3.1.4) — are **verified absent proteome-wide** and should be marked `not_expected_in_target_taxon`. KT2440 disposes of the formimino group exclusively via the HutF/HutG formate route, releasing ammonium and formate.

The most important curation issue is **scope contamination in the candidate gene list**. Of the 20 candidate genes, only **5** belong to this module (the *hut* catabolic genes). The remaining 15 are over-propagated from the shared KEGG map ppu00340, which bundles histidine **biosynthesis** and **degradation** in one bucket: the *his** biosynthesis genes (hisG/D/C/B/H/A/F/I/E, hisZ), the histidinol-phosphatases (PP_3157, PP_5147), a phosphoserine phosphatase (PP_1721), plus two unrelated cross-mapped genes — *gshA* (glutathione biosynthesis, PP_0243) and a tryptophan 2-monooxygenase (PP_4983, from ppu00350). The recommendation is to **rebind the module** to KEGG M00045 (histidine degradation, histidine → N-formiminoglutamate → glutamate) / MetaCyc PWY-5030 and mark the module `module_needs_revision` on boundary grounds only — the biology itself is complete and clean. Crucially, there is **direct target-strain experimental evidence** that the system is physiologically active: deletion of *hutT* (PP_5031) severely impairs growth of KT2440 on histidine, and reconstituted HutT is a high-affinity histidine:H⁺ symporter ([PMID: 34245008](https://pubmed.ncbi.nlm.nih.gov/34245008/)). Regulatory context is established for the species: histidine assimilation as a carbon/nitrogen source is under CbrA/B and NtrC control in *P. putida* ([PMID: 20553554](https://pubmed.ncbi.nlm.nih.gov/20553554/)).

---

## 2. Target-Organism Pathway Definition

### What the module includes

The module is the **catabolic degradation of L-histidine to L-glutamate**. In KT2440 this is a linear five-reaction sequence with a defined terminal disposal of the formimino carbon:

1. **Histidine deamination** — histidine ammonia-lyase (histidase, HutH) releases NH₃ and produces *trans*-urocanate.
2. **Urocanate hydration** — urocanate hydratase (urocanase, HutU) produces 4-imidazolone-5-propanoate.
3. **Imidazolone ring opening** — imidazolonepropionase (HutI) hydrolyzes the ring to N-formimidoyl-L-glutamate (FIGLU).
4. **FIGLU deimination** — formimidoylglutamate deiminase (HutF) releases NH₃ and forms N-formyl-L-glutamate.
5. **Deformylation** — N-formylglutamate deformylase (HutG) releases formate and yields **L-glutamate**.

Net: L-histidine + 2 H₂O → L-glutamate + 2 NH₃ (as ammonium) + formate. The glutamate is fed into central nitrogen/carbon metabolism, which is why histidine serves as both a carbon and a nitrogen source in this organism.

### Pathway boundaries — what to keep separate

- **Histidine biosynthesis (de novo, His pathway).** KEGG ppu00340 conflates biosynthesis and degradation. The *his** genes (ATP-PRT, HisD, HisC, HisB, HisH/F/A, HisI/E, HisZ) build histidine from PRPP and are **not part of this catabolic module**. They must be scored separately.
- **One-carbon / folate metabolism.** In organisms using the FTCD route, the formimino group is transferred to tetrahydrofolate and enters C1 metabolism. **This linkage does not exist in KT2440** (FTCD absent); the formimino carbon leaves as free formate via HutG.
- **Glutathione biosynthesis.** *gshA* (glutamate–cysteine ligase) is cross-mapped only because glutamate is a shared metabolite; it is unrelated to histidine catabolism.
- **Tryptophan/indole metabolism.** PP_4983 (tryptophan 2-monooxygenase) belongs to ppu00350 and is a spurious cross-map.

### Alternate names and database definitions

- **KEGG:** module M00045 "Histidine degradation, histidine => N-formiminoglutamate => glutamate" is the correct catabolic module (ppu00340 is the broader combined map).
- **MetaCyc:** PWY-5030 "L-histidine degradation III" (the HutF/HutG bacterial formate route).
- **Common names:** "hut pathway," "histidine utilization pathway," "histidine dissimilation." Genes: *hutH* (histidase), *hutU* (urocanase), *hutI* (imidazolonepropionase), *hutF* (formiminoglutamate/formimidoylglutamate deiminase), *hutG* (N-formylglutamate deformylase), *hutC* (repressor), *hutD*, *hutT* (transporter).

---

## 3. Expected Step Model and Coverage

```
 L-Histidine
     │  [1] HutH  histidase (EC 4.3.1.3)          PP_5032   COVERED (single copy)
     ▼
 trans-Urocanate
     │  [2] HutU  urocanase (EC 4.2.1.49)         PP_5033   COVERED (single copy)
     ▼
 4-Imidazolone-5-propanoate
     │  [3] HutI  imidazolonepropionase (3.5.2.7) PP_5030   COVERED (single copy)
     ▼
 N-Formimidoyl-L-glutamate (FIGLU)
     │  [4] HutF  formimidoylglutamate deiminase  PP_5036   COVERED (single copy)
     │            (EC 3.5.3.13)  -- releases NH3
     ▼
 N-Formyl-L-glutamate
     │  [5] HutG  N-formylglutamate deformylase    PP_5029   COVERED (single copy)
     │            (EC 3.5.1.68) -- releases formate
     ▼
 L-Glutamate  -> central metabolism

 ANCILLARY (same operon, PP_5029–PP_5036):
   HutT  PP_5031  L-histidine:H+ symporter (transport)   COVERED (direct KT2440 IDA)
   HutC  PP_5035  pathway repressor                       COVERED
   HutD  PP_5034  Pfam PF05962 (cupin/HutD domain)        COVERED (accessory)

 TERMINAL ALTERNATIVES (generic module) — NOT in KT2440:
   Bacillus-type formimidoylglutamase (EC 3.5.3.8)        not_expected_in_target_taxon
   Folate FTCD: formimidoyltransferase (EC 2.1.2.5)       not_expected_in_target_taxon
              + cyclodeaminase (EC 4.3.1.4)               not_expected_in_target_taxon
```

All five core catabolic steps plus transport and regulation are covered by single-copy candidate genes in one operon. No step is missing, ambiguous, or dependent on an undiscovered paralog. The module is **satisfiable end-to-end**.

---

## 4. Candidate Genes and Evidence

### 4.1 In-scope genes (the *hut* module) — high confidence

| Gene | Locus | UniProt | Enzyme / role | EC | Module step | Copy no. | Assessment |
|------|-------|---------|---------------|----|-------------|----------|------------|
| hutH | PP_5032 | Q88CZ7 | Histidase (histidine ammonia-lyase) | 4.3.1.3 | 1 | 1 | COVERED |
| hutU | PP_5033 | Q88CZ6 | Urocanate hydratase (urocanase) | 4.2.1.49 | 2 | 1 | COVERED (alias cleanup needed) |
| hutI | PP_5030 | Q88CZ9 | Imidazolonepropionase | 3.5.2.7 | 3 | 1 | COVERED |
| hutF | PP_5036 | Q88CZ3 | Formimidoylglutamate deiminase | 3.5.3.13 | 4 | 1 | COVERED |
| hutG | PP_5029 | Q88D00 | N-formylglutamate deformylase | 3.5.1.68 | 5 | 1 | COVERED |

**Evidence type.** Assignments rest on (a) UniProt/genome annotation of the contiguous PP_5029–PP_5036 cluster in the KT2440 proteome, and (b) strong congeneric biochemical genetics. The classic *Pseudomonas* work established exactly this five-step route — "successive formation of urocanate, imidazol-4-on-5-ylpropionate, N-formimino-l-glutamate, N-formyl-l-glutamate and glutamate" ([PMID: 4146796](https://pubmed.ncbi.nlm.nih.gov/4146796/)) — and *P. fluorescens* SBW25 genetics showed that "inactivation of hutF eliminated the ability to grow on histidine, indicating that SBW25 degrades histidine by the five-step enzymatic pathway" ([PMID: 17717196](https://pubmed.ncbi.nlm.nih.gov/17717196/)). Both are strong transfers to the congeneric KT2440, whose cluster carries the identical gene set. Genetic control of the *P. putida* histidine dissimilatory pathway was also mapped historically ([PMID: 4405673](https://pubmed.ncbi.nlm.nih.gov/4405673/)).

**Curation caveat on HutU (PP_5033).** The metadata label carries a spurious secondary description ("Imidazolonepropionate hydrolase"). HutU is urocanate hydratase (EC 4.2.1.49); imidazolone-propionate hydrolysis is HutI's reaction. This alias should be cleaned to avoid confusing the EC 3.5.2.7 step with the EC 4.2.1.49 step.

### 4.2 Ancillary in-scope genes

| Gene | Locus | UniProt | Role | Evidence | Assessment |
|------|-------|---------|------|----------|------------|
| hutT | PP_5031 | — | L-histidine:H⁺ symporter (major uptake) | **Direct KT2440 IDA** — Δ*hutT* growth defect; reconstituted transporter | COVERED (transport) |
| hutC | PP_5035 | — | Hut pathway repressor (helix-turn-helix) | Homology to *P. putida* / *K. aerogenes* HutC | COVERED (regulation) |
| hutD | PP_5034 | Q88CZ5 | Accessory; Pfam PF05962 (HutD), RmlC-like cupin | Domain assignment (InterPro IPR010282) | COVERED (accessory) |

**HutT direct evidence.** In KT2440, "deletion of hutT severely impairs growth of P. putida on histidine, suggesting that the encoded transporter is the major histidine uptake system of P. putida" ([PMID: 34245008](https://pubmed.ncbi.nlm.nih.gov/34245008/)). This is the strongest, target-strain-specific functional confirmation that the *hut* system is active and that histidine is a genuine growth substrate.

**HutD identification.** PP_5034 was uncharacterized in the base label but sits in the 3' region of *hutC*. It carries Pfam PF05962 / InterPro IPR010282 (HutD domain) plus RmlC-like cupin folds, identifying it as **HutD**, the conserved accessory protein of the *hut* operon.

### 4.3 Out-of-scope candidates (histidine biosynthesis — over-propagated)

These are **de novo histidine biosynthesis** genes captured only because KEGG ppu00340 merges biosynthesis and degradation. They should be **excluded from this module's satisfiability scoring**.

| Gene | Locus | Role (biosynthesis) | EC |
|------|-------|--------------------|----|
| hisG | PP_0965 | ATP phosphoribosyltransferase | 2.4.2.17 |
| hisD | PP_0966 | Histidinol dehydrogenase | 1.1.1.23 |
| hisC | PP_0967 | Histidinol-phosphate aminotransferase | 2.6.1.9 |
| hisB | PP_0289 | Imidazoleglycerol-phosphate dehydratase | 4.2.1.19 |
| hisH | PP_0290 | IGP synthase glutaminase subunit | 4.3.2.10 / 3.5.1.2 |
| hisA | PP_0292 | ProFAR isomerase | 5.3.1.16 |
| hisF | PP_0293 | IGP synthase cyclase subunit | 4.3.2.10 |
| hisI | PP_5014 | Phosphoribosyl-AMP cyclohydrolase | 3.5.4.19 |
| hisE | PP_5015 | Phosphoribosyl-ATP pyrophosphatase | 3.6.1.31 |
| hisZ | PP_4890 | ATP-PRT regulatory subunit | — |
| PP_3157 | PP_3157 | Histidinol-phosphatase | 3.1.3.15 |
| PP_5147 | PP_5147 | Histidinol-phosphatase | 3.1.3.15 |
| PP_1721 | PP_1721 | Phosphoserine phosphatase (broad 3.1.3.-) | 3.1.3.- |

### 4.4 Unrelated cross-mapped candidates

| Gene | Locus | Actual role | Why mis-mapped |
|------|-------|-------------|----------------|
| gshA | PP_0243 | Glutamate–cysteine ligase (glutathione) | Shared metabolite (glutamate) |
| PP_4983 | PP_4983 | Tryptophan 2-monooxygenase | From ppu00350; spurious cross-map |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### No genuine enzymatic gaps
Every core catabolic step (1–5) has a dedicated single-copy gene in the PP_5029–PP_5036 operon. There are **no missing steps** and **no reliance on hypothetical paralogs**. The module does not require any `candidate_uncertain` enzymatic step.

### Terminal alternatives confirmed absent (not gaps)
A proteome-wide UniProt search of KT2440 (organism_id 160488) returned **zero proteins** for:
- EC 2.1.2.5 — glutamate formimidoyltransferase (FTCD, transfer half)
- EC 4.3.1.4 — formimidoyltetrahydrofolate cyclodeaminase (FTCD, cyclodeaminase half)
- EC 3.5.3.8 — formimidoylglutamase (Bacillus-type route)
- Zero text hits for "formimino"/"formiminotransferase."

Therefore the folate-coupled and *Bacillus*-type routes are correctly `not_expected_in_target_taxon` — their absence is a **true negative**, not a coverage gap. KT2440 exclusively runs the HutF/HutG formate branch.

### Single-copy status (contrast with a relative)
Each *hut* enzyme is present in exactly one copy in KT2440. This differs from *P. fluorescens* SBW25, which carries **two *hutH* copies** (one nonfunctional) ([PMID: 17717196](https://pubmed.ncbi.nlm.nih.gov/17717196/)). KT2440 has no such paralog ambiguity, simplifying curation.

### Over-annotation issues to flag
1. **KEGG map over-propagation (primary issue).** 15 of 20 candidates are out-of-scope. The combined biosynthesis+degradation KEGG map is the root cause. This is a **module boundary problem**, not a biology problem.
2. **HutU alias contamination** (see 4.1) — "imidazolonepropionate hydrolase" should be removed from PP_5033.
3. **Broad-EC phosphatases** — PP_1721 (EC 3.1.3.-) and the two histidinol-phosphatases (PP_3157, PP_5147, EC 3.1.3.15) have broad/ambiguous mappings and belong to biosynthesis, not catabolism.

---

## 6. Module and GO-Curation Recommendations

### Step-level verdicts

| Module step | Gene(s) | Verdict |
|-------------|---------|---------|
| 1. Histidine deamination (HutH) | PP_5032 | **covered** |
| 2. Urocanate hydration (HutU) | PP_5033 | **covered** |
| 3. Imidazolone ring opening (HutI) | PP_5030 | **covered** |
| 4. FIGLU deimination (HutF) | PP_5036 | **covered** |
| 5. N-formylglutamate deformylation (HutG) | PP_5029 | **covered** |
| Transport (HutT) | PP_5031 | **covered** (direct KT2440 evidence) |
| Regulation (HutC) | PP_5035 | **covered** |
| Accessory (HutD) | PP_5034 | **covered** |
| Bacillus formimidoylglutamase route (EC 3.5.3.8) | — | **not_expected_in_target_taxon** |
| Folate FTCD route (EC 2.1.2.5 + 4.3.1.4) | — | **not_expected_in_target_taxon** |

### Module-level actions
- **Overall module verdict: COVERED.** The histidine→glutamate module is fully satisfiable via the single-copy HutF/HutG formate route.
- **`module_needs_revision` (boundaries only).** The module is currently bound to KEGG ppu00340, a combined biosynthesis+degradation map. **Rebind to KEGG M00045 / MetaCyc PWY-5030** and remove the 15 over-propagated candidates from module scoring (hisG/D/C/B/H/A/F/I/E, hisZ, PP_1721, PP_3157, PP_5147, gshA, PP_4983).
- **No new module documents needed** — the generic module structure already models the correct (formate) branch; KT2440 simply uses one of the three modeled alternatives.
- **No new GO terms required.** Existing GO terms cover all reactions: histidine catabolic process to glutamate, histidine ammonia-lyase activity (GO:0004397), urocanate hydratase activity (GO:0016153), imidazolonepropionase activity (GO:0050480), formimidoylglutamate deiminase activity (GO:0050415), N-formylglutamate deformylase activity (GO:0050129). The *hut* genes should be checked to ensure these specific GO annotations are present rather than only broad parent terms.

---

## 7. Genes to Promote to Full `fetch-gene` Review

| Gene | Locus | Reason for promotion |
|------|-------|----------------------|
| hutF | PP_5036 | Terminal-branch determinant (EC 3.5.3.13); its presence is what fixes KT2440 in the formate route vs. alternatives — verify sequence/annotation directly |
| hutG | PP_5029 | Terminal deformylase (EC 3.5.1.68); confirm activity annotation and that it is the true route terminus |
| hutD (PP_5034) | PP_5034 | Newly identified as HutD from domain evidence (PF05962) but base label was "uncharacterized"; promote to formalize the annotation |
| hutU | PP_5033 | Alias cleanup required ("imidazolonepropionate hydrolase" erroneous); confirm EC 4.2.1.49 only |

Lower priority: HutH (PP_5032), HutI (PP_5030), and HutT (PP_5031) are well-supported (HutT has direct KT2440 evidence) and need review only if annotation harmonization is desired.

---

## 8. Mechanistic Interpretation (Synthesis)

KT2440 packages the entire histidine-utilization function into a single genomic neighborhood, a hallmark of the *Pseudomonas hut* system:

```
Genomic organization (PP_5029–PP_5036):

 PP_5029  PP_5030  PP_5031  PP_5032  PP_5033  PP_5034  PP_5035  PP_5036
  hutG     hutI     hutT     hutH     hutU     hutD     hutC     hutF
 (5.1.68) (3.5.2.7)(transp) (4.3.1.3)(4.2.1.49)(access)(repress)(3.5.3.13)
   |________|________|________|________|________|________|________|
        one contiguous, single-copy cluster; His as C+N source
```

Functionally the flow is: **HutT imports histidine** → **HutH deaminates** it (NH₃ #1) → **HutU hydrates** urocanate → **HutI opens** the imidazolone ring to FIGLU → **HutF deiminates** FIGLU (NH₃ #2) to N-formyl-glutamate → **HutG deformylates** (formate) to **glutamate**. Glutamate then enters central metabolism, and its handling is itself regulated (AauR-AauS, [PMID: 17021207](https://pubmed.ncbi.nlm.nih.gov/17021207/)). Expression of the pathway is repressed by HutC and integrated into global C/N control via CbrA/B and NtrC, which is why growth on histidine as a sole C/N source depends on this regulatory network ([PMID: 20553554](https://pubmed.ncbi.nlm.nih.gov/20553554/), [25031426](https://pubmed.ncbi.nlm.nih.gov/25031426/)). A notable maturation detail: urocanase (HutU) requires an α-ketobutyrate prosthetic group whose biosynthesis depends on threonine dehydratase ([PMID: 4154935](https://pubmed.ncbi.nlm.nih.gov/4154935/)) — a dependency worth noting if urocanase activity is ever assayed but not relevant to gene-level module satisfiability.

The key curatorial insight is the mismatch between **biology** (a clean, complete, single-copy formate route) and **bookkeeping** (a KEGG bucket that dumps 15 unrelated biosynthesis/cross-mapped genes into the same list). The module is satisfiable; the candidate list is noisy.

---

## 9. Evidence Base

| PMID | Organism | Relevance | Strength for KT2440 |
|------|----------|-----------|---------------------|
| [4146796](https://pubmed.ncbi.nlm.nih.gov/4146796/) | *Pseudomonas testosteroni* | Establishes the five-step formate route (urocanate → imidazolone-propionate → N-formimino-Glu → N-formyl-Glu → Glu) | Strong (route definition) |
| [17717196](https://pubmed.ncbi.nlm.nih.gov/17717196/) | *P. fluorescens* SBW25 | Δ*hutF* abolishes histidine growth → HutF-dependent five-step route; also documents duplicate *hutH* | Strong congeneric transfer |
| [4405673](https://pubmed.ncbi.nlm.nih.gov/4405673/) | *P. putida* | Genetic control of the histidine dissimilatory pathway | Strong (same species) |
| [34245008](https://pubmed.ncbi.nlm.nih.gov/34245008/) | ***P. putida* KT2440** | Δ*hutT* growth defect; HutT is the major histidine:H⁺ symporter | **Direct target strain** |
| [20553554](https://pubmed.ncbi.nlm.nih.gov/20553554/) | *P. putida* | CbrAB required for assimilation of histidine (and proline/arginine) as C/N sources | Direct species regulatory |
| [25031426](https://pubmed.ncbi.nlm.nih.gov/25031426/) | *P. putida* / *P. aeruginosa* | CbrA/B/CrcZ(Y) carbon-catabolite-repression signaling operates similarly across species | Species-level context |
| [2203754](https://pubmed.ncbi.nlm.nih.gov/2203754/) | *Klebsiella aerogenes* | HutC repressor sequence; notes strong similarity to *P. putida* HutC | Supports HutC (PP_5035) assignment |
| [4154935](https://pubmed.ncbi.nlm.nih.gov/4154935/) | *P. putida* | Urocanase prosthetic group (α-ketobutyrate) biosynthesis via threonine dehydratase | Mechanistic detail on HutU maturation |
| [9561727](https://pubmed.ncbi.nlm.nih.gov/9561727/) | *P. syringae* (+ *P. putida* assay) | *hut* operon (urocanase/histidase) upregulated at low temperature | Genus-level regulation |
| [17021207](https://pubmed.ncbi.nlm.nih.gov/17021207/) | *P. putida* KT2440 | AauR-AauS two-component control of acidic amino acid (Glu) uptake/metabolism | Downstream glutamate handling context |

**Direct vs. inferred summary.** The strongest, *directly experimental* evidence for the target strain is the HutT transporter phenotype ([PMID: 34245008](https://pubmed.ncbi.nlm.nih.gov/34245008/)) and the CbrAB regulatory requirement ([PMID: 20553554](https://pubmed.ncbi.nlm.nih.gov/20553554/)), both confirming histidine is used as a C/N source in KT2440. The **enzymatic step assignments** rest on genome/UniProt annotation of the KT2440 cluster combined with strong biochemical genetics from congeneric *Pseudomonas* ([PMID: 4146796](https://pubmed.ncbi.nlm.nih.gov/4146796/), [17717196](https://pubmed.ncbi.nlm.nih.gov/17717196/), [4405673](https://pubmed.ncbi.nlm.nih.gov/4405673/)) — high-confidence homology transfer, not direct KT2440 enzymology for each individual enzyme.

---

## 10. Limitations and Knowledge Gaps

- **Per-enzyme direct biochemistry in KT2440 is limited.** The step assignments for HutH/HutU/HutI/HutF/HutG rely on genome annotation plus congeneric genetics, not on purified-enzyme assays from KT2440 itself. Transfer is strong (same genus, identical cluster) but not experimentally verified enzyme-by-enzyme in the target strain.
- **HutD function.** PP_5034 is confidently a HutD-domain protein (PF05962), but the precise biochemical role of HutD in the pathway remains generally under-characterized across bacteria.
- **No KT2440-specific *hut*-regulation study** was found beyond the transporter and global CbrAB/NtrC work; fine regulatory detail (HutC operator sites, inducer specificity in KT2440) is inferred from other *Pseudomonas*/*Klebsiella*.
- **Proteome search scope.** Absence of the FTCD/formimidoylglutamase routes was established by UniProt EC and text searches; this is robust but is an annotation-based negative rather than an experimental one.

---

## 11. Proposed Follow-up Actions

1. **Rebind the module** from KEGG ppu00340 to KEGG M00045 / MetaCyc PWY-5030 and remove the 15 over-propagated candidates from satisfiability scoring. (Curation action — highest priority.)
2. **Clean the HutU (PP_5033) annotation** to remove the erroneous "imidazolonepropionate hydrolase" alias.
3. **Formalize HutD (PP_5034)** annotation from "uncharacterized" to "HutD (PF05962)" and promote to `fetch-gene`.
4. **Promote HutF, HutG, HutU, HutD** to full gene review (Section 7).
5. **Verify specific GO annotations** (GO:0004397, GO:0016153, GO:0050480, GO:0050415, GO:0050129) are attached to the respective *hut* genes rather than only broad parents.
6. **Optional experimental confirmation** (if a wet-lab arm exists): construct Δ*hutH*, Δ*hutF*, Δ*hutG* single mutants in KT2440 and confirm loss of growth on histidine as sole C/N source, mirroring the SBW25 Δ*hutF* result — this would upgrade the enzymatic steps from homology-inferred to direct target-strain evidence.

---

## 12. Key References

- [PMID: 34245008](https://pubmed.ncbi.nlm.nih.gov/34245008/) — HutT is the major L-histidine transporter in *P. putida* KT2440 (direct target-strain evidence).
- [PMID: 17717196](https://pubmed.ncbi.nlm.nih.gov/17717196/) — Genetic analysis of *hut* genes in *P. fluorescens* SBW25; Δ*hutF* abolishes histidine growth.
- [PMID: 4146796](https://pubmed.ncbi.nlm.nih.gov/4146796/) — Degradation of L-histidine via the five-step formate route in *Pseudomonas*.
- [PMID: 4405673](https://pubmed.ncbi.nlm.nih.gov/4405673/) — Genetic control of the histidine dissimilatory pathway in *P. putida*.
- [PMID: 20553554](https://pubmed.ncbi.nlm.nih.gov/20553554/) — CbrB and amino-acid (histidine) assimilation in *P. putida*.
- [PMID: 25031426](https://pubmed.ncbi.nlm.nih.gov/25031426/) — CbrA/B carbon-source management in *P. putida* / *P. aeruginosa*.
- [PMID: 2203754](https://pubmed.ncbi.nlm.nih.gov/2203754/) — HutC repressor sequence; similarity to *P. putida* HutC.
- [PMID: 4154935](https://pubmed.ncbi.nlm.nih.gov/4154935/) — Urocanase α-ketobutyrate prosthetic group biosynthesis in *P. putida*.
- [PMID: 17021207](https://pubmed.ncbi.nlm.nih.gov/17021207/) — AauR-AauS control of glutamate metabolism in *P. putida* KT2440.
- [PMID: 9561727](https://pubmed.ncbi.nlm.nih.gov/9561727/) — Temperature regulation of the *hut* operon in *Pseudomonas*.

---

*Review complete. Overall module verdict: **COVERED** via the single-copy HutF/HutG formate route (PP_5029–PP_5036), with direct KT2440 evidence for transport and regulation, terminal alternatives verified absent, and candidate-list boundaries flagged for revision (rebind to KEGG M00045 / MetaCyc PWY-5030).*


## Artifacts

- [OpenScientist final report](PSEPK__histidine_catabolism__ppu00340-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__histidine_catabolism__ppu00340-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:34245008
2. PMID:20553554
3. PMID:4146796
4. PMID:17717196
5. PMID:4405673
6. PMID:17021207
7. PMID:4154935
8. PMID:25031426
9. PMID:2203754
10. PMID:9561727