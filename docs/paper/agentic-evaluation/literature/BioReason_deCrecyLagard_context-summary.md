# BioReason and de Crecy-Lagard Context Summary

## Why these papers matter together

These two papers motivate the current manuscript from opposite directions.

- **BioReason** argues that modern multimodal AI systems can produce richer, more interpretable biological reasoning than sequence models or language models alone. In the published paper, the emphasis is on *reasoning traces*, *mechanistic explanation*, and *multimodal integration* rather than on GO annotation quality per se. [Fallahpour et al. 2025, arXiv:2505.23579](https://arxiv.org/abs/2505.23579)
- **de Crecy-Lagard et al.** argue that current ML function prediction systems still make basic logic errors that human annotators avoid, especially when predictions require pathway context, paralog separation, or in vivo interpretation rather than simple pattern recognition. [de Crecy-Lagard et al. 2025](https://doi.org/10.1093/g3journal/jkaf169), [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

Taken together, they define the space our manuscript occupies:

1. modern AI systems can generate rich biological explanations,
2. but rich outputs still need biologically grounded audit,
3. and benchmark scores alone do not reveal the logic of model failure.

## 1. BioReason: what the published paper actually claims

### Core claim

The published **BioReason** paper is fundamentally a **multimodal biological reasoning** paper, not primarily a protein-function annotation paper. It presents a system that integrates a DNA foundation model with an LLM so that the LLM can reason directly over genomic embeddings rather than over text-only biological summaries. The paper frames the main problem as the gap between strong sequence representations and weak mechanistic interpretability in current foundation models. [Fallahpour et al. 2025](https://arxiv.org/abs/2505.23579)

### Main technical contributions

The paper highlights five contributions:

1. a multimodal architecture connecting a DNA foundation model to an LLM,
2. supervised fine-tuning plus reinforcement learning to incentivize biological reasoning,
3. new biological reasoning benchmarks,
4. empirical gains over single-modality baselines,
5. step-by-step interpretable reasoning traces.  
[Fallahpour et al. 2025](https://arxiv.org/abs/2505.23579)

### What tasks it evaluates

This is the most important contextual point for our manuscript: the published BioReason paper evaluates **genomic reasoning tasks**, not GO-style protein function annotation. Its curated datasets are built from:

- **KEGG-derived disease pathway reasoning**,
- **ClinVar** and **OMIM**-based variant effect prediction,
- additional linked metadata from **dbSNP** and **COSMIC**.  
[Fallahpour et al. 2025](https://arxiv.org/abs/2505.23579)

The paper reports a KEGG-derived biological reasoning dataset with **1,449 entries** and claims that BioReason improves KEGG-based disease pathway prediction from roughly the high-80% range to the high-90% range, with an average improvement of about **15%** on variant-effect tasks over strong baselines. [Fallahpour et al. 2025](https://arxiv.org/abs/2505.23579)

### Why it matters for our paper

The BioReason paper is important for us for three reasons:

1. It makes the strongest available case that **reasoning traces themselves** are a meaningful output to evaluate, not just final labels.
2. It explicitly argues that existing benchmarks under-measure **higher-order mechanistic reasoning**.
3. It positions interpretability and step-by-step explanation as central biological AI deliverables rather than optional extras.  
[Fallahpour et al. 2025](https://arxiv.org/abs/2505.23579)

Those claims align closely with our motivation for **agentic evaluation**.

### What it does not establish for our paper

The BioReason paper does **not** by itself establish that the same reasoning quality transfers to:

- protein function prediction,
- GO annotation,
- orthology-sensitive curation,
- pseudoenzyme recognition,
- localization-sensitive protein biology.

That gap is crucial. The published paper is strongest on **genomic and disease-mechanism reasoning**, while our manuscript is about **protein function prediction outputs** and their curator-relevant failure modes.

This is why the repository-side protein evaluation matters so much. In our local comparison project, the BioReason-Pro protein system is evaluated against curated AIGR reviews and often shows richer prose than older pipelines but limited value-add over InterPro2GO for many proteins, together with recurring failures in localization, paralog discrimination, pseudoenzyme handling, and organism-specific context. See [BIOREASON_COMPARISON.md](/Users/cjm/repos/ai-gene-review/projects/BIOREASON_COMPARISON.md).

### Best contextual use in the manuscript

The safest and strongest way to use the BioReason paper is:

- cite it as evidence that the field is moving toward **reasoning-first biological AI**,
- cite it as motivation for evaluating **reasoning traces and narratives**, not just labels,
- avoid claiming that the published BioReason paper already solves protein function prediction.

In other words, BioReason provides the **aspirational argument** for richer outputs; our manuscript asks whether those richer outputs are actually biologically reliable for protein function prediction.

## 2. de Crecy-Lagard et al. (2025): why it is so useful for us

### Core claim

de Crecy-Lagard et al. evaluate EC-number predictions for more than **450 E. coli proteins of unknown function** and conclude that current ML systems mostly fail to make truly novel predictions and often make elementary logic errors that human annotators avoid by using broader biological context. [de Crecy-Lagard et al. 2025](https://doi.org/10.1093/g3journal/jkaf169), [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

This is one of the clearest recent statements of the exact problem our paper addresses.

### What the paper contributes conceptually

The paper is valuable not just for its negative result but for its conceptual framing of protein annotation errors. It distinguishes:

- failures to capture or propagate known function,
- errors caused by multifunctionality or outdated curation,
- overannotation of paralogs,
- cases where in vitro activity does not justify in vivo functional assignment.  
[PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

This is already a move away from scalar benchmarking and toward **error typology**.

### Why the paper is stronger than a generic “ML fails” claim

The paper does not merely compare scores. It uses **individual expert curation** of predictions, emphasizing that:

- many errors occur in paralog-rich families,
- sequence-only similarity is insufficient,
- pathway and genome context are essential,
- uncertainty should become a standard model output,
- “hallucinations” or logic failures should be tested explicitly.  
[PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

This is highly aligned with our argument that F1 alone is insufficient.

### Concrete findings that matter for our manuscript

Several findings from de Crecy-Lagard et al. should be cited directly in the manuscript:

1. **Most current ML methods fail to make novel predictions** for the tested unknown proteins.  
   [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

2. **Paralog overannotation** is a major failure mode. The paper repeatedly shows that models assign the right broad family but the wrong specific enzymatic role or substrate.  
   [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

3. **Context-blind predictions** can be chemically plausible but biologically impossible in the organism.  
   [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

4. **In vitro activity is not equivalent to in vivo function.** This is especially important for proteins in promiscuous or recently diverged families.  
   [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

5. **Uncertainty and logic checking should be explicit outputs of future models**, not afterthoughts.  
   [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

6. Their XAI analysis suggests that correct predictions tend to be supported by localized high-signal features, whereas many incorrect predictions show weak or diffuse feature-importance patterns.  
   [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)

### Why it matters for our paper specifically

This paper gives us something extremely valuable: an **externally published failure taxonomy** that we did not invent ourselves.

That means the E. coli project in this repo is not just a convenient example set. It is a bridge from published ML error classes to our broader agentic failure taxonomy. See [VALIDATING_ECOLI_PREDICTIONS.md](/Users/cjm/repos/ai-gene-review/projects/VALIDATING_ECOLI_PREDICTIONS.md).

In manuscript terms, de Crecy-Lagard et al. support at least three claims:

1. **manual expert review is still necessary** to understand prediction validity,
2. **qualitative error classes are scientifically meaningful**, not anecdotal,
3. **logic failure** is a real and testable category of model error.

### Limits of the paper for our purposes

The de Crecy-Lagard paper is narrower than our manuscript in two ways:

- it focuses on **EC-number prediction** rather than GO-style protein annotation,
- it is centered on **E. coli enzymes of unknown function**, not cross-taxon foundation-model narratives.

That is a limitation, but also an advantage. The paper gives us a clean, well-grounded anchor case for logic-sensitive error analysis without requiring us to overclaim generality from one benchmark alone.

## 3. How the two papers fit together for our manuscript

### The conceptual intersection

The published BioReason paper says: biological AI should produce **interpretable, step-by-step reasoning**.  
The de Crecy-Lagard paper says: current ML systems still make **basic logic errors** that require expert review to detect.

Our manuscript sits exactly between those claims:

- if models produce richer reasoning outputs,
- then evaluation must ask whether that reasoning is biologically sound,
- and must classify *how* it fails, not just whether a final label matches.

That is the logic of **agentic evaluation**.

### What our manuscript adds beyond both papers

Relative to BioReason, our manuscript adds:

- evaluation of protein-function outputs rather than genomic reasoning tasks,
- curator-oriented analysis of narrative failure modes,
- direct comparison with existing annotation pipelines such as InterPro2GO, ARBA, and orthology transfer.

Relative to de Crecy-Lagard et al., our manuscript adds:

- a more general framework that applies beyond enzyme EC prediction,
- extension from structured prediction errors to **reasoning-trace and narrative** errors,
- a unified failure taxonomy spanning classifiers, transfer pipelines, and foundation-model reasoning systems.

### The strongest synthesis sentence

If we want one sentence to carry this section of the paper, it is probably:

> BioReason argues that biological AI should be evaluated as a reasoning system, while de Crecy-Lagard et al. show that current function-prediction models still fail basic biological logic; our contribution is to connect those claims through agentic, curator-aligned evaluation of model outputs.

## 4. Recommended citation use in the manuscript

### Good use

- Cite **BioReason** when motivating why richer reasoning outputs are now part of the model interface and why interpretability claims matter. [Fallahpour et al. 2025](https://arxiv.org/abs/2505.23579)
- Cite **de Crecy-Lagard et al.** when motivating qualitative error taxonomies, logic-sensitive evaluation, uncertainty, and context-aware expert review. [de Crecy-Lagard et al. 2025](https://doi.org/10.1093/g3journal/jkaf169)

### Avoid

- Do not cite the published BioReason paper as if it were already a validated GO/protein-function benchmark study.
- Do not cite de Crecy-Lagard et al. as if it already solved cross-taxon evaluation of foundation-model reasoning.

Each paper is strongest when used for the claim it actually supports.

## 5. Suggested manuscript language

### Introduction-ready paragraph

Recent biological AI systems increasingly claim not only predictive accuracy but mechanistic interpretability. For example, BioReason integrates a DNA foundation model with an LLM and emphasizes step-by-step biological reasoning as a first-class model output rather than a post hoc explanation [Fallahpour et al. 2025](https://arxiv.org/abs/2505.23579). At the same time, expert review of machine-learning-based enzyme predictions in *E. coli* has shown that current models still make basic logic errors, including paralog overannotation, context-blind predictions, and assignments that are biochemically plausible in vitro but unsupported in vivo [de Crecy-Lagard et al. 2025](https://doi.org/10.1093/g3journal/jkaf169). Together, these studies motivate evaluation frameworks that move beyond scalar benchmark scores to inspect the biological content and failure structure of model outputs.

### Discussion-ready paragraph

Our results are consistent with the broader trajectory of the field. BioReason and related systems demonstrate that multimodal biological AI can generate rich explanatory traces [Fallahpour et al. 2025](https://arxiv.org/abs/2505.23579), but de Crecy-Lagard et al. show that richer outputs do not guarantee sound biological logic [de Crecy-Lagard et al. 2025](https://doi.org/10.1093/g3journal/jkaf169). Agentic evaluation addresses this gap by treating prediction review as a structured biological audit, allowing us to distinguish between generic imprecision, paralog confusion, pathway impossibility, localization error, and other curator-relevant failure modes.
