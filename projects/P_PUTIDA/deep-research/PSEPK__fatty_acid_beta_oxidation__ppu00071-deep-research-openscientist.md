---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-10T22:48:04.008132'
end_time: '2026-08-10T23:01:16.380897'
duration_seconds: 792.37
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Mitochondrial fatty acid beta-oxidation spiral (cross-species)
  module_summary: 'The core four-step spiral of mitochondrial fatty acid beta-oxidation,
    by which saturated fatty acyl-CoA esters are degraded two carbons at a time, releasing
    one acetyl-CoA and a chain-shortened acyl-CoA per turn that re-enters the cycle.
    The four obligate reactions are (1) FAD-dependent alpha,beta-dehydrogenation of
    acyl-CoA to (2E)-enoyl-CoA by an acyl-CoA dehydrogenase; (2) hydration of the
    trans double bond to (3S)-3-hydroxyacyl-CoA by an enoyl-CoA hydratase; (3) NAD+-dependent
    oxidation to 3-ketoacyl-CoA by a 3-hydroxyacyl-CoA dehydrogenase; and (4) thiolytic
    cleavage by a 3-ketoacyl-CoA thiolase to yield acetyl-CoA plus an acyl-CoA shortened
    by two carbons. Each step is carried out by a family of chain-length-specific
    isozymes: as the acyl chain shortens through successive turns of the spiral, the
    enzyme that acts changes. The long-chain steps 2-4 are performed by the membrane-bound
    mitochondrial trifunctional protein (MTP, an alpha2-beta2 heterotetramer whose
    alpha subunit carries the hydratase and dehydrogenase activities and whose beta
    subunit carries the thiolase), whereas the medium- and short-chain steps are carried
    out by separate soluble matrix enzymes. This module is built cross-species: each
    catalytic role is grounded with both the human enzyme(s) and the Drosophila melanogaster
    ortholog(s), so the conserved enzymatic logic and the species-specific gene complement
    can be compared directly. The chain-length axis is modelled as a variant set at
    each step; "use MF specific for chain length" where such a molecular-function
    term exists, with a fall-back to the general activity where it does not. This
    module covers the SATURATED spiral. Degradation of UNSATURATED fatty acids additionally
    requires an auxiliary-enzyme cassette - a delta(3),delta(2)-enoyl-CoA isomerase
    (fly mitochondrial CG4592/CG4594/CG4598 vs peroxisomal Dci), a delta(3,5),delta(2,4)-dienoyl-CoA
    isomerase (fly Ech1), and a 2,4-dienoyl-CoA reductase (DECR1, for which no clean
    Drosophila ortholog is currently assignable) - which are curated in the project
    but not modelled as variant sets here; see the Fatty Acid beta-Oxidation project
    page (unsaturated cassette section) for details.'
  module_outline: "- Mitochondrial fatty acid beta-oxidation spiral\n  - 1. alpha,beta-dehydrogenation\
    \ of acyl-CoA (FAD-dependent)\n  - Step 1: acyl-CoA dehydrogenase\n    - Alternative\
    \ versions by acyl-CoA chain length: Chain-length-specific acyl-CoA dehydrogenases\n\
    \      - Very-long / long-chain acyl-CoA dehydrogenase (VLCAD / ACAD9)\n     \
    \   - VLCAD/ACAD9: very-long-chain acyl-CoA dehydrogenase (molecular player: Very-long/long-chain\
    \ acyl-CoA dehydrogenase (VLCAD/ACAD9); activity or role: very-long-chain fatty\
    \ acyl-CoA dehydrogenase activity)\n      - Medium-chain acyl-CoA dehydrogenase\
    \ (MCAD)\n        - MCAD: medium-chain acyl-CoA dehydrogenase (molecular player:\
    \ Medium-chain acyl-CoA dehydrogenase (MCAD); activity or role: medium-chain fatty\
    \ acyl-CoA dehydrogenase activity)\n      - Short-chain acyl-CoA dehydrogenase\
    \ (SCAD)\n        - SCAD: short-chain acyl-CoA dehydrogenase (molecular player:\
    \ Short-chain acyl-CoA dehydrogenase (SCAD); activity or role: short-chain fatty\
    \ acyl-CoA dehydrogenase activity)\n  - 2. hydration of (2E)-enoyl-CoA to (3S)-3-hydroxyacyl-CoA\n\
    \  - Step 2: enoyl-CoA hydratase\n    - Alternative versions by acyl-CoA chain\
    \ length: Chain-length-specific enoyl-CoA hydratases\n      - Long-chain enoyl-CoA\
    \ hydratase (MTP alpha subunit, HADHA)\n        - HADHA/MTP-alpha: long-chain\
    \ enoyl-CoA hydratase (molecular player: Trifunctional enzyme alpha subunit (HADHA\
    \ / MTP alpha); activity or role: enoyl-CoA hydratase activity)\n      - Short/medium-chain\
    \ enoyl-CoA hydratase (ECHS1, crotonase)\n        - ECHS1: short-chain enoyl-CoA\
    \ hydratase (crotonase) (molecular player: Short-chain enoyl-CoA hydratase (ECHS1\
    \ / crotonase); activity or role: enoyl-CoA hydratase activity)\n  - 3. NAD+-dependent\
    \ oxidation of (3S)-3-hydroxyacyl-CoA to 3-ketoacyl-CoA\n  - Step 3: 3-hydroxyacyl-CoA\
    \ dehydrogenase\n    - Alternative versions by acyl-CoA chain length: Chain-length-specific\
    \ 3-hydroxyacyl-CoA dehydrogenases\n      - Long-chain 3-hydroxyacyl-CoA dehydrogenase\
    \ (MTP alpha subunit, HADHA)\n        - HADHA/MTP-alpha: long-chain 3-hydroxyacyl-CoA\
    \ dehydrogenase (molecular player: Trifunctional enzyme alpha subunit (HADHA /\
    \ MTP alpha); activity or role: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase\
    \ (NAD+) activity)\n      - Short/medium-chain 3-hydroxyacyl-CoA dehydrogenase\
    \ (HADH / SCHAD)\n        - HADH: short/medium-chain 3-hydroxyacyl-CoA dehydrogenase\
    \ (molecular player: Short-chain 3-hydroxyacyl-CoA dehydrogenase (HADH / SCHAD);\
    \ activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)\n  -\
    \ 4. thiolytic cleavage of 3-ketoacyl-CoA to acetyl-CoA + chain-shortened acyl-CoA\n\
    \  - Step 4: 3-ketoacyl-CoA thiolase\n    - Alternative versions by acyl-CoA chain\
    \ length: Chain-length-specific 3-ketoacyl-CoA thiolases\n      - Long-chain 3-ketoacyl-CoA\
    \ thiolase (MTP beta subunit, HADHB)\n        - HADHB/MTP-beta: long-chain 3-ketoacyl-CoA\
    \ thiolase (molecular player: Trifunctional enzyme beta subunit (HADHB / MTP beta);\
    \ activity or role: acetyl-CoA C-acyltransferase activity)\n      - Medium/long-chain\
    \ 3-ketoacyl-CoA thiolase (ACAA2)\n        - ACAA2: 3-ketoacyl-CoA thiolase (molecular\
    \ player: 3-ketoacyl-CoA thiolase (ACAA2); activity or role: acetyl-CoA C-acyltransferase\
    \ activity)\n      - Short-chain / acetoacetyl-CoA thiolase (ACAT1, T2)\n    \
    \    - ACAT1: acetoacetyl-CoA thiolase (T2) (molecular player: Acetoacetyl-CoA\
    \ thiolase (ACAT1 / T2); activity or role: acetyl-CoA C-acetyltransferase activity)"
  module_connections: '- Step 1: acyl-CoA dehydrogenase precedes Step 2: enoyl-CoA
    hydratase

    - Step 2: enoyl-CoA hydratase precedes Step 3: 3-hydroxyacyl-CoA dehydrogenase

    - Step 3: 3-hydroxyacyl-CoA dehydrogenase precedes Step 4: 3-ketoacyl-CoA thiolase

    - Step 4: 3-ketoacyl-CoA thiolase feeds into Step 1: acyl-CoA dehydrogenase: The
    chain-shortened acyl-CoA produced by the thiolase re-enters step 1, making the
    pathway a spiral that iterates until the chain is fully degraded.'
  pathway_query: ppu00071
  pathway_id: ppu00071
  pathway_name: Fatty acid degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00071 with 6 primary genes; module
    area: lipid_cell_envelope_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '22'
  candidate_genes: '- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC
    1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)

    - PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)

    - frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1)
    (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III)
    (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary
    bucket kegg:ppu00626)

    - fadE: PP_1893 | Q88LN6 | Acyl-coenzyme A dehydrogenase (EC 1.3.8.7) (EC 1.3.8.8)
    (EC 1.3.8.7; 1.3.8.8; primary bucket kegg:ppu00071)

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

    - acd: PP_2216 | Q88KS3 | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC
    3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane-1-carbonyl-CoA
    dehydrogenase) (EC 1.3.8.11; 3.13.1.4; primary bucket kegg:ppu00410)

    - PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_2437: PP_2437 | Q88K54 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC
    1.3.8.8; primary bucket kegg:ppu00071)

    - PP_2793: PP_2793 | Q88J56 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC
    1.3.8.8; primary bucket kegg:ppu00071)

    - paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)

    - PP_3725: PP_3725 | Q88GJ7 | Acyl-CoA dehydrogenase (primary bucket kegg:ppu00071)

    - bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC
    2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)

    - adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1)
    (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)

    - fadD-I: PP_4549 | Q88EB7 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain
    acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)

    - fadD-II: PP_4550 | Q88EB6 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain
    acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)

    - yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9;
    primary bucket kegg:ppu00900)

    - alkT: PP_5314 | Q88C69 | Rubredoxin-NAD(+) reductase (EC 1.18.1.1) (EC 1.18.1.1;
    primary bucket kegg:ppu00071)

    - PP_5371: PP_5371 | Q88C12 | Rubredoxin/rubredoxin reductase (primary bucket
    kegg:ppu00071)'
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
  path: PSEPK__fatty_acid_beta_oxidation__ppu00071-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__fatty_acid_beta_oxidation__ppu00071-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Mitochondrial fatty acid beta-oxidation spiral (cross-species) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00071
