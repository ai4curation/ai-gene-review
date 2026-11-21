---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T01:00:56.065893'
end_time: '2026-08-11T01:17:09.413865'
duration_seconds: 973.35
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Protocatechuate ortho-cleavage pathway
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00362
  pathway_id: ppu00362
  pathway_name: Benzoate degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00362 with 8 primary genes; module
    area: aromatic_and_xenobiotic_catabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '40'
  candidate_genes: '- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC
    1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)

    - PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)

    - fdx: PP_0847 | Q88PK3 | 2Fe-2S ferredoxin (primary bucket kegg:ppu00362)

    - PP_1218: PP_1218 | Q88NI9 | Acyl-CoA thioesterase (EC 3.1.2.-) (EC 3.1.2.-;
    primary bucket kegg:ppu00130)

    - pcaF-I: PP_1377 | Q88N39 | Beta-ketoadipyl-CoA thiolase (EC 2.3.1.174) (3-oxoadipyl-CoA
    thiolase) (EC 2.3.1.174; primary bucket kegg:ppu00362)

    - pcaB: PP_1379 | Q88N37 | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2)
    (EC 5.5.1.2; primary bucket kegg:ppu01220)

    - pcaD: PP_1380 | Q88N36 | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) (EC 3.1.1.24;
    primary bucket kegg:ppu01220)

    - pcaC: PP_1381 | Q88N35 | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44)
    (EC 4.1.1.44; primary bucket kegg:ppu01220)

    - PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)

    - PP_1950: PP_1950 | Q88LI2 | Cytochrome P450 (primary bucket kegg:ppu00362)

    - fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16)
    (EC 2.3.1.16; primary bucket kegg:ppu00592)

    - fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes:
    Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA
    epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase
    (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)

    - fadA__Q88L01: PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA
    acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta)
    (EC 2.3.1.16; primary bucket kegg:ppu00592)

    - PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate
    tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)

    - galD: PP_2513 | Q88JY0 | 4-oxalomesaconate tautomerase (EC 5.3.2.8) (Gallate
    degradation protein D) (EC 5.3.2.8; primary bucket kegg:ppu00362)

    - galC: PP_2514 | Q88JX9 | 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase (CHA
    aldolase) (EC 4.1.3.17) (Gallate degradation protein C) (EC 4.1.3.17; primary
    bucket kegg:ppu00660)

    - galB: PP_2515 | Q88JX8 | 4-oxalmesaconate hydratase (OMA hydratase) (EC 4.2.1.83)
    (Gallate degradation protein B) (EC 4.2.1.83; primary bucket kegg:ppu00362)

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

    - paaJ: PP_3280 | Q88HS3 | 3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase
    (EC 2.3.1.-, EC 2.3.1.174) (EC 2.3.1.-; 2.3.1.174; primary bucket kegg:ppu00362)

    - paaH: PP_3282 | Q88HS1 | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) (EC
    1.1.1.35; primary bucket kegg:ppu00360)

    - paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)

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

    - bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC
    2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)

    - hbd: PP_3755 | Q88GG9 | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) (EC
    1.1.1.157; primary bucket kegg:ppu00360)

    - pcaI: PP_3951 | Q88FX5 | 3-oxoadipate CoA-transferase (EC 2.8.3.6) (EC 2.8.3.6;
    primary bucket kegg:ppu00362)

    - pcaJ: PP_3952 | P0A101 | 3-oxoadipate CoA-transferase subunit B (EC 2.8.3.6)
    (Beta-ketoadipate:succinyl-CoA transferase subunit B) (EC 2.8.3.6; primary bucket
    kegg:ppu00362)

    - yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - pcaG: PP_4655 | Q88E13 | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3)
    (EC 1.13.11.3; primary bucket kegg:ppu01220)

    - pcaH: PP_4656 | Q88E12 | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3)
    (EC 1.13.11.3; primary bucket kegg:ppu01220)'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__protocatechuate-ortho-cleavage-pathway__ppu00362-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__protocatechuate-ortho-cleavage-pathway__ppu00362-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Protocatechuate ortho-cleavage pathway in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00362
- Resolved ID: ppu00362
- Resolved name: Benzoate degradation
- Source: KEGG

Resolved local bucket kegg:ppu00362 with 8 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 40

- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- fdx: PP_0847 | Q88PK3 | 2Fe-2S ferredoxin (primary bucket kegg:ppu00362)
- PP_1218: PP_1218 | Q88NI9 | Acyl-CoA thioesterase (EC 3.1.2.-) (EC 3.1.2.-; primary bucket kegg:ppu00130)
- pcaF-I: PP_1377 | Q88N39 | Beta-ketoadipyl-CoA thiolase (EC 2.3.1.174) (3-oxoadipyl-CoA thiolase) (EC 2.3.1.174; primary bucket kegg:ppu00362)
- pcaB: PP_1379 | Q88N37 | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2) (EC 5.5.1.2; primary bucket kegg:ppu01220)
- pcaD: PP_1380 | Q88N36 | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) (EC 3.1.1.24; primary bucket kegg:ppu01220)
- pcaC: PP_1381 | Q88N35 | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44) (EC 4.1.1.44; primary bucket kegg:ppu01220)
- PP_1791: PP_1791 | Q88LY5 | Aldolase/synthase (primary bucket kegg:ppu00621)
- PP_1950: PP_1950 | Q88LI2 | Cytochrome P450 (primary bucket kegg:ppu00362)
- fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)
- fadA__Q88L01: PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_2504: PP_2504 | Q88JY9 | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) (EC 5.3.2.6; primary bucket kegg:ppu00621)
- galD: PP_2513 | Q88JY0 | 4-oxalomesaconate tautomerase (EC 5.3.2.8) (Gallate degradation protein D) (EC 5.3.2.8; primary bucket kegg:ppu00362)
- galC: PP_2514 | Q88JX9 | 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase (CHA aldolase) (EC 4.1.3.17) (Gallate degradation protein C) (EC 4.1.3.17; primary bucket kegg:ppu00660)
- galB: PP_2515 | Q88JX8 | 4-oxalmesaconate hydratase (OMA hydratase) (EC 4.2.1.83) (Gallate degradation protein B) (EC 4.2.1.83; primary bucket kegg:ppu00362)
- benA: PP_3161 | Q88I40 | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benB: PP_3162 | Q88I39 | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) (EC 1.14.12.10; primary bucket kegg:ppu00622)
- benC: PP_3163 | Q88I38 | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) (EC 1.14.12.10; 1.18.1.3; primary bucket kegg:ppu00622)
- benD: PP_3164 | Q88I37 | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) (EC 1.3.1.25; primary bucket kegg:ppu00622)
- catA-II: PP_3166 | Q88I35 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- paaJ: PP_3280 | Q88HS3 | 3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase (EC 2.3.1.-, EC 2.3.1.174) (EC 2.3.1.-; 2.3.1.174; primary bucket kegg:ppu00362)
- paaH: PP_3282 | Q88HS1 | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) (EC 1.1.1.35; primary bucket kegg:ppu00360)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- pobA: PP_3537 | Q88H28 | 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2) (EC 1.14.13.2; primary bucket kegg:ppu01220)
- PP_3648: PP_3648 | Q88GS0 | Carboxymuconolactone decarboxylase family protein (primary bucket kegg:ppu01220)
- catA-I: PP_3713 | Q88GK8 | catechol 1,2-dioxygenase (EC 1.13.11.1) (EC 1.13.11.1; primary bucket kegg:ppu00361)
- catC: PP_3714 | Q88GK7 | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4) (EC 5.3.3.4; primary bucket kegg:ppu01220)
- catB: PP_3715 | Q88GK6 | Muconate cycloisomerase 1 (EC 5.5.1.1) (EC 5.5.1.1; primary bucket kegg:ppu00361)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- hbd: PP_3755 | Q88GG9 | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) (EC 1.1.1.157; primary bucket kegg:ppu00360)
- pcaI: PP_3951 | Q88FX5 | 3-oxoadipate CoA-transferase (EC 2.8.3.6) (EC 2.8.3.6; primary bucket kegg:ppu00362)
- pcaJ: PP_3952 | P0A101 | 3-oxoadipate CoA-transferase subunit B (EC 2.8.3.6) (Beta-ketoadipate:succinyl-CoA transferase subunit B) (EC 2.8.3.6; primary bucket kegg:ppu00362)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- pcaG: PP_4655 | Q88E13 | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)
- pcaH: PP_4656 | Q88E12 | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3) (EC 1.13.11.3; primary bucket kegg:ppu01220)

## Generic Module Context

### Working Scope

No module YAML was resolved; use the pathway and taxon context.

### Provisional Biological Outline

No module YAML outline available.

### Known Relationships Among Steps

No module YAML connections available.

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

