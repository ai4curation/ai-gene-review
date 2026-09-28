---
title: "Validating E. coli ML Predictions"
collections: [FUNCTION_PREDICTION]
maturity: COMPLETE
tags: [PIPELINE, FLAGSHIP, EVALUATION]
species: [ECOLI]
genes: [ygfF, yciO, yegV, yjhQ, yrhB, yjdM, fepE]
sidecars:
  # Deck images: copied beside the rendered deck so its relative <img> paths resolve.
  slide_images:
    - VALIDATING_ECOLI_PREDICTIONS/slides/ecoli-predictions.svg
    - VALIDATING_ECOLI_PREDICTIONS/slides/ecoli-review-actions.svg
    - VALIDATING_ECOLI_PREDICTIONS/slides/yciO-review-table.jpg
---

# Validating E. coli ML Predictions

**Bottom line:** de Crécy-Lagard et al. (2025, PMID:40703034) had experts assess
453 DeepECTransformer EC-number predictions for *E. coli* proteins of unknown
function and found that the model mostly failed to make novel predictions (only
3 were correct and novel) and made basic logic errors such as paralog confusion
and ignoring pathway context. We picked one or two genes from five of the paper's
seven categories (7 genes: ygfF, yciO, yegV, yjhQ, yrhB, yjdM, fepE), wrote a full GO annotation review for each, and recorded
the DeepECTF prediction in a structured `*-det-predictions-review.yaml` file. All 7
reviews are complete and our assessments agree with the paper's categories: COR
for ygfF, PLI for yciO and yegV, NPI for yjhQ and yrhB, UNC for yjdM and REP for
fepE. The same logic errors also appear in existing GO annotations: the yciO
threonylcarbamoyladenylate synthase rows (GO:0061710) and a fepE tyrosine-kinase
IBA row (GO:0004713) were marked REMOVE, and the yjdM phosphonoacetate hydrolase
rows (GO:0047400) were marked over-annotated.

We did this to check whether an agentic gene review reproduces expert judgments
on ML predictions, and whether the errors those experts found in the model also
exist in GOA. The UniProt and b-number columns in the tables below were corrected
on 2026-09-26 to match the review files.

[Function prediction evaluation index](FUNCTION_PREDICTION_EVALUATION.md)


## Overview

This project evaluates GO annotations for E. coli genes highlighted in de Crecy-Lagard et al. (2025)
"Limitations of current machine learning models in predicting enzymatic functions for uncharacterized proteins"
(PMID:40703034, DOI:10.1093/g3journal/jkaf169).

The paper evaluated 453 EC number predictions made by DeepECTransformer for E. coli proteins of unknown function,
finding that current ML methods mostly fail to make novel predictions and make basic logic errors.

Our goal is to independently review GO annotations for a sample of genes from each error category
in the paper's taxonomy, to see how existing GO annotations hold up.

## Paper Error Taxonomy

| Error Type | Code | Description |
|-----------|------|-------------|
| Training data contamination | CNN | Prediction matches training data (not novel) |
| Correct novel | COR | Genuinely novel correct prediction (only 3/453) |
| Less precise | LSP | More generic than existing UniProt annotation |
| Non-paralog incorrect | NPI | Prediction contradicted by pathway/genome context |
| Paralog incorrect | PLI | Wrong paralog subfamily assignment |
| Repetition | REP | Frequency-biased duplicate EC assignment |
| Uncertain | UNC | Cannot confirm or refute |

## Selected Genes for Review

Sampling across the error taxonomy to evaluate existing GO annotations in context of the paper's findings.

### Correct Novel (COR)
| Gene | b-number | UniProt | DeepECTF Prediction | Paper Assessment | Status |
|------|----------|---------|-------------------|-----------------|--------|
| ygfF | b2902 | P52037 | EC 1.1.1.47 (glucose 1-dehydrogenase) | COR (CS=2) - validated | COMPLETE |

### Paralog Incorrect (PLI)
| Gene | b-number | UniProt | DeepECTF Prediction | Paper Assessment | Status |
|------|----------|---------|-------------------|-----------------|--------|
| yciO | b1267 | P0AFR4 | EC 2.7.7.87 (threonylcarbamoyladenylate synthase) | PLI (CS=0) - paralog of TsaC, different function | COMPLETE |
| yegV | b2100 | P76419 | EC 2.7.1.92 (dehydro-2-deoxygluconokinase) | PLI (CS=0) - correct first 3 digits, wrong substrate | COMPLETE |

