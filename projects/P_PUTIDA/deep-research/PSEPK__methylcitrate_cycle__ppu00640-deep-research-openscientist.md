---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T06:51:29.725494'
end_time: '2026-07-23T07:15:14.084578'
duration_seconds: 1424.36
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: 2-methylcitrate cycle
  module_summary: A reusable propionate-assimilation module that activates propionate
    to propionyl-CoA, condenses propionyl-CoA with oxaloacetate to form 2-methylcitrate,
    converts 2-methylcitrate to 2-methylisocitrate through alternative dehydration/isomerization
    implementations, and cleaves 2-methylisocitrate to succinate and pyruvate. The
    module distinguishes the direct PrpD route from the two-component AcnD/PrpF route
    and represents the common aconitase-family hydration step separately.
  module_outline: "- 2-methylcitrate cycle\n  - 1. propionate activation\n  - Propionate\
    \ activation to propionyl-CoA\n    - Propionate-CoA ligase (molecular player:\
    \ PSEPK canonical PrpE; activity or role: propionate-CoA ligase activity)\n  -\
    \ 2. 2-methylcitrate formation\n  - 2-methylcitrate synthesis\n    - 2-methylcitrate\
    \ synthase (molecular player: PSEPK canonical PrpC; activity or role: 2-methylcitrate\
    \ synthase activity)\n  - 3. 2-methyl-cis-aconitate generation\n  - Conversion\
    \ of 2-methylcitrate to 2-methyl-cis-aconitate\n    - Alternative versions by\
    \ reaction mechanism: 2-methylcitrate dehydration implementations\n      - Direct\
    \ PrpD route\n        - PrpD 2-methylcitrate dehydratase (molecular player: PSEPK\
    \ PrpD; activity or role: 2-methylcitrate dehydratase activity)\n      - Two-component\
    \ AcnD/PrpF route\n        - 1. AcnD-dependent dehydration\n        - AcnD-family\
    \ 2-methylcitrate dehydration\n          - AcnD-family pathway dehydratase (molecular\
    \ player: PSEPK AcnA-II/AcnD candidate)\n        - 2. methylaconitate isomerization\n\
    \        - PrpF methylaconitate isomerization\n          - PrpF aconitate isomerase\
    \ (molecular player: PSEPK PrpF)\n  - 4. 2-methylisocitrate formation\n  - 2-methyl-cis-aconitate\
    \ hydration\n    - Aconitase-family 2-methylisocitrate hydratase (molecular player:\
    \ PSEPK canonical AcnB; activity or role: 2-methylisocitrate dehydratase activity)\n\
    \  - 5. carbon-carbon cleavage\n  - 2-methylisocitrate cleavage\n    - 2-methylisocitrate\
    \ lyase (molecular player: PSEPK canonical PrpB; activity or role: methylisocitrate\
    \ lyase activity)"
  module_connections: '- Propionate activation to propionyl-CoA feeds into 2-methylcitrate
    synthesis: Propionyl-CoA is the acyl donor for 2-methylcitrate synthesis.

    - 2-methylcitrate synthesis feeds into Conversion of 2-methylcitrate to 2-methyl-cis-aconitate:
    2-methylcitrate enters either dehydration implementation.

    - Conversion of 2-methylcitrate to 2-methyl-cis-aconitate feeds into 2-methyl-cis-aconitate
    hydration: Both alternatives converge on 2-methyl-cis-aconitate.

    - 2-methyl-cis-aconitate hydration feeds into 2-methylisocitrate cleavage: 2-methylisocitrate
    is the substrate cleaved by PrpB.

    - AcnD-family 2-methylcitrate dehydration feeds into PrpF methylaconitate isomerization:
    The AcnD product is the substrate rearranged by PrpF.'
  pathway_query: ppu00640
  pathway_id: ppu00640
  pathway_name: Propanoate metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00640 with 7 primary genes; module
    area: central_carbon.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '33'
  candidate_genes: '- accC: PP_0558 | Q88QD6 | Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme
    A carboxylase biotin carboxylase subunit A) (EC 6.3.4.14; primary bucket kegg:ppu00061)

    - accB: PP_0559 | Q88QD5 | Biotin carboxyl carrier protein of acetyl-CoA carboxylase
    (primary bucket kegg:ppu00061)

    - PP_0596: PP_0596 | Q88Q98 | Omega-amino acid--pyruvate aminotransferase (EC
    2.6.1.18) (EC 2.6.1.18; primary bucket kegg:ppu00410)

    - mmsA-I: PP_0597 | Q88Q97 | methylmalonate-semialdehyde dehydrogenase (CoA acylating)
    (EC 1.2.1.27) (EC 1.2.1.27; primary bucket kegg:ppu00562)

    - pta: PP_0774 | Q88PS4 | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase)
    (EC 2.3.1.8; primary bucket kegg:ppu00430)

    - accA: PP_1607 | Q88MG4 | Acetyl-coenzyme A carboxylase carboxyl transferase
    subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyltransferase
    subunit alpha) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)

    - accD: PP_1996 | Q88LD9 | Acetyl-coenzyme A carboxylase carboxyl transferase
    subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltransferase
    subunit beta) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)

    - acnA-I: PP_2112 | Q88L24 | Aconitate hydratase (Aconitase) (EC 4.2.1.3) (EC
    4.2.1.3; primary bucket kegg:ppu00020)

    - fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes:
    Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA
    epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase
    (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)

    - PP_2213: PP_2213 | Q88KS6 | Acyl-CoA synthetase (EC 6.2.1.-) (EC 6.2.1.-; primary
    bucket kegg:ppu00680)

    - acd: PP_2216 | Q88KS3 | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC
    3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane-1-carbonyl-CoA
    dehydrogenase) (EC 1.3.8.11; 3.13.1.4; primary bucket kegg:ppu00410)

    - PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - prpB: PP_2334 | Q88KF6 | 2-methylisocitrate lyase (2-MIC) (MICL) (EC 4.1.3.30)
    ((2R,3S)-2-methylisocitrate lyase) (EC 4.1.3.30; primary bucket kegg:ppu00640)

    - prpC: PP_2335 | Q88KF5 | Citrate synthase (primary bucket kegg:ppu00020)

    - acnA-II: PP_2336 | Q88KF4 | aconitate hydratase (EC 4.2.1.3) (EC 4.2.1.3; primary
    bucket kegg:ppu00640)

    - prpF: PP_2337 | Q88KF3 | Aconitate isomerase (primary bucket kegg:ppu00640)

    - prpD: PP_2338 | Q88KF2 | 2-methylcitrate dehydratase (EC 4.2.1.79) (EC 4.2.1.79;
    primary bucket kegg:ppu00640)

    - acnB: PP_2339 | Q88KF1 | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate
    dehydratase) (EC 4.2.1.3; 4.2.1.99; primary bucket kegg:ppu00020)

    - prpE: PP_2351 | Q88KD9 | Propionyl-CoA synthetase (EC 6.2.1.17) (EC 6.2.1.17;
    primary bucket kegg:ppu00640)

    - yqhD: PP_2492 | Q88K01 | Alcohol dehydrogenase, NAD(P)-dependent (EC 1.1.1.1)
    (EC 1.1.1.1; primary bucket kegg:ppu00640)

    - paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - aceA: PP_4116 | Q88FI0 | Isocitrate lyase (EC 4.1.3.1) (EC 4.1.3.1; primary
    bucket kegg:ppu00640)

    - sucD: PP_4185 | Q88FB3 | Succinate--CoA ligase [ADP-forming] subunit alpha (EC
    6.2.1.5) (Succinyl-CoA synthetase subunit alpha) (SCS-alpha) (EC 6.2.1.5; primary
    bucket kegg:ppu00660)

    - sucC: PP_4186 | Q88FB2 | Succinate--CoA ligase [ADP-forming] subunit beta (EC
    6.2.1.5) (Succinyl-CoA synthetase subunit beta) (SCS-beta) (EC 6.2.1.5; primary
    bucket kegg:ppu00660)

    - lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - bkdAA: PP_4401 | Q88EQ2 | 2-oxoisovalerate dehydrogenase subunit alpha (EC 1.2.4.4)
    (Branched-chain alpha-keto acid dehydrogenase E1 component alpha chain) (EC 1.2.4.4;
    primary bucket kegg:ppu00785)

    - bkdAB: PP_4402 | Q88EQ1 | 2-oxoisovalerate dehydrogenase subunit beta (EC 1.2.4.4)
    (Branched-chain alpha-keto acid dehydrogenase E1 component beta chain) (EC 1.2.4.4;
    primary bucket kegg:ppu00785)

    - bkdB: PP_4403 | Q88EQ0 | Dihydrolipoamide acetyltransferase component of pyruvate
    dehydrogenase complex (EC 2.3.1.-) (EC 2.3.1.-; primary bucket kegg:ppu00785)

    - lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)

    - acsA1: PP_4487 | Q88EH6 | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1)
    (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme 1) (EC 6.2.1.1;
    primary bucket kegg:ppu00680)

    - mmsA-II: PP_4667 | Q88E01 | methylmalonate-semialdehyde dehydrogenase (CoA acylating)
    (EC 1.2.1.27) (EC 1.2.1.27; primary bucket kegg:ppu00562)

    - acsA2: PP_4702 | Q88DW6 | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2)
    (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme 2) (EC 6.2.1.1;
    primary bucket kegg:ppu00680)

    - lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4;
    primary bucket kegg:ppu00785)'
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
  path: PSEPK__methylcitrate_cycle__ppu00640-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__methylcitrate_cycle__ppu00640-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

