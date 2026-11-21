---
title: "Nematode Pathogens"
description: "Modules and gene reviews for parasitic nematode cuticle, host-interface, and drug-target biology."
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [BRUMA, HAECO, ONCVO, ASCSU, STRRB, STRER, TOXCA, TRITR, STECR, 9BILA, worm]
genes: [dpy-31, bma-dpy-18.1, bma-dpy-18.2, far-1, lev-1, cpi-2, gp29, mf1]
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
- [x] `BRUMA` `bma-dpy-18.1` / Q68VC1 - fetched and reviewed the `Bma-PHY-2` prolyl 4-hydroxylase alpha subunit
- [x] `BRUMA` `bma-dpy-18.2` / A0A1P6BZ71 - fetched and reviewed the Bma-PHY-1 prolyl 4-hydroxylase alpha subunit
- [x] `worm` `dpy-18` / Q10576 - fetched and reviewed the C. elegans prolyl 4-hydroxylase alpha-1 ortholog
- [x] `worm` `phy-2` / Q20065 - fetched and reviewed the C. elegans prolyl 4-hydroxylase alpha-2 paralog
- [x] `worm` `pdi-2` / Q17770 - fetched and reviewed the PDI/prolyl 4-hydroxylase beta subunit
- [x] `worm` `bli-4` / P51559 - fetched and reviewed the subtilisin-like convertase

Secondary cuticle candidates to resolve before fetching: ONCVO Q2YFS7 and
A0A8R1U276, ASCSU F1LHZ4/F1L4T8 and transcript duplicates, STRRB A0A090LLW4,
STRER A0A0K0DV69 and A0A0K0E1H2, TOXCA dpy-31-like duplicates, and TRITR
A0A077YYY8. Resolve duplicates by gene model, family/subfamily, sequence, and
literature before choosing review folders.

### 2. Anthelmintic drug target systems

Treat target biology, not drug class, as the module boundary. Candidate modules
are the levamisole-sensitive nicotinic acetylcholine receptor, avermectin-
sensitive glutamate-gated chloride channels, and beta-tubulin microtubules.
The first anthelmintic draft is
`modules/nematode_levamisole_sensitive_nachr.yaml`, centered on the C. elegans
five-subunit L-AChR and the RIC-3/UNC-50/UNC-74 expression factors.

Levamisole-sensitive nicotinic acetylcholine receptor:

- [x] `worm` `unc-29` / P48181 - existing nAChR beta-type receptor subunit review reused and cross-checked as the non-alpha anchor for the new L-AChR module
- [x] `worm` `lev-1` / Q27218 - fetched and reviewed as the second non-alpha L-AChR pore subunit
- [ ] `worm` `unc-38` / Q23022 - fetch and review as an alpha L-AChR pore subunit
- [ ] `worm` `unc-63` / Q9N587 - fetch and review as an alpha L-AChR pore subunit
- [ ] `worm` `lev-8` / Q93329 - fetch and review as the fifth C. elegans L-AChR pore subunit
- [ ] `worm` `ric-3` / Q22472 - fetch and review as a receptor maturation/assembly ancillary factor
- [ ] `worm` `unc-50` / Q10045 - fetch and review as an L-AChR trafficking ancillary factor
- [ ] `worm` `unc-74` / Q9N4L6 - fetch and review as the thioredoxin-domain L-AChR ancillary factor

Parasite L-AChR candidates to resolve before fetching: BRUMA A0A1P6C5A7,
A0A4E9EUJ4, A0A4E9FKF9 and the short UniProt `Bma-acr-8.1` record A0A4E9EXN3;
HAECO D6MYE9, D6MYF0, D6MYF1, D6MYF2, D6MYF3, D6MYF4, D6MYF5, D6MYF6,
A0A7I4XYK7, A0A7I4Z1Z2, A0A7I4Z2R2, A0A7I4XVV4, A0A7I4XVC3, A9XX24,
A0A7I4YXE5, A0A7I4YWD8, D2XI63, P92039, G0XFE0, G0XFE1, G0XFD9 and G0XFD8;
ONCVO P54247 and the A0A8R1* PTHR18945 candidates, with the ACR-8-like member
still unresolved from anonymous live UniProt labels; ASCSU A0A2I6TEN1,
A0ACT4VCM3, A0ACT4VCM4, A0ACT4VCM5, A0ACT4VCM6, A0ACT4VCM7, F1KYN0,
F1L123, F1L348, F1L897 and O96760. Resolve broad PTHR18945 Cys-loop
membership, ACR-8 placement, cloned paralogs, truncated entries and gene-model
duplicates before choosing review folders.

