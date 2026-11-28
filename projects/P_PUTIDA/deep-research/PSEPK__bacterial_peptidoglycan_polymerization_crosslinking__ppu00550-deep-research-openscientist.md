---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:59:49.652951'
end_time: '2026-08-31T23:21:35.605809'
duration_seconds: 1305.95
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial peptidoglycan polymerization and crosslinking
  module_summary: A reusable bacterial module downstream of lipid II export. It separates
    septal and lateral-wall SEDS-bPBP synthases from class-A bifunctional PBPs, monofunctional
    glycan polymerases, and D,D-carboxypeptidase-mediated stem peptide maturation.
    The module does not include cytoplasmic precursor synthesis, lipid II flipping,
    or peptidoglycan recycling.
  module_outline: "- Bacterial peptidoglycan polymerization and crosslinking\n  -\
    \ 1. septal glycan polymerization and peptide crosslinking\n  - Septal FtsW-FtsI\
    \ peptidoglycan synthesis\n    - 1. septal glycan polymerization\n    - FtsW glycan\
    \ polymerization\n      - FtsW peptidoglycan glycosyltransferase (molecular player:\
    \ FtsW septal SEDS glycosyltransferases; activity or role: peptidoglycan glycosyltransferase\
    \ activity)\n    - 2. septal D,D-transpeptidation\n    - FtsI peptide crosslinking\n\
    \      - FtsI D,D-transpeptidase (molecular player: FtsI/PBP3 septal D,D-transpeptidases)\n\
    \  - 2. lateral-wall glycan polymerization and peptide crosslinking\n  - RodA-MrdA\
    \ peptidoglycan synthesis\n    - 1. lateral-wall glycan polymerization\n    -\
    \ RodA glycan polymerization\n      - RodA peptidoglycan glycosyltransferase (molecular\
    \ player: RodA/MrdB lateral-wall SEDS glycosyltransferases; activity or role:\
    \ peptidoglycan glycosyltransferase activity)\n    - 2. lateral-wall D,D-transpeptidation\n\
    \    - MrdA peptide crosslinking\n      - Alternative versions by enzyme paralog:\
    \ MrdA/PBP2 paralogs\n        - MrdA-I\n          - MrdA-I D,D-transpeptidase\
    \ (molecular player: MrdA/PBP2 D,D-transpeptidases)\n        - MrdA-II\n     \
    \     - MrdA-II D,D-transpeptidase (molecular player: MrdA/PBP2 D,D-transpeptidases)\n\
    \  - 3. bifunctional glycan polymerization and peptide crosslinking\n  - Class-A\
    \ PBP peptidoglycan synthesis\n    - Alternative versions by enzyme family member:\
    \ Class-A PBP variants\n      - PBP1A/MrcA\n        - PBP1A bifunctional synthase\
    \ (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan\
    \ glycosyltransferase activity)\n      - PBP1B/MrcB\n        - PBP1B bifunctional\
    \ synthase (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan\
    \ glycosyltransferase activity)\n      - PbpC\n        - PbpC peptidoglycan synthase\
    \ (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan\
    \ glycosyltransferase activity)\n  - 4. monofunctional glycan polymerization\n\
    \  - MtgA glycan polymerization\n    - MtgA peptidoglycan glycosyltransferase\
    \ (molecular player: monofunctional biosynthetic peptidoglycan glycosyltransferases;\
    \ activity or role: peptidoglycan glycosyltransferase activity)\n  - 5. pentapeptide\
    \ stem trimming\n  - DacA D,D-carboxypeptidation\n    - DacA D,D-carboxypeptidase\
    \ (molecular player: DacA low-molecular-mass D,D-carboxypeptidases; activity or\
    \ role: serine-type D-Ala-D-Ala carboxypeptidase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00550
  pathway_id: ppu00550
  pathway_name: Peptidoglycan biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00550 with 10 primary genes; module
    area: lipid_cell_envelope_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '23'
  candidate_genes: '- pbpC: PP_0572 | Q88QC2 | peptidoglycan glycosyltransferase (EC
    2.4.99.28) (EC 2.4.99.28; primary bucket kegg:ppu00550)

    - murA: PP_0964 | Q88P88 | UDP-N-acetylglucosamine 1-carboxyvinyltransferase (EC
    2.5.1.7) (Enoylpyruvate transferase) (UDP-N-acetylglucosamine enolpyruvyl transferase)
    (EPT) (EC 2.5.1.7; primary bucket kegg:ppu00550)

    - ftsI: PP_1331 | Q88N82 | Peptidoglycan D,D-transpeptidase FtsI (EC 3.4.16.4)
    (Penicillin-binding protein 3) (PBP-3) (EC 3.4.16.4; primary bucket kegg:ppu01501)

    - murE: PP_1332 | Q88N81 | UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate
    ligase (EC 6.3.2.13) (Meso-A2pm-adding enzyme) (Meso-diaminopimelate-adding enzyme)
    (UDP-MurNAc-L-Ala-D-Glu:meso-diaminopimelate ligase) (UDP-MurNAc-tripeptide synthetase)
    (UDP-N-acetylmuramyl-tripeptide synthetase) (EC 6.3.2.13; primary bucket kegg:ppu00300)

    - murF: PP_1333 | Q88N80 | UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine
    ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) (EC 6.3.2.10; primary
    bucket kegg:ppu01502)

    - mraY: PP_1334 | Q88N79 | Phospho-N-acetylmuramoyl-pentapeptide-transferase (EC
    2.7.8.13) (UDP-MurNAc-pentapeptide phosphotransferase) (EC 2.7.8.13; primary bucket
    kegg:ppu01502)

    - murD: PP_1335 | Q88N78 | UDP-N-acetylmuramoylalanine--D-glutamate ligase (EC
    6.3.2.9) (D-glutamic acid-adding enzyme) (UDP-N-acetylmuramoyl-L-alanyl-D-glutamate
    synthetase) (EC 6.3.2.9; primary bucket kegg:ppu00470)

    - ftsW: PP_1336 | Q88N77 | Probable peptidoglycan glycosyltransferase FtsW (PGT)
    (EC 2.4.99.28) (Cell division protein FtsW) (Cell wall polymerase) (Peptidoglycan
    polymerase) (PG polymerase) (EC 2.4.99.28; primary bucket kegg:ppu00550)

    - murG: PP_1337 | Q88N76 | UDP-N-acetylglucosamine--N-acetylmuramyl-(pentapeptide)
    pyrophosphoryl-undecaprenol N-acetylglucosamine transferase (EC 2.4.1.227) (Undecaprenyl-PP-MurNAc-pentapeptide-UDPGlcNAc
    GlcNAc transferase) (EC 2.4.1.227; primary bucket kegg:ppu01502)

    - murC: PP_1338 | Q88N75 | UDP-N-acetylmuramate--L-alanine ligase (EC 6.3.2.8)
    (UDP-N-acetylmuramoyl-L-alanine synthetase) (EC 6.3.2.8; primary bucket kegg:ppu00550)

    - ddlB: PP_1339 | Q88N74 | D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala
    ligase B) (D-alanylalanine synthetase B) (EC 6.3.2.4; primary bucket kegg:ppu01502)

    - uppS: PP_1595 | Q88MH6 | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate
    specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl
    diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase)
    (EC 2.5.1.31; primary bucket kegg:ppu00900)

    - murB: PP_1904 | Q88LM5 | UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98)
    (UDP-N-acetylmuramate dehydrogenase) (EC 1.3.1.98; primary bucket kegg:ppu00550)

    - dacB: PP_2098 | Q88L37 | D-alanyl-D-alanine carboxypeptidase (primary bucket
    kegg:ppu00550)

    - uppP: PP_2862 | Q88IY7 | Undecaprenyl-diphosphatase (EC 3.6.1.27) (Bacitracin
    resistance protein) (Undecaprenyl pyrophosphate phosphatase) (EC 3.6.1.27; primary
    bucket kegg:ppu00552)

    - mrdA-I: PP_3741 | Q88GI2 | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4)
    (Penicillin-binding protein 2) (PBP-2) (EC 3.4.16.4; primary bucket kegg:ppu01501)

    - ddlA: PP_4346 | Q88EV6 | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala
    ligase A) (D-alanylalanine synthetase A) (EC 6.3.2.4; primary bucket kegg:ppu01502)

    - mrcB: PP_4683 | Q88DY5 | Penicillin-binding protein 1B (PBP-1b) (PBP1b) (Murein
    polymerase) (primary bucket kegg:ppu00550)

    - dacA: PP_4803 | Q88DM2 | serine-type D-Ala-D-Ala carboxypeptidase (EC 3.4.16.4)
    (EC 3.4.16.4; primary bucket kegg:ppu00550)

    - mrdB: PP_4806 | Q88DL9 | Peptidoglycan glycosyltransferase MrdB (PGT) (EC 2.4.99.28)
    (Cell elongation protein RodA) (Cell wall polymerase) (Peptidoglycan polymerase)
    (PG polymerase) (EC 2.4.99.28; primary bucket kegg:ppu00550)

    - mrdA-II: PP_4807 | Q88DL8 | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4)
    (Penicillin-binding protein 2) (PBP-2) (EC 3.4.16.4; primary bucket kegg:ppu01501)

    - mrcA: PP_5084 | Q88CU6 | Penicillin-binding protein 1A (EC 2.4.99.28) (EC 3.4.16.4)
    (EC 2.4.99.28; 3.4.16.4; primary bucket kegg:ppu01501)

    - mtgA: PP_5107 | Q88CS3 | Biosynthetic peptidoglycan transglycosylase (EC 2.4.99.28)
    (Glycan polymerase) (Peptidoglycan glycosyltransferase MtgA) (PGT) (EC 2.4.99.28;
    primary bucket kegg:ppu00550)'
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_peptidoglycan_polymerization_crosslinking__ppu00550-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_peptidoglycan_polymerization_crosslinking__ppu00550-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial peptidoglycan polymerization and crosslinking in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00550
- Resolved ID: ppu00550
- Resolved name: Peptidoglycan biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00550 with 10 primary genes; module area: lipid_cell_envelope_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 23

