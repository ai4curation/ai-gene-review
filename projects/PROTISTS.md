---
title: "Protists"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [PLAF7, TOXGM, TOXGO, TRYB2, TRYBB, LEIMA, TETTS, PARTE, GIAIC, TRIV3, ENTH1, PHATC, THAPS, DICDI, CHLRE, SALRS, MONBE, CAPO3]
genes: [A0BFB4, A2FPI7, B7FXQ8]
autolink_exclude: [AMA1, TERT, rod, Sil1, sil1]
---

# Protists: Gene Function Outside Animals, Fungi and Plants

**Bottom line:** most of the diversity of eukaryotes is protist, but very little
of this repository is. Of 7,176 gene folders, about 104 (1.4%) are protists, and
62 of those are *Dictyostelium*. We have no reviews at all for the parasites that
carry most protist GO curation (*Plasmodium*, *Toxoplasma*, trypanosomes,
*Leishmania*), nor for the ciliate and diatom models. This project sets out to
fill that gap, lineage by lineage, starting with a seed list of 27 well-studied
genes whose UniProt accessions we have checked.

"Protist" is not a clade. Here it means any eukaryote that is not an animal, a
fungus or a land plant. Green algae and the unicellular relatives of animals
fall inside this definition, but other projects already cover them (see
[Related projects](#related-projects)), so this project only tracks them.

## Why protists need their own project

1. **Curation is concentrated in a few databases, and GO coverage is uneven.**
   Experimental annotation of protists comes mainly from dictyBase,
   VEuPathDB/GeneDB (apicomplexans and kinetoplastids) and a few UniProt
   curators. Outside these, organisms with tens of thousands of IBA rows have
   almost no experimental rows (table below).
2. **Function is inferred mostly from animals, fungi and plants.** IBA and IEA
   transfer to divergent lineages is where over-annotation is most likely:
   animal-specific processes, ancestral activities that a lineage has lost, and
   localisations to organelles a protist does not have (or has in a modified
   form, such as the apicoplast, kinetoplast, hydrogenosome or mitosome).
3. **Many protist functions are lineage-specific and have no animal homolog.**
   Examples are antigenic variation, RNA editing, programmed genome
   rearrangement, apical-complex invasion and silica biomineralisation. GO
   terms for these may be missing or awkward, which makes them a good source of
   `proposed_new_terms`.
4. **They matter for health and the environment.** Malaria, toxoplasmosis,
   sleeping sickness, leishmaniasis, amoebiasis, giardiasis and trichomoniasis
   are protist diseases. Diatoms carry out roughly a fifth of global
   photosynthesis.

### GOA census (2026-10-14)

Annotation counts from the QuickGO API, for the exact taxon of each strain
(descendant taxa are not included). "Experimental" means evidence codes
descending from ECO:0000269 (EXP, IDA, IPI, IMP, IGI, IEP).

| Organism | Code | Taxon | Experimental | IBA | Our reviews |
|---|---|---:|---:|---:|---:|
| *Dictyostelium discoideum* | DICDI | 44689 | 10,128 | 19,137 | 62 |
| *Trypanosoma brucei* TREU927 | TRYB2 | 185431 | 12,149 | 12,281 | 0 |
| *Plasmodium falciparum* 3D7 | PLAF7 | 36329 | 2,830 | 9,002 | 0 |
| *Chlamydomonas reinhardtii* | CHLRE | 3055 | 546 | 24,014 | 19 |
| *Giardia intestinalis* WB | GIAIC | 184922 | 343 | 6,081 | 0 |
| *Entamoeba histolytica* HM-1:IMSS | ENTH1 | 294381 | 197 | 13,213 | 0 |
| *Plasmodium berghei* ANKA | PLABA | 5823 | 148 | 0 | 0 |
| *Tetrahymena thermophila* SB210 | TETTS | 312017 | 124 | 0 | 0 |
| *Toxoplasma gondii* ME49 | TOXGM | 508771 | 35 | 0 | 0 |
| *Trypanosoma cruzi* CL Brener | TRYCC | 353153 | 29 | 0 | 0 |
| *Phaeodactylum tricornutum* | PHATC | 556484 | 17 | 0 | 1 |
| *Paramecium tetraurelia* | PARTE | 5888 | 11 | 49,383 | 1 |
| *Trichomonas vaginalis* G3 | TRIV3 | 412133 | 6 | 31,122 | 1 |
| *Thalassiosira pseudonana* | THAPS | 35128 | 2 | 16,157 | 0 |
| *Leishmania major* Friedlin | LEIMA | 347515 | 0 | 0 | 0 |

Several counts need checking before we rely on them. The *Leishmania major*
Friedlin taxon has only 529 annotations in total, so its curation is probably
filed under a different taxon id. *Toxoplasma* annotations may be split across
strains (ME49, GT1, RH). And the high *T. brucei* experimental count probably
comes largely from a genome-wide localisation screen, which would make it mostly
cellular-component rows. A first task is to redo the census by species
(including descendants) and by GO aspect.

## Scope

In scope: gene products of eukaryotes outside Metazoa, Fungi and Embryophyta,
reviewed with the standard gene-review workflow. The project is organised into
tracks by lineage, roughly following the eukaryote supergroups:

| Track | Lineage | Model organisms | Status |
|---|---|---|---|
| A | Apicomplexa (Alveolata) | *P. falciparum*, *T. gondii* | not started |
| B | Kinetoplastida (Discoba) | *T. brucei*, *L. major* | not started |
| C | Ciliates (Alveolata) | *Tetrahymena*, *Paramecium* | 1 draft (PARTE) |
| D | Metamonads and *Entamoeba* | *Giardia*, *Trichomonas*, *E. histolytica* | 1 draft (TRIV3) |
| E | Stramenopiles | *Phaeodactylum*, *Thalassiosira*; oomycetes later | 1 draft (PHATC) |
| F | Amoebozoa | *Dictyostelium* | mature: [DICTYOSTELIUM_DEVELOPMENT](DICTYOSTELIUM_DEVELOPMENT.md) |
| G | Green algae (Archaeplastida) | *Chlamydomonas* | covered by [CO2_CONCENTRATING_MECHANISMS](CO2_CONCENTRATING_MECHANISMS.md) |
| H | Holozoan relatives of animals | choanoflagellates, *Capsaspora* | covered by [ORIGINS_OF_MULTICELLULARITY](ORIGINS_OF_MULTICELLULARITY.md) |

Tracks F to H are counted here so the project can report protist coverage as a
whole, but new work on them belongs to their own projects. Lineages with no
model organism in the repository yet (Rhizaria, haptophytes, cryptophytes,
euglenids, red algae) are out of scope for the first phase.

## What to look for in each review

These are the review questions most specific to protists. They add to the
normal guidelines in `CLAUDE.md`; they do not replace them.

- **Taxon-inappropriate terms.** Flag electronic terms that describe animal-only
  biology (for example immune or nervous-system processes, or
  `extracellular matrix` in organisms without one) or plant-only biology.
- **Lost or modified organelles.** Check `mitochondrion` annotations on
  *Giardia*, *Entamoeba* and *Trichomonas* (they have mitosomes or
  hydrogenosomes instead), and check plastid annotations on apicomplexans (the
  apicoplast is non-photosynthetic).
- **Paralog expansions.** Protist genomes often carry large lineage-specific
  families (PfEMP1/*var*, VSGs, *Giardia* VSPs, *Trichomonas* BspA-like
  proteins). IBA and IEA rows may be assigned to the wrong subfamily.
- **Host–pathogen terms.** Use the GO "symbiont" and "host" process terms
  correctly. A parasite protein acts *on* the host; it is not a participant in
  the host's own processes.
- **Ontology gaps.** Record missing terms for lineage-specific processes as
  `proposed_new_terms` and in the gene notes. They are not knowledge gaps.

## Related projects

- [DICTYOSTELIUM_DEVELOPMENT](DICTYOSTELIUM_DEVELOPMENT.md): 62 *Dictyostelium*
  reviews in 14 development modules.
- [ORIGINS_OF_MULTICELLULARITY](ORIGINS_OF_MULTICELLULARITY.md): choanoflagellate
  and *Capsaspora* genes.
- [CO2_CONCENTRATING_MECHANISMS](CO2_CONCENTRATING_MECHANISMS.md) and
  [PHOTOSYNTHESIS](PHOTOSYNTHESIS.md): *Chlamydomonas* and algal photosynthesis.
- [IBA_REVIEW](IBA_REVIEW.md) and [PAINT](PAINT.md): the propagation patterns
  that most protist annotations depend on.

---
# STATUS

Last updated: 2026-10-14

## Seed gene list

Species codes are UniProt mnemonics and match the `genes/<CODE>/` folders.
Accessions were checked against UniProt on 2026-10-14. Entries marked
*unreviewed* are TrEMBL entries with no gene symbol of their own; following the
repository convention, their folder name will be the accession unless UniProt
provides a symbol by the time they are fetched.

### Track A: Apicomplexa

- [ ] PLAF7 CSP (Q7K740): circumsporozoite protein, sporozoite surface coat
- [ ] PLAF7 CRT (Q8IBZ9): chloroquine resistance transporter, digestive vacuole
- [ ] PLAF7 MDR1 (Q7K6A5): ABC transporter, drug resistance
- [ ] PLAF7 PMII (Q8I6V3): plasmepsin II, haemoglobin digestion
- [ ] PLAF7 CDPK1 (P62344): calcium-dependent protein kinase 1
- [ ] PLAF7 ATP4 (A0A143ZZK9): P-type Na+ ATPase, antimalarial drug target
- [ ] PLAF7 MSP1 (Q8I0U8): merozoite surface protein 1
- [ ] PLAF7 RH5 (Q8IFM5): erythrocyte invasion ligand (binds basigin)
- [ ] PLAF7 K13 (Q8IDQ2, unreviewed): kelch13, artemisinin resistance
- [ ] PLAF7 AMA1 (Q7KQK5, unreviewed): apical membrane antigen 1, moving junction
- [ ] PLAF7 HAP2 (Q8IJQ3, unreviewed): gamete fusion factor
- [ ] TOXGO SAG1 (P13664): major surface antigen; Swiss-Prot entry is at species level (taxon 5811)
- [ ] TOXGM MIC2 (S8F9G8, unreviewed): microneme adhesin, gliding motility
- [ ] TOXGM ROP18 (A0A125YQL1, unreviewed): rhoptry kinase, virulence factor

### Track B: Kinetoplastida

- [ ] TRYB2 REL1 (P86927): RNA-editing ligase 1, mitochondrial RNA editing
- [ ] TRYBB TPR (P39051): trypanothione reductase; Swiss-Prot entry at subspecies level (taxon 5702)
- [ ] TRYBB PFRA (P22225): 69 kDa paraflagellar rod protein (PFR-A/PFR-B)
- [ ] TRYBB PFRC (Q26789): 73 kDa paraflagellar rod protein (PFR-C/PFR-D)
- [ ] LEIMA gp63 (P08148): leishmanolysin, surface metalloprotease
- [ ] LEIMA PTR1 (Q01782): pteridine reductase 1, antifolate resistance

### Track C: Ciliates

- [ ] TETTS TERT (O77448): telomerase reverse transcriptase
- [ ] TETTS TAP65 (W7X6T2): p65 telomerase holoenzyme protein (LARP7 family)
- [ ] PARTE A0BFB4: existing draft, to finish

### Track D: Metamonads and *Entamoeba*

- [ ] ENTH1 hgl1 (P32022): Gal/GalNAc lectin heavy subunit, adherence
- [ ] ENTH1 APA (P34095): amoebapore A, pore-forming peptide
- [ ] TRIV3 A2FPI7: existing draft, to finish

### Track E: Stramenopiles

- [ ] PHATC Lhcx1 (B7FYL0, unreviewed): LHCX photoprotection protein
- [ ] PHATC Sit1 (B7GBI4, unreviewed): silicic acid transporter
- [ ] THAPS Sil1 (Q5Y2C2, unreviewed): silaffin, silica biomineralisation
- [ ] PHATC B7FXQ8: existing draft, to finish

Most species codes in this list (all except PARTE, PHATC and TRIV3) are new
to `genes/`. Before fetching, check that `just fetch-gene`
resolves them, and decide whether entries filed at species or subspecies level
should stay there or be moved to the strain proteome entry.

## Candidates not yet identified in UniProt

Lookups on 2026-10-14 found no entry by gene name for these; find the right
accession (often a systematic locus id) before adding them:
*T. brucei* VEX1 and RBP10; *Tetrahymena* PDD1, TWI1 and TPB2; *Paramecium*
PiggyMac; *Phaeodactylum* aureochrome 1a; *Giardia* (strain WB) alpha-giardin.

## Tasks

- [ ] Redo the GOA census per species (with descendant taxa) and per GO aspect;
      resolve the *Leishmania* and *Toxoplasma* taxon questions
- [ ] Confirm `just fetch-gene` works for the new species codes
- [ ] Review the seed genes, one track at a time, starting with Track A
- [ ] Collect protist-specific over-annotation patterns in a
      `PROTISTS/patterns.md` sub-page as reviews accumulate
- [ ] Collect proposed GO terms for lineage-specific processes

# NOTES

## 2026-10-14

Project created. Inventory of `genes/`: eight protist species folders, holding
62 *Dictyostelium*, 19 *Chlamydomonas*, 11 *Salpingoeca*, 6 *Capsaspora*, 2
*Monosiga* and one each of *Paramecium*, *Phaeodactylum* and *Trichomonas*
reviews. Apart from *Dictyostelium* (all COMPLETE) and *Chlamydomonas* (18 of
19 COMPLETE), every protist review is DRAFT. There are no apicomplexan, kinetoplastid,
*Tetrahymena*, *Giardia* or *Entamoeba* folders. The census table above was
built from QuickGO API queries on the same day; seed accessions were checked
with the UniProt REST API.
