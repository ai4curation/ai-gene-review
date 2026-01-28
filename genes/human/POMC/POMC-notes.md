# POMC - Pro-opiomelanocortin Notes

## Polyprotein Biology

POMC is a paradigm for **post-translational processing** - fundamentally different from alternative splicing. A single mRNA produces ONE precursor protein that is then proteolytically cleaved into multiple bioactive peptides with **distinct and sometimes antagonistic functions**.

### Cleavage Products (from UniProt)

| Peptide | Residues | PRO ID | Function |
|---------|----------|--------|----------|
| Signal peptide | 1-26 | - | Secretion |
| NPP | 27-102 | PRO_0000024966 | Unknown |
| Gamma-MSH | 77-87 | PRO_0000024967 | Pigmentation |
| Potential peptide | 105-134 | PRO_0000024968 | Unknown |
| **ACTH** | 138-176 | PRO_0000024969 | **Stimulates cortisol release** |
| **Alpha-MSH** | 138-150 | PRO_0000024970 | **Anorexigenic, pigmentation** |
| CLIP | 156-176 | PRO_0000024971 | Unknown |
| Beta-LPH | 179-267 | PRO_0000024972 | Lipotropic |
| Gamma-LPH | 179-234 | PRO_0000024973 | Lipotropic |
| Beta-MSH | 217-234 | PRO_0000024974 | Pigmentation |
| **Beta-endorphin** | 237-267 | PRO_0000024975 | **Orexigenic opiate** |
| Met-enkephalin | 237-241 | PRO_0000024976 | Opiate |

### Tissue-Specific Processing

The key insight is that **different tissues produce different peptide combinations**:

1. **Anterior pituitary (corticotrophs)**: ACTH is the primary product
   - ACTH stimulates adrenal cortex to release cortisol
   - Processing stops at ACTH level - alpha-MSH is NOT produced here

2. **Intermediate pituitary** (minimal in adult humans): MSH peptides
   - ACTH is further cleaved to produce alpha-MSH and CLIP
   - This is the main source of MSH in other species

3. **Hypothalamus (arcuate nucleus)**: Both alpha-MSH and beta-endorphin
   - Alpha-MSH: reduces appetite (anorexigenic) via MC4R
   - Beta-endorphin: stimulates appetite (orexigenic), pain modulation

### Antagonistic Functions Within Same Precursor

This is critical for GO annotation:
- **Alpha-MSH**: Anorexigenic (suppresses appetite)
- **Beta-endorphin**: Orexigenic (stimulates appetite)

Both peptides are produced in the same hypothalamic neurons! The balance between them affects feeding behavior.

### GO Annotation Challenges

1. **Gene-level vs peptide-level**: GO annotates the gene, but functions are peptide-specific
2. **Antagonistic functions**: The gene should NOT be simply annotated to both "positive regulation of appetite" and "negative regulation of appetite" without context
3. **Tissue specificity**: ACTH function is relevant for pituitary; MSH function for hypothalamus
4. **PRO ontology**: UniProt provides PRO IDs for each peptide - ideal for peptide-specific GO annotation

### Key References

- PMID:9620771 - POMC mutations cause obesity, adrenal insufficiency, red hair (Krude et al. 1998)
- PMID:12165561 - R236G variant affects beta-endorphin processing, causes obesity

## Comparison to Alternative Splicing

| Feature | Alternative Splicing (e.g., BCL2L1) | Polyprotein Processing (POMC) |
|---------|-------------------------------------|-------------------------------|
| Mechanism | Pre-mRNA splicing | Post-translational proteolysis |
| Regulation point | Nucleus (splicing) | ER/Golgi/secretory pathway |
| mRNA products | Multiple distinct mRNAs | Single mRNA |
| Protein products | Different full-length proteins | Multiple peptides from one precursor |
| Tissue specificity | Splice factor expression | Prohormone convertase expression |
| Example enzymes | - | PC1/3, PC2, carboxypeptidases |

## Questions for GO Curation

1. Should annotations be made at the PRO level for peptide-specific functions?
2. How to handle antagonistic functions from the same gene?
3. Is "regulation of appetite" appropriate when the gene produces both appetite-increasing and appetite-decreasing peptides?