2-methylcitrate cycle in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00640
- Resolved ID: ppu00640
- Resolved name: Propanoate metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00640 with 7 primary genes; module area: central_carbon.

## Candidate Genes From Local Metadata

Candidate gene count: 33

- accC: PP_0558 | Q88QD6 | Biotin carboxylase (EC 6.3.4.14) (Acetyl-coenzyme A carboxylase biotin carboxylase subunit A) (EC 6.3.4.14; primary bucket kegg:ppu00061)
- accB: PP_0559 | Q88QD5 | Biotin carboxyl carrier protein of acetyl-CoA carboxylase (primary bucket kegg:ppu00061)
- PP_0596: PP_0596 | Q88Q98 | Omega-amino acid--pyruvate aminotransferase (EC 2.6.1.18) (EC 2.6.1.18; primary bucket kegg:ppu00410)
- mmsA-I: PP_0597 | Q88Q97 | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) (EC 1.2.1.27; primary bucket kegg:ppu00562)
- pta: PP_0774 | Q88PS4 | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase) (EC 2.3.1.8; primary bucket kegg:ppu00430)
- accA: PP_1607 | Q88MG4 | Acetyl-coenzyme A carboxylase carboxyl transferase subunit alpha (ACCase subunit alpha) (Acetyl-CoA carboxylase carboxyltransferase subunit alpha) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)
- accD: PP_1996 | Q88LD9 | Acetyl-coenzyme A carboxylase carboxyl transferase subunit beta (ACCase subunit beta) (Acetyl-CoA carboxylase carboxyltransferase subunit beta) (EC 2.1.3.15) (EC 2.1.3.15; primary bucket kegg:ppu00061)
- acnA-I: PP_2112 | Q88L24 | Aconitate hydratase (Aconitase) (EC 4.2.1.3) (EC 4.2.1.3; primary bucket kegg:ppu00020)
- fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)
- PP_2213: PP_2213 | Q88KS6 | Acyl-CoA synthetase (EC 6.2.1.-) (EC 6.2.1.-; primary bucket kegg:ppu00680)
- acd: PP_2216 | Q88KS3 | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane-1-carbonyl-CoA dehydrogenase) (EC 1.3.8.11; 3.13.1.4; primary bucket kegg:ppu00410)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- prpB: PP_2334 | Q88KF6 | 2-methylisocitrate lyase (2-MIC) (MICL) (EC 4.1.3.30) ((2R,3S)-2-methylisocitrate lyase) (EC 4.1.3.30; primary bucket kegg:ppu00640)
- prpC: PP_2335 | Q88KF5 | Citrate synthase (primary bucket kegg:ppu00020)
- acnA-II: PP_2336 | Q88KF4 | aconitate hydratase (EC 4.2.1.3) (EC 4.2.1.3; primary bucket kegg:ppu00640)
- prpF: PP_2337 | Q88KF3 | Aconitate isomerase (primary bucket kegg:ppu00640)
- prpD: PP_2338 | Q88KF2 | 2-methylcitrate dehydratase (EC 4.2.1.79) (EC 4.2.1.79; primary bucket kegg:ppu00640)
- acnB: PP_2339 | Q88KF1 | Aconitate hydratase B (EC 4.2.1.3) (EC 4.2.1.99) (2-methylisocitrate dehydratase) (EC 4.2.1.3; 4.2.1.99; primary bucket kegg:ppu00020)
- prpE: PP_2351 | Q88KD9 | Propionyl-CoA synthetase (EC 6.2.1.17) (EC 6.2.1.17; primary bucket kegg:ppu00640)
- yqhD: PP_2492 | Q88K01 | Alcohol dehydrogenase, NAD(P)-dependent (EC 1.1.1.1) (EC 1.1.1.1; primary bucket kegg:ppu00640)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- aceA: PP_4116 | Q88FI0 | Isocitrate lyase (EC 4.1.3.1) (EC 4.1.3.1; primary bucket kegg:ppu00640)
- sucD: PP_4185 | Q88FB3 | Succinate--CoA ligase [ADP-forming] subunit alpha (EC 6.2.1.5) (Succinyl-CoA synthetase subunit alpha) (SCS-alpha) (EC 6.2.1.5; primary bucket kegg:ppu00660)
- sucC: PP_4186 | Q88FB2 | Succinate--CoA ligase [ADP-forming] subunit beta (EC 6.2.1.5) (Succinyl-CoA synthetase subunit beta) (SCS-beta) (EC 6.2.1.5; primary bucket kegg:ppu00660)
- lpdG: PP_4187 | Q88FB1 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- bkdAA: PP_4401 | Q88EQ2 | 2-oxoisovalerate dehydrogenase subunit alpha (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component alpha chain) (EC 1.2.4.4; primary bucket kegg:ppu00785)
- bkdAB: PP_4402 | Q88EQ1 | 2-oxoisovalerate dehydrogenase subunit beta (EC 1.2.4.4) (Branched-chain alpha-keto acid dehydrogenase E1 component beta chain) (EC 1.2.4.4; primary bucket kegg:ppu00785)
- bkdB: PP_4403 | Q88EQ0 | Dihydrolipoamide acetyltransferase component of pyruvate dehydrogenase complex (EC 2.3.1.-) (EC 2.3.1.-; primary bucket kegg:ppu00785)
- lpdV: PP_4404 | Q88EP9 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)
- acsA1: PP_4487 | Q88EH6 | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme 1) (EC 6.2.1.1; primary bucket kegg:ppu00680)
- mmsA-II: PP_4667 | Q88E01 | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) (EC 1.2.1.27; primary bucket kegg:ppu00562)
- acsA2: PP_4702 | Q88DW6 | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme 2) (EC 6.2.1.1; primary bucket kegg:ppu00680)
- lpd: PP_5366 | Q88C17 | Dihydrolipoyl dehydrogenase (EC 1.8.1.4) (EC 1.8.1.4; primary bucket kegg:ppu00785)

