---
title: ProtNLM2 Evaluation
maturity: COMPLETE
tags: [EVALUATION, ML_PREDICTIONS]
species: [9PRIM, ABRPR, AEDAE, AQUCT, ARAHY, ARATH, ARTAN, ASPOR, BALMU, BORPE, BOVIN, CAEEL, CALMI, CANLF, CHRVO, COLLI, COTJA, CUCME, DANRE, DEIRA, DROPS, DROVI, GADMO, GIBF5, JUGRE, MACFA, MAIZE, MYTGA, ORYSI, ORYSJ, PANPA, PARTE, PHATC, RABIT, SOYBN, STRCO, TAKRU, TOBAC, TRIV3, WHEAT, XANCP, XENNA, XENTR]
genes: [A0A061AL94, A0A1S3BTE3, A0A1S3Y076, A0A2G9RZF1, A0A2I0M3K7, A0A2I4G8T1, A0A2K5UJ34, A0A2R9CAF4, A0A2U1PS28, A0A3B6GK97, A0A3B6NKR6, A0A3B6RKV1, A0A444Z7V7, A0A4W3GVU1, A0A674PKV4, A0A6I8TLE4, A0A6I8W8A2, A0A804UIX9, A0A8B6BFL6, A0A8B6GS20, A0A8B8L1Z3, A0A8B8WEG2, A0A8C2TBA7, A0A8C5FPT8, A0A8C9H4D2, A0A8I3PI07, A0A8J0SCI2, A0A8J1IYX6, A0A8M9QG43, A0BFB4, A2FPI7, B4MAQ2, B7FXQ8, B8BAB0, C6T1A2, D3VIU4, E1BL04, F4JLB7, F6LAX4, F6WPT1, G1TUN6, Q2U1U6, Q6YYC5, Q7NUH2, Q7VZI5, Q8P365, Q9KZ33, Q9L243, Q9RSY6, S0EDH7]
---
# ProtNLM2 Evaluation

[Function prediction evaluation index](FUNCTION_PREDICTION_EVALUATION.md)

Evaluation of Google's ProtNLM2 GO term predictions using the ARGO-ProtNLM-50 benchmark: **50 protein records across 14 taxonomic groups, 41 with GO predictions, and 77 prediction assessments**. The evaluation assesses biological support, annotation specificity, and overlap with existing GOA annotations. Nine records have empty GO prediction lists.

**[Interactive prediction evaluation table](PROTNLM_EVALUATION/protnlm-eval.html)** — filterable/sortable assessments, rationales, and links to all 50 protein reviews.