- pbpC: PP_0572 | Q88QC2 | peptidoglycan glycosyltransferase (EC 2.4.99.28) (EC 2.4.99.28; primary bucket kegg:ppu00550)
- murA: PP_0964 | Q88P88 | UDP-N-acetylglucosamine 1-carboxyvinyltransferase (EC 2.5.1.7) (Enoylpyruvate transferase) (UDP-N-acetylglucosamine enolpyruvyl transferase) (EPT) (EC 2.5.1.7; primary bucket kegg:ppu00550)
- ftsI: PP_1331 | Q88N82 | Peptidoglycan D,D-transpeptidase FtsI (EC 3.4.16.4) (Penicillin-binding protein 3) (PBP-3) (EC 3.4.16.4; primary bucket kegg:ppu01501)
- murE: PP_1332 | Q88N81 | UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase (EC 6.3.2.13) (Meso-A2pm-adding enzyme) (Meso-diaminopimelate-adding enzyme) (UDP-MurNAc-L-Ala-D-Glu:meso-diaminopimelate ligase) (UDP-MurNAc-tripeptide synthetase) (UDP-N-acetylmuramyl-tripeptide synthetase) (EC 6.3.2.13; primary bucket kegg:ppu00300)
- murF: PP_1333 | Q88N80 | UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) (EC 6.3.2.10; primary bucket kegg:ppu01502)
- mraY: PP_1334 | Q88N79 | Phospho-N-acetylmuramoyl-pentapeptide-transferase (EC 2.7.8.13) (UDP-MurNAc-pentapeptide phosphotransferase) (EC 2.7.8.13; primary bucket kegg:ppu01502)
- murD: PP_1335 | Q88N78 | UDP-N-acetylmuramoylalanine--D-glutamate ligase (EC 6.3.2.9) (D-glutamic acid-adding enzyme) (UDP-N-acetylmuramoyl-L-alanyl-D-glutamate synthetase) (EC 6.3.2.9; primary bucket kegg:ppu00470)
- ftsW: PP_1336 | Q88N77 | Probable peptidoglycan glycosyltransferase FtsW (PGT) (EC 2.4.99.28) (Cell division protein FtsW) (Cell wall polymerase) (Peptidoglycan polymerase) (PG polymerase) (EC 2.4.99.28; primary bucket kegg:ppu00550)
- murG: PP_1337 | Q88N76 | UDP-N-acetylglucosamine--N-acetylmuramyl-(pentapeptide) pyrophosphoryl-undecaprenol N-acetylglucosamine transferase (EC 2.4.1.227) (Undecaprenyl-PP-MurNAc-pentapeptide-UDPGlcNAc GlcNAc transferase) (EC 2.4.1.227; primary bucket kegg:ppu01502)
- murC: PP_1338 | Q88N75 | UDP-N-acetylmuramate--L-alanine ligase (EC 6.3.2.8) (UDP-N-acetylmuramoyl-L-alanine synthetase) (EC 6.3.2.8; primary bucket kegg:ppu00550)
- ddlB: PP_1339 | Q88N74 | D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala ligase B) (D-alanylalanine synthetase B) (EC 6.3.2.4; primary bucket kegg:ppu01502)
- uppS: PP_1595 | Q88MH6 | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase) (EC 2.5.1.31; primary bucket kegg:ppu00900)
- murB: PP_1904 | Q88LM5 | UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98) (UDP-N-acetylmuramate dehydrogenase) (EC 1.3.1.98; primary bucket kegg:ppu00550)
- dacB: PP_2098 | Q88L37 | D-alanyl-D-alanine carboxypeptidase (primary bucket kegg:ppu00550)
- uppP: PP_2862 | Q88IY7 | Undecaprenyl-diphosphatase (EC 3.6.1.27) (Bacitracin resistance protein) (Undecaprenyl pyrophosphate phosphatase) (EC 3.6.1.27; primary bucket kegg:ppu00552)
- mrdA-I: PP_3741 | Q88GI2 | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) (EC 3.4.16.4; primary bucket kegg:ppu01501)
- ddlA: PP_4346 | Q88EV6 | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala ligase A) (D-alanylalanine synthetase A) (EC 6.3.2.4; primary bucket kegg:ppu01502)
- mrcB: PP_4683 | Q88DY5 | Penicillin-binding protein 1B (PBP-1b) (PBP1b) (Murein polymerase) (primary bucket kegg:ppu00550)
- dacA: PP_4803 | Q88DM2 | serine-type D-Ala-D-Ala carboxypeptidase (EC 3.4.16.4) (EC 3.4.16.4; primary bucket kegg:ppu00550)
- mrdB: PP_4806 | Q88DL9 | Peptidoglycan glycosyltransferase MrdB (PGT) (EC 2.4.99.28) (Cell elongation protein RodA) (Cell wall polymerase) (Peptidoglycan polymerase) (PG polymerase) (EC 2.4.99.28; primary bucket kegg:ppu00550)
- mrdA-II: PP_4807 | Q88DL8 | Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Penicillin-binding protein 2) (PBP-2) (EC 3.4.16.4; primary bucket kegg:ppu01501)
- mrcA: PP_5084 | Q88CU6 | Penicillin-binding protein 1A (EC 2.4.99.28) (EC 3.4.16.4) (EC 2.4.99.28; 3.4.16.4; primary bucket kegg:ppu01501)
- mtgA: PP_5107 | Q88CS3 | Biosynthetic peptidoglycan transglycosylase (EC 2.4.99.28) (Glycan polymerase) (Peptidoglycan glycosyltransferase MtgA) (PGT) (EC 2.4.99.28; primary bucket kegg:ppu00550)

