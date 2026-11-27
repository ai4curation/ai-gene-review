---
title: "Eukaryotic Pathogens"
description: "VEuPathDB pathogen and vector coverage triage for PANTHER families and IBA annotations."
maturity: SCOPING
collections: [HOMOLOGY_PROPAGATION]
tags: [BIOLOGY_DOMAIN]
species:
  - PLAF7
  - PLAVS
  - PLABA
  - TOXGM
  - CRYPI
  - TRYB2
  - TRYCR
  - LEIMA
  - LEIDO
  - GIAIC
  - ENTH1
  - TRIV3
  - BABBO
  - BABMR
  - THEAN
  - THEPA
  - ENCCU
  - ENCIT
  - ENTBH
  - NEMP3
  - ASPFU
  - CANAL
  - CANGA
  - CRYN9
  - CRYD1
  - ANOGA
  - AEDAE
  - IXOSC
autolink_gene_symbols: false
index_group: OTHER_ORGANISM
---

# Eukaryotic Pathogens

**Bottom line:** this project scopes PANTHER family and PAINT/IBA coverage
across the eukaryotic pathogen and vector reference organisms in VEuPathDB. The
first pass samples one to five reference genomes per VEuPathDB site, counts
their UniProtKB proteins with PANTHER cross-references, IBA annotations, and
experimental GO annotations, and uses the missing-IBA or missing-PANTHER
Swiss-Prot rows to seed the first curation batches. The generated coverage
table and candidates live under
[EUKARYOTIC_PATHOGENS/](EUKARYOTIC_PATHOGENS/); no per-clade gene reviews have
started yet.

## Scope and sources

This page keeps the planning surface small. The reproducible data products are:

- [coverage_report.md](EUKARYOTIC_PATHOGENS/coverage_report.md) - generated
  Markdown report, grouped by VEuPathDB site.
- [coverage.tsv](EUKARYOTIC_PATHOGENS/coverage.tsv) - organism-level counts.
- [candidate_genes.tsv](EUKARYOTIC_PATHOGENS/candidate_genes.tsv) - the first
  50 reviewed or experimentally annotated proteins per organism that lack IBA.
- [veupathdb_panther_coverage.py](EUKARYOTIC_PATHOGENS/veupathdb_panther_coverage.py)
  - the stdlib-only script that queries VEuPathDB, UniProtKB, and QuickGO.

Counts were generated from:

- VEuPathDB organism search, release 71, using the current organism list and
  per-row gene counts.
- UniProtKB REST, release 2026_04, for accession totals, UniProt mnemonics,
  Swiss-Prot status, and PANTHER cross-references.
- QuickGO annotation search, counting IBA as `ECO:0000318` and direct
  experimental GO evidence as EXP, IDA, IPI, IMP, IGI, IEP, HTP, HDA, HMP, HGI,
  and HEP.
- Local `genes/` review folders, counted by UniProt mnemonic, for existing
  AI Gene Review coverage.

The script uses the UniProtKB taxon that gives the best species-level
accession set when VEuPathDB's exact reference strain taxon is too narrow for
current UniProtKB coverage. Those cases are flagged in
[coverage.tsv](EUKARYOTIC_PATHOGENS/coverage.tsv). The exact *Enterocytozoon
bieneusi* H348 taxon has only 26 UniProtKB accessions against 3,806 VEuPathDB
genes, so its PANTHER percentage is not a genome-wide coverage estimate.

## Confirmed Site Panel

