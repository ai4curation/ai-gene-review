---
title: "IMPC Knockouts and Gene Function"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, EVALUATION]
species: [mouse]
index_group: CROSS_CUTTING
description: "Do standardized mouse knockout phenotypes reveal molecular and cellular function, or organism-level phenotypes only?"
---

# IMPC Knockouts and Gene Function

**Bottom line:** the International Mouse Phenotyping Consortium (IMPC)
knockout screen tells you that a gene matters and roughly where in the body,
not what its product does. Of 67,350 significant phenotype calls on 8,429 genes,
none is defined on a GO molecular function. The 5,238 calls defined on a cell
type (8%) are, with three exceptions, counts and indices of circulating or
lymphoid blood cells. Everything else is anatomy, organ physiology, a
circulating analyte, behaviour or survival. That is a property of the pipeline,
not of knockouts: no IMPC procedure measures an activity, a subcellular location
or a transcript, so no IMPC call can, on its own, license a molecular-function
term. Where knockouts do say something about molecular and cellular function in
this corpus, it comes from follow-up papers using the allele, curated as IMP,
and our reviewers keep those rows but mostly as non-core (66% of 2,287 mouse
IMP rows, against 29% for IDA). The companion question, whether the knockouts
illuminate disease mechanism, is answered on the dismech side
([dismech `projects/IMPC.md`](https://github.com/monarch-initiative/dismech/blob/main/projects/IMPC.md)).

## Questions

1. Can mouse knockouts elucidate gene function, and in particular cellular and
   molecular function, or do they mostly report organism-level phenotypes?
2. (dismech) Can the knockouts elucidate mechanisms of disease, Mendelian or
   otherwise? See the companion page linked above.

This page answers question 1 in two parts: what the IMPC screen itself measures,
and how knockout-derived evidence reaches GO and fares in review.

## What the IMPC screen measures

Every significant IMPC call names an IMPReSS procedure and an MP term. We
classified each call two independent ways
([`IMPC/results/RESOLUTION.md`](IMPC/results/RESOLUTION.md)):

- **By procedure** (what was measured), through the hand-curated
  [`IMPC/procedure_readout_classes.yaml`](IMPC/procedure_readout_classes.yaml).
- **By the MP term's own OWL logical definition** (what the abnormal quality
  inheres in): a GO molecular function, a GO cellular component or cellular
  process, a CL cell type, a CHEBI/PR molecule, UBERON anatomy, a GO
  organ-level process, or NBO behaviour. A call takes the finest level its term
  supports.

IMPC data release fetched 2026-11-15 from the IMPC Solr API; MP release
2026-10-29; GO release 2026-07-26.

| Finest level in the MP logical definition | Calls | MP terms | Genes reaching it |
|---|---:|---:|---:|
| Molecular function (GO MF) | 0 | 0 | 0 |
| Cellular (CL, GO CC, cellular GO BP) | 5,238 | 89 | 2,030 |
| Circulating molecule (CHEBI, PR, a complex in blood) | 6,554 | 72 | 1,926 |
| Organ-level process (organismal GO BP) | 3,680 | 40 | 720 |
| Anatomy (UBERON) | 23,887 | 294 | 2,316 |
| Behaviour (NBO) | 8,766 | 47 | 491 |
| No logical definition | 19,224 | 270 | 946 |

| Procedure class | Calls | Genes |
|---|---:|---:|
| Gross morphology (pathology, dysmorphology, eye, X-ray, DEXA, weights) | 25,324 | 5,478 |
| Behaviour (open field, startle/PPI, light-dark, fear, SHIRPA) | 9,426 | 2,512 |
| Circulating analyte (clinical chemistry, insulin, urinalysis, Ig) | 6,980 | 3,056 |
| Survival and fertility | 6,956 | 3,380 |
| Cell population (haematology, flow immunophenotyping) | 6,892 | 2,319 |
| Embryo and placenta morphology | 5,725 | 718 |
| Organ physiology (ECG, echo, ABR, calorimetry, IPGTT, grip) | 4,478 | 2,154 |
| Tissue histology (MPATH process in a named organ) | 1,569 | 405 |

Three things stand out.

- **The vocabulary is small.** 67,350 calls use 812 MP terms. A standardised
  pipeline has to pre-register what it can find, so it can only report the
  phenotypes it was built to detect.
- **The cellular level is the blood.** 5,235 of the 5,238 cellular calls come
  from haematology and immunophenotyping (mean corpuscular volume, neutrophil
  count, platelet count). The histopathology calls are MPATH processes recorded
  per organ ("hyperplasia" in testis), which is tissue level.
- **The GO processes in MP definitions are organismal.** The 129 MP terms whose
  definitions name a GO term are dominated by prepulse inhibition, pigmentation,
  in utero embryonic development, neural tube closure and heart contraction. The
  closest IMPC comes to a cellular mechanism is coat colour: an abnormal
  pigmentation call is how melanosome-biogenesis genes (*Lyst*, *Myo5a*,
  *Rab27a*, the HPS genes) show up.

## How knockout evidence reaches GO

**IMPC calls do not enter GO.** No row of the MGI GO annotation file
(2026-05-21) cites IMPC; MGI loads IMPC data as MP annotations, a separate
product. Knockout evidence reaches GO only through curated papers, as IMP or
IGI, and in MGI's file 62% of IMP biological-process rows are qualified
`acts_upstream_of_or_within`, a qualifier that does not claim the product
takes part in the process. The qualifier does not separate knockouts from
direct assays as cleanly as one might expect: 50% of MGI's IDA process rows
carry it too ([`IMPC/results/GO_COVERAGE.md`](IMPC/results/GO_COVERAGE.md)).

**IMPC reaches many genes GO has no function for.** Of the 8,429 genes with a
significant call, 5,312 (63%) have no experimentally supported mouse molecular
function (bare protein binding excluded) and 3,325 (39%) have no experimental
mouse function or process at all. For those 3,325, the finest IMPC call is
cellular for 745 and anatomical, behavioural, systemic or undefined for the rest.
So IMPC is often the only functional observation on a gene, and it is an
organism-level observation.

Adding the human ortholog (IMPC's `human_gene_symbol`, matched to the human GO
annotation file, same experimental codes) lights up more than half of them:
1,926 of the 3,325 (58%) have an experimental human MF or BP, and 198 have no
human symbol in IMPC's gene table. That leaves 1,399 genes (17% of those with a
call) with no experimental function or process in either species; for 306 of
them the finest IMPC call is cellular. Counting molecular function alone, 2,733
genes (32%) have none in either species, against 5,312 for mouse alone.

