---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T20:20:02.139210'
end_time: '2026-08-31T20:38:10.134081'
duration_seconds: 1087.99
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial sodium-coupled proline uptake and fused-PutA catabolism
  module_summary: A reusable bacterial module in which a PutP-family sodium/proline
    symporter imports L-proline and a fused PutA protein oxidizes it to L-glutamate
    in two catalytic steps. The FAD-dependent PutA PRODH domain transfers electrons
    to a quinone while forming P5C, and the NAD-dependent GSALDH domain oxidizes the
    ring-opened glutamate 5-semialdehyde intermediate to L-glutamate.
  module_outline: "- Bacterial sodium-coupled proline uptake and fused-PutA catabolism\n\
    \  - 1. sodium-coupled proline uptake\n  - PutP sodium/proline symport\n    -\
    \ PutP sodium/proline symporter activity (molecular player: bacterial PutP sodium/proline\
    \ symporter family; activity or role: proline:sodium symporter activity)\n  -\
    \ 2. quinone-linked proline oxidation\n  - PutA proline dehydrogenase reaction\n\
    \    - Fused PutA proline dehydrogenase domain (molecular player: full-length\
    \ PSEPK PutA; activity or role: proline dehydrogenase activity)\n  - 3. glutamate\
    \ semialdehyde oxidation\n  - PutA glutamate-semialdehyde dehydrogenase reaction\n\
    \    - Fused PutA glutamate-semialdehyde dehydrogenase domain (molecular player:\
    \ full-length PSEPK PutA; activity or role: L-glutamate gamma-semialdehyde dehydrogenase\
    \ activity)"
  module_connections: '- PutP sodium/proline symport feeds into PutA proline dehydrogenase
    reaction: PutP supplies cytoplasmic L-proline to PutA.

    - PutA proline dehydrogenase reaction feeds into PutA glutamate-semialdehyde dehydrogenase
    reaction: PutA-produced P5C undergoes nonenzymatic ring opening to glutamate 5-semialdehyde,
    which is consumed by the second active site.'
  pathway_query: ppu00250
  pathway_id: ppu00250
  pathway_name: Alanine, aspartate and glutamate metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00250 with 8 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '36'
  candidate_genes: '- argH: PP_0184 | P59618 | Argininosuccinate lyase (ASAL) (EC
    4.3.2.1) (Arginosuccinase) (EC 4.3.2.1; primary bucket kegg:ppu00220)

    - davD: PP_0213 | Q88RC0 | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) (EC
    1.2.1.-; primary bucket kegg:ppu00350)

    - davT: PP_0214 | Q88RB9 | 5-aminovalerate aminotransferase DavT (EC 2.6.1.48)
    (5-aminovalerate transaminase) (Delta-aminovalerate aminotransferase) (EC 2.6.1.48;
    primary bucket kegg:ppu00310)

    - ansA: PP_0495 | Q88QJ6 | Type 1 L-asparaginase (EC 3.5.1.1) (EC 3.5.1.1; primary
    bucket kegg:ppu00460)

    - gdhA: PP_0675 | Q88Q23 | Glutamate dehydrogenase (primary bucket kegg:ppu00910)

    - PP_0859: PP_0859 | Q88PJ1 | Omega-amidase YafV (EC 3.5.1.3) (EC 3.5.1.3; primary
    bucket kegg:ppu00250)

    - argG: PP_1088 | P59604 | Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate
    ligase) (EC 6.3.4.5; primary bucket kegg:ppu00220)

    - PP_1160: PP_1160 | Q88NP7 | Asparaginase family protein (primary bucket kegg:ppu00460)

    - nadB: PP_1426 | Q88MZ2 | L-aspartate oxidase (EC 1.4.3.16) (EC 1.4.3.16; primary
    bucket kegg:ppu00760)

    - asnB: PP_1750 | Q88M25 | asparagine synthase (glutamine-hydrolyzing) (EC 6.3.5.4)
    (EC 6.3.5.4; primary bucket kegg:ppu00250)

    - alaA: PP_1872 | Q88LQ7 | Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2)
    (EC 2.6.1.2; primary bucket kegg:ppu00290)

    - purF: PP_2000 | Q88LD5 | Amidophosphoribosyltransferase (ATase) (EC 2.4.2.14)
    (Glutamine phosphoribosylpyrophosphate amidotransferase) (GPATase) (EC 2.4.2.14;
    primary bucket kegg:ppu00250)

    - gdhB: PP_2080 | Q88L55 | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) (EC
    1.4.1.2; primary bucket kegg:ppu00430)

    - puuA-I: PP_2178 | Q88KW1 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11;
    primary bucket kegg:ppu00910)

    - ansB: PP_2453 | Q88K39 | Glutaminase-asparaginase (EC 3.5.1.38) (L-ASNase/L-GLNase)
    (L-asparagine/L-glutamine amidohydrolase) (EC 3.5.1.38; primary bucket kegg:ppu00470)

    - sad-I: PP_2488 | Q88K05 | NAD+-dependent succinate semialdehyde dehydrogenase
    (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00350)

    - PP_2799: PP_2799 | Q88J50 | Aminotransferase, class III (primary bucket kegg:ppu00250)

    - PP_3148: PP_3148 | Q88I53 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - sad-II: PP_3151 | Q88I50 | NAD+-dependent succinate semialdehyde dehydrogenase
    (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00760)

    - purB: PP_4016 | Q88FR7 | Adenylosuccinate lyase (ASL) (EC 4.3.2.2) (Adenylosuccinase)
    (EC 4.3.2.2; primary bucket kegg:ppu00250)

    - PP_4399: PP_4399 | Q88EQ4 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - gabD-II: PP_4422 | Q88EN2 | Succinate-semialdehyde dehydrogenase (NADP+) (EC
    1.2.1.79) (EC 1.2.1.79; primary bucket kegg:ppu00350)

    - PP_4547: PP_4547 | Q88EB9 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - carB: PP_4723 | Q88DU6 | Carbamoyl phosphate synthase large chain (EC 6.3.4.16)
    (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain) (EC 6.3.4.16; 6.3.5.5;
    primary bucket kegg:ppu00220)

    - carA: PP_4724 | Q88DU5 | Carbamoyl phosphate synthase small chain (EC 6.3.5.5)
    (Carbamoyl phosphate synthetase glutamine chain) (EC 6.3.5.5; primary bucket kegg:ppu00220)

    - purA: PP_4889 | Q88DD8 | Adenylosuccinate synthetase (AMPSase) (AdSS) (EC 6.3.4.4)
    (IMP--aspartate ligase) (EC 6.3.4.4; primary bucket kegg:ppu00250)

    - putA: PP_4947 | Q88D80 | Bifunctional protein PutA [Includes: Proline dehydrogenase
    (EC 1.5.5.2) (Proline oxidase); Delta-1-pyrroline-5-carboxylate dehydrogenase
    (P5C dehydrogenase) (EC 1.2.1.88) (L-glutamate gamma-semialdehyde dehydrogenase)]
    (EC 1.2.1.88; 1.5.5.2; primary bucket kegg:ppu00250)

    - pyrB: PP_4998 | Q88D30 | Aspartate carbamoyltransferase catalytic subunit (EC
    2.1.3.2) (Aspartate transcarbamylase) (ATCase) (EC 2.1.3.2; primary bucket kegg:ppu00240)

    - glnA: PP_5046 | Q88CY3 | Glutamine synthetase (EC 6.3.1.2) (EC 6.3.1.2; primary
    bucket kegg:ppu00910)

    - gltD: PP_5075 | Q88CV5 | Glutamate synthase (NADPH) beta subunit (EC 1.4.1.13)
    (EC 1.4.1.13; primary bucket kegg:ppu00910)

    - gltB: PP_5076 | Q88CV4 | Glutamate synthase [NADPH] large chain (EC 1.4.1.13)
    (Glutamate synthase subunit alpha) (EC 1.4.1.13; primary bucket kegg:ppu00910)

    - spuB: PP_5183 | Q88CJ7 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)

    - spuI: PP_5184 | Q88CJ6 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)

    - puuA-II: PP_5299 | Q88C84 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11;
    primary bucket kegg:ppu00910)

    - aspA: PP_5338 | Q88C45 | Aspartate ammonia-lyase (Aspartase) (EC 4.3.1.1) (EC
    4.3.1.1; primary bucket kegg:ppu00250)

    - glmS: PP_5409 | Q88BX8 | Glutamine--fructose-6-phosphate aminotransferase [isomerizing]
    (EC 2.6.1.16) (D-fructose-6-phosphate amidotransferase) (GFAT) (Glucosamine-6-phosphate
    synthase) (Hexosephosphate aminotransferase) (L-glutamine--D-fructose-6-phosphate
    amidotransferase) (EC 2.6.1.16; primary bucket kegg:ppu00520)'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_fused_puta_proline_catabolism__ppu00250-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_fused_puta_proline_catabolism__ppu00250-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial sodium-coupled proline uptake and fused-PutA catabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00250
