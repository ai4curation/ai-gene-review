---
title: "Phagocytosis Modules"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, worm, fly, DICDI]
genes: [MEGF10, GULP1, ELMO1, DOCK1, RAC1, MERTK, GAS6, TIMD4, RAB5A, RAB7A, MON1A, CCZ1, PIK3C3, DNASE2, SLC48A1, SLC66A1, PRKDC, RICTOR, MYC, BHLHE40, BACH1, SPIC, HMOX1, NR1H3, NR1H2, PPARD, AHR, IDO1, TLR9, SIRT1, PBX1, DNMT3A, PTGS2, SLC12A2]
---

# Phagocytosis Modules

**Goal:** a set of taxon-neutral modules that follow a particle from recognition
to the programmes its digestion switches on in the phagocyte. Each step is built
from PANTHER families with exemplar members from several lineages, and the
families and exemplar genes are reviewed as the modules are built.

This project grew out of [go-ontology#32748](https://github.com/geneontology/go-ontology/issues/32748)
and [#32152](https://github.com/geneontology/go-ontology/issues/32152), where the
GO phagocytosis branch was found to stop at digestion. The proposal sent to the
GO editors is at <https://claude.ai/artifact/8MJjKA2M2SDjcZAs9dL1ET>.

## Module tree

| Order | Module | Status | Scope |
|---|---|---|---|
| — | [`phagocytosis`](../modules/phagocytosis.yaml) (umbrella) | DRAFT | Composes the steps below with `module_ref` |
| 1 | [`phagocytic_engulfment`](../modules/phagocytic_engulfment.yaml) | DRAFT, revised | Recognition, Rho-GTPase activation, actin, cup closure |
| 2 | [`phagosome_maturation`](../modules/phagosome_maturation.yaml) | DRAFT, revised | Rab5 → Rab7, fusion, acidification, NOX2 |
| 3 | [`phagolysosomal_cargo_degradation`](../modules/phagolysosomal_cargo_degradation.yaml) | DRAFT | DNase II, cathepsins, amoebal lysozyme; export of amino acids, nucleosides, heme, cholesterol |
| 4 | Post-phagocytic programmes (optional parts) | DRAFT | See below |

Post-phagocytic programmes. Each is a separate module because each has its own
trigger, signalling chain and output. The umbrella lists them as optional
alternatives.

| Module | Trigger | Genes doing the work | Lineage evidence |
|---|---|---|---|
| [`efferocytosis_induced_macrophage_proliferation`](../modules/efferocytosis_induced_macrophage_proliferation.yaml) | apoptotic-cell DNA digested by DNase II | DNASE2, PRKDC, RICTOR, MYC, BHLHE40; MERTK arm | mouse |
| [`efferocytosis_induced_macrophage_priming`](../modules/efferocytosis_induced_macrophage_priming.yaml) | corpse engulfment | drpr, bsk | Drosophila |
| [`efferocytosis_induced_anti_inflammatory_programme`](../modules/efferocytosis_induced_anti_inflammatory_programme.yaml) | cargo sterols, fatty acids, tryptophan, methionine, DNA | NR1H2/3, PPARD, SIRT1/PBX1, IDO1/AHR, TLR9, DNMT3A/PTGS2, SLC12A2 | mouse |
| [`heme_induced_iron_recycling_macrophage_differentiation`](../modules/heme_induced_iron_recycling_macrophage_differentiation.yaml) | heme from engulfed erythrocytes | SLC48A1, BACH1, SPIC, HMOX1 | mouse |

## Design rules

- **Taxon-neutral where the biology is.** Engulfment, maturation and digestion
  are eukaryote-wide (amoebae feed this way), so their core annotons use
  PANTHER families with exemplars from mammals, nematodes, insects and, where
  conserved, *Dictyostelium*. Lineage-specific parts, such as vertebrate
  opsonin receptors or NOX2, are variants or optional parts.
- **Programmes are lineage-bounded.** The post-phagocytic programmes are
  context-limited to the clade where they are shown. Their participants are
  still families, and whether a programme extends beyond that clade is recorded
  as a knowledge gap or tested as an OpenScientist hypothesis.
- **Genes doing the work, not readouts.** Only gene products shown to carry out
  a step (loss of function, rescue, epistasis) become annotons. Expression
  markers such as CD68 or LGALS3 are not participants.
- **Families are checked.** UniProt PANTHER cross-references are checked
  against `interpro/panther/panther.obo`, and PTNs come only from local PAINT
  files.

## Family assignments where PANTHER and UniProt disagree

The modules follow PANTHER's own classification files (the member index), and
record the UniProt cross-reference in a note when it differs.

| Protein | PANTHER classification | UniProt cross-reference | Used |
|---|---|---|---|
| ced-1 (Q9XWD6), drpr (Q9W0A0) | PTHR24035:SF109 PROTEIN DRAPER | PTHR24043:SF8 | PTHR24035:SF109 |
| MEGF10 (Q96KG7) | PTHR24035:SF136 | PTHR24052:SF13 | PTHR24035 |
| AKT1 (P31749, P31750) | PTHR24356:SF171 | PTHR24351 | PTHR24356:SF171 |

The existing `phagocytic_engulfment` grounding of CED-1/MEGF10 in PTHR24035
therefore agrees with PANTHER.

## OpenScientist hypotheses (planned)

Each is one computable question, run with the project defaults.

1. Phylogenetic profile of PRKDC (DNA-PKcs): is the efferocytosis-induced
   proliferation route limited to lineages that have DNA-PKcs?
2. Do the BACH1 heme-degradation (cysteine-proline) motifs and SPIC orthologs
   co-occur, and in which vertebrate clades?
3. Is HRG1/SLC48A1 present in phagotrophic protists, which would suggest that
   phagolysosomal heme export predates animals?
4. What is the distribution of DNase II across phagocytic eukaryotes?

## Plan

1. Resolve families and PTNs for every participant. *(in progress)*
2. Build the four post-phagocytic programme modules. *(done, DRAFT)*
3. Build `phagolysosomal_cargo_degradation` and the `phagocytosis` umbrella. *(done, DRAFT)*
4. Revise `phagocytic_engulfment` and `phagosome_maturation` toward family
   selectors with cross-lineage exemplars. *(done: both now Eukaryota context,
   with Dictyostelium exemplars where conserved)*
5. Write family reviews for the key families and gene reviews for exemplars
   that lack them (DNASE2, nuc-1, drpr, SPIC, BACH1, SLC48A1, GULP1, ELMO1,
   DOCK1, MERTK, BHLHE40).
6. Run the OpenScientist hypotheses and fold the results into the modules.
