# Validating E. coli ML Predictions

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
| ygfF | b2878 | P76626 | EC 1.1.1.47 (glucose 1-dehydrogenase) | COR (CS=2) - validated | PENDING |

### Paralog Incorrect (PLI)
| Gene | b-number | UniProt | DeepECTF Prediction | Paper Assessment | Status |
|------|----------|---------|-------------------|-----------------|--------|
| yciO | b1282 | P0AB18 | EC 2.7.7.87 (threonylcarbamoyladenylate synthase) | PLI (CS=0) - paralog of TsaC, different function | PENDING |
| yegV | b2100 | P0A8A8 | EC 2.7.1.92 (dehydro-2-deoxygluconokinase) | PLI (CS=0) - correct first 3 digits, wrong substrate | PENDING |

### Non-Paralog Incorrect (NPI)
| Gene | b-number | UniProt | DeepECTF Prediction | Paper Assessment | Status |
|------|----------|---------|-------------------|-----------------|--------|
| yjhQ | b4307 | P39358 | EC 2.3.1.189 (mycothiol synthase) | NPI (CS=0) - mycothiol pathway absent in E. coli | PENDING |
| yrhB | b3446 | P0AES2 | EC 4.1.2.50 (6-carboxytetrahydropterin synthase) | NPI (CS=0) - activity already encoded by QueD | PENDING |

### Uncertain
| Gene | b-number | UniProt | DeepECTF Prediction | Paper Assessment | Status |
|------|----------|---------|-------------------|-----------------|--------|
| yjdM | b4108 | P39330 | EC 3.11.1.2 (phosphonoacetate hydrolase) | UNC (CS=1) - in vitro activity not supported in vivo | PENDING |

### Repetition Error (REP)
| Gene | b-number | UniProt | DeepECTF Prediction | Paper Assessment | Status |
|------|----------|---------|-------------------|-----------------|--------|
| fepE | b0587 | P24079 | EC 2.7.13.3 (histidine kinase) | REP (CS=0) - no similarity to HK family | PENDING |

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
(none yet)

## Pending Reviews
- [ ] ECOLI/ygfF - Correct novel prediction (SDR family)
- [ ] ECOLI/yciO - Paralog incorrect (TsaC paralog)
- [ ] ECOLI/yegV - Paralog incorrect (sugar kinase)
- [ ] ECOLI/yjhQ - Non-paralog incorrect (mycothiol synthase)
- [ ] ECOLI/yrhB - Non-paralog incorrect (QueD duplicate)
- [ ] ECOLI/yjdM - Uncertain (phosphonoacetate hydrolase)
- [ ] ECOLI/fepE - Repetition error (histidine kinase)

Last updated: 2026-03-06

# NOTES

## 2026-03-06

**Project Creation**

Created project to validate E. coli gene annotations against findings from de Crecy-Lagard et al. (2025).
Selected 7 genes spanning all major error categories in the paper's taxonomy.