- Resolved ID: ppu00250
- Resolved name: Alanine, aspartate and glutamate metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00250 with 8 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 36

- argH: PP_0184 | P59618 | Argininosuccinate lyase (ASAL) (EC 4.3.2.1) (Arginosuccinase) (EC 4.3.2.1; primary bucket kegg:ppu00220)
- davD: PP_0213 | Q88RC0 | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) (EC 1.2.1.-; primary bucket kegg:ppu00350)
- davT: PP_0214 | Q88RB9 | 5-aminovalerate aminotransferase DavT (EC 2.6.1.48) (5-aminovalerate transaminase) (Delta-aminovalerate aminotransferase) (EC 2.6.1.48; primary bucket kegg:ppu00310)
- ansA: PP_0495 | Q88QJ6 | Type 1 L-asparaginase (EC 3.5.1.1) (EC 3.5.1.1; primary bucket kegg:ppu00460)
- gdhA: PP_0675 | Q88Q23 | Glutamate dehydrogenase (primary bucket kegg:ppu00910)
- PP_0859: PP_0859 | Q88PJ1 | Omega-amidase YafV (EC 3.5.1.3) (EC 3.5.1.3; primary bucket kegg:ppu00250)
- argG: PP_1088 | P59604 | Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate ligase) (EC 6.3.4.5; primary bucket kegg:ppu00220)
- PP_1160: PP_1160 | Q88NP7 | Asparaginase family protein (primary bucket kegg:ppu00460)
- nadB: PP_1426 | Q88MZ2 | L-aspartate oxidase (EC 1.4.3.16) (EC 1.4.3.16; primary bucket kegg:ppu00760)
- asnB: PP_1750 | Q88M25 | asparagine synthase (glutamine-hydrolyzing) (EC 6.3.5.4) (EC 6.3.5.4; primary bucket kegg:ppu00250)
- alaA: PP_1872 | Q88LQ7 | Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2) (EC 2.6.1.2; primary bucket kegg:ppu00290)
- purF: PP_2000 | Q88LD5 | Amidophosphoribosyltransferase (ATase) (EC 2.4.2.14) (Glutamine phosphoribosylpyrophosphate amidotransferase) (GPATase) (EC 2.4.2.14; primary bucket kegg:ppu00250)
- gdhB: PP_2080 | Q88L55 | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) (EC 1.4.1.2; primary bucket kegg:ppu00430)
- puuA-I: PP_2178 | Q88KW1 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11; primary bucket kegg:ppu00910)
- ansB: PP_2453 | Q88K39 | Glutaminase-asparaginase (EC 3.5.1.38) (L-ASNase/L-GLNase) (L-asparagine/L-glutamine amidohydrolase) (EC 3.5.1.38; primary bucket kegg:ppu00470)
- sad-I: PP_2488 | Q88K05 | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00350)
- PP_2799: PP_2799 | Q88J50 | Aminotransferase, class III (primary bucket kegg:ppu00250)
- PP_3148: PP_3148 | Q88I53 | Glutamine synthetase (primary bucket kegg:ppu00910)
- sad-II: PP_3151 | Q88I50 | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00760)
- purB: PP_4016 | Q88FR7 | Adenylosuccinate lyase (ASL) (EC 4.3.2.2) (Adenylosuccinase) (EC 4.3.2.2; primary bucket kegg:ppu00250)
- PP_4399: PP_4399 | Q88EQ4 | Glutamine synthetase (primary bucket kegg:ppu00910)
- gabD-II: PP_4422 | Q88EN2 | Succinate-semialdehyde dehydrogenase (NADP+) (EC 1.2.1.79) (EC 1.2.1.79; primary bucket kegg:ppu00350)
- PP_4547: PP_4547 | Q88EB9 | Glutamine synthetase (primary bucket kegg:ppu00910)
- carB: PP_4723 | Q88DU6 | Carbamoyl phosphate synthase large chain (EC 6.3.4.16) (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain) (EC 6.3.4.16; 6.3.5.5; primary bucket kegg:ppu00220)
- carA: PP_4724 | Q88DU5 | Carbamoyl phosphate synthase small chain (EC 6.3.5.5) (Carbamoyl phosphate synthetase glutamine chain) (EC 6.3.5.5; primary bucket kegg:ppu00220)
- purA: PP_4889 | Q88DD8 | Adenylosuccinate synthetase (AMPSase) (AdSS) (EC 6.3.4.4) (IMP--aspartate ligase) (EC 6.3.4.4; primary bucket kegg:ppu00250)
- putA: PP_4947 | Q88D80 | Bifunctional protein PutA [Includes: Proline dehydrogenase (EC 1.5.5.2) (Proline oxidase); Delta-1-pyrroline-5-carboxylate dehydrogenase (P5C dehydrogenase) (EC 1.2.1.88) (L-glutamate gamma-semialdehyde dehydrogenase)] (EC 1.2.1.88; 1.5.5.2; primary bucket kegg:ppu00250)
- pyrB: PP_4998 | Q88D30 | Aspartate carbamoyltransferase catalytic subunit (EC 2.1.3.2) (Aspartate transcarbamylase) (ATCase) (EC 2.1.3.2; primary bucket kegg:ppu00240)
- glnA: PP_5046 | Q88CY3 | Glutamine synthetase (EC 6.3.1.2) (EC 6.3.1.2; primary bucket kegg:ppu00910)
- gltD: PP_5075 | Q88CV5 | Glutamate synthase (NADPH) beta subunit (EC 1.4.1.13) (EC 1.4.1.13; primary bucket kegg:ppu00910)
- gltB: PP_5076 | Q88CV4 | Glutamate synthase [NADPH] large chain (EC 1.4.1.13) (Glutamate synthase subunit alpha) (EC 1.4.1.13; primary bucket kegg:ppu00910)
- spuB: PP_5183 | Q88CJ7 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)
- spuI: PP_5184 | Q88CJ6 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)
- puuA-II: PP_5299 | Q88C84 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11; primary bucket kegg:ppu00910)
- aspA: PP_5338 | Q88C45 | Aspartate ammonia-lyase (Aspartase) (EC 4.3.1.1) (EC 4.3.1.1; primary bucket kegg:ppu00250)
- glmS: PP_5409 | Q88BX8 | Glutamine--fructose-6-phosphate aminotransferase [isomerizing] (EC 2.6.1.16) (D-fructose-6-phosphate amidotransferase) (GFAT) (Glucosamine-6-phosphate synthase) (Hexosephosphate aminotransferase) (L-glutamine--D-fructose-6-phosphate amidotransferase) (EC 2.6.1.16; primary bucket kegg:ppu00520)

