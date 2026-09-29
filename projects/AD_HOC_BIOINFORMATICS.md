---
title: "Ad-Hoc Bioinformatics Analysis Project"
maturity: IN_PROGRESS
tags: [PIPELINE, FLAGSHIP]
species: [SCHPO, human, CANAL, BPZF4]
genes: [Epe1, PHYKPL, LPL1, AcrF8]
manifest:
  slides:
    - href: AD_HOC_BIOINFORMATICS/slides/AD_HOC_BIOINFORMATICS-slides.html
  artifacts:
    - href: https://claude.ai/artifact/L2Sufj4t2uzGbunSeHsxvK
      title: Project brief
---

# Ad-Hoc Bioinformatics Analysis Project

**Bottom line:** many GO annotations are inferred from a domain or family
match, and the fastest way to test one is often a small computation: check
whether the catalytic residues are still there, whether a "transmembrane"
segment makes sense, or whether a family member really has the family's
substrate. This page catalogues four early cases where the review agent did
that kind of ad-hoc analysis, one per analysis type. Epe1 (*S. pombe*) is the
worked example: its JmjC domain carried seven catalytic or metal-binding
annotations, and all seven are REMOVE in the review, while PHYKPL lost its IEA
`transaminase activity` and *C. albicans* LPL1 lost its IEA `membrane` row.
Only Epe1 has a scripted `-bioinformatics/` folder; PHYKPL and LPL1 were
argued inside the review, and AcrF8 has no analysis folder. The catalogue
below stopped in January 2026, while the repository now holds 237
`genes/*/*/*-bioinformatics/` folders (116 human, 40 HORSE, 24 DROME), so the
table is a sample, not an inventory; see [BIOINFORMATICS](BIOINFORMATICS.md)
for the reproducible-workflow standard.

We did this because a domain hit says what a protein's ancestors did, not what
it does, and a residue-level check is cheap evidence that can stop a wrong
enzymatic annotation from propagating to orthologs.

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
- Analysis: the Fe(II) facial triad is H297, E299 and **Y370**; the third
  ligand, which must be histidine for Fe(II) coordination, is tyrosine, the same
  substitution seen in catalytically dead human PHF2
- **Conclusion**: Pseudo-enzyme lacking catalytic activity
- **Location**: `genes/SCHPO/Epe1/Epe1-bioinformatics/`
- **Provenance of the triad call**: the first Epe1 script reported an "HVD
  instead of HXD" motif, which does not hold up (HVD fits HXD). The Y370 defect
  came from a later (2026-07) blinded OpenScientist run on the demethylase
  hypothesis
  (`genes/SCHPO/Epe1/Epe1-hypotheses/function-hypothesis-go-0032452/openscientist.md`)
  and matches the UniProt caution.

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
- [x] genes/SCHPO/Epe1/Epe1-bioinformatics/
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
- Active site analysis → HVD instead of HXD, no Fe(II) binding (superseded: the defect is Y370 at the third Fe(II) ligand; see the Epe1 example above)
- **Result**: All 7 enzymatic annotations marked REMOVE

This demonstrates how computational analysis can systematically identify pseudo-enzymes and prevent annotation errors from propagating.
