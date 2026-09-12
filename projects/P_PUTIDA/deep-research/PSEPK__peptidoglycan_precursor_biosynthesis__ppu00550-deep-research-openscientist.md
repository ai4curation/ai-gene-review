---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T06:56:26.687758'
end_time: '2026-07-23T08:11:20.254509'
duration_seconds: 4493.57
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Peptidoglycan precursor biosynthesis and lipid II export
  module_summary: A reusable bacterial pathway that converts UDP-N-acetylglucosamine
    to UDP-MurNAc-pentapeptide, transfers that nucleotide precursor to the undecaprenyl
    carrier to form lipid I, glycosylates lipid I to form lipid II, and translocates
    lipid II across the cytoplasmic membrane. D-Ala-D-Ala synthesis is modeled as
    a convergent input to MurF. The module ends at lipid II export and does not include
    glycan polymerization, peptide cross-linking, carrier recycling, or cell-wall
    remodeling.
  module_outline: "- Peptidoglycan precursor biosynthesis and lipid II export\n  -\
    \ 1. enolpyruvyl transfer to UDP-GlcNAc\n  - MurA enolpyruvyl transfer\n    -\
    \ UDP-N-acetylglucosamine 1-carboxyvinyltransferase (molecular player: PSEPK canonical\
    \ MurA; activity or role: UDP-N-acetylglucosamine 1-carboxyvinyltransferase activity)\n\
    \  - 2. UDP-MurNAc formation\n  - MurB UDP-MurNAc formation\n    - UDP-N-acetylmuramate\
    \ dehydrogenase (molecular player: PSEPK canonical MurB; activity or role: UDP-N-acetylmuramate\
    \ dehydrogenase activity)\n  - 3. L-alanine addition\n  - MurC L-alanine ligation\n\
    \    - UDP-N-acetylmuramate-L-alanine ligase (molecular player: PSEPK canonical\
    \ MurC; activity or role: UDP-N-acetylmuramate-L-alanine ligase activity)\n  -\
    \ 4. D-glutamate addition\n  - MurD D-glutamate ligation\n    - UDP-N-acetylmuramoylalanine-D-glutamate\
    \ ligase (molecular player: PSEPK canonical MurD; activity or role: UDP-N-acetylmuramoylalanine-D-glutamate\
    \ ligase activity)\n  - 5. meso-diaminopimelate addition\n  - MurE meso-diaminopimelate\
    \ ligation\n    - MurE meso-diaminopimelate ligase (molecular player: PSEPK canonical\
    \ MurE; activity or role: UDP-N-acetylmuramoylalanyl-D-glutamate-2,6-diaminopimelate\
    \ ligase activity)\n  - 6. D-Ala-D-Ala synthesis\n  - D-Ala-D-Ala synthesis\n\
    \    - D-alanine-D-alanine ligase (molecular player: PSEPK DdlB exemplar; activity\
    \ or role: D-alanine-D-alanine ligase activity)\n  - 7. UDP-MurNAc-pentapeptide\
    \ formation\n  - MurF pentapeptide ligation\n    - UDP-MurNAc-tripeptide-D-Ala-D-Ala\
    \ ligase (molecular player: PSEPK canonical MurF; activity or role: UDP-N-acetylmuramoyl-tripeptide-D-alanyl-D-alanine\
    \ ligase activity)\n  - 8. lipid I formation\n  - MraY lipid I synthesis\n   \
    \ - Phospho-MurNAc-pentapeptide transferase (molecular player: PSEPK canonical\
    \ MraY; activity or role: phospho-N-acetylmuramoyl-pentapeptide-transferase activity)\n\
    \  - 9. lipid II formation\n  - MurG lipid II synthesis\n    - Lipid I N-acetylglucosaminyltransferase\
    \ (molecular player: PSEPK canonical MurG; activity or role: undecaprenyldiphospho-muramoylpentapeptide\
    \ beta-N-acetylglucosaminyltransferase activity)\n  - 10. lipid II translocation\n\
    \  - MurJ lipid II export\n    - Lipid-linked peptidoglycan transporter (molecular\
    \ player: PSEPK canonical MurJ; activity or role: lipid-linked peptidoglycan transporter\
    \ activity)"
  module_connections: '- MurA enolpyruvyl transfer feeds into MurB UDP-MurNAc formation:
    MurA produces the enolpyruvyl substrate reduced by MurB.

    - MurB UDP-MurNAc formation feeds into MurC L-alanine ligation: MurB produces
    UDP-MurNAc for MurC.

    - MurC L-alanine ligation feeds into MurD D-glutamate ligation: MurC produces
    the mono-amino-acid precursor for MurD.

    - MurD D-glutamate ligation feeds into MurE meso-diaminopimelate ligation: MurD
    produces the dipeptide precursor for MurE.

    - MurE meso-diaminopimelate ligation feeds into MurF pentapeptide ligation: MurE
    supplies UDP-MurNAc-tripeptide to MurF.

    - D-Ala-D-Ala synthesis feeds into MurF pentapeptide ligation: Ddl supplies the
    D-Ala-D-Ala substrate to MurF.

    - MurF pentapeptide ligation feeds into MraY lipid I synthesis: MurF produces
    UDP-MurNAc-pentapeptide for MraY.

    - MraY lipid I synthesis feeds into MurG lipid II synthesis: MraY produces lipid
    I for MurG.

    - MurG lipid II synthesis feeds into MurJ lipid II export: MurG produces lipid
    II for MurJ-mediated export.'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__peptidoglycan_precursor_biosynthesis__ppu00550-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__peptidoglycan_precursor_biosynthesis__ppu00550-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Peptidoglycan precursor biosynthesis and lipid II export in Pseudomonas putida KT2440

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