## Generic Module Context

### Working Scope

A reusable bacterial module downstream of lipid II export. It separates septal and lateral-wall SEDS-bPBP synthases from class-A bifunctional PBPs, monofunctional glycan polymerases, and D,D-carboxypeptidase-mediated stem peptide maturation. The module does not include cytoplasmic precursor synthesis, lipid II flipping, or peptidoglycan recycling.

### Provisional Biological Outline

- Bacterial peptidoglycan polymerization and crosslinking
  - 1. septal glycan polymerization and peptide crosslinking
  - Septal FtsW-FtsI peptidoglycan synthesis
    - 1. septal glycan polymerization
    - FtsW glycan polymerization
      - FtsW peptidoglycan glycosyltransferase (molecular player: FtsW septal SEDS glycosyltransferases; activity or role: peptidoglycan glycosyltransferase activity)
    - 2. septal D,D-transpeptidation
    - FtsI peptide crosslinking
      - FtsI D,D-transpeptidase (molecular player: FtsI/PBP3 septal D,D-transpeptidases)
  - 2. lateral-wall glycan polymerization and peptide crosslinking
  - RodA-MrdA peptidoglycan synthesis
    - 1. lateral-wall glycan polymerization
    - RodA glycan polymerization
      - RodA peptidoglycan glycosyltransferase (molecular player: RodA/MrdB lateral-wall SEDS glycosyltransferases; activity or role: peptidoglycan glycosyltransferase activity)
    - 2. lateral-wall D,D-transpeptidation
    - MrdA peptide crosslinking
      - Alternative versions by enzyme paralog: MrdA/PBP2 paralogs
        - MrdA-I
          - MrdA-I D,D-transpeptidase (molecular player: MrdA/PBP2 D,D-transpeptidases)
        - MrdA-II
          - MrdA-II D,D-transpeptidase (molecular player: MrdA/PBP2 D,D-transpeptidases)
  - 3. bifunctional glycan polymerization and peptide crosslinking
  - Class-A PBP peptidoglycan synthesis
    - Alternative versions by enzyme family member: Class-A PBP variants
      - PBP1A/MrcA
        - PBP1A bifunctional synthase (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan glycosyltransferase activity)
      - PBP1B/MrcB
        - PBP1B bifunctional synthase (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan glycosyltransferase activity)
      - PbpC
        - PbpC peptidoglycan synthase (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan glycosyltransferase activity)
  - 4. monofunctional glycan polymerization
  - MtgA glycan polymerization
    - MtgA peptidoglycan glycosyltransferase (molecular player: monofunctional biosynthetic peptidoglycan glycosyltransferases; activity or role: peptidoglycan glycosyltransferase activity)
  - 5. pentapeptide stem trimming
  - DacA D,D-carboxypeptidation
    - DacA D,D-carboxypeptidase (molecular player: DacA low-molecular-mass D,D-carboxypeptidases; activity or role: serine-type D-Ala-D-Ala carboxypeptidase activity)

