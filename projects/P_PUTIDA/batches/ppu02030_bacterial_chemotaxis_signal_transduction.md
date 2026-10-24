---
title: "PSEPK bacterial chemotaxis signal transduction"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [pcaY, mcpS, cheR2, cheB1, PP_4332, cheA, cheY, cheZ, fliM, fliN, fliG, motA, motB, PP_4335, PP_4336]
autolink_gene_symbols: false
---

# PSEPK bacterial chemotaxis signal transduction

- Module: `bacterial_chemotaxis_signal_transduction`
- Source bucket: KEGG `ppu02030` (bacterial chemotaxis)
- Focused genes: twelve named proteins plus three locus-tagged coupling/stator proteins spanning eight mechanistic parts
- Satisfiability: complete
- OpenScientist module/pathway/taxon research: complete

## Boundary

This module connects chemoreceptor input to flagellar motor output. It does not
enumerate the full PSEPK receptor repertoire, assert common ligand specificity,
or model construction of the flagellum. McpS and PcaY are exact receptor
exemplars; flagellar assembly/export is a separate module. KT2440 CheA contains
a CheW-like P5 domain, while free CheW Q88EX0 provides the canonical receptor-array
coupling function. The adjacent CheW-domain protein Q88EW9 remains unresolved.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Receptor input | McpS Q88E10 and PcaY Q88JK6 | Covered as exemplars |
| Receptor adaptation | CheR2 Q88ER1 and CheB1 Q88EW5 | Covered; paralogs require case-by-case assignment |
| Histidine-kinase relay | CheW Q88EX0 and CheA Q88EW4 | Covered; Q88EW9 paralog role unresolved |
| Response output | CheY Q88EW2 | Covered |
| Signal reset | CheZ Q88EW3 | Covered separately from CheY |
| Motor switch | FliM Q88EU5, FliN Q88EU6, and FliG Q88ET5 | Covered as the C-ring complex |
| Proton-driven output | MotAB Q88DC2/Q88DC3 and MotCD Q88EW6/Q88EW7 | Covered as conditionally specialized stator complexes |

## Curation Findings

The module is organized by signal flow rather than by KEGG membership count.
Transporter substrate-binding proteins, Wsp-like signaling proteins, and
uncharacterized receptor paralogs remain candidates rather than interchangeable
core steps. Both stators are modeled as complexes, without assigning the complete
proton transport function to any subunit independently. Direct KT2440 deletion
and complementation evidence distinguishes MotAB-dominant liquid swimming from
the MotCD contribution in semisolid environments (PMID:36409076).

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md)
- `modules/bacterial_chemotaxis_signal_transduction.yaml`
