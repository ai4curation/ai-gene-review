---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T12:16:31.300823'
end_time: '2026-07-25T12:32:43.130799'
duration_seconds: 971.83
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-lysine catabolism through 5-aminovalerate
  module_summary: A reusable four-reaction Dav pathway that converts L-lysine to glutarate
    through 5-aminopentanamide, 5-aminopentanoate (5-aminovalerate), and 5-oxopentanoate
    (glutarate semialdehyde). The module represents the DavB, DavA, DavT, and DavD
    reaction roles independently of genomic organization. Downstream CoA-dependent
    and CoA-independent routes from glutarate to central metabolism are outside the
    boundary.
  module_outline: "- L-lysine catabolism through 5-aminovalerate\n  - 1. 5-aminopentanamide\
    \ formation\n  - L-lysine 2-monooxygenase\n    - L-lysine 2-monooxygenase (molecular\
    \ player: flavin monoamine oxidase family; activity or role: lysine 2-monooxygenase\
    \ activity)\n  - 2. 5-aminovalerate formation\n  - 5-aminopentanamidase\n    -\
    \ 5-aminopentanamidase (molecular player: carbon-nitrogen hydrolase superfamily;\
    \ activity or role: 5-aminopentanamidase activity)\n  - 3. glutarate-semialdehyde\
    \ formation\n  - 5-aminovalerate aminotransferase\n    - 5-aminovalerate aminotransferase\
    \ (molecular player: class III aminotransferases; activity or role: 5-aminovalerate:2-oxoglutarate\
    \ transaminase activity)\n  - 4. glutarate formation\n  - Glutarate-semialdehyde\
    \ dehydrogenase\n    - Glutarate-semialdehyde dehydrogenase (molecular player:\
    \ aldehyde dehydrogenase family; activity or role: glutarate-semialdehyde dehydrogenase\
    \ (NADP+) activity)"
  module_connections: '- L-lysine 2-monooxygenase feeds into 5-aminopentanamidase:
    DavB supplies 5-aminopentanamide to DavA.

    - 5-aminopentanamidase feeds into 5-aminovalerate aminotransferase: DavA supplies
    5-aminovalerate to DavT.

    - 5-aminovalerate aminotransferase feeds into Glutarate-semialdehyde dehydrogenase:
    DavT supplies glutarate semialdehyde to DavD.'
  pathway_query: ppu00310
  pathway_id: ppu00310
  pathway_name: Lysine degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00310 with 13 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '32'
  candidate_genes: '- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC
    1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)

    - PP_0159: PP_0159 | Q88RH1 | CoA-transferase family III (EC 2.8.3.-) (EC 2.8.3.-;
    primary bucket kegg:ppu00310)

    - davD: PP_0213 | Q88RC0 | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) (EC
    1.2.1.-; primary bucket kegg:ppu00350)

    - davT: PP_0214 | Q88RB9 | 5-aminovalerate aminotransferase DavT (EC 2.6.1.48)
    (5-aminovalerate transaminase) (Delta-aminovalerate aminotransferase) (EC 2.6.1.48;
    primary bucket kegg:ppu00310)

    - davA: PP_0382 | Q88QV2 | 5-aminopentanamidase (EC 3.5.1.30) (EC 3.5.1.30; primary
    bucket kegg:ppu00310)

    - davB: PP_0383 | Q88QV1 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3;
    primary bucket kegg:ppu00310)

    - PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)

    - patD: PP_1481 | Q88MT7 | Medium chain aldehyde dehydrogenase (EC 1.2.1.19, EC
    1.2.1.54) (EC 1.2.1.19; 1.2.1.54; primary bucket kegg:ppu00410)

    - fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes:
    Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA
    epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase
    (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)

    - PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - sad-I: PP_2488 | Q88K05 | NAD+-dependent succinate semialdehyde dehydrogenase
    (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00350)

    - prr: PP_2801 | Q88J48 | Gamma-aminobutyraldehyde dehydrogenase (EC 1.2.1.19)
    (EC 1.2.1.19; primary bucket kegg:ppu00410)

    - glaH: PP_2909 | Q88IU0 | Glutarate 2-hydroxylase (G-2-H) (EC 1.14.11.64) (EC
    1.14.11.64; primary bucket kegg:ppu00310)

    - lhgO: PP_2910 | Q88IT9 | L-2-hydroxyglutarate oxidase (EC 1.1.3.15) (EC 1.1.3.15;
    primary bucket kegg:ppu00310)

    - paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)

    - dpkA: PP_3591 | Q88GX6 | Delta(1)-pyrroline-2-carboxylate/Delta(1)-piperideine-2-carboxylate
    reductase (EC 1.5.1.21) (EC 1.5.1.21; primary bucket kegg:ppu00310)

    - amaD: PP_3596 | Q88GX1 | D-lysine oxidase (EC 1.4.3.-) (EC 1.4.3.-; primary
    bucket kegg:ppu00310)

    - alr: PP_3722 | Q88GJ9 | Broad specificity amino-acid racemase (EC 5.1.1.10)
    (Broad spectrum racemase) (EC 5.1.1.10; primary bucket kegg:ppu00470)

    - bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC
    2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)

    - PP_4108: PP_4108 | Q88FI7 | 2-aminoadipate transaminase (EC 2.6.1.39) (2-aminoadipate
    aminotransferase) (L-2AA aminotransferase) (EC 2.6.1.39; primary bucket kegg:ppu00310)

    - lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - sucB: PP_4188 | Q88FB0 | Dihydrolipoyllysine-residue succinyltransferase component
    of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxoglutarate dehydrogenase
    complex component E2) (EC 2.3.1.61; primary bucket kegg:ppu00785)

    - lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - gabD-II: PP_4422 | Q88EN2 | Succinate-semialdehyde dehydrogenase (NADP+) (EC
    1.2.1.79) (EC 1.2.1.79; primary bucket kegg:ppu00350)

    - ydiJ: PP_4493 | Q88EH0 | D-2-hydroxyglutarate dehydrogenase (D2HGDH) (EC 1.1.99.39)
    (EC 1.1.99.39; primary bucket kegg:ppu00310)

    - yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - amaA: PP_5257 | Q88CC4 | L-pipecolate oxidase (EC 1.5.3.7) (EC 1.5.3.7; primary
    bucket kegg:ppu00310)

    - amaB: PP_5258 | Q88CC3 | aldehyde dehydrogenase (NAD(+)) (EC 1.2.1.3) (EC 1.2.1.3;
    primary bucket kegg:ppu00310)

    - hglS: PP_5260 | Q88CC1 | 2-oxoadipate dioxygenase/decarboxylase (EC 1.13.11.93)
    (2-hydroxyglutarate synthase) (EC 1.13.11.93; primary bucket kegg:ppu00310)

    - lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__lysine_dav_catabolism__ppu00310-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__lysine_dav_catabolism__ppu00310-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-lysine catabolism through 5-aminovalerate in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00310
