---
title: "Yeast DNA Repair & Chromatin Dynamics"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [yeast]
last_reviewed: '2026-10-05'
genes: [SPT16, POB3, CHD1, SWI1]   # reviewed chromatin arm only; full candidate list is in the checklist below
manifest:
  slides:
    - href: YEAST_DNA_REPAIR_CHROMATIN/slides/YEAST_DNA_REPAIR_CHROMATIN-slides.html
      description: Yeast DNA repair and chromatin slides
---

# Yeast DNA Repair & Chromatin Dynamics

**Bottom line:** in progress, with only the chromatin arm started. Budding yeast
repairs DNA through checkpoint signalling, homologous recombination, mismatch
repair and damage-tolerant polymerases, and every one of these steps has to
open and then restore chromatin. This project plans to review the GO
annotations of 26 distinct *S. cerevisiae* genes across those pathways. We
picked the set to find where DNA repair and chromatin handling meet,
especially the FACT histone chaperone and the remodelers. Four of the 26 now
have reviews in the repo: SPT16 (65
annotation rows), POB3 (32), CHD1 (65) and SWI1 (41, including one proposed
NEW term), covering 203 rows in total: 124 ACCEPT, 24 KEEP_AS_NON_CORE, 50
REMOVE, 2 MODIFY, 1 MARK_AS_OVER_ANNOTATED, 1 UNDECIDED and 1 NEW. None of the
recombination, checkpoint, mismatch-repair or ribonucleotide-reductase genes
has a review folder, so the checklist below is still open outside the chromatin
genes.

## Overview

This project reviews *Saccharomyces cerevisiae* genes central to **DNA damage
response**, **homologous recombination**, **mismatch repair**, **damage
tolerance**, and **chromatin remodeling**. The reviewed chromatin arm starts
with FACT, CHD1 and SWI/SNF, whose GO rows connect histone chaperone or
ATP-dependent nucleosome-remodeling activities to transcription, DNA
replication and DNA repair.

## Key Research Areas

1. **DNA Damage Recognition & Signaling** - Sensor complexes and checkpoint control
2. **Homologous Recombination (HR)** - `RAD51`/`RAD52` filament formation and strand invasion
3. **Double-Strand Break Repair** - Resection, homology search, recombination
4. **Chromatin Reconfiguration** - Spatial reorganization following DNA damage
5. **FACT Complex & Histone Dynamics** - Histone recycling during replication/repair
6. **Nucleotide Excision Repair & Damage Tolerance** - TFIIH/NER, translesion synthesis and dNTP supply
7. **Mismatch Repair (MMR)** - Replication error correction

## Biological Significance

- **Conservation** - DNA repair mechanisms highly conserved; yeast reveals eukaryotic principles
- **Structural biology** - Cryo-EM revealing molecular mechanisms (FACT-replisome, nucleosome dynamics)
- **Genomic stability** - Central to preventing mutations and cancer
- **Chromatin integrity** - FACT and remodelers disassemble, reposition and reassemble nucleosomes during transcription, replication and repair
- **Disease models** - Defects in yeast homologs found in cancer and hereditary disorders

## Project Goals

- Review genes central to DNA damage response and repair pathways
- Assess GO annotations for DNA repair, chromatin remodeling, and histone dynamics
- Identify genes at the intersection of DNA repair and chromatin handling
- Incorporate emerging structural biology insights (FACT-replisome complexes)
- Create reference for DNA repair and chromatin dynamics research

---

# STATUS

Last updated: 2026-10-05

## Genes to Review

### DNA Damage Sensing & Checkpoints
- Todo: RAD9 - DNA damage checkpoint adaptor
- Todo: `CHK1` - DNA damage checkpoint kinase
- Todo: DUN1 - Effector kinase for RNR induction

### Homologous Recombination - Early Steps
- Todo: `MRE11` - MRN complex (DNA end recognition, resection)
- Todo: RAD50 - MRN complex (DNA end tethering)
- Todo: XRS2 - MRN complex (nuclear localization)
- Todo: SAE2 - `MRE11` cofactor (end processing)

### Homologous Recombination - Core Machinery
- Todo: `RAD51` - Recombinase (filament formation, strand invasion)
- Todo: RAD52 - RPA-`RAD51` mediator (recombination intermediates)
- Todo: RAD54 - dsDNA translocase (chromatin remodeling for HR)
- Todo: RAD55 - `RAD51` cofactor
- Todo: RAD57 - `RAD51` cofactor

### FACT Complex & Chromatin Remodeling at Replication/Repair
- Draft: SPT16 - FACT complex (histone chaperone, H2A/H2B transfer)
- Complete: POB3 - SSRP1 homolog (FACT complex partner)
- In progress: CHD1 - Chromatin remodeler
- Complete: SWI1 - SWI/SNF complex (chromatin remodeling)

### Nucleotide Excision Repair & Damage Tolerance
- Todo: `RAD3` - TFIIH helicase for nucleotide excision repair
- Todo: REV3 - DNA polymerase ζ catalytic subunit for translesion synthesis

### Mismatch Repair
- Todo: MSH2 - `MutS` homolog (mismatch recognition)
- Todo: MSH6 - `MutS` homolog (mismatch specificity)
- Todo: MLH1 - `MutL` homolog (endonuclease licensing)
- Todo: PMS1 - MLH1 partner

### General DNA Repair & Checkpoint Recovery
- Todo: RNR1 - Ribonucleotide reductase (dNTP synthesis)
- Todo: RNR2 - Ribonucleotide reductase (damage-inducible)
- Todo: RNR3 - Ribonucleotide reductase (damage-inducible)
- Todo: RNR4 - Ribonucleotide reductase (damage-inducible)

## Progress

- Total checklist rows: 26
- Distinct genes: 26
- Reviews present: 4
- Complete reviews: 2
- Draft/in-progress reviews: 2
- Open review rows: 22
- Remaining work: [#3963](https://github.com/ai4curation/ai-gene-review/issues/3963)

---

# NOTES

## 2025-12-30

- Project initialized
- Focus: DNA damage response, homologous recombination, chromatin dynamics during repair
- Selected 28 genes spanning DNA sensing, HR machinery, FACT complex, BER, and MMR
- Emphasis on structural biology insights (FACT-replisome, histone recycling, chromatin reconfiguration)
- Ready to begin gene review workflow