Avermectin-sensitive glutamate-gated chloride channels:

- [ ] `worm` `glc-1` / G5EBR3 - fetch if the GluCl module proceeds
- [ ] `worm` `glc-2` / Q17328 - fetch if the GluCl module proceeds

Beta-tubulin/benzimidazole target biology:

- [ ] C. elegans beta-tubulins - decide whether the benzimidazole target is a multi-part microtubule module or a gene-family review lane before fetching

### 3. Secreted fatty-acid and retinol binding

Potential module or family review target for FAR proteins, with the boundary
still to be decided. If FAR-1 remains a single binding role rather than a
multi-part process, keep it as gene/family curation until it can be joined to a
broader host lipid-scavenging module.

- [x] `BRUMA` `far-1` / Q93142 - cross-check existing review
- [x] `worm` `far-1` / P34382 - fetch and review the same PANTHER subfamily exemplar
- [ ] `worm` `far-2` / P34383 - fetch only if needed for paralog-specific comparison

### 4. Secreted immune modulators and exsheathment enzymes

These are strong parasite-interface genes but do not yet form one reusable
module. Split them by mechanism unless literature supports a shared pathway.

- [ ] `BRUMA` `cpi-2` / A0A0K0IP23 - existing cystatin review; C. elegans same-subfamily comparator is `worm` `cpi-2` / G5ECM9
- [ ] `BRUMA` `mf1` / P29030 - existing GH18 endochitinase review; C. elegans same-subfamily comparator is `worm` `cht-1` / Q11174
- [ ] `STECR` `nas-8` / D2KBH9 - existing secreted astacin review in the DPY-31/NAS PANTHER family but not the DPY-31 subfamily

### 5. Surface antioxidant defense

Start as a small extracellular glutathione peroxidase lane and merge only after
the extracellular oxidant-detoxification boundary is clear.

- [ ] `BRUMA` `gp29` / P67877 - existing cuticular glutathione peroxidase review
- [ ] `worm` `gpx-3` / Q95003 - fetch and review the same PANTHER subfamily exemplar
- [ ] `worm` `gpx-5` / Q93204 - cross-check existing review as a secreted-gpx comparator, not as an established one-to-one ortholog

# STATUS

## 2026-11-20

- [x] Read `CLAUDE.md`, `.claude/skills/module-curation`, `.claude/skills/review`, `.claude/skills/annotation-reviewer`, `.claude/skills/pm`, `.claude/skills/aigr-pr-review`, and `modules/README.md`
- [x] Inventory existing BRUMA, STECR, worm, CAEEL, CAEBR, module, and project coverage
- [x] Verify UniProt mnemonics for initial parasitic nematodes before using them in paths
- [x] Choose the first real multi-part module: nematode cuticle collagen maturation
- [x] Add `modules/nematode_cuticle_collagen_maturation.yaml`
- [x] Create the `worm` `dpy-31` review for the C. elegans DPY-31 ortholog
- [x] Create the `HAECO` `dpy-31` review for the H. contortus DPY-31 ortholog
- [x] Add or cross-check the remaining first-wave cuticle member gene reviews

## 2026-11-21

- [x] Cross-check the initialized `BRUMA` `far-1` review for the secreted
  filarial fatty-acid and retinol-binding protein Bm20
- [x] Fetch and review the `worm` `far-1` P34382 same-subfamily ortholog
- [x] Fetch and review the `BRUMA` `bma-dpy-18.1` Q68VC1 prolyl
  4-hydroxylase alpha subunit
- [x] Fetch and review the `BRUMA` `bma-dpy-18.2` A0A1P6BZ71 prolyl
  4-hydroxylase alpha subunit
- [x] Fetch and review the `worm` `dpy-18` Q10576 prolyl
  4-hydroxylase alpha-1 subunit