# Species-Aware Review: Protocatechuate *ortho*-Cleavage Pathway in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Query bucket:** KEGG `ppu00362` "Benzoate degradation" (broad overview map)
**Review topic:** Protocatechuate *ortho*-cleavage pathway (the protocatechuate branch of the β-ketoadipate pathway)
**Date:** 2026-08-11 · Finalized Iteration 5 of 5

---

## 1. Executive Summary

- The **protocatechuate (PCA) *ortho*-cleavage branch of the β-ketoadipate pathway is present and biochemically complete** in *P. putida* KT2440. All six enzymatic steps (protocatechuate → β-ketoadipate → acetyl-CoA + succinyl-CoA) are encoded by high-confidence, well-characterized genes: **pcaG/pcaH, pcaB, pcaC, pcaD, pcaI/pcaJ, pcaF**. The module should be marked **covered / satisfiable**.
- The provided 40-gene candidate list is **exactly the membership of the broad KEGG overview map `ppu00362` "Benzoate degradation"** (verified by `rest.kegg.jp/link/ppu/path:ppu00362`). It is therefore **not** a curated protocatechuate module and contains extensive **annotation over-propagation** (fatty-acid β-oxidation, phenylacetate-CoA, gallate, and generic thiolase genes).
- Only ~**9 genes are true PCA-branch members** (pcaGHBCDIJF + the entry enzyme pobA). A parallel **catechol *ortho*-cleavage branch** (catA/B/C) converges at the same lower pathway and is closely related but should be modelled as a **separate branch**.
- **KEGG has no dedicated "protocatechuate → 3-oxoadipate" module** (only M00568 "Catechol *ortho*-cleavage" exists). A new, tightly-scoped module document is recommended; the generic `ppu00362` boundary is too broad and should be flagged **module_needs_revision**.
- One clear **over-propagation** for curators: **PP_3648** is mapped by KEGG to EC 4.1.1.44 (same as pcaC/PP_1381), but InterPro shows it carries only the generic AhpD-like domain (IPR003779) and lacks the pcaC-specific signature IPR012788 — so it should **not** satisfy the decarboxylation step. The KT2440 regulator **pcaR is PP_1375** (upstream of pcaK), pinning the previously species-transferred regulatory assignment.

---

## 2. Target-Organism Pathway Definition

**Process included.** Intradiol (*ortho*) ring cleavage of protocatechuate (3,4-dihydroxybenzoate) by a non-heme Fe(III) dioxygenase, followed by lactonization, decarboxylation, hydrolysis, CoA transfer, and thiolytic cleavage, yielding the TCA-cycle intermediates **succinyl-CoA + acetyl-CoA**. This is the **protocatechuate branch of the β-ketoadipate pathway** — a chromosomally encoded convergent pathway widely distributed in soil bacteria and fungi (Harwood & Parales, 1996, PMID 8905091).

**Reaction sequence (target-organism gene → EC):**

| # | Reaction | Gene (locus) | EC | KEGG KO |
|---|----------|--------------|----|---------|
| 1 | protocatechuate + O₂ → 3-carboxy-*cis,cis*-muconate | **pcaG** (PP_4655) + **pcaH** (PP_4656) | 1.13.11.3 | K00448/K00449 |
| 2 | 3-carboxy-*cis,cis*-muconate → γ-carboxymuconolactone | **pcaB** (PP_1379) | 5.5.1.2 | K01857 |
| 3 | γ-carboxymuconolactone → β-ketoadipate enol-lactone + CO₂ | **pcaC** (PP_1381) | 4.1.1.44 | K01607 |
| 4 | β-ketoadipate enol-lactone → β-ketoadipate | **pcaD** (PP_1380) | 3.1.1.24 | K01055 |
| 5 | β-ketoadipate + succinyl-CoA → β-ketoadipyl-CoA + succinate | **pcaI** (PP_3951) + **pcaJ** (PP_3952) | 2.8.3.6 | K01031/K01032 |
| 6 | β-ketoadipyl-CoA + CoA → succinyl-CoA + acetyl-CoA | **pcaF** (PP_1377) | 2.3.1.174 | K07823 |

**Entry (boundary) step:** **pobA** (PP_3537, EC 1.14.13.2, p-hydroxybenzoate 3-monooxygenase) converts 4-hydroxybenzoate → protocatechuate and is the canonical feeder reaction (Bertani et al., 2001, PMID 11390692). Protocatechuate is also generated from quinate/shikimate, vanillate, and — after conversion — from other lignin-derived aromatics.

