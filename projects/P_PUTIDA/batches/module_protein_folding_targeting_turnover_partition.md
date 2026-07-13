---
title: "PSEPK protein folding, targeting, and turnover partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK protein folding, targeting, and turnover partition

The `module:protein_folding_targeting_turnover` bucket is a functional
UniProt-name/keyword bucket, not a single satisfiable pathway. It combines
core bacterial chaperone/foldase systems, ATP-dependent protein-turnover
machinery, cofactor/metal insertion chaperones, envelope and cell-wall
peptidases, aminopeptidases, DNA-repair and phage spillovers, and generic
low-information peptidase-family records.

- Full partition table: `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- Total primary genes: 91

| Bucket | Genes | Reviews | Curated | Asta | Proposed module | Status |
|---|---:|---:|---:|---:|---|---|
| `chaperone_folding_holdase_foldase` | 13 | 13/13 | 13/13 | 13/13 | `bacterial_chaperone_protein_folding_boundary` | QUEUED |
| `atp_dependent_protease_turnover` | 13 | 13/13 | 13/13 | 13/13 | `bacterial_atp_dependent_protein_turnover_boundary` | QUEUED |
| `cofactor_metal_maturation_chaperones` | 12 | 12/12 | 12/12 | 12/12 | `cofactor_metal_maturation_chaperone_boundary` | QUEUED |
| `cell_wall_envelope_peptidase_inhibitor` | 16 | 16/16 | 16/16 | 16/16 | `envelope_cell_wall_peptidase_inhibitor_boundary` | QUEUED |
| `peptide_processing_aminopeptidases` | 13 | 13/13 | 13/13 | 13/13 | `protein_turnover_peptide_processing_boundary` | QUEUED |
| `periplasmic_membrane_secreted_protease_qc` | 12 | 12/12 | 12/12 | 12/12 | `envelope_protease_quality_control_boundary` | QUEUED |
| `dna_damage_or_repair_spillover_proteases` | 3 | 3/3 | 3/3 | 3/3 | `dna_bucket_architectural_rna_protein_spillover_boundary` | QUEUED |
| `phage_mobile_protease_spillovers` | 2 | 2/2 | 2/2 | 2/2 | `phage_structural_packaging_boundary` | QUEUED |
| `low_information_peptidase_spillovers` | 7 | 7/7 | 7/7 | 7/7 | `protein_turnover_peptidase_spillover_boundary` | QUEUED |