**Independent adjudication, both directions.** Focused [OpenScientist](https://www.openscientist.io) investigations evaluate both uncertain predictions and predictions disputed by the review. Their integration of sequence, structure, comparative biology, and literature provides substantial evidence for adjudication. Examples include the missing kinase domain in ARATH/F4JLB7 and experimental autophagosome localization in the human ortholog of GADMO/A0A8C5FPT8. See the [OpenScientist investigation report](PROTNLM_EVALUATION/openscientist-adjudication.md) for the individual investigations and their findings.

## Key findings

1. **Useful additional annotations can follow from established biology and mapping gaps.** Supported family transfers include chloroplastic EF4 localization for ARTAN/A0A2U1PS28 and a laterality role for MACFA/A0A2K5UJ34. The [InterPro2GO coverage analysis](PROTNLM_EVALUATION/interpro2go-coverage-gaps.md) identifies absent mappings, mappings on unassigned superfamily entries, and unintegrated Pfam signatures as routes by which plausible functions can be absent from GOA. A mapping gap alone does not establish the predicted function: nuclear localization for the 74-residue CAEEL/A0A061AL94 record remains uncertain. Matrix organization for 9PRIM/A0A8C9H4D2 is supported by an experimentally grounded mouse OLFML2A annotation, providing a basis for ortholog transfer beyond localization alone.

2. **Exact matches often lack specificity.** Of the 19 predictions classified as EXACT in the GOA comparison, 13 are LSP and six are CNN. The predicted term can already be present while a more informative, supported annotation is also available.

3. **Catalytic-domain completeness matters.** Shared domains or family membership can support an inference while missing catalytic regions contradict a specific activity. The wheat patatin and Arabidopsis LRR protein below illustrate why the deposited sequence needs to be examined.

4. **Cross-kingdom localization errors occur.** Neuronal cell body and neuron projection are incompatible with wheat F6LAX4. Its other predictions require separate assessment: protein antigen binding is not restricted to adaptive immunity, and heterodimerization is supported by the conserved PP2A core complex.

5. **Core functions transfer more readily than regulatory context.** JMJ22-related sequence and experimental evidence support epigenetic regulation for WHEAT/A0A3B6RKV1, while its four specific light, hormone, and germination predictions remain uncertain. For COLLI/A0A2I0M3K7, TRUB2 family membership does not establish the predicted tRNA substrate.

6. **Biological assessment adds information beyond ontology overlap.** Sigma-factor activity supports transcription initiation even when an is_a/part_of comparison reports NO_OVERLAP. Conversely, matching an existing annotation does not override target-specific contrary evidence.

## Aggregate results

Assessment categories follow [de Crécy-Lagard et al. 2025 (PMID:40703034)](https://pubmed.ncbi.nlm.nih.gov/40703034/), with the project's GO prediction guidelines.

| Category | Code | CS | Count | Percentage |
|----------|------|----|-------|------------|
| Correct novel | COR | 2 | 19 | 24.7% |
| Correct not novel | CNN | 2 | 8 | 10.4% |
| Less precise | LSP | 2 | 13 | 16.9% |
| Uncertain | UNC | 1 | 30 | 39.0% |
| Nonparalog incorrect | NPI | 0 | 7 | 9.1% |
| Paralog incorrect | PLI | 0 | 0 | 0.0% |
| Repetition | REP | 0 | 0 | 0.0% |
| **Total** | | | **77** | **100%** |

**Supported:** 40/77 (51.9%). **Uncertain:** 30/77 (39.0%). **Contradicted:** 7/77 (9.1%). The mean assessment score is **110/77 = 1.43 out of 2**. This ordinal score is not a calibrated estimate of model accuracy. The stratified sample is small, and many proteins lack direct experimental characterization.

### Results by GOA overlap category

The [closure-based GOA comparison](PROTNLM_EVALUATION/bench50_evaluation_results.csv) classifies annotation overlap for 75 predictions. The table below joins those categories to the current biological assessments by accession and GO term; two additional reviewed predictions have no row in that comparison. Overlap categories describe the comparison dataset, while assessment categories express biological judgments.

| Match category | n | Current assessments |
|----------------|---|---------------------|
| EXACT | 19 | CNN: 6, LSP: 13 |
| MORE_SPECIFIC | 6 | COR: 2, UNC: 4 |
| LESS_SPECIFIC | 1 | NPI: 1 |
| NO_OVERLAP | 26 | COR: 10, UNC: 11, NPI: 5 |
| NOT_IN_GOA | 23 | COR: 7, UNC: 15, NPI: 1 |
| Not in overlap snapshot | 2 | CNN: 2 |

**Total: 77 predictions.** An exact match can still be less precise than another supported annotation on the same protein; no ontology overlap can still accompany a sound biological inference across GO aspects.

### Error analysis (7 incorrect predictions)

| Biological contradiction | Count | Examples |
|--------------------------|-------|----------|
| Neuronal localization in a plant | 2 | Neuronal cell body and neuron projection for WHEAT/F6LAX4 |
| Intrinsic activity incompatible with the deposited sequence or domain architecture | 5 | Kinase activity for ARATH/F4JLB7; ligase activity for the short RCC1-like DROPS/A0A6I8W8A2 record; PI3P phosphatase activity for MYTGA/A0A8B6GS20; lipase activity for WHEAT/A0A3B6GK97; ligand-gated channel activity for XENNA/D3VIU4 |

These seven predictions are assessed as NPI. The table groups biological contradictions; it does not infer a model error mechanism where the optional `error_type` field is unset. The evidence identifies biological incompatibilities; frequency bias and training-data contamination are not established as their causes.

## Illustrative case studies

These five proteins, included in ARGO-50, illustrate annotation transfer, catalytic-domain checks, taxonomic constraints, and limitations of ontology-based evaluation. Each has a full AIGR gene review and a separate ProtNLM prediction assessment.

### Catalytic-region check: A0A3B6GK97 (wheat patatin)

ProtNLM2 predicts `lipase activity` and `lipid catabolic process` for WHEAT/A0A3B6GK97. Existing IBA annotations include more specific lipase activities, making the process prediction look like a straightforward extension of known biology. However, the reproducible alignment and motif analysis show that the deposited 302-residue sequence lacks the patatin catalytic-serine region. **Lipase activity is NPI; lipid catabolic process is UNC.** The sequence may reflect an incomplete gene model or an inactive protein; neither a corrected full-length product nor a noncatalytic role in lipid catabolism is established. This case shows why annotation overlap alone cannot settle correctness.

### Phmmer transfer: A0A3B6RKV1 (wheat JmjC)

ProtNLM2 predicts five plant biology terms for WHEAT/A0A3B6RKV1: gibberellin signaling, photomorphogenesis, seed germination, epigenetic regulation, and red-light response. The corroboration records identify *Arabidopsis* JMJ22 (Q67XX3; phmmer score 689.2), which has experimental annotations for all five terms. This provides a concrete basis for examining transfer from a characterized relative. **Epigenetic regulation is COR**, supported by the JMJ22 relationship and histone-arginine-demethylation evidence. **The four specific regulatory/process predictions are UNC** because their Arabidopsis experimental contexts do not establish the same roles in wheat. The phmmer hit is corroborating evidence; it does not reveal how the model generated its predictions or why PAINT omitted a term.

### False positive: F4JLB7 (Arabidopsis LRR protein)

ProtNLM2 predicts `kinase activity` and `phosphorylation` for ARATH/F4JLB7. The exploratory analysis identifies a weak phmmer corroboration hit to mouse LRRK2 (score 33), a multidomain protein containing LRR and kinase regions. Sharing an LRR region does not establish kinase catalysis. The focused OpenScientist investigation integrates LRR domain assignments, catalytic-motif analysis, and predicted structure to refute a kinase domain in F4JLB7. **Kinase activity is NPI; phosphorylation is UNC**, since participation through another protein remains possible. The RIC7 name in the database record does not establish that this LRR protein is the CRIB-domain ROP effector described in RIC7 literature.

### Cross-kingdom error: F6LAX4 (wheat PP2A scaffold)

ProtNLM2 predicts `neuron projection` and `neuronal cell body` for WHEAT/F6LAX4. Wheat has no neurons, so **both localizations are NPI**. The remaining predictions have different evidential standing: **protein heterodimerization is COR**, supported by the PP2A A-C core complex; **chromosome segregation, centromeric localization, and protein antigen binding are UNC**. Protein antigen binding is not an animal-specific function by definition, but binding of the viral small-t antigen inhibitor to human PP2A A scaffolds does not establish antigen-recognition activity. There is no positive evidence for that activity in this wheat protein. This example separates clear taxonomic errors from plausible but unverified transfers.

### Ontology gap: Q9KZ33 (S. coelicolor sigma factor)

STRCO/Q9KZ33 has an IBA annotation for `sigma factor activity`; ProtNLM2 predicts `DNA-templated transcription initiation`. The closure-based GOA comparison classifies the prediction as NO_OVERLAP. The molecular activity and biological process are nevertheless functionally connected: an ECF sigma factor supports promoter recognition and transcription initiation. **The prediction is COR**, adding a supported process annotation absent from the cached record. This illustrates a limitation of evaluating biological agreement solely through is_a/part_of paths across GO aspects.

## What is ProtNLM2?

ProtNLM2 is a transformer-based sequence-to-sequence model developed by Google DeepMind with UniProt, trained on 240 million protein entries from UniProt release 2023_04. It generates protein names, GO terms, subcellular locations, keywords, and function comments from amino acid sequence. UniProt describes the current model as trained entirely on sequence. See the [UniProt ProtNLM documentation](https://www.uniprot.org/help/ProtNLM).

Predictions are post-processed by the **Evidencer**, which applies exclusion criteria including GO taxon constraints and seeks corroboration through string matches, phmmer sequence similarity (bit score greater than 25), and TM-align structural similarity. This corroboration can explain the biological source of support for a prediction, but it is separate from the neural model's generation of that prediction. The exploratory XML dataset and public release differ in coverage; the [data provenance](PROTNLM_EVALUATION/data_history.md) describes the source versions used here.

## ARGO-ProtNLM-50 benchmark design

ARGO-ProtNLM-50 was constructed **after the ProtNLM release**, rather than specified in advance as a benchmark for the model. ProtNLM predictions were released for a partly arbitrary set of proteins, mostly unreviewed/TrEMBL entries. We then selected 50 proteins from that available set to sample different species and kinds of annotations. The resulting benchmark is an exploratory, stratified sample, not a prospective test set or a random sample of protein space.

The selection covers:

- 14 taxonomic groups, including mammals, plants, bacteria, fish, insects, and fungi.
- Four prediction categories: rich, partial, GO-only, and name-only.
- Multiple corroboration methods: string match, phmmer, and TM-align.
- Five case studies from exploratory analysis, described above.

All 50 proteins have AIGR gene reviews and prediction-review YAMLs. The 41 records with GO predictions contribute 77 assessments; nine prediction lists are empty. The [benchmark CSV](PROTNLM_EVALUATION/argo_protnlm_50.csv) records selection metadata. Each protein's `*-protnlm-predictions-review.yaml` preserves the prediction and source-method metadata alongside its assessment, rationale, and supporting sources.

## Overlap with existing AIGR reviews

The exploratory comparison against the 1,334-review AIGR collection found eight proteins in the ProtNLM2 dataset, all unreviewed/TrEMBL entries: C5AXM3, O94267, Q09490, Q21303, Q86WA8, Q9BZE2, Q9UNW9, and Q9XUS3. This is the comparison set used in the exploratory analysis, rather than a count of the expanding AIGR collection; ARGO-50 provides a broader dedicated evaluation sample.

## Evidence standards

Prediction sidecars are checked with `just validate-predictions`, including publication titles, source excerpts, local paths, and assessment scores. The CI artifact `prediction-evidence-validation` records those checks.

The [function-prediction review skill](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/review-function-prediction/SKILL.md) defines the review criteria. Assessments integrate primary literature, sequence and domain evidence, structural analyses, experimentally grounded curated annotations, and focused OpenScientist investigations. These investigations synthesize multiple lines of evidence and carry substantial weight when their findings address the prediction. Reviews cite the relevant analyses and their limitations, distinguishing computational inference from experimental validation. A well-supported family transfer can establish a reasonable function or localization inference without a new experiment on every target; the rationale identifies the characterized relative, the target's family evidence, and the limits of transfer.

Each prediction is assessed at the specificity of its actual GO term. Extracellular localization does not establish matrix organization, and a catalytic fold does not establish a substrate. Conversely, absence of intrinsic catalytic activity does not exclude participation in the corresponding biological process through a regulatory complex. Missing evidence leads to uncertainty unless there is contrary evidence. Broad but true annotations are not biological errors.

COR and CNN distinguish absence versus presence of an equivalent annotation in the **target's cached GOA/UniProt records**, after biological support has been established. LSP requires an existing, supported, more specific annotation. These labels do not establish whether an example was in the model's training data. The assessment uses the available evidence, including studies published after the prediction release; it is not a time-restricted prospective benchmark.

## References

- [UniProt ProtNLM help page](https://www.uniprot.org/help/ProtNLM) — model and Evidencer documentation.
- [ProtNLM2 accession list](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv) — public release coverage.
- [de Crécy-Lagard et al. 2025 (PMID:40703034)](https://pubmed.ncbi.nlm.nih.gov/40703034/) — assessment categories.

## Files and methods

| Resource | Role |
|----------|------|
| [Benchmark CSV](PROTNLM_EVALUATION/argo_protnlm_50.csv) | Sampling metadata for all 50 proteins |
| [GOA overlap comparison](PROTNLM_EVALUATION/bench50_evaluation_results.csv) | Closure-based comparison for 75 predictions |
| [Prediction evaluation table](PROTNLM_EVALUATION/protnlm-eval.html) | Current 77 GO assessments across all 50 records |
| [UniProt ProtNLM documentation](https://www.uniprot.org/help/ProtNLM) | Prediction method and corroboration pipeline |
| [REST API fetch pipeline](PROTNLM_EVALUATION/fetch_protnlm_api.py) | Retrieval of raw prediction and corroboration records |
| [Exploratory notebook](PROTNLM_EVALUATION/protnlm_summary.ipynb) | Dataset exploration |
| [Benchmark notebook](PROTNLM_EVALUATION/protnlm_bench50_eval.ipynb) | Benchmark overlap analysis |
| [Slide deck](PROTNLM_EVALUATION/protnlm_evaluation_slides.md) | Exploratory presentation; assessment totals and case judgments on this page reflect the current reviews |
| [OpenScientist investigation report](PROTNLM_EVALUATION/openscientist-adjudication.md) | Focused investigations integrating multiple lines of evidence to inform prediction assessments |
| [InterPro2GO coverage analysis](PROTNLM_EVALUATION/interpro2go-coverage-gaps.md) | Domain-to-GO mapping coverage across the benchmark |
| [Data history](PROTNLM_EVALUATION/data_history.md) | XML/API source provenance |