## Generic Module Context

### Working Scope

A reusable bacterial module in which a PutP-family sodium/proline symporter imports L-proline and a fused PutA protein oxidizes it to L-glutamate in two catalytic steps. The FAD-dependent PutA PRODH domain transfers electrons to a quinone while forming P5C, and the NAD-dependent GSALDH domain oxidizes the ring-opened glutamate 5-semialdehyde intermediate to L-glutamate.

### Provisional Biological Outline

- Bacterial sodium-coupled proline uptake and fused-PutA catabolism
  - 1. sodium-coupled proline uptake
  - PutP sodium/proline symport
    - PutP sodium/proline symporter activity (molecular player: bacterial PutP sodium/proline symporter family; activity or role: proline:sodium symporter activity)
  - 2. quinone-linked proline oxidation
  - PutA proline dehydrogenase reaction
    - Fused PutA proline dehydrogenase domain (molecular player: full-length PSEPK PutA; activity or role: proline dehydrogenase activity)
  - 3. glutamate semialdehyde oxidation
  - PutA glutamate-semialdehyde dehydrogenase reaction
    - Fused PutA glutamate-semialdehyde dehydrogenase domain (molecular player: full-length PSEPK PutA; activity or role: L-glutamate gamma-semialdehyde dehydrogenase activity)