**Alternate names / database definitions.**
- "β-ketoadipate pathway (protocatechuate branch)"; "PCA *ortho*-cleavage"; "protocatechuate 3,4-cleavage pathway"; the enzymes are the *pca* genes.
- KEGG scatters these enzymes across maps `ppu00362` (Benzoate degradation), `ppu00360` (Phenylalanine metabolism), and the overview map `ppu01220` (Degradation of aromatic compounds). MetaCyc groups them under "protocatechuate degradation I (*meta*-cleavage is separate)".

**Neighboring pathways to keep SEPARATE:**
- **Catechol *ortho*-cleavage branch** (catA/B/C → β-ketoadipate enol-lactone): parallel branch of the same β-ketoadipate pathway; converges at pcaD. KEGG module **M00568**.
- **Benzoate 1,2-dioxygenase pathway** (benABCD → catechol): *upstream* of the catechol branch, KEGG map `ppu00622`. A boundary, not part of PCA cleavage.
- **Gallate degradation** (galA + galBCD → 4-oxalomesaconate → pyruvate + oxaloacetate): a **type-II extradiol / 4,5-type** ring cleavage that is *mechanistically distinct from ortho-cleavage* (Nogales et al., 2005, PMID 16030014).
- **Phenylacetate-CoA (paa) pathway**, **fatty-acid β-oxidation (fad)**, and **generic β-ketothiolases** — unrelated central/peripheral pathways that share only EC-class (thiolase/hydratase/dehydrogenase) similarity.

---

## 3. Expected Step Model (satisfiability)

| Step | Expected enzyme | Status in KT2440 | Gene |
|------|-----------------|------------------|------|
| PCA ring cleavage | protocatechuate 3,4-dioxygenase (αβ) | **covered** | pcaG/pcaH |
| cycloisomerization | 3-carboxy-*cis,cis*-muconate cycloisomerase | **covered** | pcaB |
| decarboxylation | γ-carboxymuconolactone decarboxylase | **covered** | pcaC |
| enol-lactone hydrolysis | β-ketoadipate enol-lactone hydrolase | **covered** | pcaD |
| CoA transfer | 3-oxoadipate CoA-transferase (αβ) | **covered** | pcaI/pcaJ |
| thiolysis | β-ketoadipyl-CoA thiolase | **covered** | pcaF |
| substrate uptake | 4-HB/PCA transporter; dicarboxylate permease | **covered (transport)** | pcaK (PP_1376), pcaT (PP_1378) |
| regulation | PcaR (IclR-family activator), induced by β-ketoadipate | **covered (regulatory)** | pcaR (PP_1375) |
| entry from 4-HB | p-hydroxybenzoate 3-monooxygenase | **covered (boundary)** | pobA (PP_3537) |

PcaR (IclR-family activator; KT2440 locus **PP_1375**, UniProt Q88N41, verified by UniProt gene:pcaR query for taxon 160488) sits immediately upstream of pcaK, completing the cluster **pcaR(PP_1375)–pcaK(PP_1376)–pcaF(PP_1377)–pcaT(PP_1378)–pcaB(PP_1379)–pcaD(PP_1380)–pcaC(PP_1381)**. It activates pcaBDC, pcaIJF and pcaK; β-ketoadipate is the inducer, and pcaK (but not pcaF) is additionally repressed by benzoate (Nichols & Harwood, 1995, PMID 8522507). No PCA-branch enzymatic step is missing.

**No steps are "not expected."** The complete pathway is a defining metabolic capability of KT2440 and is directly documented experimentally in *P. putida*.

---

## 4. Candidate Genes and Evidence

### 4a. High-confidence PCA-branch genes (assign to module = **covered**)

- **pcaG (PP_4655) / pcaH (PP_4656)** — protocatechuate 3,4-dioxygenase α/β (EC 1.13.11.3, K00448/K00449). Adjacent on chromosome (verified). Deleting *pcaHG* abolishes PCA degradation in KT2440 (Dias et al., 2023, PMID 36357545). **Evidence: direct (target organism).**
- **pcaB (PP_1379)** — 3-carboxy-*cis,cis*-muconate cycloisomerase (EC 5.5.1.2). In pcaK-pcaF-pcaT-**pcaB**-pcaD-pcaC cluster. **Direct/strong.**
- **pcaC (PP_1381)** — γ-carboxymuconolactone (4-carboxymuconolactone) decarboxylase (EC 4.1.1.44). **Direct/strong.** *Caveat:* a paralog (PP_3648) shares the EC (see §5).
- **pcaD (PP_1380)** — 3-oxoadipate enol-lactonase (EC 3.1.1.24); annotated "enol-lactonase **2**", implying possible isozyme naming. **Direct/strong.**
- **pcaI (PP_3951) / pcaJ (PP_3952)** — 3-oxoadipate CoA-transferase α/β (EC 2.8.3.6). Stand-alone locus next to a chemotaxis transducer (consistent with β-ketoadipate chemotaxis biology). **Direct/strong.** (Note: PP_3952 curated UniProt P0A101.)
- **pcaF (PP_1377)** — β-ketoadipyl-CoA thiolase (EC 2.3.1.174, K07823). Required for **both** benzoate (catechol branch) and 4-HB (PCA branch) degradation; PcaR-regulated (Nichols & Harwood, 1995, PMID 8522507). **Direct/strong.**

