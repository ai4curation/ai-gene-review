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

---

# STATUS

Last updated: 2026-10-10

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

## Later Candidates

- [ ] `PTHR24055` MAP kinases across HOG/p38 and pheromone pathways
- [ ] `PTHR31297` fungal glucan exo-1,3-beta-glucosidases
- [ ] `PTHR19370` fungal NADH-cytochrome b5 reductases
- [ ] `PTHR10615` MYST-family histone acetyltransferases
- [ ] `PTHR43762` fungal D-arabinono-1,4-lactone oxidases

## Family 2: Chitin Synthase Export Chaperones

`PTHR35329` contains a compact fungal CHS7-family ancestor,
`PANTHER:PTN002175570`, with PAINT assertions for ER membrane, chitin
biosynthetic process, protein folding, and protein folding chaperone activity.

- [x] `yeast/CHS7` - *S. cerevisiae* CHS7 anchor; already reviewed and aligned
  to the current `PTN002175570` PAINT assertions before this project
- [x] `NEUCR/csc-1` - *Neurospora crassa* CSE-7/CHS-4 export factor; drafted
  in this branch
- [ ] *Candida albicans* Q5AA40 - CGD seed for the
  `GO:0006031 chitin biosynthetic process` IBD

---

# NOTES

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
- Merged all six sibling Hsp100/ClpB reviews, bringing the mitochondrial Hsp78
  and cytosolic non-*S. cerevisiae* Hsp104/hsp98 PAINT checks onto `main`.
- Started `PTHR35329` as a compact CHS7-family follow-up. Yeast `CHS7` was
  already reviewed; `NEUCR/csc-1` checks the same `PTN002175570` fungal PAINT
  ancestor against the direct CSE-7/CHS-4 trafficking paper and the newer
  CSE-8 paralog paper, leaving `CANAL/CHS7` as the next Candida seed to review.
