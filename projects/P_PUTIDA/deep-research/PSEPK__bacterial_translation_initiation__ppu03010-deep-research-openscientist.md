---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T13:01:41.698100'
end_time: '2026-09-01T14:18:10.062540'
duration_seconds: 4588.36
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial translation initiation
  module_summary: A reusable bacterial module for assembly of a translation-competent
    70S initiation complex. IF2 and IF3 associate with the 30S subunit early, IF1
    stabilizes their binding and organizes the preinitiation complex, and IF2 promotes
    initiator fMet-tRNA accommodation and 50S joining while hydrolyzing GTP. The boundary
    ends with factor release and formation of the mature 70S initiation complex. Ribosome
    biogenesis, initiator-tRNA aminoacylation and formylation, elongation, and termination
    are excluded. RRF/EF-G-driven recycling is outside the module, but IF3 stabilization
    of newly split 30S subunits is retained as the recycling-to-initiation interface.
  module_outline: "- Bacterial translation initiation\n  - 1. early 30S initiation-factor\
    \ loading and subunit availability\n  - Early IF2 and IF3 loading on the 30S subunit\n\
    \    - IF2 early 30S initiation role (molecular player: translation initiation\
    \ factor IF2-related family; activity or role: translation initiation factor activity)\n\
    \    - IF3 free-30S maintenance role (molecular player: translation initiation\
    \ factor IF3 family; activity or role: translation initiation factor activity)\n\
    \  - 2. IF1-stabilized preinitiation-complex assembly\n  - IF1 stabilization of\
    \ the 30S preinitiation complex\n    - IF1 initiation-factor activity (molecular\
    \ player: translation initiation factor IF1 family; activity or role: translation\
    \ initiation factor activity)\n  - 3. initiator-tRNA accommodation and large-subunit\
    \ joining\n  - IF2-dependent initiator-tRNA accommodation and 50S joining\n  \
    \  - IF2 GTPase activity during 70S-complex formation (molecular player: translation\
    \ initiation factor IF2-related family; activity or role: GTPase activity)"
  module_connections: '- Early IF2 and IF3 loading on the 30S subunit precedes IF1
    stabilization of the 30S preinitiation complex: Real-time kinetic measurements
    support IF2/IF3 arrival before IF1 as a favored Escherichia coli assembly route;
    this edge does not require a strict universal sequence in every bacterium or condition.

    - IF1 stabilization of the 30S preinitiation complex precedes IF2-dependent initiator-tRNA
    accommodation and 50S joining: IF1-stabilized preinitiation assembly precedes
    IF2-dependent GTP hydrolysis, 50S joining, and factor release.'
  pathway_query: ppu03010
  pathway_id: ppu03010
  pathway_name: Ribosome
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03010 with 54 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '54'
  candidate_genes: '- rpmH: PP_0009 | P0A161 | Large ribosomal subunit protein bL34
    (50S ribosomal protein L34) (primary bucket kegg:ppu03010)

    - rpsU: PP_0389 | P0A165 | Small ribosomal subunit protein bS21 (30S ribosomal
    protein S21) (primary bucket kegg:ppu03010)

    - rplK: PP_0443 | Q88QP5 | Large ribosomal subunit protein uL11 (50S ribosomal
    protein L11) (primary bucket kegg:ppu03010)

    - rplA: PP_0444 | Q88QP4 | Large ribosomal subunit protein uL1 (50S ribosomal
    protein L1) (primary bucket kegg:ppu03010)

    - rplJ: PP_0445 | Q88QP3 | Large ribosomal subunit protein uL10 (50S ribosomal
    protein L10) (primary bucket kegg:ppu03010)

    - rplL: PP_0446 | P0A157 | Large ribosomal subunit protein bL12 (50S ribosomal
    protein L7/L12) (primary bucket kegg:ppu03010)

    - rpsL: PP_0449 | Q88QP0 | Small ribosomal subunit protein uS12 (30S ribosomal
    protein S12) (primary bucket kegg:ppu03010)

    - rpsG: PP_0450 | Q88QN9 | Small ribosomal subunit protein uS7 (30S ribosomal
    protein S7) (primary bucket kegg:ppu03010)

    - rpsJ: PP_0453 | Q88QN6 | Small ribosomal subunit protein uS10 (30S ribosomal
    protein S10) (primary bucket kegg:ppu03010)

    - rplC: PP_0454 | Q88QN5 | Large ribosomal subunit protein uL3 (50S ribosomal
    protein L3) (primary bucket kegg:ppu03010)

    - rplD: PP_0455 | Q88QN4 | Large ribosomal subunit protein uL4 (50S ribosomal
    protein L4) (primary bucket kegg:ppu03010)

    - rplW: PP_0456 | Q88QN3 | Large ribosomal subunit protein uL23 (50S ribosomal
    protein L23) (primary bucket kegg:ppu03010)

    - rplB: PP_0457 | Q88QN2 | Large ribosomal subunit protein uL2 (50S ribosomal
    protein L2) (primary bucket kegg:ppu03010)

    - rpsS: PP_0458 | Q88QN1 | Small ribosomal subunit protein uS19 (30S ribosomal
    protein S19) (primary bucket kegg:ppu03010)

    - rplV: PP_0459 | Q88QN0 | Large ribosomal subunit protein uL22 (50S ribosomal
    protein L22) (primary bucket kegg:ppu03010)

    - rpsC: PP_0460 | Q88QM9 | Small ribosomal subunit protein uS3 (30S ribosomal
    protein S3) (primary bucket kegg:ppu03010)

    - rplP: PP_0461 | Q88QM8 | Large ribosomal subunit protein uL16 (50S ribosomal
    protein L16) (primary bucket kegg:ppu03010)

    - rpmC: PP_0462 | Q88QM7 | Large ribosomal subunit protein uL29 (50S ribosomal
    protein L29) (primary bucket kegg:ppu03010)

    - rpsQ: PP_0463 | Q88QM6 | Small ribosomal subunit protein uS17 (30S ribosomal
    protein S17) (primary bucket kegg:ppu03010)

    - rplN: PP_0464 | Q88QM5 | Large ribosomal subunit protein uL14 (50S ribosomal
    protein L14) (primary bucket kegg:ppu03010)

    - rplX: PP_0465 | Q88QM4 | Large ribosomal subunit protein uL24 (50S ribosomal
    protein L24) (primary bucket kegg:ppu03010)

    - rplE: PP_0466 | Q88QM3 | Large ribosomal subunit protein uL5 (50S ribosomal
    protein L5) (primary bucket kegg:ppu03010)

    - rpsN: PP_0467 | Q88QM2 | Small ribosomal subunit protein uS14 (30S ribosomal
    protein S14) (primary bucket kegg:ppu03010)

    - rpsH: PP_0468 | Q88QM1 | Small ribosomal subunit protein uS8 (30S ribosomal
    protein S8) (primary bucket kegg:ppu03010)

    - rplF: PP_0469 | Q88QM0 | Large ribosomal subunit protein uL6 (50S ribosomal
    protein L6) (primary bucket kegg:ppu03010)

    - rplR: PP_0470 | Q88QL9 | Large ribosomal subunit protein uL18 (50S ribosomal
    protein L18) (primary bucket kegg:ppu03010)

    - rpsE: PP_0471 | Q88QL8 | Small ribosomal subunit protein uS5 (30S ribosomal
    protein S5) (primary bucket kegg:ppu03010)

    - rpmD: PP_0472 | Q88QL7 | Large ribosomal subunit protein uL30 (50S ribosomal
    protein L30) (primary bucket kegg:ppu03010)

    - rplO: PP_0473 | Q88QL6 | Large ribosomal subunit protein uL15 (50S ribosomal
    protein L15) (primary bucket kegg:ppu03010)

    - rpmJ: PP_0475 | P61113 | Large ribosomal subunit protein bL36 (50S ribosomal
    protein L36) (primary bucket kegg:ppu03010)

    - rpsM: PP_0476 | Q88QL3 | Small ribosomal subunit protein uS13 (30S ribosomal
    protein S13) (primary bucket kegg:ppu03010)

    - rpsK: PP_0477 | P59374 | Small ribosomal subunit protein uS11 (30S ribosomal
    protein S11) (primary bucket kegg:ppu03010)

    - rpsD: PP_0478 | Q88QL2 | Small ribosomal subunit protein uS4 (30S ribosomal
    protein S4) (primary bucket kegg:ppu03010)

    - rplQ: PP_0480 | Q88QL0 | Large ribosomal subunit protein bL17 (50S ribosomal
    protein L17) (primary bucket kegg:ppu03010)

    - rpsT: PP_0600 | Q88Q95 | Small ribosomal subunit protein bS20 (30S ribosomal
    protein S20) (primary bucket kegg:ppu03010)

    - rplU: PP_0688 | Q88Q10 | Large ribosomal subunit protein bL21 (50S ribosomal
    protein L21) (primary bucket kegg:ppu03010)

    - rpmA: PP_0689 | Q88Q09 | Large ribosomal subunit protein bL27 (50S ribosomal
    protein L27) (primary bucket kegg:ppu03010)

    - rplY: PP_0721 | Q88PX7 | Large ribosomal subunit protein bL25 (50S ribosomal
    protein L25) (General stress protein CTC) (primary bucket kegg:ppu03010)

    - rplM: PP_1315 | Q88N97 | Large ribosomal subunit protein uL13 (50S ribosomal
    protein L13) (primary bucket kegg:ppu03010)

    - rpsI: PP_1316 | Q88N96 | Small ribosomal subunit protein uS9 (30S ribosomal
    protein S9) (primary bucket kegg:ppu03010)

    - rpsP: PP_1462 | Q88MV6 | Small ribosomal subunit protein bS16 (30S ribosomal
    protein S16) (primary bucket kegg:ppu03010)

    - rplS: PP_1465 | Q88MV3 | Large ribosomal subunit protein bL19 (50S ribosomal
    protein L19) (primary bucket kegg:ppu03010)

    - rpsB: PP_1591 | Q88MI0 | Small ribosomal subunit protein uS2 (30S ribosomal
    protein S2) (primary bucket kegg:ppu03010)

    - rpsA: PP_1772 | Q88M03 | 30S ribosomal protein S1 (primary bucket kegg:ppu03010)

    - rpmF: PP_1911 | Q88LL9 | Large ribosomal subunit protein bL32 (50S ribosomal
    protein L32) (primary bucket kegg:ppu03010)

    - rpmI: PP_2467 | Q88K25 | Large ribosomal subunit protein bL35 (50S ribosomal
    protein L35) (primary bucket kegg:ppu03010)

    - rplT: PP_2468 | Q88K24 | Large ribosomal subunit protein bL20 (50S ribosomal
    protein L20) (primary bucket kegg:ppu03010)

    - rpsO: PP_4709 | Q88DV9 | Small ribosomal subunit protein uS15 (30S ribosomal
    protein S15) (primary bucket kegg:ppu03010)

    - rplI: PP_4874 | Q88DF1 | Large ribosomal subunit protein bL9 (50S ribosomal
    protein L9) (primary bucket kegg:ppu03010)

    - rpsR: PP_4876 | Q88DE9 | Small ribosomal subunit protein bS18 (30S ribosomal
    protein S18) (primary bucket kegg:ppu03010)

    - rpsF: PP_4877 | Q88DE8 | Small ribosomal subunit protein bS6 (30S ribosomal
    protein S6) (primary bucket kegg:ppu03010)

    - rpmE: PP_5087 | Q88CU3 | Large ribosomal subunit protein bL31 (50S ribosomal
    protein L31) (primary bucket kegg:ppu03010)

    - rpmG: PP_5281 | Q88CA0 | Large ribosomal subunit protein bL33 (50S ribosomal
    protein L33) (primary bucket kegg:ppu03010)

    - rpmB: PP_5282 | Q88C99 | Large ribosomal subunit protein bL28 (50S ribosomal
    protein L28) (primary bucket kegg:ppu03010)'
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
  path: PSEPK__bacterial_translation_initiation__ppu03010-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_translation_initiation__ppu03010-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial translation initiation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03010
