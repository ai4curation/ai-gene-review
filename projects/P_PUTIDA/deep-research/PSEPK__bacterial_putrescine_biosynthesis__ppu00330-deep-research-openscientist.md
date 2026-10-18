---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T01:59:47.257621'
end_time: '2026-08-13T02:16:33.707274'
duration_seconds: 1006.45
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial putrescine biosynthesis by arginine and ornithine routes
  module_summary: A reusable bacterial module for putrescine supply through two alternative
    amino-acid routes. In the two-step arginine route, SpeA decarboxylates L-arginine
    to agmatine and SpeB hydrolyzes agmatine to putrescine. In the alternative direct
    route, SpeC decarboxylates L-ornithine to putrescine. Downstream spermidine synthesis,
    putrescine uptake, and putrescine catabolism are outside the module boundary.
  module_outline: "- Bacterial putrescine biosynthesis by arginine and ornithine routes\n\
    \  - 1. arginine-route agmatine formation\n  - SpeA arginine decarboxylation\n\
    \    - Biosynthetic arginine decarboxylase activity (molecular player: bacterial\
    \ biosynthetic arginine decarboxylase family; activity or role: arginine decarboxylase\
    \ activity)\n  - 2. arginine-route putrescine formation\n  - SpeB agmatine hydrolysis\n\
    \    - Agmatinase activity (molecular player: bacterial agmatinase subfamily;\
    \ activity or role: agmatinase activity)\n  - 3. alternative direct ornithine\
    \ route\n  - SpeC ornithine decarboxylation\n    - Ornithine decarboxylase activity\
    \ (molecular player: ornithine decarboxylase 1-related subfamily; activity or\
    \ role: ornithine decarboxylase activity)"
  module_connections: '- SpeA arginine decarboxylation feeds into SpeB agmatine hydrolysis:
    SpeA supplies agmatine, the substrate hydrolyzed by SpeB.'
  pathway_query: ppu00330
  pathway_id: ppu00330
  pathway_name: Arginine and proline metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00330 with 30 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '39'
  candidate_genes: '- aguA: PP_0266 | Q88R68 | Agmatine deiminase (EC 3.5.3.12) (Agmatine
    iminohydrolase) (EC 3.5.3.12; primary bucket kegg:ppu00330)

    - speA: PP_0567 | Q88QC7 | Biosynthetic arginine decarboxylase (ADC) (EC 4.1.1.19)
    (EC 4.1.1.19; primary bucket kegg:ppu00330)

    - proB: PP_0691 | Q88Q07 | Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl kinase)
    (GK) (EC 2.7.2.11; primary bucket kegg:ppu00332)

    - speC: PP_0864 | Q88PI6 | ornithine decarboxylase (EC 4.1.1.17) (EC 4.1.1.17;
    primary bucket kegg:ppu04148)

    - patD: PP_1481 | Q88MT7 | Medium chain aldehyde dehydrogenase (EC 1.2.1.19, EC
    1.2.1.54) (EC 1.2.1.19; 1.2.1.54; primary bucket kegg:ppu00410)

    - speB: PP_2196 | Q88KU3 | Agmatinase (EC 3.5.3.11) (EC 3.5.3.11; primary bucket
    kegg:ppu00330)

    - puuB: PP_2448 | Q88K44 | Gamma-glutamylputrescine oxidase (primary bucket kegg:ppu00330)

    - PP_2588: PP_2588 | Q88JR1 | Aminotransferase, class III (primary bucket kegg:ppu00330)

    - PP_2589: PP_2589 | Q88JR0 | Aldehyde dehydrogenase family protein (primary bucket
    kegg:ppu00330)

    - prr: PP_2801 | Q88J48 | Gamma-aminobutyraldehyde dehydrogenase (EC 1.2.1.19)
    (EC 1.2.1.19; primary bucket kegg:ppu00410)

    - nspC: PP_2929 | Q88IS0 | Carboxynorspermidine/carboxyspermidine decarboxylase
    (CANS DC/CAS DC) (CANSDC/CASDC) (EC 4.1.1.96) (EC 4.1.1.96; primary bucket kegg:ppu00330)

    - PP_2932: PP_2932 | Q88IR7 | Amidase family protein (primary bucket kegg:ppu00643)

    - PP_3146: PP_3146 | Q88I55 | Oxidoreductase (primary bucket kegg:ppu00330)

    - codA: PP_3189 | Q88I13 | Cytosine deaminase / isoguanine deaminase (EC 3.5.4.-,
    EC 3.5.4.1) (EC 3.5.4.-; 3.5.4.1; primary bucket kegg:ppu00240)

    - oplB: PP_3514 | Q88H51 | 5-oxoprolinase B (EC 3.5.2.9) (EC 3.5.2.9; primary
    bucket kegg:ppu00330)

    - oplA: PP_3515 | Q88H50 | 5-oxoprolinase A (EC 3.5.2.9) (EC 3.5.2.9; primary
    bucket kegg:ppu00330)

    - ocd__Q88H32: PP_3533 | Q88H32 | Ornithine cyclodeaminase (OCD) (EC 4.3.1.12)
    (EC 4.3.1.12; primary bucket kegg:ppu00330)

    - creA: PP_3667 | Q88GQ1 | Creatinase (EC 3.5.3.3) (EC 3.5.3.3; primary bucket
    kegg:ppu00330)

    - aruH: PP_3721 | Q88GK0 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00330)

    - aruI: PP_3723 | A0A140FWH9 | 2-ketoarginine decarboxylase AruI (EC 4.1.1.75)
    (EC 4.1.1.75; primary bucket kegg:ppu00330)

    - ldcC: PP_4140 | A0A140FWL0 | Lysine decarboxylase (EC 4.1.1.18) (EC 4.1.1.18;
    primary bucket kegg:ppu00330)

    - ooxA: PP_4456 | Q88EK6 | Opine oxidase subunit A (EC 1.-.-.-) (EC 1.-.-.-; primary
    bucket kegg:ppu00330)

    - ooxB: PP_4457 | Q88EK5 | Opine oxidase subunit B (EC 1.-.-.-) (EC 1.-.-.-; primary
    bucket kegg:ppu00330)

    - astE: PP_4475 | Q88EI7 | Succinylglutamate desuccinylase (EC 3.5.1.96) (EC 3.5.1.96;
    primary bucket kegg:ppu00330)

    - astB: PP_4477 | Q88EI5 | N-succinylarginine dihydrolase (EC 3.5.3.23) (EC 3.5.3.23;
    primary bucket kegg:ppu00330)

    - astD: PP_4478 | Q88EI4 | N-succinylglutamate 5-semialdehyde dehydrogenase (EC
    1.2.1.71) (Succinylglutamic semialdehyde dehydrogenase) (SGSD) (EC 1.2.1.71; primary
    bucket kegg:ppu00330)

    - astA-I: PP_4479 | Q88EI3 | Arginine N-succinyltransferase (EC 2.3.1.109) (EC
    2.3.1.109; primary bucket kegg:ppu00330)

    - astA-II: PP_4480 | Q88EI2 | Arginine N-succinyltransferase, subunit alpha (EC
    2.3.1.109) (EC 2.3.1.109; primary bucket kegg:ppu00330)

    - argD: PP_4481 | P59319 | Acetylornithine aminotransferase (ACOAT) (EC 2.6.1.11)
    (EC 2.6.1.11; primary bucket kegg:ppu00330)

    - PP_4523: PP_4523 | Q88EE2 | Agmatinase (primary bucket kegg:ppu00330)

    - PP_4548: PP_4548 | Q88EB8 | Oxidoreductase (primary bucket kegg:ppu00330)

    - proA: PP_4811 | Q88DL4 | Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41)
    (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialdehyde dehydrogenase)
    (GSA dehydrogenase) (EC 1.2.1.41; primary bucket kegg:ppu00332)

    - putA: PP_4947 | Q88D80 | Bifunctional protein PutA [Includes: Proline dehydrogenase
    (EC 1.5.5.2) (Proline oxidase); Delta-1-pyrroline-5-carboxylate dehydrogenase
    (P5C dehydrogenase) (EC 1.2.1.88) (L-glutamate gamma-semialdehyde dehydrogenase)]
    (EC 1.2.1.88; 1.5.5.2; primary bucket kegg:ppu00250)

    - PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3;
    primary bucket kegg:ppu00350)

    - pip: PP_5028 | Q88D01 | Proline iminopeptidase (PIP) (EC 3.4.11.5) (Prolyl aminopeptidase)
    (EC 3.4.11.5; primary bucket kegg:ppu00330)

    - proI: PP_5095 | Q88CT5 | Pyrroline-5-carboxylate reductase (P5C reductase) (P5CR)
    (EC 1.5.1.2) (PCA reductase) (EC 1.5.1.2; primary bucket kegg:ppu00330)

    - spuC-II: PP_5182 | Q88CJ8 | Polyamine:pyruvate transaminase (primary bucket
    kegg:ppu00330)

    - PP_5273: PP_5273 | Q88CA8 | Oxidoreductase (primary bucket kegg:ppu00330)

    - kauB: PP_5278 | Q88CA3 | 4-guanidinobutyraldehyde dehydrogenase (EC 1.2.1.54)
    (EC 1.2.1.54; primary bucket kegg:ppu00330)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_putrescine_biosynthesis__ppu00330-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_putrescine_biosynthesis__ppu00330-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial putrescine biosynthesis by arginine and ornithine routes in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00330
