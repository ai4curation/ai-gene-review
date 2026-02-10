# PANTHER IBA Annotation Error Report: NTN1/NTN3 Incorrectly Annotated as dbTFs

## Summary

Netrin-1 (NTN1, O95631) and Netrin-3 (NTN3, O00634) have erroneous IBA (Inferred from Biological Ancestor) annotations to DNA-binding transcription factor activity (GO:0000981). These annotations should be removed.

## The Error

### Affected Annotations

| Gene | UniProt | GO Term | Evidence | Source Node |
|------|---------|---------|----------|-------------|
| NTN1 | O95631 | GO:0000981 (dbTF activity, RNAP II-specific) | IBA | PTN000180816 |
| NTN1 | O95631 | GO:0006357 (regulation of transcription by RNAP II) | IBA | PTN000180816 |
| NTN1 | O95631 | GO:0000978 (cis-regulatory region sequence-specific DNA binding) | IBA | PTN000180816 |
| NTN3 | O00634 | GO:0000981 (dbTF activity, RNAP II-specific) | IBA | PTN000180816 |
| NTN3 | O00634 | GO:0006357 (regulation of transcription by RNAP II) | IBA | PTN000180816 |
| NTN3 | O00634 | GO:0000978 (cis-regulatory region sequence-specific DNA binding) | IBA | PTN000180816 |

### Evidence Used (WITH/FROM field)

The IBA annotations cite the following proteins as evidence:
- **UniProtKB:P14859** - POU2F1 (OCT1) - POU domain TF
- **UniProtKB:P28069** - POU1F1 (Pit-1) - POU domain TF
- **UniProtKB:Q01851** - POU4F1 - POU domain TF
- **UniProtKB:Q01860** - POU5F1 (OCT4) - POU domain TF
- **UniProtKB:Q12837** - POU4F2 - POU domain TF
- **UniProtKB:Q14863** - POU6F1 - POU domain TF
- **UniProtKB:Q15319** - POU4F3 - POU domain TF
- **UniProtKB:Q9UKI9** - POU2F3 - POU domain TF
- Various FlyBase, MGI, RGD, WormBase orthologs

## Why This Is Wrong

### 1. Different PANTHER Families

| Protein | PANTHER Family | Family Name |
|---------|---------------|-------------|
| NTN1 | **PTHR10574** | NETRIN/LAMININ-RELATED |
| NTN3 | **PTHR10574** | NETRIN/LAMININ-RELATED |
| POU2F1 | **PTHR11636** | POU DOMAIN |
| POU1F1 | **PTHR11636** | POU DOMAIN |

These proteins belong to **completely different PANTHER families**. There is no phylogenetic relationship that would justify propagating POU TF annotations to netrins.

### 2. Different Domain Architecture

| Protein Type | Domains |
|--------------|---------|
| **Netrins (NTN1/NTN3)** | Signal peptide, Laminin N-terminal (VI), Laminin EGF-like, NTR domain |
| **POU TFs (POU2F1 etc.)** | POU-specific domain, POU homeodomain (DNA-binding) |

Netrins have **no DNA-binding domains**. They are secreted extracellular matrix proteins.

### 3. Different Molecular Function

| Protein Type | Function | Localization |
|--------------|----------|--------------|
| **Netrins** | Axon guidance via receptor binding (DCC, UNC5) | Secreted, extracellular |
| **POU TFs** | Sequence-specific DNA binding, transcription regulation | Nuclear |

### 4. Supporting Literature

PMID:28945198 states: *"Netrin-1 is a secreted protein that was first identified 20 years ago as an axon guidance molecule."*

There is **no literature evidence** that netrins bind DNA or regulate transcription as transcription factors.

## Root Cause Analysis

The PANTHER node **PTN000180816** appears to be an erroneous ancestral node in the GO-PAINT phylogenetic tree that incorrectly groups:
- Netrins (PTHR10574 - extracellular guidance cues)
- POU domain TFs (PTHR11636 - nuclear transcription factors)

This violates the fundamental principle of phylogenetic annotation inference: proteins should share function only if they share evolutionary ancestry of the functional domains.

## Recommended Actions

### 1. Remove Erroneous Annotations
The following annotations should be removed from GOA:
- NTN1: GO:0000981, GO:0006357, GO:0000978 (IBA)
- NTN3: GO:0000981, GO:0006357, GO:0000978 (IBA)

### 2. Review PANTHER Node PTN000180816
The GO Consortium/PANTHER team should review node PTN000180816 to:
- Determine why netrins were grouped with POU TFs
- Correct the phylogenetic tree structure
- Prevent similar errors in future IBA propagation

### 3. Other PTHR10574 Members Checked

We verified that other members of PTHR10574 (NETRIN/LAMININ-RELATED) do NOT have the erroneous dbTF annotations:

| Protein | UniProt | dbTF Annotation? |
|---------|---------|------------------|
| NTN1 | O95631 | **YES - ERROR** |
| NTN3 | O00634 | **YES - ERROR** |
| NTN4 | Q9HB63 | No |
| NTN5 | Q8WTR8 | No |
| NTNG1 | Q9Y2I2 | No |
| NTNG2 | Q96CW9 | No |
| Laminins | Various | No |

The error appears limited to NTN1 and NTN3 specifically.

## How to Report

1. **GitHub Issue**: [geneontology/go-annotation](https://github.com/geneontology/go-annotation/issues)
2. **PANTHER Contact**: Via [pantherdb.org](https://www.pantherdb.org/) feedback

## References

- [GO_REF:0000033 - IBA Annotation Method](https://geneontology.org/GO_REF/0000033.html)
- [PANTHER Classification System](https://www.pantherdb.org/)
- [GO Consortium Phylogenetic Annotation](https://wiki.geneontology.org/index.php/Phylogenetic_Annotation_Project)

## Files

- `genes/human/NTN1/NTN1-ai-review.yaml` - NTN1 annotation review
- `genes/human/NTN3/NTN3-ai-review.yaml` - NTN3 annotation review