**Reviewers keep knockout rows but rarely as core.** Across 228 mouse reviews
in this repository ([`IMPC/results/REVIEW_ACTIONS.md`](IMPC/results/REVIEW_ACTIONS.md)):

| Evidence | Rows | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE |
|---|---:|---:|---:|---:|---:|---:|
| IMP | 2,287 | 23% | 66% | 3% | 5% | 1% |
| IGI | 557 | 25% | 67% | 3% | 2% | 0% |
| IDA | 2,334 | 55% | 29% | 8% | 4% | 1% |

Knockout-derived annotations are almost never judged wrong (1% removed), but
two thirds are judged true and peripheral. That matches what
[ASSAY_TO_FUNCTION](ASSAY_TO_FUNCTION.md) found for phenotypic readouts
generally and [BEHAVIOR](BEHAVIOR.md) found for behaviour terms: the failure
mode of a phenotype is distance from the gene product, not error. These are
literature IMP rows, mostly from classical single-gene knockouts, not IMPC data.

## Follow-up analyses

### Human annotations for the dark genes

Covered in the dark-gene paragraph above; the numbers are in the "Human coverage
of the dark genes" section of
[`IMPC/results/GO_COVERAGE.md`](IMPC/results/GO_COVERAGE.md). Human GO file of
2026-05-21. A mouse gene counts as covered when any of the human symbols IMPC
maps it to carries the annotation, so the human figure is an upper bound where
IMPC lists several orthologs.

### Papers that use IMPC alleles

Europe PMC finds 1,396 non-preprint records whose text names an IMPC, KOMP or
EUCOMM allele designation (`tm1a(EUCOMM)`, `tm1b(KOMP)`, `tm1(KOMP)Vlcg`,
`em1(IMPC)` and nine more; searched in the methods, results, figure, table and
supplement fields as well as the default field, which misses most methods
text). After removing 7 consortium resource and screen papers, a fixed-seed
sample of 200 from the remaining 1,382 was classified by the finest readout it
reports, with the [ASSAY_TO_FUNCTION](ASSAY_TO_FUNCTION.md) readout catalogue:
molecular if a `proximity: molecular` class matches, cellular if only
phenotypic (cell-level) classes match, organism-only otherwise
([`IMPC/results/ALLELE_FOLLOWUP.md`](IMPC/results/ALLELE_FOLLOWUP.md)).