### 4b. Pathway-context genes (functionally part of the module, not core cleavage enzymes)

- **pobA (PP_3537)** — 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2). Entry step producing PCA. **Boundary — include as feeder.**
- **pcaK (PP_1376)** and **pcaT (PP_1378)** — 4-HB/PCA MFS transporter and dicarboxylate permease. **Transport steps.**
- **pcaR (PP_1375, UniProt Q88N41)** — IclR-family transcriptional activator of the pca regulon; integral regulatory member of the main cluster. **Regulatory step.**

### 4c. Catechol *ortho*-cleavage branch (parallel branch — model separately, converges at pcaD)

- **catA-I (PP_3713)**, **catA-II (PP_3166)** — catechol 1,2-dioxygenase (EC 1.13.11.1, K03381). Two genuine isozymes: catA-I in the *catBCA/catR* cluster; catA-II embedded in the *ben* cluster (benABCD-benK-**catA-II**-benE), co-induced with benzoate catabolism. **Redundancy is real, not over-propagation.**
- **catB (PP_3715)** — muconate cycloisomerase (EC 5.5.1.1); **catC (PP_3714)** — muconolactone Δ-isomerase (EC 5.3.3.4). Cluster with LysR regulator **catR** (PP_3716).

### 4d. Boundary/upstream (keep separate from PCA cleavage)

- **benA/B/C/D (PP_3161–3164)** — benzoate 1,2-dioxygenase system → cyclohexadiene-diol-carboxylate → catechol (feeds the catechol branch, not PCA). KEGG map `ppu00622`.

### 4e. Over-propagated / unrelated (exclude from module)

- **gal genes — galB (PP_2515), galC (PP_2514), galD (PP_2513):** gallate degradation via **4-oxalomesaconate** (EC 4.2.1.83 / 4.1.3.17 / 5.3.2.8). galA is a **type-II extradiol** dioxygenase, sharing ancestry with protocatechuate **4,5**-dioxygenase, **not** the 3,4-*ortho* enzyme (Nogales et al., 2005, PMID 16030014). **Distinct pathway.**
- **paa genes — paaJ (PP_3280), paaH (PP_3282), paaF (PP_3284):** phenylacetate-CoA (aerobic hybrid) pathway. Thiolase/hydratase/dehydrogenase EC overlap only.
- **fad/β-oxidation — fadA (PP_2051, PP_2137), fadB (PP_2136), PP_2217, hbd (PP_3755):** fatty-acid oxidation.
- **Generic thiolases EC 2.3.1.9/2.3.1.16 — PP_0582, PP_2215, PP_3355, bktB (PP_3754), yqeF (PP_4636):** broad acetyl-CoA acetyltransferase / β-ketothiolase family; over-propagated via EC-class similarity to pcaF.
- **gcdH (PP_0158)** glutaryl-CoA dehydrogenase; **PP_1218** acyl-CoA thioesterase; **PP_2504** 4-oxalocrotonate tautomerase (*meta*-cleavage); **PP_1791** 4-hydroxy-2-oxovalerate aldolase (*meta*-cleavage); **PP_1950** cytochrome P450; **fdx (PP_0847)** 2Fe-2S ferredoxin — none are PCA *ortho*-cleavage enzymes.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

