---
title: "Nematode Pathogens"
description: "Modules and gene reviews for parasitic nematode cuticle, host-interface, and drug-target biology."
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [BRUMA, HAECO, ONCVO, ASCSU, STRRB, STRER, TOXCA, TRITR, STECR, 9BILA, worm]
genes: [dpy-31, bma-dpy-18.1, bma-dpy-18.2, far-1, cpi-2, gp29, mf1]
index_group: OTHER_ORGANISM
---

# Nematode Pathogens

## Overview

This project curates reusable modules and gene reviews for biology that makes
animal-parasitic nematodes infective, druggable, or able to survive at the host
interface. It starts from the existing *Brugia malayi* Swiss-Prot set and then
adds orthologous or same-role proteins from other parasitic nematodes plus the
*Caenorhabditis elegans* comparator in `genes/worm/` whenever the ortholog or
same PANTHER subfamily is clear.

Verified UniProt mnemonics in scope:

| Species | Mnemonic | NCBI taxon | Role in this project |
|---|---:|---:|---|
| *Brugia malayi* | `BRUMA` | 6279 | Initial filarial anchor; five existing reviewed secreted/surface/cuticle proteins |
| *Haemonchus contortus* | `HAECO` | 6289 | Strongyle gastrointestinal parasite with a reviewed DPY-31 ortholog |
| *Onchocerca volvulus* | `ONCVO` | 6282 | Human filarial pathogen; dpy-31-like candidates need duplicate resolution |
| *Ascaris suum* | `ASCSU` | 6253 | Ascarid helminth; dpy-31-like candidates need duplicate resolution |
| *Strongyloides ratti* | `STRRB` | 34506 | Rodent threadworm comparator |
| *Strongyloides stercoralis* | `STRER` | 6248 | Human threadworm pathogen |
| *Toxocara canis* | `TOXCA` | 6265 | Canine roundworm; dpy-31-like candidates need duplicate resolution |
| *Trichuris trichiura* | `TRITR` | 36087 | Human whipworm |
| *Steinernema carpocapsae* | `STECR` | 34508 | Existing entomopathogenic nematode astacin review |
| *Steinernema hermaphroditum* | `9BILA` | 289476 | Emerging entomopathogenic model; provisional UniProt mnemonic |
| *C. elegans* | `worm` | 6239 | Genetic comparator for orthologous nematode biology |

`BRUA2` is not in scope: it is *Brucella abortus* 2308, not a *Brugia*
mnemonic.

## Prioritized modules

### 1. Nematode cuticle collagen maturation

First ModuleReview target: `modules/nematode_cuticle_collagen_maturation.yaml`.

The modeled boundary is the core cuticle-collagen maturation workflow: ER
prolyl 4-hydroxylation by prolyl 4-hydroxylase alpha plus PDI/beta subunits,
subtilisin-like cleavage of collagen precursors, and extracellular DPY-31-family
C-terminal processing. The module is pathogen-relevant because molting and
cuticle assembly are essential in parasitic nematodes, and the first existing
anchor, `BRUMA/dpy-31`, is in the same PANTHER subfamily as *C. elegans*
`dpy-31`.

- [x] `BRUMA` `dpy-31` / A8Q2D1 - cross-check existing review against the module
- [x] `worm` `dpy-31` / P98060 - fetched and reviewed the C. elegans DPY-31 ortholog
- [x] `HAECO` `dpy-31` / D5FM34 - fetched and reviewed the reviewed *H. contortus* DPY-31 ortholog
- [ ] `BRUMA` `bma-dpy-18.1` / Q68VC1 - fetch and review a prolyl 4-hydroxylase alpha candidate
- [ ] `BRUMA` `bma-dpy-18.2` / A0A1P6BZ71 - fetch and review the second prolyl 4-hydroxylase alpha candidate
- [ ] `worm` `dpy-18` / Q10576 - fetch and review the C. elegans prolyl 4-hydroxylase alpha-1 ortholog
- [ ] `worm` `phy-2` / Q20065 - fetch and review the C. elegans prolyl 4-hydroxylase alpha-2 ortholog
- [ ] `worm` `pdi-2` / Q17770 - fetch and review the PDI/prolyl 4-hydroxylase beta subunit
- [ ] `worm` `bli-4` / P51559 - fetch and review the subtilisin-like convertase