| Finest readout | Abstract (198 papers) | Full text (182 papers) |
|---|---:|---:|
| Molecular | 8 (4%) | 95 (52%) |
| Cellular | 18 (9%) | 51 (28%) |
| Organism only | 172 (87%) | 36 (20%) |

- **The abstracts look organism-level; the papers are not.** 85% of abstracts
  match no catalogue readout at all, while 76 papers whose abstract reads as
  organism-only report a molecular assay in the full text and 44 a cellular one.
  The catalogue's patterns are probe and instrument names, which live in methods.
- **The full-text figure is an upper bound.** A match anywhere in the article
  counts, including the introduction and discussion, and the commonest molecular
  match, "electrophysiolog", also covers whole-animal recordings. Three
  catalogue patterns that mean something else in these papers (haematopoietic
  "reconstitution", ".edu" addresses read as EdU, and FLP "flippase") are
  dropped; every kept match is listed in
  [`allele_followup_matches.tsv`](IMPC/results/allele_followup_matches.tsv).
- **Reading:** about half of the papers that use an IMPC allele report at least
  one molecular-level assay somewhere and four in five reach at least the
  cellular level. That is where knockout-derived molecular and cellular knowledge
  comes from, and none of it is in the IMPC phenotype data.

### IMP rows tied to IMPC in our reviews

There are none to spot-check
([`IMPC/results/IMPC_IMP_ROWS.md`](IMPC/results/IMPC_IMP_ROWS.md)). No IMP or
IGI row in any review in this repository cites one of the IMPC consortium or
centre-screen papers (the eight on this page plus the Sanger Mouse Genetics
Project screen, PMID:23870131), and no cached publication cited by such a row has
a title naming IMPC or high-throughput phenotyping. The absence is upstream: in
MGI's whole GO file only 4 IMP rows cite any of these papers, all to PMID:23870131,
all biological process with `acts_upstream_of_or_within` (*Cbx7*, *Git2*,
*Fam107b*, *Trmt10a*), and none of the four genes has a review here. The one
review that uses IMPC data in its reasoning, `human/ARHGAP4`, uses it the other
way round: the knockout's zero significant calls across 413 tests is cited as a
tested absence of phenotype when downgrading process rows. The rubric line now in
the `annotation-reviewer` skill states the page's conclusion: a high-throughput
knockout result supports at most an organism-level process row, usually
`KEEP_AS_NON_CORE`, and never a molecular-function or `core_functions` claim
without a separate assay.

### Lethality and cell essentiality

The DepMap portal's download API did not return its file listing (it answered
with a browser-verification page and then HTTP 403). The comparison uses the
same files from the DepMap team's own deposit of the 24Q4 public release on
figshare (doi:10.25452/figshare.plus.27993248.v1, MD5-checked), which is older
than the portal's current release. No other essential-gene list was used
([`IMPC/results/ESSENTIALITY.md`](IMPC/results/ESSENTIALITY.md)).

| IMPC call (genes with a human symbol) | Genes | DepMap common essential |
|---|---:|---:|
| Preweaning, embryonic or prenatal lethality | 2,996 | 665 (22%) |
| Phenotyped, no lethality call | 6,549 | 122 (2%) |

- **Most lethal knockouts are developmental-only.** 2,331 of 2,996 lethal genes
  (78%) are not common-essential in human cancer cell lines, so the lethality
  reflects a requirement of the embryo or the animal, not of every cell. For
  these the call says nothing at the cell level.
- **Common essentials are lethal, as expected.** Of 787 phenotyped genes whose
  human ortholog is common-essential, 665 (84%) have a lethality call; the earlier
  the lethality, the higher the share (59% of genes lethal before organogenesis
  against 3% for incomplete-penetrance preweaning lethality).
- **So lethality has a cell-level reading for about a fifth of genes**, and only
  in combination with a cell-line screen. "No lethality call" includes genes
  whose viability was not assessed as well as viable lines.

## Answer to question 1, as far as it goes

- **Molecular function: no, by design.** A knockout removes the product and
  observes a consequence; it cannot show which activity was lost. The IMPC
  pipeline has no assay that could, and none of its MP terms is defined on one.
