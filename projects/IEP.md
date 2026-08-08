---
title: "Inferred from Expression Pattern (IEP) Evidence Code Review"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [rat, ARATH, human, worm, DICDI, ECOLI, ORYSJ, MEDTR, mouse, yeast, DROME]
genes:
  - Hmgcs2
  - Gsta4
  - Gstt1
  - Qdpr
  - Hsd11b2
  - Ckmt2
  - Pgam2
  - Ephx1
  - Gss
  - Gamt
  - Casp3
  - Hspa8
  - Mapk1
  - Tp53
  - App
  - Notch1
  - PIF3
  - CRY1
  - CRY2
  - CCA1
  - TOC1
  - SOC1
  - UVR8
  - SOS1
  - CBF1
  - HSP17.6A
  - CDK1
  - PGK1
  - CPT1A
  - ACADVL
  - FN3K
  - LGALS3
  - TOLLIP
  - ACTL8
  - RB1
  - BAG6
  - NFE2L2
  - ADAM10
  - APOE
  - HTT
  - Mir26a-1
  - Mir384
  - Mir30e
  - Mir100
  - Mir127
  - hsp-16.2
  - hsp-4
  - hsp-6
  - hsp-60
  - irg-1
  - irg-2
  - lys-1
  - skn-1
  - xbp-1
  - DnaK
  - DnaJ
  - arnF
  - cotB
  - ecmB
  - mhcA
  - acaA
  - NFP
  - EME1
  - THI22
---

# Inferred from Expression Pattern (IEP) Evidence Code Review

## Overview

IEP (Inferred from Expression Pattern, ECO:0000270) is the one experimental
evidence code whose underlying observation is not about the gene product's
behaviour at all. IDA watches the protein do something; IMP removes it and
watches what breaks; IPI catches it holding a partner. IEP watches the gene's
*own transcript or protein abundance* go up or down, and infers participation in
whatever process the experimenter was manipulating.

That extra inferential step is the whole subject of this project. The review
question for an IEP row is therefore not the question asked of a propagated
annotation:

> Is this gene product an **agent** in the annotated process, or is its
> abundance merely **modulated by** it?

The same question is what GO itself asks. The [GO best-practices
paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3706743/) (PMID:23842463) puts
the bar explicitly:

> "The 'response to' GO terms are intended to annotate gene products that are
> required for the response to occur and are a direct result of the organism's
> reaction to the stimuli... It is acceptable to not annotate from such
> expression studies since changes in expression of a gene product does not in
> itself indicate its contribution to the function or process."