- Resolved ID: ppu03010
- Resolved name: Ribosome
- Source: KEGG

Resolved local bucket kegg:ppu03010 with 54 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 54

- rpmH: PP_0009 | P0A161 | Large ribosomal subunit protein bL34 (50S ribosomal protein L34) (primary bucket kegg:ppu03010)
- rpsU: PP_0389 | P0A165 | Small ribosomal subunit protein bS21 (30S ribosomal protein S21) (primary bucket kegg:ppu03010)
- rplK: PP_0443 | Q88QP5 | Large ribosomal subunit protein uL11 (50S ribosomal protein L11) (primary bucket kegg:ppu03010)
- rplA: PP_0444 | Q88QP4 | Large ribosomal subunit protein uL1 (50S ribosomal protein L1) (primary bucket kegg:ppu03010)
- rplJ: PP_0445 | Q88QP3 | Large ribosomal subunit protein uL10 (50S ribosomal protein L10) (primary bucket kegg:ppu03010)
- rplL: PP_0446 | P0A157 | Large ribosomal subunit protein bL12 (50S ribosomal protein L7/L12) (primary bucket kegg:ppu03010)
- rpsL: PP_0449 | Q88QP0 | Small ribosomal subunit protein uS12 (30S ribosomal protein S12) (primary bucket kegg:ppu03010)
- rpsG: PP_0450 | Q88QN9 | Small ribosomal subunit protein uS7 (30S ribosomal protein S7) (primary bucket kegg:ppu03010)
- rpsJ: PP_0453 | Q88QN6 | Small ribosomal subunit protein uS10 (30S ribosomal protein S10) (primary bucket kegg:ppu03010)
- rplC: PP_0454 | Q88QN5 | Large ribosomal subunit protein uL3 (50S ribosomal protein L3) (primary bucket kegg:ppu03010)
- rplD: PP_0455 | Q88QN4 | Large ribosomal subunit protein uL4 (50S ribosomal protein L4) (primary bucket kegg:ppu03010)
- rplW: PP_0456 | Q88QN3 | Large ribosomal subunit protein uL23 (50S ribosomal protein L23) (primary bucket kegg:ppu03010)
- rplB: PP_0457 | Q88QN2 | Large ribosomal subunit protein uL2 (50S ribosomal protein L2) (primary bucket kegg:ppu03010)
- rpsS: PP_0458 | Q88QN1 | Small ribosomal subunit protein uS19 (30S ribosomal protein S19) (primary bucket kegg:ppu03010)
- rplV: PP_0459 | Q88QN0 | Large ribosomal subunit protein uL22 (50S ribosomal protein L22) (primary bucket kegg:ppu03010)
- rpsC: PP_0460 | Q88QM9 | Small ribosomal subunit protein uS3 (30S ribosomal protein S3) (primary bucket kegg:ppu03010)
- rplP: PP_0461 | Q88QM8 | Large ribosomal subunit protein uL16 (50S ribosomal protein L16) (primary bucket kegg:ppu03010)
- rpmC: PP_0462 | Q88QM7 | Large ribosomal subunit protein uL29 (50S ribosomal protein L29) (primary bucket kegg:ppu03010)
- rpsQ: PP_0463 | Q88QM6 | Small ribosomal subunit protein uS17 (30S ribosomal protein S17) (primary bucket kegg:ppu03010)
- rplN: PP_0464 | Q88QM5 | Large ribosomal subunit protein uL14 (50S ribosomal protein L14) (primary bucket kegg:ppu03010)
- rplX: PP_0465 | Q88QM4 | Large ribosomal subunit protein uL24 (50S ribosomal protein L24) (primary bucket kegg:ppu03010)
- rplE: PP_0466 | Q88QM3 | Large ribosomal subunit protein uL5 (50S ribosomal protein L5) (primary bucket kegg:ppu03010)
- rpsN: PP_0467 | Q88QM2 | Small ribosomal subunit protein uS14 (30S ribosomal protein S14) (primary bucket kegg:ppu03010)
- rpsH: PP_0468 | Q88QM1 | Small ribosomal subunit protein uS8 (30S ribosomal protein S8) (primary bucket kegg:ppu03010)
- rplF: PP_0469 | Q88QM0 | Large ribosomal subunit protein uL6 (50S ribosomal protein L6) (primary bucket kegg:ppu03010)
- rplR: PP_0470 | Q88QL9 | Large ribosomal subunit protein uL18 (50S ribosomal protein L18) (primary bucket kegg:ppu03010)
- rpsE: PP_0471 | Q88QL8 | Small ribosomal subunit protein uS5 (30S ribosomal protein S5) (primary bucket kegg:ppu03010)
- rpmD: PP_0472 | Q88QL7 | Large ribosomal subunit protein uL30 (50S ribosomal protein L30) (primary bucket kegg:ppu03010)
- rplO: PP_0473 | Q88QL6 | Large ribosomal subunit protein uL15 (50S ribosomal protein L15) (primary bucket kegg:ppu03010)
- rpmJ: PP_0475 | P61113 | Large ribosomal subunit protein bL36 (50S ribosomal protein L36) (primary bucket kegg:ppu03010)
- rpsM: PP_0476 | Q88QL3 | Small ribosomal subunit protein uS13 (30S ribosomal protein S13) (primary bucket kegg:ppu03010)
- rpsK: PP_0477 | P59374 | Small ribosomal subunit protein uS11 (30S ribosomal protein S11) (primary bucket kegg:ppu03010)
- rpsD: PP_0478 | Q88QL2 | Small ribosomal subunit protein uS4 (30S ribosomal protein S4) (primary bucket kegg:ppu03010)
- rplQ: PP_0480 | Q88QL0 | Large ribosomal subunit protein bL17 (50S ribosomal protein L17) (primary bucket kegg:ppu03010)
- rpsT: PP_0600 | Q88Q95 | Small ribosomal subunit protein bS20 (30S ribosomal protein S20) (primary bucket kegg:ppu03010)
- rplU: PP_0688 | Q88Q10 | Large ribosomal subunit protein bL21 (50S ribosomal protein L21) (primary bucket kegg:ppu03010)
- rpmA: PP_0689 | Q88Q09 | Large ribosomal subunit protein bL27 (50S ribosomal protein L27) (primary bucket kegg:ppu03010)
- rplY: PP_0721 | Q88PX7 | Large ribosomal subunit protein bL25 (50S ribosomal protein L25) (General stress protein CTC) (primary bucket kegg:ppu03010)
- rplM: PP_1315 | Q88N97 | Large ribosomal subunit protein uL13 (50S ribosomal protein L13) (primary bucket kegg:ppu03010)
- rpsI: PP_1316 | Q88N96 | Small ribosomal subunit protein uS9 (30S ribosomal protein S9) (primary bucket kegg:ppu03010)
- rpsP: PP_1462 | Q88MV6 | Small ribosomal subunit protein bS16 (30S ribosomal protein S16) (primary bucket kegg:ppu03010)
- rplS: PP_1465 | Q88MV3 | Large ribosomal subunit protein bL19 (50S ribosomal protein L19) (primary bucket kegg:ppu03010)
- rpsB: PP_1591 | Q88MI0 | Small ribosomal subunit protein uS2 (30S ribosomal protein S2) (primary bucket kegg:ppu03010)
- rpsA: PP_1772 | Q88M03 | 30S ribosomal protein S1 (primary bucket kegg:ppu03010)
- rpmF: PP_1911 | Q88LL9 | Large ribosomal subunit protein bL32 (50S ribosomal protein L32) (primary bucket kegg:ppu03010)
- rpmI: PP_2467 | Q88K25 | Large ribosomal subunit protein bL35 (50S ribosomal protein L35) (primary bucket kegg:ppu03010)
- rplT: PP_2468 | Q88K24 | Large ribosomal subunit protein bL20 (50S ribosomal protein L20) (primary bucket kegg:ppu03010)
- rpsO: PP_4709 | Q88DV9 | Small ribosomal subunit protein uS15 (30S ribosomal protein S15) (primary bucket kegg:ppu03010)
- rplI: PP_4874 | Q88DF1 | Large ribosomal subunit protein bL9 (50S ribosomal protein L9) (primary bucket kegg:ppu03010)
- rpsR: PP_4876 | Q88DE9 | Small ribosomal subunit protein bS18 (30S ribosomal protein S18) (primary bucket kegg:ppu03010)
- rpsF: PP_4877 | Q88DE8 | Small ribosomal subunit protein bS6 (30S ribosomal protein S6) (primary bucket kegg:ppu03010)
- rpmE: PP_5087 | Q88CU3 | Large ribosomal subunit protein bL31 (50S ribosomal protein L31) (primary bucket kegg:ppu03010)
- rpmG: PP_5281 | Q88CA0 | Large ribosomal subunit protein bL33 (50S ribosomal protein L33) (primary bucket kegg:ppu03010)
- rpmB: PP_5282 | Q88C99 | Large ribosomal subunit protein bL28 (50S ribosomal protein L28) (primary bucket kegg:ppu03010)