- Resolved ID: ppu00310
- Resolved name: Lysine degradation
- Source: KEGG

Resolved local bucket kegg:ppu00310 with 13 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 32

- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)
- PP_0159: PP_0159 | Q88RH1 | CoA-transferase family III (EC 2.8.3.-) (EC 2.8.3.-; primary bucket kegg:ppu00310)
- davD: PP_0213 | Q88RC0 | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) (EC 1.2.1.-; primary bucket kegg:ppu00350)
- davT: PP_0214 | Q88RB9 | 5-aminovalerate aminotransferase DavT (EC 2.6.1.48) (5-aminovalerate transaminase) (Delta-aminovalerate aminotransferase) (EC 2.6.1.48; primary bucket kegg:ppu00310)
- davA: PP_0382 | Q88QV2 | 5-aminopentanamidase (EC 3.5.1.30) (EC 3.5.1.30; primary bucket kegg:ppu00310)
- davB: PP_0383 | Q88QV1 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3; primary bucket kegg:ppu00310)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- patD: PP_1481 | Q88MT7 | Medium chain aldehyde dehydrogenase (EC 1.2.1.19, EC 1.2.1.54) (EC 1.2.1.19; 1.2.1.54; primary bucket kegg:ppu00410)
- fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- sad-I: PP_2488 | Q88K05 | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00350)
- prr: PP_2801 | Q88J48 | Gamma-aminobutyraldehyde dehydrogenase (EC 1.2.1.19) (EC 1.2.1.19; primary bucket kegg:ppu00410)
- glaH: PP_2909 | Q88IU0 | Glutarate 2-hydroxylase (G-2-H) (EC 1.14.11.64) (EC 1.14.11.64; primary bucket kegg:ppu00310)
- lhgO: PP_2910 | Q88IT9 | L-2-hydroxyglutarate oxidase (EC 1.1.3.15) (EC 1.1.3.15; primary bucket kegg:ppu00310)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- dpkA: PP_3591 | Q88GX6 | Delta(1)-pyrroline-2-carboxylate/Delta(1)-piperideine-2-carboxylate reductase (EC 1.5.1.21) (EC 1.5.1.21; primary bucket kegg:ppu00310)
- amaD: PP_3596 | Q88GX1 | D-lysine oxidase (EC 1.4.3.-) (EC 1.4.3.-; primary bucket kegg:ppu00310)
- alr: PP_3722 | Q88GJ9 | Broad specificity amino-acid racemase (EC 5.1.1.10) (Broad spectrum racemase) (EC 5.1.1.10; primary bucket kegg:ppu00470)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- PP_4108: PP_4108 | Q88FI7 | 2-aminoadipate transaminase (EC 2.6.1.39) (2-aminoadipate aminotransferase) (L-2AA aminotransferase) (EC 2.6.1.39; primary bucket kegg:ppu00310)
- lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- sucB: PP_4188 | Q88FB0 | Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex (EC 2.3.1.61) (2-oxoglutarate dehydrogenase complex component E2) (EC 2.3.1.61; primary bucket kegg:ppu00785)
- lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- gabD-II: PP_4422 | Q88EN2 | Succinate-semialdehyde dehydrogenase (NADP+) (EC 1.2.1.79) (EC 1.2.1.79; primary bucket kegg:ppu00350)
- ydiJ: PP_4493 | Q88EH0 | D-2-hydroxyglutarate dehydrogenase (D2HGDH) (EC 1.1.99.39) (EC 1.1.99.39; primary bucket kegg:ppu00310)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- amaA: PP_5257 | Q88CC4 | L-pipecolate oxidase (EC 1.5.3.7) (EC 1.5.3.7; primary bucket kegg:ppu00310)
- amaB: PP_5258 | Q88CC3 | aldehyde dehydrogenase (NAD(+)) (EC 1.2.1.3) (EC 1.2.1.3; primary bucket kegg:ppu00310)
- hglS: PP_5260 | Q88CC1 | 2-oxoadipate dioxygenase/decarboxylase (EC 1.13.11.93) (2-hydroxyglutarate synthase) (EC 1.13.11.93; primary bucket kegg:ppu00310)
- lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)

