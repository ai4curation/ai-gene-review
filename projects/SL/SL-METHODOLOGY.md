---
title: "SL Methodology"
maturity: SCOPING
tags: [PIPELINE]
autolink_gene_symbols: false
---

# SL Methodology

Supporting page for [the SL project](../SL.md). All tables are generated:

```bash
uv run python projects/SL/scripts/scan_sl_unique.py
```

Takes ~5 minutes over the full `genes/` tree. Rerun and replace the tables wholesale.

## What counts as SL-unique

A gene's annotation to a GO term is **SL-unique** when `GO_REF:0000044` is the *only*
reference supporting that gene-term pair. If the same term also carries an IDA, an IBA, an
ISS, or any other reference, it is excluded — the point is to isolate annotations where the
UniProt subcellular-location mapping is the sole load-bearing evidence.

This mirrors the SPKW project's definition of keyword-unique annotations, with one
simplification. SPKW had to reverse-map GO terms to their originating keywords through the
external2go `keyword2go` file, because the GAF stores only the GO term. Here the source is in
the annotation: the WITH/FROM column carries `UniProtKB-SubCell:SL-xxxx`, so per-location
statistics fall out of the same scan.

Two caveats on the definition:

- **Closure is not applied.** SPKW's methodology filters annotations whose term is an ancestor
  of another term the gene already has, which removed 70%+ of naive hits in well-curated
  organisms. That filter is not applied here, so some SL-unique annotations are redundant
  rather than wrong. Given that the headline finding is precisely about under-specified terms,
  adding closure filtering would remove the signal being measured — but it means the 39%
  "downgraded or worse" figure mixes redundancy with error. The 8% hard-issue rate is the more
  conservative number.
- **The corpus is not a sample of GOA.** These 1,380 gene folders were selected for review for
  unrelated reasons. Rates here describe this corpus, not the pipeline at large.

## Reading the tables

- The **by GO term** and **by SL location** tables are near-duplicates by construction, since
  the mapping is close to one-to-one. Divergences between them are worth a look: they mean one
  GO term is reached from more than one SL location, or vice versa.
- "Issues" counts `REMOVE`, `MARK_AS_OVER_ANNOTATED`, and `MODIFY`. `KEEP_AS_NON_CORE` is
  excluded — it is a judgment that the location is real but peripheral, which is a different
  claim from the annotation being wrong.
- Rows below 10 reviewed annotations are omitted. SL-0221, the subject of the first
  subproject, now falls below that threshold because GO:0034045 is obsolete and GOA no longer
  seeds that SubCell mapping into new rows; it is documented separately.

## SL names

Names are resolved live from `https://rest.uniprot.org/locations/SL-xxxx`. Pass `--offline`
to skip the lookup when running without network access.

## Corpus totals

- SL-unique annotations (sole source GO_REF:0000044): **1852**
- distinct gene folders: **1380**
- reviewed SL-unique annotations: **1837**
- aspect: {'cellular_component': 1851, 'C': 1}
- actions: ACCEPT 1060, KEEP_AS_NON_CORE 567, MODIFY 74, MARK_AS_OVER_ANNOTATED 59, UNDECIDED 53, REMOVE 18, PENDING 6
- downgraded or worse: **718/1837 (39%)**
- issue rate (REMOVE/MARK_AS_OVER_ANNOTATED/MODIFY): **151/1837 (8%)**

## By GO term (>= 10 reviewed)