Secondary cuticle candidates to resolve before fetching: ONCVO Q2YFS7 and
A0A8R1U276, ASCSU F1LHZ4/F1L4T8 and transcript duplicates, STRRB A0A090LLW4,
STRER A0A0K0DV69 and A0A0K0E1H2, TOXCA dpy-31-like duplicates, and TRITR
A0A077YYY8. Resolve duplicates by gene model, family/subfamily, sequence, and
literature before choosing review folders.

### 2. Secreted fatty-acid and retinol binding

Potential module or family review target for FAR proteins, with the boundary
still to be decided. If FAR-1 remains a single binding role rather than a
multi-part process, keep it as gene/family curation until it can be joined to a
broader host lipid-scavenging module.

- [x] `BRUMA` `far-1` / Q93142 - cross-check existing review
- [ ] `worm` `far-1` / P34382 - fetch and review the same PANTHER subfamily exemplar
- [ ] `worm` `far-2` / P34383 - fetch only if needed for paralog-specific comparison

### 3. Secreted immune modulators and exsheathment enzymes

These are strong parasite-interface genes but do not yet form one reusable
module. Split them by mechanism unless literature supports a shared pathway.

- [ ] `BRUMA` `cpi-2` / A0A0K0IP23 - existing cystatin review; C. elegans same-subfamily comparator is `worm` `cpi-2` / G5ECM9
- [ ] `BRUMA` `mf1` / P29030 - existing GH18 endochitinase review; C. elegans same-subfamily comparator is `worm` `cht-1` / Q11174
- [ ] `STECR` `nas-8` / D2KBH9 - existing secreted astacin review in the DPY-31/NAS PANTHER family but not the DPY-31 subfamily

### 4. Surface antioxidant defense

Start as a small extracellular glutathione peroxidase lane and merge only after
the extracellular oxidant-detoxification boundary is clear.

- [ ] `BRUMA` `gp29` / P67877 - existing cuticular glutathione peroxidase review
- [ ] `worm` `gpx-3` / Q95003 - fetch and review the same PANTHER subfamily exemplar
- [ ] `worm` `gpx-5` / Q93204 - cross-check existing review as a secreted-gpx comparator, not as an established one-to-one ortholog

### 5. Anthelmintic drug target systems

Treat target biology, not drug class, as the module boundary. Candidate modules
are the levamisole-sensitive nicotinic acetylcholine receptor, avermectin-
sensitive glutamate-gated chloride channels, and beta-tubulin microtubules.
Pathogen accessions need UniProt and literature resolution before fetching.

- [ ] `worm` `unc-29` / P48181 - existing nAChR beta-type receptor subunit review
- [ ] `worm` `lev-1` / Q27218 - fetch if the nAChR module proceeds
- [ ] `worm` `unc-38` / Q23022 - fetch if the nAChR module proceeds
- [ ] `worm` `unc-63` / Q9N587 - fetch if the nAChR module proceeds
- [ ] `worm` `glc-1` / G5EBR3 - fetch if the GluCl module proceeds
- [ ] `worm` `glc-2` / Q17328 - fetch if the GluCl module proceeds

# STATUS

## 2026-11-20

- [x] Read `CLAUDE.md`, `.claude/skills/module-curation`, `.claude/skills/review`, `.claude/skills/annotation-reviewer`, `.claude/skills/pm`, `.claude/skills/aigr-pr-review`, and `modules/README.md`
- [x] Inventory existing BRUMA, STECR, worm, CAEEL, CAEBR, module, and project coverage
- [x] Verify UniProt mnemonics for initial parasitic nematodes before using them in paths
- [x] Choose the first real multi-part module: nematode cuticle collagen maturation
- [x] Add `modules/nematode_cuticle_collagen_maturation.yaml`
- [x] Create the `worm` `dpy-31` review for the C. elegans DPY-31 ortholog
- [x] Create the `HAECO` `dpy-31` review for the H. contortus DPY-31 ortholog
- [ ] Add or cross-check the remaining first-wave cuticle member gene reviews

## 2026-11-21

- [x] Cross-check the initialized `BRUMA` `far-1` review for the secreted
  filarial fatty-acid and retinol-binding protein Bm20