- Resolved ID: ppu00330
- Resolved name: Arginine and proline metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00330 with 30 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 39

- aguA: PP_0266 | Q88R68 | Agmatine deiminase (EC 3.5.3.12) (Agmatine iminohydrolase) (EC 3.5.3.12; primary bucket kegg:ppu00330)
- speA: PP_0567 | Q88QC7 | Biosynthetic arginine decarboxylase (ADC) (EC 4.1.1.19) (EC 4.1.1.19; primary bucket kegg:ppu00330)
- proB: PP_0691 | Q88Q07 | Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl kinase) (GK) (EC 2.7.2.11; primary bucket kegg:ppu00332)
- speC: PP_0864 | Q88PI6 | ornithine decarboxylase (EC 4.1.1.17) (EC 4.1.1.17; primary bucket kegg:ppu04148)
- patD: PP_1481 | Q88MT7 | Medium chain aldehyde dehydrogenase (EC 1.2.1.19, EC 1.2.1.54) (EC 1.2.1.19; 1.2.1.54; primary bucket kegg:ppu00410)
- speB: PP_2196 | Q88KU3 | Agmatinase (EC 3.5.3.11) (EC 3.5.3.11; primary bucket kegg:ppu00330)
- puuB: PP_2448 | Q88K44 | Gamma-glutamylputrescine oxidase (primary bucket kegg:ppu00330)
- PP_2588: PP_2588 | Q88JR1 | Aminotransferase, class III (primary bucket kegg:ppu00330)
- PP_2589: PP_2589 | Q88JR0 | Aldehyde dehydrogenase family protein (primary bucket kegg:ppu00330)
- prr: PP_2801 | Q88J48 | Gamma-aminobutyraldehyde dehydrogenase (EC 1.2.1.19) (EC 1.2.1.19; primary bucket kegg:ppu00410)
- nspC: PP_2929 | Q88IS0 | Carboxynorspermidine/carboxyspermidine decarboxylase (CANS DC/CAS DC) (CANSDC/CASDC) (EC 4.1.1.96) (EC 4.1.1.96; primary bucket kegg:ppu00330)
- PP_2932: PP_2932 | Q88IR7 | Amidase family protein (primary bucket kegg:ppu00643)
- PP_3146: PP_3146 | Q88I55 | Oxidoreductase (primary bucket kegg:ppu00330)
- codA: PP_3189 | Q88I13 | Cytosine deaminase / isoguanine deaminase (EC 3.5.4.-, EC 3.5.4.1) (EC 3.5.4.-; 3.5.4.1; primary bucket kegg:ppu00240)
- oplB: PP_3514 | Q88H51 | 5-oxoprolinase B (EC 3.5.2.9) (EC 3.5.2.9; primary bucket kegg:ppu00330)
- oplA: PP_3515 | Q88H50 | 5-oxoprolinase A (EC 3.5.2.9) (EC 3.5.2.9; primary bucket kegg:ppu00330)
- ocd__Q88H32: PP_3533 | Q88H32 | Ornithine cyclodeaminase (OCD) (EC 4.3.1.12) (EC 4.3.1.12; primary bucket kegg:ppu00330)
- creA: PP_3667 | Q88GQ1 | Creatinase (EC 3.5.3.3) (EC 3.5.3.3; primary bucket kegg:ppu00330)
- aruH: PP_3721 | Q88GK0 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00330)
- aruI: PP_3723 | A0A140FWH9 | 2-ketoarginine decarboxylase AruI (EC 4.1.1.75) (EC 4.1.1.75; primary bucket kegg:ppu00330)
- ldcC: PP_4140 | A0A140FWL0 | Lysine decarboxylase (EC 4.1.1.18) (EC 4.1.1.18; primary bucket kegg:ppu00330)
- ooxA: PP_4456 | Q88EK6 | Opine oxidase subunit A (EC 1.-.-.-) (EC 1.-.-.-; primary bucket kegg:ppu00330)
- ooxB: PP_4457 | Q88EK5 | Opine oxidase subunit B (EC 1.-.-.-) (EC 1.-.-.-; primary bucket kegg:ppu00330)
- astE: PP_4475 | Q88EI7 | Succinylglutamate desuccinylase (EC 3.5.1.96) (EC 3.5.1.96; primary bucket kegg:ppu00330)
- astB: PP_4477 | Q88EI5 | N-succinylarginine dihydrolase (EC 3.5.3.23) (EC 3.5.3.23; primary bucket kegg:ppu00330)
- astD: PP_4478 | Q88EI4 | N-succinylglutamate 5-semialdehyde dehydrogenase (EC 1.2.1.71) (Succinylglutamic semialdehyde dehydrogenase) (SGSD) (EC 1.2.1.71; primary bucket kegg:ppu00330)
- astA-I: PP_4479 | Q88EI3 | Arginine N-succinyltransferase (EC 2.3.1.109) (EC 2.3.1.109; primary bucket kegg:ppu00330)
- astA-II: PP_4480 | Q88EI2 | Arginine N-succinyltransferase, subunit alpha (EC 2.3.1.109) (EC 2.3.1.109; primary bucket kegg:ppu00330)
- argD: PP_4481 | P59319 | Acetylornithine aminotransferase (ACOAT) (EC 2.6.1.11) (EC 2.6.1.11; primary bucket kegg:ppu00330)
- PP_4523: PP_4523 | Q88EE2 | Agmatinase (primary bucket kegg:ppu00330)
- PP_4548: PP_4548 | Q88EB8 | Oxidoreductase (primary bucket kegg:ppu00330)
- proA: PP_4811 | Q88DL4 | Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41) (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialdehyde dehydrogenase) (GSA dehydrogenase) (EC 1.2.1.41; primary bucket kegg:ppu00332)
- putA: PP_4947 | Q88D80 | Bifunctional protein PutA [Includes: Proline dehydrogenase (EC 1.5.5.2) (Proline oxidase); Delta-1-pyrroline-5-carboxylate dehydrogenase (P5C dehydrogenase) (EC 1.2.1.88) (L-glutamate gamma-semialdehyde dehydrogenase)] (EC 1.2.1.88; 1.5.5.2; primary bucket kegg:ppu00250)
- PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3; primary bucket kegg:ppu00350)
- pip: PP_5028 | Q88D01 | Proline iminopeptidase (PIP) (EC 3.4.11.5) (Prolyl aminopeptidase) (EC 3.4.11.5; primary bucket kegg:ppu00330)
- proI: PP_5095 | Q88CT5 | Pyrroline-5-carboxylate reductase (P5C reductase) (P5CR) (EC 1.5.1.2) (PCA reductase) (EC 1.5.1.2; primary bucket kegg:ppu00330)
- spuC-II: PP_5182 | Q88CJ8 | Polyamine:pyruvate transaminase (primary bucket kegg:ppu00330)
- PP_5273: PP_5273 | Q88CA8 | Oxidoreductase (primary bucket kegg:ppu00330)
- kauB: PP_5278 | Q88CA3 | 4-guanidinobutyraldehyde dehydrogenase (EC 1.2.1.54) (EC 1.2.1.54; primary bucket kegg:ppu00330)