## Generic Module Context

### Working Scope

A reusable four-reaction Dav pathway that converts L-lysine to glutarate through 5-aminopentanamide, 5-aminopentanoate (5-aminovalerate), and 5-oxopentanoate (glutarate semialdehyde). The module represents the DavB, DavA, DavT, and DavD reaction roles independently of genomic organization. Downstream CoA-dependent and CoA-independent routes from glutarate to central metabolism are outside the boundary.

### Provisional Biological Outline

- L-lysine catabolism through 5-aminovalerate
  - 1. 5-aminopentanamide formation
  - L-lysine 2-monooxygenase
    - L-lysine 2-monooxygenase (molecular player: flavin monoamine oxidase family; activity or role: lysine 2-monooxygenase activity)
  - 2. 5-aminovalerate formation
  - 5-aminopentanamidase
    - 5-aminopentanamidase (molecular player: carbon-nitrogen hydrolase superfamily; activity or role: 5-aminopentanamidase activity)
  - 3. glutarate-semialdehyde formation
  - 5-aminovalerate aminotransferase
    - 5-aminovalerate aminotransferase (molecular player: class III aminotransferases; activity or role: 5-aminovalerate:2-oxoglutarate transaminase activity)
  - 4. glutarate formation
  - Glutarate-semialdehyde dehydrogenase
    - Glutarate-semialdehyde dehydrogenase (molecular player: aldehyde dehydrogenase family; activity or role: glutarate-semialdehyde dehydrogenase (NADP+) activity)