### Known Relationships Among Steps

No explicit connections.

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

# Bacterial Peptidoglycan Polymerization and Crosslinking in *Pseudomonas putida* KT2440 — Module/Pathway/Taxon Review

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00550 "Peptidoglycan biosynthesis" — resolved to the reusable module *Bacterial peptidoglycan polymerization and crosslinking* (lipid II-downstream)
**Module area:** lipid_cell_envelope_metabolism

---

## 1. Executive Summary

The lipid II-downstream peptidoglycan (PG) polymerization/crosslinking module is **fully satisfiable** in *P. putida* KT2440. Every canonical step class of the generic module maps to at least one candidate gene whose role is corroborated by conserved Pfam domain architecture: septal SEDS–bPBP synthesis (FtsW/FtsI), lateral-wall SEDS–bPBP synthesis (MrdB/RodA plus PBP2/MrdA), class-A bifunctional PBP synthesis (PBP1A/MrcA, PBP1B/MrcB, PbpC), monofunctional glycan polymerization (MtgA), and pentapeptide stem trimming (DacA/PBP5 D,D-carboxypeptidase). No canonical step is a genuine gap in the target organism.

However, the KEGG-derived candidate list requires substantial curation before it can drive automated module satisfiability. Three structural issues dominate: (i) **scope contamination** — only 11 of the 23 candidate genes actually belong to the polymerization/crosslinking module; the remaining 12 are cytoplasmic Mur/Ddl precursor-synthesis enzymes or undecaprenyl-carrier metabolism enzymes that the module scope explicitly excludes; (ii) **paralog multiplicity** — KT2440 carries **two genuine PBP2/MrdA D,D-transpeptidase paralogs** (PP_3741 and PP_4807, 73.5% identical), which must both be represented rather than collapsed; and (iii) **annotation completeness/misassignment** — pbpC has an incomplete EC (only its glycosyltransferase activity is captured, not its transpeptidase), and dacB (PP_2098) is a PBP4/peptidase-S13 D,D-endopeptidase that does *not* satisfy the DacA/PBP5 carboxypeptidase step and should not be conflated with it.

Two module-revision needs emerged. First, the generic module has no node for the **PBP4-class D,D-endopeptidase** activity that dacB encodes, which is functionally relevant in *Pseudomonas* β-lactam/AmpC biology. Second, the module omits **L,D-transpeptidation** (3-3 crosslink formation) entirely; a direct proteome scan confirms KT2440 encodes two YkuD-family L,D-transpeptidases (PP_1451 and PP_2320) that are absent from the candidate list — a documented module gap rather than an organism gap. Critically, **all in-scope genes are homology-inferred (UniProt evidence level PE=3) with no KT2440-specific experimental characterization**, so all functional assignments carry species-transfer uncertainty. The two MrdA/PBP2 paralogs should be flagged `candidate_uncertain` and promoted to full gene review.

---

## 2. Target-Organism Pathway Definition

*P. putida* KT2440 is a Gram-negative γ-proteobacterium with DAP-type (A1γ) peptidoglycan, so its PG polymerization/crosslinking machinery follows the canonical two-machine (divisome + elongasome) plus class-A PBP architecture.

### What is included

The module covers the **membrane-associated, lipid II-downstream reactions** that build and crosslink the sacculus:

- **Glycan-chain polymerization (glycosyltransfer, EC 2.4.99.28):** transfer of the disaccharide-pentapeptide from lipid II onto growing glycan strands, performed by two structurally unrelated enzyme classes — **SEDS-family polymerases** (FtsW, RodA/MrdB; Pfam PF01098) and the **GT51/Transglycosylase domains of class-A PBPs** plus the standalone monofunctional transglycosylase MtgA (Pfam PF00912). SEDS enzymes add lipid II monomers to the reducing end of the strand ([PMID: 31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/)).
- **Peptide crosslinking (D,D-transpeptidation, 4→3 crosslink; EC 3.4.16.4):** by **class-B PBPs (bPBPs)** — FtsI/PBP3 (division) and MrdA/PBP2 (elongation) — and by the transpeptidase (PF00905) domains of class-A PBPs.
- **Stem-peptide maturation:** **D,D-carboxypeptidase** trimming of the terminal D-Ala from pentapeptide stems (serine-type, S11/PBP5; DacA) to control crosslink density.

### What must be kept separate (neighboring pathways)

The module scope statement explicitly excludes, and this review confirms should be curated **out of this bucket**:

- **Cytoplasmic precursor synthesis** — the Mur ligase pathway (MurA, MurB, MurC, MurD, MurE, MurF), MraY, MurG, and the D-Ala–D-Ala ligases (DdlA, DdlB), which build UDP-MurNAc-pentapeptide and lipid II *before* export (KEGG ppu00300/00470/01502).
- **Undecaprenyl-carrier metabolism** — UppS (undecaprenyl-diphosphate synthase; ppu00900) and UppP (undecaprenyl-diphosphatase; ppu00552), which regenerate the lipid carrier.
- **Lipid II flipping** (MurJ/Amj) and **PG recycling** (AmpD/AmpG/NagZ/Mpl) — both explicitly outside scope.

### Alternate names / database definitions

- KEGG map **ppu00550** ("Peptidoglycan biosynthesis") is a *whole-map* bucket, broader than this mechanistic module — the reason 12 of the 23 candidates are out-of-scope.
- The machinery is referred to as the **divisome** (FtsW-FtsI), the **elongasome / Rod system** (RodA-PBP2), the **class-A PBPs** (aPBPs), and collectively as **penicillin-binding proteins (PBPs)** / "murein synthases."
- GO anchors: peptidoglycan glycosyltransferase activity (GO:0008955); serine-type D-Ala-D-Ala carboxypeptidase activity (GO:0009002); peptidoglycan biosynthetic process (GO:0009252).

