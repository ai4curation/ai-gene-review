---
title: "Fungal PAINT Family Reviews"
maturity: IN_PROGRESS
collections: [HOMOLOGY_PROPAGATION]
species: [yeast, SCHPO, CANAL, NEUCR]
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

---

# STATUS

Last updated: 2026-10-11

## Family 1: Hsp100/ClpB Disaggregases

`PTHR11638` contains two fungal PAINT subtrees relevant to this batch:
cytosolic Hsp104-family disaggregases at `PANTHER:PTN007521008` and
mitochondrial Hsp78-family disaggregases at `PANTHER:PTN000909045`.

- [ ] `yeast/HSP104` - cytosolic ATP-dependent disaggregase; existing
  curated anchor, not yet rechecked in this project
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
- [ ] `SCHPO/mst1` - fission yeast MYST acetyltransferase
- [x] `SCHPO/mst2` - fission yeast MYST acetyltransferase; drafted in this branch
- [x] `CANAL/ESA1` - CGD-seeded Esa1/NuA4 catalytic subunit; merged in PR
  #4774
- [ ] `NEUCR` MYST-family member

## Later Candidates

- [ ] `PTHR24055` MAP kinases across HOG/p38 and pheromone pathways
- [ ] `PTHR31297` fungal glucan exo-1,3-beta-glucosidases
- [ ] `PTHR19370` fungal NADH-cytochrome b5 reductases
- [ ] `PTHR43762` fungal D-arabinono-1,4-lactone oxidases

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
- [ ] `SCHPO/sty1` - fission yeast Sty1/Spc1 stress MAPK; drafted in PR #4573
  and awaiting follow-up review
- [ ] `yeast/HOG1` - *S. cerevisiae* HOG stress MAPK; drafted in this branch

## Family 5: Fungal Glucanases

`PTHR31297` contains several fungal GH5 glucanase subtrees. The current
EXG1/XOG1-family IBA rows split over a broad Aspergillus-root
`PTN001262628` glucan-catabolism node, a fungal `PTN001262686` extracellular
cell-wall beta-glucan node, and a Saccharomycetes `PTN001262687`
exo-1,3-beta-glucosidase node.

- [x] `yeast/EXG1` - secreted exo-1,3-beta-glucosidase; drafted in PR #4610
- [ ] `yeast/SPR1` - sporulation-specific glucanase in the EXG1/Spr1/XOG1
  clade
- [ ] `SCHPO/exg1` - fission-yeast extracellular glucanase seed for the
  fungal wall beta-glucan node
- [ ] `CANAL/XOG1` - CGD-seeded *Candida albicans*
  exo-1,3-beta-glucosidase; review in PR #4596
- [ ] `NEUCR/NCU09652` - *Neurospora crassa* PTHR31297 member to place against
  the yeast, PomBase, and CGD subtrees

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

---

# NOTES

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
- Added `PTHR10868` as a compact sterol C-8 isomerase family after sibling
  `yeast/ERG2`, `SCHPO/erg2`, and `NEUCR/erg-1` reviews had checked the same
  fungal node placements. The `CANAL/ERG2` follow-up accepts the fungal
  `PTN001280219` C-8 sterol isomerase and ergosterol-biosynthesis IBAs,
  accepts the broader `PTN001328958` ER localization IBA, and verifies that
  animal Sigma-receptor signaling assertions are confined to descendant PTNs
  outside the fungal ERG2 rows.