### Known Relationships Among Steps

- L-lysine 2-monooxygenase feeds into 5-aminopentanamidase: DavB supplies 5-aminopentanamide to DavA.
- 5-aminopentanamidase feeds into 5-aminovalerate aminotransferase: DavA supplies 5-aminovalerate to DavT.
- 5-aminovalerate aminotransferase feeds into Glutarate-semialdehyde dehydrogenase: DavT supplies glutarate semialdehyde to DavD.

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

# Species-Aware Module Review: L-Lysine Catabolism through 5-Aminovalerate in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module scope:** Four-reaction Dav pathway L-lysine → 5-aminovaleramide → 5-aminovalerate → glutarate semialdehyde → glutarate
**Local bucket:** KEGG ppu00310 "Lysine degradation" (32 candidate genes, 13 primary)
**Date:** 2026-07-25

---

## 1. Executive Summary

The four-reaction Dav module (DavB → DavA → DavT → DavD) that converts L-lysine to
glutarate via 5-aminovalerate is **fully covered and experimentally validated** in
*P. putida* KT2440. All four reaction roles map to characterized, adjacent-operon genes
with **direct target-organism evidence**: `davB` (PP_0383), `davA` (PP_0382), `davT`
(PP_0214), `davD` (PP_0213). This is the primary/major L-lysine catabolic route in
KT2440 (Revelles et al. 2005, PMID 16237033).

Two curation issues dominate:

1. **DavB (PP_0383) is misannotated** in local metadata as "Tryptophan 2-monooxygenase
   (EC 1.13.12.3)." The experimentally supported activity is **L-lysine 2-monooxygenase
   (EC 1.13.12.2)** (Liu 2014; Kim 2019; Revelles 2005). Recommend EC/name correction.
2. **The candidate list is a broad-map over-inclusion.** Only **4 of 32** candidates are
   core module genes. ~28 belong to (a) the *parallel* D-lysine/L-pipecolate/2-aminoadipate
   route, (b) *downstream* glutarate catabolism (outside the module boundary), or
   (c) generic β-oxidation / 2-oxoacid-dehydrogenase housekeeping enzymes.

No module step is a gap or "not expected." The module is satisfiable; the work needed is
scoping/annotation cleanup, not gap-filling.

---

## 2. Target-Organism Pathway Definition

**Included process:** Aerobic oxidative deamination of L-lysine to glutarate through the
"aminovalerate (Dav) pathway":

1. L-lysine + O₂ → 5-aminopentanamide (δ-aminovaleramide) + CO₂ + H₂O — flavin-dependent
   monooxygenase (DavB).
2. 5-aminopentanamide + H₂O → 5-aminopentanoate (5-aminovalerate) + NH₃ — amidohydrolase
   (DavA).
3. 5-aminovalerate + 2-oxoglutarate → glutarate semialdehyde (5-oxopentanoate) +
   L-glutamate — class-III aminotransferase (DavT).
4. Glutarate semialdehyde + NAD(P)⁺ + H₂O → glutarate + NAD(P)H — aldehyde
   dehydrogenase (DavD).

**Neighboring processes to keep separate (do NOT fold into this module):**