---

## 3. Expected Step Model and Satisfiability

The generic module defines five step classes. All are covered in KT2440:

| Module step | Enzyme class | KT2440 candidate gene(s) | Status |
|---|---|---|---|
| 1. Septal glycan polymerization | FtsW SEDS GTase | **ftsW** PP_1336 | Covered |
| 1. Septal D,D-transpeptidation | FtsI/PBP3 bPBP | **ftsI** PP_1331 | Covered |
| 2. Lateral glycan polymerization | RodA/MrdB SEDS GTase | **mrdB** PP_4806 | Covered |
| 2. Lateral D,D-transpeptidation | MrdA/PBP2 bPBP | **mrdA-II** PP_4807 (operonic) + **mrdA-I** PP_3741 (paralog) | Covered (2 paralogs) |
| 3. Bifunctional GTase + TPase | Class-A PBPs | **mrcA** PP_5084, **mrcB** PP_4683, **pbpC** PP_0572 | Covered |
| 4. Monofunctional glycan polymerization | Standalone GTase | **mtgA** PP_5107 | Covered |
| 5. Pentapeptide stem trimming | DacA/PBP5 D,D-CPase | **dacA** PP_4803 | Covered |

**Steps missing from the generic module but present in the organism (module gaps, not organism gaps):**

- **PBP4-class D,D-endopeptidase** — dacB (PP_2098) is a peptidase-S13/PBP4 enzyme with D,D-endo/carboxypeptidase activity; the generic module has no node for it.
- **L,D-transpeptidation (3-3 crosslink)** — encoded by YkuD-family PP_1451 and PP_2320, absent from the candidate list and unmodeled.

**Steps probably not expected / not applicable:** None of the five canonical steps is absent. There is no evidence for loss of any elongasome or divisome component in KT2440.

---

## 4. Candidate Genes and Evidence

All 11 in-scope assignments below are supported by **conserved Pfam domain architecture** (verified from UniProt) and pathway-database placement; **none has direct KT2440 experimental characterization** (all UniProt PE=3, inferred from homology). Paralog relationships were computed by global alignment.

### 4.1 In-scope genes (11) — the actual module

| Gene | Locus | UniProt | Length | Pfam architecture | Module role | Curation note |
|---|---|---|---|---|---|---|
| ftsW | PP_1336 | Q88N77 | — | PF01098 (10 TM) | Septal SEDS GTase | High confidence; divisome partner of FtsI |
| ftsI | PP_1331 | Q88N82 | — | PF03717 + PF00905, 1 TM | Septal bPBP (PBP3) TPase | ~38–39% id to PBP2; aztreonam/ceftazidime target |
| mrdB/rodA | PP_4806 | Q88DL9 | — | PF01098 (9 TM) | Lateral SEDS GTase | Operonic upstream of mrdA-II; Rod system |
| mrdA-II | PP_4807 | Q88DL8 | 629 aa | PF03717 + PF00905, 1 TM | Lateral bPBP (PBP2) TPase | Canonical operonic elongasome PBP2 |
| mrdA-I | PP_3741 | Q88GI2 | 631 aa | PF03717 + PF00905, 1 TM | Lateral bPBP (PBP2) TPase | **Second, dispersed PBP2 paralog** |
| mrcA | PP_5084 | Q88CU6 | — | PCB_OB + Transgly + Transpeptidase | Class-A PBP1A | Bifunctional; EC 2.4.99.28 + 3.4.16.4 (correct) |
| mrcB | PP_4683 | Q88DY5 | — | Transgly + Transpeptidase + UB2H | Class-A PBP1B | **No EC listed — add bifunctional EC pair** |
| pbpC | PP_0572 | Q88QC2 | 784 aa | PF00912 + PF00905 + PF06832 | Class-A PBP1C | **EC 3.4.16.4 TPase not captured** |
| mtgA | PP_5107 | Q88CS3 | 236 aa | PF00912 only | Monofunctional GTase | Accessory/dispensable |
| dacA | PP_4803 | Q88DM2 | — | PF00768 (S11) + PF07943 | DacA D,D-carboxypeptidase | Satisfies stem-trimming step |

**SEDS glycosyltransferases (ftsW, mrdB).** Both carry PF01098 with the expected transmembrane counts (10 TM and 9 TM). FtsW is the septal SEDS polymerase partnering FtsI; MrdB/RodA sits immediately upstream of mrdA-II in the canonical *mrd/rod* operon and is the lateral-wall SEDS polymerase of the Rod system/elongasome. Transfer from *E. coli* and general bacterial SEDS biology is **strong** because these are universally conserved, essential enzymes.

**PBP2 paralogs (Finding F002).** A global Needleman–Wunsch alignment gives **73.5% identity** between MrdA-I (PP_3741, 631 aa) and MrdA-II (PP_4807, 629 aa). Both share the canonical PBP2 architecture (PF03717 PBP_dimer + PF00905 Transpeptidase, single N-terminal TM anchor) and are only ~38–39% identical to FtsI/PBP3 (PP_1331), confirming both are **elongasome-type PBP2, not divisome FtsI**. PP_4807 sits immediately downstream of mrdB/rodA (the "housekeeping" elongation PBP2); PP_3741 is a genome-dispersed second copy. This is a genuine gene duplication, not a mis-split annotation. The physiological division of labor (redundant, specialized, or condition-specific) is **unknown in KT2440** — these are the strongest candidates for `candidate_uncertain`.

**Class-A bifunctional PBPs (mrcA, mrcB, pbpC).** MrcA/PBP1A is annotated with both EC 2.4.99.28 and 3.4.16.4 — a correctly-annotated bifunctional template. MrcB/PBP1B (Transgly + Transpeptidase + UB2H/PF14814) is unambiguously bifunctional by architecture but carries **no EC in the metadata**. PbpC/PBP1C (PF00912 + PF00905 + PF06832 BiPBP_C) is a full class-A PBP whose EC lists **only the glycosyltransferase (2.4.99.28)**, omitting the transpeptidase (Finding F003). In *E. coli*, PBP1C is a minor/low-activity synthase, so exact functional transfer to KT2440 is **uncertain** even though the structural call is clear.

