---
title: "Fungal PAINT Family Reviews"
maturity: IN_PROGRESS
collections: [HOMOLOGY_PROPAGATION]
species: [yeast, SCHPO, CANAL, NEUCR, ASPFU, EMENI]
autolink_exclude: [Ser]
---

# Fungal PAINT Family Reviews

**Bottom line:** review compact PANTHER families whose GO-Central PAINT
assertions were placed on fungal ancestral nodes, comparing *Saccharomyces
cerevisiae*, *Schizosaccharomyces pombe*, CGD/*Candida* genes, and at least one
filamentous fungus such as *Neurospora crassa*. The immediate aim is to read the
PAINT node placement, cached gene references, and any newer literature for each
orthologous gene set before deciding whether the IBA assertions are correct,
over-propagated, or too conservative.

## Selection Rule

Families enter this project when the local PANTHER PAINT cache has at least one
IBD row asserted at a fungal taxon node, especially `taxon:4751` for Fungi, and
the family has representative members in two or more curated fungal MODs.
Priority goes to families that are small enough for a combined family review and
that include Candida Genome Database seeds or *Neurospora crassa* members.

## Initial Families

| Family | PAINT scope | First genes |
| --- | --- | --- |
| `PTHR11638` ATP-DEPENDENT CLP PROTEASE | fungal `HSP104` and `HSP78` nodes | `HSP104`/`HSP78`, `hsp104`/`hsp78`, `HSP104`/`HSP78`, `hsp98` |
| `PTHR24055` MITOGEN-ACTIVATED PROTEIN KINASE | fungal MAPK subtrees | `HOG1`/`sty1`/`HOG1`/`hog-1` and pheromone MAPKs |
| `PTHR31297` GLUCAN ENDO-1,6-BETA-GLUCOSIDASE B | fungal glucanase nodes | `EXG1`/`SPR1`/`exg` paralogs/`XOG1`/`EXG2` |
| `PTHR19370` NADH-CYTOCHROME B5 REDUCTASE | fungal reductase nodes | `MCR1`/`CBR1`/`cbr1`/`mcr-1` |
| `PTHR10615` HISTONE ACETYLTRANSFERASE | fungal MYST acetyltransferase nodes | `ESA1`/`SAS` paralogs/`mst` paralogs |
| `PTHR43762` L-GULONOLACTONE OXIDASE | fungal `ALO1` node | `ALO1`/`alo1`/`ALO1`/`alo-1` |
| `PTHR35329` CHITIN SYNTHASE EXPORT CHAPERONE | fungal `CHS7` node | `CHS7`/`Q5AA40`/`csc-1` |
| `PTHR11635` PKA REGULATORY SUBUNIT | conserved PKA-R node, fungal nuclear node, and broad cAMP-signaling node | `BCY1`/`cgs1`/`BCY1`/`mcb` |
| `PTHR10868` SIGMA 1-TYPE OPIOID RECEPTOR-RELATED | fungal `ERG2` node | `ERG2`/`erg2`/`ERG2`/`erg-1` |
| `PTHR43290` MEVALONATE KINASE | root mevalonate-kinase node and fungal ergosterol node | `ERG12`/`erg12`/`ERG12`/`ASPFU/erg12` |
| `PTHR10572` 3-HYDROXY-3-METHYLGLUTARYL-COENZYME A REDUCTASE | root HMGR/isoprenoid node, eukaryotic ER-membrane node, and fungal ergosterol node | `HMG1`/`HMG2`/`hmg1`/`ASPFU/hmg1`/`ASPFU/hmg2`/`EMENI/AN1593` |
| `PTHR19855` WD40 REPEAT PROTEIN 12, 37 | Ascomycota WDR12/Ytm1 node | `YTM1`/`ytm1`/`YTM1`/`ytm1` |
| `PTHR10969` MICROTUBULE-ASSOCIATED PROTEINS 1A/1B LIGHT CHAIN 3-RELATED | eukaryotic ATG8 node and fungal vacuole-membrane node | `ATG8`/`atg8`/`apg-6` |
| `PTHR10806` SIGNAL PEPTIDASE COMPLEX CATALYTIC SUBUNIT SEC11 | PTHR10806 root peptidase node and eukaryotic Sec11/SPC node | `SEC11`/`sec11`/`SEC11`/`sec11` |
| `PTHR11671` V-TYPE ATP SYNTHASE SUBUNIT D | fungal V-ATPase subunit D node | `VMA8`/`vma8`/`VMA8`/`vma-8` |
| `PTHR43607` V-TYPE PROTON ATPASE CATALYTIC SUBUNIT A | conserved A-subunit and fungal vacuole-membrane nodes | `VMA1`/`vma1`/`TFP1`/`vma-1` |
| `PTHR10572` 3-HYDROXY-3-METHYLGLUTARYL-COENZYME A REDUCTASE | root HMGR/isoprenoid node, eukaryotic ER-membrane node, and fungal ergosterol node | `HMG1`/`HMG2`/`hmg1`/`ASPFU/hmg1`/`ASPFU/hmg2`/`EMENI/AN1593` |

---

# STATUS

Last updated: 2026-11-01

## Family 1: Hsp100/ClpB Disaggregases

`PTHR11638` contains two fungal PAINT subtrees relevant to this batch:
cytosolic Hsp104-family disaggregases at `PANTHER:PTN007521008` and
mitochondrial Hsp78-family disaggregases at `PANTHER:PTN000909045`.

- [x] `yeast/HSP104` - cytosolic ATP-dependent disaggregase; merged in PR
  #3692
- [x] `yeast/HSP78` - mitochondrial `Hsp104`/ClpB paralog; merged in PR #4519
- [x] `SCHPO/hsp104` - fission yeast cytosolic `Hsp104` ortholog; merged in
  PR #4524
- [x] `SCHPO/hsp78` - fission yeast mitochondrial Hsp78 ortholog; merged in PR
  #4521
- [x] `CANAL/HSP104` - CGD-seeded *Candida albicans* `Hsp104` ortholog; merged
  in PR #4523
- [x] `CANAL/HSP78` - *Candida albicans* mitochondrial Hsp78 ortholog; merged in
  PR #4522
- [x] `NEUCR/hsp98` - *Neurospora crassa* Hsp104-family member; merged in PR
  #4520

## Family 2: MYST Histone Acetyltransferases

`PTHR10615` contains a broad eukaryotic MYST histone-acetyltransferase node and
separate fungal Esa1/NuA4, Sas2/SAS-I, and Sas3/NuA3 placements that need
paralog-aware activity and complex checks.

- [x] `yeast/ESA1` - NuA4 catalytic subunit; drafted in PR #4604
- [x] `yeast/SAS2` - SAS-I catalytic subunit; drafted in PR #4606
- [x] `yeast/SAS3` - NuA3 catalytic subunit; merged in PR #4608
- [x] `SCHPO/mst2` - fission yeast MYST acetyltransferase; drafted in this branch
- [x] `SCHPO/mst1` - fission yeast NuA4 MYST acetyltransferase; drafted in this
  branch
- [x] `CANAL/ESA1` - CGD-seeded Esa1/NuA4 catalytic subunit; merged in PR
  #4774
- [x] `NEUCR/esa-1` - Neurospora ESA1/NuA4 catalytic subunit; drafted in
  this branch

## Later Candidates

- [ ] `PTHR24055` MAP kinases across HOG/p38 and pheromone pathways
- [x] `PTHR19370` fungal NADH-cytochrome b5 reductases

## Family 3: Chitin Synthase Export Chaperones

`PTHR35329` contains a compact fungal CHS7-family ancestor,
`PANTHER:PTN002175570`, with PAINT assertions for ER membrane, chitin
biosynthetic process, protein folding, and protein folding chaperone activity.

- [x] `yeast/CHS7` - *S. cerevisiae* CHS7 anchor; already reviewed and aligned
  to the current `PTN002175570` PAINT assertions before this project
- [x] `NEUCR/csc-1` - *Neurospora crassa* CSE-7/CHS-4 export factor; drafted
  in this branch
- [x] `CANAL/CHS7` - CGD's *Candida albicans* seed for the
  `GO:0006031 chitin biosynthetic process` IBD; drafted in this branch

## Family 4: MAP Kinases

`PTHR24055` includes broad MAPK-family PAINT placements for generic kinase
activity and active compartments, plus fungal HOG/Sty1 stress-MAPK placements
such as `PANTHER:PTN001172058` for osmosensory, oxidative-stress, and
stress-activated MAPK-cascade assertions.

- [x] `NEUCR/hog-1` - *Neurospora crassa* OS-2/HOG-1 stress MAPK; merged in PR
  #4570
- [x] `CANAL/HOG1` - *Candida albicans* HOG stress MAPK; merged in PR #4565
- [x] `SCHPO/sty1` - fission yeast Sty1/Spc1 stress MAPK; merged in PR #4573
- [x] `yeast/HOG1` - *S. cerevisiae* HOG stress MAPK; merged in PR #4703
- [x] `CANAL/MKC1` - *Candida albicans* Slt2/Spm1-family cell-wall-integrity
  MAPK; merged in PR #5868

## Family 5: Fungal Glucanases

`PTHR31297` contains several fungal GH5 glucanase subtrees. The current
EXG1/XOG1-family IBA rows split over a broad Aspergillus-root
`PTN001262628` glucan-catabolism node, a fungal `PTN001262686` extracellular
cell-wall beta-glucan node, and a Saccharomycetes `PTN001262687`
exo-1,3-beta-glucosidase node.

- [x] `yeast/EXG1` - secreted exo-1,3-beta-glucosidase; merged in PR #4610
- [x] `yeast/SPR1` - sporulation-specific glucanase in the EXG1/Spr1/XOG1
  clade; merged in PR #4612
- [x] `SCHPO/exg1` - fission-yeast extracellular glucanase seed for the
  fungal wall beta-glucan node; merged in PR #4699
- [x] `SCHPO/exg2` - SF34 membrane GH5 protein with S. pombe cell-wall
  phenotypes; merged in PR #4701
- [x] `SCHPO/exg3` - SF43 glucanase-family protein; merged in PR
  #4702
- [x] `CANAL/XOG1` - CGD-seeded *Candida albicans*
  exo-1,3-beta-glucosidase; merged in PR #4596
- [x] `CANAL/EXG2` - CGD-seeded SF1 exo-1,3-beta-glucosidase; merged in PR
  #4618
- [x] `ASPFU/exgA` - *Aspergillus fumigatus* SF1 exoglucanase inheriting
  the broad exgD/exgB-seeded glucan-catabolism node; merged in PR #5417
- [x] `NEUCR/NCU03914` - *Neurospora crassa* SF34 exgD-like member; supersedes
  the earlier `NCU09652` placeholder, which is a GH43 beta-xylosidase; drafted
  in PR #5433

## Family 6: PKA Regulatory Subunits

`PTHR11635` contains the root PKA regulatory-chain node
`PANTHER:PTN004280545`, which carries the conserved cAMP binding, PKA
catalytic-subunit binding, PKA inhibitor, and PKA-complex assertions; fungal
node `PANTHER:PTN000908765`, which carries nuclear localization; and the broad
cAMP-signaling/cytosol node `PANTHER:PTN000180782`, which carries cytosol and
an over-scoped GPCR/adenylate-cyclase pathway assertion.

- [x] `CANAL/BCY1` - *Candida albicans* PKA regulatory subunit; merged in PR
  #4751
- [x] `NEUCR/mcb` - *Neurospora crassa* PKA regulatory subunit; merged in PR
  #4756
- [x] `SCHPO/cgs1` - fission-yeast PKA regulatory subunit; merged in PR #4763
- [x] `yeast/BCY1` - budding-yeast PKA regulatory-subunit anchor; drafted in
  this branch

## Family 7: Sterol C-8 Isomerases

`PTHR10868` contains a fungal ERG2 ancestor, `PANTHER:PTN001280219`,
with PAINT assertions for C-8 sterol isomerase activity and ergosterol
biosynthetic process. The family also has a broader ER-localization IBD on
`PANTHER:PTN001328958`; animal Sigma-receptor signaling annotations are on
separate descendant PTNs and do not propagate to the fungal ERG2 genes.

- [x] `yeast/ERG2` - *S. cerevisiae* sterol C-8 isomerase anchor; drafted in
  PR #4725
- [x] `SCHPO/erg2` - fission yeast sterol C-8 isomerase; drafted in PR #4723
- [x] `CANAL/ERG2` - *Candida albicans* CGD seed for the
  `GO:0000247 C-8 sterol isomerase activity` IBD; drafted in this branch
- [x] `NEUCR/erg-1` - *Neurospora crassa* sterol C-8 isomerase; merged in PR
  #4719

## Family 8: WDR12/Ytm1 Pre-60S Assembly Factors

`PTHR19855` contains an Ascomycota WDR12/Ytm1 ancestor,
`PANTHER:PTN000458086`, with PAINT assertions for the large-subunit
preribosome, PeBoW complex, and ribosomal large subunit biogenesis. The node is
seeded by curated *S. cerevisiae* YTM1 evidence, with additional *S. pombe*
`ytm1` support for `GO:0042273 ribosomal large subunit biogenesis`, and sits
separately from the sibling fungal mitochondrial/peroxisome-fission adaptor
node `PANTHER:PTN002336496`.

- [x] `yeast/YTM1` - *S. cerevisiae* Nop7-Erb1-Ytm1 pre-60S factor; merged in
  PR #5118
- [x] `SCHPO/ytm1` - fission-yeast WDR12/Ytm1 seed; merged in PR #5121
- [x] `CANAL/YTM1` - *Candida albicans* CGD member; merged in PR #5120
- [x] `NEUCR/ytm1` - *Neurospora crassa* WDR12/Ytm1 member; merged in PR
  #5117

## Family 9: ATG8/LC3/GABARAP Autophagy Modifiers

`PTHR10969` contains the compact eukaryotic ATG8/LC3/GABARAP ancestor,
`PANTHER:PTN000103522`, with PAINT assertions for autophagosome membrane,
phosphatidylethanolamine binding, autophagosome assembly, mitophagy,
nitrogen-starvation response, and autophagosome maturation. It also contains
the fungal `PANTHER:PTN000861115` node for fungal-type vacuole membrane,
seeded by budding- and fission-yeast Atg8 annotations.

- [x] `yeast/ATG8` - *S. cerevisiae* Atg8 anchor with extensive Cvt,
  mitophagy, nucleophagy, ER-phagy, vacuole-membrane, and lipid-droplet rows;
  opened in PR #5258
- [x] `SCHPO/atg8` - fission-yeast Atg8 seed with direct PAS, Hfl1,
  Atg38, mitophagy, ER-phagy, and nucleophagy evidence; opened in PR #5256
- [x] `CANAL/ATG8` - CGD-seeded *Candida albicans* Atg8 ortholog with
  autophagy and ER-stress genetic-interaction evidence; opened in PR #5257
- [x] `NEUCR/apg-6` - *Neurospora crassa* ATG8-family member; opened in PR
  #5255
- [x] `ASPFU/atg8` - *Aspergillus fumigatus* ATG8-family member with direct
  GFP/RFP-AfAtg8 literature; opened in PR #5260
- [x] `EMENI/atg8` - *Aspergillus nidulans* ATG8-family member with direct
  PAS and GFP-Atg8 imaging literature; opened in PR #5261

## Family 10: Sec11 Signal Peptidase Catalytic Subunits

`PTHR10806` contains signal peptidase complex catalytic subunits. PAINT places
generic `GO:0008233 peptidase activity` at the family root,
`PANTHER:PTN000086749`, and the eukaryotic ER signal-peptidase-complex role at
`PANTHER:PTN000086750`, which carries `GO:0005787 signal peptidase complex` and
`GO:0051604 protein maturation`. This family is included as a compact
paralog-aware comparison set even though these particular IBD rows are at the
PTHR10806 root and Eukaryota rather than at a fungal-only node.

- [x] `yeast/SEC11` - *S. cerevisiae* SPC catalytic subunit; drafted in PR
  #5264
- [x] `SCHPO/sec11` - fission-yeast Sec11 seed for fungal and PomBase homology
  transfers; drafted in PR #5269
- [x] `CANAL/SEC11` - CGD *Candida albicans* Sec11/SPC member; drafted in PR
  #5266
- [x] `NEUCR/sec11` - *Neurospora crassa* Sec11/SPC member; drafted in PR
  #5265
- [x] `ASPFU/sec11` - *Aspergillus fumigatus* AfSec1/sec11 member with direct
  Gel1-processing evidence; drafted in PR #5267
- [x] `EMENI/sec11` - *Aspergillus nidulans* Sec11/SPC member; drafted in PR
  #5268

## Family 11: V-type ATPase Subunit D

`PTHR11671` contains the conserved V-type ATPase subunit D family. The fungal
node `PANTHER:PTN000912657` carries PAINT assertions to
`GO:0000329 fungal-type vacuole membrane` and
`GO:0016471 vacuolar proton-transporting V-type ATPase complex`, while broader
nodes carry `GO:0007035 vacuolar acidification` and
`GO:0046961 proton-transporting ATPase activity, rotational mechanism`.

- [x] `yeast/VMA8` - *S. cerevisiae* V1 subunit D with direct assembly,
  rotor-coupling, and vacuolar/Golgi V-ATPase evidence; drafted in PR #5273
- [x] `SCHPO/vma8` - fission-yeast V-ATPase subunit D with PomBase ORFeome
  localization and PTHR11671 PAINT rows; drafted in PR #5274
- [x] `CANAL/VMA8` - CGD *Candida albicans* V-ATPase subunit D; drafted in PR
  #5276
- [x] `NEUCR/vma-8` - *Neurospora crassa* V-ATPase subunit D with direct 1999
  V-ATPase subunit evidence; drafted in PR #5275

## Family 12: V-type ATPase Catalytic Subunit A

`PTHR43607` contains the conserved V-type ATPase catalytic A-subunit family.
The family-root `PANTHER:PTN000389800` node carries the rotary
proton-transporting ATPase activity and proton-transport process assertions,
`PANTHER:PTN000389802` places V1-domain membership on the eukaryotic branch,
and fungal node `PANTHER:PTN001032540` asserts fungal-type vacuole membrane
localization for the vacuolar proton pump.

- [x] `yeast/VMA1` - *S. cerevisiae* V1 catalytic A subunit and PI-SceI/VDE
  intein precursor; drafted in PR #5279
- [x] `SCHPO/vma1` - fission-yeast V-ATPase A subunit with PomBase
  disruption evidence; drafted in PR #5278
- [x] `CANAL/TFP1` - CGD *Candida albicans* V-ATPase A subunit with
  filamentation, stress, and acidification literature; drafted in PR #5281
- [x] `NEUCR/vma-1` - *Neurospora crassa* V-ATPase A subunit with direct
  vacuolar ATPase context; drafted in PR #5280

## Family 13: Mevalonate Kinases

`PTHR43290` is a compact GHMP-kinase family whose local fungal members all sit
in the mevalonate kinase subfamily `PTHR43290:SF2`. PAINT places
`GO:0004496` mevalonate kinase activity, `GO:0005829` cytosol, and
`GO:0019287` IPP biosynthesis via mevalonate at the family-root
`PANTHER:PTN000048555` node, adds fungal `GO:0006696` ergosterol biosynthetic
process on `PANTHER:PTN000825284`, and keeps metazoan cholesterol biosynthesis
on the separate animal node `PANTHER:PTN000825262`. The same PAINT file also
records the non-fungal branch structure: eukaryotic `PANTHER:PTN002214956`
prunes the root mevalonate-kinase and IPP-biosynthesis assertions by IRD, while
plant `PANTHER:PTN008680403` carries `GO:0047940` glucuronokinase activity.

- [x] `yeast/ERG12` - *S. cerevisiae* mevalonate-kinase anchor; merged in PR
  #5765
- [x] `SCHPO/erg12` - fission-yeast mevalonate kinase; re-reviewed in PR
  #5358
- [x] `ASPFU/erg12` - *Aspergillus fumigatus* mevalonate kinase; drafted in PR
  #5359
- [x] `CANAL/ERG12` - *Candida albicans* mevalonate kinase; drafted in PR #5361

## Family 14: ALO/GULO Aldonolactone Oxidoreductases

`PTHR43762` contains a broad `GO:0016491` oxidoreductase placement and a
plant/animal/bacterial L-ascorbate-biosynthesis placement at
`PANTHER:PTN000356408`, a CGD/SGD-seeded exact `GO:0003885`
D-arabinono-1,4-lactone oxidase node at `PANTHER:PTN000356435`, a
Dikarya mitochondrial node at `PANTHER:PTN001015900`, and an IRD on that
Dikarya node that prunes the L-ascorbate process rather than fungal
D-erythroascorbate biosynthesis.

- [x] `yeast/ALO1` - *S. cerevisiae* ALO1 anchor; revalidated without changes
- [x] `CANAL/ALO1` - CGD *Candida albicans* `CANAL/ALO1` seed; revalidated without
  changes
- [x] `NEUCR/alo-1` - *Neurospora crassa* ALO-family member; revalidated
  without changes
- [x] `SCHPO/alo1` - fission-yeast ALO-family member with PomBase NOT IGC rows
  against exact substrate/process transfer; marked `COMPLETE` in PR #5368

## Family 15: Saccharopine Dehydrogenases

`PTHR11133` contains a broad eukaryotic saccharopine-dehydrogenase ancestor,
`PANTHER:PTN000123605`, that carries `GO:0004753 saccharopine dehydrogenase
activity` and `GO:0005737 cytoplasm`. PAINT places `GO:0009085 L-lysine
biosynthetic process` on two separate fungal nodes: `PANTHER:PTN000875292` for
the NAD(+), L-lysine-forming `LYS1`/`lys3` branch and
`PANTHER:PTN000875327` for the reciprocal NADP(+), L-glutamate-forming
`LYS9`/`lys9` branch.

- [x] `yeast/LYS1` - *S. cerevisiae* peroxisomal/cytosolic
  LYS1-family enzyme; merged in PR #5436
- [x] `yeast/LYS9` - *S. cerevisiae* LYS9-family saccharopine reductase;
  merged in PR #5442
- [x] `SCHPO/lys3` - fission-yeast LYS1-family member; merged in PR #5439
- [x] `SCHPO/lys9` - fission-yeast LYS9-family member; merged in PR #5445
- [x] `CANAL/LYS1` - CGD-seeded *Candida albicans* LYS1-family member; merged
  in PR #5434
- [x] `NEUCR/lys-4` - *Neurospora crassa* LYS1-family member; merged in PR
  #4644

## Family 16: Homocysteine/Cysteine Synthases

`PTHR43797` is a compact homocysteine/cysteine synthase family. Its fungal
members sit in `PTHR43797:SF2`, and the current PAINT file places cytoplasm,
`GO:0051009` O-acetylhomoserine sulfhydrylase activity, and
`GO:0071269` L-homocysteine biosynthetic process on the shared
`PANTHER:PTN002887184` node seeded by *S. cerevisiae* `MET17`,
*S. pombe* `met17`, the CGD *C. albicans* `MET15` member, and bacterial MetY.

- [x] `yeast/MET17` - *S. cerevisiae* bifunctional Met17/Met15 enzyme; merged
  in PR #5451
- [x] `SCHPO/met17` - fission-yeast O-acetylhomoserine sulfhydrylase; merged in
  PR #5450
- [x] `CANAL/MET15` - CGD *Candida albicans* MET15 seed with 2024 direct
  CaMet15p biochemical evidence; merged in PR #5447
- [x] `EMENI/cysD` - *Aspergillus nidulans* CysD member in the same
  PTHR43797:SF2 subfamily; merged in PR #5449

## Family 17: HMG-CoA Reductases

`PTHR10572` contains the conserved `PANTHER:PTN000060346` HMG-CoA reductase
activity and broad isoprenoid-biosynthesis node, the eukaryotic
`PANTHER:PTN000060347` membrane node that carries both ER and over-propagated
peroxisomal localization, and the fungal `PANTHER:PTN000832055` ergosterol
node seeded by a canonical sterol-pathway HMGR. The short AN1593 branch is an
exception to the ER and ergosterol propagation, but retains the catalytic and
broad isoprenoid-biosynthesis terms.

- [x] `yeast/HMG1` - *S. cerevisiae* major HMG-CoA reductase isozyme; merged in
  PR #5463
- [x] `yeast/HMG2` - *S. cerevisiae* regulated minor HMG-CoA reductase isozyme;
  merged in PR #5464
- [x] `SCHPO/hmg1` - essential fission-yeast HMG-CoA reductase; existing
  exemplar; merged in PR #5460
- [x] `CANAL/HMG1` - Candida albicans long sterol-pathway HMG-CoA reductase;
  merged in PR #5454
- [x] `ASPFU/hmg1` - Aspergillus fumigatus long sterol-pathway HMG-CoA
  reductase; merged in PR #5456
- [x] `ASPFU/hmg2` - Aspergillus fumigatus Hmg1-related HMG-CoA reductase;
  merged in PR #5458
- [x] `EMENI/AN1593` - Aspergillus nidulans short pimaradiene-cluster
  HMG-CoA reductase; merged in PR #5459

---

# NOTES

## 2026-11-01

- Cleaned the PTHR11638, PTHR11133, PTHR43797, PTHR43290, and PTHR10572
  ledger rows touched by this PR shepherding pass. The `yeast/HSP104`,
  `CANAL/LYS1`, `SCHPO/lys3`, `yeast/LYS1`, `yeast/LYS9`, `SCHPO/lys9`,
  `CANAL/MET15`, `SCHPO/met17`, `yeast/MET17`, `EMENI/cysD`, `CANAL/HMG1`,
  `ASPFU/hmg1`, `ASPFU/hmg2`, `EMENI/AN1593`, `SCHPO/hmg1`, `yeast/HMG1`,
  `yeast/HMG2`, and `yeast/ERG12` reviews have merged in PRs #3692, #5434,
  #5439, #5436, #5442, #5445, #5447, #5450, #5451, #5449, #5454, #5456,
  #5458, #5459, #5460, #5463, #5464, and #5765.
- Confirmed the PTHR19370 fungal NADH-cytochrome b5 reductase set is already
  complete across the MCR1, CBR1, and related CYC2-like branches, including
  the October MCR1/CBR1 follow-up PRs #5413-#5415 and #5419-#5423.

## 2026-10-24

- Added `PTHR43797`, the compact homocysteine/cysteine synthase family, as the
  next fungal PAINT tranche. The initial batch covers the existing
  `yeast/MET17` and `SCHPO/met17` drafts plus CGD `CANAL/MET15` and
  `EMENI/cysD`, all of which fall in `PTHR43797:SF2` under the shared
  `PTN002887184` PAINT node for homocysteine synthase activity and
  L-homocysteine biosynthesis.
- Started PTHR10572 HMG-CoA reductases with `CANAL/HMG1`. The family review
  already marks the exact HMG-CoA reductase, broad isoprenoid/sterol, ER
  membrane, and fungal ergosterol-biosynthesis IBD rows as sound while flagging
  the eukaryotic peroxisomal-membrane IBA for fungal pruning.
- Continued PTHR10572 with `ASPFU/hmg1`, carrying forward the same conserved
  exact HMG-CoA reductase, isoprenoid, ER-membrane, fungal ergosterol, and
  fungal peroxisomal-overpropagation decisions into a siderophore-producing
  filamentous ascomycete.

- Started `PTHR10572`, separating long fungal sterol-pathway HMG-CoA
  reductases from Aspergillus short cluster paralogs. `CANAL/HMG1`,
  `ASPFU/hmg1`, `ASPFU/hmg2`, and `SCHPO/hmg1` all remove the stale
  peroxisomal-membrane IBA from `PTN000060347` while keeping exact HMGR
  activity and the ER-membrane and fungal ergosterol branches where appropriate;
  `EMENI/AN1593` keeps exact HMGR catalysis but removes ergosterol and
  ER-specific terms that overreach the pimaradiene-cluster paralog.
- Re-reviewed the compact `PTHR43290` mevalonate-kinase set across
  `yeast/ERG12`, `SCHPO/erg12`, `ASPFU/erg12`, and `CANAL/ERG12`. The fission
  yeast, Aspergillus, and Candida reviews were updated in PRs #5358-#5361;
  budding-yeast `ERG12` was already complete. All reviewed fungal members align
  with root `PTN000048555` for mevalonate kinase activity, cytosol, and
  mevalonate-pathway IPP biosynthesis, and with fungal `PTN000825284` for
  ergosterol biosynthesis.
- Finished the `PTHR43762` ALO/GULO tranche across `yeast/ALO1`,
  `SCHPO/alo1`, `CANAL/ALO1`, and `NEUCR/alo-1`. The S. pombe review needed
  only completion/follow-up in PR #5368: it keeps PomBase NOT rows against exact
  D-arabinono-1,4-lactone oxidase and D-erythroascorbate biosynthesis, records
  the anomalous deprecated `GO_REF:0000025` IGC citation as a source defect, and
  treats broad PAINT/ARBA parent rows as too general beside `GO:0016899`.
- Started `PTHR10572`, separating long fungal sterol-pathway HMG-CoA
  reductases from Aspergillus short cluster paralogs. `CANAL/HMG1`,
  `ASPFU/hmg1`, and `ASPFU/hmg2` retain the fungal ergosterol node where
  supported; `EMENI/AN1593` keeps exact HMGR catalysis but removes ergosterol
  and precise ER localization because the direct literature places it in the
  pimaradiene secondary-metabolite cluster.

## 2026-10-21

- Drafted the compact `PTHR10969` ATG8 set across `yeast/ATG8`,
  `SCHPO/atg8`, `CANAL/ATG8`, `NEUCR/apg-6`, `ASPFU/atg8`, and
  `EMENI/atg8`. All six reviews endorse the eukaryotic `PTN000103522`
  ATG8/LC3/GABARAP PAINT placements and the fungal `PTN000861115`
  fungal-type vacuole membrane placement. The reviews handled generic
  `GO:0005774` vacuolar-membrane rows as broad source annotations that
  should not add a second core location beside fungal-type vacuole membrane.
- Drafted the compact `PTHR11671` V-ATPase subunit D set across
  `yeast/VMA8`, `SCHPO/vma8`, `CANAL/VMA8`, and `NEUCR/vma-8` in PRs
  #5273-#5276. All four reviews treat `PTN000912657` as the curated fungal
  vacuolar V-ATPase node and retain Vma8's `contributes_to` relation to rotary
  proton-transporting ATPase activity. The set distinguishes the supported
  stress-induced vacuolar membrane-raft localization in `yeast/VMA8` from
  unsupported cross-species transfers in `CANAL/VMA8` and `NEUCR/vma-8`, and
  records standalone `enables GO:0046961` rows as relation problems where the
  upstream source asserts full pump activity for non-catalytic subunit D.
- Drafted the compact `PTHR10806` Sec11/SPC catalytic-subunit set across
  `yeast/SEC11`, `SCHPO/sec11`, `CANAL/SEC11`, `NEUCR/sec11`, `ASPFU/sec11`,
  and `EMENI/sec11` in PRs #5264-#5269. All six reviews accept the eukaryotic
  `PTN000086750` signal-peptidase-complex placement, treat its
  `GO:0051604 protein maturation` row as correct but generic beside exact
  `GO:0016485 protein processing`, treat the root `PTN000086749` peptidase
  assertion as correct but generic beside exact `GO:0009003 signal peptidase
  activity`, and reject propagated `GO:0045047 protein targeting to ER` where
  it confuses signal-peptide cleavage with the upstream targeting step.
- Drafted the compact `PTHR43607` V-ATPase catalytic A-subunit set across
  `yeast/VMA1`, `SCHPO/vma1`, `CANAL/TFP1`, and `NEUCR/vma-1` in PRs
  #5278-#5281. All four reviews accept the root PAINT activity/transport node,
  the eukaryotic V1-domain node, and the fungal vacuole-membrane node, while
  handling species-specific biology such as the budding-yeast PI-SceI/VDE
  intein and Candida TFP1 phenotypes outside the conserved catalytic core.

## 2026-10-17

- Started the compact WDR12/Ytm1 set in `PTHR19855` across `yeast/YTM1`,
  `SCHPO/ytm1`, `CANAL/YTM1`, and `NEUCR/ytm1`; the individual gene reviews
  merged in PRs #5117, #5118, #5120, and #5121.

## 2026-10-11

- Drafted `CANAL/CHS7` to complete the compact `PTHR35329` CHS7-family set.
  The review accepts the `PANTHER:PTN002175570` ER-membrane, protein-folding,
  and chitin-biosynthesis IBAs, adds the current PAINT `GO:0044183 protein
  folding chaperone` assertion as a `NEW` row, removes the stale no-data
  molecular-function placeholder, and keeps the direct C. albicans morphology
  annotations as non-core outcomes of impaired Chs3-dependent wall chitin
  synthesis.

## 2026-10-05

- Started the project by scanning cached `*-paint.tsv` PAINT files for fungal
  ancestral-node assertions at `taxon:4751` and child fungal clades, then
  cross-referencing `*-entries.csv` files for local *S. cerevisiae*,
  *S. pombe*, *C. albicans*, and *N. crassa* proteins.
- Chose `PTHR11638` as the first family because the fungal PAINT split is
  compact: `Hsp104`-like cytosolic disaggregases and Hsp78-like mitochondrial
  disaggregases. The family also includes a CGD `HSP104` seed and a curated
  *S. cerevisiae* HSP104 review that already records how the current PAINT nodes
  ground the IBA rows.
- Drafted `CANAL/HSP104` as the first CGD review. The `HSP104`-node IBAs were
  accepted, the direct C. albicans heat-acclimation rows were accepted, the
  Candida biofilm row was kept as a non-core phenotype, generic `protein
  folding` was redirected to `protein refolding`, and an abstract-only
  cell-surface assignment was left undecided pending full-text verification.
- Drafted `NEUCR/hsp98` as the first filamentous-fungal review. The fungal
  `Hsp104` IBA rows were accepted from the PAINT node placements, and the
  similarity-based nuclear localization row was left undecided because the
  cached Neurospora hsp98 paper does not test nuclear recruitment.

## 2026-10-09

- Drafted `yeast/HSP78` as the experimental mitochondrial Hsp78 anchor. The
  Hsp78-specific `PANTHER:PTN000909045` IBAs were accepted, the mixed-node
  `cytoplasm` IBA was marked over-annotated, generic `protein folding` and
  `intracellular organelle lumen` rows were redirected to `protein refolding`
  and `mitochondrial matrix`, and a direct `GO:0140545 ATP-dependent protein
  disaggregase activity` proposal was added from Hsp78 disaggregation assays.
- Drafted `SCHPO/hsp104` and accepted the fungal `Hsp104`-node IBAs on
  `PANTHER:PTN007521008`. Two narrow localization rows remain unresolved pending
  full-text inspection: the ORFeome-derived nuclear-envelope row and the NuR
  row whose cached abstract shows `hsp104`-dependent disaggregation but not
  `hsp104` localization to NuRs.
- Drafted `SCHPO/hsp78` and `CANAL/HSP78` as mitochondrial Hsp78 orthologs.
  Both retain the Hsp78-node matrix/refolding/unfolding IBAs, both flag the
  broad mixed-node `cytoplasm` IBA as over-scoped, and the Candida review now
  proposes `GO:0140545` by ISO from SGD HSP78.

## 2026-10-10

- Opened sibling PRs for the six drafted Hsp100/ClpB reviews: `yeast/HSP78`
  (#4519), `NEUCR/hsp98` (#4520), `SCHPO/hsp78` (#4521), `CANAL/HSP78`
  (#4522), `CANAL/HSP104` (#4523), and `SCHPO/hsp104` (#4524).
- Started the PTHR31297 fungal glucanase family with `yeast/EXG1`. Its exact
  exo-1,3-beta-glucosidase IBA from `PTN001262687` and fungal extracellular
  wall beta-glucan IBAs from `PTN001262686` were retained, while the broader
  Aspergillus-seeded `PTN001262628` glucan-catabolism IBA was marked as
  over-scoped for the EXG1/XOG1/Spr1 subclade.
- Merged all six sibling Hsp100/ClpB reviews, bringing the mitochondrial Hsp78
  and cytosolic non-*S. cerevisiae* Hsp104/hsp98 PAINT checks onto `main`.
- Re-reviewed `yeast/SAS3` in the MYST family. Broad
  `PANTHER:PTN004172926` IBA rows fit Sas3's conserved MYST activity in
  chromatin, and the fungal `PANTHER:PTN008308138` row correctly places the
  NuA3a complex assertion on the Sas3 branch.
- Re-reviewed `yeast/ESA1` as the first MYST-family entry. The current
  `PTHR10615` PAINT assertions are consistent with ESA1's placement under the
  broad eukaryotic MYST and fungal ESA1/H4-acetyltransferase nodes; the refresh
  mostly added current GOA rows, removed generic `protein binding`, and
  redirected a nucleosome component row to `GO:0031491 nucleosome binding`.
- Re-reviewed `yeast/SAS2` in the MYST family. The `PANTHER:PTN007449682`
  activity transfer to `GO:0046972 histone H4K16 acetyltransferase activity`
  is correct for Sas2/SAS-I, but the same node leaks `GO:0035267 NuA4 histone
  acetyltransferase complex` across the Sas2-versus-TIP60 complex boundary.
- Started `PTHR35329` as a compact CHS7-family follow-up. Yeast `CHS7` was
  already reviewed; `NEUCR/csc-1` checks the same `PTN002175570` fungal PAINT
  ancestor against the direct CSE-7/CHS-4 trafficking paper and the newer
  CSE-8 paralog paper, leaving `CANAL/CHS7` as the next Candida seed to review.

## 2026-10-11

- Re-reviewed `yeast/HOG1` against `PTHR24055`. The broad
  `PANTHER:PTN000622075` Ser/Thr kinase, nucleus, and cytoplasm rows all remain
  appropriate for an experimentally characterized MAPK, and the fungal
  `PANTHER:PTN001172058` osmosensory/stress-MAPK placements fit the budding
  yeast HOG cascade. The oxidative-stress IBA is valid but secondary for
  budding yeast, so it remains non-core while the ancestral node itself is
  recorded as `NO_FAILURE_NON_CORE`.
- Drafted `SCHPO/mst2` in `PTHR10615`. The broad `PTN004172926` MYST-family
  IBAs are appropriate for Mst2, while the fungal `PTN008308138`
  NuA3a-complex IBA is too exact for the related fission-yeast Mst2 complex and
  was redirected to `GO:0036410`. The direct Mst2 heterochromatin rows were
  aligned with the negative-regulation model supported by the 2011, 2015, 2024,
  and 2026 fission-yeast papers.
- Rechecked the existing `CANAL/ESA1` CGD MYST review. The broad
  `PANTHER:PTN004172926` MYST-root IBA rows and the fungal ESA1-node
  `PANTHER:PTN000834946` H4 acetyltransferase row still align with the
  PTHR10615 tree, while PMID:40988556 remains abstract-free and unresolved for
  the CGD phenotypic-switching row.
- Added PTHR11635, the cAMP-dependent protein kinase regulatory-subunit family,
  as a fungal PAINT family. The first two reviews check the conserved PKA-R
  node, the fungal nuclear node, and the broad cAMP-signaling node in
  *C. albicans* `BCY1` and *N. crassa* `mcb`.
- Drafted `NEUCR/mcb`. The four `PTN004280545` activity/complex IBAs were
  accepted, `PTN000908765` nucleus was accepted as a fungal inference without
  contrary Neurospora localization data, and the over-specific `GO:0007189`
  GPCR pathway row from `PTN000180782` was redirected to neutral
  `GO:0141156` cAMP/PKA signal transduction.
- Drafted the `yeast/BCY1` anchor review. It keeps Bcy1's starvation, P-body,
  chromatin, and plasma-membrane rows as non-core contexts, narrows TPK
  `protein binding` rows to `protein kinase A catalytic subunit binding`,
  removes the Ess1 generic binding rows, leaves an abstract-only
  Siva/PMP22-cited self-interaction row undecided, and removes Ras/Lte1
  bud-neck localization rows where `bcy1` was only a bypass background.
- Rechecked `NEUCR/esa-1` as the filamentous-fungal ESA1 representative in
  `PTHR10615:SF218`. The fungal `PANTHER:PTN000834946` H4-acetyltransferase
  row and the broad eukaryotic `PANTHER:PTN004172926` MYST-root rows remain
  sound against the PAINT placement; the second-pass edits only tightened
  UniProt evidence snippets.
- Added `PTHR10868` as a compact sterol C-8 isomerase family after sibling
  `yeast/ERG2`, `SCHPO/erg2`, and `NEUCR/erg-1` reviews had checked the same
  fungal node placements. The `CANAL/ERG2` follow-up accepts the fungal
  `PTN001280219` C-8 sterol isomerase and ergosterol-biosynthesis IBAs,
  accepts the broader `PTN001328958` ER localization IBA, and verifies that
  animal Sigma-receptor signaling assertions are confined to descendant PTNs
  outside the fungal ERG2 rows.