| VEuPathDB site | Release 71 organism rows | Reference panel | Existing AIGR reviews |
|---|---:|---|---:|
| PlasmoDB | 64 | *Plasmodium falciparum* 3D7 `PLAF7`; *P. vivax* Sal-1 `PLAVS`; *P. berghei* ANKA `PLABA` | 11 |
| ToxoDB | 42 | *Toxoplasma gondii* ME49 `TOXGM`, plus species-level `TOXGO` reviews already in the repo | 3 |
| CryptoDB | 28 | *Cryptosporidium parvum* Iowa II `CRYPI` | 0 |
| TriTrypDB | 89 | *Trypanosoma brucei brucei* TREU927 `TRYB2`; *T. cruzi* Dm28c 2014 `TRYCR`; *Leishmania major* Friedlin `LEIMA`; *L. donovani* BPK282A1 `LEIDO` | 7 |
| GiardiaDB | 16 | *Giardia* Assemblage A isolate WB `GIAIC` | 0 |
| AmoebaDB | 43 | *Entamoeba histolytica* HM-1:IMSS `ENTH1` | 0 |
| TrichDB | 6 | *Trichomonas vaginalis* G3 `TRIV3`, plus existing `TRIVA` reviews | 2 |
| PiroplasmaDB | 25 | *Babesia bovis* T2Bo `BABBO`; *B. microti* RI `BABMR`; *Theileria annulata* Ankara `THEAN`; *T. parva* Muguga `THEPA` | 0 |
| MicrosporidiaDB | 55 | *Encephalitozoon cuniculi* GB-M1 `ENCCU`; *E. intestinalis* ATCC 50506 `ENCIT`; *Enterocytozoon bieneusi* H348 `ENTBH`; *Nematocida parisii* ERTm3 `NEMP3` | 0 |
| FungiDB | 347 | *Aspergillus fumigatus* Af293 `ASPFU`; *Candida albicans* SC5314 `CANAL`; *Nakaseomyces glabratus* CBS 138 `CANGA`; *Cryptococcus neoformans* H99 `CRYN9`; *C. deneoformans* JEC21 `CRYD1` | 154 |
| VectorBase | 105 | *Anopheles gambiae* PEST `ANOGA`; *Aedes aegypti* LVP_AGWG `AEDAE`; *Ixodes scapularis* Wikel `IXOSC` | 29 |

Changes from the seed list:

- `GiardiaDB`, `AmoebaDB`, and `TrichDB` are separate VEuPathDB sites; each
  gets its own subproject.
- `PiroplasmaDB` and `MicrosporidiaDB` are separate sites; the first panel uses
  exact Babesia, Theileria, Encephalitozoon, Enterocytozoon, and Nematocida
  reference rows instead of genus-level placeholders.
- FungiDB has a broad pathogen and model-fungus scope; the first panel starts
  with Aspergillus, Candida/Nakaseomyces, and Cryptococcus anchors that expose
  many missing-IBA and host-interface families.
- VectorBase is retained as a sibling subproject for pathogen vectors, not as a
  pathogen subproject.

## Proposed Order

1. **FungiDB** - large existing `ASPFU`, `CANAL`, and `CANGA` review base; many
   experimentally annotated Swiss-Prot adhesins, wall proteins, hydrophobins,
   and virulence regulators lack PANTHER or IBA.
2. **PlasmoDB** - *P. falciparum* has 399 experimentally annotated proteins
   with no IBA, and *P. vivax* plus *P. berghei* have reviewed proteins but no
   current IBA rows in QuickGO.
3. **TriTrypDB** - kinetoplastid-specific RNA-editing, glycosome, surface, and
   chromosomal-passenger proteins expose both missing PANTHER families and IBA
   gaps in *Trypanosoma* and *Leishmania*.
4. **VectorBase** - not pathogens, but mosquito and tick saliva, immunity, and
   host-anticoagulation proteins are well-studied, host-interface enriched, and
   often outside PANTHER.
5. **ToxoDB** - a compact reviewed experimental set can test whether the
   complete absence of ME49 IBA rows is a PAINT coverage issue or a strain/taxon
   mapping issue.
6. **GiardiaDB** - a moderate IBA base plus a small set of reviewed
   experimental gaps makes this a tractable diplomonad pilot.
7. **AmoebaDB** - *E. histolytica* has strong glycolysis and Gal/GalNAc-lectin
   anchors, with several experimentally characterized proteins outside
   PANTHER.
8. **CryptoDB** - very sparse experimental GO rows, but a small Swiss-Prot
   anchor set can expose which apicomplexan families are genuinely uncovered.
