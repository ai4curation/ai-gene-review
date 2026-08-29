---
title: ProTrek Evaluation
maturity: COMPLETE
tags: [EVALUATION, ML_PREDICTIONS]
species: [SCHPO, human, worm, yeast, mouse, rat, BACSU, ECOLI, PSEPK, DROME, ARATH, 9CAUD, AGKCO, ANOGA, 9PRIM, ABRPR, AEDAE, AQUCT, ARAHY, ARTAN, ASPOR, BALMU, BORPE, BOVIN, CAEEL, CALMI, CANLF, CHRVO, COLLI, COTJA, CUCME, DANRE, DEIRA, DROPS, DROVI, GADMO, GIBF5, JUGRE, MACFA, MAIZE, MYTGA, ORYSI, ORYSJ, PANPA, PARTE, PHATC, RABIT, SOYBN, STRCO, TAKRU, TOBAC, TRIV3, WHEAT, XANCP, XENNA, XENTR]
genes: [APP, Akt1, BCL2, BRCA2, BRI1, Bcl2, BenR, Buffy, CAT2, CDC37, COP1, CRY, CYCS, Calm1, Casp3, CnoX, CpxP, Ctnnb1, DnaJ, DnaK, Dscam1, EGFR, ETR1, Egfr, Epe1, FXN, Fyn, GAPDH, Git, GroEL, HSP104, HSP60, HTT, Hsp83, Hspa5, Hspa8, IRE1, KAR2, KEAP1, LRRK2, LysB, MYC, Mapk1, Myc, NFE2L2, NOTCH1, Nmnat, Notch1, PARK7, PDI1, PGRPLB, PTEN, Prkaa2, Pten, RAS2, Rgn, RidA, SIR2, SIRT1, SPAC8E11.10, SPCC16C4.02c, SSA1, SecB, Shu1, Skp, Slc5a1, SlyD, Spy, Src, St13, TARDBP, TOR1, TP53, Tp53, Trp53, Uggt1, VEGFA, alo1, amyE, aprE, atfs-1, atg101, atg13, atg16, atg2, atg38, atg5, bst1, catA, cmd-1, comK, cps1, csr-1, cts2, daf-16, daf-2, dfrP, divIVA, drp-1, fibrolase, fliY, ftsI, ftsY, ftsZ, gaa1, hlh-30, hsf-1, hsp-90, ire-1, lgg-1, mrcA, mrdA, pedH, pgl-1, phaC, pink-1, pmk-1, pmp20, pol5, pvdA, ral2, rpoS, secA, sigF, sigG, sigK, skn-1, snx41, spo0A, spoIIE, spoIIGA, surA, tam10, tim10, tpx1, ura7, A0A061AL94, A0A1S3BTE3, A0A1S3Y076, A0A2G9RZF1, A0A2I0M3K7, A0A2I4G8T1, A0A2K5UJ34, A0A2R9CAF4, A0A2U1PS28, A0A3B6GK97, A0A3B6NKR6, A0A3B6RKV1, A0A444Z7V7, A0A4W3GVU1, A0A674PKV4, A0A6I8TLE4, A0A6I8W8A2, A0A804UIX9, A0A8B6BFL6, A0A8B6GS20, A0A8B8L1Z3, A0A8B8WEG2, A0A8C2TBA7, A0A8C5FPT8, A0A8C9H4D2, A0A8I3PI07, A0A8J0SCI2, A0A8J1IYX6, A0A8M9QG43, A0BFB4, A2FPI7, B4MAQ2, B7FXQ8, B8BAB0, C6T1A2, D3VIU4, E1BL04, F4JLB7, F6LAX4, F6WPT1, G1TUN6, Q2U1U6, Q6YYC5, Q7NUH2, Q7VZI5, Q8P365, Q9KZ33, Q9L243, Q9RSY6, S0EDH7]
sidecars:
  protrek_go_calls: PROTREK_EVALUATION/argo50_protrek_go_calls.csv
  protrek_summary: PROTREK_EVALUATION/argo50_protrek_summary.json
  assessment_summary: PROTREK_EVALUATION/argo50_assessment_summary.json
  head_to_head: PROTREK_EVALUATION/argo50_head_to_head.json
  assessment_head_to_head: PROTREK_EVALUATION/argo50_assessment_head_to_head.json
  core_function_recall: PROTREK_EVALUATION/argo50_core_function_recall.csv
  training_overlap: PROTREK_EVALUATION/argo50_training_overlap.csv
  argo139_go_calls: PROTREK_EVALUATION/argo139_protrek_go_calls.csv
  argo139_summary: PROTREK_EVALUATION/argo139_protrek_summary.json
  argo139_assessment_summary: PROTREK_EVALUATION/argo139_assessment_summary.json
  argo139_three_way: PROTREK_EVALUATION/argo139_three_way.json
  argo139_core_function_recall: PROTREK_EVALUATION/argo139_core_function_recall.csv
  argo139_swissprot_status: PROTREK_EVALUATION/argo139_swissprot_status.csv
---
# ProTrek Evaluation