- **Parallel D-lysine / 2-aminoadipate pathway** (KT2440 runs *both* routes simultaneously):
  L-lysine ⇌ D-lysine (racemase `alr`) → Δ¹-piperideine-2-carboxylate → L-pipecolate
  (`dpkA`) → Δ¹-piperideine-6-carboxylate → 2-aminoadipate → 2-oxoadipate → glutaryl-CoA/
  glutarate. Genes: `alr`, `amaC`/PP_3590, `amaD`/PP_3596, `dpkA`/PP_3591, `amaA`/PP_5257,
  `amaB`/PP_5258, PP_4108, `hglS`/PP_5260 (Revelles 2005 PMID 16237033; Revelles 2007
  PMID 17259313; Muramatsu 2005 PMID 15561717). This is a **sibling module**, not this one.
- **Downstream glutarate → central carbon** (explicitly outside module boundary):
  (i) CoA-dependent glutaryl-CoA dehydrogenation (`gcdH`/PP_0158 + CoA-transferase
  PP_0159); (ii) CoA-independent glutarate hydroxylation via L-2-hydroxyglutarate
  (`glaH`/CsiD/PP_2909 + `lhgO`/PP_2910), with `ydiJ`/PP_4493 handling D-2-HG
  (Zhang 2018 PMID 29844506).
- **Generic overview maps / housekeeping:** β-oxidation thiolases and hydratases (`fadB`,
  `bktB`, `yqeF`, `paaF`, PP_0582/2215/2217/3355) and the 2-oxoglutarate/branched-chain
  dehydrogenase E2/E3 components (`sucB`, `lpd`, `lpdG`, `lpdV`) are shared central-metabolism
  enzymes swept in by the broad KEGG map.

**Alternate names / database definitions:** "aminovalerate pathway," "Dav pathway,"
"5-aminovalerate (AMV/AVA) pathway." KEGG ppu00310 ("Lysine degradation") is a broad
overview that **conflates** the Dav module, the aminoadipate module, and downstream
glutarate catabolism. MetaCyc separates "L-lysine degradation I (via cadaverine)" and the
aminovalerate route; the KT2440 route corresponds to the DavBADT segment.

---

## 3. Expected Step Model (Satisfiability)

| # | Reaction role | Enzyme (family) | KT2440 gene | Status |
|---|---------------|-----------------|-------------|--------|
| 1 | 5-aminopentanamide formation | L-lysine 2-monooxygenase (flavin MAO family) | `davB` / PP_0383 | **covered** (direct) |
| 2 | 5-aminovalerate formation | 5-aminopentanamidase (C–N hydrolase superfamily) | `davA` / PP_0382 | **covered** (direct) |
| 3 | glutarate-semialdehyde formation | 5-aminovalerate:2-OG aminotransferase (class III AT) | `davT` / PP_0214 | **covered** (direct); paralog-ambiguity note |
| 4 | glutarate formation | glutarate-semialdehyde dehydrogenase (ALDH family) | `davD` / PP_0213 | **covered** (direct); paralog-ambiguity note |

**No missing steps.** No step is "not expected." Genomic organization: `davAB`
(PP_0382–PP_0383) and `davTD`/`davDT` (PP_0213–PP_0214) are two separate adjacent
operons — the module is encoded across two loci, consistent with the "role independent of
genomic organization" scope.

---

## 4. Candidate Genes and Evidence (Core Module)

**DavB — PP_0383 (Q88QV1). Role:** L-lysine 2-monooxygenase (step 1).
**Evidence:** *Direct, target strain.* Genetic assignment (Revelles 2005); purified-enzyme
biotransformation of L-lysine to 5-aminovalerate with DavA (Liu 2014, PMID 25012259);
repeatedly used as the KT2440 "lysine monooxygenase" part (Adkins 2013; Kim 2019).
**Caveat:** Local EC 1.13.12.3 (tryptophan 2-monooxygenase) is an **over-propagated
misannotation**; correct to EC 1.13.12.2 (L-lysine 2-monooxygenase). Same flavin-amine-
oxidase fold explains the confusion. **Promote to full review** to fix EC/name.

