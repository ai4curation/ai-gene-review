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
  adding closure filtering would remove the signal being measured — but it means the 40%
  "downgraded or worse" figure mixes redundancy with error. The 9% hard-issue rate is the more
  conservative number.
- **The corpus is not a sample of GOA.** These 986 gene folders were selected for review for
  unrelated reasons. Rates here describe this corpus, not the pipeline at large.

## Reading the tables

- The **by GO term** and **by SL location** tables are near-duplicates by construction, since
  the mapping is close to one-to-one. Divergences between them are worth a look: they mean one
  GO term is reached from more than one SL location, or vice versa.
- "Issues" counts `REMOVE`, `MARK_AS_OVER_ANNOTATED`, and `MODIFY`. `KEEP_AS_NON_CORE` is
  excluded — it is a judgment that the location is real but peripheral, which is a different
  claim from the annotation being wrong.
- Rows below 10 reviewed annotations are omitted. `SL-0221`, the subject of the first
  subproject, falls below that threshold in this corpus (9 assertions) and is documented
  separately.

## SL names

Names are resolved live from `https://rest.uniprot.org/locations/SL-xxxx`. Pass `--offline`
to skip the lookup when running without network access.

## Corpus totals

- SL-unique annotations (sole source GO_REF:0000044): **1300**
- distinct gene folders: **986**
- reviewed SL-unique annotations: **1297**
- aspect: {'cellular_component': 1299, 'C': 1}
- actions: ACCEPT 760, KEEP_AS_NON_CORE 406, MODIFY 58, MARK_AS_OVER_ANNOTATED 43, REMOVE 15, UNDECIDED 9, PENDING 6
- downgraded or worse: **522/1297 (40%)**
- issue rate (REMOVE/MARK_AS_OVER_ANNOTATED/MODIFY): **116/1297 (9%)**

## By GO term (>= 10 reviewed)

| Term | Label | Reviewed | Issues | Rate |
|---|---|---|---|---|
| GO:0005737 | cytoplasm | 176 | 9 | 5% |
| GO:0005576 | extracellular region | 94 | 13 | 14% |
| GO:0005886 | plasma membrane | 83 | 9 | 11% |
| GO:0005634 | nucleus | 77 | 8 | 10% |
| GO:0016020 | membrane | 61 | 14 | 23% |
| GO:0005856 | cytoskeleton | 59 | 10 | 17% |
| GO:0005789 | endoplasmic reticulum membrane | 36 | 0 | 0% |
| GO:0005819 | spindle | 25 | 2 | 8% |
| GO:0005794 | Golgi apparatus | 23 | 4 | 17% |
| GO:0005783 | endoplasmic reticulum | 21 | 2 | 10% |
| GO:0000139 | Golgi membrane | 21 | 0 | 0% |
| GO:0005743 | mitochondrial inner membrane | 19 | 2 | 11% |
| GO:0031902 | late endosome membrane | 18 | 0 | 0% |
| GO:0030665 | clathrin-coated vesicle membrane | 18 | 0 | 0% |
| GO:0005694 | chromosome | 18 | 1 | 6% |
| GO:0042470 | melanosome | 17 | 1 | 6% |
| GO:0048471 | perinuclear region of cytoplasm | 17 | 0 | 0% |
| GO:0005813 | centrosome | 15 | 1 | 7% |
| GO:0005759 | mitochondrial matrix | 14 | 1 | 7% |
| GO:0042597 | periplasmic space | 14 | 0 | 0% |
| GO:0005730 | nucleolus | 13 | 1 | 8% |
| GO:0031966 | mitochondrial membrane | 13 | 4 | 31% |
| GO:0005829 | cytosol | 13 | 0 | 0% |
| GO:0005929 | cilium | 12 | 3 | 25% |
| GO:0030425 | dendrite | 12 | 0 | 0% |
| GO:0005776 | autophagosome | 11 | 1 | 9% |
| GO:0030672 | synaptic vesicle membrane | 11 | 0 | 0% |
| GO:0043204 | perikaryon | 11 | 0 | 0% |
| GO:0009507 | chloroplast | 11 | 2 | 18% |
| GO:0030424 | axon | 10 | 0 | 0% |
| GO:0005764 | lysosome | 10 | 0 | 0% |
| GO:0012505 | endomembrane system | 10 | 2 | 20% |
| GO:0031965 | nuclear membrane | 10 | 0 | 0% |

