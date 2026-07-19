---
title: "Stilbene Cleavage Oxygenases (SCO / lignostilbene α,β-dioxygenase family)"
maturity: SCOPING
tags: [ENZYME_FAMILY]
species: [NEUCR, NOVAD, SPHPI]
genes:
  - cao-1
  - cao-2
  - Saro_0802
  - lsdB
---

# Stilbene Cleavage Oxygenases (SCO / LSD family)

## Overview

**Stilbene cleavage oxygenases (SCOs)**, also called **lignostilbene α,β-dioxygenases (LSDs,
EC 1.13.11.43)**, are non-heme iron enzymes that oxidatively cleave the **interphenyl Cα–Cβ double
bond of stilbenes**, converting one stilbene into two aromatic aldehydes. They are one branch of the
larger **carotenoid cleavage oxygenase (CCO)** family: they share the seven-bladed β-propeller fold
and the four-His mononuclear Fe(II) center of carotenoid cleavers, but have a substrate-binding cleft
adapted to the smaller, hydroxylated stilbene scaffold instead of a long polyene.

This project scopes the SCO/LSD class as a whole — fungal and bacterial members, the chemistry and
substrate recognition, and the Gene Ontology representation of the activity — building on the
Neurospora `cao-1` review that opened the thread.

## The reaction and the family

- **Chemistry:** a stilbene + O₂ → two phenolic/aromatic aldehydes (dioxygenase; both oxygen atoms
  incorporated). E.g. resveratrol → 3,5-dihydroxybenzaldehyde + 4-hydroxybenzaldehyde;
  lignostilbene → 2 vanillin.
- **Founding member:** lignostilbene α,β-dioxygenase (LSD) of *Sphingomonas paucimobilis*, the first
  enzyme shown to cleave the central stilbene double bond, acting in **lignin-derived stilbene
  catabolism**.
- **CCO-family context:** the carotenoid-cleaving sister enzymes (e.g. Neurospora **CAO-2**, a
  torulene dioxygenase in the neurosporaxanthin pathway) share the fold but act on carotenes — a
  substrate-class split that is the source of a recurring IBA over-annotation (see below).

## Members reviewed / in scope

| Gene | UniProt | Organism | Role | Status |
|---|---|---|---|---|
| **cao-1** | Q7S860 | *Neurospora crassa* (NEUCR) | resveratrol/piceatannol (hydroxystilbene) cleavage | reviewed |
| cao-2 (contrast) | A7UXI1 | *Neurospora crassa* (NEUCR) | torulene (carotenoid) cleavage — CCO sister | reviewed |
| **NOV1** (Saro_0802) | Q2GA76 | *Novosphingobium aromaticivorans* (NOVAD) | resveratrol / isoeugenol-cleaving dioxygenase (structure + mechanism) | reviewed |
| NOV2 | (Novosphingobium) | *Novosphingobium aromaticivorans* | stilbenoid-cleaving CCO | planned |
| **LSD-III (lsdB)** | Q52008 | *Sphingomonas paucimobilis* (SPHPI) | lignostilbene α,β-dioxygenase (founding LSD; EC 1.13.11.43) | reviewed |
| LSD-I | Q53353 | *Sphingomonas paucimobilis* (SPHPI) | lignostilbene α,β-dioxygenase isozyme I | candidate |
| Rco1 | (U. maydis) | *Ustilago maydis* | resveratrol cleavage oxygenase (fungal) | candidate |

## Substrate recognition: a two-ring-anchor model

A structure-based analysis of the CAO-1 co-crystals (5U90 resveratrol, 5U97 piceatannol) —
[cao-1 bioinformatics RESULTS](../genes/NEUCR/cao-1/cao-1-bioinformatics/RESULTS.md) — recovers a
**two-anchor recognition model**: a **4′-hydroxyl → Tyr133/Lys164** anchor on one ring and a
**3/5-hydroxyl → Glu383** anchor on the other, clamping the substrate with its scissile alkene ~4.6 Å
over the metal. This retrospectively explains CAO-1's entire empirical substrate panel (PMID:23893079),
including why a free 4′-OH is *necessary but not sufficient* (4-hydroxystilbene has it but lacks the
second anchor). Per-member specificity varies across the family: CAO-1 requires several free hydroxyls,
whereas bacterial LsdA reportedly cleaves even 4-hydroxystilbene — a difference the planned bacterial
reviews will examine structurally.

## Gene Ontology representation (a live issue)

The GO representation of this activity was actively revised in **July 2026**, overlapping exactly with
this work:

- **GO:1905594 "resveratrol binding" is being obsoleted** (go-ontology #32321/#32333) as ill-defined —
  its only two experimental annotations were CAO-1 (Q7S860, where resveratrol is a **substrate**) and
  NQO2 (P16083, where resveratrol is an **inhibitor**), which the single term conflated.
- **GO:7770086 "resveratrol dioxygenase activity"** was added (go-ontology #32332; RHEA:73735; parent
  GO:0016702), explicitly avoiding the carotenoid-dioxygenase branch.
- This project proposes a **grouping term** — provisionally *"stilbene α,β-dioxygenase activity"* (the
  literature-conventional name; "hydroxystilbene α,β-dioxygenase" is the scope-accurate descriptive
  variant) — as the **parent** of GO:7770086 and GO:0050054 (lignostilbene α,β-dioxygenase), to
  organize the currently-flat set of stilbene-cleavage leaf terms and to serve family-level (IBA)
  annotation.

## The IBA lesson

CAO-1 is a flagship example in the [IBA Annotation Quality project](IBA_REVIEW.md) (Pattern 11:
substrate over-propagation from a multi-specificity family). Because SCOs and carotenoid cleavers share
the PANTHER PTHR10543 family, carotenoid-dioxygenase terms over-propagate to the stilbenoid-cleaving
members. The *N. crassa* paralog pair is the decisive positive control: the **same** family IBA terms
are **wrong for cao-1** (a stilbene cleaver) and **right for cao-2** (a genuine torulene/carotenoid
cleaver). Getting the family node right — a stilbene-cleavage subfamily annotated with the grouping
term above — would fix the whole clade at once.

The same error recurs through **automated** pipelines: the bacterial **NOV1** carries the identical
carotenoid-dioxygenase over-annotation, but via **TreeGrafter** (IEA, GO_REF:0000118) rather than
manual IBA — so both the phylogenetic-inference and the tree-grafting propagation routes make the
identical substrate-class mistake on this family. (See also the TreeGrafter Inference Evaluation
project.)

## Open questions
- What is CAO-1's natural physiological stilbenoid substrate (plant-host vs microbial-competitor
  origin)? (See the cao-1 knowledge gaps.)
- Do the bacterial (NOV1/NOV2/LsdA) and fungal (CAO-1/Rco1) members differ structurally in the
  two-anchor architecture in a way that explains their differing hydroxylation requirements?
- Should GO adopt the proposed *stilbene α,β-dioxygenase activity* grouping as the parent of the
  reaction-specific leaves?

**Source**: [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review)
