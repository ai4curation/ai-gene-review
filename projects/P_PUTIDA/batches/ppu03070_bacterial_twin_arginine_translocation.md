---
title: "PSEPK twin-arginine protein translocation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [tatA-I, tatB-I, tatC-I, tatA-II, tatB, tatC-II]
autolink_gene_symbols: false
---

# PSEPK twin-arginine protein translocation

This batch resolves the Tat branch split across KEGG protein-export and
bacterial-secretion maps. The reusable module is
`modules/bacterial_twin_arginine_translocation.yaml`; Sec export, type II
secretion, and type VI secretion are separate modules.

## Boundary

The module contains three substantive roles:

1. TatC-dependent twin-arginine signal recognition and membrane scaffolding.
2. TatB-dependent receptor-complex organization.
3. TatA-dependent, proton-motive-force-driven translocation assembly.

Substrate folding/cofactor installation, signal-peptide cleavage, and the
downstream functions of exported proteins are outside the boundary.

## Status

- [x] Fetch both PSEPK `tatABC` loci from UniProt and GOA.
- [x] Create a species-neutral, multi-part Tat module with exact exemplars.
- [ ] Complete OpenScientist gene, module, and module + pathway + taxon research
  (one gene report complete; session `14967` remains active and non-blocking).
- [x] Complete independent annotation-reviewer and module-curation audits.
- [x] Validate and render all changed artifacts.
- [x] Publish one draft PR for this module.

## Focused Genes

| Gene | Locus | UniProt | Module role |
|---|---|---|---|
| `tatC-I` | PP_1039 | Q88P14 | TatC receptor/scaffold, system I |
| `tatB-I` | PP_1040 | Q88P13 | TatB receptor organization, system I |
| `tatA-I` | PP_1041 | Q88P12 | TatA translocation assembly, system I |
| `tatA-II` | PP_5016 | Q88D13 | TatA translocation assembly, system II |
| `tatB` | PP_5017 | Q88D12 | TatB receptor organization, system II |
| `tatC-II` | PP_5018 | Q88D11 | TatC receptor/scaffold, system II |

The existence of two intact loci supports structural satisfiability, but their
substrate specificity and physiological division of labor remain unresolved.
PMID:23530902 provides direct KT2440 evidence that both complete Tat systems can
transport UxpB; it does not isolate individual subunit mechanisms or establish
broader locus-specific substrate sets.

The exact UniProt symbol for PP_5017 is `tatB` and is retained here. The
OpenScientist protein-export report's `tatB-II` relabel suggestion is treated as
a non-authoritative naming proposal, not as a source-annotation change.
