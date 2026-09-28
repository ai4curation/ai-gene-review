---
title: "Sea Urchin Endomesoderm GRN"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [STRPU]
genes:
  - Tcf
  - SoxB1
  - Wnt8
  - Blimp1
  - Otx
  - GataE
  - FoxA
  - Eve
  - Pmar1
  - HesC
  - Alx1
  - Ets1
  - Erg
  - Dri
  - Delta
  - Gcm
  - GataC
  - Bra
---

# Sea Urchin Endomesoderm GRN

## Overview

Eric Davidson's laboratory built the first large, experimentally grounded gene
regulatory network (GRN) for an embryonic specification process: the
endomesoderm network of the purple sea urchin, *Strongylocentrotus purpuratus*
(UniProt mnemonic `STRPU`, NCBITaxon:7668). The network describes how maternal
inputs (nuclear beta-catenin acting through Tcf) are converted, through a
cascade of transcription factors and two short-range signals, into the
regulatory states of the skeletogenic micromere lineage, the non-skeletogenic
mesoderm, and the endoderm. It was assembled from systematic perturbation
(morpholino and dominant-negative) experiments, quantitative PCR time courses and
cis-regulatory analysis, and its architecture was reported in Davidson et al.
2002 (*Science*), refined for the micromere lineage in Oliveri, Tu and Davidson
2008 (*PNAS*) and for endoderm in Peter and Davidson 2011 (*Nature*). A common
misattribution assigns this work to the sea squirt; the *Ciona* networks were
built by other groups, and this project covers only the sea urchin.

This project holds gene reviews for the network's core nodes. GO annotation
coverage for *S. purpuratus* is almost entirely electronic (InterPro and UniRule
IEA, PANTHER IBA), so every review is literature-driven: the electronic rows are
audited, and the experimentally established functions are proposed as `NEW`
rows anchored to the primary Davidson-lab, Ettensohn-lab, McClay-lab and
Angerer-lab papers.

## Network architecture and the reviewed nodes

The nodes are grouped by the sub-network they belong to. Gene symbols follow
Echinobase usage; each links to its review.

### Maternal input and the ectoderm boundary

- **Tcf** (SpTcf/Lef, Q9Y0B2). The single sea urchin Tcf/Lef HMG-box factor.
  With Groucho it represses endomesoderm genes in the animal half; nuclearised
  beta-catenin converts it into an activator in vegetal blastomeres, an
  obligatory input to almost every early node below.
- **SoxB1** (Q9Y0D7). The ectoderm-side antagonist of the vegetal program,
  cleared from vegetal cells by beta-catenin-dependent degradation.

### Endoderm and the outward-moving torus

- **Wnt8** (Q6RFL8). Secreted Wnt ligand driven by Blimp1 and beta-catenin/Tcf.
  With Blimp1 it forms the "torus" subcircuit that propagates nuclear
  beta-catenin and endomesoderm specification outward from the vegetal pole.
- **Blimp1** (blimp1/krox, Q2VF23). PR-domain zinc-finger factor that activates
  wnt8 and otx, and represses its own gene, so that the endoderm regulatory state
  sweeps outward as a ring.
- **Otx** (Q26417). Orthodenticle-class homeodomain activator whose beta1/2
  cis-regulatory module integrates beta-catenin/Tcf, Blimp1 and GataE inputs; it
  feeds back on gatae and, in micromeres, helps activate pmar1.
- **GataE** (Q64HK6). GATA4/5/6-class factor locked in a positive feedback loop
  with Otx that stabilises endoderm specification, and later required for pigment
  cells.
- **FoxA** (Q1PA44). Forkhead factor of the veg2 endoderm that represses
  mesodermal fate (gcm) within endoderm and drives foregut and midgut regulatory
  state.
- **Eve** (Q8MMJ3). Even-skipped homeodomain factor of the veg2/veg1 endoderm
  ring, driven by beta-catenin/Tcf and Blimp1.

### The skeletogenic micromere lineage and the double-negative gate

