---
title: "Chromatin: complexes, locations and the GO chromatin subtree"
maturity: SCOPING
last_reviewed: '2026-11-14'
tags: [BIOLOGY_DOMAIN]
species: [yeast]
genes: [HAT1, HAT2, HIF1]
---

# Chromatin: complexes, locations and the GO chromatin subtree

**Bottom line:** GO's chromatin term (GO:0000785) is deliberately not part of
the nucleus, which is defensible, but the terms below it are inconsistent.
Some chromatin-acting complexes are asserted to be part of chromatin while
their close relatives are not, and one of those assertions is wrong. This
project curates chromatin-acting complexes as modules, starting with the
*S. cerevisiae* histone acetyltransferases. Each module records where the
complex actually acts, so module curation and the ontology question inform
each other. The first module is the type B histone acetyltransferase (HAT-B,
Hat1-Hat2-Hif1).

## Why chromatin is not part of the nucleus

Chromatin is `part_of` chromosome, and chromosome has no link to nucleus. The
nucleus link sits on GO:0000228 nuclear chromosome. "Nuclear chromatin"
(GO:0000790) was merged into chromatin in
[geneontology/go-ontology#20000](https://github.com/geneontology/go-ontology/issues/20000),
because chromatin is outside a nucleus during open mitosis. Two other reasons
support keeping it that way:

- Nucleus is restricted to Eukaryota (`only_in` taxon 2759). A
  chromatin-`part_of`-nucleus link would make the archaeal annotations to
  chromatin and nucleosome (57 in QuickGO on 2026-11-14, all IEA) taxon
  violations, although some archaea do package DNA with histones.
- The practical cost is small. In the human GAF, 18 of 1,431 genes with a
  chromatin annotation (1.3%) have no annotation that reaches nucleus, so a
  "genes in the nucleus" query misses only 0.17% of its 10,810 genes. Several
  of the 18 look like questionable chromatin annotations in the first place.

For location-based drawing of GO-CAMs (AmiGO 3), 1,071 of 10,609 activity
locations in the cached GO-CAM index (10.1%) reach none of nucleus,
cytoplasm, plasma membrane or extracellular region by is_a/part_of. Of these,
497 are under chromosome (chromatin alone: 193 activities in 90 models). A
display-only default table (anything under chromosome is drawn in the nucleus
for eukaryotic models, flagged as a layout default) handles most of them
without asserting anything in the ontology.

## The problem in the chromatin subtree

The is_a children of chromatin mix four axes (state, composition, position
and condition). Logical definitions exist for only two of the position-based
terms. There is no constitutive or facultative heterochromatin term, and
nucleolus organizer region and sex chromatin have definitions that disagree
with their placement.

The bigger problem is in the part_of children:

| Complex | Asserted location |
|---|---|
| histone acetyltransferase complex (GO:0000123) | part_of chromatin |
| HDA1, Set3, Sin3-type, Rpd3L-Expanded, Snt2C complexes | part_of chromatin |
| histone deacetylase complex (GO:0000118), their parent | part_of nucleoplasm |
| histone methyltransferase complex (GO:0035097) | part_of nucleoplasm |
| chromatin silencing complex (GO:0005677) | part_of nucleus |
| cohesin, condensin | part_of chromosome |
| SWI/SNF superfamily-type, FACT, HULC, Swi5-Sfr1, Swi5-Swi2, dosage compensation | part_of chromatin |

GO:0000123 is logically defined as any complex capable of histone
acetyltransferase activity, so its `part_of chromatin` edge is inherited by
every such complex. That includes the type B enzyme, which acetylates histone
H4 before the histone is deposited into chromatin. The edge came in with
[geneontology/go-ontology#23892](https://github.com/geneontology/go-ontology/issues/23892),
because nucleoplasm is defined as "nuclear content other than the
chromosomes"; that definition makes the `part_of nucleoplasm` links on the
deacetylase and methyltransferase complexes equally questionable. Removing
`part_of chromatin` from the complexes (keeping nucleosome) would drop 120
human genes from chromatin queries, 109 of which still reach nucleus through
other annotations. A go-ontology issue setting this out has been drafted for
filing.

## Modules

| Module | Members | Status | Notes |
|---|---|---|---|
| [HAT-B complex](../modules/scer_hat_b_complex.html) (`modules/scer_hat_b_complex.yaml`) | HAT1, HAT2, HIF1 | DRAFT | Proposes a GO term for the type B HAT complex and records the GO:0000123 `part_of chromatin` edge as a proposed deletion. Two biology gaps: free H4 versus H3-H4 dimer as substrate, and HAT-B's role at double-strand breaks. |

The HAT-B case is concrete: all three yeast subunits are annotated `part_of`
GO:0000123 (IDA, IPI), so they inherit `part_of chromatin`. Meanwhile
UniProt's curated text for Hat1 says it acetylates free histone H4 in the
cytoplasm and that modification of chromatin-packaged H4 is not established.

## Plan

Yeast histone acetyltransferase complexes, each as its own module:

- [x] HAT-B (Hat1, Hat2, Hif1)
- [ ] gene reviews for HAT1, HAT2 and HIF1 (scaffolds created; annotations PENDING)
- [ ] Rtt109-Vps75 (H3K56 acetylation of new histones; RTT109 already reviewed)
- [ ] NuA4 and piccolo NuA4 (Esa1, Epl1, Yng2; ESA1 already reviewed)
- [ ] SAGA HAT module (Gcn5, Ada2, Ada3, Sgf29; GCN5 already reviewed)
- [ ] NuA3 (Sas3; SAS3 already reviewed)
- [ ] SAS-I (Sas2, Sas4, Sas5; SAS2 already reviewed)

Then the deacetylase complexes asserted `part_of chromatin` (Rpd3L, Rpd3S,
Hda1, Set3, Snt2C) and the remodelers, so that every complex in the table
above has a module that records where it acts.

Ontology track:

- [ ] file the go-ontology issue on the chromatin subtree
- [ ] update the HAT-B module's `request_status` once filed

## Reproducing the numbers

Scripts are in [`CHROMATIN/scripts/`](CHROMATIN/scripts/). The figures above
came from go-basic.obo (`releases/2026-07-26`), goa_human.gaf (generated
2026-05-21) and `gocams/index.tsv` as committed on 2026-11-14:

```bash
python projects/CHROMATIN/scripts/chromatin_nucleus_queries.py go-basic.obo goa_human.gaf.gz
python projects/CHROMATIN/scripts/gocam_unplaced_locations.py go-basic.obo gocams/index.tsv
```

Both follow is_a and part_of only, and count protein rows only (NOT and
complex rows excluded).