- **Cellular function: occasionally, mostly in blood and pigment.** Where a
  procedure counts cells (haematology, flow cytometry) or a visible trait reports
  an organelle (coat colour for melanosomes), a knockout can point at a cellular
  process. These are also the places where the dismech analysis finds IMPC
  touching a disease's mechanism nodes.
- **What knockouts are good for here:** saying that a gene is required,
  roughly for what system, and at what stage (lethality, embryo screens); and
  nominating dark genes for mechanistic follow-up. In a review, an IMPC result
  supports at most an organism-level process row, usually `KEEP_AS_NON_CORE`,
  and never a molecular-function or `core_functions` claim without a separate
  assay.
- **Follow-up work with the alleles is where molecular knowledge comes from.**
  In a sample of 200 papers that use IMPC/KOMP/EUCOMM alleles, about half report
  a molecular assay in the full text and four in five reach at least a cellular
  readout, though only 13% of abstracts show it. Those results reach GO as
  ordinary curated IMP or IDA rows, not as IMPC data.

## Plan

- [x] Fetch IMPC significant calls and gene table; classify by procedure and by
      MP logical definition.
- [x] Measure GO coverage of IMPC-phenotyped genes and how MGI qualifies
      knockout-derived annotations.
- [x] Tabulate reviewer actions on mouse IMP/IGI rows against IDA.
- [x] Follow-up use of alleles: sample papers citing IMPC/KOMP alleles and
      classify whether they report molecular or cellular readouts.
- [x] Count human experimental support for the 3,325 genes with no experimental
      mouse annotation, so the dark-gene figure covers both species.
- [x] Spot-check reviews whose IMP rows cite an IMPC-centre paper, and write a
      short rubric line for IMPC-derived claims in `annotation-reviewer`.
- [x] Look at the embryo and lethality screens separately: essentiality is the
      one organism-level IMPC readout with a clear cell-level reading (cell
      viability, proliferation) when combined with human cell-line screens.

## Reproduce

Raw data are cached under the git-ignored `.cache/impc/`; only scripts and
derived summaries are committed.

```bash
uv run python projects/IMPC/fetch_impc.py
curl -sSL -o .cache/impc/mp.owl https://purl.obolibrary.org/obo/mp.owl
curl -sSL -o .cache/impc/go-basic.obo https://purl.obolibrary.org/obo/go/go-basic.obo
curl -sSL -o .cache/impc/mgi.gaf.gz http://current.geneontology.org/annotations/mgi.gaf.gz
curl -sSL -o .cache/impc/goa_human.gaf.gz http://current.geneontology.org/annotations/goa_human.gaf.gz
uv run python projects/IMPC/mp_resolution.py
uv run python projects/IMPC/go_coverage.py
uv run python projects/IMPC/review_actions.py
uv run python projects/IMPC/impc_imp_rows.py
uv run python projects/IMPC/allele_followup.py   # Europe PMC + PMC; slow, caches under .cache/impc/europepmc/
uv run python projects/IMPC/essentiality.py      # DepMap; caches under .cache/impc/depmap/
```

## Key literature

Titles verified against PubMed; these are background, not quoted here.

- PMID:36305825 Groza T et al. 2023. The International Mouse Phenotyping
  Consortium: comprehensive knockout phenotyping underpinning the study of human
  disease.
- PMID:29626206 Brown SDM et al. 2018. High-throughput mouse phenomics for
  characterizing mammalian gene function.
- PMID:27626380 Dickinson ME et al. 2016. High-throughput discovery of novel
  developmental phenotypes.
- PMID:28650954 Karp NA et al. 2017. Prevalence of sexual dimorphism in
  mammalian phenotypic traits.
- PMID:29348434 Rozman J et al. 2018. Identification of genetic elements in
  metabolism by high-throughput mouse phenotyping.
- PMID:29026089 Bowl MR et al. 2017. A large scale hearing loss screen reveals
  an extensive unexplored genetic landscape for auditory dysfunction.

## Related projects

- [BEHAVIOR](BEHAVIOR.md), which ingested the IMPReSS behavioural procedures
  and maps each to the GO behaviour terms it can support.
- [ASSAY_TO_FUNCTION](ASSAY_TO_FUNCTION.md), on which readouts license a
  molecular-function term.
- [MOUSE_GENES_RE_REVIEW](MOUSE_GENES_RE_REVIEW.md).
