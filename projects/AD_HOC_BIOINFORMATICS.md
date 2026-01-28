# Ad-Hoc Bioinformatics Analysis Project

## Overview

This project tracks cases where AI-assisted gene review required computational analysis beyond standard database lookups to validate or refute annotations. These analyses demonstrate the value of integrating bioinformatics capabilities into the curation workflow.

The agentic AI system can:
- Write and execute Python code for sequence analysis
- Query structural databases (PDB, AlphaFold)
- Perform domain architecture analysis
- Compare sequences across species
- Validate active site residues

**Source**: Presented at Gene Ontology Consortium Meeting, October 2025, Cambridge UK. See [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review).

## Categories of Bioinformatics Analysis

### 1. Active Site Validation

**Purpose**: Verify whether proteins with enzyme-like domains have conserved catalytic residues.

**Example - Epe1 (S. pombe)**:
- JmjC domain suggests histone demethylase activity
- Analysis revealed: HVD instead of canonical HXD motif
- Missing Fe(II)-binding histidine residues
- **Conclusion**: Pseudo-enzyme lacking catalytic activity
- **Location**: `genes/pombe/Epe1/Epe1-bioinformatics/`

### 2. Domain Architecture Analysis

**Purpose**: Map protein domains and compare to characterized homologs.

**Example - AcrF8 (phage ZF40)**:
- Small 92-residue protein
- Analysis of protein-protein and protein-RNA interaction surfaces
- Structural comparison to other Type I-F anti-CRISPRs
- **Conclusion**: Unique dual-binding mechanism

### 3. Substrate Specificity Prediction

**Purpose**: Determine whether predicted enzymatic activity matches actual substrate.

**Example - PHYKPL (human)**:
- Classified in aminotransferase III family
- Sequence analysis showed it functions as phospho-lyase
- Active site comparison to characterized family members
- **Conclusion**: Not a transaminase despite domain classification

### 4. Cofactor Binding Site Analysis

**Purpose**: Validate cofactor binding predictions.

**Example - Epe1 JmjC domain**:
- Fe(II) binding predicted from domain
- Analysis of metal coordination residues
- Comparison to active JmjC demethylases
- **Conclusion**: Cannot coordinate Fe(II) due to substitutions

### 5. Localization Signal Prediction

**Purpose**: Validate predicted localization based on signal sequences.

**Example - LPL1 (C. albicans)**:
- Predicted transmembrane domain (residues 286-306)
- Analysis suggests hydrophobic region for lipid droplet association
- **Conclusion**: Not a membrane protein; lipid droplet localized

## Genes with Bioinformatics Analyses

| Gene | Species | Analysis Type | Key Finding | Status |
|------|---------|--------------|-------------|--------|
| Epe1 | pombe | Active site, cofactor binding | Pseudo-demethylase, no Fe(II) binding | COMPLETE |
| AcrF8 | BPZF4 | Domain architecture, structure | Dual protein-RNA binding mechanism | COMPLETE |
| PHYKPL | human | Substrate specificity | Phospho-lyase, not transaminase | COMPLETE |
| LPL1 | CANAL | Localization signals | Lipid droplet, not membrane | COMPLETE |

## Analysis Resources

### Bioinformatics Folders
Each gene with computational analysis has a dedicated folder:
```
genes/<species>/<gene>/<gene>-bioinformatics/
├── RESULTS.md           # Summary of findings
├── *.py                 # Analysis scripts
├── data/                # Input data
└── results/             # Output files
```

### Common Tools Used
- **UniProt API** - Sequence retrieval
- **InterPro** - Domain predictions
- **PDB/AlphaFold** - Structural information
- **BLAST/HMMER** - Sequence comparison
- **Python (BioPython)** - Custom analysis scripts

## Best Practices

1. **Reproducibility**: All analyses should be scripted, not manual
2. **Documentation**: `RESULTS.md` summarizes key findings
3. **Citations**: Reference bioinformatics results in annotations
4. **Limitations**: Acknowledge when analysis is inconclusive

## When to Perform Bioinformatics Analysis

Consider computational analysis when:
- Domain-based predictions conflict with literature
- Active site conservation is questioned
- Substrate specificity is ambiguous
- Localization predictions seem inconsistent
- Pseudo-enzyme status is suspected

---

# STATUS

## Completed Analyses
- [x] pombe/Epe1 - JmjC domain analysis, Fe(II) binding
- [x] human/PHYKPL - Enzyme classification
- [x] CANAL/LPL1 - Localization prediction

## Bioinformatics Folders
- [x] genes/pombe/Epe1/Epe1-bioinformatics/
- [ ] genes/human/PHYKPL/PHYKPL-bioinformatics/ (to be created)
- [ ] genes/CANAL/LPL1/LPL1-bioinformatics/ (to be created)

Last updated: 2026-01-22

# NOTES

## 2026-01-22

**Project Creation**

Documented cases where ad-hoc bioinformatics resolved annotation ambiguities.

**Key Insight**: The most valuable bioinformatics application is **active site validation** for enzymes. Many proteins are annotated with enzymatic activity based on domain presence (IEA), but lack conserved catalytic residues.

**Epe1 Example**:
- JmjC domain → 7 enzymatic activity annotations
- Active site analysis → HVD instead of HXD, no Fe(II) binding
- **Result**: All 7 enzymatic annotations marked REMOVE

This demonstrates how computational analysis can systematically identify pseudo-enzymes and prevent annotation errors from propagating.