## Generic Module Context

### Working Scope

A reusable bacterial module for putrescine supply through two alternative amino-acid routes. In the two-step arginine route, SpeA decarboxylates L-arginine to agmatine and SpeB hydrolyzes agmatine to putrescine. In the alternative direct route, SpeC decarboxylates L-ornithine to putrescine. Downstream spermidine synthesis, putrescine uptake, and putrescine catabolism are outside the module boundary.

### Provisional Biological Outline

- Bacterial putrescine biosynthesis by arginine and ornithine routes
  - 1. arginine-route agmatine formation
  - SpeA arginine decarboxylation
    - Biosynthetic arginine decarboxylase activity (molecular player: bacterial biosynthetic arginine decarboxylase family; activity or role: arginine decarboxylase activity)
  - 2. arginine-route putrescine formation
  - SpeB agmatine hydrolysis
    - Agmatinase activity (molecular player: bacterial agmatinase subfamily; activity or role: agmatinase activity)
  - 3. alternative direct ornithine route
  - SpeC ornithine decarboxylation
    - Ornithine decarboxylase activity (molecular player: ornithine decarboxylase 1-related subfamily; activity or role: ornithine decarboxylase activity)

### Known Relationships Among Steps

- SpeA arginine decarboxylation feeds into SpeB agmatine hydrolysis: SpeA supplies agmatine, the substrate hydrolyzed by SpeB.

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