- [x] Fetch and review the `worm` `phy-2` Q20065 prolyl
  4-hydroxylase alpha-2 subunit
- [x] Fetch and review the `worm` `pdi-2` Q17770 PDI/prolyl
  4-hydroxylase beta subunit
- [x] Fetch and review the `worm` `bli-4` P51559 subtilisin-like
  proprotein convertase
- [x] Move anthelmintic drug target systems ahead of the FAR,
  immune-modulator, and antioxidant lanes for the next module after cuticle
  collagen maturation
- [x] Add a draft levamisole-sensitive nicotinic acetylcholine receptor module
  with the five C. elegans pore subunits, RIC-3/UNC-50/UNC-74 ancillary
  factors, and UniProt-resolved BRUMA, HAECO, ONCVO and ASCSU candidate lists
- [x] Expand the L-AChR parasite queue with ACR-8 candidates after HAECO
  reconstitution and resistance evidence showed parasite pore composition is not
  a one-to-one LEV-8 projection
- [x] Fetch and review the `worm` `lev-1` Q27218 non-alpha L-AChR
  pore subunit

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
- HAECO L-AChR oocyte reconstitution identified Hco-ACR-8 as important for
  selective levamisole sensitivity (PMID:21486278, *Br J Pharmacol* 2011), and
  Hco-acr-8b truncation/resistance papers make ACR-8 a named
  parasite-specific resolution lane rather than a simple C. elegans LEV-8
  ortholog slot (PMID:21945142, *Mol Biochem Parasitol* 2011; PMID:24503202,
  *Int J Parasitol* 2014). All three records are now cached in `publications/`.