## Generic Module Context

### Working Scope

A reusable bacterial module for assembly of a translation-competent 70S initiation complex. IF2 and IF3 associate with the 30S subunit early, IF1 stabilizes their binding and organizes the preinitiation complex, and IF2 promotes initiator fMet-tRNA accommodation and 50S joining while hydrolyzing GTP. The boundary ends with factor release and formation of the mature 70S initiation complex. Ribosome biogenesis, initiator-tRNA aminoacylation and formylation, elongation, and termination are excluded. RRF/EF-G-driven recycling is outside the module, but IF3 stabilization of newly split 30S subunits is retained as the recycling-to-initiation interface.

### Provisional Biological Outline

- Bacterial translation initiation
  - 1. early 30S initiation-factor loading and subunit availability
  - Early IF2 and IF3 loading on the 30S subunit
    - IF2 early 30S initiation role (molecular player: translation initiation factor IF2-related family; activity or role: translation initiation factor activity)
    - IF3 free-30S maintenance role (molecular player: translation initiation factor IF3 family; activity or role: translation initiation factor activity)
  - 2. IF1-stabilized preinitiation-complex assembly
  - IF1 stabilization of the 30S preinitiation complex
    - IF1 initiation-factor activity (molecular player: translation initiation factor IF1 family; activity or role: translation initiation factor activity)
  - 3. initiator-tRNA accommodation and large-subunit joining
  - IF2-dependent initiator-tRNA accommodation and 50S joining
    - IF2 GTPase activity during 70S-complex formation (molecular player: translation initiation factor IF2-related family; activity or role: GTPase activity)