## Generic Module Context

### Working Scope

A reusable propionate-assimilation module that activates propionate to propionyl-CoA, condenses propionyl-CoA with oxaloacetate to form 2-methylcitrate, converts 2-methylcitrate to 2-methylisocitrate through alternative dehydration/isomerization implementations, and cleaves 2-methylisocitrate to succinate and pyruvate. The module distinguishes the direct PrpD route from the two-component AcnD/PrpF route and represents the common aconitase-family hydration step separately.

### Provisional Biological Outline

- 2-methylcitrate cycle
  - 1. propionate activation
  - Propionate activation to propionyl-CoA
    - Propionate-CoA ligase (molecular player: PSEPK canonical PrpE; activity or role: propionate-CoA ligase activity)
  - 2. 2-methylcitrate formation
  - 2-methylcitrate synthesis
    - 2-methylcitrate synthase (molecular player: PSEPK canonical PrpC; activity or role: 2-methylcitrate synthase activity)
  - 3. 2-methyl-cis-aconitate generation
  - Conversion of 2-methylcitrate to 2-methyl-cis-aconitate
    - Alternative versions by reaction mechanism: 2-methylcitrate dehydration implementations
      - Direct PrpD route
        - PrpD 2-methylcitrate dehydratase (molecular player: PSEPK PrpD; activity or role: 2-methylcitrate dehydratase activity)
      - Two-component AcnD/PrpF route
        - 1. AcnD-dependent dehydration
        - AcnD-family 2-methylcitrate dehydration
          - AcnD-family pathway dehydratase (molecular player: PSEPK AcnA-II/AcnD candidate)
        - 2. methylaconitate isomerization
        - PrpF methylaconitate isomerization
          - PrpF aconitate isomerase (molecular player: PSEPK PrpF)
  - 4. 2-methylisocitrate formation
  - 2-methyl-cis-aconitate hydration
    - Aconitase-family 2-methylisocitrate hydratase (molecular player: PSEPK canonical AcnB; activity or role: 2-methylisocitrate dehydratase activity)
  - 5. carbon-carbon cleavage
  - 2-methylisocitrate cleavage
    - 2-methylisocitrate lyase (molecular player: PSEPK canonical PrpB; activity or role: methylisocitrate lyase activity)