The [GO wiki entry for IEP](https://wiki.geneontology.org/Inferred_from_Expression_Pattern_(IEP))
is blunter still — "Use this code with caution!" — and adds two operational
constraints that this project treats as testable: IEP is "usually used in
conjunction with **high level** GO terms in the Biological Process ontology",
and only *normal* expression counts (an overexpression or ectopic-expression
experiment is IDA or IMP territory, not IEP). A third constraint is a hard
validation rule: [GORULE:0000006](https://github.com/geneontology/go-site/blob/master/metadata/rules/gorule-0000006.md)
restricts IEP (and its high-throughput twin HEP) to the Biological Process
aspect.

### Relationship to the sibling evidence-code projects

This page is the third in a set, and the contrast between them is the point.

| Project | Where the defect lives | Review question |
|---|---|---|
| [SPKW](SPKW.md) | The **mapping layer** — a UniProt keyword is converted to a GO term by a rule that ignores the individual gene. | Is this keyword→term mapping valid for *this* gene? |
| [IBA](IBA_REVIEW.md) / [ISO](ISO.md) | The **transfer** — a sound source annotation is propagated to a target that has diverged. | Is the source sound, and is this term safe to move across this edge? |
| **IEP** (this page) | The **inference itself** — there is no mapping and no transfer, only the leap from a correlation in abundance to a claim of participation. | Is the gene an agent in this process, or a bystander whose expression happens to track it? |

Because there is no source annotation and no propagation edge to audit, the
`review.propagation_review` machinery that IBA and ISO reviews rely on only
partly fits IEP; see [Action items](#action-items).

## Corpus Snapshot

Three views. [`IEP/iep_corpus_survey.py`](IEP/iep_corpus_survey.py) (output:
[iep-corpus-survey.md](IEP/iep-corpus-survey.md)) produces two of them: the
**GOA view** counts rows in the repo's cached `*-goa.tsv` downloads, and the
**review view** counts annotations in `*-ai-review.yaml`, i.e. what reviewers
concluded. Neither is a sample of IEP, because a gene directory exists only
because somebody chose that gene for review.

[`IEP/iep_global_atlas.py`](IEP/iep_global_atlas.py) (output:
[iep-global-atlas.md](IEP/iep-global-atlas.md)) supplies the denominator: the
**complete** set of IEP annotations in UniProt-GOA, downloaded from QuickGO. IEP
is rare enough that no sampling is needed — there are only 25,401 of them.

| | Global (UniProt-GOA) | Repo GOA files | Coverage |
|---|---:|---:|---:|
| IEP annotations | 25,401 | 543 | 2.1% |
| Gene products with IEP | 10,618 | 207 | 1.9% |
| Distinct GO terms | 2,383 | 277 | 11.6% |
| Distinct references | 11,777 | 357 | 3.0% |

Within the repo, IEP is rare in the same way it is globally: 530 of 147,856
cached GOA rows (0.4%), roughly one IEP row per 40 IDA rows. 538 of those have
been reviewed, across 215 review files.

The reviewed sample is 2% of global IEP, so before drawing conclusions from it,
see [how representative it is](#is-the-reviewed-sample-representative). The short
answer: representative for the *term-type* stratifications this page's main
findings rest on, badly skewed by organism and annotation group.

### IEP is used to say one kind of thing

| GO branch (is_a + part_of closure) | Global rows | Global share | Repo share | Flagged in repo |
|---|---:|---:|---:|---:|
| response to stimulus (GO:0050896) | 17,099 | 67.3% | 70.1% | 16.7% |
| developmental process (GO:0032502) | 4,110 | 16.2% | 14.1% | **23.7%** |
| unclassified (obsolete/unresolvable) | 1,395 | 5.5% | 4.3% | 8.7% |
| cellular component | 1,147 | 4.5% | 2.6% | 0% |
| biological regulation (GO:0065007) | 1,060 | 4.2% | 6.1% | 15.2% |
| metabolic process / localization / MF | 590 | 2.3% | 2.6% | 7.1% |

Seven out of ten IEP annotations are a "response to X" term, both globally and in
the repo, which follows directly from the experiment type: expose an organism to
a stimulus, see which transcripts move. Globally the most frequent terms are
`response to xenobiotic stimulus` (512 rows), `response to cold` (387),
`response to bacterium` (384) and `response to abscisic acid` (379).

The flag rates in that table carry the first non-obvious finding: **the
developmental branch is the riskier one**. A "response to X" row is usually at
least *true* — the transcript really did move when the stimulus was applied. A
"X development" row inferred from a developmental time-course is more often a
genuine over-reach, because rising abundance as a tissue matures reflects
demand for the enzyme's product rather than an instructive role in building the
tissue.

### The disposition data: IEP is not wrong so much as peripheral

Reviewers flagged 16.7% of IEP rows (REMOVE + MARK_AS_OVER_ANNOTATED + MODIFY).
That is worse than the other experimental codes (IDA 6.7%, IMP 6.8%, IGI 6.4%)
but comparable to ISO (16.8%) and better than IEA (20.4%) — not, on its own, a
damning number.

The damning number is the other end of the distribution:

| Code | Reviewed rows | % ACCEPT | % whose term reaches `core_functions` |
|---|---:|---:|---:|
| TAS | 15,036 | 73.8% | 55.8% |
| IBA | 9,568 | 72.4% | 50.8% |
| IDA | 21,599 | 69.5% | 43.9% |
| IEA | 31,198 | 50.8% | 29.4% |
| IMP | 9,770 | 48.5% | 32.7% |
| IGI | 1,555 | 45.3% | 26.5% |
| ISO | 4,237 | 33.2% | 16.1% |
| **IEP** | **538** | **22.7%** | **10.0%** |
| IPI | 17,472 | 10.9% | 4.3% |

IEP has the lowest ACCEPT rate and the lowest core-function grounding rate of
any code surveyed except IPI — and IPI's position is a known artifact of
`protein binding` rather than a property of physical-interaction evidence. The
missing IEP mass went to `KEEP_AS_NON_CORE`, which absorbs **55.4%** of IEP
rows, the highest share of any code.

So the characteristic IEP annotation is not false. It is *true and peripheral*:
a real observation about how the gene is regulated, phrased as a claim about
what the gene does. That is a harder problem than outright error, because
nothing in the annotation is checkably wrong.

Two more measurements sharpen it:

- **72.1%** of IEP rows are the **sole** carrier of their GO term in the review
  — no other evidence code in the same gene supports that term. IEP is not
  mostly redundant confirmation of what IDA/IMP already say; it is mostly
  adding terms nothing else supports.
- IEP clusters heavily. The median IEP-carrying gene has **one** IEP row, but
  21 genes (10% of them) carry **43%** of all IEP rows. rat/Hmgcs2 alone has 33;
  rat/Hspa8 25; rat/Casp3 23; rat/Tp53 18. A gene that attracts stimulus-response
  papers accumulates a proportional cloud of IEP terms. Globally the same shape
  holds almost exactly: the 1,117 gene products with 5 or more IEP rows are 10.5%
  of IEP-carrying products and account for **42.3%** of all IEP annotations.

## Is the reviewed sample representative?

The reviewed corpus is 2.1% of global IEP and was assembled by gene-review
interest, not by sampling IEP. The
[global atlas](IEP/iep-global-atlas.md#sampling-bias-of-the-reviewed-corpus)
compares each stratum's repo share against its global share; a ratio of 1.00x
means proportional, above 1 over-sampled, below 1 under-sampled.

**Representative where it matters most for this page.** The stratifications the
main findings rest on come out close to proportional:

| Stratum | Global | Repo | Ratio |
|---|---:|---:|---:|
| `response to stimulus` branch | 67.3% | 69.4% | 1.03x |
| `developmental process` branch | 16.2% | 14.3% | 0.89x |
| `involved_in` qualifier | 75.3% | 73.2% | 0.97x |
| `acts_upstream_of_or_within` qualifier | 19.1% | 21.7% | 1.14x |
| biological_process aspect | 95.2% | 95.5% | 1.00x |
| Genes with ≥5 IEP rows, as share of IEP rows | 42.3% | 43% | 1.02x |

So "IEP is overwhelmingly a stimulus-response code", "the developmental branch is
the riskier one", and "IEP load concentrates in a few genes" are not artifacts of
which genes the repo happens to contain.

**Badly skewed by organism and annotation group.** Here the sample is a poor
picture of IEP:

| Stratum | Global | Repo | Ratio |
|---|---:|---:|---:|
| *Homo sapiens* | 3.7% | 16.8% | **4.58x** |
| *Dictyostelium discoideum* | 0.7% | 4.3% | **6.34x** |
| *Arabidopsis* / TAIR | 19.7% | 29.1% | 1.47x |
| *Rattus norvegicus* / RGD | 47.5% | 35.8% | 0.76x |
| *Mus musculus* | 8.0% | 2.6% | **0.33x** |
| MGI as annotation group | 3.4% | 0.2% | **0.05x** |
| *Drosophila* / FlyBase | 4.4% | 1.3% | **0.30x** |

Entirely absent from the repo: **AgBase** (785 rows), **ZFIN** (326),
**CollecTF** (211); *Gossypium hirsutum* (395), *Danio rerio* (335),
*Gallus gallus* (279), *M. tuberculosis* H37Rv (179).

The human over-sampling is expected — the repo is human-centric — and it is
benign for the term-type findings, because human IEP looks like everyone else's
IEP. The **MGI gap is not benign**, for a specific reason: the largest
single-screen IEP batches in all of GOA are MGI's (see
[pattern 3](#3-differential-expression-screen-batch-one-screen-one-term-n-genes)),
so the stratum the repo samples at 0.05x is precisely where the most extreme
instance of a pattern this page documents actually lives.

**A slice the repo under-samples but can represent.** 840 global IEP rows
(3.3%), on 437 gene products, are **RNAcentral** entries rather than proteins —
almost all microRNA precursors from miRNA-profiling studies. This is IEP in its
purest form: the only observation is that a non-coding RNA's abundance changed.
The `genes/` tree handles ncRNA entries natively (`id: URS…`, `product_type:
MIRNA`, fetched with `ai-gene-review fetch-ncrna`), so the gap was coverage, not
capability. Five of them are now reviewed — see
[the miRNA cohort](#cohort-review-130-mirnas-one-term-one-paper) below.

**Corrections this forces.** Two claims made from the repo sample alone need
restating:

1. *Aspect violations are not a curiosity.* The repo's 23 non-BP IEP rows looked
   like a rounding error. Globally there are **1,223** (4.5% CC, 0.3% MF) — and
   the repo sample was proportionally *accurate* (1.00x for BP, 0.84x for CC) all
   along. The mechanism proposed from 20 rows holds at scale: see
   [below](#gorule0000006-violations-are-an-eco-mapping-artifact).
2. *No GO term is majority-IEP.* Within a gene, 72% of IEP rows are the sole
   carrier of their term. But measured per term across the whole ontology, IEP is
   never the dominant support: the most IEP-dependent frequent term is
   `seed trichome elongation` at **19.6%** of its annotations, then
   `cellular response to leukemia inhibitory factor` (13.7%) and
   `response to ethanol` (13.4%); most sit below 2%. Both statements are true and
   they answer different questions — IEP is load-bearing *for the gene it sits
   on*, never *for the term it points at*.

## Failure Patterns

| Pattern | Description | Examples | Typical action |
|---|---|---|---|
| **Inducible bystander** | A constitutively-functioning enzyme is transcriptionally induced by many unrelated stimuli; each induction paper yields one `response to X` row. | rat/Gsta4, rat/Gstt1, rat/Qdpr, rat/Hsd11b2, rat/Gss | MARK_AS_OVER_ANNOTATED |
| **Developmental time-course → tissue term** | Abundance rises as a tissue matures; curated as involvement in building that tissue. | rat/Ckmt2, rat/Ephx1, rat/Qdpr, rat/Hmgcs2, rat/Gamt, rat/Pgam2 | MARK_AS_OVER_ANNOTATED |
| **Differential-expression screen batch** | One screen generates one term across many unrelated genes. | PMID:21492153 → 8 genes, all `epithelial cell differentiation`; globally up to 291 genes from one paper | MARK_AS_OVER_ANNOTATED / REMOVE |
| **Promiscuous hub inversion** | A signalling hub whose own transcript answers every stimulus collects the whole stimulus catalogue — while its actual role is to *drive* those responses. | ARATH/PIF3 (7 rows, one paper), ARATH/CRY1, ARATH/CRY2 | MARK_AS_OVER_ANNOTATED / MODIFY |
| **Regulon membership ≠ function** | Being a transcriptional target of a stimulus-responsive regulator is a property of the promoter, not of the protein. | ECOLI/arnF, yeast/THI22 | MARK_AS_OVER_ANNOTATED |
| **Marker-gene circularity** | A cell-type marker's expression is *definitionally* correlated with the stage it marks. | DICDI/cotB, DICDI/mhcA | MARK_AS_OVER_ANNOTATED |
| **Over-specific stimulus term** | The opposite of GO's "use high-level terms" advice: a hyper-specific stimulus term from a single exposure experiment. | ARATH/PIF3 `response to water-immersion restraint stress`, DICDI/acaA `response to imidacloprid` | MODIFY / MARK_AS_OVER_ANNOTATED |
| **Aspect violation** | CC or MF terms carrying IEP, contrary to GORULE:0000006. | 1,223 rows globally, 91% of the CC ones from one ECO class | see [below](#gorule0000006-violations-are-an-eco-mapping-artifact) |

### 1. Inducible bystander — the "response to X" cloud

The largest and most systematic class. A detoxification or intermediary
metabolic enzyme has one stable job; because that job is useful under stress,
its transcript is induced by a long list of chemically unrelated insults; and
because each induction was published separately, each becomes an annotation.

rat/Gstt1 carries `response to salicylic acid`, `response to selenium ion`,
`response to vitamin E` and `response to xenobiotic stimulus` — four separate
PMIDs, one enzyme, one activity. rat/Qdpr, whose actual job is quinonoid
dihydrobiopterin reduction in tetrahydrobiopterin recycling, carries `response
to aluminum ion`, `response to lead ion`, `response to glucagon`, `cellular
response to xenobiotic stimulus` and `liver development`. rat/Hsd11b2 has six
flagged stimulus terms.

What makes these hard is that they are not false. GSTT1 activity *is* part of
how a cell handles a xenobiotic. The problem is proportion: the annotation set
implies a stimulus-specialist when the biology is one broad-specificity
transferase. GO's own criterion — "required for the response to occur" — is the
right discriminator, and it is exactly the question the induction experiment
does not answer.

A sharp variant is the **co-exposure artifact**. rat/Gsta4's `response to zinc
ion` and `response to herbicide` come from the *same* zinc/paraquat co-exposure
experiment (PMID:20553223); the reviewer noted there is "no mechanistic evidence
that zinc directly modulates GSTA4-4". A factorial exposure design yields one
term per factor regardless of which factor drove the induction.

### 2. Developmental time-course → tissue-development term

rat/Ckmt2 is the cleanest instance. Sarcomeric mitochondrial creatine kinase
mRNA is undetectable in prenatal heart and rises sharply after birth
(PMID:8086475), so it carries `heart development` and `skeletal muscle tissue
development`. As the review puts it, that profile "reflects the maturing heart's
increasing metabolic demand for phosphocreatine buffering, not a direct
instructive role of Ckmt2 in heart morphogenesis."

The same shape recurs: rat/Ephx1 and rat/Qdpr → `liver development`, rat/Gamt →
`embryonic liver development`, rat/Hmgcs2 → `lung development` and `adipose
tissue development`, rat/Pgam2 → `spermatogenesis`. In every case the protein is
a metabolic enzyme whose product the maturing tissue needs more of. The tissue
builds the enzyme; the enzyme does not build the tissue.

This is why the developmental branch flags at 23.7% versus 15.1% for
stimulus-response: a metabolic enzyme genuinely *participates in* a stress
response in a way it does not *participate in* organogenesis.

### 3. Differential-expression screen batch: one screen, one term, N genes

PMID:21492153 is a 2-D gel proteomics comparison of proliferating versus
differentiated Caco-2 intestinal cells. It reports "53 proteins that were
differently regulated during the differentiation process", 34 of them identified
by MALDI-TOF, and those identifications were curated `involved_in`
`GO:0030855 epithelial cell differentiation` with IEP. In
this corpus that single paper is the source for eight genes:
human/ACADVL, human/ACTL8, human/CDK1, human/CPT1A, human/FN3K, human/LGALS3,
human/PGK1 and human/TOLLIP — a very-long-chain acyl-CoA dehydrogenase, a
cyclin-dependent kinase, a glycolytic kinase, a fructosamine kinase, a galectin
and a TLR adaptor. Six of the eight were flagged (five MARK_AS_OVER_ANNOTATED,
human/FN3K REMOVE); the other two, human/LGALS3 and human/TOLLIP, were kept as
non-core with reviewers noting the evidence is "correlative expression-pattern"
and the process "secondary" to the protein's actual role.

human/CDK1 is the case that exposes the underlying logic error. The review notes
that CDK1 "promotes proliferation, which decreases during differentiation" —
CDK1's abundance is *anti*-correlated with its causal contribution. The paper
itself says as much: "proteins associated with proliferation, cell growth and
cancer were downregulated, reflecting the loss of the tumorigenic phenotype of
the cells." An abundance change carries no sign information about the direction
of the causal role, so "changed during process X" and "promotes process X" are
simply different claims — and here the annotation was made from a change in the
wrong direction.

This pattern is the IEP analogue of the SPKW mapping layer: a single upstream
decision (here, "annotate every hit in this screen") propagates a term across a
functionally unrelated gene set, and the resulting annotations look independent
because they sit on different genes.

**At global scale this is the dominant shape of IEP, and eight genes was a small
example.** The distribution of IEP over references is sharply bimodal: 62.4% of
the 11,777 references behind global IEP contribute exactly *one* annotation,
while the top ten contribute 1,130 between them. Every one of the six largest is
a single screen annotated to a single term:

| Reference | IEP rows | Gene products | Terms | The one term | Group |
|---|---:|---:|---:|---|---|
| PMID:20439489 — miRNA 34a/100/137 modulate mouse ESC differentiation | 291 | 291 | 1 | `cellular response to leukemia inhibitory factor` | MGI |
| PMID:23012479 — Impact of lactobacilli on orally acquired listeriosis | 153 | 153 | 1 | `response to bacterium` | MGI |
| PMID:11967071 — *Over 1000 genes are involved in the DNA damage response of E. coli* | 152 | 152 | 1 | `DNA damage response` | EcoliWiki |
| PMID:25858512 — miR-26a/miR-384-5p required for LTP maintenance | 130 | 130 | 1 | `long-term synaptic potentiation` | MGI |
| PMID:23646144 — miRNAs in organ-of-Corti degeneration in age-related hearing loss | 100 | 100 | 1 | `sensory perception of sound` | MGI |
| PMID:11486054 — Patterns of gene expression during *Drosophila* mesoderm development | 72 | 72 | 1 | `mesoderm development` | FlyBase |

Three of those are miRNA-profiling studies annotating differentially expressed
miRNA precursors, so "changed abundance" is the *entire* observation. And
PMID:11967071 is the clearest single case in all of IEP: a genome-wide *E. coli*
DNA-damage transcriptome, whose own title concedes that "over 1000 genes are
involved", yielding `DNA damage response` for 152 genes including the maltoporin
`lamB`, the maltose transport subunit `malF`, fumarate reductase `frdA`,
D-serine deaminase `dsdA` and asparagine synthetase `asnA`. Those are not DNA
repair proteins; they are genes whose transcripts moved. This is
[pattern 5](#5-regulon-membership-is-a-property-of-the-promoter) executed 152
times from one experiment.

Two review consequences follow. A batch-sourced IEP row should be judged against
its cohort, not on its own, because the cohort reveals the annotation rule that
produced it. And because these batches are concentrated in MGI — the group the
repo samples at 0.05x — the reviewed corpus systematically under-represents the
most extreme form of the pattern.

#### Cohort review: 130 miRNAs, one term, one paper

PMID:25858512 is a natural experiment, because the paper itself sorts its miRNAs
into tiers. It detected **372** miRNAs in hippocampal slices, found that only
**12** changed during LTP, and functionally validated **three** — miR-26a,
miR-384-5p and let-7a — by electrophysiology, time-lapse spine imaging and 3'
UTR reporter assays. MGI annotated **130** miRNA precursors to
`long-term synaptic potentiation`. The paper's own abstract describes what the
rest amount to: "presents a catalogue of candidate 'LTP miRNAs'".

Five members were reviewed, one from each tier, so that the batch is tested with
an internal positive control rather than assumed to be wrong:

| Tier | miRNA | What the paper shows | Action |
|---|---|---|---|
| Validated | mouse/Mir26a-1 | Title miRNA; required for LTP maintenance and spine enlargement via RSK3 | ACCEPT |
| Validated | mouse/Mir384 | Title miRNA; same experiments | ACCEPT |
| Changed, untested | mouse/Mir30e | Named as one of the six downregulated among the 12 that changed | MARK_AS_OVER_ANNOTATED |
| Detected only | mouse/Mir100 | Not mentioned anywhere in the full text | REMOVE |
| Detected only | mouse/Mir127 | Not mentioned anywhere in the full text | REMOVE |

The tier predicts the verdict exactly. This matters because it separates two
claims that are easy to conflate: the batch is not wrong because it is a batch,
it is wrong for the members whose only qualification is having been detected.
mouse/Mir30e is the instructive middle case — its expression genuinely changed,
so IEP is the correct evidence code and the observation is sound; what fails is
the leap from "changed" to "acts upstream of or within".

The batch also has a defect visible only from the cohort: it **omits let-7a**,
one of the three miRNAs the paper establishes as required, while including 127
that it does not. The annotation set is not merely over-inclusive, it is
misaligned with the paper's conclusions at both ends.

Three further batch papers annotate these same five miRNAs, and two produced
sharper findings than the LTP batch itself:

- **A source that refutes its own annotation.** mouse/Mir26a-1 carries
  `response to bacterium` from PMID:24205035, a circulating-miRNA survey in a
  cecal-ligation-and-puncture sepsis model. The authors asked whether bacterial
  sensing drives the increase and concluded it does not — it persists in *Tlr2*,
  *Tlr4* and *NF-kB* knockouts, indicating the change "was not directly mediated
  by the TLR2/NF-κB or TLR4/NF-κB pathway, and pathways induced by exposure to
  the gram-positive or gram-negative bacteria". The annotation asserts precisely
  what the cited paper tested and rejected, which is what makes it a REMOVE
  rather than an over-annotation. The companion `response to wounding` row
  describes the surgery used to perturb the animals.
- **The pattern inside a single paper.** PMID:20439489 supports both a validated
  IMP row on mouse/Mir100 (`positive regulation of stem cell differentiation`,
  via direct repression of Smarca5 — miR-100 is one of the paper's three title
  miRNAs) and an unvalidated IEP batch row (`cellular response to leukemia
  inhibitory factor`, one of 291). The same study, the same gene, one row
  recording what was demonstrated and one recording what was merely observed.
  The IEP term is also a poor description of the experiment, which induced
  differentiation by *withdrawing* LIF.
- **Wrong direction as well as wrong evidence.** mouse/Mir100's
  `sensory perception of sound` comes from an ageing survey (PMID:23646144)
  whose full text never mentions miR-100 and whose subject is *degeneration* of
  the organ of Corti during hearing loss, not normal hearing.

Across the 13 IEP rows in this cohort: 2 ACCEPT, 7 MARK_AS_OVER_ANNOTATED,
4 REMOVE — an 85% flag rate against 16.7% corpus-wide, and 4 REMOVEs added to a
corpus that previously held 7 in total. Targeting batch cohorts rather than
individual rows is therefore a high-yield review strategy, which is the practical
lesson for the remaining candidates.

### 4. Promiscuous hub inversion: the regulator annotated as a responder

ARATH/PIF3 carries seven IEP rows — `response to heat`, `response to cold`,
`response to ethylene`, `response to auxin`, `response to abscisic acid`,
`response to salt`, `response to water-immersion restraint stress` — six of them
from a single gene-family expression survey (PMID:23708772). All seven were
flagged.

PIF3 is a phytochrome-interacting transcription factor: it *runs* the light and
hormone response programmes. Its transcript answering every stimulus is what a
signalling hub's transcript does. Annotating the hub as a responder to each
stimulus inverts the regulator/target relationship and buries the actual
function, which the gene's IMP annotations already carry. The same inversion
underlies the MODIFY calls on ARATH/CRY1 and ARATH/CRY2, where the generic
`response to light stimulus` sits on the blue-light *photoreceptors* themselves.

The seventh PIF3 row also illustrates the over-specific-term pattern:
`response to water-immersion restraint stress` (GO:1990785) is a rodent
stress-model term applied to a plant submergence experiment. Granularity errors
run the other way too — ARATH/SOC1's IEP row on `positive regulation of
DNA-templated transcription` was MODIFYed to the Pol II-specific child.

### 5. Regulon membership is a property of the promoter

ECOLI/arnF is annotated `response to iron(III) ion` because the *arnBCADTEF*
operon is induced by iron through the BasS-BasR two-component system. The
review's verdict
is precise: "the IEP evidence code is technically appropriate... However,
annotating a gene to 'response to iron(III) ion' based solely on transcriptional
induction conflates regulation with function. ArnF is a flippase that
translocates undecaprenyl phosphate-alpha-L-Ara4N." The iron-responsiveness
belongs to the operon's promoter; the flippase does not sense or handle iron.
(This case also appears in the [IBA project](IBA_REVIEW.md#arnf-pthr30561-functional-divergence-within-smr-superfamily),
where the same gene's IBA rows are analysed.)

yeast/THI22 is the same shape with an extra twist: thiamine-dependent regulation
is real, but the paper that establishes the regulation (PMID:10383756) also
establishes that THI22 is *not required* for thiamine biosynthesis, so the
regulon membership points at a process the gene demonstrably does not carry out.

### 6. Marker-gene circularity in *Dictyostelium*

*Dictyostelium* development is staged, and stage-specific genes are used as
stage markers precisely because their expression tracks the stage. A
developmental transcriptome (PMID:25887420) supplies IEP rows for 17 genes here.

The circularity has to be judged case by case, and this corpus contains both
verdicts. DICDI/cotB is a prespore marker: the review flags
`slug development involved in sorocarp development` because "there is no
evidence that the SP70 protein participates causally in slug development... the
gene's core function lies in spore coat structure, not in the morphogenesis."
DICDI/mhcA gets the same treatment for `aggregation involved in sorocarp
development`. But DICDI/ecmB was **accepted as core** for `culmination involved
in sorocarp development` — ecmB is a prestalk extracellular-matrix protein, so
the late-development induction the transcriptome records is the production of
the material culmination consumes. The marker is the product.

### GORULE:0000006 violations are an ECO-mapping artifact

Globally **1,223 IEP annotations (4.8%)** sit on non-BP terms, violating the hard
validation rule: 1,147 cellular-component and 76 molecular-function. They are not
sloppy curation, and the diagnosis is worth recording because it is mechanical
and it accounts for nearly all of them.

"IEP" in a GAF is not one ECO class. Of the 25,401 rows, 23,747 (93.5%) are
literally `ECO:0000270`; the other 1,654 use a more specific descendant class
that collapses to IEP in the GAF projection. Splitting the aspect violations by
ECO class localises the problem almost perfectly:

| ECO class | IEP rows | BP | MF | CC |
|---|---:|---:|---:|---:|
| ECO:0000270 (expression pattern) | 23,747 | 23,691 | 36 | 20 |
| **ECO:0000279** (qualitative western immunoblotting) | 1,417 | 285 | 22 | **1,110** |
| all other descendant classes | 237 | 202 | 18 | 17 |

The generic parent class is 99.8% BP — essentially rule-compliant. One descendant
class, ECO:0000279, contributes **91% of every CC violation in GOA** while being
6% of IEP.

The repo's 23 examples are that global picture in miniature (its aspect mix is
proportional to global at 1.00x for BP and 0.84x for CC). Twenty are SynGO
cellular-component annotations (`postsynaptic density`,
`glutamatergic synapse`, `presynapse`, `presynaptic active zone`) on rat/Hspa8,
rat/Mapk1, mouse/Hspa8, mouse/Casp3, mouse/App, mouse/Notch1, human/APOE and
human/HTT. In the cached GOA rows these carry **ECO:0000279**, "qualitative
western immunoblotting evidence used in manual assertion" — the evidence class
for detecting a protein in a biochemically fractionated preparation such as a
synaptosome or PSD prep.

ECO:0000279 has **two** relevant ancestors: `ECO:0000270` (expression pattern
evidence used in manual assertion → IEP) and `ECO:0000314` (direct assay
evidence used in manual assertion → IDA). Collapsing the specific ECO class down
to a three-letter GAF code forces a choice between them, and the pipeline picks
IEP — dragging a localization assay into a BP-only code. GORULE:0000006 itself
names the correct resolution: "For CC annotations that assess the localization of
a gene product, IDA should be used." The remaining three violations are DisProt
molecular-function rows (human/NFE2L2 `ubiquitin protein ligase binding`,
human/BAG6 `molecular function activator activity`, human/ADAM10 `protein
homodimerization activity`); human/BAG6's was reviewed and REMOVEd.

The lesson generalises beyond IEP: where a specific ECO class is multiply
parented across GAF code boundaries, the GAF round-trip is lossy, and a
downstream hard rule then fires on an annotation whose *evidence* was never
actually expression-pattern evidence.

## Where IEP Is Legitimate

IEP is not a code to review adversarially. 22.7% of IEP rows were accepted and
49 of them ground a term in a gene's `core_functions`. The accepted cases share
a single property, and it is the discriminator this project turns on: **the
gene's job is the response itself**.

- **Inducible stress-response effectors.** For a heat-shock protein, induction
  by heat is not a correlate of the function — being made when the cell is hot
  *is* the function. worm/hsp-16.2, ECOLI/DnaK, ECOLI/DnaJ and ARATH/HSP17.6A
  all keep `response to heat`; worm/hsp-4 keeps `endoplasmic reticulum unfolded
  protein response` (four separate accepted rows); worm/hsp-6 and worm/hsp-60
  keep `mitochondrial unfolded protein response`. These are regulon *outputs*
  whose entire deployment is the stress programme.
- **Infection-inducible immune effectors.** worm/irg-1 and worm/irg-2 keep both
  `antibacterial innate immune response` and `defense response to Gram-negative
  bacterium`: strong, specific, replicated induction by *P. aeruginosa* is the
  defining property of an infection-response gene. worm/lys-1 is the same call
  with independent backing: the same paper that shows infection-inducible
  expression also shows that overexpression confers resistance.
- **Clock genes.** ARATH/CCA1 and ARATH/TOC1 keep `circadian rhythm`. Oscillating
  expression is not evidence about a clock component; it is the mechanism by
  which the oscillator works.
- **Corroboration inside a converging set.** ARATH/UVR8 (`response to UV-B`),
  ARATH/SOS1 (`response to salt stress`), ARATH/CBF1 (`cold acclimation`),
  MEDTR/NFP (`nodulation`), worm/skn-1 (`response to oxidative stress`) and
  worm/xbp-1 (`IRE1-mediated unfolded protein response`) all keep IEP rows that
  restate what IMP and IDA independently establish. Here IEP costs nothing and
  adds a line of evidence — the 27.9% of IEP rows that are *not* the sole carrier
  of their term.
- **Markers that are the differentiated product.** DICDI/ecmB, as above.

The contrast with the failure cases is not about evidence quality; the
induction experiments behind rat/Gstt1 are as sound as those behind worm/hsp-4.
It is about whether the gene product exists *for* the annotated process. A
heat-shock chaperone is deployed only during heat shock. A glutathione
transferase does the same chemistry whether or not the animal was dosed with
selenium.

## Reviewer Checklist

Before accepting or flagging an IEP row.

### Read the experiment, not just the term

- Identify what was measured (transcript or protein), by what method, and under
  what perturbation. Northern/microarray induction, a developmental time-course,
  and a differential-abundance proteomics screen fail in different ways.
- Check the paper is a **normal**-expression study. Overexpression and ectopic
  expression are IDA/IMP evidence, not IEP, per the GO wiki.
- Check whether one paper supplies IEP rows for many genes (a screen) or many
  terms for one gene (a stimulus cloud). Both are batch artifacts and neither is
  visible from a single annotation row.

### Ask the agency question

- Is the gene product **required for the annotated process to occur**, or does
  the process merely change its abundance? This is GO's own wording and it
  decides most cases.
- If the gene is a regulator, check for inversion: does it *drive* the response
  programme it is annotated as responding to (ARATH/PIF3)?
- If the gene is an enzyme, ask whether the annotated process needs *more of its
  normal product* (rat/Ckmt2 in maturing muscle) rather than a distinct
  activity.
- Check the sign. An abundance change carries no direction — human/CDK1 falls
  during the differentiation it is annotated to.
- Distinguish regulon membership from function: an iron-responsive promoter does
  not make an iron-responsive protein (ECOLI/arnF).

### Check the term and the aspect

- Verify the aspect is Biological Process (GORULE:0000006). If it is CC or MF,
  check the underlying ECO class before blaming the curator — the GAF collapse
  may have chosen the wrong parent.
- Check granularity in both directions. GO advises high-level terms for IEP;
  a hyper-specific stimulus term from one exposure experiment (`response to
  imidacloprid`) is over-reach, and the correct fix is usually MODIFY to the
  parent rather than REMOVE.
- Check whether the term already has non-IEP support in the same gene. If it
  does, the IEP row is cheap corroboration; if it does not (72% of rows), the
  IEP row is load-bearing and deserves the full agency question.

### Prefer the right action

- `KEEP_AS_NON_CORE` is the correct default for a sound induction observation
  that is not the gene's job. It is already the modal IEP outcome and should
  stay that way.
- `MARK_AS_OVER_ANNOTATED` fits when the observation is real but the term
  overstates the role — the inducible-bystander and developmental cases.
- `REMOVE` should be reserved for a categorical mismatch, where the process is
  not merely peripheral but belongs to a different functional class entirely
  (human/RB1 `Ras protein signal transduction`, human/FN3K `epithelial cell
  differentiation`). Only 11 of 538 rows met that bar, four of them added by the
  miRNA cohort below.
- Do not REMOVE an IEP row merely because the evidence code is weak. The
  induction happened; what is at issue is the term, not the experiment.

## Recommendations

**For reviewers.** Treat an IEP row as a statement about *regulation* and ask
whether it has been mis-phrased as a statement about *function*. The most common
correct answer is "true, keep it, but it is not what this gene is for."

**For curators and GO.**

1. **Batch-annotating a screen deserves a second look.** The signature is
   mechanical and cheap to detect: one reference, one GO term, many gene products.
   Globally the top six such references produce 72–291 annotations each, and
   `reference × term × gene-product-count` would flag every one of them at
   submission time rather than at review time. PMID:11967071 is the case for
   doing so — a paper titled "Over 1000 genes are involved in the DNA damage
   response of *E. coli*" should not yield `DNA damage response` for a maltoporin.
2. **Cap stimulus clouds.** When a gene accumulates many `response to X` terms
   from independent exposure papers and has a single well-characterised
   activity, the informative annotation is the parent term once, not the
   catalogue. rat/Gstt1's four sibling stimulus terms say less together than
   `response to xenobiotic stimulus` alone.
3. **Developmental time-courses need a higher bar than stimulus responses.**
   The 23.7% versus 15.1% flag-rate gap is consistent and mechanistic: metabolic
   demand tracks tissue maturation without any instructive role.
4. **Fix the ECO→GAF collapse rather than the annotations.** The GORULE:0000006
   violations come from a multiply-parented ECO class (ECO:0000279) whose GAF
   projection picks IEP over the equally valid IDA. Choosing the parent by the
   annotation's *aspect* would clear **1,110 of the 1,147** CC violations in GOA
   in one change, with no curation effort at all.
5. **`response to` terms could carry the requirement explicitly.** GO's
   best-practice text says these terms are for products "required for the
   response to occur", but nothing in the term definitions or the evidence code
   enforces it. An annotation-extension or qualifier distinguishing "acts in the
   response" from "is induced during the response" would let the two claims
   coexist instead of competing.

## Action Items

- [x] Build a reproducible two-view IEP survey (GOA rows + reviewed rows) with
      an evidence-code baseline rather than IEP in isolation.
- [x] Quantify the ACCEPT / core-function-grounding gap that distinguishes IEP
      from the other experimental codes.
- [x] Catalogue the failure patterns against reviewed examples.
- [x] Diagnose the GORULE:0000006 aspect violations.
- [x] Establish the global denominator (all 25,401 IEP annotations) and measure
      the reviewed sample's bias against it, so page claims can be marked as
      sample-robust or sample-dependent.
- [ ] Review the remaining 22 `PENDING` IEP rows, all on rat/Casp3 — the largest
      single unreviewed block already in the repo.
- [x] Review a batch cohort rather than another single gene, sampling tiers
      within the cohort so the batch is tested rather than assumed. Done for
      PMID:25858512 — see
      [the miRNA cohort](#cohort-review-130-mirnas-one-term-one-paper).
- [ ] Do the same for **PMID:11967071** (152 *E. coli* genes → `DNA damage
      response`), the cleanest test of the regulon-membership pattern, in an
      organism this repo already covers well. The tiering is available there too:
      the paper distinguishes SOS-regulon members from the wider induced set.
- [ ] Continue closing the MGI gap (still sampled well below its 3.4% global
      share). `cellular response to leukemia inhibitory factor` now has 3 rows
      reviewed of 294; `long-term synaptic potentiation` 5 of 139;
      `sensory perception of sound` 1 of 100.
- [ ] Review the IEP-heaviest gene products, none of which are in the repo: rat
      Ppargc1a (50 IEP rows), Il6 (48), Nos3 (45), Serpine1 (44), Tnf (43), Star
      (43), Hif1a (41), Ccl2 (40), Il1b (39). These are the extreme form of the
      inducible-bystander pattern — cytokines and stress hubs whose transcripts
      move under every perturbation — and rat/Hmgcs2's 33 rows, the repo's
      current maximum, is smaller than any of them.
- [ ] Work through [`data/iep_review_candidates.tsv`](IEP/data/iep_review_candidates.tsv):
      4,811 not-yet-reviewed gene products sampled up to 3 per global term
      stratum, so the long tail of terms is reachable and not just the head.
- [ ] Decide whether IEP warrants structured review fields. `PropagationReview`
      is documented as covering "a propagated **or inferred** annotation" and its
      `TERM_SCOPING_PROBLEM`, `NO_FAILURE_NON_CORE`, `ROLE_CONFLATION`,
      `GRANULARITY_MISMATCH` and `CONTEXT_OR_TISSUE_MISMATCH` values already fit
      IEP, but there is no value for the central IEP failure — *correlation
      asserted as participation*. Candidate additions: an
      `EXPRESSION_CORRELATION_ONLY` failure mode and a `REGULON_MEMBERSHIP`
      subtype.
- [ ] Extend the survey to HEP (the high-throughput IEP twin), which shares
      GORULE:0000006 and every pattern on this page but is generated at screen
      scale.
- [ ] Check the reviewed IEP corpus against the "normal expression only" rule —
      any row whose source paper is an overexpression study is mis-coded, not
      merely over-annotated.
- [x] Establish that the RNAcentral slice (840 rows, 437 miRNA precursors) is in
      scope. It is, via `ai-gene-review fetch-ncrna`; five miRNA reviews now
      exist. 432 gene products remain.

---

## Session Notes

### 2026-08-02 (third pass — the first batch cohort reviewed)

- **Retracted the scope claim.** The second pass said the RNAcentral slice was
  "out of scope by construction". That was wrong: the repo already reviews ncRNA
  entries (`id: URS…`, `product_type: MIRNA`; see human/MIR155, human/XIST) and
  has a dedicated `ai-gene-review fetch-ncrna` command. The gap was coverage, not
  capability.
- Reviewed five mouse miRNA precursors from the PMID:25858512 LTP batch, chosen
  to span the tiers the paper itself defines: 372 detected, 12 changed, 3
  validated, 130 annotated. Full details in
  [the cohort section](#cohort-review-130-mirnas-one-term-one-paper).
- **The tier predicted the verdict in every case.** Validated members
  (mouse/Mir26a-1, mouse/Mir384) ACCEPT; changed-but-untested (mouse/Mir30e)
  MARK_AS_OVER_ANNOTATED; detected-only (mouse/Mir100, mouse/Mir127) REMOVE. The
  middle tier is the useful one: mouse/Mir30e's expression change is real and IEP
  is the right code, so the failure is isolated to the inference, not the
  evidence.
- **Two findings stronger than the LTP batch itself.** mouse/Mir26a-1's
  `response to bacterium` is refuted by its own source, which shows the
  circulating-miRNA increase survives *Tlr2*, *Tlr4* and *NF-kB* knockout and
  concludes bacterial sensing is not the driver. And PMID:20439489 supplies
  mouse/Mir100 with both a validated IMP row and an unvalidated IEP batch row —
  the pattern visible within one paper and one gene.
- **The LTP batch omits let-7a**, one of the three miRNAs the paper establishes
  as required, while including 127 it never tested. Batch annotation is not just
  over-inclusive here; it is misaligned at both ends.
- Cohort flag rate 11/13 (85%) versus 16.7% corpus-wide, and 4 REMOVEs added to a
  corpus that previously held 7. **Reviewing batch cohorts is high-yield**, and
  reviewing them tier-by-tier is what makes the verdicts defensible rather than
  reflexive.
- Corpus figures updated throughout: reviewed IEP rows 525 → 538, flagged 15.0% →
  16.7%, REMOVE 7 → 11.

### 2026-07-27 (second pass — global denominator)

- Added [`iep_global_atlas.py`](IEP/iep_global_atlas.py) and
  [iep-global-atlas.md](IEP/iep-global-atlas.md). The first pass measured only the
  repo, whose GOA files exist because genes were picked for review; this pass
  downloads **all 25,401** IEP annotations in UniProt-GOA from QuickGO as the
  denominator. IEP is small enough that this is the complete population, not a
  sample.
- The reviewed corpus is **2.1%** of global IEP. Crucially, it is
  **representative for the stratifications the page's findings rest on** —
  stimulus-response branch 1.03x, developmental branch 0.89x, `involved_in` 0.97x,
  BP aspect 1.00x, gene-concentration 1.02x — and **skewed by organism**: human
  4.58x, *Dictyostelium* 6.34x, mouse 0.33x, fly 0.30x, MGI 0.05x, with AgBase,
  ZFIN, CollecTF, cotton, zebrafish, chicken and *M. tuberculosis* absent entirely.
- **Correction (aspect violations).** Querying QuickGO with
  `evidenceCodeUsage=exact` initially suggested non-BP IEP was ~0.2% of the code
  and that the repo had over-sampled it. Using `descendants` — which is what a
  GAF's IEP column actually means — gives **1,223** non-BP rows (4.8%), and the
  repo's 4.3% was proportionally accurate all along. The mechanism proposed from
  20 rows scales: **ECO:0000279 alone supplies 1,110 of the 1,147 CC violations
  (91%)** while being 6% of IEP, whereas the generic `ECO:0000270` parent is 99.8%
  BP and essentially rule-compliant. Fixing the ECO→GAF parent choice by aspect
  would clear 91% of the violations with zero curation.
- **The screen-batch pattern is the dominant global shape, and the Caco-2 case was
  a small instance.** References are sharply bimodal: 62.4% contribute exactly one
  IEP annotation, while the top six each annotate 72–291 gene products to exactly
  **one** term. The largest is PMID:20439489 (291 mouse gene products →
  `cellular response to leukemia inhibitory factor`). Three of the six are
  miRNA-profiling studies. PMID:11967071 is the flagship: a paper titled "Over
  1000 genes are involved in the DNA damage response of *E. coli*" yields
  `DNA damage response` for 152 genes including maltoporin `lamB` and maltose
  transporter `malF`.
- **The MGI gap is the consequential one.** The biggest batches are MGI's, and MGI
  is the group the repo samples at 0.05x — so the reviewed corpus systematically
  misses the most extreme form of a pattern the page documents.
- **New framing: IEP is load-bearing per gene, never per term.** Within a gene,
  72% of IEP rows are the sole carrier of their term; measured per term across the
  ontology, no frequent term exceeds **19.6%** IEP support
  (`seed trichome elongation`), and most are under 2%.
- Wrote [`data/iep_review_candidates.tsv`](IEP/data/iep_review_candidates.tsv):
  4,811 unreviewed gene products stratified across the global term distribution
  (≤3 per term, seeded), so future review can sample the tail rather than the head.

### 2026-07-27 (first pass — reviewed corpus)

- Created the project. Built [`iep_corpus_survey.py`](IEP/iep_corpus_survey.py),
  which surveys 147,856 cached GOA rows and 210 gene reviews, and writes
  [iep-corpus-survey.md](IEP/iep-corpus-survey.md). Everything below is measured
  on the repo only; see the second pass for how representative that is.
- **Headline finding:** IEP's problem is not error rate (15.0% flagged at the
  time, between ISO and IEA) but *centrality*. At 22.9% ACCEPT and 9.9%
  core-function grounding it was the weakest experimental code by both measures, with 56.8% of
  rows landing in `KEEP_AS_NON_CORE` — the highest of any code. The
  characteristic IEP annotation is true and peripheral.
- **Second finding:** the developmental branch (23.7% flagged) is riskier than
  the stimulus-response branch (15.1%), despite the latter carrying 70.5% of all
  IEP rows.
- **Third finding:** the 23 GORULE:0000006 aspect violations are an ECO→GAF
  mapping artifact, not curator error. ECO:0000279 (qualitative western
  immunoblotting) descends from both ECO:0000270 (→IEP) and ECO:0000314 (→IDA);
  the GAF projection picks IEP, so SynGO's fractionation-based CC annotations
  trip a BP-only rule.
- Identified PMID:21492153 (Caco-2 differentiation proteomics) as a
  single-screen batch source: 8 unrelated human genes, all annotated
  `epithelial cell differentiation`, 6 of them flagged and the other 2 kept only
  as non-core.
- Recorded the legitimate-use criterion: IEP holds when the gene's job *is* the
  response (heat-shock and UPR chaperones, infection-inducible effectors, clock
  genes, stage markers that are the differentiated product), and fails when a
  constitutively-functioning protein is merely swept up by the condition.