## By UniProt subcellular location (>= 10 reviewed)

| SL | Name | Reviewed | Issues | Rate |
|---|---|---|---|---|
| SL-0086 | Cytoplasm | 176 | 9 | 5% |
| SL-0243 | Secreted | 89 | 13 | 15% |
| SL-0191 | Nucleus | 77 | 8 | 10% |
| SL-0039 | Cell membrane | 74 | 7 | 9% |
| SL-0162 | Membrane | 61 | 14 | 23% |
| SL-0090 | Cytoskeleton | 59 | 10 | 17% |
| SL-0097 | Endoplasmic reticulum membrane | 36 | 0 | 0% |
| SL-0251 | Spindle | 25 | 2 | 8% |
| SL-0132 | Golgi apparatus | 23 | 4 | 17% |
| SL-0095 | Endoplasmic reticulum | 21 | 2 | 10% |
| SL-0134 | Golgi apparatus membrane | 21 | 0 | 0% |
| SL-0168 | Mitochondrion inner membrane | 19 | 2 | 11% |
| SL-0151 | Late endosome membrane | 18 | 0 | 0% |
| SL-0071 | Clathrin-coated vesicle membrane | 18 | 0 | 0% |
| SL-0468 | Chromosome | 18 | 1 | 6% |
| SL-0161 | Melanosome | 17 | 1 | 6% |
| SL-0198 | Perinuclear region | 17 | 0 | 0% |
| SL-0048 | Centrosome | 15 | 1 | 7% |
| SL-0170 | Mitochondrion matrix | 14 | 1 | 7% |
| SL-0200 | Periplasm | 14 | 0 | 0% |
| SL-0188 | Nucleolus | 13 | 1 | 8% |
| SL-0171 | Mitochondrion membrane | 13 | 4 | 31% |
| SL-0091 | Cytosol | 13 | 0 | 0% |
| SL-0066 | Cilium | 12 | 3 | 25% |
| SL-0283 | Dendrite | 12 | 0 | 0% |
| SL-0023 | Autophagosome | 11 | 1 | 9% |
| SL-0260 | Synaptic vesicle membrane | 11 | 0 | 0% |
| SL-0197 | Perikaryon | 11 | 0 | 0% |
| SL-0049 | Chloroplast | 11 | 2 | 18% |
| SL-0279 | Axon | 10 | 0 | 0% |
| SL-0158 | Lysosome | 10 | 0 | 0% |
| SL-0147 | Endomembrane system | 10 | 2 | 20% |
| SL-0182 | Nucleus membrane | 10 | 0 | 0% |


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
batches deliberately selected redundant annotations, which inflates the redundant group's issue
rate from 10% to 12%. The result quoted on the project page is the pre-batch measurement.

## Redundancy of SL-unique annotations

- SL-unique annotations examined: **1300**
- with a review action: **1297**
- of those, the gene already carries a more specific CC term from another source: **445/1297 (34%)**

### Issue rate, split by redundancy

| Group | n | Issue rate | KEEP_AS_NON_CORE |
|---|---|---|---|
| Redundant (more specific term present) | 445 | 54/445 (12%) | 137 (31%) |
| Not redundant (SL term is the most specific) | 852 | 71/852 (8%) | 269 (32%) |

### By SL location (>= 10 reviewed)