### Known Relationships Among Steps

- Early IF2 and IF3 loading on the 30S subunit precedes IF1 stabilization of the 30S preinitiation complex: Real-time kinetic measurements support IF2/IF3 arrival before IF1 as a favored Escherichia coli assembly route; this edge does not require a strict universal sequence in every bacterium or condition.
- IF1 stabilization of the 30S preinitiation complex precedes IF2-dependent initiator-tRNA accommodation and 50S joining: IF1-stabilized preinitiation assembly precedes IF2-dependent GTP hydrolysis, 50S joining, and factor release.

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

# Species-Aware Module Review: Bacterial Translation Initiation in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Nominal bucket:** KEGG `ppu03010` "Ribosome" (54 candidate genes)
**Module under review:** Bacterial translation initiation (assembly of a translation-competent 70S initiation complex)
**Date:** 2026-09-01

---

## 1. Executive summary

- The **module is satisfiable** in *P. putida* KT2440. All three canonical initiation factors are encoded as single-copy genes with reviewed SwissProt entries: **IF-1 `infA` = PP_4007** (P65117), **IF-2 `infB` = PP_4712** (Q88DV7), **IF-3 `infC` = PP_2466** (Q88K26).
- **Critical curation finding — bucket/module mismatch.** The resolved candidate bucket `kegg:ppu03010` "Ribosome" contains **only ribosomal proteins** (rps*/rpl*/rpm*) and **none of the three initiation factors**. KEGG map ppu03010 by definition enumerates the r-protein/rRNA parts of the 30S/50S subunits; the soluble initiation factors live in KEGG BRITE **ko03012 "Translation factors"** (≈ GO:0006413 *translation initiation*). The 54 candidate genes therefore describe the **ribosomal substrate / assembly platform**, not the module's active molecular players.
- Consequently **every module step maps to a real KT2440 gene, but those genes are outside the supplied candidate list.** Curation must pull IF genes from the translation-factor bucket, not from ppu03010.
- Evidence for the KT2440 IF genes is **UniProt homology transfer** (proteinExistence "Inferred from homology", annotation score 2.0), not direct in-species biochemistry. Assignments are nevertheless high-confidence because of sequence conservation, single-copy status, and conserved operon context (`thrS–infC–rpmI–rplT`, with rpmI = PP_2467 and rplT = PP_2468 already in the candidate list).
- Recommended module dispositions: **all three initiation steps → `covered`**, but flagged as `covered_offbucket` (genes not in ppu03010); the ppu03010 bucket itself → `module_needs_revision` for this module (wrong bucket, right organism).