### Known Relationships Among Steps

- Propionate activation to propionyl-CoA feeds into 2-methylcitrate synthesis: Propionyl-CoA is the acyl donor for 2-methylcitrate synthesis.
- 2-methylcitrate synthesis feeds into Conversion of 2-methylcitrate to 2-methyl-cis-aconitate: 2-methylcitrate enters either dehydration implementation.
- Conversion of 2-methylcitrate to 2-methyl-cis-aconitate feeds into 2-methyl-cis-aconitate hydration: Both alternatives converge on 2-methyl-cis-aconitate.
- 2-methyl-cis-aconitate hydration feeds into 2-methylisocitrate cleavage: 2-methylisocitrate is the substrate cleaved by PrpB.
- AcnD-family 2-methylcitrate dehydration feeds into PrpF methylaconitate isomerization: The AcnD product is the substrate rearranged by PrpF.

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

# Species-Aware Module Review: 2-Methylcitrate Cycle in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI 160488; proteome UP000000556)
**Bucket:** KEGG ppu00640 "Propanoate metabolism"
**Scope:** Propionate → propionyl-CoA → 2-methylcitrate → 2-methylisocitrate → succinate + pyruvate
**Date:** 2026-07-23 · Finalized across Iterations 1–3
**Evidence base:** UniProt/InterPro + KEGG KO cross-check + 7 literature references. No KT2440-specific enzymology exists; all conclusions are orthology/annotation-based (see §5, Appendix A).