# Commissioned Review: Bacterial Putrescine Biosynthesis by Arginine and Ornithine Routes in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK, NCBI taxon 160488, proteome UP000000556)
**Target bucket:** KEGG `ppu00330` — "Arginine and proline metabolism" (30 primary genes; 39 candidates)
**Module under review:** Putrescine supply through two alternative amino-acid routes — arginine route (SpeA → agmatine → SpeB → putrescine) and direct ornithine route (SpeC → putrescine). Spermidine synthesis, putrescine uptake, and putrescine catabolism are out of scope.
**Date:** 2026-08-13 · Supersedes an Iteration-1 error (aguB = PP_1639), corrected below.

---

## 1. Executive Summary

The putrescine-biosynthesis module is **satisfiable** in *Pseudomonas putida* KT2440. The genome encodes high-confidence orthologs for every core step of both canonical routes. In the **arginine route**, biosynthetic arginine decarboxylase SpeA (PP_0567, K01585, EC 4.1.1.19) converts L-arginine to agmatine, and agmatinase SpeB (PP_2196, K01480, EC 3.5.3.11) hydrolyzes agmatine directly to putrescine + urea. In the **direct ornithine route**, ornithine decarboxylase SpeC (PP_0864, K01581, EC 4.1.1.17) decarboxylates L-ornithine to putrescine in a single step. Module steps 1 (SpeA agmatine formation), 2 (SpeB agmatine hydrolysis), and 3 (SpeC ornithine decarboxylation) should all be marked **covered**.

The one genuinely uncertain element is the **alternative two-step agmatine-deiminase branch** of the arginine route. KT2440 encodes agmatine deiminase AguA (PP_0266, K10536, EC 3.5.3.12), which converts agmatine to N-carbamoylputrescine, but the genome appears to lack an annotated downstream N-carbamoylputrescine amidohydrolase (**aguB / NCPAH, K12251, EC 3.5.1.53**) and has **no aguBA operon** analogous to the well-characterized *P. aeruginosa* system. This branch should be marked **candidate_uncertain (with an aguB gap)**: AguA alone cannot complete the two-step route, and because the direct agmatinase SpeB already delivers putrescine from agmatine, the module remains satisfiable regardless of the deiminase branch status.

Two curation actions are important. First, **PP_4523**, labeled "Agmatinase" in local UniProt-derived metadata, is a **likely over-propagated annotation**: KEGG resolves it as guanidinobutyrase (K12255, EC 3.5.3.7), an arginine-catabolism ureohydrolase, not the biosynthetic agmatinase. It is a same-family paralog of the genuine agmatinase PP_2196 and should be demoted out of the module. Second, the KEGG `ppu00330` bucket is far broader than the putrescine module — roughly 33 of the 39 candidate genes belong to neighboring processes and must not be counted toward satisfiability. Critically, **no KT2440-strain-specific functional evidence** exists for any module gene; all calls rest on strong same-genus orthology transfer, primarily from *P. aeruginosa* PAO1 and *P. chlororaphis* O6.

---

## 2. Target-Organism Pathway Definition

### 2.1 Exact process included

The module covers **de novo putrescine (1,4-diaminobutane) supply from amino-acid precursors** in *P. putida* KT2440 via two alternative routes:

1. **Arg → agmatine + CO₂** — biosynthetic arginine decarboxylase (ADC / SpeA, EC 4.1.1.19).
2. **Agmatine → putrescine** — either:
   - **(2a) direct:** agmatinase (SpeB, EC 3.5.3.11): agmatine + H₂O → putrescine + urea; **or**
   - **(2b) two-step deiminase branch:** agmatine deiminase (AguA, EC 3.5.3.12) → *N*-carbamoylputrescine → N-carbamoylputrescine amidohydrolase (AguB, EC 3.5.1.53) → putrescine + CO₂ + NH₃.
3. **Ornithine → putrescine + CO₂** — ornithine decarboxylase (ODC / SpeC, EC 4.1.1.17).

### 2.2 Neighboring pathways to keep separate

The resolved KEGG bucket `ppu00330` ("Arginine and proline metabolism") is an aggregate map, not a module. The following co-bucketed processes are **outside** the module boundary and must not be counted toward putrescine satisfiability:

| Adjacent process | Representative KT2440 candidate genes | Relationship to module |
|---|---|---|
| Arginine succinyltransferase (AST) catabolism | astA-I/PP_4479, astA-II/PP_4480, astB/PP_4477, astD/PP_4478, astE/PP_4475 | Arginine → glutamate; not putrescine |
| Arginine oxidase / 2-ketoarginine route | aruH/PP_3721, aruI/PP_3723, kauB/PP_5278 | Arginine catabolism → GABA; not putrescine |
| Proline biosynthesis / catabolism | proB/PP_0691, proA/PP_4811, proI/PP_5095, putA/PP_4947, pip/PP_5028 | Proline metabolism (ppu00332/ppu00250) |
| 5-Oxoprolinase | oplA/PP_3515, oplB/PP_3514 | Glutathione cycle |
| Ornithine cyclodeaminase; acetylornithine AT | ocd/PP_3533, argD/PP_4481 | Ornithine→proline / ornithine *biosynthesis* |
| Creatine/creatinine, opine oxidase | creA/PP_3667, ooxA/PP_4456, ooxB/PP_4457 | Guanidino/opine catabolism |
| Downstream polyamine/GABA aldehyde DHs | patD/PP_1481, prr/PP_2801, spuC-II/PP_5182, puuB/PP_2448, PP_2588, PP_2589 | Putrescine/GABA *catabolism* — downstream of module |
| Other decarboxylases | ldcC/PP_4140 (Lys→cadaverine), nspC/PP_2929 (spermidine branch) | Different diamine/polyamine products |
| Guanidinobutyrase (mis-labeled "agmatinase") | PP_4523 | Arginine catabolism ureohydrolase (see §5) |