### Known Relationships Among Steps

- PutP sodium/proline symport feeds into PutA proline dehydrogenase reaction: PutP supplies cytoplasmic L-proline to PutA.
- PutA proline dehydrogenase reaction feeds into PutA glutamate-semialdehyde dehydrogenase reaction: PutA-produced P5C undergoes nonenzymatic ring opening to glutamate 5-semialdehyde, which is consumed by the second active site.

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

# Species-Aware Module Review: Sodium-Coupled Proline Uptake and Fused-PutA Catabolism in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module:** Bacterial Na⁺-coupled proline uptake + fused-PutA catabolism of L-proline → L-glutamate
**Local bucket reviewed:** `kegg:ppu00250` ("Alanine, aspartate and glutamate metabolism", 36 candidate genes)
**Date:** 2026-09-01

---

## 1. Executive summary

The module is **fully satisfiable** in *P. putida* KT2440, but the local `ppu00250` candidate bucket is the **wrong container** for it and is missing its transporter. All three expected steps are encoded by just **two adjacent genes**:

- **Step 1 (Na⁺/proline uptake):** `putP` / **PP_4946** (Q88D81) — a bona fide Na⁺/proline symporter of the SSS family. **This gene is absent from the 36-gene candidate list** because transporters are not part of the KEGG `ppu00250` map.
- **Steps 2 + 3 (proline → glutamate):** `putA` / **PP_4947** (Q88D80) — a **1317-aa fused enzyme** with an FAD-dependent, quinone-linked proline dehydrogenase (PRODH; EC 1.5.5.2) domain and an NAD-dependent L-glutamate-γ-semialdehyde dehydrogenase (GSALDH/P5CDH; EC 1.2.1.88) domain.