---

## 1. Executive Summary

The 2-methylcitrate cycle (2-MCC) is **fully satisfiable** in *P. putida* KT2440. All five module
steps are encoded by high-confidence candidates concentrated in a single chromosomal cluster,
**PP_2334–PP_2339** (*prpB–prpC–acnA-II–prpF–prpD–acnB*), plus **PP_2351** (*prpE*, propionyl-CoA
synthetase). The 2-MCC is the *only* characterized propionate-oxidation route in *Pseudomonas*
(PMID 37995793), so the module should be marked **covered**.

The most curation-relevant finding is that KT2440 encodes **both** 2-methylcitrate-dehydration
implementations that the generic module treats as mutually exclusive alternatives:
- the **direct, cofactor-less PrpD route** (PP_2338), and
- the **two-component Fe/S AcnD/PrpF route** (PP_2336 + PP_2337).

PP_2336 (labelled "acnA-II") is not a generic aconitase — it carries the diagnostic InterPro
**IPR012708** (Fe/S-dependent 2-methyl-isocitrate/2-methylcitrate dehydratase, the AcnD family) and
sits immediately beside a bona fide **PrpF** gene (IPR012709 / PF04303), which is required only in
AcnD-using organisms. This resolves the module's "AcnA-II/AcnD candidate" to **AcnD (covered)**.

Main curation actions: reinterpret PP_2336 as AcnD; add EC 2.3.3.5 / methylcitrate-synthase GO to
PP_2335 (currently the over-broad "Citrate synthase, no EC"); treat PrpE substrate specificity as
context-inferred; note all cluster entries are UniProtKB **TrEMBL (unreviewed)**.

---

## 2. Target-Organism Pathway Definition

**Included biochemistry (5 steps):**
1. Propionate activation to **propionyl-CoA** — PrpE (ATP-dependent, AMP-forming ligase).
2. Condensation of propionyl-CoA + oxaloacetate → **(2S,3S)-2-methylcitrate** — PrpC (2-methylcitrate synthase).
3. Dehydration of 2-methylcitrate → **2-methyl-*cis*-aconitate** — PrpD (direct) **or** AcnD+PrpF (two-component).
4. Hydration of 2-methyl-*cis*-aconitate → **2-methyl-D-*threo*-isocitrate** — aconitase-family AcnB.
5. Aldol cleavage of 2-methylisocitrate → **succinate + pyruvate** — PrpB (2-methylisocitrate lyase).

**Neighboring maps to keep separate (do NOT merge into this module):**
- TCA-cycle aconitase (*acnA-I* PP_2112, *acnB* PP_2339 housekeeping role) and citrate synthase (*gltA*) — ppu00020.
- Methylmalonyl-CoA / vitamin-B12 propionate route (*mmsA*, methylmalonate-semialdehyde; ppu00562/00640 fringe) — a *distinct* propionate pathway not used here.
- Fatty-acid β-oxidation and BCAA/BCKA dehydrogenase genes (fadB, paaF, bkd*, lpd*, acd, acsA*, acc*, pta) — these are ppu00061/00071/00280/00785 members that appear in the candidate list only because ppu00640 is a broad KEGG "overview" bucket; they are **not** 2-MCC steps.

**Alternate names / DB definitions:** "2-methylcitric acid cycle (2-MCC)", "methylcitrate cycle
(MCC)", "propionate/propionyl-CoA oxidation pathway". KEGG folds it inside map00640 (Propanoate
metabolism) with module **M00741** (propanoyl-CoA → succinyl-CoA is the *other* route, not this one) —
the 2-MCC proper corresponds to the *prpBCDE* gene set, not a single tidy KEGG module.