9. **TrichDB** - the huge 50,190-protein UniProtKB set and 18.9% IBA coverage
   make this important, but its first pass should be a targeted audit of the
   few experimentally supported PTN placements rather than a broad gene batch.
10. **PiroplasmaDB** - no sampled Babesia or Theileria protein currently has an
    IBA row; the first pass is a small Swiss-Prot surface-antigen and enzyme
    triage.
11. **MicrosporidiaDB** - no sampled microsporidian protein has IBA; start with
    *E. cuniculi* polar-tube/spore-wall proteins and Nematocida family coverage
    after the richer sites have established the review pattern.

## Subprojects

### PlasmoDB

*P. falciparum* 3D7 has the largest experimental/no-IBA set in the apicomplexan
panel. The first batch should review invasion, rhoptry, merozoite-surface, and
sexual-stage proteins that are Swiss-Prot plus experimental but lack PANTHER,
including PfSUB1-ProM, apicortin/DCX, RhopH2/RhopH3, MSP1/MSP2, RH1, Pfs16,
RH5, and CyRPA. A second small batch should add the *P. vivax* DBP, PMV, LAP,
RBP2b, and PNP rows and the *P. berghei* G37, OMG1, ICP, AP2-Z, PIMMS2, CSP,
and P45/48 rows.

### ToxoDB

The sampled ME49 proteome has PANTHER families for 4,801 of 8,306 UniProtKB
proteins but no IBA rows in the QuickGO query. First batch: RON2 and RON2L2
rhoptry neck proteins, MAF1a1, CEN1/CEN2, AQP, ApiAT1/NPT1, and BFD1.

### CryptoDB

The *C. parvum* Iowa II sample has 2,467 PANTHER-family proteins but no IBA.
Start with its three Swiss-Prot experimental anchors, SSAT, SKSR1, and the
ADP/ATP translocase CpAAC, then add FEN1, ASNA1, COQ4, SLX1, and DRE2 as
reviewed conserved proteins that test whether apicomplexan propagation stops at
Cryptosporidium or only lacks terminal IBA export.

### TriTrypDB

*T. brucei* has heavy experimental GO coverage but thousands of rows without
IBA, so the first batch should stay reviewed and compact: mitochondrial
RNA-editing ligases REL1/REL2, kinetoplastid-specific CPC1/CPC2, glycosomal
PEX13.1/PEX13.2, CWC21, XAC1, and PuREBP2. Follow with cross-genus surface and
glycosome anchors: *T. cruzi* NETNES, KMP-11, AdoMetDC, TCP17, TOR, and
chagasin; *Leishmania major* gp63, IU-nucleoside hydrolase, and ecotins; and
*L. donovani* G5K, PEX5, PEX14, eIF5A, DHS, DOHH, and GMPR.

### GiardiaDB

The Assemblage A WB strain has 1,842 proteins with IBA, but several
experimentally characterized Swiss-Prot proteins lack propagation. First batch:
UPPS, fructose-bisphosphate aldolase, median body protein, Notch homolog, and
BIVM, followed by conserved Swiss-Prot no-IBA entries such as SLX1, ASNA1,
TRM5, and COQ4.

### AmoebaDB

*E. histolytica* has useful IBA coverage overall and several distinctive
experimental holes. First batch: the PEPCK1/2/3 PPi-type phosphoenolpyruvate
carboxykinase paralogs, Gal/GalNAc lectin heavy subunit HGL2, inositol
polyphosphate 1-phosphatase, SREHP, ADH1, and PPDK.

### TrichDB

The *T. vaginalis* proteome is the outlier: 98,611 VEuPathDB genes, 50,190
UniProtKB proteins, 25,806 proteins in PANTHER families, but only 9,480 with
IBA. Its six experimentally annotated exact-strain accessions all already have
IBA, so start by auditing that PTN propagation on the ALG5 paralogs, then
compare the pyrophosphate-dependent phosphofructokinases and SEY1 paralogs in
Swiss-Prot for paralog-specific propagation.

