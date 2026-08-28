---
title: ProTrek Evaluation
maturity: COMPLETE
tags: [EVALUATION, ML_PREDICTIONS]
species: [9PRIM, ABRPR, AEDAE, AQUCT, ARAHY, ARATH, ARTAN, ASPOR, BALMU, BORPE, BOVIN, CAEEL, CALMI, CANLF, CHRVO, COLLI, COTJA, CUCME, DANRE, DEIRA, DROPS, DROVI, GADMO, GIBF5, JUGRE, MACFA, MAIZE, MYTGA, ORYSI, ORYSJ, PANPA, PARTE, PHATC, RABIT, SOYBN, STRCO, TAKRU, TOBAC, TRIV3, WHEAT, XANCP, XENNA, XENTR]
genes: [A0A061AL94, A0A1S3BTE3, A0A1S3Y076, A0A2G9RZF1, A0A2I0M3K7, A0A2I4G8T1, A0A2K5UJ34, A0A2R9CAF4, A0A2U1PS28, A0A3B6GK97, A0A3B6NKR6, A0A3B6RKV1, A0A444Z7V7, A0A4W3GVU1, A0A674PKV4, A0A6I8TLE4, A0A6I8W8A2, A0A804UIX9, A0A8B6BFL6, A0A8B6GS20, A0A8B8L1Z3, A0A8B8WEG2, A0A8C2TBA7, A0A8C5FPT8, A0A8C9H4D2, A0A8I3PI07, A0A8J0SCI2, A0A8J1IYX6, A0A8M9QG43, A0BFB4, A2FPI7, B4MAQ2, B7FXQ8, B8BAB0, C6T1A2, D3VIU4, E1BL04, F4JLB7, F6LAX4, F6WPT1, G1TUN6, Q2U1U6, Q6YYC5, Q7NUH2, Q7VZI5, Q8P365, Q9KZ33, Q9L243, Q9RSY6, S0EDH7]
sidecars:
  protrek_go_calls: PROTREK_EVALUATION/argo50_protrek_go_calls.csv
  protrek_summary: PROTREK_EVALUATION/argo50_protrek_summary.json
  assessment_summary: PROTREK_EVALUATION/argo50_assessment_summary.json
  head_to_head: PROTREK_EVALUATION/argo50_head_to_head.json
  assessment_head_to_head: PROTREK_EVALUATION/argo50_assessment_head_to_head.json
  core_function_recall: PROTREK_EVALUATION/argo50_core_function_recall.csv
  training_overlap: PROTREK_EVALUATION/argo50_training_overlap.csv
---
# ProTrek Evaluation