A reusable bacterial pathway that converts UDP-N-acetylglucosamine to UDP-MurNAc-pentapeptide, transfers that nucleotide precursor to the undecaprenyl carrier to form lipid I, glycosylates lipid I to form lipid II, and translocates lipid II across the cytoplasmic membrane. D-Ala-D-Ala synthesis is modeled as a convergent input to MurF. The module ends at lipid II export and does not include glycan polymerization, peptide cross-linking, carrier recycling, or cell-wall remodeling.

### Provisional Biological Outline

- Peptidoglycan precursor biosynthesis and lipid II export
  - 1. enolpyruvyl transfer to UDP-GlcNAc
  - MurA enolpyruvyl transfer
    - UDP-N-acetylglucosamine 1-carboxyvinyltransferase (molecular player: PSEPK canonical MurA; activity or role: UDP-N-acetylglucosamine 1-carboxyvinyltransferase activity)
  - 2. UDP-MurNAc formation
  - MurB UDP-MurNAc formation
    - UDP-N-acetylmuramate dehydrogenase (molecular player: PSEPK canonical MurB; activity or role: UDP-N-acetylmuramate dehydrogenase activity)
  - 3. L-alanine addition
  - MurC L-alanine ligation
    - UDP-N-acetylmuramate-L-alanine ligase (molecular player: PSEPK canonical MurC; activity or role: UDP-N-acetylmuramate-L-alanine ligase activity)
  - 4. D-glutamate addition
  - MurD D-glutamate ligation
    - UDP-N-acetylmuramoylalanine-D-glutamate ligase (molecular player: PSEPK canonical MurD; activity or role: UDP-N-acetylmuramoylalanine-D-glutamate ligase activity)
  - 5. meso-diaminopimelate addition
  - MurE meso-diaminopimelate ligation
    - MurE meso-diaminopimelate ligase (molecular player: PSEPK canonical MurE; activity or role: UDP-N-acetylmuramoylalanyl-D-glutamate-2,6-diaminopimelate ligase activity)
  - 6. D-Ala-D-Ala synthesis
  - D-Ala-D-Ala synthesis
    - D-alanine-D-alanine ligase (molecular player: PSEPK DdlB exemplar; activity or role: D-alanine-D-alanine ligase activity)
  - 7. UDP-MurNAc-pentapeptide formation
  - MurF pentapeptide ligation
    - UDP-MurNAc-tripeptide-D-Ala-D-Ala ligase (molecular player: PSEPK canonical MurF; activity or role: UDP-N-acetylmuramoyl-tripeptide-D-alanyl-D-alanine ligase activity)
  - 8. lipid I formation
  - MraY lipid I synthesis
    - Phospho-MurNAc-pentapeptide transferase (molecular player: PSEPK canonical MraY; activity or role: phospho-N-acetylmuramoyl-pentapeptide-transferase activity)
  - 9. lipid II formation
  - MurG lipid II synthesis
    - Lipid I N-acetylglucosaminyltransferase (molecular player: PSEPK canonical MurG; activity or role: undecaprenyldiphospho-muramoylpentapeptide beta-N-acetylglucosaminyltransferase activity)
  - 10. lipid II translocation
  - MurJ lipid II export
    - Lipid-linked peptidoglycan transporter (molecular player: PSEPK canonical MurJ; activity or role: lipid-linked peptidoglycan transporter activity)

