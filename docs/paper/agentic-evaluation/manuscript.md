# Agentic Evaluation of AI Methods for Protein Function Prediction

## Abstract

Benchmarks for protein function prediction typically summarize performance with aggregate term-level metrics such as precision, recall, and F1. These measures are valuable, but they do not explain what kinds of biological mistakes a model makes, whether a prediction is genuinely informative to curators, or whether a fluent narrative output merely restates existing domain-based priors. Here we introduce **agentic evaluation** as a complementary framework for assessing AI methods for protein function prediction. Our approach uses AI Gene Review (AIGR), a structured literature-grounded curation system, to audit model outputs against curated gene reviews, supporting references, and existing annotation sources. We focus on foundation-model-based methods, especially BioReason-Pro and its upstream GO-GPT predictor, and compare them with established non-foundation-model pipelines including ARBA and orthology-based transfer. As an anchor dataset, we use a 139-gene BioReason comparison set spanning multiple taxa together with a seven-gene *Escherichia coli* benchmark derived from a published machine-learning error taxonomy. Agentic evaluation recovers published error classes such as paralog overannotation, pathway-context blindness, and frequency bias, and further reveals curator-relevant failure modes not captured by scalar metrics, including localization defaults, pseudoenzyme blindness, organism-specific context loss, narrative-annotation mismatch, and propagation of misleading family labels. These results suggest that agentic evaluation can complement CAFA-style benchmarking by turning model disagreement into an interpretable failure taxonomy that is actionable for both model developers and biocurators.

## Introduction

### Why scalar benchmarking is not enough

Protein function prediction is usually evaluated as an annotation overlap problem. In community benchmarks such as CAFA, predicted functions are compared with reference annotations and summarized using aggregate measures such as precision, recall, and F1 [doi:10.1007/978-1-4939-3743-1_10]. This evaluation style is useful because it is scalable, quantitative, and comparable across methods. It is also incomplete.

Two models with similar F1 can fail in qualitatively different ways. One may predict a close parent term where a child term is warranted; another may assign an impossible function because it ignores pathway context. A reasoning model may generate a fluent and mostly plausible paragraph while quietly confusing a periplasmic chaperone for a cytoplasmic stress protein. Another model may achieve respectable overlap with existing annotations simply by reproducing common training-set labels or by restating domain-to-function mappings already available through InterPro2GO. Scalar benchmarks compress these differences into a single number.

For curator-facing applications, that compression is a problem. Biocurators do not merely need to know whether a model overlaps existing annotations. They need to know whether the model:

- identifies the right molecular activity for the right biological reason,
- distinguishes paralogs with different substrate or pathway roles,
- respects cellular compartment and membrane topology,
- handles pseudoenzymes and moonlighting proteins correctly,
- preserves organism-specific biology, and
- adds value beyond pre-existing automated annotation pipelines.

### Agentic evaluation as a complementary framework

We use the term **agentic evaluation** to describe a review process in which an AI system actively inspects a model output, compares it with curated evidence, identifies the likely source of disagreement, and records a structured judgment rather than only a scalar score. In our setting, the evaluator is AIGR, a literature-grounded curation framework that integrates existing GO annotations, cached publications, computational evidence, and explicit review actions such as `ACCEPT`, `MODIFY`, `REMOVE`, and `MARK_AS_OVER_ANNOTATED`.

This is not intended as a replacement for benchmark evaluation. Instead, the goal is to augment it. CAFA-style metrics answer questions such as: *How often does a method match current annotations?* Agentic evaluation answers different questions: *Why did a model fail? Is the failure biologically benign or curator-critical? Did the model add useful reasoning beyond an existing pipeline, or did it simply produce a polished restatement of prior annotations?*

### Foundation models need richer evaluation

These questions are especially important for foundation-model-based methods. Unlike earlier pipelines that output only GO terms or EC numbers, recent models may produce:

- high-recall term predictions from sequence models,
- natural-language reasoning traces,
- free-text functional summaries,
- mixed outputs combining structured and unstructured claims.

This richer output space creates new opportunities and new failure modes. A model can be directionally correct in prose while wrong in formal annotation. It can explain a protein family well at a generic level while missing the decisive gene-specific feature. It can appear insightful while merely laundering existing InterPro or family labels into fluent biological language. These behaviors are difficult to diagnose with term-level overlap alone.

In this manuscript we argue that agentic evaluation provides a practical way to expose those gaps.

### Position relative to recent literature