**DavA — PP_0382 (Q88QV2). Role:** 5-aminovaleramidase / δ-aminovaleramidase (step 2).
**Evidence:** *Direct, target strain.* Revelles 2005; purified with DavB (Liu 2014). EC
3.5.1.30 in metadata is consistent. High confidence; caveat minor (the "5-aminopentanamidase"
name vs. common "5-aminovaleramidase" synonym).

**DavT — PP_0214 (Q88RB9). Role:** 5-aminovalerate:2-oxoglutarate aminotransferase (step 3).
**Evidence:** *Direct, target strain.* Named DavT with EC 2.6.1.48; genetic assignment
(Revelles 2005); functions in reconstituted davDT glutarate production (Adkins 2013).
**Caveat:** class-III aminotransferase overlapping with GABA transaminase (GabT); GABA-
pathway paralogs can perform the reaction (Rohles 2016, PMID 27618862). Keep DavT as
primary; add paralog-ambiguity flag.

**DavD — PP_0213 (Q88RC0). Role:** glutarate-semialdehyde dehydrogenase (step 4).
**Evidence:** *Direct, target strain.* Genetic assignment (Revelles 2005); davDT reconstitution
(Adkins 2013). EC 1.2.1.- (NAD(P)+-dependent ALDH). **Caveat:** metadata primary bucket is
ppu00350, and multiple ALDH paralogs (`sad-I`/PP_2488, `gabD-II`/PP_4422, `amaB`/PP_5258,
`patD`/PP_1481, `prr`/PP_2801) share broad EC space. Keep DavD as primary module assignment.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

- **No true gaps.** All four steps covered by direct evidence.
- **DavB EC misannotation** (EC 1.13.12.3 → 1.13.12.2): highest-priority correction.
- **Bucket over-inclusion (pathway-level over-propagation):** ~28/32 candidates are not
  Dav-module genes. They are correctly annotated enzymes placed in the wrong *module*:
  - *Sibling aminoadipate/D-lysine module:* `alr` (PP_3722), `amaD` (PP_3596),
    `dpkA` (PP_3591), `amaA` (PP_5257), `amaB` (PP_5258), PP_4108, `hglS` (PP_5260).
  - *Downstream glutarate catabolism (out of boundary):* `gcdH` (PP_0158), PP_0159,
    `glaH` (PP_2909), `lhgO` (PP_2910), `ydiJ` (PP_4493).
  - *Generic β-oxidation / dehydrogenase housekeeping:* `fadB`, `bktB`, `yqeF`, `paaF`,
    PP_0582/2215/2217/3355, `sucB`, `lpd`, `lpdG`, `lpdV`.
- **Paralog / broad-EC ambiguity** at steps 3–4: multiple class-III aminotransferases and
  ALDHs share EC/GO space with DavT/DavD; automated EC→gene mapping would over-call. Loss
  of `davTD` may be partially buffered by the GABA pathway (Rohles 2016).
- **`amaD`/PP_3596 EC ambiguity:** metadata "D-lysine oxidase (EC 1.4.3.-)" vs. Revelles
  2007's functional assignment as **D-lysine dehydrogenase** — a curation-relevant
  discrepancy, but belongs to the sibling module.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status |
|-------------|--------------------|
| 1. L-lysine 2-monooxygenase (DavB) | **covered** — correct EC to 1.13.12.2 |
| 2. 5-aminopentanamidase (DavA) | **covered** |
| 3. 5-aminovalerate aminotransferase (DavT) | **covered** (paralog-ambiguity note) |
| 4. glutarate-semialdehyde dehydrogenase (DavD) | **covered** (paralog-ambiguity note) |

- **Module boundaries are correct for this organism** as written (module ends at glutarate;
  downstream CoA-dependent and CoA-independent routes excluded). No `module_needs_revision`.
- **Recommend a separate sibling module** for the D-lysine/L-pipecolate/2-aminoadipate route,
  which KT2440 runs simultaneously and which the candidate list currently mixes in.
- **Bucket cleanup:** demote the ~28 non-Dav candidates from this module's satisfiability set
  (retain as pathway-context, not module members).