### PiroplasmaDB

None of the sampled Babesia or Theileria taxa has an IBA row. Because the
experimental set is tiny, the first batch should be a Swiss-Prot spot review:
Babesia BABR/high-molecular-weight antigens, Theileria p23/p67/p104 surface or
apical antigens, and the experimentally annotated Theileria PIN1 and
thioredoxin-domain proteins.

### MicrosporidiaDB

The first pass should avoid the under-represented *E. bieneusi* H348 taxon and
use *E. cuniculi* polar-tube and spore-wall anchors: PTP1, PTP2, PTP3, SWP3,
EnP1, the ECU11_0510 polysaccharide-deacetylase-domain protein, and adenylate
kinase. Nematocida has the lowest sampled PANTHER-family coverage at 43.8%;
after the *E. cuniculi* anchors, use it to look for lineage-specific families
that need either a family review or a note that no PTN family exists.

### FungiDB

This subproject should reuse the [FUNGAL_PAINT_FAMILIES](FUNGAL_PAINT_FAMILIES.md)
pattern for cross-species family work and avoid duplicating that status page.
First concrete batches:

- *A. fumigatus*: RodA/RodB/RodC hydrophobins, asp-hemolysin, pptB, cwhA, fumR,
  ncaA, FleA, and hrmA.
- *C. albicans*: HNV1, CSA6, EED1/DEF1, KRE1, ADF1, HWP1, ECE1/candidalysin,
  BMT2, MSS11, RBT1, HWP2, and PGA/IFF adhesin-family members.
- *N. glabratus*: AWP2/AWP3b adhesins, MT-I/MT-II metallothioneins, PUP1, TDA7,
  HRI1, and MSS11.
- Cryptococcus: QSP1, PQP1, EGC1, CRZ1, CCK1, CHS4, MDR1, CXT1, CAS1, and
  CLMP1.

### VectorBase

VectorBase is in scope because mosquito and tick host-interface proteins show
the same PAINT blind spots as pathogen secretomes, but it should stay visibly
separate from pathogen clades. First batch: *Anopheles* SAMSP1, Yob, Def3,
gSG6, anophelin, EBP, D7R3, and TEP1; *Aedes* Aegyptin, vitelline membrane
protein 15a-2, Head peptide, Nix, CPB1, Ir8a, Ir76b, and SGS1; and *Ixodes*
Dae2, ISAMP, microplusin, TSLPI, P23, ixonnexin, and ixodegrins.

## Status

- [x] Confirm VEuPathDB release 71 site membership and exact organism rows.
- [x] Count current UniProtKB/PANTHER, QuickGO IBA, experimental GO, Swiss-Prot,
  and local AIGR coverage for the first reference panel.
- [x] Record reproducible coverage machinery and generated TSV/Markdown
  outputs under `projects/EUKARYOTIC_PATHOGENS/`.
- [x] Propose a site order and a first concrete batch for each site.
- [ ] Wait for cmungall/Ros-orchestrate to choose the first clade before
  opening per-clade gene-review sessions.

Future gene, family, or module content PRs should touch only their owned
organism or family files. Update this status page in a separate status PR
after those content PRs merge.

## Related Projects

- [PARASITES](PARASITES.md) - broader parasite umbrella, currently focused on
  nematodes.
- [PARASITE_IMMUNE_MODULATORS](PARASITE_IMMUNE_MODULATORS.md) - host-interface
  and immune-modulating secreted proteins.
- [NEMATODE_PATHOGENS](NEMATODE_PATHOGENS.md) - pathogenic nematode modules and
  gene reviews.
- [FUNGAL_PAINT_FAMILIES](FUNGAL_PAINT_FAMILIES.md) - fungal PAINT family
  reviews that FungiDB pathogen work should reuse where possible.
- [FUNGAL_PHENOTYPES](FUNGAL_PHENOTYPES.md) - fungal phenotype resources that
  can contextualize but usually cannot by themselves support GO annotations.