- Resolved ID: ppu00071
- Resolved name: Fatty acid degradation
- Source: KEGG

Resolved local bucket kegg:ppu00071 with 6 primary genes; module area: lipid_cell_envelope_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 22

- gcdH: PP_0158 | Q88RH2 | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) (EC 1.3.8.6; primary bucket kegg:ppu00380)
- PP_0582: PP_0582 | Q88QB2 | Thiolase family protein (primary bucket kegg:ppu00900)
- frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary bucket kegg:ppu00626)
- fadE: PP_1893 | Q88LN6 | Acyl-coenzyme A dehydrogenase (EC 1.3.8.7) (EC 1.3.8.8) (EC 1.3.8.7; 1.3.8.8; primary bucket kegg:ppu00071)
- fadA__Q88L84: PP_2051 | Q88L84 | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- fadB: PP_2136 | Q88L02 | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomerase/3-hydroxybutyryl-CoA epimerase (EC 4.2.1.17) (EC 5.1.2.3) (EC 5.3.3.8); 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)] (EC 1.1.1.35; 4.2.1.17; 5.1.2.3; 5.3.3.8; primary bucket kegg:ppu00930)
- fadA__Q88L01: PP_2137 | Q88L01 | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta) (EC 2.3.1.16; primary bucket kegg:ppu00592)
- PP_2215: PP_2215 | Q88KS4 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- acd: PP_2216 | Q88KS3 | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane-1-carbonyl-CoA dehydrogenase) (EC 1.3.8.11; 3.13.1.4; primary bucket kegg:ppu00410)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_2437: PP_2437 | Q88K54 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC 1.3.8.8; primary bucket kegg:ppu00071)
- PP_2793: PP_2793 | Q88J56 | long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) (EC 1.3.8.8; primary bucket kegg:ppu00071)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- PP_3355: PP_3355 | Q88HK1 | Beta-ketothiolase (primary bucket kegg:ppu00900)
- PP_3725: PP_3725 | Q88GJ7 | Acyl-CoA dehydrogenase (primary bucket kegg:ppu00071)
- bktB: PP_3754 | Q88GH0 | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) (EC 2.3.1.16; 2.3.1.9; primary bucket kegg:ppu00900)
- adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)
- fadD-I: PP_4549 | Q88EB7 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)
- fadD-II: PP_4550 | Q88EB6 | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) (EC 6.2.1.3; primary bucket kegg:ppu04146)
- yqeF: PP_4636 | Q88E32 | Acetyl-CoA acetyltransferase (EC 2.3.1.9) (EC 2.3.1.9; primary bucket kegg:ppu00900)
- alkT: PP_5314 | Q88C69 | Rubredoxin-NAD(+) reductase (EC 1.18.1.1) (EC 1.18.1.1; primary bucket kegg:ppu00071)
- PP_5371: PP_5371 | Q88C12 | Rubredoxin/rubredoxin reductase (primary bucket kegg:ppu00071)