---

## 3. Expected Step Model vs. PSEPK Genes

| # | Module step | Enzyme / EC | PSEPK gene | Status |
|---|-------------|-------------|------------|--------|
| 1 | Propionate activation | Propionyl-CoA synthetase, 6.2.1.17 | **prpE** PP_2351 (Q88KD9) | covered (specificity inferred) |
| 2 | 2-methylcitrate synthesis | 2-methylcitrate synthase, 2.3.3.5 | **prpC** PP_2335 (Q88KF5) | covered (EC missing) |
| 3a | Dehydration (direct) | 2-MC dehydratase, 4.2.1.79 | **prpD** PP_2338 (Q88KF2) | covered |
| 3b | Dehydration (2-component) | AcnD Fe/S dehydratase + PrpF isomerase | **acnA-II/AcnD** PP_2336 (Q88KF4) + **prpF** PP_2337 (Q88KF3) | covered |
| 4 | Hydration to 2-methylisocitrate | Aconitase-family, 4.2.1.99 | **acnB** PP_2339 (Q88KF1); paralog **acnA-I** PP_2112 (K27802) | covered (redundant paralogs) |
| 5 | C–C cleavage | 2-methylisocitrate lyase, 4.1.3.30 | **prpB** PP_2334 (Q88KF6) | covered |

No step is a **gap** or **not_expected_in_target_taxon**.

---

## 4. Candidate Genes and Evidence

**High-confidence, in-cluster (promote-worthy):**

- **PrpE — PP_2351 (Q88KD9, 629 aa).** AMP-binding acyl-CoA ligase (Pfam PF00501 + ACAS_N PF16177).
  Role: propionate → propionyl-CoA. Caveat: the AMP-binding family is broad; propionyl- vs
  acetyl-CoA specificity is inferred from *prp*-cluster context (KT2440 also has dedicated acetyl-CoA
  synthetases acsA1/acsA2), not from a PSEPK biochemical assay. Salmonella PrpE is a propionyl-CoA
  synthetase (PMID 10482501).
- **PrpC — PP_2335 (Q88KF5, 375 aa).** InterPro **IPR011278** "2-MeCitrate/Citrate_synth_II" = the
  type-II (methyl)citrate synthase clade. Function is well established across bacteria; PrpC prefers
  propionyl-CoA (PMID 10482501; C. glutamicum PrpC has 2-methylcitrate synthase activity, PMID 11976302).
  **Caveat:** UniProt calls it "Citrate synthase" with **no EC** — over-broad; should be EC 2.3.3.5.
- **PrpD — PP_2338 (Q88KF2, EC 4.2.1.79).** Cofactor-less 2-methylcitrate dehydratase. Direct-route enzyme.
- **AcnD — PP_2336 (Q88KF4, 862 aa).** Carries diagnostic **IPR012708** (Fe/S 2-methylcitrate/2-
  methylisocitrate dehydratase = AcnD) with 4Fe-4S/Iron-sulfur keywords. AcnD performs only the first
  half-reaction (dehydration to a 4-methylaconitate isomer) and requires PrpF (PMID 14702315, 29145506).
  **Caveat:** UniProt annotates it merely as "aconitate hydratase (EC 4.2.1.3)"; reinterpret as AcnD.
- **PrpF — PP_2337 (Q88KF3, 396 aa).** InterPro **IPR012709** / Pfam **PF04303** "PrpF"; isomerase.
  Isomerizes the AcnD product into 2-methyl-*cis*-aconitate, the substrate of housekeeping aconitase
  (PMID 17567742, 29145506). Presence of PrpF is itself strong evidence the AcnD route is functional.