### Known Relationships Among Steps

- MurA enolpyruvyl transfer feeds into MurB UDP-MurNAc formation: MurA produces the enolpyruvyl substrate reduced by MurB.
- MurB UDP-MurNAc formation feeds into MurC L-alanine ligation: MurB produces UDP-MurNAc for MurC.
- MurC L-alanine ligation feeds into MurD D-glutamate ligation: MurC produces the mono-amino-acid precursor for MurD.
- MurD D-glutamate ligation feeds into MurE meso-diaminopimelate ligation: MurD produces the dipeptide precursor for MurE.
- MurE meso-diaminopimelate ligation feeds into MurF pentapeptide ligation: MurE supplies UDP-MurNAc-tripeptide to MurF.
- D-Ala-D-Ala synthesis feeds into MurF pentapeptide ligation: Ddl supplies the D-Ala-D-Ala substrate to MurF.
- MurF pentapeptide ligation feeds into MraY lipid I synthesis: MurF produces UDP-MurNAc-pentapeptide for MraY.
- MraY lipid I synthesis feeds into MurG lipid II synthesis: MraY produces lipid I for MurG.
- MurG lipid II synthesis feeds into MurJ lipid II export: MurG produces lipid II for MurJ-mediated export.

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

# Module/Pathway/Taxon Review

## Peptidoglycan precursor biosynthesis and lipid II export in *Pseudomonas putida* KT2440

- **Organism:** *Pseudomonas putida* KT2440 (PSEPK, NCBI taxon 160488, proteome UP000000556)
- **Module bucket:** kegg:ppu00550 ("Peptidoglycan biosynthesis"); module area *lipid_cell_envelope_metabolism*
- **Module scope (as commissioned):** UDP-GlcNAc → UDP-MurNAc-pentapeptide → lipid I → lipid II → lipid II export. Ends at the flippase step; **excludes** glycan polymerization, transpeptidation/cross-linking, carrier recycling, and cell-wall remodeling.

---

## 1. Executive summary

The peptidoglycan-precursor-and-lipid-II-export module is **fully satisfiable** in *P. putida* KT2440. All ten conceptual steps are encoded by identifiable, mostly single-copy genes with EC/domain evidence consistent with the expected model.

Two curation-critical points dominate this review:

1. **The terminal step (step 10, lipid II export) IS present but was OMITTED from the candidate list.** MurJ is encoded by **PP_0601 (Q88Q94)**, a MurJ/MviN-family protein (Pfam PF03023, InterPro IPR004268). It was excluded because the seeding bucket (KEGG map ppu00550) does not catalog the membrane flippase. Step 10 should be marked **covered**, not gap.
2. **The 23-gene candidate list is over-inclusive.** Only ~10 of 23 genes belong to this module. The other ~13 are downstream polymerases/transpeptidases/carboxypeptidases and undecaprenyl-carrier enzymes that the module scope explicitly excludes — a boundary artifact of using a whole KEGG-map bucket to seed a narrower biosynthetic module.

Evidence is largely **homology/annotation-based with strong within-Proteobacteria transfer**; there is little KT2440-*direct* genetic characterization of these specific loci, which is normal for essential housekeeping genes.

---

## 2. Target-organism pathway definition

