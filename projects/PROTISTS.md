---
title: "Protists"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [PLAF7, TOXGM, TOXGO, TRYB2, TRYBB, LEIMA, TETTS, PARTE, GIAIC, TRIV3, ENTH1, PHATC, THAPS, DICDI, CHLRE, SALRS, MONBE, CAPO3]
genes: [CSP, CRT, MDR1, PMII, CDPK1, ATP4, MSP1, RH5, K13, AMA1, HAP2, SAG1, MIC2, ROP18, A0BFB4, A2FPI7, B7FXQ8]
autolink_exclude: [TERT, rod, Sil1, sil1]
---

# Protists: Gene Function Outside Animals, Fungi and Plants

**Bottom line:** most of the diversity of eukaryotes is protist, but very little
of this repository is. Of 7,176 gene folders, about 104 (1.4%) are protists, and
62 of those are *Dictyostelium*. We have no reviews at all for the parasites that
carry most protist GO curation (*Plasmodium*, *Toxoplasma*, trypanosomes,
*Leishmania*), nor for the ciliate and diatom models. This project sets out to
fill that gap, lineage by lineage, starting with a seed list of 27 well-studied
genes whose UniProt accessions we have checked. Track A (Apicomplexa) is done:
all 14 genes (11 *P. falciparum*, 3 *T. gondii*) have COMPLETE reviews covering
241 existing annotations plus 26 new ones. The most common corrections were
removing terms carried over from animal homologs and replacing generic `membrane`
and `protein binding` rows with the compartment or binding partner each paper
shows.

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

Annotation counts from the QuickGO API, for the exact taxon of each row
(descendant taxa are not included), which is a strain except where the row says
otherwise. *Toxoplasma* appears twice because its curation really is split that
way: the species-level taxon 5811 carries SAG1's Swiss-Prot entry, while ME49
(508771) carries the TrEMBL entries, and neither row's count includes the
other's. "Experimental" means evidence codes
descending from ECO:0000269 (EXP, IDA, IPI, IMP, IGI, IEP). The review counts
are current as of 2026-10-15; *T. brucei brucei* (TRYBB, taxon 5702) holds 3
more and is not a row here because its annotations sit under the TREU927 strain.

| Organism | Code | Taxon | Experimental | IBA | Our reviews |
|---|---|---:|---:|---:|---:|
| *Dictyostelium discoideum* | DICDI | 44689 | 10,128 | 19,137 | 62 |
| *Trypanosoma brucei* TREU927 | TRYB2 | 185431 | 12,149 | 12,281 | 1 |
| *Plasmodium falciparum* 3D7 | PLAF7 | 36329 | 2,830 | 9,002 | 11 |
| *Chlamydomonas reinhardtii* | CHLRE | 3055 | 546 | 24,014 | 19 |
| *Giardia intestinalis* WB | GIAIC | 184922 | 343 | 6,081 | 0 |
| *Entamoeba histolytica* HM-1:IMSS | ENTH1 | 294381 | 197 | 13,213 | 0 |
| *Plasmodium berghei* ANKA | PLABA | 5823 | 148 | 0 | 0 |
| *Toxoplasma gondii* (species) | TOXGO | 5811 | 133 | 0 | 1 |
| *Tetrahymena thermophila* SB210 | TETTS | 312017 | 124 | 0 | 0 |
| *Toxoplasma gondii* ME49 | TOXGM | 508771 | 35 | 0 | 2 |
| *Trypanosoma cruzi* CL Brener | TRYCC | 353153 | 29 | 0 | 0 |
| *Phaeodactylum tricornutum* | PHATC | 556484 | 17 | 0 | 1 |
| *Paramecium tetraurelia* | PARTE | 5888 | 11 | 49,383 | 1 |
| *Trichomonas vaginalis* G3 | TRIV3 | 412133 | 6 | 31,122 | 1 |
| *Thalassiosira pseudonana* | THAPS | 35128 | 2 | 16,157 | 0 |
| *Leishmania major* Friedlin | LEIMA | 347515 | 0 | 0 | 2 |

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
| A | Apicomplexa (Alveolata) | *P. falciparum*, *T. gondii* | 14/14 COMPLETE |
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
*unreviewed* are TrEMBL entries that carry no `GN Name=` in UniProt. These were
fetched by accession with `--alias`, so the folder uses the standard
nomenclature name; `gene_symbol` is set to that same standard symbol and the
accession stays in `id`. Expect this for any TrEMBL-only apicomplexan gene.