| SL | GO term | n | Redundant | Issue rate | Issue rate if redundant | if not |
|---|---|---|---|---|---|---|
| SL-0086 | cytoplasm | 176 | 116 (66%) | 9/176 (5%) | 4/116 (3%) | 5/60 (8%) |
| SL-0243 | extracellular region | 89 | 13 (15%) | 13/89 (15%) | 1/13 (8%) | 12/76 (16%) |
| SL-0191 | nucleus | 77 | 32 (42%) | 8/77 (10%) | 2/32 (6%) | 6/45 (13%) |
| SL-0039 | plasma membrane | 74 | 12 (16%) | 7/74 (9%) | 0/12 (0%) | 7/62 (11%) |
| SL-0162 | membrane | 61 | 34 (56%) | 17/61 (28%) | 12/34 (35%) | 5/27 (19%) |
| SL-0090 | cytoskeleton | 59 | 47 (80%) | 16/59 (27%) | 14/47 (30%) | 2/12 (17%) |
| SL-0097 | endoplasmic reticulum membrane | 36 | 2 (6%) | 0/36 (0%) | 0/2 (0%) | 0/34 (0%) |
| SL-0251 | spindle | 25 | 22 (88%) | 2/25 (8%) | 2/22 (9%) | 0/3 (0%) |
| SL-0132 | Golgi apparatus | 23 | 13 (57%) | 4/23 (17%) | 2/13 (15%) | 2/10 (20%) |
| SL-0134 | Golgi membrane | 21 | 0 (0%) | 0/21 (0%) | n/a | 0/21 (0%) |
| SL-0095 | endoplasmic reticulum | 21 | 4 (19%) | 2/21 (10%) | 0/4 (0%) | 2/17 (12%) |
| SL-0168 | mitochondrial inner membrane | 19 | 4 (21%) | 2/19 (11%) | 1/4 (25%) | 1/15 (7%) |
| SL-0468 | chromosome | 18 | 15 (83%) | 1/18 (6%) | 1/15 (7%) | 0/3 (0%) |
| SL-0071 | clathrin-coated vesicle membrane | 18 | 0 (0%) | 0/18 (0%) | n/a | 0/18 (0%) |
| SL-0151 | late endosome membrane | 18 | 7 (39%) | 0/18 (0%) | 0/7 (0%) | 0/11 (0%) |
| SL-0198 | perinuclear region of cytoplasm | 17 | 0 (0%) | 0/17 (0%) | n/a | 0/17 (0%) |
| SL-0161 | melanosome | 17 | 0 (0%) | 1/17 (6%) | n/a | 1/17 (6%) |
| SL-0048 | centrosome | 15 | 3 (20%) | 1/15 (7%) | 0/3 (0%) | 1/12 (8%) |
| SL-0200 | periplasmic space | 14 | 3 (21%) | 0/14 (0%) | 0/3 (0%) | 0/11 (0%) |
| SL-0170 | mitochondrial matrix | 14 | 1 (7%) | 1/14 (7%) | 0/1 (0%) | 1/13 (8%) |
| SL-0091 | cytosol | 13 | 0 (0%) | 0/13 (0%) | n/a | 0/13 (0%) |
| SL-0188 | nucleolus | 13 | 0 (0%) | 1/13 (8%) | n/a | 1/13 (8%) |
| SL-0171 | mitochondrial membrane | 13 | 9 (69%) | 4/13 (31%) | 3/9 (33%) | 1/4 (25%) |
| SL-0066 | cilium | 12 | 8 (67%) | 3/12 (25%) | 2/8 (25%) | 1/4 (25%) |
| SL-0283 | dendrite | 12 | 2 (17%) | 0/12 (0%) | 0/2 (0%) | 0/10 (0%) |
| SL-0049 | chloroplast | 11 | 1 (9%) | 2/11 (18%) | 1/1 (100%) | 1/10 (10%) |
| SL-0197 | perikaryon | 11 | 0 (0%) | 0/11 (0%) | n/a | 0/11 (0%) |
| SL-0023 | autophagosome | 11 | 1 (9%) | 1/11 (9%) | 0/1 (0%) | 1/10 (10%) |
| SL-0260 | synaptic vesicle membrane | 11 | 2 (18%) | 0/11 (0%) | 0/2 (0%) | 0/9 (0%) |
| SL-0147 | endomembrane system | 10 | 4 (40%) | 2/10 (20%) | 1/4 (25%) | 1/6 (17%) |
| SL-0279 | axon | 10 | 4 (40%) | 0/10 (0%) | 0/4 (0%) | 0/6 (0%) |
| SL-0158 | lysosome | 10 | 5 (50%) | 0/10 (0%) | 0/5 (0%) | 0/5 (0%) |
| SL-0182 | nuclear membrane | 10 | 0 (0%) | 0/10 (0%) | n/a | 0/10 (0%) |