Two recent lines of work motivate this manuscript. First, the published BioReason paper argues that biological AI systems should be evaluated not only as predictors but as **reasoning systems**, with multimodal inputs and step-by-step mechanistic explanations treated as first-class outputs rather than post hoc justifications [arXiv:2505.23579]. That paper is an important signal that richer reasoning traces are becoming part of the model interface. At the same time, its published evaluation is centered on genomic reasoning tasks such as KEGG-derived disease pathway and variant-effect prediction rather than on GO-style protein function annotation [arXiv:2505.23579].

Second, de Crécy-Lagard et al. performed expert review of more than 450 machine-learning-based EC predictions for *E. coli* proteins of unknown function and showed that current systems still make basic logic errors, including paralog overannotation, context-blind pathway assignments, and predictions that are chemically plausible in vitro but unsupported in vivo [PMID:40703034]. That study provides a strong precedent for qualitative, curator-driven error analysis rather than sole reliance on aggregate benchmark metrics.

Our manuscript sits between these two positions. BioReason motivates evaluation of **reasoning-rich biological AI**, while de Crécy-Lagard et al. motivate evaluation of **logic-sensitive biological validity**. Agentic evaluation connects these ideas by asking not only whether a model output overlaps a reference annotation set, but also whether the reasoning it presents is biologically coherent, curator-useful, and distinct from pre-existing automated annotation priors.

## Study Design

### Systems examined

The primary focus of this paper is the evaluation of AI methods, especially foundation-model-based systems for protein function prediction.

The main systems considered are:

1. **GO-GPT**, the sequence-based upstream predictor used in the BioReason-Pro pipeline.
2. **BioReason-Pro**, the protein-function system evaluated in this repository, which combines GO-GPT predictions with InterPro and other contextual inputs to generate functional summaries and reasoning traces [doi:10.64898/2026.03.19.712954]. Conceptually, this system is aligned with the broader BioReason agenda of multimodal biological reasoning, but its evaluation setting here is protein function prediction rather than the genomic reasoning tasks emphasized in the published BioReason paper [arXiv:2505.23579].
3. **DeepECTF**, evaluated here through a curated *E. coli* benchmark based on the published analysis of de Crécy-Lagard et al. [PMID:40703034].
4. **ARBA**, a UniProt automated annotation system that generates human-readable rules and propagates annotations to UniProtKB/TrEMBL proteins [GO_REF:0000117].
5. **ISO/orthology transfer**, used as a contrast class for annotation transfer based on sequence orthology [GO_REF:0000008, GO_REF:0000107].

Although ARBA and ISO are not foundation models, they are important comparators because they highlight what kinds of errors are shared across generations of automated annotation systems and what kinds are distinctive to foundation-model-based reasoning.

### Reference framework

The reference standard in this work is not a single static label set. Instead, we use AIGR gene reviews as structured, evidence-linked audit records. Each review integrates:

- existing GO annotations,
- literature-derived supporting statements,
- curation judgments for each annotation,
- core-function summaries,
- proposed replacement terms where appropriate.

This matters because the paper is not only about agreement with existing annotations. It is about whether a method produces claims that withstand curator-style scrutiny.

### Datasets used in this first draft

This manuscript draft is centered on three sources already present in the repository:

1. **BioReason comparison set**  
   A 139-gene evaluation set spanning bacteria, fungi, plants, worms, flies, and mammals. Each gene has a curated AIGR review and a BioReason-Pro RL review with correctness and completeness scores.

2. ***E. coli* ML prediction validation set**  
   A seven-gene benchmark assembled from de Crécy-Lagard et al. (2025), spanning published error categories including correct novel, paralog incorrect, non-paralog incorrect, repetition/frequency bias, and uncertain predictions [PMID:40703034].

3. **Computational pipeline case studies**  
   ARBA rule reviews and ISO-bearing gene reviews are used as contrastive examples showing how agentic evaluation can audit rule-based propagation and orthology transfer in addition to foundation-model outputs.

The first draft emphasizes the first two datasets because they already provide the clearest bridge between published error taxonomies and the richer failure taxonomy revealed by agentic review.

## From Benchmark Scores to Failure Taxonomy

### A layered view of evaluation

We propose thinking about evaluation in three layers:

1. **Scalar benchmarking**  
   Did the method overlap the reference annotation set?

2. **Published task-specific error classes**  
   If not, what broad category of error occurred? For example, paralog confusion or pathway-context failure.

