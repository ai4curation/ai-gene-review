---
title: "PSEPK DNA replication, repair, and recombination functional-bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK DNA replication, repair, and recombination functional-bucket partition

The `module:dna_replication_repair_recombination` bucket is a broad
functional umbrella assembled from UniProt names and keywords. It mixes
core DNA topology and repair proteins with phage/mobile-element enzymes,
reverse transcriptases, toxin nucleases, RNA-helicase/protein-folding
spillovers, and DNA-binding architectural proteins. It should not be
curated as one pathway.

## Outputs

- Partition table: `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Example genes |
|---|---:|---|---|---|
| `dna_topology_topoisomerase` | 9 | `dna_topology_topoisomerase_boundary` | NEW_SUBMODULE | `gyrB`, `yacG`, `gyrA`, `topA`, `PP_3831`, `topB`, `PP_4476`, `parC` |
| `replication_accessory_polymerase` | 6 | `bacterial_dna_replication` | REUSE_OR_EXTEND_EXISTING | `PP_0978`, `hda`, `PP_2270`, `PP_2273`, `rarA`, `rep` |
| `sos_translesion_alkylation_repair` | 9 | `dna_damage_response_translesion_repair_boundary` | NEW_SUBMODULE | `dinB`, `PP_1348`, `lexA1`, `polB`, `ogt`, `lexA2`, `imuB`, `dnaE2` |
| `repair_helicase_recombination_core` | 20 | `bacterial_homologous_recombination` | REUSE_OR_EXTEND_EXISTING | `PP_0152`, `PP_1061`, `PP_1103`, `PP_1106`, `dinG`, `PP_1410`, `rdgC`, `PP_1937` |
| `mobile_integrase_recombinase_transposase` | 25 | `mobile_genetic_elements_boundary` | REASSIGN_TO_MOBILE_ELEMENTS | `PP_1116`, `PP_1118`, `PP_1532`, `PP_1533`, `PP_1555`, `PP_1865`, `PP_1960`, `PP_1962` |
| `retroelement_reverse_transcriptase` | 3 | `mobile_genetic_elements_boundary` | REASSIGN_TO_MOBILE_ELEMENTS | `PP_0635`, `PP_1250`, `PP_1846` |
| `nuclease_dnase_toxin_side_nodes` | 14 | `nuclease_dnase_boundary` | NEW_SUBMODULE | `PP_1306`, `PP_1554`, `PP_2276`, `tatD`, `endX`, `PP_2838`, `yoeB`, `endA` |
| `architectural_rna_protein_spillovers` | 7 | `dna_bucket_architectural_rna_protein_spillover_boundary` | NEW_SUBMODULE | `tldD`, `ihfB`, `ihfA`, `cspD`, `hrpA`, `dnaJ`, `hrpB` |

## Working Decisions

- Do not curate all 93 primary genes as one DNA replication/repair PR.
- Reuse existing KEGG-derived modules for canonical bacterial DNA replication,
  base excision repair, nucleotide excision repair, mismatch repair,
  homologous recombination, and non-homologous end joining.
- The DNA-topology/topoisomerase, replication-accessory/polymerase,
  SOS/translesion/alkylation, repair-helicase/recombination, and
  nuclease/DNase/toxin sub-batches, and architectural/RNA/protein
  spillovers are separate from the mobile-element spillover set.
- Route reverse transcriptases, phage integrases, transposases, and many
  recombinases to the mobile-genetic-elements boundary unless gene-level
  evidence supports direct chromosomal DNA repair.

## Current Coverage

- Review status: {'PRESENT': 93}
- Curation status: {'CURATED': 93}
- Asta research status: {'PRESENT': 93}

## Next Steps

- `dna_topology_topoisomerase` is complete as a compact 9-gene first-pass
  sub-batch with the new `dna_topology_topoisomerase_boundary` module.
- `sos_translesion_alkylation_repair` is complete as a compact 9-gene
  first-pass sub-batch with the new
  `dna_damage_response_translesion_repair_boundary` module.
- `repair_helicase_recombination_core` is complete as a 20-gene
  first-pass sub-batch extending `bacterial_homologous_recombination`.
- `nuclease_dnase_toxin_side_nodes` is complete as a 14-gene
  first-pass sub-batch with the new `nuclease_dnase_boundary` module.
- `replication_accessory_polymerase` is complete as a 6-gene
  first-pass sub-batch extending `bacterial_dna_replication`.
- `architectural_rna_protein_spillovers` is complete as a 7-gene
  first-pass sub-batch with the new
  `dna_bucket_architectural_rna_protein_spillover_boundary` module.
- `mobile_integrase_recombinase_transposase` is complete as a 25-gene
  first-pass sub-batch with the new `mobile_genetic_elements_boundary`
  module.
- `retroelement_reverse_transcriptase` is complete as a 3-gene
  first-pass sub-batch represented in `mobile_genetic_elements_boundary`.
- The full 93-gene DNA replication/repair/recombination functional bucket
  now has review files, curated reviews, and Asta reports for every
  partition member.