1. **PP_3648 (candidate_uncertain — resolved to over-propagation).** KEGG maps it to K01607/EC 4.1.1.44, identical to pcaC (PP_1381), but **InterPro discriminates the two decisively**: pcaC (PP_1381, Q88N35) carries the *specific* signature **IPR012788 "4-carboxymuconolactone decarboxylase (PcaC)"**, whereas **PP_3648 (Q88GS0) has only the *generic* domain IPR003779 (carboxymuconolactone-decarboxylase-like / AhpD superfamily) + Pfam PF02627** and lacks IPR012788. Both share PANTHER PTHR33570:SF2 and PF02627, which is exactly why KEGG over-propagated EC 4.1.1.44 onto PP_3648. **Conclusion: PP_1381 is the true PcaC (module = covered); PP_3648 should NOT satisfy the decarboxylation step and should be flagged over-propagated/candidate_uncertain** (likely an AhpD-like redox/stress protein).
2. **pcaD naming ("enol-lactonase 2").** Suggests the annotation pipeline recognized a second enol-lactonase; verify there is no mis-split. Functionally the PP_1380 assignment is sound.
3. **Broad EC/thiolase over-propagation.** EC 2.3.1.9/2.3.1.16 thiolases (PP_0582, PP_2215, PP_3355, bktB, yqeF) and paaJ (also carrying EC 2.3.1.174) can be spuriously linked to pcaF. Only **pcaF (PP_1377, K07823)** is the β-ketoadipate-pathway thiolase; **paaJ (PP_3280)** carries 2.3.1.174 but belongs to the phenylacetate route — a real EC-overlap trap for curators.
4. **catA redundancy vs. over-propagation.** catA-I and catA-II are two authentic catechol 1,2-dioxygenases; keep both but in the **catechol** branch, not the PCA branch.
5. **No true gaps** in the PCA branch: every enzymatic step has a strong, mostly direct assignment.

**Per-step paralog scan (UniProt EC search, organism 160488) — curation confidence:**

| Step (EC) | # KT2440 loci with this EC | Module gene | EC-unique? | Curation note |
|-----------|---------------------------|-------------|-----------|---------------|
| 1.13.11.3 | 2 (α+β of one enzyme) | pcaG/pcaH | yes | single enzyme; unambiguous |
| 5.5.1.2 | 1 | pcaB | **yes** | single copy, high confidence |
| 4.1.1.44 | 1 | pcaC (PP_1381) | **yes** | PP_3648 is NOT given this EC by UniProt → KEGG-only over-propagation |
| 3.1.1.24 | 1 | pcaD | **yes** | single copy; "enol-lactonase 2" label does not imply a 2nd EC 3.1.1.24 gene |
| 2.8.3.6 | 4 | pcaI/pcaJ | no | **atoA/atoB (PP_3122/PP_3123)** = acetoacetate CoA-transferase paralog; exclude |
| 2.3.1.174 | 6 | pcaF | no | shared with paaJ, yqeF, PP_2215, bktB, fadA → identify pcaF by KO **K07823** + context, not EC |
| 1.13.11.1 | 2 | catA-I/catA-II | (branch) | two genuine catechol-branch isozymes |

**Take-home:** four of six enzymatic steps are EC-unique (very high confidence); only the **CoA-transferase (pcaIJ)** and **thiolase (pcaF)** steps sit in multi-member EC families and must be pinned by KEGG orthology/genomic context rather than EC number.

---

## 6. Module and GO-Curation Recommendations

**Module step status:**

| Module element | Recommended status |
|----------------|--------------------|
| protocatechuate 3,4-dioxygenase (pcaGH) | **covered** |
| 3-carboxymuconate cycloisomerase (pcaB) | **covered** |
| γ-carboxymuconolactone decarboxylase (pcaC) | **covered** (PP_1381; PP_3648 = candidate_uncertain paralog) |
| enol-lactone hydrolase (pcaD) | **covered** |
| 3-oxoadipate CoA-transferase (pcaIJ) | **covered** |
| β-ketoadipyl-CoA thiolase (pcaF) | **covered** (exclude paaJ/generic thiolases) |
| PCA supply from 4-HB (pobA) | **covered (boundary/feeder)** |
| Whole `ppu00362` candidate list as the module | **module_needs_revision** (prune to pca + feeders) |

**Boundary corrections:**
- The generic `ppu00362` "Benzoate degradation" overview map is **too broad** to serve as this module. Split into: (a) protocatechuate *ortho*-cleavage (this module), (b) catechol *ortho*-cleavage (M00568), (c) benzoate→catechol (ben), (d) gallate/4-oxalomesaconate, (e) phenylacetate-CoA, (f) β-oxidation. Genes in (c)–(f) should not satisfy this module.

**New documents / GO requests:**
- **Author a dedicated module** "protocatechuate *ortho*-cleavage: protocatechuate ⇒ β-ketoadipate ⇒ acetyl-CoA + succinyl-CoA" with the six EC steps above — KEGG currently lacks it (only the catechol counterpart M00568 exists).
- GO annotations are largely available (GO:0018578 protocatechuate 3,4-dioxygenase activity; GO:0019619 3,4-dihydroxybenzoate catabolic process). Ensure pcaB/C/D/I/J/F carry the **process** term GO:0019619 and appropriate MF terms; request/verify a specific term for "3-oxoadipate CoA-transferase activity" (EC 2.8.3.6) if missing.