**Monofunctional transglycosylase (mtgA).** PF00912-only, 236 aa, EC 2.4.99.28 — an accessory glycan polymerase, individually dispensable in model bacteria. Activity transfer is **strong**; physiological necessity is **moderate**.

**D,D-carboxypeptidase (dacA).** PF00768 (Peptidase_S11) + PF07943 (PBP5_C), EC 3.4.16.4 — the LMM D,D-carboxypeptidase (PBP5) that satisfies the module's stem-trimming step. Transfer **strong**.

### 4.2 Out-of-scope genes (12) — should be removed from this module

Correctly PG-related but belonging to **cytoplasmic precursor synthesis** or **carrier metabolism**, both explicitly excluded by the module scope (Finding F001):

- **Mur ligases / precursor:** murA (PP_0964), murB (PP_1904), murC (PP_1338), murD (PP_1335), murE (PP_1332), murF (PP_1333), murG (PP_1337)
- **First membrane step (pre-export):** mraY (PP_1334)
- **D-Ala–D-Ala ligases:** ddlA (PP_4346), ddlB (PP_1339)
- **Undecaprenyl carrier:** uppS (PP_1595), uppP (PP_2862)

These should be reassigned to their correct buckets rather than counted toward module satisfiability.

### 4.3 dacB — distinct enzyme, not the DacA step (Findings F003, F004)

**dacB (PP_2098, Q88L37, 470 aa)** carries Pfam **PF02113 (Peptidase_S13)**, the **PBP4 family** (D,D-endopeptidase / D,D-carboxypeptidase). This is biochemically and structurally distinct from dacA (PP_4803, PF00768/Peptidase_S11, PBP5-type). The generic module's single "DacA D,D-carboxypeptidation" step is satisfied by **dacA**, not dacB. dacB represents an additional, un-modeled activity that is functionally important in *Pseudomonas* — LMW-PBP (PBP4/dacB) inactivation drives AmpC β-lactamase overexpression in *P. aeruginosa* ([PMID: 41206063](https://pubmed.ncbi.nlm.nih.gov/41206063/)). A pipeline that maps dacB to the DacA step by the generic "D,D-carboxypeptidase" label would be in error.

---

## 5. Mechanistic Model / Interpretation

The KT2440 PG polymerization/crosslinking machinery follows the canonical Gram-negative two-machine architecture, with lineage-specific paralog expansion at PBP2:

```
                        lipid II (from cytoplasmic Mur pathway — OUT OF SCOPE)
                                     |
        ┌────────────────────────────┼────────────────────────────┐
        |                            |                            |
   DIVISOME (septal)           ELONGASOME (lateral)          CLASS-A PBPs
   ┌───────────────┐           ┌───────────────┐            (bifunctional, dispersed)
   │FtsW  (PP_1336)│ GTase     │MrdB/RodA(4806)│ GTase      MrcA/PBP1A (PP_5084) GT+TP
   │FtsI/PBP3(1331)│ TPase     │MrdA-II (4807) │ TPase      MrcB/PBP1B (PP_4683) GT+TP
   └───────────────┘           │MrdA-I  (3741) │ TPase*     PbpC/PBP1C (PP_0572) GT+TP
                               └───────────────┘            MtgA      (PP_5107) GTase-only
                                     |
                          crosslinked sacculus (4-3 D,D crosslinks)
                                     |
        ┌────────────────────────────┼────────────────────────────┐
   DacA/PBP5 (PP_4803)          dacB/PBP4 (PP_2098)          L,D-TPases
   D,D-carboxypeptidase          D,D-endopeptidase           PP_1451, PP_2320
   [MODULE STEP 5]               [NOT in generic module]      3-3 crosslinks
                                                              [NOT in generic module]

   * PP_3741 is a second PBP2 paralog (73.5% id to PP_4807); role in KT2440 unknown.
```

The interpretation for curation is that KT2440's genome is **complete for canonical PG polymerization/crosslinking**, and in fact **richer** than the generic module in two respects (a PBP2 duplication, and both PBP4/S13 endopeptidase and YkuD L,D-transpeptidase activities). The module boundaries are correct in excluding precursor synthesis and carrier metabolism, but the module under-represents the LMW-PBP / non-classical crosslinking layer that is biologically and clinically important in *Pseudomonas*.

---

## 6. Gaps, Ambiguities, and Likely Over-Annotations

### 6.1 Scope contamination (highest-impact curation issue)

Only **11 of 23** KEGG ppu00550 candidates are in-scope. The KEGG map bundles the whole PG pathway, so the 12 Mur/Ddl/MraY/Upp genes are propagated into this bucket incorrectly, inflating apparent satisfiability. Correcting this is the single most impactful curation action.

### 6.2 Paralog ambiguity (not over-propagation)

The two PBP2/MrdA paralogs (PP_3741, PP_4807) are **real** (73.5% identity, correct Pfam, one operonic). The generic module already anticipates "MrdA-I/MrdA-II" — this is confirmed, not spurious. Neither should be dropped; PP_3741's specific role is the key open question.

### 6.3 Broad / incomplete EC and GO mappings

- **pbpC (PP_0572):** under-annotated — EC 3.4.16.4 transpeptidase missing despite PF00905.
- **mrcB (PP_4683):** no EC despite unambiguous class-A bifunctional architecture.
- **dacB (PP_2098):** generic "D-alanyl-D-alanine carboxypeptidase" name with no EC; its S13/PBP4 endopeptidase identity is not captured — risk of conflation with the DacA step.
- **mrcA (PP_5084):** dual EC (2.4.99.28 + 3.4.16.4) correctly applied — the template for bifunctional PBP annotation.

### 6.4 Missing module nodes (module_needs_revision)