- **Pmar1** (Q8WRE9). Micromere-specific paired-class homeodomain repressor,
  activated by Otx and beta-catenin/Tcf, that represses hesC.
- **HesC** (A0A7M7RIK0). bHLH-Orange repressor expressed everywhere except the
  micromeres; it represses alx1, ets1, tbr and delta. Pmar1 repression of hesC is
  the "double-negative gate" that confines the skeletogenic program to the
  micromeres.
- **Alx1** (Q7Z0W3). Cart1/Alx3/Alx4-subfamily homeodomain activator essential
  for skeletogenic (primary mesenchyme) fate, EMT and biomineralization.
- **Ets1** (Ets1/2, Q26645). ETS-family activator required for skeletogenic
  specification, alx1 cross-regulation and PMC ingression.
- **Erg** (Q6R7X7). ETS-family factor of the erg/hex/tgif feedback subcircuit
  downstream of ets1 and alx1.
- **Dri** (Spdri, Q8MQH7). ARID-domain factor required in the micromere lineage
  and later a key oral-ectoderm regulator.
- **Delta** (Q8T4N9). The Notch ligand expressed by the micromeres that induces
  non-skeletogenic mesoderm in the adjacent veg2 cells.

### Non-skeletogenic mesoderm

- **Gcm** (Q8MMJ4). Glial-cells-missing-family factor, the immediate target of
  micromere Delta/Notch signalling in veg2, and the driver of pigment cell
  specification.
- **GataC** (O77156). GATA1/2/3-class factor of the oral non-skeletogenic
  mesoderm (blastocoelar cell) lineage.
- **Bra** (brachyury, A0A7M7PDZ1). T-box factor expressed in the endoderm ring and
  in the oral ectoderm around the stomodeum.

## Nodes not yet covered

Several canonical nodes have no resolvable UniProt entry under a recognisable
name (Tbr, Hox11/13b, Hex, Tgif, FoxB) and were not reviewed. They can be added
once an accession is established from Echinobase or from a primary sequence.

## Curation conventions applied

- **Participation before annotation.** A transcription factor receives a
  cell-fate specification term only where it performs the regulatory step
  itself, with mapped binding sites or direct perturbation evidence. Downstream
  outcomes such as skeleton formation or pigment synthesis are not annotated to
  upstream regulators.
- **Ligands are ligands.** Wnt8 and Delta carry receptor ligand activity and the
  pathway term for the signal they deliver, not the transcriptional outcomes in
  the receiving cell.
- **Electronic rows are audited, not trusted or dismissed.** Generic IEA terms
  (DNA binding, regulation of DNA-templated transcription) are kept or modified
  to the RNA polymerase II-specific term supported by the literature. IBA rows
  are challenged only on phylogenetic grounds, with a `propagation_review`
  recording the source node and failure mode.
- **Organism caveats are explicit.** Several foundational papers used
  *Lytechinus variegatus* or *Paracentrotus lividus*; these are cited as
  orthologue support with the caveat recorded in `reference_review`, and
  `NEW` rows are anchored on *S. purpuratus* papers.
- **Cached abstracts only.** Many primary Davidson-lab papers are abstract-only
  in the publication cache; supporting quotes are drawn from those abstracts,
  and full-text availability is recorded per reference.

## Key references

- Davidson EH et al. 2002. A genomic regulatory network for development.
  *Science*. PMID:11872831.
- Oliveri P, Tu Q, Davidson EH. 2008. Global regulatory logic for specification
  of an embryonic cell lineage. *PNAS*. PMID:18413610.
- Revilla-i-Domingo R, Oliveri P, Davidson EH. 2007. A missing link in the sea
  urchin embryo gene regulatory network: hesC and the double-negative
  specification of micromeres. *PNAS*. PMID:17636127.
- Smith J, Davidson EH. 2008. Gene regulatory network subcircuit controlling a
  dynamic spatial pattern of signaling in the sea urchin embryo. *PNAS*.
  PMID:19104065.
- Peter IS, Davidson EH. 2011. A gene regulatory network controlling the
  embryonic specification of endoderm. *Nature*. PMID:21623371.