---

## 2. Target-organism pathway definition

**In-scope biochemistry (this module).** Assembly of the bacterial 70S initiation complex: early loading of IF2 and IF3 onto the 30S subunit; IF1-stabilized 30S pre-initiation complex (PIC); IF2-driven accommodation of initiator fMet-tRNA^fMet and 50S joining with GTP hydrolysis; and factor release yielding the mature 70S initiation complex. IF3's maintenance of free/newly-split 30S subunits is retained as the recycling→initiation interface.

**Explicitly excluded (keep as separate buckets/maps):**
- **Ribosome biogenesis / structure** — the 54 ppu03010 r-proteins belong here (KEGG ppu03010, GO:0042254 assembly / GO:0005840 ribosome). They are the *platform*, not the initiation machinery.
- **Initiator-tRNA charging and formylation** — methionyl-tRNA synthetase (`metG`) and methionyl-tRNA formyltransferase **`fmt` = PP_0067** (Q88RR2). fmt is present in KT2440 but is a boundary/excluded step.
- **Elongation** — EF-Tu (`tufA` PP_0440 / `tufB` PP_0452), EF-Ts (`tsf` PP_1592), EF-G (`fusA` PP_0451 / `fusB` PP_4111).
- **Ribosome recycling** — RRF (`frr` = PP_1594, Q88MH7) + EF-G; outside the module except via the IF3 interface above.

