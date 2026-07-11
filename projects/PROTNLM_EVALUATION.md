---
title: ProtNLM2 Evaluation
maturity: COMPLETE
tags: [EVALUATION, ML_PREDICTIONS]
species: [9PRIM, ABRPR, AEDAE, AQUCT, ARAHY, ARATH, ARTAN, ASPOR, BALMU, BORPE, BOVIN, CAEEL, CALMI, CANLF, CHRVO, COLLI, COTJA, CUCME, DANRE, DEIRA, DROPS, DROVI, GADMO, GIBF5, JUGRE, MACFA, MAIZE, MYTGA, ORYSI, ORYSJ, PANPA, PARTE, PHATC, RABIT, SOYBN, STRCO, TAKRU, TOBAC, TRIV3, WHEAT, XANCP, XENNA, XENTR]
genes: [A0A061AL94, A0A1S3BTE3, A0A1S3Y076, A0A2G9RZF1, A0A2I0M3K7, A0A2I4G8T1, A0A2K5UJ34, A0A2R9CAF4, A0A2U1PS28, A0A3B6GK97, A0A3B6NKR6, A0A3B6RKV1, A0A444Z7V7, A0A4W3GVU1, A0A674PKV4, A0A6I8TLE4, A0A6I8W8A2, A0A804UIX9, A0A8B6BFL6, A0A8B6GS20, A0A8B8L1Z3, A0A8B8WEG2, A0A8C2TBA7, A0A8C5FPT8, A0A8C9H4D2, A0A8I3PI07, A0A8J0SCI2, A0A8J1IYX6, A0A8M9QG43, A0BFB4, A2FPI7, B4MAQ2, B7FXQ8, B8BAB0, C6T1A2, D3VIU4, E1BL04, F4JLB7, F6LAX4, F6WPT1, G1TUN6, Q2U1U6, Q6YYC5, Q7NUH2, Q7VZI5, Q8P365, Q9KZ33, Q9L243, Q9RSY6, S0EDH7]
---
# ProtNLM2 Evaluation

Evaluation of Google's ProtNLM2 GO term predictions against expert-curated AIGR gene reviews and existing GOA annotations, using the ARGO-ProtNLM-50 benchmark (50 proteins, 14 taxonomic groups, 75 GO predictions).

**[Interactive prediction evaluation table](PROTNLM_EVALUATION/protnlm-eval.html)** — filterable/sortable HTML view of all 50 proteins and 77 prediction assessments.

**Independent adjudication, both directions.** Predictions were re-tested as blinded, independent
[OpenScientist](https://www.openscientist.io) gene-function hypotheses in two rounds. (1) The
borderline `UNC` calls: **ProtNLM2's localization calls held up (3/3 correct — one even caught a
mis-localized *curated* annotation), while its specific function/process refinements over-reached
(9/14 → `NPI`)**; two were undecidable and kept as leads. (2) Our own **disputed** (`NPI`/`PLI`)
calls: **9 of 10 independently confirmed as misassignments, and 1 caught as over-harsh** —
autophagosome for tbc1d14, which has a direct experimental IDA in the human ortholog, so it was
overturned `NPI → CNN`. See the [OpenScientist adjudication report](PROTNLM_EVALUATION/openscientist-adjudication.md)
for per-gene verdicts and curation leads.

## Key findings

1. **ProtNLM2 is strongest for uncharacterized proteins, but its "novel" hits are mostly InterPro2GO coverage gaps, not new biology**: 12/23 (52%) of NOT_IN_GOA predictions were **likely correct** (domain/orthology-based — no experimental support) and absent from GOA — e.g. DNA binding for a KilA-N domain protein (A2FPI7), ECM organization for OLFML2A (A0A8C9H4D2), nuclear localization for MCM-4 (A0A061AL94). These functions follow directly from the proteins' domains; the standard InterPro2GO pipeline (`GO_REF:0000002`) simply does not emit them, because the relevant domain has no InterPro2GO mapping (olfactomedin, KilA-N), the mapping sits only on a superfamily entry the protein was not assigned (KilA-N → the APSES superfamily IPR036887), or the protein matched only an unintegrated Pfam and never the InterPro entry that carries the mapping (MCM-4 → PF21128, with the rich IPR008047 mapping unassigned). See [InterPro2GO coverage gaps](PROTNLM_EVALUATION/interpro2go-coverage-gaps.md).