| Term | Label | Reviewed | Issues | Rate |
|---|---|---|---|---|
| GO:0005737 | cytoplasm | 234 | 9 | 4% |
| GO:0005886 | plasma membrane | 125 | 9 | 7% |
| GO:0005576 | extracellular region | 112 | 16 | 14% |
| GO:0005856 | cytoskeleton | 110 | 18 | 16% |
| GO:0016020 | membrane | 103 | 22 | 21% |
| GO:0005634 | nucleus | 103 | 8 | 8% |
| GO:0005789 | endoplasmic reticulum membrane | 50 | 0 | 0% |
| GO:0048471 | perinuclear region of cytoplasm | 34 | 3 | 9% |
| GO:0005794 | Golgi apparatus | 33 | 5 | 15% |
| GO:0000139 | Golgi membrane | 33 | 0 | 0% |
| GO:0005819 | spindle | 32 | 2 | 6% |
| GO:0005783 | endoplasmic reticulum | 24 | 2 | 8% |
| GO:0031902 | late endosome membrane | 22 | 0 | 0% |
| GO:0005813 | centrosome | 21 | 1 | 5% |
| GO:0005743 | mitochondrial inner membrane | 21 | 2 | 10% |
| GO:0005829 | cytosol | 21 | 0 | 0% |
| GO:0005694 | chromosome | 20 | 1 | 5% |
| GO:0042597 | periplasmic space | 20 | 2 | 10% |
| GO:0030665 | clathrin-coated vesicle membrane | 20 | 1 | 5% |
| GO:0042470 | melanosome | 18 | 0 | 0% |
| GO:0045202 | synapse | 18 | 1 | 6% |
| GO:0030425 | dendrite | 18 | 1 | 6% |
| GO:0030424 | axon | 17 | 0 | 0% |
| GO:0005938 | cell cortex | 17 | 1 | 6% |
| GO:0005759 | mitochondrial matrix | 16 | 1 | 6% |
| GO:0012505 | endomembrane system | 16 | 4 | 25% |
| GO:0005929 | cilium | 15 | 4 | 27% |
| GO:0005730 | nucleolus | 14 | 1 | 7% |
| GO:0031965 | nuclear membrane | 14 | 0 | 0% |
| GO:0030659 | cytoplasmic vesicle membrane | 14 | 0 | 0% |
| GO:0000922 | spindle pole | 14 | 0 | 0% |
| GO:0031966 | mitochondrial membrane | 14 | 5 | 36% |
| GO:0030672 | synaptic vesicle membrane | 12 | 0 | 0% |
| GO:0005654 | nucleoplasm | 12 | 1 | 8% |
| GO:0070161 | anchoring junction | 11 | 1 | 9% |
| GO:0043204 | perikaryon | 11 | 0 | 0% |
| GO:0005739 | mitochondrion | 11 | 1 | 9% |
| GO:0009507 | chloroplast | 11 | 1 | 9% |
| GO:0005776 | autophagosome | 11 | 1 | 9% |
| GO:0032580 | Golgi cisterna membrane | 11 | 0 | 0% |
| GO:0010008 | endosome membrane | 11 | 1 | 9% |
| GO:0030670 | phagocytic vesicle membrane | 10 | 0 | 0% |
| GO:0005768 | endosome | 10 | 1 | 10% |
| GO:0005774 | vacuolar membrane | 10 | 0 | 0% |
| GO:0005764 | lysosome | 10 | 0 | 0% |

## By UniProt subcellular location (>= 10 reviewed)

| SL | Name | Reviewed | Issues | Rate |
|---|---|---|---|---|
| SL-0086 | Cytoplasm | 234 | 9 | 4% |
| SL-0090 | Cytoskeleton | 110 | 18 | 16% |
| SL-0243 | Secreted | 107 | 16 | 15% |
| SL-0162 | Membrane | 103 | 22 | 21% |
| SL-0191 | Nucleus | 103 | 8 | 8% |
| SL-0039 | Cell membrane | 102 | 7 | 7% |
| SL-0097 | Endoplasmic reticulum membrane | 50 | 0 | 0% |
| SL-0198 | Perinuclear region | 34 | 3 | 9% |
| SL-0132 | Golgi apparatus | 33 | 5 | 15% |
| SL-0134 | Golgi apparatus membrane | 33 | 0 | 0% |
| SL-0251 | Spindle | 32 | 2 | 6% |
| SL-0095 | Endoplasmic reticulum | 24 | 2 | 8% |
| SL-0151 | Late endosome membrane | 22 | 0 | 0% |
| SL-0048 | Centrosome | 21 | 1 | 5% |
| SL-0168 | Mitochondrion inner membrane | 21 | 2 | 10% |
| SL-0091 | Cytosol | 21 | 0 | 0% |
| SL-0468 | Chromosome | 20 | 1 | 5% |
| SL-0200 | Periplasm | 20 | 2 | 10% |
| SL-0037 | Cell inner membrane | 20 | 2 | 10% |
| SL-0071 | Clathrin-coated vesicle membrane | 20 | 1 | 5% |
| SL-0161 | Melanosome | 18 | 0 | 0% |
| SL-0258 | Synapse | 18 | 1 | 6% |
| SL-0283 | Dendrite | 18 | 1 | 6% |
| SL-0279 | Axon | 17 | 0 | 0% |
| SL-0138 | Cell cortex | 17 | 1 | 6% |
| SL-0170 | Mitochondrion matrix | 16 | 1 | 6% |
| SL-0147 | Endomembrane system | 16 | 4 | 25% |
| SL-0066 | Cilium | 15 | 4 | 27% |
| SL-0188 | Nucleolus | 14 | 1 | 7% |
| SL-0182 | Nucleus membrane | 14 | 0 | 0% |
| SL-0089 | Cytoplasmic vesicle membrane | 14 | 0 | 0% |
| SL-0448 | Spindle pole | 14 | 0 | 0% |
| SL-0171 | Mitochondrion membrane | 14 | 5 | 36% |
| SL-0260 | Synaptic vesicle membrane | 12 | 0 | 0% |
| SL-0190 | Nucleoplasm | 12 | 1 | 8% |
| SL-0038 | Cell junction | 11 | 1 | 9% |
| SL-0197 | Perikaryon | 11 | 0 | 0% |
| SL-0173 | Mitochondrion | 11 | 1 | 9% |
| SL-0049 | Chloroplast | 11 | 1 | 9% |
| SL-0023 | Autophagosome | 11 | 1 | 9% |
| SL-0136 | Golgi stack membrane | 11 | 0 | 0% |
| SL-0100 | Endosome membrane | 11 | 1 | 9% |
| SL-0205 | Phagosome membrane | 10 | 0 | 0% |
| SL-0101 | Endosome | 10 | 1 | 10% |
| SL-0271 | Vacuole membrane | 10 | 0 | 0% |
| SL-0158 | Lysosome | 10 | 0 | 0% |


