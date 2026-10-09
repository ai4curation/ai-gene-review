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
manifest:
  slides:
    - href: FUNCTION_PREDICTION_EVALUATION/slides/FUNCTION_PREDICTION_EVALUATION-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/FWa7DRJiqJvUFZNxGvrErV
      title: Project brief
---
# Function Prediction Evaluation

**Bottom line:** new protein-function predictors appear faster than curators can
judge them, and aggregate benchmarks do not say whether a given method's
predictions are safe to import. This page indexes the AI Gene Review projects
that test such predictions claim by claim against agent-adjudicated gene
reviews, scoring GO terms with the COR/CNN/LSP/UNC/PLI/NPI/REP taxonomy from de
Crécy-Lagard et al. 2025 (PMID:40703034). Across projects the errors concentrate
in specificity, paralogs, pseudoenzymes and organism context. In the largest
model benchmark most correct predictions were already known: as of the review
snapshot (2026-09-27, commit `c7551cb3db`), 682 of 955 BioReason-Pro SFT terms
were correct but not novel and 23 were correct and novel. ProtNLM2's purposive
cohorts invert that balance because they were selected for likely-novel targets.
Affinage's GO layer rarely reached the specific curated function, and reviewers
accepted uncorroborated TreeGrafter inferences much less often than curated
PAINT/IBA ones. Each project below has its own cohorts, methods and denominators.

**[Browse all predictions](../app/predictions/index.html)** — a shared faceted catalog of prediction sets and GO/EC claims, including narrative reviews and assessed empty outputs. Filter by method, species, project, cohort, or assessment; share the resulting URL. [Browser guide](../docs/prediction_browser.md).

The project pages keep their prose to findings and methods; per-category counts
are facet counts in the browser. Useful starting views:
[ARGO95 SFT claims](../app/predictions/index.html?dataset=claims&cohorts=argo95_sft_terms),
[ProtNLM2 GO claims](../app/predictions/index.html?dataset=claims&source_method=ProtNLM2),
[DeepECTF claims](../app/predictions/index.html?dataset=claims&source_method=DeepECTF), and the
[GO-GPT three-level overlap](../app/predictions/index.html?dataset=overlap), which is fixed at the review snapshot.

**[Cross-project review (2026-09-26)](FUNCTION_PREDICTION_EVALUATION/REVIEW-2026-09-26.md)** — consistency, independence, and reproducibility audit of the evaluations below, with prioritized fixes.

## Model and agent evaluations

| Project | What is evaluated | Explore |
|---------|-------------------|---------|
| **[ProtNLM2](PROTNLM_EVALUATION.md)** | GO predictions across a taxonomically diverse protein benchmark, assessed for biological support, specificity, and overlap with existing annotations. | [Prediction reviews](PROTNLM_EVALUATION/protnlm-eval.html) |
| **[BioReason-Pro and GO-GPT](BIOREASON_COMPARISON.md)** | BioReason-Pro functional summaries and reasoning traces, its SFT GO predictions, and the separate upstream GO-GPT term predictions. | [SFT reviews](BIOREASON_COMPARISON/sft-eval.html) · [GO-GPT reviews](BIOREASON_COMPARISON/gogpt-eval.html) · [Manuscript](BIOREASON_COMPARISON/article/manuscript.pdf) |
| **[DeepECTransformer / E. coli](VALIDATING_ECOLI_PREDICTIONS.md)** | Enzyme-function predictions for selected E. coli proteins, with attention to substrate specificity, paralogs, and physiological context. | [Prediction reviews](VALIDATING_ECOLI_PREDICTIONS/deepectf-eval.html) · [Blinded recapitulation](BIOREASON_COMPARISON/recapitulation-experiment/claude-expt-1/README.md) ([table](BIOREASON_COMPARISON/deepectf-eval.html); 4/7 match) |
| **[Affinage](AFFINAGE_EVALUATION.md)** | Literature-derived functional narratives, GO grounding, and retrieval of relevant publications. | [Pilot results](AFFINAGE_EVALUATION/results/summary.md) · [Narrative versus GO analysis](AFFINAGE_EVALUATION/results/narrative-vs-go.md) · [Project findings](AFFINAGE_EVALUATION.md) |
| **[Structure-based prediction](STRUCTURE_FUNCTION.md)** | Fold, active-site and structure-aware learned methods for distant homologs, tested against cases from existing reviews. | [Project page](STRUCTURE_FUNCTION.md) |
| **[OpenScientist co-scientist](COSCIENTIST.md)** | An autonomous research agent used as an independent bioinformatician to test gene-function hypotheses; its verdicts also serve as adjudicators in the ProtNLM2 and TreeGrafter evaluations. | [Project page](COSCIENTIST.md) |
| **[Prokaryotic immunity term prediction](PROKARYOTIC_IMMUNITY_TERM_PREDICTION.md)** | Scoping: translating family-level defense-system calls into review-ready GO term suggestions. | [Project page](PROKARYOTIC_IMMUNITY_TERM_PREDICTION.md) |

BioReason-Pro SFT, RL narratives, and upstream GO-GPT outputs are separate
evaluation targets. The GO-GPT review includes unresolved predictions; its table
is a review workspace as well as a results browser. DeepECTransformer has two
tables: the project's own calls (rendered from `genes/ECOLI/*/*-det-predictions-review.yaml`,
the same records shown in the prediction browser) and a blinded recapitulation run,
hosted with the BioReason comparison material, whose calls match the published
expert labels for only 4 of the 7 genes.

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
| [UniProt keywords (SPKW)](SPKW.md) | Annotations derived only from UniProt keyword mappings (`GO_REF:0000043`) and their over-annotation patterns. |
| [Pfam → GO](PFAM.md) | Whether pfam2go adds specificity beyond InterPro2GO, and headroom for new family mappings. |
| [Rhea → GO](RHEA.md) | What rhea2go contributes beyond ec2go, and reactions with no GO target. |
| [TCDB → GO](TCDB.md) | Transporter classifications that never become GO annotations, and candidate TC-to-GO mappings. |
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