### Track A: Apicomplexa

- [x] PLAF7 CSP (Q7K740): circumsporozoite protein, sporozoite surface coat
- [x] PLAF7 CRT (Q8IBZ9): chloroquine resistance transporter, digestive vacuole
- [x] PLAF7 MDR1 (Q7K6A5): ABC transporter, drug resistance
- [x] PLAF7 PMII (Q8I6V3): plasmepsin II, haemoglobin digestion
- [x] PLAF7 CDPK1 (P62344): calcium-dependent protein kinase 1
- [x] PLAF7 ATP4 (A0A143ZZK9): P-type Na+ ATPase, antimalarial drug target
- [x] PLAF7 MSP1 (Q8I0U8): merozoite surface protein 1
- [x] PLAF7 RH5 (Q8IFM5): erythrocyte invasion ligand (binds basigin)
- [x] PLAF7 K13 (Q8IDQ2, unreviewed): kelch13, artemisinin resistance
- [x] PLAF7 AMA1 (Q7KQK5, unreviewed): apical membrane antigen 1, moving junction
- [x] PLAF7 HAP2 (Q8IJQ3, unreviewed): gamete fusion factor
- [x] TOXGO SAG1 (P13664): major surface antigen; Swiss-Prot entry is at species level (taxon 5811)
- [x] TOXGM MIC2 (S8F9G8, unreviewed): microneme adhesin, gliding motility
- [x] TOXGM ROP18 (A0A125YQL1, unreviewed): rhoptry kinase, virulence factor