Evaluation of **ProTrek** (Su et al., *Nature Biotechnology* 2026,
[PMID:41039041](https://pubmed.ncbi.nlm.nih.gov/41039041/),
[doi:10.1038/s41587-025-02836-0](https://doi.org/10.1038/s41587-025-02836-0)) as a GO-annotation
source, on two cohorts and with the assessment taxonomy of
[de Crécy-Lagard et al. 2025 (PMID:40703034)](https://pubmed.ncbi.nlm.nih.gov/40703034/):

- **ARGO-ProtNLM-50** — the 50 proteins of the [ProtNLM2 evaluation](PROTNLM_EVALUATION.md), all
  unreviewed TrEMBL entries, giving a direct head-to-head with ProtNLM2.
  **[Interactive table](PROTREK_EVALUATION/protrek-eval.html)** — 50 proteins, 150 assessments.
- **ARGO139** — the 139 genes of the [BioReason comparison](BIOREASON_COMPARISON.md), overwhelmingly
  reviewed SwissProt entries in well-studied model organisms, giving a three-way comparison with
  BioReason-SFT and GO-GPT.
  **[Interactive table](PROTREK_EVALUATION/protrek-eval-argo139.html)** — 139 proteins, 417 assessments.

The two cohorts are **not pooled**, and the reason is the single most important control on this page:
127 of the 139 ARGO139 queries are SwissProt entries and ProTrek was trained on SwissProt
protein-text pairs, against **0 of 50** in ARGO-ProtNLM-50. Aggregate accuracy on ARGO139 is therefore partly
recall of memorised annotation, and the two numbers measure different things.

## Bottom line

ProTrek's protein→GO retrieval is **more specific and less reliable** than ProtNLM2's on this
benchmark. It reaches leaf-level terms that ProtNLM2 never attempts — naming the transported
substrate, the exact EC-level reaction, the correct cyclin partner — and on unannotated bacterial
proteins it produces specific correct calls where ProtNLM2 produced nothing. But roughly half its
top-3 output is wrong, and the errors are confident and plausible-looking rather than vague.

The most consequential finding is not about accuracy at all: **ProTrek's two text channels disagree
with each other on the same query.** Its free-text `Function` retrieval routinely returns the
correct UniProt function comment for a protein whose GO-annotation retrieval fails completely
(cohort 1, finding 1). Anyone using ProTrek to generate GO annotations is using its weaker channel.

On ARGO139 the headline numbers look much better — mean CS 1.30 against 0.85, concordance 58% against
35% — but **the entire gain is in already-known annotations**. Correct *novel* calls run at 13.2% on
ARGO139 and 13.3% on ARGO-ProtNLM-50. Moving from unreviewed proteins to the best-annotated genes in
biology improves what ProTrek can recite, not what it can contribute. Against BioReason-SFT and
GO-GPT on those same 139 genes, all three models sit within 0.02 of the same mean confidence score by
entirely different routes: the other two emit 40–80 mostly-ancestral terms per gene and are almost
never wrong, ProTrek emits three specific terms and is substantively wrong on 28% of them.

## What was evaluated, and why it had to be generated

ProTrek is a **retrieval** model, not a function predictor. It publishes weights and precomputed
embedding indexes; there is no prediction table to download and no API on the public server. So the
predictions were generated locally by reproducing the server's `sequence → text` mode against the
authors' own released SwissProt text indexes — see
[README](PROTREK_EVALUATION/README.md) for the pipeline and
[`run_protrek_retrieval.py`](PROTREK_EVALUATION/run_protrek_retrieval.py) for the re-implementation.
Only ProTrek's protein encoder is loaded; the text side is the authors' index.

**What a "ProTrek GO prediction" is here.** The SwissProt `GO_annotation` index holds 28,816
templated sentences of the form *"The GO term for this protein involving \<aspect\> incorporates
\<label\>."* Retrieving against it and parsing the label back to a GO id turns a retrieval into a GO
prediction. That index is ProTrek's entire GO vocabulary — about two thirds the size of GO's
non-obsolete term count, and frozen at index build time.

**Validation.** Five characterised SwissProt proteins (SOD1, GPX4, TP53, DnaK, GroEL) were run as
positive controls; the re-implementation retrieves their own UniProt FUNCTION comments verbatim, as
expected for training-set proteins ([`control_protrek_hits.tsv`](PROTREK_EVALUATION/control_protrek_hits.tsv)).

**Benchmark and contamination.** The queries are the 50 proteins of ARGO-ProtNLM-50, all TrEMBL
(unreviewed) entries with full AIGR reviews. ProTrek trained on SwissProt plus TrEMBL50 cluster
*representatives*; 9 of the 50 are the representative of their current UniRef50 cluster and so are
plausibly in training, the other 41 are not
([`argo50_training_overlap.csv`](PROTREK_EVALUATION/argo50_training_overlap.csv)). This is an
approximation — it uses the current UniRef50 release, not ProTrek's.

## Cohort 1: ARGO-ProtNLM-50

### Aggregate results

150 assessed predictions (top 3 per protein), categories from
[de Crécy-Lagard et al. 2025 (PMID:40703034)](https://pubmed.ncbi.nlm.nih.gov/40703034/).

| Category | Code | CS | Count | % |
|----------|------|----|-------|---|
| Correct novel | COR | 2 | 20 | 13.3% |
| Correct not novel | CNN | 2 | 20 | 13.3% |
| Less precise | LSP | 2 | 12 | 8.0% |
| Uncertain | UNC | 1 | 24 | 16.0% |
| Paralog incorrect | PLI | 0 | 23 | 15.3% |
| Nonparalog incorrect | NPI | 0 | 50 | 33.3% |
| Repetition | REP | 0 | 1 | 0.7% |
| **Total** | | | **150** | **Mean CS: 0.85/2.0** |

**Concordant** (CS=2): 52/150 (34.7%) · **Uncertain** (CS=1): 24/150 (16.0%) · **Discordant** (CS=0): 74/150 (49.3%)

#### Head-to-head with ProtNLM2

Same 50 proteins, same reviewer process, same categories. The prediction sets are built differently —
ProtNLM2 emits a variable-length set filtered by its Evidencer, ProTrek returns a ranked list that has
to be cut somewhere — so ProTrek is shown at both depth 3 and depth 1.

| | Proteins with predictions | Predictions | Mean CS | Concordant | Discordant |
|---|---|---|---|---|---|
| ProTrek (top 3) | 50 | 150 | 0.85 | 34.7% | 49.3% |
| ProTrek (top 1) | 50 | 50 | 0.92 | 40.0% | 48.0% |
| ProtNLM2 | 41 | 77 | 1.34 | 64.9% | 31.2% |

ProtNLM2 wins clearly, and the gap does not close when ProTrek is cut to one prediction per protein.
But the two models are wrong in opposite directions, and the aggregate hides that:

- **ProtNLM2's dominant non-error is imprecision.** 18 of its 77 calls are LSP — parent terms of
  annotations the protein already has. Its top call for a bifunctional amidating enzyme was one of
  the two reactions; for an ISG15-specific E2 it was "transferase activity".
- **ProTrek's dominant error is over-commitment.** It reaches the leaf and picks the wrong leaf:
  the wrong divalent cation, the wrong amino acid, the wrong cyclin partner, the wrong histone
  residue, the wrong phosphoinositide.
- **ProTrek covers proteins ProtNLM2 skipped.** Nine of the 50 got no ProtNLM2 GO prediction at all.
  ProTrek's single best result in the benchmark is one of them: *Bordetella* BP0922, an unannotated
  PrpF-family protein, where the rank-1 call (methylitaconate delta-isomerase activity, score 19.66,
  3.2 units clear of rank 2) is exactly the core function the AIGR review derived independently.
- **Term-level agreement between the models is almost nil**: 8 identical GO terms in total, on 7 of
  the 39 proteins for which ProtNLM2 emitted GO predictions
  ([`argo50_head_to_head.json`](PROTREK_EVALUATION/argo50_head_to_head.json)). They are not two
  views of one answer.

#### Recall of the curated core function

A stricter question than GOA agreement: does ProTrek retrieve the function the AIGR review calls
*core*, and at what rank? ([`core_function_recall.py`](PROTREK_EVALUATION/core_function_recall.py))

| Aspect | n | Exact @1 | Exact @3 | Exact @5 | Exact @25 | Any is_a/part_of relation @25 |
|--------|---|----------|----------|----------|-----------|-------------------------------|
| Molecular function | 49 | 6 | 11 | 12 | 19 (39%) | 34 (69%) |
| Biological process | 40 | 1 | 3 | 10 | 13 (33%) | 24 (60%) |
| Cellular component | 42 | 0 | 1 | 2 | 6 (14%) | 20 (48%) |

Molecular function is where ProTrek is strongest and cellular component is where it is weakest —
the opposite of what a localisation-oriented pipeline gives you, and a genuine complementarity.

### Key findings

#### 1. The GO channel and the free-text channel are different predictors

Run on the same sequence, ProTrek's `Function` index and its `GO_annotation` index frequently
disagree, and the free-text one is right more often. This is the single most actionable result here,
because GO annotation is exactly the use case that runs on the weaker index.

| Protein | Free-text `Function` hit (rank 1) | `GO_annotation` top calls | Verdict |
|---|---|---|---|
| Q9RSY6 *(D. radiodurans bS1)* | "Binds mRNA; thus facilitating recognition of the initiation point… short Shine-Dalgarno" (18.6) | misfolded RNA binding, poly(A) binding, poly(A)-tail-shortening regulation (12.6) | free-text exactly right; GO channel returns eukaryotic mRNA metabolism for a bacterial ribosomal protein |
| Q6YYC5 *(rice RGLG4)* | RGLG1/2/4 comments incl. "mediates the formation of 'Lys-63'-linked ubiquitin chains" (18.8) | five plant defence/hormone processes; no ubiquitination at all | GO channel never mentions the annotated E3 activity |
| A0A8B6GS20 *(mussel MTMR9)* | "Probably acts as an adapter for other myotubularin-like phosphatases" (15.4) | four phosphoinositide phosphatase activities | free-text identifies the pseudophosphatase; GO channel assigns the lost catalytic activity |
| A0A3B6RKV1 *(wheat JmjC)* | AtJMJ22: "demethylates 'Arg-3' (H4R3me)… specific activity for H4R3me2" (19.1) | H3K27 and H3K9 demethylase terms | free-text names the right substrate; GO channel names the frequent ones |
| Q7NUH2 *(C. violaceum MarR)* | "Regulatory protein involved in autolytic activity, multidrug resistance and virulence" (15.4) | sterol-biosynthesis enzymes (11.6) | free-text right, GO channel not merely imprecise but unrelated |
| A0A444Z7V7 *(peanut CSLD3)* | "Golgi-localized beta-glycan synthase… noncellulosic polysaccharides (hemicelluloses)" (21.9) | four cellulose-synthesis terms | free-text distinguishes CSLD from CESA; GO channel does not |

The cause is structural, not a bug: SwissProt's *prose* records scaffolding roles, lost catalytic
activity, substrate identity and lineage-specific caveats, while its *GO* annotations for the same
families are dominated by the frequent catalytic terms. ProTrek can only return what is in the index
it is pointed at.

#### 2. Errors are within-family, not random

`PARALOG_OVERANNOTATION` is the largest error class (33 of 74 discordant calls), followed by
`FREQUENCY_BIAS` (20), `PSEUDOENZYME_OVERANNOTATION` (9), `TAXON_CONSTRAINT_VIOLATION` (8) and
`LOCALIZATION_DEFAULT` (4). ProTrek almost always lands in the right neighbourhood and then picks
the wrong occupant of it:

- **Wrong substrate**: manganese for magnesium (CNNM4); L-histidine for L-cystine (FliY, 0.23 score
  units apart); five glucosyltransferase acceptors within 0.6 units of each other (walnut UGT73C).
- **Wrong partner**: cyclin K–CDK12/13 for a cyclin-Y–CDK16 kinase, at the benchmark's fourth-highest
  top-1 score.
- **Wrong direction**: a Ras GEF complex for a RasGAP; 3'-trailer cleavage for a 5'-leader enzyme;
  RNA-directed RNA polymerase for a reverse transcriptase; a deubiquitinase for a HERC ligase
  fragment. Opposite-signed regulatory terms also appear together in one top-3 (RIC7: positive *and*
  negative regulation of the same defence response).
- **Has-domain vs binds-domain**: for fugu gas7a, an F-BAR protein, the top call is `F-BAR domain
  binding` — the term for proteins that bind one. A domain-mapping pipeline structurally cannot make
  this error.

#### 3. Pseudoenzymes fail in both models, independently

MTMR9 (missing CX5R catalytic cysteine) drew the same wrong catalytic term — `GO:0004438` — from
ProTrek and ProtNLM2. TBC1D14, shown not to be a Rab-GAP, drew GTPase-activation terms. Auxilin's
degenerate PTEN-like domain drew PTEN's exact reaction three times over. Neither
sequence-similarity retrieval nor seq2seq naming can detect a missing active-site residue; this
needs a separate check, and the GOA IEA annotations for these entries carry the same error, so the
models are reinforcing rather than correcting the record.

#### 4. The score is a usable abstention signal — and the only one

ProTrek always returns *k* results, with no way to say "no match". The score is what carries that
information, and it works:

| Score cutoff | n predictions | Concordant | Discordant |
|---|---|---|---|
| < 10 | 12 | **0%** | 66.7% |
| ≥ 12 | 113 | 42.5% | 46.0% |
| ≥ 15 | 66 | 50.0% | 42.4% |
| ≥ 16 | 48 | 58.3% | 35.4% |

Median score is 16.3 for concordant calls and 14.3 for discordant ones. Below 10 nothing was
correct. The two worst results in the benchmark — a 74-aa MCM-4 fragment that drew methanogenesis
and archaeal flagellum, and a 169-aa HERC3 isoform that drew fucose binding and semaphorin receptor
activity — both sit in that band, and both are **short predicted fragments**. Read without scores
those lists look like five confident annotations each. Any pipeline consuming ProTrek output should
threshold, and should exclude short predicted isoforms.

#### 5. The GO index is frozen and has drifted

Of the 150 assessed (top-3) calls, 10 resolve to terms GO has since **obsoleted** and 2 to labels that
no longer resolve at all — 12 (8.0%) could not be entered as annotations even when correct. Across
the full top-5 output the rate is the same: 16 obsolete and 3 unresolved out of 250. The sharpest
case is the tobacco PRORP, where the closest-to-correct call (`endonucleolytic cleavage
involved in tRNA processing`) is obsolete: index staleness, not model error, blocks it. This is a
maintenance property of any retrieval system with a precomputed text index, and it is invisible to
the user.

#### 6. It sometimes corrects the record

Two cases where ProTrek's top call disagreed with the existing automatic annotation and was right:

- **A0A2U1PS28** — UniProt names it "Translation factor GUF1 homolog, **mitochondrial**" from a HAMAP
  rule and GOA annotates mitochondrial matrix and inner membrane. ProTrek's five top calls are all
  **plastid**, agreeing with the AIGR review's paralog reassignment.
- **A0A3B6NKR6** — GOA carries mevalonate-pathway IEA; ProTrek's rank 1 is glucuronokinase activity,
  the sugar-kinase branch of the GHMP family the review argues for. Its rank 2, however, is the
  disputed GOA term, so both sides of the dispute appear in one top three, 1.1 score units apart.

The second case is also a warning for automated scoring: agreeing with GOA is not the same as being
right, and a benchmark that treats an existing IEA annotation as truth would score that call as
correct.

## Cohort 2: ARGO139

The 139 genes of the [BioReason comparison](BIOREASON_COMPARISON.md), run through the identical
pipeline and assessed with the identical taxonomy, so ProTrek can be placed beside BioReason-SFT and
GO-GPT on the same genes. Fourteen organisms: *S. pombe* (23), human (19), *C. elegans* (15),
*B. subtilis* (13), *E. coli* (13), rat (12), mouse (11), *S. cerevisiae* (11), *D. melanogaster* (8),
*P. putida* (8), *A. thaliana* (3), and one each from *A. gambiae*, a copperhead snake and a phage.

### Read this cohort as recall, not prediction

127 of the 139 queries (91.4%) are **SwissProt** entries
([`argo139_swissprot_status.csv`](PROTREK_EVALUATION/argo139_swissprot_status.csv)). ProTrek's
searched `GO_annotation` index is built from SwissProt, so for those 128 proteins the model's own GO
sentences are inside the index it is retrieving from. An exact GOA match there is the model finding
an annotation it was shown, not generalising to a new one. The ARGO-ProtNLM-50 cohort has none of
this — every query is TrEMBL — which is why the two are reported separately.

The effect is exactly what that predicts. Top-3 calls that exactly match an existing GOA term:
**34.1% in ARGO139 (142/417) against 10.7% in ARGO-ProtNLM-50 (16/150)**.

### Aggregate results

417 assessed predictions (top 3 per protein, 139 proteins).

| Category | Code | CS | Count | % | ARGO-ProtNLM-50 % |
|----------|------|----|-------|---|-------------------|
| Correct novel | COR | 2 | 55 | 13.2% | 13.3% |
| Correct not novel | CNN | 2 | 157 | 37.6% | 13.3% |
| Less precise | LSP | 2 | 31 | 7.4% | 8.0% |
| Uncertain | UNC | 1 | 55 | 13.2% | 16.0% |
| Paralog incorrect | PLI | 0 | 33 | 7.9% | 15.3% |
| Nonparalog incorrect | NPI | 0 | 82 | 19.7% | 33.3% |
| Repetition | REP | 0 | 4 | 1.0% | 0.7% |
| **Total** | | | **417** | **Mean CS: 1.30/2.0** | **0.85/2.0** |

**Concordant** (CS=2): 243/417 (58.3%) · **Uncertain** (CS=1): 55/417 (13.2%) · **Discordant** (CS=0): 119/417 (28.5%)

**The whole gain is CNN.** ProTrek looks far better here — mean CS 1.30 against 0.85, concordance 58%
against 35% — and every point of that comes from correct-but-already-annotated calls, which rise from
13.3% to 37.6%. The rate of **correct novel** calls is 13.2% here and 13.3% there: statistically
identical. Put plainly, moving from unreviewed proteins to some of the best-annotated genes in biology
does not improve ProTrek's ability to tell a curator something new. It improves its ability to recite
what the curator already has. For a curation workflow, where the value is in COR and the cost is in
PLI and NPI, the two cohorts are roughly equally useful and equally expensive.

### Three-way comparison on the same 139 genes

BioReason-SFT and GO-GPT emit large sets that include ancestor terms, so most of their calls are
unassessable in this scheme; both distributions are shown with and without UNC.

| | Predictions | per gene | Mean CS | Concordant | Discordant | UNC |
|---|---|---|---|---|---|---|
| ProTrek (top 3) | 417 | 3.0 | 1.30 | 58.3% | 28.5% | 13.2% |
| ProTrek (top 1) | 139 | 1.0 | 1.44 | 64.7% | 20.9% | 14.4% |
| BioReason-SFT | 10,697 | 77.0 | 1.31 | 32.3% | 1.5% | 66.1% |
| GO-GPT (leaf) | 5,923 | 42.6 | 1.30 | 32.1% | 2.1% | 65.8% |

All three land within 0.02 of the same mean confidence score, and the number is meaningless as a
ranking: it is produced three different ways. BioReason-SFT and GO-GPT reach it by emitting 40–80
terms per gene, two thirds of which are ancestors too general to adjudicate and almost none of which
are wrong — a *precision-by-vagueness* profile. ProTrek reaches it by emitting three specific terms,
of which roughly one is new, one is already known and one is wrong. **Discordance is the honest
column**: 28.5% against 1.5% and 2.1%. ProTrek is the only one of the three that will put a
substantively false statement in front of a curator, and it does so on more than a quarter of its
output. It is also the only one that names a specific enzyme reaction or complex rather than a
superclass.

### Recall of the curated core function

Does ProTrek retrieve the function the AIGR review calls *core*, and at what rank?
([`argo139_core_function_recall.csv`](PROTREK_EVALUATION/argo139_core_function_recall.csv))

| Aspect | n | Exact @1 | Exact @3 | Exact @5 | Exact @25 | Any is_a/part_of relation @25 |
|--------|---|----------|----------|----------|-----------|-------------------------------|
| Molecular function | 136 | 15 | 32 | 37 | 66 (49%) | 80 (59%) |
| Biological process | 117 | 8 | 22 | 42 | 68 (58%) | 92 (79%) |
| Cellular component | 115 | 10 | 20 | 21 | 38 (33%) | 61 (53%) |

Better than ARGO-ProtNLM-50 across the board, as memorisation predicts — but note that the curated
core molecular function is still absent from the top 3 for 104 of 136 core functions, on genes whose
GOA records mostly already contain it.

### Findings specific to this cohort

#### 1. A third of all calls are sentences the model also emits for a different gene

Across the 139 genes' top-5 output there are 687 resolvable calls drawing on 540 distinct GO terms,
and **256 of those calls (37%) use a term ProTrek also returns for at least one other gene in the
same set**; 26 terms are emitted for three or more genes. Some of that sharing is legitimate — the three *B.
subtilis* sporulation sigma factors *sigF*, *sigG* and *sigK* really do share sporulation terms, and
BACSU/sigF's identical output to its paralogs reproduces the same collapse BioReason showed. Much
of it is not:

- `GO:1902097` (an obsolete Gram-negative-defence transcription composite) is returned for **five
  different *C. elegans* genes** — as rank 1 for `hlh-30`, `pmk-1` and `skn-1`, rank 4 for `atfs-1`
  and `hsf-1`. It is defensible for all five, but the model is emitting one sentence for five
  unrelated transcription factors and kinases rather than distinguishing them.
- `GO:0031249` denatured protein binding is the model's generic HSP70 answer, returned for four
  genes: rank 2 for both rat/`Hspa8` and rat/`St13`, rank 5 for yeast/`SSA1`, and again for
  rat/`Hspa5`.
- yeast/`CDC37` and yeast/`RAS2` — a co-chaperone and a GTPase, sharing no pathway — receive the
  **same two pheromone-response terms at the same two ranks** (`GO:0010969` at rank 2, `GO:0062038`
  at rank 3). The mating and pheromone neighbourhood recurs for yeast/`SSA1` and yeast/`TOR1` too,
  and *yeast* mating-type-switching terms are returned for worm/`skn-1`, where the process cannot
  occur.

The pattern is an organism-level prior: having recognised what kind of organism the sequence comes
from, the model draws from that organism's most heavily annotated literature.

#### 2. Orthologs get identical lists, errors included

Yeast `IRE1` and worm `ire-1` return **the same four terms in the same order** — Ire1 complex,
IRE1-mediated UPR, IRE1-TRAF2-ASK1 complex, ER UPR — with the worm scores running about 3 units
higher throughout (23.29 against 20.34 at rank 1). The third
of those is a mammalian module defined by TRAF2 and ASK1, which neither organism has, so the same
impossible complex is asserted for a fungus and a nematode. Rat `Tp53` and mouse `Trp53` likewise
share ranks 1–4 exactly (ATP-dependent DNA/DNA annealing, two ranks of actinomycin-D response,
circadian behavior) while human `TP53` gets a completely different list dominated by thymocyte and
oligodendrocyte apoptosis — and none of the three retrieves the transcription factor activity that
defines p53. Three orthologs, three unrelated answers, the two rodents matching each other because
they share a thin ISS/ISO annotation layer.

#### 3. The templated index cannot separate a claim from its negation

Every GO term is stored as one sentence, so a term and its opposite differ by a single word and the
embedding does not reliably separate them:

- worm/`pink-1`: rank 1 *positive* regulation of autophagy of mitochondrion (correct), rank 2
  *negative* regulation of the same process (wrong), 0.74 units apart.
- yeast/`SIR2`: rank 4 is *negative* regulation of silent mating-type cassette heterochromatin
  formation — the exact inversion of the protein's best-known function, which GOA holds with IMP.
- yeast/`CDC37`: the unsigned, positive and negative forms of one pheromone-pathway claim occupy
  ranks 2, 3 and 4 of a single top five.

A curator spots this instantly. A pipeline consuming top-*k* ingests the claim and its negation
together.

#### 4. The specificity is real, and so is the cost of it

Where the model commits to a specific reaction it is often right and often wrong at nearly the same
score, which is where most of the reviewer time went:

- yeast/`SIR2` — the *residue lottery*. Four of five calls are residue-specific NAD-dependent histone
  deacetylase activities spanning 0.97 score units: H3K14 and H4K16 are exact GOA matches; H3K18 is a
  SIRT7 specificity; H3K56 belongs to Hst3/Hst4, Sir2's own paralogs. Ranks 2 and 3 — one right, one
  wrong — differ by 0.003 units.
- yeast/`CAT2` — acetyl-, palmitoyl- and octanoyl-carnitine transferase at ranks 1, 2 and 3. Only the
  first exists in *S. cerevisiae*.
- rat/`Slc5a1` — low-affinity glucose (SGLT2/SGLT4) and mannose (SGLT4) symporter activities at ranks
  1 and 2, **above** the correct high-affinity D-glucose symporter at rank 3, which they outscore by
  0.085 and 0.001 units.

`PARALOG_OVERANNOTATION` is again the largest error class (58 of 119 discordant calls), followed by
`FREQUENCY_BIAS` (16), `TAXON_CONSTRAINT_VIOLATION` (16), `LOCALIZATION_DEFAULT` (10) and
`PSEUDOENZYME_OVERANNOTATION` (8).

#### 5. Molecular function goes missing on exactly the proteins that have one

A recurring shape across the cohort: for a well-characterised enzyme or chaperone, the top five is
processes, compartments and complexes, and the catalytic activity is absent — including from GOA
records that hold it with IDA support.

| Gene | Curated core molecular function | In ProTrek top 5? |
|---|---|---|
| yeast/`HSP104` | ATP-dependent protein disaggregase activity | no — three stress processes, two aggregate compartments |
| yeast/`SSA1` | ATP-dependent protein folding chaperone | no — no ATP, chaperone or folding term at all |
| worm/`lgg-1` | phosphatidylethanolamine binding | no — four correct autophagosome/autophagy terms, no MF |
| worm/`ire-1` | RNA endonuclease + Ser/Thr kinase activity | no — complexes and processes only |
| worm/`pgl-1` | ribonuclease T1 activity | no — condensate-biology terms; free-text channel has it at rank 1 |
| worm/`pmk-1` | MAP kinase activity (IDA) | no |
| rat/`Mapk1` | MAP kinase activity (IDA) | no |
| yeast/`TOR1` | protein Ser/Thr kinase activity (IDA) | no |

Two CMGC MAP kinases in different phyla, both with IDA-supported MAP kinase activity, and neither
retrieves it.

#### 6. Score calibration collapses on this cohort

In ARGO-ProtNLM-50 the score separated right from wrong: median 16.3 for concordant calls against
14.3 for discordant. Here the medians are **16.68 and 16.29** — a 0.39-unit gap that is unusable as a
filter. Thresholding at ≥16 lifts concordance only from 58.0% to 62.2%.

The one part that survives is the abstention band. Only 11 of 417 calls score below 10, and **0% of
them are concordant** while 81.8% are discordant — the same finding as the other cohort. Both of the
worst results sit there and are the same kind of protein: yeast/`TOR1` (2470 aa, top-1 score 9.70)
and human/`BRCA2` (3418 aa, 9.85); human/`LRRK2` (2527 aa) is lowest of all at 9.38 and human/`HTT`
(3142 aa) sits at the boundary at 10.00. All four are very large multi-domain proteins with no
dominant repeat type — and *not* simply long ones, since human/`NOTCH1` (2555 aa) scores 15.87,
mouse/`Notch1` (2531 aa) 16.10 and DROME/`Dscam1` (2016 aa) 17.17. Across both cohorts top-1 score
correlates with length at Spearman ρ = 0.19
([`score_vs_length.json`](PROTREK_EVALUATION/score_vs_length.json)), so length alone does not
explain it.

#### 7. Index staleness is worse here

34 of the 417 top-3 calls (8.2%) resolve to terms GO has since obsoleted and 5 to labels that no
longer resolve at all, against 6.7% and 1.3% in the other cohort. worm/`hsf-1` is the extreme case:
**three of its five calls are obsolete, including the top one at 18.83**, all of them GO-CAM-style
composites the ontology has retired. Every one of the three is a correct statement about HSF-1 that
cannot be entered as an annotation, and nothing in the output signals this.

### Per-organism results

| Organism | Genes | Predictions | Mean CS | Concordant | Discordant |
|---|---|---|---|---|---|
| *S. pombe* | 23 | 69 | 1.16 | 50.7% | 34.8% |
| Human | 19 | 57 | 1.18 | 47.4% | 29.8% |
| *C. elegans* | 15 | 45 | 1.22 | 57.8% | 35.6% |
| *B. subtilis* | 13 | 39 | 1.28 | 56.4% | 28.2% |
| *E. coli* | 13 | 39 | 1.44 | 66.7% | 23.1% |
| Rat | 12 | 36 | 1.56 | 69.4% | 13.9% |
| Mouse | 11 | 33 | 1.70 | 78.8% | 9.1% |
| *S. cerevisiae* | 11 | 33 | 1.27 | 57.6% | 30.3% |
| *D. melanogaster* | 8 | 24 | 1.25 | 58.3% | 33.3% |
| *P. putida* | 8 | 24 | 1.25 | 58.3% | 33.3% |

Mouse and rat score highest and human lowest of the three mammals, which is the opposite of what
literature volume would predict. The likely reason is visible in the reviews: rodent GOA records are
padded with ISS/ISO annotations transferred from each other, and those thin, transferred terms are
what the retrieval reproduces — which is why rat/`Tp53` scores well while retrieving nothing that
matters about p53.

### A data-hygiene finding that was masking a model finding

worm/`csr-1` was originally unscorable. The gene folder cached UniProt **Q17370 — nuclear hormone
receptor nhr-47** — instead of the Argonaute CSR-1 its own review describes, so the sequence
submitted was the wrong protein's; the same was true of the BioReason-SFT and GO-GPT prediction
sets, whose RL export embeds that 579 aa sequence verbatim. The cause was a resolver bug:
`gene_exact:` matches gene *synonyms*, `nhr-47` carries `csr-1` as a stale synonym, and the
prefer-reviewed rule then chose it over the real gene, which is TrEMBL-only
([#2720](https://github.com/ai4curation/ai-gene-review/issues/2720),
[#2721](https://github.com/ai4curation/ai-gene-review/issues/2721)).

The folder has been re-fetched against **H2KZD5** and ProTrek re-run. The corrected result is worth
having, because it reproduces the cohort's signature failure in the hardest setting available:
*C. elegans* encodes 24 Argonautes with sharply divided jobs. Rank 1 (RNAi effector complex, 18.26)
is the right compartment class and the parent of GOA's RISC complex, and the free-text channel
returns what is effectively CSR-1's own description at 19.32 — an Argonaute binding
RNA-dependent-RNA-polymerase-derived 22G endo-siRNAs. Below that the retrieval reaches for other
family members' specialities: co-transcriptional nuclear silencing (NRDE-3/HRDE-1) at rank 2, and
antiviral RNAi (RDE-1/DRH-1) at ranks 4 and 5. The `Subcellular_location` channel names the
substitution outright, returning a sentence about nrde-3 at rank 2. Right family, wrong member —
the same shape as CAT2, SIR2 and Slc5a1, on a gene family with 24 members to choose from.

The BioReason-SFT and GO-GPT rows are web-app exports that cannot be regenerated here. They had been
scored against CSR-1 — 30 of 37 SFT calls marked NPI — which penalised those models for correctly
describing the protein they were handed; all of their csr-1 rows are now recorded as UNC with
`WRONG_INPUT_SEQUENCE`. Reassuringly, the corrupt row never drove anything: correcting it moves
every headline figure in this section by at most 0.005 mean CS and 0.5 percentage points.

## Reproducibility

All numbers on this page are recomputed from the committed files by scripts in
[`PROTREK_EVALUATION/`](PROTREK_EVALUATION/README.md); none is hard-coded. The retrieval itself needs
the ProTrek weights and SwissProt faiss indexes (several GB, not committed) — the README gives the
download commands. Per-protein assessments live beside each gene as
`genes/<SPECIES>/<GENE>/<GENE>-protrek-predictions-review.yaml` — keyed by accession for
ARGO-ProtNLM-50 and by gene symbol for ARGO139, following each cohort's directory convention.

| File | Description |
|------|-------------|
| [`README.md`](PROTREK_EVALUATION/README.md) | Pipeline, prerequisites, file index |
| [`argo50_protrek_hits.tsv`](PROTREK_EVALUATION/argo50_protrek_hits.tsv) | Raw ranked retrieval output, 4 subsections × top 25 |
| [`argo50_protrek_go_calls.csv`](PROTREK_EVALUATION/argo50_protrek_go_calls.csv) | Top-5 GO calls with label resolution and GOA overlap |
| [`argo50_assessment_summary.json`](PROTREK_EVALUATION/argo50_assessment_summary.json) | Curated assessment counts, error types, score calibration |
| [`argo50_assessment_head_to_head.json`](PROTREK_EVALUATION/argo50_assessment_head_to_head.json) | ProTrek vs ProtNLM2 assessment distributions |
| [`argo50_head_to_head.json`](PROTREK_EVALUATION/argo50_head_to_head.json) | Term-level overlap between the two models |
| [`argo50_core_function_recall.csv`](PROTREK_EVALUATION/argo50_core_function_recall.csv) | Rank at which each curated core function is retrieved |
| [`argo50_training_overlap.csv`](PROTREK_EVALUATION/argo50_training_overlap.csv) | UniRef50 representative status per query |
| [`argo139_protrek_hits.tsv`](PROTREK_EVALUATION/argo139_protrek_hits.tsv) | Raw ranked retrieval output for cohort 2 |
| [`argo139_protrek_go_calls.csv`](PROTREK_EVALUATION/argo139_protrek_go_calls.csv) | Top-5 GO calls with label resolution and GOA overlap |
| [`argo139_assessment_summary.json`](PROTREK_EVALUATION/argo139_assessment_summary.json) | Curated assessment counts, error types, score calibration |
| [`argo139_three_way.json`](PROTREK_EVALUATION/argo139_three_way.json) | ProTrek vs BioReason-SFT vs GO-GPT on the same 139 genes |
| [`argo139_core_function_recall.csv`](PROTREK_EVALUATION/argo139_core_function_recall.csv) | Rank at which each curated core function is retrieved |
| [`argo139_swissprot_status.csv`](PROTREK_EVALUATION/argo139_swissprot_status.csv) | SwissProt vs TrEMBL section per query — the memorisation control |
| [`score_vs_length.json`](PROTREK_EVALUATION/score_vs_length.json) | Top-1 score against sequence length across both cohorts |
| [`dump_argo139_context.py`](PROTREK_EVALUATION/dump_argo139_context.py) | Per-gene curation digest used by the reviewer |
| [`write_reviews.py`](PROTREK_EVALUATION/write_reviews.py) | Emits prediction-review YAMLs from a judgement-only spec |

## Limitations

- **One retrieval mode.** Only `sequence → text` against the SwissProt index was evaluated. ProTrek's
  structure encoder, its larger databases (UniRef50, OMG, MGnify — billions of sequences), and its
  text→sequence direction are untested here. The paper's headline claims concern retrieval quality
  against alignment tools, which this does not measure.
- **The reference is agent-adjudicated, not expert-signed.** The AIGR reviews are the comparison
  standard and carry mixed maturity, as in the [BioReason comparison](BIOREASON_COMPARISON.md).
- **Depth 3 is a choice.** ProTrek has no natural prediction-set boundary. Depth 1 is also reported;
  intermediate depths were not scored.
- **Neither benchmark was built for ProTrek.** ARGO-ProtNLM-50 was built to stratify ProtNLM2's
  behaviour and is enriched for unreviewed proteins and ProtNLM2 case studies; ARGO139 was built for
  the BioReason comparison and is enriched for well-studied model-organism genes. Together they
  bracket the range rather than sample it.
- **ARGO139 is 92% SwissProt.** Its aggregate accuracy is not a generalisation measure. The
  correct-novel rate, which is insensitive to memorisation, is the number to carry forward.
- **Mixed reference maturity in ARGO139.** Of the 139 AIGR reviews used as the comparison standard,
  67 are COMPLETE, 48 DRAFT, 20 IN_PROGRESS and 4 INITIALIZED; yeast/`PDI1` has no `core_functions`
  at all (assessed against GOA instead), and worm/`csr-1` was re-fetched mid-evaluation after its
  cached accession was found to name a different gene — its ProTrek row is current, but its
  BioReason-SFT and GO-GPT rows still derive from the wrong sequence and are scored UNC.
- **One reviewer, one pass.** Every assessment on both cohorts is agent-adjudicated by a single
  reviewer without a second opinion; borderline COR/CNN and NPI/UNC calls in particular would move
  under a different reviewer.

## References

- [PMID:41039041](https://pubmed.ncbi.nlm.nih.gov/41039041/) — Su J, He Y, You S, et al. *A trimodal protein language model enables advanced protein searches.* Nat Biotechnol 2026
- [ProTrek GitHub](https://github.com/westlake-repl/ProTrek) · [web server](http://search-protrek.com) · [ProTrek_650M weights](https://huggingface.co/westlake-repl/ProTrek_650M) · [faiss indexes](https://huggingface.co/datasets/westlake-repl/faiss_index)
- [ProtNLM2 evaluation](PROTNLM_EVALUATION.md) — the companion evaluation on the same 50 proteins
- [BioReason comparison](BIOREASON_COMPARISON.md) — the source of the ARGO139 gene set and of the
  BioReason-SFT and GO-GPT prediction sets compared here
- [de Crécy-Lagard et al. 2025 (PMID:40703034)](https://pubmed.ncbi.nlm.nih.gov/40703034/) — assessment categories
