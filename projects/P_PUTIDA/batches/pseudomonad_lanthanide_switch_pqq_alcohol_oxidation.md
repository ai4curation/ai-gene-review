---
title: "PSEPK lanthanide-switch PQQ alcohol oxidation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_2671, exaE, pedE, pedH]
autolink_gene_symbols: false
---

# PSEPK lanthanide-switch PQQ alcohol oxidation

- Module: `pseudomonad_lanthanide_switch_pqq_alcohol_oxidation`
- Source bucket: `ppu00625` (chloroalkane and chloroalkene degradation)
- Focused genes: 4
- Source GOA rows: 32

## Boundary

This batch replaces the incoherent literal KEGG bucket with the experimentally
defined Ped lanthanide switch. It contains three linked parts:

1. PedS2 membrane sensor-kinase signaling.
2. PedR2/ExaE response-regulator control of pedE and pedH transcription.
3. Alternative calcium-dependent PedE and lanthanide-dependent PedH
   periplasmic PQQ alcohol oxidation.

The `ppu00625` primary assignments for PedE and PedH reflect broad alcohol
dehydrogenase reaction mapping, not a demonstrated KT2440 chloroalkane pathway.
`fdhA` is excluded as unrelated KEGG spillover. PQQ biosynthesis, cytochrome-c
electron transfer, lanthanide uptake, and downstream aldehyde metabolism are
adjacent systems rather than extra parts of this module.

## Status

- [x] Fetch UniProt and GOA inputs for the previously unreviewed control pair.
- [x] Define and validate a reusable three-part module.
- [x] Curate all PP_2671 and exaE/PedR2 GOA rows.
- [x] Remove unsupported direct transcription-regulatory roles from PedH.
- [x] Complete and adjudicate all six OpenScientist reports.
- [x] Validate and render all artifacts.
- [ ] Open one module PR and complete `/review` follow-up.

## Focused Genes

| Gene | Locus | UniProt | GOA rows | Module role | Evidence boundary |
|---|---|---:|---:|---|---|
| `PP_2671` / PedS2 | PP_2671 | Q88JH8 | 8 | sensor histidine kinase | direct switch genetics; direct metal ligand unresolved |
| `exaE` / PedR2 | PP_2672 | Q88JH7 | 5 | response regulator | direct deletion, phosphosite, and promoter evidence |
| `pedE` | PP_2674 | Q88JH5 | 9 | calcium-dependent PQQ-ADH | purified enzyme and metal-dependent physiology |
| `pedH` | PP_2679 | Q88JH0 | 10 | lanthanide-dependent PQQ-ADH | purified enzyme and metal-dependent physiology |

The focused inventory is recorded in
[`pseudomonad_lanthanide_switch_pqq_alcohol_oxidation.tsv`](pseudomonad_lanthanide_switch_pqq_alcohol_oxidation.tsv).

## Evidence And Adjudication

- PMID:30158283 directly identifies PP_2671/PP_2672 as PedS2/PedR2 and
  establishes phosphorylation-dependent activation of pedE plus contribution
  to pedH repression.
- PMID:28655819 establishes overlapping PedE/PedH substrate ranges and their
  contrasting calcium versus lanthanide catalytic requirements.
- PedH affects its own promoter output genetically, but neither paper assigns
  PedH a DNA-binding or transcription-regulator molecular function. The old
  direct regulatory core function was removed and the feedback mechanism is
  retained as a knowledge gap.
- The completed PP_2671 OpenScientist report correctly identifies PedS2 and its
  topology, but overstates direct lanthanide perception and several cluster
  roles. Direct versus indirect sensing remains unresolved in the primary paper.
- The completed exaE report correctly reconciles ExaE with PedR2. Its claim of
  promoter DNA binding is supported at family/domain level; exact operator
  contacts remain unmeasured.
- The gene and module reports reinforce the PedE/PedH catalytic and metal
  assignments. They also identify the specific physiological cytochrome c
  partner as unresolved; the EC-derived cytochrome-c MF is retained without
  assigning the adjacent c550 as a directly demonstrated partner.
- The PedH report repeats the hypothesis that PedH itself is a sensory module.
  This genetic feedback is not converted into a DNA-binding or transcriptional
  regulator MF. Its statement that no PedH structure exists is rejected because
  UniProt Q88JH0 records crystal structures 6ZCV and 6ZCW.
- The species-aware report confirms that `ppu00625` is an EC-based mapping
  mismatch and that `fdhA`, `frmA`, and `adhP` are outside this module. It also
  identifies AgmR/PP_2665 as a nearby response-regulator paralog hazard rather
  than a PedR2 substitute.
- The generic module report supports the three-part boundary but extrapolates
  some architecture and evolutionary claims beyond direct evidence. The module
  context is therefore limited to `Pseudomonas` rather than all bacteria.
- No PANTHER/PTN selector is asserted for Ped-specific regulatory identity.
  Broad response-regulator and sensor-kinase families do not establish this
  particular lanthanide-switch role.

## Residual Uncertainty

- The direct molecular input to PedS2 is unknown.
- The positive activator required for full pedH induction is unknown.
- PedH-dependent promoter feedback is real genetically but mechanistically
  unresolved.
- The taxonomic range over which the complete four-protein Ped architecture is
  conserved remains to be established.