**Alternate names / database definitions.** IF1/IF2/IF3 = gene symbols `infA`/`infB`/`infC`. KEGG orthologs: K02518 (infA), K02519 (infB), K02520 (infC). KEGG BRITE ko03012 "Translation factors" is the correct grouping; the "Ribosome" pathway map (ko03010 / ppu03010) is a distinct, non-overlapping definition.

---

## 3. Expected step model (generic module → KT2440 assignment)

| # | Generic module step | Molecular player | KT2440 gene | Disposition |
|---|---|---|---|---|
| 1 | Early IF2/IF3 loading; free-30S maintenance | IF2 (early role), IF3 | `infB` PP_4712; `infC` PP_2466 | **covered** (off-bucket) |
| 2 | IF1-stabilized 30S pre-initiation complex | IF1 | `infA` PP_4007 | **covered** (off-bucket) |
| 3 | fMet-tRNA accommodation + 50S joining + GTP hydrolysis; factor release | IF2 (GTPase) | `infB` PP_4712 | **covered** (off-bucket) |
| — | Initiator-tRNA formylation (boundary, excluded) | Fmt | `fmt` PP_0067 | not_in_module (present) |
| — | Recycling→initiation interface | IF3 (retained) / RRF (excluded) | `infC` PP_2466 / `frr` PP_1594 | interface covered by IF3 |

Known step order (IF2/IF3 → IF1 → IF2-GTPase/50S joining) is derived from *E. coli* real-time kinetics (Milón et al. 2012, PMID 22562136) and recent cryo-EM/fast-kinetics (Guerra et al. 2026, PMID 42427554). These are **not** KT2440 measurements; transfer to KT2440 is **strong** at the level of factor identity/role (deep conservation of IF1/IF2/IF3), but the precise assembly *sequence* should be treated as a favored *E. coli* route, not a proven KT2440 mechanism.

---

## 4. Candidate genes and evidence

### 4a. The module's true genes (NOT in the ppu03010 candidate list — must be added)