3. **Agentic biological audit**  
   What was the specific biological misunderstanding? Was the model fooled by a misleading family label, did it ignore a signal peptide, did it over-transfer a function from an ortholog, or did it collapse two distinct paralogs into one generic family narrative?

This paper focuses on the third layer, while explicitly treating the first two as important but insufficient.

## Published Error Classes Recoverable by Agentic Evaluation

The *E. coli* validation project is especially useful because it starts from an external, published taxonomy rather than one invented post hoc for our own system [PMID:40703034]. AIGR review recovers these categories cleanly and makes them biologically interpretable.

| Published class | Meaning in de Crécy-Lagard et al. | Example in this repo | Agentic interpretation |
|---|---|---|---|
| `CNN` | Prediction reproduces known annotation rather than contributing novelty | Present in the source taxonomy, not emphasized in current seven-gene set | Useful for distinguishing novelty from memorization or label recapitulation |
| `COR` | Correct novel prediction | `ygfF` | Rare category; useful positive control showing that agentic review can recognize genuine novelty |
| `LSP` | Less precise than existing annotation | General pattern seen in many automated term assignments | Scalar metrics may partly reward this, but agentic review exposes specificity loss |
| `PLI` | Paralog incorrect | `yciO`, `yegV` | Model recognizes a broad family correctly but assigns the wrong subfamily or substrate-specific activity |
| `NPI` | Non-paralog incorrect | `yjhQ`, `yrhB` | Model predicts a chemically plausible function that is biologically impossible in organism/pathway context |
| `REP` | Repetition / frequency bias | `fepE` | Model defaults to a frequent training label without sequence- or mechanism-level justification |
| `UNC` | Uncertain | `yjdM` | Useful category for separating unsupported novelty from clearly wrong claims |

This mapping is already more informative than raw correctness alone. But the agentic review layer goes further by identifying the mechanism of failure.

## Agentic Failure Taxonomy

### Overview

Across the BioReason comparison set, the *E. coli* ML validation set, and the computational pipeline case studies, several recurring failure modes emerge. Some align with existing ML taxonomies; others are mostly invisible to scalar benchmarks.

| Failure category | Description | Representative examples | Systems where prominent |
|---|---|---|---|
| **Training-set recapitulation / non-novel output** | Output looks plausible because it reproduces existing label priors rather than providing new biological insight | `CNN` class in the published *E. coli* taxonomy | Deep learning classifiers, high-recall term predictors |
| **Specificity error** | Prediction is too broad, too narrow, or at the wrong granularity | generic binding/process terms; less-precise labels | GO-GPT, ARBA, orthology transfer |
| **Paralog conflation** | Correct family identified, wrong paralog-specific function assigned | `yciO`, `yegV`; Fyn vs Src; sporulation sigma factors | DeepECTF, BioReason, orthology transfer |
| **Pathway-context blindness** | Prediction is chemically plausible but impossible given organismal or genomic context | `yjhQ`, `yrhB` | Sequence-only or family-heavy predictors |
| **Frequency bias** | Model defaults to common high-frequency labels when evidence is weak | `fepE` predicted as histidine kinase | Classifiers trained on imbalanced labels |
| **Localization default** | Model falls back to cytoplasm or another default compartment when topology/export cues are missed | Skp, CpxP, Spy, mrdA | BioReason and related narrative systems |
| **Pseudoenzyme / catalytic-state error** | Conserved fold treated as active enzyme despite catalytic degeneration or functional divergence | Epe1, pmp20, RidA narrative ambiguity | Foundation-model reasoning and domain-based propagation |
| **Narrative-annotation mismatch** | Prose is approximately right but structured term choice is wrong, generic, or contradictory | RidA, CpxP, Spy | Foundation-model systems combining language and term outputs |
| **Organism-specific context loss** | Generic family biology replaces lineage-specific or gene-specific roles | daf-16, atfs-1, sporulation factors, Skp pathway context | Foundation-model reasoning summaries |
| **Upstream label propagation error** | Misleading domain/family assignment drives a coherent but wrong downstream story | Spy classified as Cpx auxiliary protein; CpxP/Spy family-label spillover | BioReason and related multimodal pipelines |
| **Rule explosion / over-breadth** | Automated rule system creates huge, weakly interpretable annotation scope | ARBA00022825, ARBA00028334, ARBA00022679 | Rule-based pipelines |
| **Orthology over-transfer** | Conserved core function is transferred too aggressively into non-core process, localization, or context-specific claims | Uggt1: core glucosyltransferase function transfers well, but generic binding-related claims become over-annotated | ISO and related transfer pipelines |