## Generic Module Context

### Working Scope

The core four-step spiral of mitochondrial fatty acid beta-oxidation, by which saturated fatty acyl-CoA esters are degraded two carbons at a time, releasing one acetyl-CoA and a chain-shortened acyl-CoA per turn that re-enters the cycle. The four obligate reactions are (1) FAD-dependent alpha,beta-dehydrogenation of acyl-CoA to (2E)-enoyl-CoA by an acyl-CoA dehydrogenase; (2) hydration of the trans double bond to (3S)-3-hydroxyacyl-CoA by an enoyl-CoA hydratase; (3) NAD+-dependent oxidation to 3-ketoacyl-CoA by a 3-hydroxyacyl-CoA dehydrogenase; and (4) thiolytic cleavage by a 3-ketoacyl-CoA thiolase to yield acetyl-CoA plus an acyl-CoA shortened by two carbons. Each step is carried out by a family of chain-length-specific isozymes: as the acyl chain shortens through successive turns of the spiral, the enzyme that acts changes. The long-chain steps 2-4 are performed by the membrane-bound mitochondrial trifunctional protein (MTP, an alpha2-beta2 heterotetramer whose alpha subunit carries the hydratase and dehydrogenase activities and whose beta subunit carries the thiolase), whereas the medium- and short-chain steps are carried out by separate soluble matrix enzymes. This module is built cross-species: each catalytic role is grounded with both the human enzyme(s) and the Drosophila melanogaster ortholog(s), so the conserved enzymatic logic and the species-specific gene complement can be compared directly. The chain-length axis is modelled as a variant set at each step; "use MF specific for chain length" where such a molecular-function term exists, with a fall-back to the general activity where it does not. This module covers the SATURATED spiral. Degradation of UNSATURATED fatty acids additionally requires an auxiliary-enzyme cassette - a delta(3),delta(2)-enoyl-CoA isomerase (fly mitochondrial CG4592/CG4594/CG4598 vs peroxisomal Dci), a delta(3,5),delta(2,4)-dienoyl-CoA isomerase (fly Ech1), and a 2,4-dienoyl-CoA reductase (DECR1, for which no clean Drosophila ortholog is currently assignable) - which are curated in the project but not modelled as variant sets here; see the Fatty Acid beta-Oxidation project page (unsaturated cassette section) for details.

