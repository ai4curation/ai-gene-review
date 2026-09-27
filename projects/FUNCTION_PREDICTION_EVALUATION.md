---
title: "Function Prediction Evaluation"
maturity: IN_PROGRESS
tags: [EVALUATION, PIPELINE, FLAGSHIP]
autolink_gene_symbols: false
sidecars:
  # Deck images: copied beside the rendered deck so its relative <img> paths resolve.
  slide_images:
    - FUNCTION_PREDICTION_EVALUATION/slides/evaluation-loop.svg
    - FUNCTION_PREDICTION_EVALUATION/slides/prediction-results.svg
---
# Function Prediction Evaluation

**Bottom line:** new protein-function predictors appear faster than curators can
judge them, and aggregate benchmarks do not say whether a given method's
predictions are safe to import. This page indexes the AI Gene Review projects
that test such predictions claim by claim against agent-adjudicated gene
reviews, scoring GO terms with the COR/CNN/LSP/UNC/PLI/NPI/REP taxonomy from de
Crécy-Lagard et al. 2025 (PMID:40703034). Across projects the errors concentrate
in specificity, paralogs, pseudoenzymes and organism context, and in the larger
model benchmarks most correct predictions were already known: 682 of 955
BioReason-Pro SFT terms were correct but not novel and 23 were correct and novel
(ProtNLM2's purposive cohorts give 53 COR and 32 CNN of 288 GO terms). Affinage's GO layer reached
the specific curated function for 1 of 42 genes, and reviewers accepted 41% of uncorroborated TreeGrafter inferences
against 72% of curated PAINT/IBA ones. Each project below has its own cohorts,
methods and denominators.

**[Browse all predictions](../app/predictions/index.html)** — a shared faceted catalog of prediction sets and GO/EC claims, including narrative reviews and assessed empty outputs. Filter by method, species, project, cohort, or assessment; share the resulting URL. [Browser guide](../docs/prediction_browser.md).

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
provide context for evaluating additional model predictions. Transfers by
orthology, phylogeny, and family membership have their own index,
[Propagation by Homology](HOMOLOGY_PROPAGATION.md), with a
[browser of all propagated annotations](../app/propagation/index.html).

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

## Slides

- [Slides](FUNCTION_PREDICTION_EVALUATION/slides/FUNCTION_PREDICTION_EVALUATION-slides.html) (Marp source: [FUNCTION_PREDICTION_EVALUATION-slides.md](FUNCTION_PREDICTION_EVALUATION/slides/FUNCTION_PREDICTION_EVALUATION-slides.md)) — AI generated