| Gene | Locus | UniProt | Len | Evidence | Role | Caveats |
|---|---|---|---|---|---|---|
| `infA` (IF-1) | PP_4007 | P65117 (reviewed) | 72 aa | Homology-inferred; SwissProt | Stabilizes IF-2/IF-3 on 30S, forms 30S PIC (step 2) | Small protein; single copy; no in-species assay |
| `infB` (IF-2) | PP_4712 | Q88DV7 (reviewed) | 846 aa | Homology-inferred; SwissProt; GTP-binding KW | Protects fMet-tRNA, promotes 30S binding + GTP hydrolysis for 70S (steps 1 & 3) | *E. coli* IF2 makes N-terminally truncated isoforms from internal starts — check for the same in KT2440 if isoform-level curation matters |
| `infC` (IF-3) | PP_2466 | Q88K26 (reviewed) | 183 aa | Homology-inferred; SwissProt; operon context | Free-30S maintenance / anti-association (step 1 + recycling interface) | May use non-AUG (AUU/AUG) autoregulatory start as in *E. coli* — verify start codon during fetch-gene review |

### 4b. Candidate list (ppu03010) — role in this module

The 54 supplied genes are the **30S** (uS2–uS21, bS16/bS18/bS20/bS21, S1) and **50S** (uL1–uL30, bL9/bL17/…/bL36) ribosomal proteins. For the initiation module they are **context, not players**: they constitute the 30S and 50S subunits onto/into which the factors act. High-confidence, unambiguous r-protein annotations (standard bacterial nomenclature, one gene per protein). They should be marked as belonging to the **ribosome-structure module**, and used here only to confirm that both subunits are fully encoded (they are), so 30S availability and 50S joining are structurally possible.

Note two candidate loci provide operon evidence for the true module gene: **rpmI (PP_2467)** and **rplT (PP_2468)** are the downstream members of the `thrS–infC–rpmI–rplT` cluster, placing `infC` (PP_2466) immediately adjacent — independent support for the IF-3 assignment.

### 4c. Operon / synteny evidence (verified from KT2440 genome neighbors)

Gene-neighborhood context (UniProt loci) independently corroborates all three assignments and raises confidence beyond pure homology:

| IF gene | Locus | Conserved operon context in KT2440 | Note |
|---|---|---|---|
| `infC` (IF-3) | PP_2466 | `thrS`(PP_2465)–**`infC`**–`rpmI`(PP_2467)–`rplT`(PP_2468)–`pheS`(PP_2469) | Classic `thrS-infC-rpmI-rplT`; rpmI/rplT are candidate-list genes |
| `infB` (IF-2) | PP_4712 | `pnp`(4708)–`rpsO`(4709)–`truB`(4710)–`rbfA`(4711)–**`infB`**–`nusA`(4713)–`rimP`(4714) | Classic `rbfA-infB-nusA` / metY-nusA-infB macro-operon; rpsO is a candidate-list gene |
| `infA` (IF-1) | PP_4007 | `aat`(4005)–`bpt`(4006)–**`infA`**–`clpA`(4008)–`clpS`(4009) | Standalone, as in *E. coli* (not in an r-protein operon) |

Two candidate ppu03010 ribosomal genes physically flank two of the three module genes (**rpsO** next to infB; **rpmI/rplT** next to infC), so the wrong-bucket candidate list is nonetheless syntenically linked to the correct module genes — a useful curation cross-check.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No gap in factor content.** IF1/IF2/IF3 all present, single-copy; no missing step.
- **Paralog ambiguity:** none for the IFs. (By contrast, elongation factors EF-Tu and EF-G *are* duplicated in KT2440 — tufA/tufB, fusA/fusB — but those are outside this module.)
- **Bucket-level over-scoping, not gene over-propagation.** The main annotation issue is that the *module was pointed at the wrong KEGG bucket*. There is no evidence of over-propagated IF annotation; the r-proteins are correctly r-proteins.
- **Loose "initiation factor" names to exclude (curation traps).** A proteome name/GO scan surfaces non-canonical hits that must NOT be pulled into the module:
  - **PP_4196** (Q88FA2, "Translation initiation factor 2", 144 aa, *Predicted*) — far too short for real IF-2 (846 aa); over-propagated/loose name. **Exclude.**
  - **PP_5605** (A0A140FWF6, "Secretion system X translation initiation factor", 168 aa, *Predicted*) — name tied to a secretion system; spurious for this module. **Exclude.**
  - **PP_0566 `yciH`** (Q88QC8, 123 aa, SUI1/eIF1-like domain, carries GO:0003743) — a genuine translation-*associated* SUI1-family protein, but **not** one of the canonical IF1/IF2/IF3; note as auxiliary only, do not use to satisfy any core step.
  Only PP_4007/PP_4712/PP_2466 should populate the module.