---

## 7. Genes to Promote to Full `fetch-gene` Review

Priority order:
1. **PP_3648** — pcaC paralog ambiguity now **largely resolved by InterPro** (generic IPR003779/AhpD-like, lacks pcaC-specific IPR012788). Promote only to *confirm* it is not a functional decarboxylase and to reassign it away from EC 4.1.1.44. *High curation value (fixes an over-propagation).*
2. **pcaD (PP_1380)** — clarify the "enol-lactonase 2" designation / possible isozyme.
3. **paaJ (PP_3280)** — confirm it is excluded from the PCA branch despite carrying EC 2.3.1.174 (EC-overlap trap).
4. **catA-I (PP_3713) vs catA-II (PP_3166)** — document isozyme roles and branch assignment.
5. **pcaR (PP_1375)** — locus now **pinned** (UniProt Q88N41; upstream of pcaK). Optional: confirm the KT2440 regulon membership experimentally (transfer from *P. putida* PRS2000 is strong).

---

## 8. Key References

- Harwood CS, Parales RE. *The β-ketoadipate pathway and the biology of self-identity.* Annu Rev Microbiol. 1996;50:553–590. **PMID 8905091.** (Defines protocatechuate & catechol branches; conservation across *P. putida* and others.)
- Nichols NN, Harwood CS. *Repression of 4-hydroxybenzoate transport and degradation by benzoate…* J Bacteriol. 1995. **PMID 8522507.** (pca structural genes = complete protocatechuate branch; PcaR regulation; benzoate repression of pcaK.)
- Nogales J, et al. *Molecular characterization of the gallate dioxygenase from Pseudomonas putida KT2440…* J Biol Chem. 2005. **PMID 16030014.** (galA/gal pathway is a distinct type-II extradiol/4-oxalomesaconate route — not *ortho*-cleavage.)
- Dias ACF, et al. *From degrader to producer: reversing the gallic acid metabolism of Pseudomonas putida KT2440.* 2023. **PMID 36357545.** (pcaHG deletion blocks PCA degradation in KT2440 — direct functional evidence.)
- Bertani I, et al. *Regulation of the p-hydroxybenzoic acid hydroxylase gene (pobA)…* 2001. **PMID 11390692.** (pobA → protocatechuate → β-ketoadipate pathway.)
- Gerischer U, et al. *PcaU, a transcriptional activator of genes for protocatechuate utilization in Acinetobacter.* 1998. **PMID 9515921.** (pcaIJFBDKCHG operon architecture — related-organism comparator; transfer to *Pseudomonas* is partial: gene set conserved, cluster organization differs.)
- KEGG (rest.kegg.jp), verified 2026-08-11: `link/ppu/path:ppu00362` (candidate list = overview-map membership); gene KO/EC for pcaGHBCDIJF, catABC, benABCD; module list (M00568 catechol *ortho*-cleavage; no protocatechuate module).

---

### Evidence-strength notes
- **Direct (target organism, experimental):** pcaHG function (KT2440 deletion), pcaF/pcaK regulation and PcaR control (*P. putida* PRS2000/KT2440), galA distinctness (KT2440), pobA feeder role (*P. putida*).
- **Strong homology + genomic context (target genome):** pcaB, pcaC, pcaD, pcaI, pcaJ assignments (clustered, correct KO/EC).
- **Related-organism transfer:** *Acinetobacter* operon architecture (comparator only; conserved enzymes, different cluster layout — transfer of gene *identity* strong, of *organization* weak).
- **Uncertain (now resolved):** PP_3648 identity → generic AhpD-like/CMD family (IPR003779), over-propagated to EC 4.1.1.44 by KEGG only; pcaR locus → PP_1375 (UniProt Q88N41). Residual open question: whether PP_3648 has any physiological decarboxylase activity (recommend experimental check).

---

## Appendix A — Disposition of all 40 candidate genes (curation quick-reference)

