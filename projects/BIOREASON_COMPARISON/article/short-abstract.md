---
title: "short-abstract"
---

Assigning functions to gene products is foundational in molecular biology, traditionally through expert curation and computational prediction. Most annotation databases deploy HMM- and family-based pipelines, but protein language models and agentic LLM predictors now generate new candidates at scale. How should databases decide whether to deploy them?

CAFA-style aggregate metrics track progress against GOA snapshots, but carry biases in metric choice, ground truth, and holdout composition, and leave free-text reasoning traces from agentic predictors such as BioReason-Pro unscored. de Crécy-Lagard et al. manually reviewed 453 predictions from a top deep learning method on uncharacterised *E. coli* proteins: only 3/453 were genuinely novel and correct, with the remainder falling into systematic error classes. Such manual review does not scale.

We present AI Gene Review (AIGR), an agentic curation pipeline that partially automates this expert synthesis step, classifying each prediction with a biologically motivated taxonomy. Applied to BioReason-Pro on ARGO139/ARGO95, AIGR finds: (i) seven reproducible RL narrative failure modes across 139 genes; (ii) in ARGO95, the cleaner HuggingFace SFT subset (95 genes, 955 terms), 67.5% restate GOA, 10.6% are incorrect, and 5.4% are correct novel terms known from the literature but absent from GOA; and (iii) `ESR-ECOLI-DET-Mini`, a 7-gene Expert Synthetic Review positive control, is reproducible, while an answer-key-withheld recap reaches 4/7 exact labels. We frame evaluation as three tiers: aggregate metrics, expert/agentic review, and prospective experiment. Tier 2, partially automated by AIGR, is a practical smell test for deployment decisions, not a replacement for expert judgment.