**Included process (KT2440):** the cytoplasmic and inner-membrane-associated synthesis of the peptidoglycan precursor. Sequentially: enolpyruvyl transfer onto UDP-GlcNAc (MurA) → reduction to UDP-MurNAc (MurB) → sequential ligation of L-Ala, D-Glu, meso-DAP, and the D-Ala-D-Ala dipeptide onto UDP-MurNAc (MurC, MurD, MurE, MurF; D-Ala-D-Ala supplied by Ddl) → transfer of phospho-MurNAc-pentapeptide to the undecaprenyl-phosphate carrier to form **lipid I** (MraY) → GlcNAc addition to form **lipid II** (MurG) → translocation of lipid II to the periplasmic face (MurJ). KT2440 is a Gram-negative rod with **DAP-type (meso-A2pm) peptidoglycan**, consistent with the meso-DAP-adding MurE (EC 6.3.2.13) rather than a Lys-adding MurE.

**Neighboring pathways/maps to keep SEPARATE:**
- **PG polymerization & cross-linking** (SEDS glycosyltransferases FtsW/RodA, class-A/B PBPs) — maps ppu01501/ppu01502; downstream of this module.
- **Cell-wall remodeling** — D,D-carboxypeptidases (DacA/DacB).
- **Undecaprenyl carrier metabolism** — Und-PP synthase (UppS, ppu00900) and Und-PP phosphatase/BacA (UppP, ppu00552); carrier supply/recycling, explicitly excluded.
- **D-amino-acid supply** — alanine racemase, glutamate racemase (MurI), DAP epimerase (DapF); convergent inputs sitting in amino-acid metabolism maps.

