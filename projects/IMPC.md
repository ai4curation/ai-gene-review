---
title: "IMPC Knockouts and Gene Function"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, EVALUATION]
species: [mouse]
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
organism-level observation. This counts mouse annotations only; a human
ortholog's experimental annotation would reach the mouse gene as ISO, which we
did not count as experimental.

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
- **What we did not measure:** how much molecular and cellular knowledge comes
  from follow-up work with IMPC/KOMP alleles. That is probably the IMPC's
  largest contribution to gene function, and it is not visible in phenotype
  data.

## Plan

- [x] Fetch IMPC significant calls and gene table; classify by procedure and by
      MP logical definition.
- [x] Measure GO coverage of IMPC-phenotyped genes and how MGI qualifies
      knockout-derived annotations.
- [x] Tabulate reviewer actions on mouse IMP/IGI rows against IDA.
- [ ] Follow-up use of alleles: sample papers citing IMPC/KOMP alleles and
      classify whether they report molecular or cellular readouts.
- [ ] Count human ISO support for the 3,325 genes with no experimental mouse
      annotation, so the dark-gene figure covers both species.
- [ ] Spot-check reviews whose IMP rows cite an IMPC-centre paper, and write a
      short rubric line for IMPC-derived claims in `annotation-reviewer`.
- [ ] Look at the embryo and lethality screens separately: essentiality is the
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
uv run python projects/IMPC/mp_resolution.py
uv run python projects/IMPC/go_coverage.py
uv run python projects/IMPC/review_actions.py
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