Two curation-critical corrections emerge:

1. **PutA is trifunctional, not "bifunctional."** In addition to the two catalytic domains, KT2440 PutA carries an N-terminal ribbon-helix-helix (RHH) DNA-binding domain and acts as an autogenous repressor of the *put* operon. This is supported by **direct target-species structural data** (PDB **2JXI**: NMR of the *P. putida* PutA DNA-binding domain bound to its operator DNA).
2. **The module belongs to KEGG map00330 (Arginine and proline metabolism), not ppu00250.** Only 1 of the 36 candidates (`putA`) is mechanistically part of the module; ~34 are unrelated Ala/Asp/Glu/purine enzymes, and the transporter is missing. `ppu00250` should be treated as a downstream sink (PutA-derived glutamate feeds into it), not the module's home map.

Overall confidence is **high**: the assignments rest on the specific InterPro/SSS-family signature for PutP, the multi-domain architecture and pathway annotation for PutA, and a direct *P. putida* structure for the regulatory domain.

---

## 2. Target-organism pathway definition

**Included process (this module):** the catabolic route by which extracellular L-proline is (i) imported across the inner membrane by a **Na⁺-coupled proline symporter (PutP)** and (ii) oxidized in the cytoplasm to L-glutamate by the fused flavo-/NAD-enzyme **PutA**. PutA performs a 4-electron oxidation: the PRODH (FAD) half-reaction oxidizes proline to Δ¹-pyrroline-5-carboxylate (P5C), passing electrons to the membrane quinone pool; P5C non-enzymatically ring-opens to L-glutamate-γ-semialdehyde (GSA), which the GSALDH half-reaction oxidizes (NAD⁺) to L-glutamate (PMID 28712849).

**Alternate names / database definitions.**
- Enzyme names: proline dehydrogenase = proline oxidase (EC 1.5.5.2, "proline dehydrogenase (quinone)"); GSALDH = Δ¹-pyrroline-5-carboxylate dehydrogenase = P5C dehydrogenase = P5CDH (EC 1.2.1.88).
- Pathway: UniProt "L-proline degradation into L-glutamate" (steps 1/2 and 2/2); KEGG map00330 "Arginine and proline metabolism"; MetaCyc "L-proline degradation" (PROUT-PWY).
- Genes: `putP` (permease), `putA` (fused catabolic enzyme); the operon is the *putPA* / *put* regulon.