| Locus | Gene | Disposition for THIS module | Rationale |
|-------|------|-----------------------------|-----------|
| PP_4655 | pcaG | **covered** (core) | protocatechuate 3,4-dioxygenase α (EC 1.13.11.3, K00448) |
| PP_4656 | pcaH | **covered** (core) | protocatechuate 3,4-dioxygenase β (EC 1.13.11.3, K00449) |
| PP_1379 | pcaB | **covered** (core) | EC 5.5.1.2, single-copy |
| PP_1381 | pcaC | **covered** (core) | EC 4.1.1.44, specific IPR012788 |
| PP_1380 | pcaD | **covered** (core) | EC 3.1.1.24, single-copy |
| PP_3951 | pcaI | **covered** (core) | 3-oxoadipate CoA-transferase α (EC 2.8.3.6, K01031) |
| PP_3952 | pcaJ | **covered** (core) | 3-oxoadipate CoA-transferase β (EC 2.8.3.6, K01032) |
| PP_1377 | pcaF-I | **covered** (core) | β-ketoadipyl-CoA thiolase (EC 2.3.1.174, K07823) |
| PP_3537 | pobA | **covered** (feeder/boundary) | 4-HB 3-monooxygenase supplies PCA |
| PP_1376 | pcaK | **covered** (transport) | 4-HB/PCA MFS transporter |
| PP_1378 | pcaT | **covered** (transport) | dicarboxylate permease |
| PP_1375 | pcaR | **covered** (regulatory) | IclR-family activator of pca regulon |
| PP_3713 | catA-I | separate branch (catechol) | catechol 1,2-dioxygenase isozyme |
| PP_3166 | catA-II | separate branch (catechol) | catechol 1,2-dioxygenase isozyme (ben cluster) |
| PP_3715 | catB | separate branch (catechol) | muconate cycloisomerase (EC 5.5.1.1) |
| PP_3714 | catC | separate branch (catechol) | muconolactone Δ-isomerase (EC 5.3.3.4) |
| PP_3161–3164 | benABCD | upstream/boundary | benzoate 1,2-dioxygenase → catechol |
| PP_3648 | — | **candidate_uncertain / over-propagated** | generic AhpD/CMD (IPR003779); not true PcaC |
| PP_3280 | paaJ | exclude (phenylacetate) | EC 2.3.1.174 overlap only |
| PP_3282 | paaH | exclude (phenylacetate) | 3-hydroxyadipyl-CoA DH |
| PP_3284 | paaF | exclude (phenylacetate) | enoyl-CoA hydratase-isomerase |
| PP_2513 | galD | exclude (gallate/4-OMA) | distinct non-ortho route |
| PP_2514 | galC | exclude (gallate/4-OMA) | CHA aldolase |
| PP_2515 | galB | exclude (gallate/4-OMA) | OMA hydratase |
| PP_2051 | fadA | exclude (β-oxidation) | 3-ketoacyl-CoA thiolase |
| PP_2136 | fadB | exclude (β-oxidation) | FA oxidation complex α |
| PP_2137 | fadA | exclude (β-oxidation) | 3-ketoacyl-CoA thiolase |
| PP_2217 | — | exclude (β-oxidation) | enoyl-CoA hydratase |
| PP_3755 | hbd | exclude (β-oxidation) | 3-hydroxybutyryl-CoA DH |
| PP_0582 | — | exclude (generic thiolase) | EC over-propagation |
| PP_2215 | — | exclude (generic thiolase) | acetyl-CoA acetyltransferase |
| PP_3355 | — | exclude (generic thiolase) | β-ketothiolase |
| PP_3754 | bktB | exclude (generic thiolase) | β-ketothiolase |
| PP_4636 | yqeF | exclude (generic thiolase) | acetyl-CoA acetyltransferase |
| PP_0158 | gcdH | exclude (unrelated) | glutaryl-CoA DH |
| PP_1218 | — | exclude (unrelated) | acyl-CoA thioesterase |
| PP_2504 | — | exclude (meta-cleavage) | 4-oxalocrotonate tautomerase |
| PP_1791 | — | exclude (meta-cleavage) | 4-OH-2-oxovalerate aldolase |
| PP_1950 | — | exclude (unrelated) | cytochrome P450 |
| PP_0847 | fdx | exclude (unrelated) | 2Fe-2S ferredoxin |

**Summary counts:** 8 core enzymatic + 1 feeder + 3 transport/regulatory = **12 module members**; 4 catechol-branch (model separately); 4 ben upstream; **1 candidate_uncertain (PP_3648)**; **19 exclude (over-propagated/unrelated)**.


## Artifacts

- [OpenScientist final report](PSEPK__protocatechuate-ortho-cleavage-pathway__ppu00362-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__protocatechuate-ortho-cleavage-pathway__ppu00362-deep-research-openscientist_artifacts/final_report.pdf)