- **Evidence-quality caveat:** all three IF entries are homology-inferred (no direct KT2440 experiment). Genome-wide screens (Molina-Henares et al. 2010, PMID 20158506) did not report IF knockouts — consistent with IF1/IF2/IF3 being essential (non-recoverable), but this is inference, not a positive KT2440 result.
- **fMet-tRNA and metZ/metW tRNA genes** are not protein-coding candidates and won't appear in a proteome bucket; if the module requires the initiator tRNA as a component, that must be sourced from tRNA annotation, not KEGG proteome buckets.

---

## 6. Module and GO-curation recommendations

1. **Reassign the bucket.** For "bacterial translation initiation," resolve to KEGG BRITE **ko03012 (translation factors)** / GO:0006413, not KEGG pathway map **ppu03010 (ribosome)**. Mark `kegg:ppu03010` as `module_needs_revision` *for this module* (correct organism, wrong bucket); keep ppu03010 as the bucket for a separate **ribosome-structure** module.
2. **Step dispositions:** Step 1 (IF2/IF3 loading) = **covered**; Step 2 (IF1 PIC) = **covered**; Step 3 (IF2 GTPase / 50S joining) = **covered**. Tag all as `covered_offbucket` because the supporting genes (PP_4007, PP_4712, PP_2466) are not in the supplied candidate set.
3. **Add genes to the module:** PP_4007 (infA), PP_4712 (infB), PP_2466 (infC). Optionally record boundary genes PP_0067 (fmt) and PP_1594 (frr) as `excluded/adjacent`.
4. **GO term requests:** none new required — GO:0003743 (translation initiation factor activity), GO:0006413 (translational initiation), GO:0003924 (GTPase activity, for IF2) already cover the module. Ensure PP_4712 carries GO:0003924 / GTP-binding.
5. **Module boundary check:** the generic boundaries (excluding elongation, termination, biogenesis, aminoacylation/formylation, RRF/EF-G recycling but retaining IF3 free-30S maintenance) are appropriate for KT2440 — no organism-specific boundary revision needed.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_4712 `infB` (IF-2)** — highest priority: multidomain GTPase, module's catalytic hub; confirm GTPase motifs, GTP-binding annotation, and whether KT2440 produces IF2 isoforms (internal start sites) as in *E. coli*.
2. **PP_2466 `infC` (IF-3)** — verify start codon (possible non-AUG autoregulatory start) and operon `thrS–infC–rpmI–rplT`; central to the recycling→initiation interface.
3. **PP_4007 `infA` (IF-1)** — short protein; confirm annotation and (in)essentiality; low complexity but mechanistically required for step 2.

(Ribosomal-protein candidates do not need promotion for *this* module; they belong to the ribosome-structure module review.)

---

## 8. Key references

- Milón P, Maracci C, Filonava L, Gualerzi CO, Rodnina MV. **Real-time assembly landscape of bacterial 30S translation initiation complex.** *Nat Struct Mol Biol* 2012. PMID **22562136**. — Establishes IF3/IF2-first, then IF1-locking assembly order (E. coli).
- Guerra J, et al. (Demo lab). **Molecular mechanism of IF1- and IF2-driven translation initiation in bacteria.** 2026. PMID **42427554**. — Cryo-EM/fast-kinetics of IF1/IF2 roles, GTP hydrolysis, Pi release, factor departure.
- Molina-Henares MA, et al. **Identification of conditionally essential genes for growth of *Pseudomonas putida* KT2440… genome-wide mutant library.** *Environ Microbiol* 2010. PMID **20158506**. — KT2440 mini-Tn5 knockout screen; IFs not recovered (consistent with essentiality).
- UniProtKB reviewed entries (taxon 160488): P65117 (IF1/PP_4007), Q88DV7 (IF2/PP_4712), Q88K26 (IF3/PP_2466), Q88RR2 (Fmt/PP_0067), Q88MH7 (RRF/PP_1594).

---

### Evidence-transfer summary

| Claim | Basis | Transfer strength to KT2440 |
|---|---|---|
| IF1/IF2/IF3 present & single-copy in KT2440 | UniProt reviewed, genome | **Direct** (in-species sequence) |
| IF functional roles per step | UniProt homology from *E. coli* | **Strong** (deep conservation) |
| IF gene identity correct (not mis-annotation) | UniProt homology **+ conserved operon synteny** (thrS-infC-rpmI-rplT; rbfA-infB-nusA) | **Strong** (sequence + genomic context) |
| Assembly *sequence* (IF2/3→IF1→GTPase) | *E. coli* kinetics/cryo-EM | **Moderate** (mechanism not tested in KT2440) |
| IF essentiality in KT2440 | Absence from Tn screen recoverables | **Weak/indirect** |


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_translation_initiation__ppu03010-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_translation_initiation__ppu03010-deep-research-openscientist_artifacts/final_report.pdf)