**Neighboring pathways to keep separate.**
- **Proline *biosynthesis*** (opposite direction): `proB`/PP_0691, `proA`/PP_4811, `proC`/PP_5095 (+ PP_3778). These make proline from glutamate and must NOT be merged into the catabolic module.
- **Osmoprotectant proline *uptake*** (different physiology): `proP`/PP_2914 (MFS osmosensory proline/betaine/H⁺ permease) and the glycine-betaine/proline ABC transporter (PP_2774–PP_2775). These import proline/betaine as compatible solutes under osmotic stress; they are H⁺- or ATP-coupled, not the Na⁺-coupled catabolic feeder.
- **Ala/Asp/Glu metabolism (`ppu00250`)**, glutamate/glutamine metabolism (`ppu00910`), arginine/urea-cycle (`ppu00220`), and 4-hydroxyproline catabolism (`proR`/PP_1258, PP_1255) — all downstream/adjacent, not part of this module.

---

## 3. Expected step model

| # | Expected step | Molecular activity | KT2440 gene | Status |
|---|---------------|--------------------|-------------|--------|
| 1 | Na⁺-coupled proline uptake | proline:Na⁺ symporter (GO:0005298) | **putP / PP_4946** | **covered** (add to module) |
| 2 | Quinone-linked proline oxidation | proline dehydrogenase, FAD→quinone (EC 1.5.5.2) | **putA / PP_4947** (PRODH domain) | **covered** |
| 3 | Glutamate-semialdehyde oxidation | L-glutamate-γ-semialdehyde dehydrogenase, NAD⁺ (EC 1.2.1.88) | **putA / PP_4947** (GSALDH domain) | **covered** |
| — | (Regulatory, not in generic outline) | RHH DNA-binding autorepressor of *put* operon | **putA / PP_4947** (RHH domain) | present (module extension) |

The two known inter-step relationships hold in KT2440: PutP supplies cytoplasmic proline to PutA, and PutA's P5C→GSA intermediate is passed between the two active sites. In fused PutAs this hand-off is a **substrate-channeling** tunnel connecting the ~42-Å-separated active sites, demonstrated structurally and kinetically for the PutA family (PMID 28712849; PMID 40738191; channeling first shown for a PRODH–P5CDH pair, PMID 25492892). Transfer of the channeling mechanism to KT2440 is **strong** (conserved fused architecture; same enzyme family and domain order).

---

## 4. Candidate genes and evidence

### High-confidence, in-module genes

**putA — PP_4947 (Q88D80)** — *covered (steps 2 & 3); promote to full review.*
- Role: fused proline→glutamate catabolic enzyme. Domains (UniProt/InterPro): PutA RHH DNA-binding (res 11–43; IPR013321), PRODH/FAD (res ~87–567; IPR025703, IPR029041), Aldehyde-dehydrogenase/GSALDH (res 654–1101; IPR015590/IPR016161-63; active-site residues ~881/915). Length 1317 aa.
- Evidence type: **direct target-species structure** for the regulatory domain (PDB 2JXI, *P. putida* PutA DNA-binding domain + operator DNA, solution NMR); UniProt catalytic/pathway annotation (EC 1.5.5.2 + EC 1.2.1.88; "L-proline degradation into L-glutamate"). Mechanistic detail transferred from the well-characterized PutA family (PMIDs 28712849, 27679491).
- **Caveat:** the metadata name "Bifunctional protein PutA" and the module outline ("fused PutA … two catalytic steps") **understate** the protein — KT2440 PutA is **trifunctional** (adds autogenous transcriptional repression). This matches the report that *P. putida* PutA, unlike *P. aeruginosa* PutA, retains a regulatory function (PMID 12270821).

**putP — PP_4946 (Q88D81)** — *covered (step 1); MISSING from candidate list; promote to full review.*
- Role: Na⁺/proline symporter (proline permease), 542 aa. InterPro IPR011851 (Na/Pro_symporter) + IPR001734/IPR018212 (Na/solute symporter, SSS family); GO:0005298 proline:sodium symporter, GO:0031402 sodium-ion binding. Immediately adjacent to `putA`.
- Evidence type: family-diagnostic signature (strong) + genomic context (adjacent to *putA*, canonical *putPA* arrangement). The *P. aeruginosa putAP* study notes 80 % PutP identity to the *P. putida* counterpart (PMID 12270821). PutP mechanism/Na⁺-coupling is well established for the family (PMIDs 33668649, 24358297, 27793991).
- **Caveat:** not in `ppu00250`; must be added to the module manually.