### 2.3 Alternate names and database definitions

- **SpeA** = biosynthetic arginine decarboxylase (ADC); EC 4.1.1.19; KEGG K01585. Distinguish from acid-inducible AdiA.
- **SpeB** = agmatinase (agmatine ureohydrolase); EC 3.5.3.11; KEGG K01480.
- **SpeC** = ornithine decarboxylase (ODC); EC 4.1.1.17; KEGG K01581.
- **AguA** = agmatine deiminase / iminohydrolase (AIH); EC 3.5.3.12; KEGG K10536.
- **AguB** = N-carbamoylputrescine amidohydrolase (NCPAH / CPA); EC 3.5.1.53; KEGG K12251. Note the frequent historical confusion with `ptcA` (putrescine transcarbamylase), a non-homologous, non-analogous enzyme found in Gram-positive bacteria.
- MetaCyc separates "putrescine biosynthesis I (ODC)," "II (agmatine → agmatinase)," "III (agmatine → AguA+AguB)," and "IV (arginine → ADC)." KEGG map = "Arginine and proline metabolism" (`ppu00330`).

---

## 3. Expected Step Model

```
                         L-Arginine
                             |
                    SpeA (ADC, EC 4.1.1.19)      [STEP 1: covered — PP_0567]
                             v
                          Agmatine
                        /          \
     SpeB (agmatinase)/            \ AguA (agmatine deiminase, EC 3.5.3.12)
     EC 3.5.3.11     /              \  [PP_0266 present]
   [STEP 2: covered]/                \
     PP_2196       v                  v
              Putrescine        N-carbamoylputrescine
                   ^                  |
                   |                  | AguB / NCPAH (EC 3.5.1.53)
                   |                  |  *** NO ANNOTATED GENE in KT2440 ***
                   |                  v   [deiminase branch: candidate_uncertain / gap]
                   |              Putrescine
                   |
     SpeC (ODC, EC 4.1.1.17)                        [STEP 3: covered — PP_0864]
                   ^
              L-Ornithine
```

| Module step | Enzyme (EC) | KEGG KO | KT2440 gene | Call |
|---|---|---|---|---|
| 1. Arg → agmatine | ADC / SpeA (4.1.1.19) | K01585 | **PP_0567** | **covered** |
| 2a. Agmatine → putrescine (direct) | Agmatinase / SpeB (3.5.3.11) | K01480 | **PP_2196** | **covered** |
| 2b-i. Agmatine → N-carbamoylputrescine | Agmatine deiminase / AguA (3.5.3.12) | K10536 | **PP_0266** | present |
| 2b-ii. N-carbamoylputrescine → putrescine | NCPAH / AguB (3.5.1.53) | K12251 | **none annotated** (PP_3019?) | **candidate_uncertain / gap** |
| 3. Ornithine → putrescine (direct) | ODC / SpeC (4.1.1.17) | K01581 | **PP_0864** | **covered** |

**Net:** Steps 1, 2 (via agmatinase), and 3 are **covered**. The optional deiminase branch (2b) is **incomplete** — treat as `candidate_uncertain`, not a module-blocking gap, because step 2 is already satisfied by agmatinase.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence core module genes

**SpeA — PP_0567 (Q88QC7), biosynthetic arginine decarboxylase, EC 4.1.1.19.**
KEGG orthology places PP_0567 in K01585, the biosynthetic ADC ortholog group; this is the committed first step of the arginine route, producing agmatine. UniProt annotates "Catalyzes the biosynthesis of agmatine from arginine" (evidence inferred from homology, PE3). Evidence type: **orthology, strong same-genus transfer**. The route it initiates is experimentally validated in *P. aeruginosa* PAO1, where putrescine is synthesized "indirectly from arginine via arginine decarboxylase (ADC; the speA product)" [PMID: 12634339], and in *P. chlororaphis* O6, *speA* contributes to the polyamine pool under GacS control [PMID: 28862813]. No KT2440-specific enzymatic assay exists. **Call: covered.**

**SpeB — PP_2196 (Q88KU3), agmatinase, EC 3.5.3.11.**
KEGG assigns PP_2196 to K01480 (agmatinase, biosynthetic, agmatine → putrescine + urea) and it is the sole K01480 ortholog in ppu. This is the direct, single-enzyme completion of the arginine route and the reason the module is satisfiable independent of the deiminase branch. UniProt family: arginase family, agmatinase subfamily (IPR005925/IPR006035/IPR020855). Evidence type: **orthology, strong**. Curation caveat: PP_2196 shares identical InterPro signatures with the paralog PP_4523; KEGG correctly discriminates them (§5). **Call: covered.**

**SpeC — PP_0864 (Q88PI6), ornithine decarboxylase, EC 4.1.1.17.**
KEGG assigns PP_0864 to K01581 (ODC), the sole K01581 ortholog; UniProt reaction "L-ornithine → putrescine + CO₂." This single enzyme constitutes the entire direct ornithine route. Local metadata lists a spurious primary bucket (`kegg:ppu04148`); the EC/KO are unambiguous and the bucket tag should be treated as an artifact. The route is experimentally established in *P. aeruginosa* PAO1: putrescine is synthesized "directly from ornithine by ornithine decarboxylase (ODC; the speC product)" and a *speA speC* double mutant is a putrescine auxotroph [PMID: 12634339]. Evidence type: **orthology, strong**. **Call: covered.**