### Non-Paralog Incorrect (NPI)
| Gene | b-number | UniProt | DeepECTF Prediction | Paper Assessment | Status |
|------|----------|---------|-------------------|-----------------|--------|
| yjhQ | b4307 | P39368 | EC 2.3.1.189 (mycothiol synthase) | NPI (CS=0) - mycothiol pathway absent in E. coli | COMPLETE |
| yrhB | b3446 | P46857 | EC 4.1.2.50 (6-carboxytetrahydropterin synthase) | NPI (CS=0) - activity already encoded by QueD | COMPLETE |

### Uncertain
| Gene | b-number | UniProt | DeepECTF Prediction | Paper Assessment | Status |
|------|----------|---------|-------------------|-----------------|--------|
| yjdM | b4108 | P0AFJ1 | EC 3.11.1.2 (phosphonoacetate hydrolase) | UNC (CS=1) - in vitro activity not supported in vivo | COMPLETE |

### Repetition Error (REP)
| Gene | b-number | UniProt | DeepECTF Prediction | Paper Assessment | Status |
|------|----------|---------|-------------------|-----------------|--------|
| fepE | b0587 | P26266 | EC 2.7.13.3 (histidine kinase) | REP (CS=0) - no similarity to HK family | COMPLETE |

## Key Questions

1. Do existing GO annotations for these genes reflect the paper's findings?
2. Are there over-annotations that would be caught by the same logic errors ML models make?
3. For the "unknown" genes, what can we infer from genomic context and structural data?
4. How well do current GO terms capture the nuanced functions described in the paper?

## References

- de Crecy-Lagard V et al. (2025) Limitations of current machine learning models in predicting enzymatic functions for uncharacterized proteins. G3 15(10). PMID:40703034

---

# STATUS

## Completed Reviews
- [x] ECOLI/ygfF - Correct novel prediction (SDR family) - glucose 1-dehydrogenase confirmed
- [x] ECOLI/yciO - Paralog incorrect (TsaC paralog) - 10,000x weaker activity, recommends removing EC 2.7.7.87
- [x] ECOLI/yegV - Paralog incorrect (sugar kinase) - first 3 EC digits correct, substrate unknown
- [x] ECOLI/yjhQ - Non-paralog incorrect (mycothiol synthase) - mycothiol absent from E. coli; actually antitoxin
- [x] ECOLI/yrhB - Non-paralog incorrect (QueD duplicate) - activity belongs to QueD; Imm35 immunity domain
- [x] ECOLI/yjdM - Uncertain (phosphonoacetate hydrolase) - in vitro activity but no in vivo support
- [x] ECOLI/fepE - Repetition error (histidine kinase) - frequency bias; actually Wzz O-antigen regulator

## Pending Reviews
(none)

Last updated: 2026-09-26

# NOTES

## 2026-03-22

**All 7 reviews completed**

Completed reviews for all 7 E. coli genes spanning the de Crecy-Lagard et al. error taxonomy.
Key findings:
- COR (ygfF): DeepECTF prediction validated; existing GO annotations mostly appropriate
- PLI (yciO, yegV): Paralog confusion leads to incorrect substrate/function annotations
- NPI (yjhQ, yrhB): ML models ignore organism pathway context entirely
- UNC (yjdM): In vitro activity != in vivo function; genetic evidence contradicts ML prediction
- REP (fepE): Frequency-biased prediction of histidine kinase; also found erroneous IBA tyrosine kinase annotation

Also created predictions-review.yaml files for all 7 genes with structured error assessments.

## 2026-03-06

**Project Creation**

Created project to validate E. coli gene annotations against findings from de Crecy-Lagard et al. (2025).
Selected 7 genes spanning all major error categories in the paper's taxonomy.

## Slides

- [Slides](VALIDATING_ECOLI_PREDICTIONS/slides/VALIDATING_ECOLI_PREDICTIONS-slides.html) (Marp source: [VALIDATING_ECOLI_PREDICTIONS-slides.md](https://github.com/ai4curation/ai-gene-review/blob/main/projects/VALIDATING_ECOLI_PREDICTIONS/slides/VALIDATING_ECOLI_PREDICTIONS-slides.md)) — AI generated