- **AcnB — PP_2339 (Q88KF1, 869 aa, EC 4.2.1.3/4.2.1.99).** Aconitase-B family (IPR004406); catalyzes
  the hydration of 2-methyl-*cis*-aconitate to 2-methylisocitrate (the module's aconitase-family step).
- **PrpB — PP_2334 (Q88KF6, 296 aa).** InterPro **IPR012695** "PrpB"; 2-methylisocitrate lyase
  (EC 4.1.3.30), Mg-dependent. Cleaves 2-methylisocitrate → succinate + pyruvate. A *Pseudomonas prpB*
  mutant is blocked in propionate oxidation (PMID 37995793).

**Candidate-list members that are NOT 2-MCC steps (over-inclusion by the broad bucket):**
accA/B/C/D (fatty-acid/malonyl-CoA, ppu00061), pta, PP_2213/acsA1/acsA2 (acetate activation),
acnA-I PP_2112 (housekeeping TCA aconitase), fadB/paaF/PP_2217/acd (β-oxidation/CoA hydratases),
mmsA-I/II & PP_0596 (methylmalonate-semialdehyde route), sucC/sucD (succinyl-CoA ligase), and the
bkd*/lpd*/lpdG BCKA-dehydrogenase complex (ppu00785). These should stay mapped to their own modules.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

- **No true gaps.** Every step has a diagnostic-family candidate.
- **Redundant dehydration:** PrpD *and* AcnD/PrpF coexist — the generic module's "alternative
  implementations" are **both realized**, not either/or. Module boundary text should allow parallel
  co-encoded implementations in a single genome.
- **Over-broad annotations to fix:** PrpC "Citrate synthase (no EC)" → methylcitrate synthase (2.3.3.5);
  AcnD PP_2336 "aconitate hydratase (4.2.1.3)" → AcnD Fe/S 2-methylcitrate dehydratase.
- **Paralog ambiguity (aconitases):** three aconitase-family proteins (AcnA-I PP_2112, AcnD PP_2336,
  AcnB PP_2339) share EC 4.2.1.3 by homology. AcnB does the 2-MCC hydration; KEGG also credits AcnA-I
  (K27802) with 2-methylisocitrate-dehydratase activity, so AcnA-I is *not* purely housekeeping. AcnD
  performs only the dehydration half-reaction. Only the "2-methyl-" activities relevant to the 2-MCC
  should be curated on the correct paralogs.
- **Paralog ambiguity (lyase superfamily):** PrpB (PP_2334, 2-methylisocitrate lyase, EC 4.1.3.30) and
  **AceA (PP_4116, isocitrate lyase, EC 4.1.3.1)** share the ICL/PEP-mutase fold (IPR039556) but have
  distinct substrate pockets (Salmonella PrpB structure, PMID 14575713). AceA is a **decoy** in the
  ppu00640 bucket — it belongs to the glyoxylate shunt, not the 2-MCC. Map the cleavage step to PrpB
  only and exclude AceA to prevent over-propagation of 2-methylisocitrate-lyase activity.
- **Evidence level:** all findings rest on *homology + genomic context + strong ortholog biochemistry*
  in Salmonella/Shewanella/Vibrio/Corynebacterium. There is **no KT2440-specific enzymology** in the
  retrieved literature; all UniProt entries are TrEMBL (unreviewed, electronic).

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended mark |
|-------------|------------------|
| Propionate activation (PrpE) | **covered** (note: specificity inferred) |
| 2-methylcitrate synthesis (PrpC) | **covered** (request EC 2.3.3.5 / GO:0050440 addition) |
| Direct PrpD dehydration | **covered** |
| AcnD/PrpF two-component dehydration | **covered** (reassign PP_2336 → AcnD) |
| Aconitase-family hydration (AcnB) | **covered** |
| 2-methylisocitrate cleavage (PrpB) | **covered** |

- **Module needs minor revision:** allow the two dehydration implementations to be *simultaneously*
  present (parallel), not modeled as exclusive alternatives, since Pseudomonas carries both.
- **GO requests:** ensure GO:0050440 (2-methylcitrate synthase), GO:0047547 (2-methylcitrate
  dehydratase), GO:0046421 (methylisocitrate lyase), and an AcnD/2-methyl-cis-aconitate isomerase
  (PrpF, GO:0016853 isomerase / trans-aconitate isomerase) term are attached to the right loci.
- No new module document is required; the generic outline already captures both routes.

## 7. Genes to Promote to Full `fetch-gene` Review

1. **PP_2336 (acnA-II/AcnD)** — highest priority: annotation says "aconitase" but InterPro says AcnD; needs functional reassignment.
2. **PP_2335 (prpC)** — add methylcitrate-synthase EC/GO; distinguish from housekeeping gltA.
3. **PP_2351 (prpE)** — confirm propionyl-CoA (vs acetyl-CoA) specificity.
4. **PP_2337 (prpF)** — confirm isomerase EC/GO (currently no EC).
5. **PP_2339 (acnB)** — confirm 2-methylisocitrate-dehydratase (4.2.1.99) role vs housekeeping aconitase.

## 8. Key References

- Horswill & Escalante-Semerena 1999, *Salmonella typhimurium* 2-MCC (**PMID 10482501**).
- Grimek & Escalante-Semerena 2004, AcnD is a new Fe/S 2-methylcitrate dehydratase requiring PrpF (**PMID 14702315**).
- Garvey et al. 2007, PrpF crystal structure / aconitate isomerase (**PMID 17567742**).
- Rocco et al. 2017, PrpF isomerizes the AcnD product to the AcnB substrate (**PMID 29145506**).
- Claes et al. 2002, *C. glutamicum* prpDBC / 2-methylcitrate synthase (**PMID 11976302**).
- Simanshu et al. 2003, *Salmonella* PrpB (2-methylisocitrate lyase) crystal structure; PrpB vs isocitrate-lyase substrate specificity (**PMID 14575713**).
- Santos-Oliveira et al. 2024, *Pseudomonas* prpB mutant; 2-MCC is the only propionate-oxidation route (**PMID 37995793**).

**Uncertainty statement:** Conclusions are strong by orthology + diagnostic InterPro families +
genomic clustering, but no direct *P. putida* KT2440 enzymology was found in the retrieved literature;
all UniProt annotations are unreviewed (TrEMBL). Species transfer from *Salmonella/Shewanella/Vibrio*
to PSEPK is **strong** for pathway logic and **moderate** for individual substrate specificities.

---

## Appendix A — Independent KEGG KO cross-check (added Iteration 2)

An orthology system independent of UniProt/InterPro (KEGG KO) agrees on every step and adds detail:

| Locus | Gene | KEGG KO | KO name / EC | Interpretation |
|-------|------|---------|--------------|----------------|
| PP_2334 | prpB | K03417 | methylisocitrate lyase, EC 4.1.3.30 | confirms PrpB |
| PP_2335 | prpC | K01659 | **2-methylcitrate synthase, EC 2.3.3.5** | supplies the EC missing from UniProt |
| PP_2336 | acnA-II | **K20455** | **2-methylcitrate dehydratase (2-methyl-*trans*-aconitate forming), EC 4.2.1.117** | confirms **AcnD** (distinct KO from PrpD) |
| PP_2337 | prpF | K09788 | **2-methylaconitate isomerase, EC 5.3.3.-** | confirms **PrpF** isomerase |
| PP_2338 | prpD | K01720 | 2-methylcitrate dehydratase, EC 4.2.1.79 | confirms PrpD |
| PP_2339 | acnB | K01682 | aconitate hydratase 2 / 2-methylisocitrate dehydratase, EC 4.2.1.3/4.2.1.99 | confirms AcnB (hydration) |
| PP_2351 | prpE | K01908 | **propionyl-CoA synthetase, EC 6.2.1.17** | confirms PrpE specificity (reduces earlier caveat) |
| PP_2112 | acnA-I | K27802 | aconitate hydratase A / 2-methylisocitrate dehydratase, EC 4.2.1.3/4.2.1.99 | **AcnA-I also carries the hydration activity → step-4 redundancy** |

**Consequences for curation:**
1. **AcnD confirmed twice.** PP_2336 is AcnD by KEGG KO **K20455 / EC 4.2.1.117** *and* by InterPro IPR012708. Its product is 2-methyl-*trans*-aconitate, which PrpF (2-methylaconitate isomerase, EC 5.3.3.-) converts to the 2-methyl-*cis*-aconitate accepted by aconitase — this fully resolves the module's "AcnD-family dehydration → PrpF isomerization" sub-steps to real genes with matched product chemistry.
2. **PrpC EC and PrpE specificity are corroborated** by KEGG (EC 2.3.3.5; EC 6.2.1.17), so those caveats downgrade from "over-broad" to "UniProt EC field incomplete — fill from KEGG."
3. **Step 4 (hydration) is redundant:** both **AcnB (PP_2339)** and **AcnA-I (PP_2112)** carry 2-methylisocitrate-dehydratase capability (EC 4.2.1.99). Mark the step covered with a paralog note; do not attribute it solely to AcnB, and conversely do not treat AcnA-I as purely housekeeping.
4. **No in-cluster regulator:** PP_2340 (between *acnB* and *prpE*) is K06938 "uncharacterized"; no *prpR*-type regulator was found immediately adjacent (regulation likely encoded elsewhere — an open question).

**Boundary confirmation:** KEGG's ppu00640 gene set is identical to the 33-gene candidate list, confirming that list is the *broad overview map* (Propanoate metabolism), not the 2-MCC module proper. Only PP_2334–PP_2339 + PP_2351 (+ PP_2112 as a hydration paralog) belong to the 2-MCC; the remaining ~25 genes stay in their own modules.


## Artifacts

- [OpenScientist final report](PSEPK__methylcitrate_cycle__ppu00640-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__methylcitrate_cycle__ppu00640-deep-research-openscientist_artifacts/final_report.pdf)