*Toxoplasma* folders follow the UniProt mnemonic of each entry, so they split
between `TOXGO` (species level, taxon 5811; SAG1's Swiss-Prot entry) and
`TOXGM` (strain ME49, taxon 508771; the TrEMBL entries MIC2 and ROP18). Put a
new *Toxoplasma* gene wherever its own UniProt entry sits rather than picking
one folder for the species.

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
- [x] Confirm `just fetch-gene` works for the new species codes (it does; entries
      with no UniProt gene symbol need `just fetch-gene <ORG> <ACC> --alias <NAME>`)
- [x] Review Track A (Apicomplexa)
- [ ] Review Track B (Kinetoplastida)
- [ ] Decide whether to submit "food vacuole membrane" and "moving junction" as
      GO term requests (see 2026-10-15 notes)
- [ ] Collect protist-specific over-annotation patterns in a
      `PROTISTS/patterns.md` sub-page as reviews accumulate
- [ ] Collect proposed GO terms for lineage-specific processes

# NOTES

## 2026-10-15

Track A reviewed: 14 genes, one review agent each, all `status: COMPLETE`
and passing `just validate`.

| Gene | Annotations reviewed | ACCEPT | NON_CORE | MODIFY | REMOVE | Other | NEW |
|---|---:|---:|---:|---:|---:|---:|---:|
| PLAF7 CSP | 11 | 9 | 2 | 0 | 0 | 0 | 2 |
| PLAF7 CRT | 12 | 2 | 5 | 2 | 0 | 3 | 2 |
| PLAF7 MDR1 | 14 | 5 | 0 | 9 | 0 | 0 | 0 |
| PLAF7 PMII | 20 | 12 | 3 | 5 | 0 | 0 | 0 |
| PLAF7 CDPK1 | 71 | 41 | 13 | 12 | 4 | 1 | 0 |
| PLAF7 ATP4 | 16 | 4 | 1 | 7 | 4 | 0 | 2 |
| PLAF7 MSP1 | 23 | 8 | 10 | 4 | 0 | 1 | 3 |
| PLAF7 RH5 | 50 | 21 | 1 | 18 | 10 | 0 | 1 |
| PLAF7 K13 | 3 | 0 | 1 | 0 | 1 | 1 | 2 |
| PLAF7 AMA1 | 7 | 3 | 0 | 4 | 0 | 0 | 0 |
| PLAF7 HAP2 | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| TOXGO SAG1 | 2 | 0 | 1 | 1 | 0 | 0 | 2 |
| TOXGM MIC2 | 1 | 0 | 1 | 0 | 0 | 0 | 7 |
| TOXGM ROP18 | 9 | 2 | 0 | 1 | 2 | 4 | 3 |

"Other" is TOO_GENERAL or MARK_AS_OVER_ANNOTATED.

**No deep research.** Falcon authentication failed and the OpenAI key was
rejected in this environment, so no `-deep-research-` files exist. Each gene's
`-notes.md` is a manual literature review and says so at the top. Re-running
deep research later would be a useful cross-check.

**Recurring patterns** (candidates for `PROTISTS/patterns.md`):

- *Animal or plant terms carried over electronically.* ROP18 `nucleus` and `mitotic DNA damage checkpoint
  signaling` (TreeGrafter, from an animal kinase family); ATP4 potassium and
  calcium transport (inherited from ENA and SERCA nodes; the activity is
  insensitive to both ions); CDPK1 `calmodulin binding` (CDPKs carry their own
  calmodulin-like domain). All removed. A related case went the other way: RH5's
  `bicellular tight junction` is equally an animal epithelial term imported on a
  word match, but the parasite structure it describes is real, so that row is
  `MODIFY` to the proposed `moving junction` term rather than a removal.
- *Glutathione transport on CRT.* Comes from Arabidopsis CLT donors and from
  mutant alleles only; marked over-annotated rather than removed.
- *Drug-response terms.* `response to xenobiotic stimulus` (CDPK1, K13, MDR1)
  describes inhibitor screens or resistance alleles, not a process the protein
  carries out. It was removed, marked over-annotated, or changed to
  `xenobiotic transmembrane transport` depending on the case.
- *Sparse GOA.* MIC2, SAG1, HAP2 and K13 had 1 to 3 annotations each, with no
  molecular function. Most of their core content came from NEW rows. MIC2
  (7 NEW rows) is the heaviest and is a good candidate for a second look.
- *Non-symbol entries.* MDR1, K13, AMA1 and HAP2 have no `GN Name=` in UniProt,
  so `just fetch-gene` seeded `gene_symbol` with the accession. All four were
  set to the standard *P. falciparum* symbol, matching the folder, with the
  accession kept in `id`. A convention note in CLAUDE.md would stop this
  recurring; left for a maintainer.

**Proposed terms to consolidate.**

- `food vacuole membrane` (a child of GO:0005774): proposed independently by the
  CRT and MDR1 reviews, which worded their definitions differently. Canonical
  text for the eventual term request: *"The lipid bilayer surrounding the food
  vacuole (GO:0020020), the acidic digestive compartment of intraerythrocytic
  Plasmodium and related apicomplexans in which host haemoglobin is degraded."*
  Parent: GO:0005774 vacuolar membrane.
- `moving junction` (AMA1 and RH5, parent GO:0030054 cell junction): the
  merozoite-erythrocyte ring that RH5's `bicellular tight junction` row was
  reaching for. Both reviews carry identical definition text.
- `RH5-CyRPA-Ripr invasion complex` (RH5).
- `Kelch13 compartment` and `cytostome-mediated endocytosis of host cell
  cytosol` (K13).

**Calls to check.** AMA1 replaces its RON2 and RON4 `protein binding` rows with
`host cell surface binding`, on the grounds that RON2 sits in the host membrane
when AMA1 binds it. That stretches the term, since RON2 is a parasite protein.
The open question is whether a parasite-ligand-in-host-membrane case needs
its own term.

## 2026-10-14

Project created. Inventory of `genes/`: eight protist species folders, holding
62 *Dictyostelium*, 19 *Chlamydomonas*, 11 *Salpingoeca*, 6 *Capsaspora*, 2
*Monosiga* and one each of *Paramecium*, *Phaeodactylum* and *Trichomonas*
reviews. Apart from *Dictyostelium* (all COMPLETE) and *Chlamydomonas* (18 of
19 COMPLETE), every protist review is DRAFT. There are no apicomplexan, kinetoplastid,
*Tetrahymena*, *Giardia* or *Entamoeba* folders. The census table above was
built from QuickGO API queries on the same day; seed accessions were checked
with the UniProt REST API.