- **GO terms:** ensure DavB carries GO:0050048 (L-lysine 2-monooxygenase activity), not a
  tryptophan-monooxygenase term; DavA GO:0047622 (5-aminovaleramidase); DavT
  GO:0019481-type / EC 2.6.1.48 transaminase activity; DavD glutarate-semialdehyde
  dehydrogenase activity. No new GO term requests appear necessary.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **PP_0383 / davB** — priority: fix EC 1.13.12.3 → 1.13.12.2 and name; confirm GO.
2. **PP_0213 / davD** and **PP_0214 / davT** — confirm primary bucket (davD currently ppu00350),
   attach paralog-ambiguity note, verify NAD(P)⁺ cofactor preference for davD.
3. **PP_0382 / davA** — light-touch: confirm synonym normalization (5-aminovaleramidase).
4. (Sibling-module, if that module is curated) **PP_3596 / amaD** — resolve oxidase vs.
   dehydrogenase discrepancy (Revelles 2007).

---

## 8. Key References

- Revelles O, Espinosa-Urgel M, Fuhrer T, Sauer U, Ramos JL. **Multiple and interconnected
  pathways for L-lysine catabolism in *Pseudomonas putida* KT2440.** *J Bacteriol* 2005.
  **PMID 16237033.** — Foundational; genetic + ¹³C/¹⁵N-tracing assignment of davB/davA and
  both parallel routes. *Direct target-strain evidence.*
- Liu P, et al. **Enzymatic production of 5-aminovalerate from L-lysine using L-lysine
  monooxygenase and 5-aminovaleramide amidohydrolase.** 2014. **PMID 25012259.** — Purified
  KT2440 DavB + DavA. *Direct.*
- Adkins J, Jordan J, Nielsen DR. **Engineering *E. coli* for renewable production of
  5-aminovalerate and glutarate.** 2013. **PMID 23296991.** — davBA + davDT reconstitution.
  *Parts from KT2440.*
- Kim HT, et al. **Metabolic engineering of *C. glutamicum* for glutaric acid.** 2019.
  **PMID 30144560.** — davB = lysine 2-monooxygenase, davA = δ-aminovaleramidase, davT/davD.
- Rohles CM, et al. **Systems metabolic engineering of *C. glutamicum* for 5-aminovalerate
  and glutarate.** 2016. **PMID 27618862.** — GabT/GSA-DH paralog redundancy for steps 3–4.
- Revelles O, Wittich RM, Ramos JL. **Identification of the initial steps in D-lysine
  catabolism in *P. putida*.** 2007. **PMID 17259313.** — Sibling D-lysine route (amaC/amaD).
- Muramatsu H, et al. **DpkA — Δ¹-piperideine-2-carboxylate/Δ¹-pyrroline-2-carboxylate
  reductase.** 2005. **PMID 15561717.** — Sibling route (dpkA).
- Zhang M, et al. **Increased glutarate production by blocking glutaryl-CoA dehydrogenation
  and an L-2-hydroxyglutarate pathway.** 2018. **PMID 29844506.** — Downstream glutarate
  catabolism (gcdH; CsiD/glaH + lhgO). *Direct target-strain.*

### Evidence character
- **Direct experimental (KT2440):** all four module steps (Revelles 2005; Liu 2014; Zhang 2018).
- **Homology / heterologous parts:** engineering studies transferring KT2440 genes into
  *E. coli*/*C. glutamicum* corroborate function (strong transfer, same genes).
- **Inferred:** paralog redundancy at steps 3–4 (strong mechanistically; from *C. glutamicum*).

### Open questions for experts
- NAD⁺ vs NADP⁺ preference of DavD (PP_0213) in KT2440.
- In-vivo contribution of GABA-pathway paralogs to Dav flux under `davTD` loss.
- Correct EC/functional class of `amaD`/PP_3596 (oxidase vs. dehydrogenase) — sibling module.


## Artifacts

- [OpenScientist final report](PSEPK__lysine_dav_catabolism__ppu00310-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__lysine_dav_catabolism__ppu00310-deep-research-openscientist_artifacts/final_report.pdf)