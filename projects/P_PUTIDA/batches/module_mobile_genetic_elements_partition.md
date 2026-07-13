---
title: "PSEPK mobile genetic elements functional-bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK mobile genetic elements functional-bucket partition

The `module:mobile_genetic_elements` bucket is a broad UniProt-name/keyword bucket. It mixes insertion-sequence
transposases, integrases, prophage structural proteins, phage DNA replication/processing proteins, phage lysis
or host-interaction proteins, and low-information prophage proteins. It should not be curated as one pathway.

## Outputs

- Partition table: `projects/P_PUTIDA/batches/module_mobile_genetic_elements_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Status | Example genes |
|---|---:|---|---|---|---|
| `transposase_goa_supported` | 18 | `mobile_genetic_elements_boundary` | REUSE_OR_EXTEND_EXISTING | COMPLETE | `PP_0014`, `PP_0334`, `PP_0526`, `PP_0568`, `PP_1133`, `PP_1931`, `PP_2570`, `PP_2976` |
| `transposase_domain_or_fragment` | 22 | `mobile_genetic_elements_boundary` | DEFER_LOW_EVIDENCE | COMPLETE | `PP_0015`, `PP_0016`, `PP_0637`, `PP_0638`, `PP_0650`, `PP_3113`, `PP_3114`, `PP_3115` |
| `integrase_mobile_element_context` | 3 | `mobile_genetic_elements_boundary` | REUSE_OR_EXTEND_EXISTING | COMPLETE | `PP_1963`, `PP_2825`, `PP_3677` |
| `prophage_structural_packaging` | 21 | `prophage_structural_packaging_boundary` | NEW_SUBMODULE | COMPLETE | `PP_1562`, `PP_1563`, `PP_1565`, `PP_1569`, `PP_1574`, `PP_1577`, `PP_2287`, `PP_2288` |
| `phage_dna_replication_processing` | 6 | `phage_dna_replication_processing_boundary` | NEW_SUBMODULE | COMPLETE | `PP_1551`, `PP_1552`, `PP_2267`, `PP_2268`, `PP_3864`, `PP_3894` |
| `phage_lysis_host_interaction` | 2 | `phage_lysis_host_interaction_boundary` | NEW_SUBMODULE | COMPLETE | `PP_1561`, `PP_4858` |
| `phage_regulatory_toxin_antitoxin` | 3 | `phage_regulation_toxin_antitoxin_boundary` | NEW_SUBMODULE | COMPLETE | `PP_2500`, `PP_5558`, `PP_5626` |
| `low_information_prophage_proteins` | 14 | `mobile_genetic_elements_low_information_boundary` | DEFER_LOW_EVIDENCE | COMPLETE | `PP_1538`, `PP_1546`, `PP_1557`, `PP_1571`, `PP_2285`, `PP_3049`, `PP_3860`, `PP_3861` |

## Current Coverage

- Review status: {'PRESENT': 89}
- Curation status: {'CURATED': 89}
- Asta research status: {'PRESENT': 89}

## Working Decisions

- Start with the `transposase_goa_supported` split because it has direct GOA evidence for transposition or integration.
- Keep domain-only/fragmentary transposases separate until each can be reviewed without overpromoting fragments.
- Keep prophage structural and low-information proteins separate from enzymatic transposition/recombination calls.