### Candidate-list genes that are NOT in this module (representative)
All remaining 34 candidates are downstream/adjacent amino-acid or nucleotide enzymes, e.g. `glnA`/`PP_3148`/`PP_4399`/`PP_4547` (glutamine synthetases), `gltB`/`gltD` (glutamate synthase), `gdhA`/`gdhB` (glutamate dehydrogenases), `asnB`, `ansA`/`ansB`, `aspA`, `carA`/`carB`, `pyrB`, `purA`/`purB`/`purF`, `argG`/`argH`, `glmS`, `davT`/`davD`, `sad-I/II`, `gabD-II`. They handle glutamate/glutamine/aspartate/asparagine/arginine/purine/polyamine metabolism. **None** participate in proline uptake or PutA catabolism; PutA-derived glutamate merely feeds them.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Missing transporter in metadata (gap in candidate list, not in genome):** `putP`/PP_4946 is present in the genome and is the module's uptake step but is absent from the `ppu00250` candidate set. Action: add PP_4946.
- **PutA "bifunctional" label = under-annotation:** should read trifunctional (PRODH + GSALDH + RHH autorepressor). Direct evidence: PDB 2JXI.
- **Transporter paralog ambiguity / likely over-annotation:** **PP_3331 (Q88HM3)** is named "Sodium:proline symporter" but its only InterPro domain is IPR005625 (PepSY-associated TM helix) — **no SSS/symporter domain**. Its proline-symporter name is a **likely over-propagated annotation**; do not count it as a second PutP without review. Mark `candidate_uncertain`.
- **Osmolyte transporters are not catabolic feeders:** `proP`/PP_2914 and the betaine/proline ABC system (PP_2774–75) import proline as an osmoprotectant; keep them out of this module (different coupling ion/energetics and physiological role).
- **Electron-acceptor detail:** PRODH is quinone-linked (EC 1.5.5.2); in aerobic *P. putida* the physiological acceptor is ubiquinone. This is inferred from EC assignment and family biochemistry (strong), not from a KT2440-specific electron-transfer measurement.
- **No direct KT2440 growth/mutant paper retrieved** in this review demonstrating proline as sole C/N source for KT2440 specifically; the phenotype is firmly established genus-wide (*P. aeruginosa* PMID 12270821) and mechanistically for the PutA family. Transfer to KT2440 is strong by orthology + operon structure + the *P. putida* PutA structure, but a strain-specific growth/fitness citation would upgrade this from "inferred" to "direct."

---

## 6. Module and GO-curation recommendations

**Step status calls**
- Step 1 (Na⁺-coupled proline uptake): **covered** by PP_4946 (`putP`). *Add gene to module.*
- Step 2 (quinone-linked proline oxidation): **covered** by PP_4947 PRODH domain.
- Step 3 (glutamate-semialdehyde oxidation): **covered** by PP_4947 GSALDH domain.
- Regulatory sub-function (not in generic outline): **present** — RHH autorepressor domain of PP_4947.

**Boundary / module-document actions**
- `module_needs_revision` for the local bucket mapping: the module is anchored to `kegg:ppu00250`, which neither contains the transporter nor scopes proline catabolism. **Re-anchor to KEGG map00330 (Arg/Pro metabolism) / MetaCyc PROUT-PWY**, and record `ppu00250` only as the downstream glutamate sink.
- Update the module's PutA descriptor from "bifunctional/fused, two catalytic steps" to **"trifunctional: PRODH + GSALDH + RHH autoregulator (autogenous *put*-operon repressor)."** Optionally add a fourth (regulatory) node or a note, since the generic outline omits it.
- Keep biosynthetic (`proBAC`) and osmoprotectant-uptake (`proP`, betaine/proline ABC) genes explicitly excluded to prevent future over-merging.

**GO annotations supported for KT2440 PutA (PP_4947)**
- GO:0004657 proline dehydrogenase activity; GO:0003842 (1-pyrroline-5-carboxylate / L-glutamate-γ-semialdehyde dehydrogenase) activity; GO:0071949 FAD binding; GO:0010133 proline catabolic process to glutamate.
- Regulatory: GO:0003700 DNA-binding transcription factor activity / GO:0003677 DNA binding and GO:0045892 negative regulation of transcription — **directly supported by PDB 2JXI** (operator-bound DNA-binding domain). Recommend adding these to the KT2440 PutA record if not present.
- PutP (PP_4946): GO:0005298 proline:sodium symporter activity and GO:0015824 proline transport (already annotated).