**AguA — PP_0266 (Q88R68), agmatine deiminase / iminohydrolase, EC 3.5.3.12.**
KEGG assigns PP_0266 to K10536; UniProt describes "hydrolysis of agmatine into N-carbamoylputrescine in the ADC pathway of putrescine biosynthesis." AguA is the first step of the alternative deiminase branch. In *P. aeruginosa*, the aguA product with the aguB product "biosynthetically convert agmatine to putrescine in the ADC pathway" [PMID: 12634339]. Evidence type: **orthology, strong for AguA function; weak for branch completeness in KT2440**. Presence of AguA does **not** imply the branch is complete — the downstream amidohydrolase is required and appears unannotated (§5). **Call: present, branch candidate_uncertain.**

### 4.2 Paralog / over-annotation cases

- **PP_4523 (Q88EE2)** — labeled "Agmatinase" (arginase family, agmatinase subfamily; same InterPro as PP_2196) but KEGG = **K12255 guanidinobutyrase (EC 3.5.3.7)**, an arginine-catabolism ureohydrolase acting on 4-guanidinobutyrate (→ GABA + urea). **Out of module.**
- **PP_3019 (Q88II0)** — "Carbon-nitrogen hydrolase family protein" (nitrilase superfamily; IPR003010, IPR050345); no KO. **Unverified candidate** for the missing NCPAH (AguB is a nitrilase-family enzyme; [PMID: 12634339]).

### 4.3 Summary table

| Gene | Locus | UniProt | KO | Role in module | Evidence | Call |
|---|---|---|---|---|---|---|
| speA | PP_0567 | Q88QC7 | K01585 | Arg→agmatine (step 1) | Orthology (strong) | covered |
| speB | PP_2196 | Q88KU3 | K01480 | Agmatine→putrescine (step 2, direct) | Orthology (strong) | covered |
| speC | PP_0864 | Q88PI6 | K01581 | Orn→putrescine (step 3) | Orthology (strong) | covered |
| aguA | PP_0266 | Q88R68 | K10536 | Agmatine→N-carbamoylputrescine (branch) | Orthology (strong) | present / branch uncertain |
| aguB (NCPAH) | — | — | K12251 | N-carbamoylputrescine→putrescine | absent from annotation | gap |
| PP_4523 | PP_4523 | Q88EE2 | K12255 | mis-labeled "agmatinase" | KEGG = guanidinobutyrase | over-annotation → demote |
| PP_3019 | PP_3019 | Q88II0 | none | candidate NCPAH (nitrilase) | homology only, unverified | promote to review |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 The deiminase branch is incomplete (a genuine gap)

In *P. aeruginosa*, the deiminase branch is a two-gene *aguBA* operon: AguA (agmatine deiminase) and AguB (N-carbamoylputrescine amidohydrolase), the latter "purified as a homohexamer of 33 kDa subunits" and structurally distinct from AguA [PMID: 12634339]. In KT2440:

- The genuine NCPAH ortholog group is **K12251 (EC 3.5.1.53)**. KEGG `link/ppu/K12251` and `link/ppu/ec:3.5.1.53` return **no ppu gene**.
- The *aguA* locus PP_0266 has **no adjacent amidohydrolase** — its neighbors are unrelated (DctB kinase PP_0264, dTDP-rhamnose epimerase PP_0265, outer-membrane proteins PP_0267/0268). There is **no aguBA operon** as in *P. aeruginosa*.
- **Correction to Iteration 1:** an early assignment of *aguB* to PP_1639 was an **error** — PP_1639 (Q88MD4) is "Protein SprT" (KEGG K02742 = SprT), not NCPAH.
- PP_3019 (Q88II0), a carbon-nitrogen hydrolase / nitrilase-superfamily protein, is a **structurally plausible but experimentally unverified** candidate for the missing amidohydrolase.

Because agmatinase SpeB (PP_2196) already converts agmatine directly to putrescine, the module remains satisfiable. The deiminase branch is therefore recorded as **candidate_uncertain (with an aguB gap)**, not a module-breaking failure. Recent work shows this space is evolutionarily labile: non-homologous, convergently evolved NCPAHs ("AguY") in *Shewanella oneidensis* and *Microterricola gilva* are "as efficient as the canonical NCPAH from *Pseudomonas aeruginosa*" [PMID: 40673658], so a cryptic KT2440 amidohydrolase cannot be excluded without direct assay.

### 5.2 PP_4523 is a likely over-propagated "agmatinase"