**Alternate names / database definitions:** MraY = phospho-N-acetylmuramoyl-pentapeptide-transferase (translocase I). MurJ = MviN (historical). Ddl = D-Ala–D-Ala ligase (DdlA/DdlB). The *mur*/*mra* cluster is the **dcw (division and cell wall) cluster**. KEGG ppu00550 is broader than this module (it is the whole "Peptidoglycan biosynthesis" map, including polymerization and PBPs).

---

## 3. Expected step model and satisfiability call

| # | Step | Expected player | KT2440 gene (locus / UniProt) | Call |
|---|------|-----------------|-------------------------------|------|
| 1 | Enolpyruvyl transfer to UDP-GlcNAc | MurA | murA / PP_0964 / Q88P88 (EC 2.5.1.7) | **covered** |
| 2 | UDP-MurNAc formation | MurB | murB / PP_1904 / Q88LM5 (EC 1.3.1.98) | **covered** |
| 3 | L-Ala addition | MurC | murC / PP_1338 / Q88N75 (EC 6.3.2.8) | **covered** |
| 4 | D-Glu addition | MurD | murD / PP_1335 / Q88N78 (EC 6.3.2.9) | **covered** |
| 5 | meso-DAP addition | MurE | murE / PP_1332 / Q88N81 (EC 6.3.2.13) | **covered** |
| 6 | D-Ala-D-Ala synthesis | Ddl | ddlB / PP_1339 / Q88N74 **and** ddlA / PP_4346 / Q88EV6 (EC 6.3.2.4) | **covered** (2 paralogs) |
| 7 | UDP-MurNAc-pentapeptide formation | MurF | murF / PP_1333 / Q88N80 (EC 6.3.2.10) | **covered** |
| 8 | Lipid I formation | MraY | mraY / PP_1334 / Q88N79 (EC 2.7.8.13) | **covered** |
| 9 | Lipid II formation | MurG | murG / PP_1337 / Q88N76 (EC 2.4.1.227) | **covered** |
| 10 | Lipid II export | MurJ | **murJ / PP_0601 / Q88Q94** (MurJ/MviN family) | **covered** — *but was absent from candidate list* |

**Convergent inputs (present, but outside module boundary):** glutamate racemase MurI (PP_0736, EC 5.1.1.3 → D-Glu for MurD); DAP epimerase DapF (PP_5228 and PP_3790, EC 5.1.1.7 → meso-DAP for MurE); alanine racemase activity from broad-specificity Alr (PP_3722, EC 5.1.1.10) and/or catabolic DadX (PP_5269, EC 5.1.1.1 → D-Ala for Ddl).

No step is **not_expected_in_target_taxon**; this module is universal in walled Gram-negative bacteria and KT2440 is no exception.

---

## 4. Candidate genes and evidence

### 4a. In-scope, high-confidence (module backbone)
- **MurA (PP_0964):** EPSP-synthase family, MurA subfamily; single copy (no MurZ paralog). First committed, non-redundant step; fosfomycin target. Evidence: sequence/family + universal biochemistry. Transfer: strong.
- **MurB (PP_1904):** UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98). Single copy. Homology-based; strong.
- **MurC–MurF (PP_1338, PP_1335, PP_1332, PP_1333):** the Mur ligase cascade, single copy each, clustered in the dcw locus (PP_1331–PP_1339). EC numbers match the expected chemistry exactly. MurE is the **meso-DAP-adding** form (correct for a DAP-type Gram-negative). Strong.
- **MraY (PP_1334):** phospho-MurNAc-pentapeptide transferase (EC 2.7.8.13), integral-membrane translocase I. Strong.
- **MurG (PP_1337):** lipid I β-GlcNAc-transferase (EC 2.4.1.227). Strong.
- **DdlA (PP_4346) & DdlB (PP_1339):** two genuine D-Ala-D-Ala ligase paralogs. DdlB sits in the dcw cluster (likely primary biosynthetic ligase); DdlA is dispersed. Redundancy makes the step robust to single-gene loss. Caveat: physiological dominance of the two paralogs is not experimentally resolved in KT2440.

### 4b. In-scope terminal step, MISSING from candidates
- **MurJ (PP_0601 / Q88Q94):** MurJ/MviN family (Pfam PF03023; InterPro IPR004268), ~512 aa, MOP-superfamily topology — the diagnostic signature of a lipid II flippase. It is the **sole** PF03023-family member in KT2440 (two orthogonal UniProt queries return only this entry), i.e. a **single-copy, non-redundant** step — unlike multi-paralog Firmicutes (*B. subtilis* has four MviN homologs that are individually dispensable, PMID 19666716), so no cryptic paralog offsets its omission. By transfer from essential single-copy MurJ in *E. coli* and *Burkholderia*, it is expected to be essential in KT2440. Not in the 23-gene metadata because the KEGG map bucket omits the transporter. **This is the single most important correction to the candidate list.**

### 4c. Out-of-scope candidates (legitimate genes, wrong module)
Downstream PG synthesis/remodeling and carrier metabolism, to be reassigned:
- **SEDS/PBP polymerases & transpeptidases:** pbpC (PP_0572), ftsI/PBP3 (PP_1331), ftsW (PP_1336), mrdB/RodA (PP_4806), mrdA-I (PP_3741), mrdA-II (PP_4807), mrcA/PBP1a (PP_5084), mrcB/PBP1b (PP_4683), mtgA (PP_5107).
- **D,D-carboxypeptidase remodeling:** dacA (PP_4803), dacB (PP_2098).
- **Undecaprenyl-carrier metabolism:** uppS (PP_1595, Und-PP synthase; carrier *supply*), uppP (PP_2862, Und-PP phosphatase/BacA; carrier *recycling*).

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Apparent gap that is actually covered:** step 10 (export). Resolve by adding PP_0601. Do **not** attempt to satisfy step 10 with FtsW (PP_1336): FtsW was historically proposed as the flippase but is now established as a SEDS peptidoglycan glycosyltransferase; the flippase is MurJ (the "FtsW vs MurJ vs AmJ" debate is resolved in favor of MurJ for lipid II translocation).
- **Paralog ambiguity:** DdlA vs DdlB (step 6) — both real; dominance unresolved. Two DapF entries (PP_5228, PP_3790) — a possible epimerase paralog or an over-called annotation; both are *input-supply* enzymes, outside the module.
- **Broad EC/GO over-propagation:** EC 2.4.99.28 (peptidoglycan glycosyltransferase) is shared by MtgA, FtsW, RodA, PBP1a/1b — this shared EC drove several polymerases into the ppu00550 bucket. EC 3.4.16.4 (D,D-carboxypeptidase/transpeptidase) similarly pulled in FtsI, MrdA, DacA. These are annotation-map artifacts, not evidence of module membership.
- **Carrier boundary:** uppS/uppP border the module (Und-P is the acceptor for MraY) but the commissioned scope excludes carrier recycling. Keep them adjacent, not inside.
- **Evidence caveat:** all calls are homology/family-based; no KT2440-*direct* knockout/biochemical study was located for these specific loci. Transfer within Gram-negative Proteobacteria (E. coli/*Pseudomonas*/*Burkholderia*) is strong for the essential Mur enzymes and for MurJ.