No new GO *terms* appear to be needed — existing terms cover all activities. The main deliverables are (a) adding PP_4946 to the module, (b) correcting the PutA functional description, and (c) re-anchoring the map boundary.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_4947 `putA`** (Q88D80) — core catalytic + regulatory; verify trifunctional annotation, active-site residues, quinone acceptor, and add regulatory GO terms.
2. **PP_4946 `putP`** (Q88D81) — module's uptake step, currently missing from the candidate set; confirm Na⁺-coupling and add to module.
3. **PP_3331** (Q88HM3) — resolve the "Sodium:proline symporter" name vs. its PepSY-only domain content; likely over-annotation (`candidate_uncertain`).

Lower priority (boundary confirmation only): `proP`/PP_2914 and PP_2774–75 (confirm exclusion as osmolyte transporters).

---

## 8. Key references

- Nakada Y, Nishijyo T, Itoh Y. *Divergent structure and regulatory mechanism of proline catabolic systems: … putAP operon of Pseudomonas aeruginosa PAO1 …* J Bacteriol. 2002. **PMID 12270821.** (PutP ~80 % identity to *P. putida*; *P. putida*/enteric PutA retain a regulatory function.)
- PDB **2JXI** — *Solution structure of the DNA-binding domain of Pseudomonas putida Proline utilization A (PutA) bound to GTTGCA DNA* (solution NMR; maps to UniProt Q88D80/PP_4947). Direct target-species evidence for the RHH autorepressor.
- Liu LK, Becker DF, Tanner JJ. *Structure, function, and mechanism of proline utilization A (PutA).* Arch Biochem Biophys. 2017. **PMID 28712849.**
- Luo M, et al. (Tanner). *Structures of Proline Utilization A (PutA) Reveal the Fold and Functions of the ALDH-superfamily DUF domain.* 2016. **PMID 27679491.**
- Sanyal N, et al. (Becker/Tanner). *First evidence for substrate channeling between proline catabolic enzymes …* J Biol Chem. 2015. **PMID 25492892.**
- Buckley, Becker, Tanner. *Visualization of covalent intermediates and conformational states of PutA …* 2025. **PMID 40738191.** (channeling tunnel; 42-Å active-site separation.)
- Henriquez T, et al. (Jung). *Prokaryotic Solute/Sodium Symporters …* 2021. **PMID 33668649.** (PutP as the archetypal bacterial Na⁺/proline symporter.)
- Rivera-Ordaz A, et al. (Jung). *The sodium/proline transporter PutP of Helicobacter pylori.* 2013. **PMID 24358297.** (Na⁺-exclusive proline symport by PutP.)
- UniProt: Q88D80 (PutA/PP_4947), Q88D81 (PutP/PP_4946), Q88HM3 (PP_3331). InterPro: IPR011851 (Na/Pro_symporter), IPR013321 (Arc RHH), IPR025703 (Bifunct_PutA). KEGG map00330 (Arginine and proline metabolism).

---

### Evidence-strength ledger

| Claim | Evidence basis | Strength for KT2440 |
|-------|----------------|---------------------|
| PutP (PP_4946) is the Na⁺/proline uptake step | SSS-family InterPro signature + operon context + genus homology | Strong |
| PutA (PP_4947) performs both oxidation steps | UniProt catalytic + pathway annotation; conserved family mechanism | Strong |
| PutA is trifunctional (adds DNA-binding repressor) | **Direct** *P. putida* structure (PDB 2JXI) + PMID 12270821 | Strong / direct |
| PRODH acceptor is ubiquinone | EC 1.5.5.2 + family biochemistry | Moderate (inferred) |
| PP_3331 is a genuine second PutP | Name only; domain content contradicts | Weak → likely over-annotation |
| KT2440 grows on proline as sole C/N | Genus/family evidence; no strain-specific paper retrieved here | Moderate (inferred) |


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_fused_puta_proline_catabolism__ppu00250-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_fused_puta_proline_catabolism__ppu00250-deep-research-openscientist_artifacts/final_report.pdf)