### Provisional Biological Outline

- Mitochondrial fatty acid beta-oxidation spiral
  - 1. alpha,beta-dehydrogenation of acyl-CoA (FAD-dependent)
  - Step 1: acyl-CoA dehydrogenase
    - Alternative versions by acyl-CoA chain length: Chain-length-specific acyl-CoA dehydrogenases
      - Very-long / long-chain acyl-CoA dehydrogenase (VLCAD / ACAD9)
        - VLCAD/ACAD9: very-long-chain acyl-CoA dehydrogenase (molecular player: Very-long/long-chain acyl-CoA dehydrogenase (VLCAD/ACAD9); activity or role: very-long-chain fatty acyl-CoA dehydrogenase activity)
      - Medium-chain acyl-CoA dehydrogenase (MCAD)
        - MCAD: medium-chain acyl-CoA dehydrogenase (molecular player: Medium-chain acyl-CoA dehydrogenase (MCAD); activity or role: medium-chain fatty acyl-CoA dehydrogenase activity)
      - Short-chain acyl-CoA dehydrogenase (SCAD)
        - SCAD: short-chain acyl-CoA dehydrogenase (molecular player: Short-chain acyl-CoA dehydrogenase (SCAD); activity or role: short-chain fatty acyl-CoA dehydrogenase activity)
  - 2. hydration of (2E)-enoyl-CoA to (3S)-3-hydroxyacyl-CoA
  - Step 2: enoyl-CoA hydratase
    - Alternative versions by acyl-CoA chain length: Chain-length-specific enoyl-CoA hydratases
      - Long-chain enoyl-CoA hydratase (MTP alpha subunit, HADHA)
        - HADHA/MTP-alpha: long-chain enoyl-CoA hydratase (molecular player: Trifunctional enzyme alpha subunit (HADHA / MTP alpha); activity or role: enoyl-CoA hydratase activity)
      - Short/medium-chain enoyl-CoA hydratase (ECHS1, crotonase)
        - ECHS1: short-chain enoyl-CoA hydratase (crotonase) (molecular player: Short-chain enoyl-CoA hydratase (ECHS1 / crotonase); activity or role: enoyl-CoA hydratase activity)
  - 3. NAD+-dependent oxidation of (3S)-3-hydroxyacyl-CoA to 3-ketoacyl-CoA
  - Step 3: 3-hydroxyacyl-CoA dehydrogenase
    - Alternative versions by acyl-CoA chain length: Chain-length-specific 3-hydroxyacyl-CoA dehydrogenases
      - Long-chain 3-hydroxyacyl-CoA dehydrogenase (MTP alpha subunit, HADHA)
        - HADHA/MTP-alpha: long-chain 3-hydroxyacyl-CoA dehydrogenase (molecular player: Trifunctional enzyme alpha subunit (HADHA / MTP alpha); activity or role: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
      - Short/medium-chain 3-hydroxyacyl-CoA dehydrogenase (HADH / SCHAD)
        - HADH: short/medium-chain 3-hydroxyacyl-CoA dehydrogenase (molecular player: Short-chain 3-hydroxyacyl-CoA dehydrogenase (HADH / SCHAD); activity or role: (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity)
  - 4. thiolytic cleavage of 3-ketoacyl-CoA to acetyl-CoA + chain-shortened acyl-CoA
  - Step 4: 3-ketoacyl-CoA thiolase
    - Alternative versions by acyl-CoA chain length: Chain-length-specific 3-ketoacyl-CoA thiolases
      - Long-chain 3-ketoacyl-CoA thiolase (MTP beta subunit, HADHB)
        - HADHB/MTP-beta: long-chain 3-ketoacyl-CoA thiolase (molecular player: Trifunctional enzyme beta subunit (HADHB / MTP beta); activity or role: acetyl-CoA C-acyltransferase activity)
      - Medium/long-chain 3-ketoacyl-CoA thiolase (ACAA2)
        - ACAA2: 3-ketoacyl-CoA thiolase (molecular player: 3-ketoacyl-CoA thiolase (ACAA2); activity or role: acetyl-CoA C-acyltransferase activity)
      - Short-chain / acetoacetyl-CoA thiolase (ACAT1, T2)
        - ACAT1: acetoacetyl-CoA thiolase (T2) (molecular player: Acetoacetyl-CoA thiolase (ACAT1 / T2); activity or role: acetyl-CoA C-acetyltransferase activity)

### Known Relationships Among Steps

- Step 1: acyl-CoA dehydrogenase precedes Step 2: enoyl-CoA hydratase
- Step 2: enoyl-CoA hydratase precedes Step 3: 3-hydroxyacyl-CoA dehydrogenase
- Step 3: 3-hydroxyacyl-CoA dehydrogenase precedes Step 4: 3-ketoacyl-CoA thiolase
- Step 4: 3-ketoacyl-CoA thiolase feeds into Step 1: acyl-CoA dehydrogenase: The chain-shortened acyl-CoA produced by the thiolase re-enters step 1, making the pathway a spiral that iterates until the chain is fully degraded.

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

# Species-Aware Module Review: Fatty Acid β-Oxidation Spiral in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI 160488; proteome UP000000556)
**Module reviewed:** Mitochondrial fatty acid β-oxidation spiral (cross-species generic module)
**Local pathway bucket:** KEGG `ppu00071` "Fatty acid degradation"
**Prepared for:** manual module satisfiability and gene-annotation curation

---

## 1. Executive summary

- The generic module is a **eukaryotic/mitochondrial** construct. In the bacterium *P. putida* KT2440 the identical four-step chemistry is executed in the **cytoplasm** by the **FadBA fatty-acid-oxidation multienzyme complex** plus standalone acyl-CoA dehydrogenases — **not** by a mitochondrial trifunctional protein (MTP). The module is **satisfiable by conserved enzyme families**, but should be curated as *covered-by-bacterial-analog*, not mapped subunit-for-subunit onto HADHA/HADHB/ECHS1/HADH/ACAA2.
- **All four obligate steps + the upstream activation feeder are covered.** No step is a genuine gap.
- **Evidence tier is thin.** Of the 22 candidates, **only fadB (PP_2136) and fadA (PP_2137) are Swiss-Prot "reviewed"**; the other 20 are unreviewed TrEMBL, and **all 22 have UniProt protein-existence = "Inferred from homology."** There is no protein-level experimental annotation for any candidate; functional support comes from KT2440 physiology/engineering studies, not per-gene biochemistry.
- **≈ Half of the candidate list is over-propagation** from neighboring CoA-thioester pathways (glutaryl-CoA, sulfinopropanoyl-CoA, phenylacetyl-CoA, alcohol dehydrogenases, alkane-hydroxylase redox partners, and EC 2.3.1.9 PHA/acetoacetyl thiolases) and should **not** count toward spiral coverage.
- **The candidate metadata has omissions.** A proteome-wide EC scan (UniProt, taxon 160488) shows the true standalone step-3 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35) is **PP_2214 (Q88KS5), absent from the 22-gene list**, and a third fatty-acyl-CoA ligase **PP_2038 (Q88L97)** is likewise missing. PP_2214–PP_2217 form a **contiguous four-gene β-oxidation cassette** (steps 3-4-1-2), so several genes previously read as "scattered over-annotation" are actually a coherent paralogous operon.

## 2. Target-organism pathway definition

**Included process (working scope):** the iterative, cytoplasmic degradation of saturated acyl-CoA esters two carbons per turn, comprising four obligate reactions — (1) FAD-dependent α,β-dehydrogenation (acyl-CoA dehydrogenase, EC 1.3.8.x), (2) hydration of *trans*-2-enoyl-CoA (enoyl-CoA hydratase, EC 4.2.1.17), (3) NAD⁺-dependent oxidation to 3-ketoacyl-CoA (3-hydroxyacyl-CoA dehydrogenase, EC 1.1.1.35), (4) thiolytic cleavage to acetyl-CoA + chain-shortened acyl-CoA (3-ketoacyl-CoA thiolase, EC 2.3.1.16). The chain-shortened acyl-CoA re-enters step 1 (the spiral). An upstream **activation feeder** (long-chain-fatty-acid–CoA ligase, EC 6.2.1.3) is required to make the acyl-CoA substrate.

**Keep separate (neighboring pathways / overview maps):**
- De novo **fatty-acid biosynthesis** (fab genes; ACP-linked, EC 2.3.1.- synthases) — opposite direction; a documented source of confusion in *P. putida* (cryptic FabF2, PMID 34181948).
- **mcl-PHA biosynthesis** (phaC/phaG/phaJ) — draws (R)-3-hydroxyacyl-CoA *from* the β-oxidation spiral but is a distinct module (PMID 36763117).
- **Unsaturated-FA auxiliary cassette** (Δ3,Δ2-enoyl-CoA isomerase; Δ3,5,Δ2,4-dienoyl-CoA isomerase; 2,4-dienoyl-CoA reductase) — explicitly out of scope for the *saturated* spiral.
- **Alkane oxidation (alk system)** — upstream of β-oxidation; supplies fatty acids but is not part of the spiral (relevant to mis-bucketed alkT/PP_5371).
- Amino-acid / aromatic / alicyclic acyl-CoA catabolism (glutaryl-CoA, phenylacetyl-CoA, cyclohexanecarbonyl-CoA) — separate KEGG buckets.

**Alternate names / DB definitions:** KEGG `ppu00071` "Fatty acid degradation"; EC-level it overlaps E. coli **fad** regulon nomenclature (fadD, fadE, fadBA, fadL, fadR). Bacterial FadB ≡ eukaryotic "trifunctional enzyme α" by homology only (PMID 1699931).

## 3. Expected step model (as realized in KT2440)

| Step | Chemistry (EC) | Eukaryotic players (module) | KT2440 realization |
|---|---|---|---|
| Activation (feeder) | acyl-CoA synthetase (6.2.1.3) | — | **fadD-I/II** PP_4549/PP_4550 (+ dispersed fadD paralogs) |
| 1. α,β-dehydrogenation | acyl-CoA dehydrogenase (1.3.8.7/1.3.8.8) | VLCAD/MCAD/SCAD | **fadE** PP_1893 (+ PP_2437, PP_2793, PP_3725) |
| 2. hydration | enoyl-CoA hydratase (4.2.1.17) | HADHA (MTP-α), ECHS1 | **fadB** PP_2136 (bifunctional α); ancillary PP_2217 |
| 3. NAD⁺ oxidation | 3-hydroxyacyl-CoA DH (1.1.1.35) | HADHA (MTP-α), HADH | **fadB** PP_2136 (same polypeptide) + standalone **PP_2214** |
| 4. thiolysis | 3-ketoacyl-CoA thiolase (2.3.1.16) | HADHB (MTP-β), ACAA2, ACAT1 | **fadA** PP_2137 (+ paralog PP_2051) |

**Key architectural point:** steps 2 + 3 are fused in one multifunctional FadB polypeptide (EC 4.2.1.17 + 1.1.1.35 + 5.1.2.3 epimerase + 5.3.3.8 isomerase), and FadB (PP_2136) + FadA (PP_2137) are adjacent — a **fadBA operon** homologous to the E. coli α₂β₂ complex (PMID 1699931).

**Second architectural point (proteome scan):** a distinct **contiguous cassette PP_2214–PP_2217** supplies each activity as *separate* polypeptides — PP_2214 (3-hydroxyacyl-CoA dehydrogenase type-2, EC 1.1.1.35 → step 3), PP_2215 (thiolase EC 2.3.1.9 → step 4-type), PP_2216 (*acd*, acyl-CoA dehydrogenase family → step 1-type), PP_2217 (enoyl-CoA hydratase EC 4.2.1.17 → step 2). Its *acd* (cyclohexanecarbonyl-CoA / sulfinopropanoyl-CoA) annotation suggests specialization for alicyclic/branched or sulfur-containing acyl-CoAs, but it is a real β-oxidation-type operon, not noise. **PP_2214 is the only standalone EC 1.1.1.35 step-3 gene besides fadB and is missing from the candidate list.**

**Full proteome EC complement (taxon 160488):** step 1 = 3 ACADs (fadE PP_1893, PP_2437, PP_2793); step 2 = fadB, PP_2217, paaF (paa); step 3 = fadB, **PP_2214**, paaH PP_3282 (paa-specific); step 4 = fadA PP_2137, fadA PP_2051, bktB; activation = fadD PP_4549, PP_4550, **PP_2038**.

## 4. Candidate genes and evidence

**Core spiral — retain (high confidence):**
- **fadB PP_2136 / Q88L02** — *Swiss-Prot reviewed.* Fatty-acid-oxidation complex subunit α; covers **steps 2 & 3** (+ auxiliary epimerase/isomerase for unsaturated substrates). Highest-confidence assignment. → promote.
- **fadA PP_2137 / Q88L01** — *Swiss-Prot reviewed.* 3-ketoacyl-CoA thiolase (β subunit); **step 4**, EC 2.3.1.16. Operonic with fadB. → promote.
- **fadE PP_1893 / Q88LN6** — acyl-CoA dehydrogenase EC 1.3.8.7/1.3.8.8; primary **step 1** candidate; primary bucket already ppu00071. Homology-only. → promote.
- **fadD-I PP_4549 / fadD-II PP_4550** — EC 6.2.1.3; linked **activation** pair analogous to *P. aeruginosa* fadD1/fadD2 (long- vs short-chain; PMID 21042406, 23737986). → promote both.

**Core spiral — retain (paralogs, medium confidence):**
- **PP_2437 / PP_2793** — long-chain acyl-CoA dehydrogenases (EC 1.3.8.8); plausible chain-length isozymes for **step 1**.
- **fadA PP_2051 / Q88L84** — thiolase I (EC 2.3.1.16); plausible second **step-4** thiolase.
- **PP_2217 / Q88KS2** — enoyl-CoA hydratase (EC 4.2.1.17); possible standalone **step-2** ancillary (crotonase-family).
- **PP_3725 / Q88GJ7** — "acyl-CoA dehydrogenase," *no EC assigned*; weak step-1 candidate, needs review.

**Physiological context (direct KT2440 evidence that the spiral operates):** fatty acids and alkane-derived octanoate/decanoate are catabolized through β-oxidation, and its intermediate *trans*-2-enoyl-CoA feeds mcl-PHA synthesis (PMID 36763117, 41555335). This supports module activity even though per-gene biochemistry is absent.

## 5. Gaps, ambiguities, and likely over-annotations

**Not the core saturated spiral — reassign / candidate_uncertain:**
- **gcdH PP_0158** (glutaryl-CoA dehydrogenase, EC 1.3.8.6) — Lys/Trp degradation (ppu00380).
- **acd PP_2216** (3-sulfinopropanoyl-CoA desulfinase / cyclohexanecarbonyl-CoA dehydrogenase, EC 1.3.8.11/3.13.1.4) — sulfur/alicyclic CoA catabolism (ppu00410).
- **paaF PP_3284** (enoyl-CoA hydratase-isomerase) — phenylacetate (paa) catabolism.
- **frmA PP_1616** (S-hydroxymethylglutathione/formaldehyde dehydrogenase, EC 1.1.1.1/1.1.1.284) and **adhP PP_3839** (short-chain alcohol dehydrogenase, EC 1.1.1.1) — alcohol dehydrogenases, **not** the EC 1.1.1.35 3-hydroxyacyl-CoA dehydrogenase of step 3. Classic over-propagation via the shared "1.1.1.-" root.
- **alkT PP_5314** (rubredoxin-NAD⁺ reductase, EC 1.18.1.1) and **PP_5371** (rubredoxin/rubredoxin reductase) — electron-transfer partners of the **alkane hydroxylase** system, upstream of β-oxidation, not spiral enzymes.
- **EC 2.3.1.9 thiolases** — PP_2215, PP_3355, PP_0582, **yqeF PP_4636**, **bktB PP_3754**: acetoacetyl-CoA / PHA-biosynthetic thiolases (condensing direction). The degradative spiral thiolase is **EC 2.3.1.16**; only fadA/PP_2051 qualify. bktB in particular is a known PHA-pathway β-ketothiolase.

**Missing from candidate metadata (should be ADDED):**
- **PP_2214 (Q88KS5)** — 3-hydroxyacyl-CoA dehydrogenase type-2, EC 1.1.1.35: the genuine standalone **step-3** gene (candidate list had only the multifunctional fadB for this step; frmA/adhP were wrong). High priority to add.
- **PP_2038 (Q88L97)** — a third long-chain-fatty-acid–CoA ligase (EC 6.2.1.3): additional **activation** feeder.
- Note the **PP_2214–PP_2217 cassette** is coherent; PP_2215/PP_2216/PP_2217 are better curated as a specialized β-oxidation-type operon (candidate_uncertain, likely alicyclic/branched substrate) than as isolated over-annotations.
- **paaH PP_3282** (EC 1.1.1.35) sits beside paaF PP_3284 → confirms a phenylacetate (paa) cluster; keep both out of the core spiral.

**Ambiguities / caveats for curation:**
- Broad EC/GO on acyl-CoA-dehydrogenase and thiolase superfamilies drives false membership; filter step-1 by EC 1.3.8.7/1.3.8.8 and step-4 by EC 2.3.1.16.
- "Reviewed" status of fadBA is UniRule-based, **not experimental for KT2440**; treat as high-confidence homology, not proof.
- Chain-length specialization of fadE/PP_2437/PP_2793 and fadD-I/II is inferred from *Pseudomonas* orthologs, not measured in KT2440.

## 6. Module and GO-curation recommendations

| Module element | Recommended status | Rationale |
|---|---|---|
| Step 1 acyl-CoA dehydrogenase | **covered** | fadE PP_1893 + paralogs; multiple candidates, homology-strong |
| Step 2 enoyl-CoA hydratase | **covered** | fadB PP_2136 (Swiss-Prot), +PP_2217 |
| Step 3 3-hydroxyacyl-CoA DH | **covered** | fadB PP_2136 (Swiss-Prot) + standalone **PP_2214** (EC 1.1.1.35, add to metadata) |
| Step 4 3-ketoacyl-CoA thiolase | **covered** | fadA PP_2137 (Swiss-Prot) + PP_2051 |
| Activation feeder (EC 6.2.1.3) | **covered** | fadD-I/II PP_4549/4550 + dispersed paralogs |
| Mis-bucketed dehydrogenases/thiolases/redox | **candidate_uncertain → reassign** | belong to gcdH/acd/paa/alk/PHA modules |
| Eukaryotic subunit mapping (MTP α/β) | **module_needs_revision** | bacterial FadBA ≠ MTP; add bacterial-analog note |

- **Module boundary revision:** the generic module's subunit-level scaffold (HADHA/HADHB split, ECHS1/HADH vs MTP) is **wrong for bacteria**. Add a species-aware note that steps 2+3 are fused in one FadB polypeptide and step 4 is the operonic FadA; do not require MTP-specific GO terms.
- **GO terms:** existing GO MF terms suffice (GO:0016508/0016509-type acyl-CoA dehydrogenase, GO:0004300 enoyl-CoA hydratase, GO:0003857 3-hydroxyacyl-CoA dehydrogenase, GO:0003988 acetyl-CoA C-acyltransferase, GO:0004467 long-chain fatty-acid–CoA ligase). No new GO request appears necessary; use CC "cytoplasm," not mitochondrion.
- **No new module document needed** for the saturated spiral beyond the bacterial-analog annotation; the unsaturated auxiliary cassette remains separately curated.

## 7. Genes to promote to full `fetch-gene` review

1. **PP_2136 (fadB)** — anchor, steps 2+3; confirm operon and multifunctionality.
2. **PP_2137 (fadA)** — anchor, step 4.
3. **PP_1893 (fadE)** — primary step-1 dehydrogenase.
4. **PP_4549 / PP_4550 (fadD-I/II)** — activation pair; resolve chain-length roles vs *P. aeruginosa* fadD1/fadD2.
5. **PP_2051 (thiolase I)** and **PP_2437 / PP_2793** (long-chain acyl-CoA DHs) — resolve paralog redundancy and chain-length coverage.
6. **PP_2214 (Q88KS5)** — add to metadata and review as the standalone step-3 dehydrogenase; review the **PP_2214–PP_2217 cassette** as a unit to determine substrate specialization. Also add/review **PP_2038 (Q88L97)** as a third acyl-CoA ligase.
*(Down-rank — reassign to their primary buckets rather than promote:)* gcdH, acd, paaF, frmA, adhP, alkT, PP_5371, PP_2215, PP_3355, PP_0582, yqeF, bktB.

## 8. Key references

- DiRusso CC (1990) *J Bacteriol* — E. coli fadBA operon; α₂β₂ multienzyme complex; homology to eukaryotic trifunctional enzyme. **PMID 1699931.**
- Kang Y et al. (2010) — multiple FadD acyl-CoA synthetases; fadD1 long-chain / fadD2 short-chain in *P. aeruginosa*. **PMID 21042406.**
- Zarzycki-Siek J et al. (2013) — six FadD homologs in *P. aeruginosa*; chain-length division of labor. **PMID 23737986.**
- Liu Q et al. (2023) *Appl Microbiol Biotechnol* — β-oxidation–PHA relationship in *P. putida* KT2440 revisited; PhaJ homologs. **PMID 36763117.**
- Palacios-Ferrer A et al. (2026) — alkane→octanoate/decanoate enter β-oxidation in *P. putida*. **PMID 41555335.**
- Sathesh-Prabu C et al. (2025) — *E. coli* vs *P. putida* KT2440 as fatty-acid cell factories. **PMID 40706765.**
- Dong H et al. (2021) — cryptic FabF2 / FA-synthesis vs β-oxidation competition in *P. putida* F1. **PMID 34181948.**

---

### Uncertainty & species-transfer notes
- **Direct KT2440 evidence:** functional β-oxidation operates (physiology/engineering; PMID 36763117, 41555335). Per-gene biochemistry is **absent**; all 22 annotations are homology-inferred.
- **Same-genus transfer (moderate–strong):** FadD chain-length specialization from *P. aeruginosa* (PMID 21042406/23737986).
- **Family-level transfer only (weak on subunit identity):** eukaryotic MTP/ACAD/thiolase subunit assignments — use EC/family, not orthology.


## Artifacts

- [OpenScientist final report](PSEPK__fatty_acid_beta_oxidation__ppu00071-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__fatty_acid_beta_oxidation__ppu00071-deep-research-openscientist_artifacts/final_report.pdf)