---

# Redundancy test

```bash
uv run python projects/SL/scripts/sl_redundancy.py
```

Asks, for each SL-unique annotation to term T, whether the gene carries any other CC term that
is a proper descendant of T under `is_a`/`part_of`, using the local GO SQLite build. Used to
test — and refute — the hypothesis that SL over-annotation is duplication; see
[the project page](../SL.md#the-redundancy-hypothesis-tested-and-refuted).

**The output below is post-intervention and partly circular**: the SL-0162 and SL-0090 review
batches deliberately selected redundant annotations. The result quoted on the project page is
the least biased pre-batch measurement.

## Redundancy of SL-unique annotations

- SL-unique annotations examined: **1852**
- with a review action: **1837**
- of those, the gene already carries a more specific CC term from another source: **652/1837 (35%)**

### Issue rate, split by redundancy

| Group | n | Issue rate | KEEP_AS_NON_CORE |
|---|---|---|---|
| Redundant (more specific term present) | 652 | 64/652 (10%) | 184 (28%) |
| Not redundant (SL term is the most specific) | 1185 | 87/1185 (7%) | 383 (32%) |

### By SL location (>= 10 reviewed)

| SL | GO term | n | Redundant | Issue rate | Issue rate if redundant | if not |
|---|---|---|---|---|---|---|
| SL-0086 | cytoplasm | 234 | 145 (62%) | 9/234 (4%) | 5/145 (3%) | 4/89 (4%) |
| SL-0090 | cytoskeleton | 110 | 89 (81%) | 18/110 (16%) | 15/89 (17%) | 3/21 (14%) |
| SL-0243 | extracellular region | 107 | 17 (16%) | 16/107 (15%) | 1/17 (6%) | 15/90 (17%) |
| SL-0162 | membrane | 103 | 68 (66%) | 22/103 (21%) | 15/68 (22%) | 7/35 (20%) |
| SL-0191 | nucleus | 103 | 47 (46%) | 8/103 (8%) | 2/47 (4%) | 6/56 (11%) |
| SL-0039 | plasma membrane | 102 | 20 (20%) | 7/102 (7%) | 0/20 (0%) | 7/82 (9%) |
| SL-0097 | endoplasmic reticulum membrane | 50 | 2 (4%) | 0/50 (0%) | 0/2 (0%) | 0/48 (0%) |
| SL-0198 | perinuclear region of cytoplasm | 34 | 0 (0%) | 3/34 (9%) | n/a | 3/34 (9%) |
| SL-0134 | Golgi membrane | 33 | 0 (0%) | 0/33 (0%) | n/a | 0/33 (0%) |
| SL-0132 | Golgi apparatus | 33 | 19 (58%) | 5/33 (15%) | 3/19 (16%) | 2/14 (14%) |
| SL-0251 | spindle | 32 | 26 (81%) | 2/32 (6%) | 2/26 (8%) | 0/6 (0%) |
| SL-0095 | endoplasmic reticulum | 24 | 4 (17%) | 2/24 (8%) | 0/4 (0%) | 2/20 (10%) |
| SL-0037 | plasma membrane | 23 | 3 (13%) | 2/23 (9%) | 0/3 (0%) | 2/20 (10%) |
| SL-0151 | late endosome membrane | 22 | 8 (36%) | 0/22 (0%) | 0/8 (0%) | 0/14 (0%) |
| SL-0168 | mitochondrial inner membrane | 21 | 4 (19%) | 2/21 (10%) | 1/4 (25%) | 1/17 (6%) |
| SL-0091 | cytosol | 21 | 0 (0%) | 0/21 (0%) | n/a | 0/21 (0%) |
| SL-0048 | centrosome | 21 | 3 (14%) | 1/21 (5%) | 0/3 (0%) | 1/18 (6%) |
| SL-0468 | chromosome | 20 | 16 (80%) | 1/20 (5%) | 1/16 (6%) | 0/4 (0%) |
| SL-0200 | periplasmic space | 20 | 4 (20%) | 2/20 (10%) | 2/4 (50%) | 0/16 (0%) |
| SL-0071 | clathrin-coated vesicle membrane | 20 | 1 (5%) | 1/20 (5%) | 0/1 (0%) | 1/19 (5%) |
| SL-0258 | synapse | 18 | 12 (67%) | 1/18 (6%) | 1/12 (8%) | 0/6 (0%) |
| SL-0283 | dendrite | 18 | 4 (22%) | 1/18 (6%) | 0/4 (0%) | 1/14 (7%) |
| SL-0161 | melanosome | 18 | 0 (0%) | 0/18 (0%) | n/a | 0/18 (0%) |
| SL-0138 | cell cortex | 17 | 6 (35%) | 1/17 (6%) | 1/6 (17%) | 0/11 (0%) |
| SL-0279 | axon | 17 | 6 (35%) | 0/17 (0%) | 0/6 (0%) | 0/11 (0%) |
| SL-0147 | endomembrane system | 16 | 7 (44%) | 4/16 (25%) | 2/7 (29%) | 2/9 (22%) |
| SL-0170 | mitochondrial matrix | 16 | 1 (6%) | 1/16 (6%) | 0/1 (0%) | 1/15 (7%) |
| SL-0066 | cilium | 15 | 10 (67%) | 4/15 (27%) | 1/10 (10%) | 3/5 (60%) |
| SL-0182 | nuclear membrane | 14 | 1 (7%) | 0/14 (0%) | 0/1 (0%) | 0/13 (0%) |
| SL-0188 | nucleolus | 14 | 0 (0%) | 1/14 (7%) | n/a | 1/14 (7%) |
| SL-0448 | spindle pole | 14 | 3 (21%) | 0/14 (0%) | 0/3 (0%) | 0/11 (0%) |
| SL-0171 | mitochondrial membrane | 14 | 9 (64%) | 5/14 (36%) | 3/9 (33%) | 2/5 (40%) |
| SL-0089 | cytoplasmic vesicle membrane | 14 | 6 (43%) | 0/14 (0%) | 0/6 (0%) | 0/8 (0%) |
| SL-0190 | nucleoplasm | 12 | 3 (25%) | 1/12 (8%) | 0/3 (0%) | 1/9 (11%) |
| SL-0260 | synaptic vesicle membrane | 12 | 2 (17%) | 0/12 (0%) | 0/2 (0%) | 0/10 (0%) |
| SL-0049 | chloroplast | 11 | 1 (9%) | 1/11 (9%) | 0/1 (0%) | 1/10 (10%) |
| SL-0100 | endosome membrane | 11 | 5 (45%) | 1/11 (9%) | 1/5 (20%) | 0/6 (0%) |
| SL-0038 | anchoring junction | 11 | 7 (64%) | 1/11 (9%) | 1/7 (14%) | 0/4 (0%) |
| SL-0136 | Golgi cisterna membrane | 11 | 0 (0%) | 0/11 (0%) | n/a | 0/11 (0%) |
| SL-0197 | perikaryon | 11 | 0 (0%) | 0/11 (0%) | n/a | 0/11 (0%) |
| SL-0173 | mitochondrion | 11 | 4 (36%) | 1/11 (9%) | 0/4 (0%) | 1/7 (14%) |
| SL-0023 | autophagosome | 11 | 1 (9%) | 1/11 (9%) | 0/1 (0%) | 1/10 (10%) |
| SL-0205 | phagocytic vesicle membrane | 10 | 1 (10%) | 0/10 (0%) | 0/1 (0%) | 0/9 (0%) |
| SL-0158 | lysosome | 10 | 5 (50%) | 0/10 (0%) | 0/5 (0%) | 0/5 (0%) |
| SL-0271 | vacuolar membrane | 10 | 4 (40%) | 0/10 (0%) | 0/4 (0%) | 0/6 (0%) |
| SL-0101 | endosome | 10 | 7 (70%) | 1/10 (10%) | 1/7 (14%) | 0/3 (0%) |