2. **"Exact" matches are mostly less precise, not novel**: 13/19 (68%) are parent terms of more specific existing annotations (e.g., predicting "cytoplasm" when "clathrin-coated vesicle" is already annotated). ProtNLM2 captures broad functional categories but lacks resolution.

3. **Frequency bias is the dominant error mode** (13/22 error annotations): the model over-predicts common GO terms (membrane, transferase activity, phosphorylation) without biological specificity, especially problematic for proteins with unusual functions.

4. **Cross-kingdom errors persist despite taxon filtering**: animal-specific terms (neuronal cell body, protein antigen binding) predicted for plant proteins, indicating the Evidencer's taxon constraint checking has gaps.

5. **Paralog discrimination is a weakness**: the model conflates catalytically active and inactive family members (MTMR9 pseudophosphatase, RIC7 lacking kinase domain) — a Type 6 error that sequence similarity methods inherently struggle with.

6. **Expert review substantially revises mechanical assessment**: the automated category mapping (EXACT→CNN, NO_OVERLAP→UNC) was heavily corrected once protein biology was considered (EXACT→LSP, MORE_SPECIFIC→NPI, etc.).

## Aggregate results (75 predictions, 39 proteins)

Assessment categories follow [de Crécy-Lagard et al. 2025 (PMID:40703034)](https://pubmed.ncbi.nlm.nih.gov/40703034/).

| Category | Code | CS | Count | % |
|----------|------|----|-------|---|
| Correct novel | COR | 2 | 17 | 23% |
| Correct not novel | CNN | 2 | 11 | 15% |
| Less precise | LSP | 2 | 18 | 24% |
| Uncertain | UNC | 1 | 13 | 17% |
| Nonparalog incorrect | NPI | 0 | 14 | 19% |
| Paralog incorrect | PLI | 0 | 2 | 3% |
| **Total** | | | **75** | **Mean CS: 1.40/2.0 (70%)** |

**Concordant** (CS=2): 46/75 (61%) | **Uncertain** (CS=1): 13/75 (17%) | **Discordant** (CS=0): 16/75 (21%)

### Results by GOA overlap category

| Match category | n | Dominant assessments |
|----------------|---|---------------------|
| EXACT | 19 | LSP:13, CNN:6 — typically parent terms of existing annotations |
| MORE_SPECIFIC | 6 | CNN:3, NPI:2, UNC:1 — some correctly refine GOA, others overreach |
| LESS_SPECIFIC | 1 | LSP:1 |
| NO_OVERLAP | 26 | NPI:9, UNC:6, COR:5, PLI:2 — novel predictions often wrong |
| NOT_IN_GOA | 23 | COR:12, UNC:6, NPI:3 — best category for genuinely novel discoveries |

### Error analysis (16 incorrect predictions)

| Error type | Count | Examples |
|------------|-------|---------|
| FREQUENCY_BIAS | 13 | Generic "membrane", "transferase activity" for proteins with unusual functions |
| PARALOG_OVERANNOTATION | 4 | Phosphatase activity for catalytically dead MTMR9; kinase activity for RIC7 (no kinase domain) |
| PATHWAY_CONTEXT_IGNORED | 3 | Neuronal/immune terms for plant proteins |
| TRAINING_DATA_CONTAMINATION | 2 | Predictions that reproduce existing IEA annotations |

## Illustrative case studies

These 5 proteins (included in ARGO-50) were identified during exploratory analysis and represent the main error patterns. Each has a full AIGR review (`*-ai-review.yaml`) and prediction assessment (`*-protnlm-predictions-review.yaml`).

### Trivially correct: A0A3B6GK97 (wheat patatin)

ProtNLM2 predicts `lipid catabolic process` > GOA's `lipid metabolic process`. The protein already has IBA annotations for glycerophospholipase + monoacylglycerol lipase activity. In wheat GOA, 94% of proteins with glycerophospholipase activity already have lipid catabolic process annotated. ProtNLM2 is doing bookkeeping, not discovering biology.

### Phmmer transfer: A0A3B6RKV1 (wheat JmjC)

ProtNLM2 predicts 5 specific plant biology terms (gibberellin signaling, photomorphogenesis, seed germination, epigenetic regulation, red light response). All 5 trace to one phmmer hit: Q67XX3 = *Arabidopsis* JMJ22 (score 689.2). This is ISS/ISO-style annotation transfer — the "added value" over IBA is that ProtNLM2 transfers BP annotations that PAINT's more conservative approach chose not to propagate.

### False positive: F4JLB7 (Arabidopsis RIC7)

ProtNLM2 predicts `kinase activity` + `phosphorylation` (score 0.23). The phmmer hit is mouse LRRK2 (score 33, barely above noise) — a 2,527 aa multidomain protein with LRR + ROC + COR + kinase domains. RIC7 only has LRR repeats and is a ROP GTPase effector, not a kinase. Classic multidomain annotation leakage.

### Cross-kingdom error: F6LAX4 (wheat PP2A scaffold)

ProtNLM2 predicts `neuron projection`, `neuronal cell body`, and `protein antigen binding` for a wheat protein. Plants have no neurons and no adaptive immune system. The predictions leak from mammalian PP2A orthologs that are annotated to neuronal compartments. All 6 predictions scored CS=0 (NPI).

### Ontology gap: Q9KZ33 (S. coelicolor sigma factor)

IBA: `sigma factor activity`. ProtNLM2: `transcription initiation`. These are biologically coupled but classified as NO_OVERLAP because there is no is_a/part_of path between "regulation of transcription initiation" (MF ancestry) and "DNA-templated transcription" (BP ancestry). This is a real limitation of closure-based evaluation, not a ProtNLM2 error.

## What is ProtNLM2?

ProtNLM2 is a T5-based seq2seq model developed by Google DeepMind with UniProt, trained on 240M proteins (UniProt 2023_04). It predicts protein names, GO terms, subcellular locations, and function comments from amino acid sequence, organism TaxID, and AlphaFold secondary structure.

Predictions are post-processed by the **Evidencer** — a corroboration pipeline that checks each prediction against string matches, phmmer sequence similarity (bit score > 25), and TM-align structural similarity. Predictions failing GO taxon constraints or lacking corroboration are excluded. See the [UniProt help page](https://www.uniprot.org/help/ProtNLM) for details.

## ARGO-ProtNLM-50 benchmark design

50 proteins curated for systematic evaluation, stratified across:
- 14 taxonomic groups (mammals, plants, bacteria, fish, insects, fungi, etc.)
- 4 prediction categories (rich, partial, go_only, name_only)
- Multiple evidence methods (string match, phmmer, tmalign)
- 5 case studies from exploratory analysis (see above)

All 50 received full AIGR annotation reviews with falcon deep research. The 39 with GO predictions received biologically informed prediction assessments. The 11 name-only proteins have reviews but no prediction-review YAMLs. See [`argo_protnlm_50.csv`](PROTNLM_EVALUATION/argo_protnlm_50.csv).

## Overlap with existing AIGR reviews

Only 8 of 1,334 previously reviewed genes appear in the ProtNLM2 dataset (all TrEMBL/unreviewed): C5AXM3, O94267, Q09490, Q21303, Q86WA8, Q9BZE2, Q9UNW9, Q9XUS3.

## References

- [UniProt ProtNLM help page](https://www.uniprot.org/help/ProtNLM)
- [ProtNLM2 accession list (FTP)](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv)
- [de Crécy-Lagard et al. 2025 (PMID:40703034)](https://pubmed.ncbi.nlm.nih.gov/40703034/) — assessment categories

## Files and methods

| File | Description |
|------|-------------|
| [`argo_protnlm_50.csv`](PROTNLM_EVALUATION/argo_protnlm_50.csv) | Benchmark set of 50 proteins |
| [`protnlm_summary.ipynb`](PROTNLM_EVALUATION/protnlm_summary.ipynb) | Exploratory analysis (full 28K dataset) |
| [`protnlm_bench50_eval.ipynb`](PROTNLM_EVALUATION/protnlm_bench50_eval.ipynb) | ARGO-ProtNLM-50 benchmark evaluation |
| [`fetch_protnlm_api.py`](PROTNLM_EVALUATION/fetch_protnlm_api.py) | REST API fetch pipeline |
| [`protnlm_evaluation_slides.md`](PROTNLM_EVALUATION/protnlm_evaluation_slides.md) | Slide deck (Marp) |
| [OpenScientist adjudication](PROTNLM_EVALUATION/openscientist-adjudication.md) | Per-gene verdicts on the borderline (UNC) predictions + curation leads |
| [InterPro2GO coverage gaps](PROTNLM_EVALUATION/interpro2go-coverage-gaps.md) | Why the "correct novel" hits are missed by standard domain pipelines |
| [Data history](PROTNLM_EVALUATION/data_history.md) | XML vs API data source history |