---

## 6. Module and GO-curation recommendations

- **Mark covered:** steps 1–10, using the mapping in Section 3. In particular, record step 10 = **PP_0601 (MurJ)**.
- **module_needs_revision (candidate list, not the module logic):** add PP_0601; remove/reassign the 13 out-of-scope downstream genes to the correct adjacent modules (PG polymerization/cross-linking; carrier metabolism; remodeling).
- **candidate_uncertain:** none of the backbone steps; the only residual uncertainty is *which* Ddl paralog is primary (annotation-level, not satisfiability-level).
- **not_expected_in_target_taxon:** none.
- **New module documents / GO requests:** likely **not** needed for GO terms (MurJ, MraY, MurG, all Mur ligases have established GO/EC). A curation note should record that the seeding bucket (whole KEGG map) is broader than this module, so future bucket→module seeding for lipid-cell-envelope should (a) inject the transporter/flippase step manually and (b) exclude EC 2.4.99.28 / EC 3.4.16.4 polymerase/carboxypeptidase genes.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0601 (murJ / Q88Q94)** — highest priority: newly identified terminal step, unreviewed TrEMBL ("Probable"), needs confidence upgrade and formal addition to the module.
2. **PP_1339 (ddlB)** and **PP_4346 (ddlA)** — resolve paralog roles / which is essential.
3. **PP_1334 (mraY)** and **PP_1337 (murG)** — membrane steps flanking export; confirm single-copy essentiality annotations.
4. (Lower priority) **PP_0964 (murA)** — confirm fosfomycin-target/essentiality flag as the single non-redundant first step.

---

## 8. Key references

- Ruiz N. (2008) *PNAS* 105:15553–15557. Bioinformatic identification of MviN/MurJ as the *E. coli* lipid II flippase. **PMID 18832143.**
- Mohamed YF, Valvano MA. (2014) *Glycobiology*/*J. Bacteriol.* A *Burkholderia cenocepacia* MurJ (MviN) homolog is essential for PG synthesis and viability; depletion causes lipid II precursor accumulation. **PMID 24688094.**
- Ruiz N. (2015) *Curr. Opin. Microbiol.*/review. Lipid flippases for bacterial PG biosynthesis; FtsW vs MurJ vs AmJ debate. **PMID 26792999.**
- Fay A, Dworkin J. (2009) *J. Bacteriol.* 191:6020–6028. *B. subtilis* MviN/MurJ homologs are not essential — a caveat that MurJ essentiality is lineage-dependent (strong in Gram-negatives). **PMID 19666716.**
- Molina-Henares MA et al. (2010) *Environ. Microbiol.* Genome-wide conditionally essential genes of *P. putida* KT2440 (context for KT2440 gene essentiality). **PMID 20158506.**
- UniProt Knowledgebase, proteome UP000000556 (*P. putida* KT2440): entries Q88P88, Q88LM5, Q88N75/78/81/80/79/76, Q88N74, Q88EV6, Q88Q94, Q88PW2, plus racemase/epimerase inputs. Family/domain evidence: Pfam PF03023, InterPro IPR004268 (MurJ/MviN).

---

*Evidence class summary:* Steps 1–9 — direct family/EC assignment + universal biochemistry, strong within-Proteobacteria transfer. Step 10 — domain-level (MurJ/MviN, PF03023) assignment; function transferred by strong homology from *E. coli*/*Burkholderia* (no KT2440-direct experiment). Scope corrections — based on module definition + KEGG map structure + shared EC over-propagation.


## Artifacts

- [OpenScientist final report](PSEPK__peptidoglycan_precursor_biosynthesis__ppu00550-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__peptidoglycan_precursor_biosynthesis__ppu00550-deep-research-openscientist_artifacts/final_report.pdf)