Evaluation of **ProTrek** (Su et al., *Nature Biotechnology* 2026,
[PMID:41039041](https://pubmed.ncbi.nlm.nih.gov/41039041/),
[doi:10.1038/s41587-025-02836-0](https://doi.org/10.1038/s41587-025-02836-0)) as a GO-annotation
source, on the same 50 proteins and with the same assessment taxonomy as the
[ProtNLM2 evaluation](PROTNLM_EVALUATION.md), giving a direct head-to-head.

**[Interactive prediction evaluation table](PROTREK_EVALUATION/protrek-eval.html)** — all 50 proteins
and 150 prediction assessments.

## Bottom line

ProTrek's protein→GO retrieval is **more specific and less reliable** than ProtNLM2's on this
benchmark. It reaches leaf-level terms that ProtNLM2 never attempts — naming the transported
substrate, the exact EC-level reaction, the correct cyclin partner — and on unannotated bacterial
proteins it produces specific correct calls where ProtNLM2 produced nothing. But roughly half its
top-3 output is wrong, and the errors are confident and plausible-looking rather than vague.

The most consequential finding is not about accuracy at all: **ProTrek's two text channels disagree
with each other on the same query.** Its free-text `Function` retrieval routinely returns the
correct UniProt function comment for a protein whose GO-annotation retrieval fails completely
(§3 below). Anyone using ProTrek to generate GO annotations is using its weaker channel.

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

## Aggregate results

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

### Head-to-head with ProtNLM2

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

### Recall of the curated core function

A stricter question than GOA agreement: does ProTrek retrieve the function the AIGR review calls
*core*, and at what rank? ([`core_function_recall.py`](PROTREK_EVALUATION/core_function_recall.py))

| Aspect | n | Exact @1 | Exact @3 | Exact @5 | Exact @25 | Any is_a/part_of relation @25 |
|--------|---|----------|----------|----------|-----------|-------------------------------|
| Molecular function | 49 | 6 | 11 | 12 | 19 (39%) | 34 (69%) |
| Biological process | 40 | 1 | 3 | 10 | 13 (33%) | 24 (60%) |
| Cellular component | 42 | 0 | 1 | 2 | 6 (14%) | 20 (48%) |

Molecular function is where ProTrek is strongest and cellular component is where it is weakest —
the opposite of what a localisation-oriented pipeline gives you, and a genuine complementarity.

## Key findings

### 1. The GO channel and the free-text channel are different predictors

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

### 2. Errors are within-family, not random

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

### 3. Pseudoenzymes fail in both models, independently

MTMR9 (missing CX5R catalytic cysteine) drew the same wrong catalytic term — `GO:0004438` — from
ProTrek and ProtNLM2. TBC1D14, shown not to be a Rab-GAP, drew GTPase-activation terms. Auxilin's
degenerate PTEN-like domain drew PTEN's exact reaction three times over. Neither
sequence-similarity retrieval nor seq2seq naming can detect a missing active-site residue; this
needs a separate check, and the GOA IEA annotations for these entries carry the same error, so the
models are reinforcing rather than correcting the record.

### 4. The score is a usable abstention signal — and the only one

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

### 5. The GO index is frozen and has drifted

Of the 150 assessed (top-3) calls, 10 resolve to terms GO has since **obsoleted** and 2 to labels that
no longer resolve at all — 12 (8.0%) could not be entered as annotations even when correct. Across
the full top-5 output the rate is the same: 16 obsolete and 3 unresolved out of 250. The sharpest
case is the tobacco PRORP, where the closest-to-correct call (`endonucleolytic cleavage
involved in tRNA processing`) is obsolete: index staleness, not model error, blocks it. This is a
maintenance property of any retrieval system with a precomputed text index, and it is invisible to
the user.

### 6. It sometimes corrects the record

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

## Reproducibility

All numbers on this page are recomputed from the committed files by scripts in
[`PROTREK_EVALUATION/`](PROTREK_EVALUATION/README.md); none is hard-coded. The retrieval itself needs
the ProTrek weights and SwissProt faiss indexes (several GB, not committed) — the README gives the
download commands. Per-protein assessments live beside each gene as
`genes/<SPECIES>/<ACC>/<ACC>-protrek-predictions-review.yaml`.

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

## Limitations

- **One retrieval mode.** Only `sequence → text` against the SwissProt index was evaluated. ProTrek's
  structure encoder, its larger databases (UniRef50, OMG, MGnify — billions of sequences), and its
  text→sequence direction are untested here. The paper's headline claims concern retrieval quality
  against alignment tools, which this does not measure.
- **The reference is agent-adjudicated, not expert-signed.** The AIGR reviews are the comparison
  standard and carry mixed maturity, as in the [BioReason comparison](BIOREASON_COMPARISON.md).
- **Depth 3 is a choice.** ProTrek has no natural prediction-set boundary. Depth 1 is also reported;
  intermediate depths were not scored.
- **50 proteins, one benchmark.** ARGO-ProtNLM-50 was built to stratify ProtNLM2's behaviour, not
  ProTrek's; it is enriched for unreviewed proteins and for cases chosen as ProtNLM2 case studies.

## References

- [PMID:41039041](https://pubmed.ncbi.nlm.nih.gov/41039041/) — Su J, He Y, You S, et al. *A trimodal protein language model enables advanced protein searches.* Nat Biotechnol 2026
- [ProTrek GitHub](https://github.com/westlake-repl/ProTrek) · [web server](http://search-protrek.com) · [ProTrek_650M weights](https://huggingface.co/westlake-repl/ProTrek_650M) · [faiss indexes](https://huggingface.co/datasets/westlake-repl/faiss_index)
- [ProtNLM2 evaluation](PROTNLM_EVALUATION.md) — the companion evaluation on the same 50 proteins
- [de Crécy-Lagard et al. 2025 (PMID:40703034)](https://pubmed.ncbi.nlm.nih.gov/40703034/) — assessment categories