UniProt annotates **both** PP_2196 (Q88KU3) and PP_4523 (Q88EE2) with the submission name "Agmatinase," the rule "Belongs to the arginase family. Agmatinase subfamily," and identical InterPro signatures (IPR005925, IPR006035, IPR020855). This is a classic paralog-driven over-propagation: family-level annotation cannot discriminate substrate specificity. KEGG splits them — **PP_2196 = K01480 agmatinase (EC 3.5.3.11)**, the true biosynthetic enzyme, versus **PP_4523 = K12255 guanidinobutyrase (EC 3.5.3.7)**. The distinction is further underscored by the literature record that *aguB*/*ptcA* and related ureohydrolase-family genes have "frequently been erroneously annotated in the past" [PMID: 21404211]. **Curation action: demote PP_4523 out of the putrescine module and re-label as guanidinobutyrase.**

### 5.3 Bucket-level over-inclusion

The `ppu00330` bucket contributed 39 candidates, but only ~5–6 are module-relevant. The remaining ~33 belong to arginine AST/aru catabolism, proline metabolism, 5-oxoprolinase, creatine/creatinine, opine oxidation, and downstream polyamine/GABA aldehyde dehydrogenases (§2.2). These are correctly annotated for their own pathways but must **not** be counted toward putrescine-module satisfiability — a boundary artifact of using a broad KEGG overview map as the starting bucket.

---

## 6. Mechanistic Model / Interpretation

KT2440 provides putrescine through a redundant, well-buffered supply system. Two independent precursors converge on the diamine:

- **Ornithine → putrescine** in a single decarboxylation (SpeC/PP_0864). This is the most direct route and, in the sister species PAO1, is biosynthetically sufficient by itself (a *speA speC* double mutant, not single mutants, is required to abolish putrescine — implying either route alone suffices) [PMID: 12634339].
- **Arginine → agmatine → putrescine.** SpeA (PP_0567) commits arginine, and agmatinase SpeB (PP_2196) completes the conversion in one step. A parallel deiminase branch (AguA/PP_0266 + a missing AguB) could in principle also complete it, but in KT2440 the amidohydrolase appears absent, so the arginine route is effectively single-track through agmatinase.

The functional consequence is that **the module is doubly redundant at the network level** (two precursors) but **single-track within the arginine branch** at the agmatine→putrescine node in KT2440, unlike PAO1 which additionally carries the operonic deiminase branch. This has a concrete curation implication: satisfiability should be scored on SpeA+SpeB+SpeC, and the deiminase branch should be flagged as a lineage-variable alternative that is *incomplete* here, so that presence of AguA alone does not auto-satisfy branch 2b.

The AguA present in KT2440 without an annotated AguB most plausibly functions in **agmatine catabolism/interconversion** rather than a complete biosynthetic branch — unless PP_3019 (or another nitrilase-family gene) supplies a cryptic NCPAH activity. Distinguishing these possibilities is the single most valuable experiment for this module.

---

## 7. Module and GO-Curation Recommendations

| Step | Recommended status | Rationale |
|---|---|---|
| SpeA arginine decarboxylation | **covered** | PP_0567 = K01585, strong orthology |
| Agmatine → putrescine (agmatinase) | **covered** | PP_2196 = K01480, strong orthology |
| Agmatine → putrescine (AguA + AguB) | **candidate_uncertain** | PP_0266 present; AguB (K12251) not annotated; PP_3019 unverified |
| SpeC ornithine decarboxylation | **covered** | PP_0864 = K01581, strong orthology |
| PP_4523 "agmatinase" | **remove from module** | KEGG = guanidinobutyrase K12255 |
| ~33 neighboring-pathway candidates | **not part of module** | AST, proline, oxoprolinase, creatine, GABA catabolism |

**Module boundary verdict:** The generic module boundaries are **correct** for KT2440. The module (SpeA→SpeB arginine route + SpeC ornithine route) is satisfiable, and treating the deiminase branch as an optional/alternative sub-branch is appropriate. **No module revision or new module document is required.** Add an optional note flagging the AguA deiminase branch as a lineage-variable alternative that is incomplete in KT2440 (aguB gap), to prevent auto-satisfaction from aguA alone. Do **not** add PP_1639 (SprT) or treat PP_4523 as an agmatinase step.

**GO-curation notes:** Existing terms suffice — GO:0033389 (putrescine biosynthesis from arginine), GO:0033388 (…from ornithine); activities GO:0008792 (ADC / PP_0567), GO:0008783 (agmatinase / PP_2196), GO:0047632 (agmatine deiminase / PP_0266), GO:0004586 (ODC / PP_0864), GO:0050126 (NCPAH, for any confirmed aguB). All assignments are ISS/orthology (no direct KT2440 evidence). No new GO term request is needed. Flag the PP_2196/PP_4523 pair for a paralog-split curation rule so "agmatinase" is not re-propagated to PP_4523.

---

## 8. Genes to Promote to Full `fetch-gene` Review

1. **PP_4523 (Q88EE2)** — HIGH. Resolve the agmatinase-vs-guanidinobutyrase conflict; confirm K12255/EC 3.5.3.7 and correct the UniProt-derived "Agmatinase" label; remove from module.
2. **PP_3019 (Q88II0)** — HIGH. Test as the candidate N-carbamoylputrescine amidohydrolase (nitrilase family) that would complete the deiminase branch.
3. **PP_0266 (aguA)** — HIGH. Resolve its physiological partner/role given the missing aguB; characterize genomic neighborhood and regulation.
4. **PP_2196 (speB)** — MEDIUM. Confirm agmatinase vs arginase specificity (module step-2 enzyme).
5. **PP_0864 (speC)** — MEDIUM. Confirm biosynthetic (vs biodegradative/inducible) ODC role in KT2440.
6. **PP_0567 (speA)** — LOW/confirmatory. Core, high confidence.

---

## 9. Evidence Base and Key References

All module calls for KT2440 rest on **orthology transfer**, predominantly from *P. aeruginosa* PAO1; there is **no KT2440-strain-specific functional publication** for these genes. Species transfer within *Pseudomonas* is judged **strong** for core enzymatic assignments and **weaker** for pathway architecture details such as the presence/absence of an operonic deiminase branch.

| PMID | Title (abbrev.) | Organism | How it supports/challenges the review |
|---|---|---|---|
| [12634339](https://pubmed.ncbi.nlm.nih.gov/12634339/) | *Identification of putrescine biosynthetic genes in P. aeruginosa; characterization of agmatine deiminase and NCPAH* | *P. aeruginosa* PAO1 | **Foundational.** Defines both routes (ODC/SpeC, ADC/SpeA); AguA+AguB convert agmatine→putrescine; *speA speC* / *aguAB speC* mutants are putrescine auxotrophs; AguB is a nitrilase-family enzyme. Anchors orthology transfer to KT2440. |
| [40673658](https://pubmed.ncbi.nlm.nih.gov/40673658/) | *T6SS toxin Tse8 evolved from a novel NCPAH* | *P. aeruginosa*, *Shewanella*, *Microterricola* | Documents three agmatine→putrescine routes and non-homologous, convergently evolved NCPAHs (AguY). Cautions that a cryptic KT2440 amidohydrolase cannot be excluded by homology alone. |
| [21404211](https://pubmed.ncbi.nlm.nih.gov/21404211/) | *Two enzyme families in putrescine synthesis from agmatine via agmatine deiminase* | Multiple bacteria | Establishes that *aguB* (Gram-negatives) and *ptcA* (Gram-positives) are non-homologous and "frequently erroneously annotated" — directly relevant to the aguB gap and PP_4523 paralog caution. |
| [28862813](https://pubmed.ncbi.nlm.nih.gov/28862813/) | *Polyamine is a critical determinant of P. chlororaphis O6…* | *P. chlororaphis* O6 | *speA* and *speC* both contribute; *speAspeC* mutant eliminates polyamine production. Reinforces the both-routes model in a related pseudomonad. |
| [20149107](https://pubmed.ncbi.nlm.nih.gov/20149107/) | *Operon in agmatine metabolism regulating biofilm in P. aeruginosa* | *P. aeruginosa* PA14 | Shows agmatine-metabolism operon architecture (aguBA and agu2ABCA') varies across strains — supports caution about assuming a KT2440 operon. |
| [18721677](https://pubmed.ncbi.nlm.nih.gov/18721677/) | *Comparative survey of putrescine from agmatine deamination* | Multiple, incl. PAO1 | Confirms agmatine→putrescine flux and regulation differ by organism. |
| [17101165](https://pubmed.ncbi.nlm.nih.gov/17101165/) | *Chlorella viruses encode complete polyamine pathway* | Chloroviruses | Independent characterization of AIH (AguA-like) and CPA (AguB-like) enzymes; corroborates two-step deiminase branch biochemistry. |
| [31451546](https://pubmed.ncbi.nlm.nih.gov/31451546/) | *Arginine biosynthesis modulates pyoverdine in P. putida* | *P. putida* | Context for arginine flux in the target species; not directly on putrescine genes. |
| [36922543](https://pubmed.ncbi.nlm.nih.gov/36922543/) | *Polyamine-mediated oxidative-stress tolerance in P. syringae* | *P. syringae* | Broader *Pseudomonas* context for polyamine physiology. |

**Database evidence (accessed 2026-08-13):** KEGG orthology (rest.kegg.jp): ppu:PP_0567→K01585; PP_2196→K01480; PP_0864→K01581; PP_0266→K10536; PP_4523→K12255; K12251/EC 3.5.1.53 → **no ppu gene**; PP_1639→K02742 (SprT). UniProt (rest.uniprot.org): Q88KU3 & Q88EE2 = arginase family/agmatinase subfamily; Q88II0 = carbon-nitrogen hydrolase (nitrilase) family.

---

## 10. Limitations and Knowledge Gaps

1. **No strain-specific functional data.** Every module call for KT2440 is inferred by orthology. Multiple targeted PubMed searches returned **zero** KT2440-specific functional papers on putrescine/polyamine biosynthesis, agmatinase, or the decarboxylases. The strongest experimental anchors are one genus away (*P. aeruginosa* PAO1; *P. chlororaphis* O6).
2. **The aguB gap is unresolved.** Whether KT2440 has a functional deiminase branch depends on an amidohydrolase (K12251/EC 3.5.1.53) that is not annotated. PP_3019 is a plausible but untested candidate, and convergent AguY-type enzymes [PMID: 40673658] mean absence of a canonical homolog is not proof of absence of activity.
3. **Paralog-driven over-annotation** (PP_2196 vs PP_4523) shows that UniProt family rules can propagate "agmatinase" to a guanidinobutyrase; the KEGG discrimination is trusted here but should be confirmed biochemically.
4. **SpeC type** (biosynthetic vs acid-inducible biodegradative ODC) is not directly confirmed for KT2440.
5. **Bucket breadth.** The broad `ppu00330` map inflates the candidate list; module satisfiability must be judged on the ~5–6 relevant genes, not the 39.

---

## 11. Proposed Follow-up Experiments and Actions

- **Close the aguB gap (highest value):** Assay recombinant PP_3019 for N-carbamoylputrescine amidohydrolase activity; if negative, screen KT2440 nitrilase-superfamily and amidase-family loci. Alternatively, delete *speB* (PP_2196) and test residual agmatine→putrescine flux — residual activity would imply a functional deiminase branch.
- **Genetic validation of core routes:** Construct KT2440 *speB* (PP_2196), *speC* (PP_0864), *speA* (PP_0567), and *speA speC* mutants; test for putrescine auxotrophy as in PAO1 to convert orthology calls into direct evidence.
- **Confirm PP_4523 identity:** Enzymatic assay for guanidinobutyrase (EC 3.5.3.7) vs agmatinase (EC 3.5.3.11); update annotation and add a paralog-split curation rule.
- **Confirm SpeC regulation/type:** Determine whether PP_0864 is constitutive/biosynthetic or acid-inducible under physiological conditions.
- **Curation deliverables:** (a) mark steps 1–3 covered; (b) file aguB/NCPAH as a gap with PP_3019 flagged; (c) remove PP_4523 from the module; (d) exclude the ~33 neighboring-pathway genes from module scoring.

---

*Uncertainty statement:* Step calls rest on 1:1 KEGG orthology plus experimental validation in the sister species *P. aeruginosa* PAO1 and *P. chlororaphis* O6 (strong same-genus transfer). No KT2440-strain-specific functional study of speA/speB/speC/aguA (knockout, enzymology, or polyamine-pool measurement) was located — so all target-organism calls are homology-based inferences, not direct evidence. The completeness of the agmatine-deiminase branch and the identity of PP_3019 as NCPAH are open questions requiring biochemical confirmation.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_putrescine_biosynthesis__ppu00330-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_putrescine_biosynthesis__ppu00330-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12634339
2. PMID:28862813
3. PMID:40673658
4. PMID:21404211