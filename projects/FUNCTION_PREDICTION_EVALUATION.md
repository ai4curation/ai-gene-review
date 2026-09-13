---
title: "Function Prediction Evaluation"
maturity: IN_PROGRESS
tags: [EVALUATION, PIPELINE, FLAGSHIP]
autolink_gene_symbols: false
---
# Function Prediction Evaluation

An index to evaluations of computational protein-function predictions, functional
summaries, and annotation-transfer methods in AI Gene Review. Each project provides
its own evidence, review criteria, datasets, and results.

## Model and agent evaluations

| Project | What is evaluated | Explore |
|---------|-------------------|---------|
| **[ProtNLM2](PROTNLM_EVALUATION.md)** | GO predictions across a taxonomically diverse protein benchmark, assessed for biological support, specificity, and overlap with existing annotations. | [Prediction reviews](PROTNLM_EVALUATION/protnlm-eval.html) |
| **[BioReason-Pro and GO-GPT](BIOREASON_COMPARISON.md)** | BioReason-Pro functional summaries and reasoning traces, its SFT GO predictions, and the separate upstream GO-GPT term predictions. | [SFT reviews](BIOREASON_COMPARISON/sft-eval.html) · [GO-GPT reviews](BIOREASON_COMPARISON/gogpt-eval.html) · [Manuscript](BIOREASON_COMPARISON/article/manuscript.pdf) |
| **[DeepECTransformer / E. coli](VALIDATING_ECOLI_PREDICTIONS.md)** | Enzyme-function predictions for selected E. coli proteins, with attention to substrate specificity, paralogs, and physiological context. | [Prediction reviews](BIOREASON_COMPARISON/deepectf-eval.html) · [Recapitulation experiment](BIOREASON_COMPARISON/recapitulation-experiment/claude-expt-1/README.md) |
| **[Affinage](AFFINAGE_EVALUATION.md)** | Literature-derived functional narratives, GO grounding, and retrieval of relevant publications. | [Pilot results](AFFINAGE_EVALUATION/results/summary.md) · [Narrative versus GO analysis](AFFINAGE_EVALUATION/results/narrative-vs-go.md) · [Project findings](AFFINAGE_EVALUATION.md) |

BioReason-Pro SFT, RL narratives, and upstream GO-GPT outputs are separate
evaluation targets. The GO-GPT review includes unresolved predictions; its table
is a review workspace as well as a results browser. The DeepECTransformer table
is hosted with the BioReason comparison material and is also accessible through
the E. coli project.

## Annotation-transfer and rule reviews

These projects examine the methods and mappings behind existing annotations and
provide context for evaluating additional model predictions.

| Project | Focus |
|---------|-------|
| [TreeGrafter](TREEGRAFTER.md) | Automated placement onto PANTHER trees and transfer of ancestral GO annotations. |
| [InterPro2GO](INTERPRO.md) | GO mappings attached to domain and family signatures, including specificity and propagation limits. |
| [NCBIFam](NCBIFam.md) | Functional-family mappings and opportunities or risks in extending GO coverage. |
| [PAINT / IBA](IBA_REVIEW.md) | Curator-assessed phylogenetic function inheritance and the evidence for individual transfers. |
| [ARBA rule reviews](https://ai4curation.io/ai-gene-review/rules/arba/index.html) | Reviews of UniProt's automated annotation rules and their biological scope. |

## Reading the evaluations

Biological correctness, annotation specificity, novelty relative to existing
annotations, and reference quality are distinct questions. The projects use
different cohorts and review procedures, so their scores should be read with
their own methods and denominators. Local AI-assisted reviews also vary in
maturity; they are not automatically independent experimental ground truth.

For the shared approach to term-level review, see the
[evidence standards](PROTNLM_EVALUATION.md#evidence-standards). For narrative
correctness and completeness, see the
[BioReason evaluation rubric](BIOREASON_COMPARISON.md#evaluation-rubric).