- UniProtKB live query receipt for ACR-8 candidates: exact-accession query
  against release 2026_04, dated 2026-11-04, returned BRUMA A0A4E9EXN3
  (`Bma-acr-8.1`; "Neurotransmitter-gated ion-channel ligand-binding
  domain-containing protein"); HAECO A9XX24 and A0A7I4YXE5 ("Nicotinic
  acetylcholine receptor 8"), A0A7I4YWD8 ("Nicotinic acetylcholine receptor
  8"), and D2XI63 (`acr8`; "Nicotinic acetylcholine receptor alpha subunit
  isoform b"); and ASCSU A0A2I6TEN1, A0ACT4VCM3, A0ACT4VCM4, A0ACT4VCM5,
  A0ACT4VCM6 and A0ACT4VCM7 (all "Nicotinic acetylcholine receptor alpha
  subunit 8", no gene name in UniProt). The ONCVO ACR-8 member remains to be
  placed among anonymous PTHR18945 A0A8R1* records.
- Added `genes/worm/lev-1` and curated LEV-1 as the second non-alpha pore
  subunit of the five-subunit C. elegans L-AChR. The review adds the missing
  neuromuscular synaptic transmission row, refines generic Cys-loop receptor,
  channel, transport, membrane, and membrane-potential rows in parallel with
  `unc-29`, and keeps calcium flux, neuronal localization, locomotion, and
  egg-laying behavior as non-core contexts.
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
- Added `genes/worm/far-1` for P34382, the same `PTHR31418:SF7` FAR-1
  subfamily exemplar as B. malayi FAR-1. Direct QuickGO and UniProt
  cross-checks found live InterPro lipid-binding and UniProtKB-SubCell
  extracellular-region rows for P34382, and the review proposes more specific
  fatty-acid and retinol-binding rows from the Ce-FAR recombinant ligand
  assays in PMID:12502713. No C. elegans biological-process term was proposed:
  native FAR-1 cargoes and far-1 loss-of-function phenotypes remain explicit
  open questions.
- Added `genes/BRUMA/bma-dpy-18.1` for Q68VC1, the `Bma-PHY-2` collagen
  prolyl 4-hydroxylase alpha subunit. The UniProt symbol resolver initially
  selected the shorter duplicate A0A4E9F4D5 for the same WormBase gene, so the
  review was re-fetched with `--uniprot-id Q68VC1`; the curated review keeps
  the core ER-lumen procollagen-proline 4-dioxygenase activity, adds the
  directly supported native procollagen-proline 4-dioxygenase complex
  membership, and treats broad cofactor/oxygenase terms and generic embryonic
  or growth process transfers as accepted, refined, or over-annotated
  according to the Q68VC1 evidence.
- Added `genes/BRUMA/bma-dpy-18.2` for A0A1P6BZ71, the Bm3843
  procollagen-proline 4-dioxygenase that matches the cloned Bma-PHY-1
  sequence. The review keeps the seeded core ER-lumen
  procollagen-proline 4-dioxygenase activity and the direct larval-development
  phenotype, refines broad oxygenase rows to collagen P4H activity, and adds
  direct annotations to the native prolyl 4-hydroxylase complex and
  collagenous-cuticle development from the Bma-PDI-2 co-IP and combined
  `Bma-phy-1`/`Bma-phy-2` RNAi evidence.
- Added `genes/worm/dpy-18` for Q10576, the C. elegans PHY-1 prolyl
  4-hydroxylase alpha subunit. The review keeps direct and PAINT
  procollagen-proline 4-dioxygenase activity, accepts the informative ER and
  ER-lumen rows, treats embryonic hatching, basement-membrane morphogenesis,
  and multicellular growth as non-core phenotype/context rows, and marks the
  tunicamycin high-throughput expression row for IRE1-mediated unfolded
  protein response as over-annotated.
- Added `genes/worm/phy-2` for Q20065, the C. elegans PHY-2 prolyl
  4-hydroxylase alpha-2 subunit. The review keeps PAINT and
  EC/Rhea-supported procollagen-proline 4-dioxygenase activity, accepts
  PDI-2-containing procollagen-proline 4-dioxygenase complex membership and
  ER/ER-lumen localization, refines broad peptidyl-proline and paired-donor
  oxygenase activities to the collagen P4H reaction, and adds a conservative
  direct cuticle-development row without copying the downstream
  dpy-18-specific phenotype annotations onto buffered phy-2.
- Added `genes/worm/pdi-2` for Q17770, the C. elegans PDI-2
  protein-disulfide-isomerase and procollagen-proline 4-dioxygenase beta
  subunit. The review accepts the ER-lumen PDI/P4H-beta role, adds direct
  collagenous-cuticle development from the pdi-2 RNAi phenotype and the
  PHY-1/PHY-2/PDI-2 complex literature, keeps the broad ER-stress response row
  as non-core, marks the tunicamycin high-throughput expression row for
  IRE1-mediated unfolded protein response as over-annotated, and leaves the
  transglutaminase-like activity rows undecided pending full text of the
  abstract-only PDI-3 paper.
- Added `genes/worm/bli-4` for P51559, the C. elegans furin/Kex2-like
  proprotein convertase that anchors the N-terminal cuticle-collagen
  processing step. The review accepts the core serine endopeptidase and
  collagenous-cuticle process rows, proposes a direct non-core peptide hormone
  processing row for the ASEL INS-6 high-salt circuit, treats root proteolysis
  and membrane rows as too general beside protein processing and Golgi/TGN
  location, and leaves the old nucleus row plus neuromuscular-junction
  synaptic-assembly rows undecided because the relevant 1995 and 2013 papers
  are abstract-only locally.
- Ros-orchestrate reprioritized anthelmintic drug target systems as the next
  module lane after cuticle collagen maturation. Keep the mechanism split:
  scope levamisole-sensitive nicotinic acetylcholine receptors,
  avermectin-sensitive glutamate-gated chloride channels, and
  beta-tubulin/benzimidazole as separate candidate modules, resolving parasite
  orthologs from UniProt/PANTHER before adding HAECO, BRUMA, ONCVO, ASCSU, or
  other accessions.
- Added `modules/nematode_levamisole_sensitive_nachr.yaml` as the first
  anthelmintic target module. The draft models the C. elegans
  levamisole-sensitive AChR as a five-subunit UNC-29/LEV-1/UNC-38/UNC-63/LEV-8
  acetylcholine-gated cation channel plus RIC-3, UNC-50 and UNC-74 ancillary
  expression factors. The parasite accessions from BRUMA, HAECO, ONCVO and
  ASCSU are listed as candidates to resolve rather than as asserted
  one-to-one orthologs, because UniProt/PTHR18945 currently mixes L-AChR,
  GluCl, GABA/glycine, MOD-1-like, ACR-16-like and monepantel-channel records.