- [ ] Fetch and review the `worm` `far-1` P34382 same-subfamily ortholog

# NOTES

## 2026-11-20

- `genes/BRUMA` currently contains `cpi-2`, `dpy-31`, `far-1`, `gp29`, and
  `mf1`; all five have review YAML and rendered HTML. They have no local notes
  or deep-research files yet.
- `genes/STECR/nas-8` has review YAML and HTML for the entomopathogenic
  *Steinernema* astacin anchor.
- Existing history covers `BRUMA/cpi-2` and `STECR/nas-8`, but not the other
  BRUMA seeds.
- `projects/PARASITES.md` already scouted the BRUMA and STECR set and
  `projects/PARASITE_IMMUNE_MODULATORS.md` leaves nematodes to that umbrella.
  This page narrows the next work to module-scale nematode pathogen biology.
- No existing module models nematode cuticle collagen maturation, FAR host lipid
  scavenging, filarial cystatin/chitinase/GPX secretion, or anthelmintic target
  systems. The existing C. elegans modules cover PMK-1 immunity, DBL-1 body-size
  signaling, DAF-2 signaling, cGMP sensory transduction, P granules, 22G RNAs,
  lysosomal lipid signaling, JAK-independent STAT signaling, core apoptosis, and
  translation surveillance immunity.
- PANTHER `PTHR10127:SF813` places BRUMA A8Q2D1, HAECO D5FM34, and worm P98060
  together as DPY-31/NAS-35 orthologs. ONCVO, ASCSU, STRRB, STRER, TOXCA, and
  TRITR have dpy-31-like entries but need duplicate/model resolution before
  curation.
- PANTHER same-subfamily checks also matched BRUMA FAR-1 to worm FAR-1
  (`PTHR31418:SF7`), BRUMA CPI-2 to worm CPI-2 (`PTHR46186:SF2`), BRUMA MF1 to
  worm CHT-1 (`PTHR11177:SF400`), and BRUMA GP29 to worm GPX-3
  (`PTHR11592:SF88`).
- Added the first draft of `modules/nematode_cuticle_collagen_maturation.yaml`
  with three ordered processing steps: ER procollagen prolyl 4-hydroxylation,
  BLI-4-dependent N-terminal cleavage before secretion, and DPY-31-dependent
  extracellular C-terminal cleavage.
- Added `genes/worm/dpy-31` and curated DPY-31/NAS-35 as the C. elegans
  zinc-dependent extracellular procollagen C-proteinase that processes SQT-3
  C termini during collagenous cuticle formation and molting. Falcon and
  Perplexity Lite deep-research providers were unavailable, so the review uses
  the cached WormBase gene description, the full text of PMID:15579684, the
  cached PMID:19883650 abstract, UniProt sequence features, and PAINT loss
  checks.
- Cross-checked the initialized `genes/BRUMA/dpy-31` review for A8Q2D1 against
  the new cuticle module and the freshly reviewed worm DPY-31 ortholog. The
  updated review keeps all Brugia DPY-31 cuticle-collagen assignments, records
  the 2026 action treatment for the generic metallopeptidase parent row, and
  adds local supporting quotes from the B. malayi recombinant cleavage and
  inhibitor literature.
- Added `genes/HAECO/dpy-31` and curated D5FM34 as the H. contortus DPY-31
  ortholog. The review keeps the same six GOA rows as BRUMA DPY-31, anchors the
  molecular function and collagenous-cuticle process to the Stepek/Page abstract
  reporting H. contortus dpy-31 rescue of a C. elegans dpy-31 mutant and
  recombinant SQT-3 cleavage, and leaves parasite-native H. contortus substrates
  and in-species loss-of-function phenotypes as explicit biology gaps.

## 2026-11-21

- Cross-checked `genes/BRUMA/far-1` as the Q93142/Bm20 filarial FAR protein in
  PANTHER `PTHR31418:SF7`. The existing direct fatty-acid and retinol-binding
  rows were sound; the InterPro2GO `lipid binding` parent is now treated as a
  true-but-too-general row beside the direct ligand annotations, and the review
  records an explicit remaining gap around native in vivo cargoes and far-1
  loss-of-function phenotypes in *B. malayi*.