### Why this taxonomy matters

These categories are not interchangeable. A less-precise parent term, a pathway-impossible prediction, and a localization hallucination should not be treated as equivalent just because they all contribute to lower overlap with a reference set. Their implications for model debugging, curator trust, and downstream scientific use are different.

For example:

- **Paralog conflation** suggests that the model needs finer-grained family discrimination.
- **Pathway-context blindness** suggests missing systems-level or organism-level reasoning.
- **Localization defaults** suggest failure to integrate sequence topology and export signals.
- **Narrative-annotation mismatch** suggests poor coupling between a language model's prose output and its formal ontology mapping.

This is precisely the kind of information lost when evaluation is reduced to F1 alone.

## Case Studies

### Case Study 1: Published ML error classes become biologically interpretable

The *E. coli* benchmark illustrates how agentic review sharpens existing error labels.

#### `yciO`: paralog overannotation

DeepECTF assigns `yciO` the same EC number as the TsaC/Sua5 family, but agentic review identifies this as a paralog overannotation rather than a generic false positive. The key issue is not that the model failed to recognize the family. It recognized the family but over-transferred a specific catalytic role. Review evidence shows that YciO has orders-of-magnitude weaker activity than TsaC, fails to complement the relevant mutant in vivo, and likely has a distinct RNA-related role. This is a more precise diagnosis than “incorrect prediction.”

#### `fepE`: frequency bias

`fepE` was predicted as a histidine kinase despite lacking histidine-kinase family features. Agentic review identifies the likely source as label frequency bias rather than local sequence confusion. The model appears to back off to a common EC class when evidence is weak. This is qualitatively different from a paralog mix-up or a small specificity error.

#### `yjhQ` and `yrhB`: pathway-context blindness

These genes highlight another important distinction: a function can be chemically plausible but biologically impossible in the organism. In both cases, the prediction fails because the model ignores genomic and pathway context. Such failures are hard to diagnose from overlap metrics alone but are obvious in a curator-style audit.

### Case Study 2: Foundation-model reasoning can be coherent yet biologically wrong

The BioReason comparison set reveals a different family of errors: failures in multimodal biological reasoning rather than simple classifier output.

#### Skp: localization default plus pathway-context collapse

For Skp, BioReason produces a fluent description of a generic ATP-independent stress chaperone, but it places the protein in the cytoplasm and casts it as part of a broad cytosolic proteostasis network. The actual biology is more specific: Skp is a **periplasmic** carrier for unfolded outer-membrane proteins. This is not a small annotation mismatch. It is a failure to use a decisive signal peptide and a failure to place the protein in the correct compartment and pathway.

#### Spy: propagation of a misleading family label

For Spy, BioReason builds a coherent but wrong narrative around a Cpx-system auxiliary label, describing the protein as a signaling component rather than as a periplasmic chaperone. Here the failure is not random hallucination. It is a structured propagation error in which an upstream family interpretation drives a polished but incorrect biological story.

#### RidA: narrative-annotation mismatch

RidA shows that a reasoning model can describe broad function correctly while still missing the core molecular truth. BioReason recognizes the reactive-imine detoxification context and the trimeric cytoplasmic scaffold, yet the narrative drifts toward “non-enzymatic” or generic binding-centered language even though RidA is an enzyme with a specific deaminase activity. This is a canonical narrative-annotation mismatch.

### Case Study 3: Foundation-model reasoning can also add value

Not all findings are negative. DnaJ provides an example where BioReason adds genuine biological synthesis beyond a simple domain-to-term pipeline. The model correctly reconstructs the Hsp40 cochaperone architecture and its stimulation of DnaK ATPase activity, while avoiding a specific InterPro2GO-derived mistake that would have assigned ATP binding to DnaJ itself. This is a useful positive control because it shows that the purpose of agentic evaluation is not to enumerate failures only. It is to distinguish genuine mechanistic synthesis from fluent but derivative output.

## Comparison with Older Automated Pipelines

### ARBA as a contrast class

ARBA is useful in this paper because it represents an earlier generation of automated annotation: explicit, human-readable rules trained on reviewed UniProt data and propagated to unreviewed proteins [GO_REF:0000117]. The failure signatures differ from those of foundation-model reasoning but are still highly informative.

In the reviewed rule set, the dominant problems are:

- extreme rule complexity,
- over-broad annotation targets,
- taxonomic overreach,
- redundancy with InterPro2GO,
- low interpretability at large scale.

Rules such as ARBA00022825, ARBA00028334, and ARBA00022679 are not merely “low precision.” They represent a distinct failure mode in which an automated system becomes too broad and too complex to validate meaningfully. Agentic evaluation captures this as **rule explosion / over-breadth**, a failure category with clear remediation implications.

### Orthology transfer as another contrast class

ISO-style transfer occupies a different point in the design space. Orthology is often reliable for conserved core molecular functions, but it is vulnerable to over-transfer of context-specific biological process, localization, or paralog-specific detail [GO_REF:0000008, GO_REF:0000107]. In this sense, orthology transfer and foundation-model reasoning share a common temptation: both may produce outputs that are directionally plausible while overcommitting on specificity.

Even in cases where the transferred core function is sound, agentic review can still separate robustly conserved function from overextended secondary claims. In the current review set, rat Uggt1 illustrates this pattern: core UDP-glucose:glycoprotein glucosyltransferase activity transfers cleanly, while more generic binding-centered claims are treated as non-core or over-annotated.

This is important conceptually. Not all qualitative errors are unique to foundation models. Some are recurring annotation problems that foundation models inherit, while others are amplified by the richer narrative output of those models.

## Discussion

### Agentic evaluation complements CAFA-style benchmarking

The main claim of this paper is not that benchmark metrics are obsolete. Precision, recall, and F1 remain essential. The claim is narrower and more practical: **they are insufficient for curator-aligned evaluation of modern AI systems for protein function prediction.**

Agentic evaluation provides three benefits that scalar metrics do not:

1. **It identifies the biological reason for failure.**
2. **It distinguishes harmless imprecision from curator-critical misunderstanding.**
3. **It reveals whether a reasoning model adds biological value beyond existing automated annotation sources.**

This is especially important for foundation models, whose outputs may appear more compelling than earlier systems precisely because they are expressed in fluent language.

### Not all “correct” predictions are equally useful

A second implication is that correctness should not be treated as a single axis. A prediction that gets the right general family but misses the decisive paralog-specific function is different from one that recovers a curated core function and misses only a peripheral process label. A prediction that is “less precise” may still be very useful. A prediction that is impossible in organismal context may be actively misleading.

Agentic evaluation makes these distinctions explicit.

### Toward curator-aligned benchmarks for foundation models

We suggest that future benchmarks for AI-based function prediction should include:

- term-level overlap metrics,
- novelty-aware analyses separating memorization from discovery,
- failure taxonomies grounded in curator practice,
- explicit evaluation of narrative outputs versus structured annotations,
- organism- and pathway-context checks,
- targeted challenge sets for pseudoenzymes, paralogs, and localization-sensitive proteins.

The *E. coli* benchmark derived from de Crécy-Lagard et al. is a promising model for this. It shows how published ML failure classes can seed a more general curator-aligned audit framework.

## Limitations

This manuscript draft has several limitations.

1. The current version is built from repository-based review sets and case studies rather than from a fully frozen benchmark release.
2. The BioReason comparison dataset is broad, but the quantitative summary in this draft is still high-level.
3. ARBA and ISO are currently used mainly as contrastive case studies; they should be expanded into more systematic analyses in later drafts.
4. The present work emphasizes qualitative diagnosis. A final paper should pair this with a more explicit quantitative prevalence analysis for each failure mode.

These are drafting limitations, not conceptual limitations. The key argument already holds: curator-aligned audit yields information that scalar metrics cannot.

## Next Writing Targets

The next pass of this manuscript should add:

1. a finalized abstract with tighter quantitative claims,
2. a figure showing the three-layer evaluation model,
3. a figure or table summarizing failure-category frequencies in the BioReason comparison set,
4. a dedicated subsection on GO-GPT versus BioReason,
5. a more systematic ARBA and ISO analysis,
6. a short section addressing concerns about “LLM judging LLM” by emphasizing literature-linked and structured review criteria.

## Provisional Conclusion

Agentic evaluation turns model disagreement into a biological audit trail. In doing so, it exposes failure modes that are central to curation but largely invisible to F1: paralog conflation, context blindness, localization defaults, pseudoenzyme errors, narrative-annotation mismatch, and over-broad automated propagation. This makes it a useful complement to benchmark evaluation, and a particularly important one for foundation-model-based methods whose outputs are richer, more persuasive, and more heterogeneous than those of earlier automated pipelines.