- **L,D-transpeptidation (3-3 crosslink):** direct proteome evidence (Finding F005) — a scan of UP000000556 for Pfam **PF03734 (YkuD/L,D-transpeptidase)** returns exactly two proteins, **PP_1451 (Q88MW7)** and **PP_2320 (Q88KH0)**, both "L,D-TPase catalytic domain-containing protein." Neither is in the candidate list. L,D-transpeptidases produce 3-3 crosslinks and contribute to β-lactam tolerance and cell-wall remodeling in Gram-negative bacteria; the module has no node for them. This is a **module gap, not an organism gap**.
- **PBP4 D,D-endopeptidase (dacB):** no node exists for this activity.
- **Additional LMM-PBPs:** *Pseudomonas* genomes typically encode further PBP5-like/PBP7-like carboxy/endopeptidases; the single DacA slot under-represents this layer.

### 6.5 Naming inconsistency (Finding F005)

A name search for "penicillin-binding" in the KT2440 proteome returns only 5 proteins (mrcA, mrcB, mrdA-I, mrdA-II, ftsI). The SEDS polymerases (ftsW, mrdB), the class-A PbpC, MtgA, and the LMW PBPs (dacA, dacB) are **not retrievable by the "penicillin-binding" name string** — curators relying on name-based retrieval will miss functionally central genes. Retrieval must be by Pfam/EC, not name.

---

## 7. Evidence Base

All functional assignments for KT2440 in-scope genes rest on **homology and domain architecture (UniProt PE=3)**; there is no direct experimental characterization of these enzymes in KT2440 itself. Supporting mechanistic literature (from related organisms) and its transfer strength:

| PMID | Finding supported | Organism / transfer strength |
|---|---|---|
| [31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/) | RodA/FtsW are SEDS PG polymerases (verified quote: "the ubiquitous Shape, Elongation, Division, and Sporulation (SEDS)-family proteins RodA and FtsW were shown to be peptidoglycan polymerases") | General bacterial; **strong** — SEDS mechanism conserved; KT2440 ftsW/mrdB carry PF01098 |
| [33558391](https://pubmed.ncbi.nlm.nih.gov/33558391/) | Lateral RodA-PBP2 elongasome (verified quote: "PG is incorporated along the cell cylinder by the RodA-PBP2 synthase of the multi-protein Rod system (elongasome)") | General bacterial; **strong** — KT2440 has the mrdB-mrdA operon |
| [28289035](https://pubmed.ncbi.nlm.nih.gov/28289035/) | PBP2/PBP3 as essential β-lactam/enhancer targets in *Pseudomonas* | *P. aeruginosa*; **moderate** transfer to *P. putida* (same genus, conserved PBPs) |
| [41206063](https://pubmed.ncbi.nlm.nih.gov/41206063/) | PBP4/dacB is a distinct LMW-PBP whose inactivation drives AmpC induction | *P. aeruginosa* PAO1; **moderate** — supports treating dacB separately from dacA |
| [33830599](https://pubmed.ncbi.nlm.nih.gov/33830599/) | *P. putida* cell-wall chemical editing; PG crosslinking/transpeptidase biology | *P. putida* (direct genus/species context) + Rhizobiales; **moderate–strong** context |
| [28861525](https://pubmed.ncbi.nlm.nih.gov/28861525/) | PBP2 inactivation alters muropeptide profile and β-lactamase expression | *Pseudomonas*; **moderate** — supports functional importance of PBP2 |
| [42294650](https://pubmed.ncbi.nlm.nih.gov/42294650/) | PBP2 mutation (V516M) confers zidebactam resistance — PBP2 is the DBO target | *Pseudomonas*; **moderate** — supports PBP2 as elongation TPase |

Papers on xeruborbactam ([PMID: 36102663](https://pubmed.ncbi.nlm.nih.gov/36102663/)), avibactam/AmpC ([PMID: 33802668](https://pubmed.ncbi.nlm.nih.gov/33802668/)), and KT2440 Tn-seq/BarSeq metabolism screens ([PMID: 40302248](https://pubmed.ncbi.nlm.nih.gov/40302248/), [PMID: 32826213](https://pubmed.ncbi.nlm.nih.gov/32826213/)) provide broader context but do not directly characterize the KT2440 PG synthases.

---

## 8. Module and GO-Curation Recommendations

**Per-step module status:**

| Module step | Recommended status | Gene(s) |
|---|---|---|
| Septal SEDS GTase (FtsW) | `covered` | ftsW PP_1336 |
| Septal bPBP TPase (FtsI) | `covered` | ftsI PP_1331 |
| Lateral SEDS GTase (RodA/MrdB) | `covered` | mrdB PP_4806 |
| Lateral bPBP TPase (MrdA/PBP2) | `covered`; flag paralogs `candidate_uncertain` | mrdA-II PP_4807, mrdA-I PP_3741 |
| Class-A PBP1A | `covered` | mrcA PP_5084 |
| Class-A PBP1B | `covered` (add missing EC) | mrcB PP_4683 |
| Class-A PbpC | `covered` structurally (add EC 3.4.16.4) | pbpC PP_0572 |
| Monofunctional GTase (MtgA) | `covered` (accessory) | mtgA PP_5107 |
| DacA D,D-carboxypeptidase | `covered` | dacA PP_4803 |
| PBP4 D,D-endopeptidase | `module_needs_revision` (new node) | dacB PP_2098 |
| L,D-transpeptidation (3-3) | `module_needs_revision` / new companion module | PP_1451, PP_2320 |
| 12 Mur/Ddl/MraY/Upp genes | remove from bucket (out of scope) | — |

**Actions:**
1. **Remove** the 12 out-of-scope precursor/carrier genes from the polymerization module bucket; re-map to precursor synthesis / isoprenoid-carrier modules.
2. **Complete EC annotations** for pbpC (add EC 3.4.16.4) and mrcB (add EC 2.4.99.28 + 3.4.16.4), using mrcA as the correctly-annotated template.
3. **Reclassify dacB** as PBP4/peptidase-S13 D,D-endopeptidase; do not use it to satisfy the DacA carboxypeptidase step. Add a module node for D,D-endopeptidase activity.
4. **Add a module node / GO representation for L,D-transpeptidation** (3-3 crosslink) and associate PP_1451/PP_2320. A GO term request may be warranted if the module ontology lacks a 3-3 crosslink node.
5. **Keep SEDS GTase (GO:0008955 via PF01098) distinct from GT51 class-A GTase** in curation, and ensure GO:0009002 is applied only to the S11/PBP5 DacA family.
6. **Flag the naming inconsistency**: retrieval of PG synthases must be by Pfam/EC, not by the "penicillin-binding" name string.

---

## 9. Genes to Promote to Full `fetch-gene` Review

Priority for full gene-level review (all are PE=3, no direct KT2440 data):

1. **mrdA-I (PP_3741)** and **mrdA-II (PP_4807)** — the two PBP2 paralogs. Highest priority: paralog role assignment, operon context, redundancy vs specialization. Flag `candidate_uncertain`.
2. **pbpC (PP_0572)** — resolve bifunctional EC/GO annotation; assess whether it is an active TPase in KT2440.
3. **dacB (PP_2098)** — confirm PBP4/S13 identity and D,D-endopeptidase activity; decide module placement.
4. **mrcB (PP_4683)** — add missing bifunctional EC.
5. **PP_1451 and PP_2320** — YkuD L,D-transpeptidases; promote to establish the L,D-crosslink node even though absent from the original candidate list.
6. **ftsW (PP_1336)** and **mrdB (PP_4806)** — confirm SEDS partner pairing (FtsW–FtsI vs RodA–PBP2) as reference anchors.

---

## 10. Limitations and Knowledge Gaps

- **No direct experimental evidence in KT2440.** Every in-scope functional assignment is homology-inferred (UniProt PE=3). Mechanistic confidence rests on transfer from *E. coli*/general bacterial SEDS-bPBP biology and from *P. aeruginosa* PBP studies. Transfer within genus (*P. aeruginosa* → *P. putida*) is moderate; transfer from distant taxa is weaker.
- **Paralog function is unresolved.** The distinct roles of the two PBP2 paralogs (PP_3741 vs PP_4807) cannot be assigned from sequence alone.
- **L,D-transpeptidase and PBP4 activities are inferred from domain content only**; their in vivo contribution to KT2440 crosslinking has not been measured.
- **Module ontology limits.** Whether suitable GO terms / module nodes exist for 3-3 L,D-crosslinking and PBP4 endopeptidase activity was not verified against the live ontology.
- This review analyzed sequence/domain metadata and literature; **no muropeptide (HPLC/MS) crosslink profiling** of KT2440 was available to confirm which crosslink types are actually made.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Muropeptide profiling** of KT2440 sacculi (LC-MS) to quantify 4-3 vs 3-3 crosslinks and confirm L,D-transpeptidase activity in vivo.
2. **Single and double knockouts** of PP_3741 / PP_4807 to resolve PBP2 paralog redundancy and essentiality (with Bocillin-FL PBP profiling).
3. **Bocillin-FL PBP labeling** of KT2440 membranes to enumerate expressed PBPs and cross-check the in-silico roster.
4. **Curation task tickets:** (a) strip 12 precursor/carrier genes from bucket; (b) complete pbpC/mrcB EC; (c) reclassify dacB; (d) add L,D-TPase + PBP4 nodes; (e) add PP_1451/PP_2320.
5. **Expert question:** Does the curation ontology already have GO/module nodes for L,D-transpeptidation (3-3 crosslink) and PBP4 D,D-endopeptidase? If not, file GO term requests.

---

## 12. Key References

- Welsh MK, *et al.* *Direction of Chain Growth and Substrate Preferences of SEDS-Family Peptidoglycan Glycosyltransferases.* [PMID: 31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/) — RodA/FtsW are the SEDS PG polymerases.
- Rohs PDA, *et al.* *Identification of potential regulatory domains within the MreC and MreD components of the cell elongation machinery.* [PMID: 33558391](https://pubmed.ncbi.nlm.nih.gov/33558391/) — RodA–PBP2 synthase of the Rod system (elongasome).
- Moya B, *et al.* *WCK 5107 (Zidebactam)/WCK 5153: novel PBP2 inhibitors with β-lactam enhancer activity against P. aeruginosa.* [PMID: 28289035](https://pubmed.ncbi.nlm.nih.gov/28289035/) — PBP2/PBP3 as essential *Pseudomonas* targets.
- *Unravelling the triad of PBPs, β-lactamase activity, and mRNA dynamics in P. aeruginosa AmpC induction.* [PMID: 41206063](https://pubmed.ncbi.nlm.nih.gov/41206063/) — PBP4/dacB as a distinct LMW-PBP regulator/enzyme.
- Aliashkevich A, *et al.* *d-canavanine affects peptidoglycan structure, morphogenesis and fitness in Rhizobiales.* [PMID: 33830599](https://pubmed.ncbi.nlm.nih.gov/33830599/) — uses *P. putida*; PG crosslinkage and transpeptidase editing.
- *Characterizing the V516M penicillin-binding protein 2 (PBP2) mutation causing zidebactam resistance.* [PMID: 42294650](https://pubmed.ncbi.nlm.nih.gov/42294650/) — PBP2 as elongation transpeptidase target.
- *Impacts of Penicillin Binding Protein 2 Inactivation on β-Lactamase Expression and Muropeptide Profile.* [PMID: 28861525](https://pubmed.ncbi.nlm.nih.gov/28861525/) — PBP2 function and muropeptide effects.

---

*Prepared for manual module satisfiability and gene-annotation curation. All KT2440 functional calls are homology-inferred (UniProt PE=3); species-transfer strength is stated per claim. **Module verdict: satisfiable with revisions** — 11 in-scope genes cover all five canonical steps, but the bucket must be de-contaminated (12 out-of-scope genes), EC-completed (pbpC, mrcB), dacB reclassified (PBP4/S13 D,D-endopeptidase), and extended with L,D-transpeptidation (PP_1451, PP_2320) and PBP4 endopeptidase nodes. The two MrdA/PBP2 paralogs are flagged candidate_uncertain and promoted to full gene review.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_peptidoglycan_polymerization_crosslinking__ppu00550-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_peptidoglycan_polymerization_crosslinking__ppu00550-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:31386359
2. PMID:41206063
3. PMID:36102663
4. PMID:33802668
5. PMID:40302248
6. PMID:32826213
7. PMID:33558391
8. PMID:28289035
9. PMID:33830599
10. PMID:42294650
11. PMID:28861525