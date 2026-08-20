---
title: "PSEPK bacterial chemotaxis signal transduction"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [pcaY, mcpS, cheA, cheY, cheZ, fliG, motA, motB]
autolink_gene_symbols: false
---

# PSEPK bacterial chemotaxis signal transduction

- Module: `bacterial_chemotaxis_signal_transduction`
- Source bucket: KEGG `ppu02030` (bacterial chemotaxis)
- Focused genes: eight proteins spanning five mechanistic parts
- Satisfiability: complete
- OpenScientist module/pathway/taxon research: running

## Boundary

This module connects chemoreceptor input to flagellar motor output. It does not
enumerate the full PSEPK receptor repertoire, assert common ligand specificity,
or model construction of the flagellum. McpS and PcaY are exact receptor
exemplars; flagellar assembly/export is a separate module.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| Receptor input | McpS Q88E10 and PcaY Q88JK6 | Covered as exemplars |
| Histidine-kinase relay | CheA Q88EW4 | Covered |
| Response and reset | CheY Q88EW2 and CheZ Q88EW3 | Covered |
| Motor switch | FliG Q88ET5 | Covered |
| Proton-driven output | MotA Q88DC2 and MotB Q88DC3 | Covered as a stator complex |

## Curation Findings

The module is organized by signal flow rather than by KEGG membership count.
Transporter substrate-binding proteins and uncharacterized receptor paralogs
remain candidates, not interchangeable core steps. MotA and MotB are modeled as
complex contributors, without assigning the complete stator transport function
to either subunit independently.

## Evidence

- [OpenScientist module/pathway/taxon report](../deep-research/PSEPK__bacterial-chemotaxis-signal-transduction__ppu02030-deep-research-openscientist.md)
- `modules/bacterial_chemotaxis_signal_transduction.yaml`
