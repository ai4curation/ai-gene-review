# FGFR2 (Fibroblast Growth Factor Receptor 2) Notes - ISOFORMS Project

## Key Isoform Biology

FGFR2 encodes a receptor tyrosine kinase with **tissue-specific isoform switching** that determines ligand specificity.

### Critical Isoforms: IIIb vs IIIc

| Isoform | UniProt ID | Exon Usage | Ligand Specificity | Tissue Expression |
|---------|------------|------------|-------------------|-------------------|
| **FGFR2IIIb** | P21802-1 | Exon IIIb | FGF1, FGF3, FGF7 (KGF), FGF10 | **EPITHELIAL** |
| **FGFR2IIIc** | P21802-3 | Exon IIIc | FGF1, FGF2, FGF4, FGF6, FGF9 | **MESENCHYMAL** |

### The IIIb vs IIIc Switch

The Ig-like domain III is alternatively spliced:
- **Exon IIIb** encodes epithelial-specific splice variant
- **Exon IIIc** encodes mesenchymal-specific splice variant

This creates **mutually exclusive ligand binding**:
- FGF7 (KGF) binds ONLY to IIIb (epithelial)
- FGF2 binds preferentially to IIIc (mesenchymal)

### Biological Significance: Epithelial-Mesenchymal Communication

The IIIb/IIIc isoform switching enables **paracrine signaling**:
- Mesenchyme produces FGF7/10 → signals to epithelium (IIIb)
- Epithelium produces FGF2/4 → signals to mesenchyme (IIIc)

This is critical for:
- Limb development
- Lung branching morphogenesis
- Prostate development
- Wound healing

### Soluble/Secreted Isoforms

- **Isoform 8** (P21802-8): Secreted
- **Isoform 13** (P21802-13): Secreted

These may act as decoy receptors, similar to soluble FAS.

### Cancer Relevance

**Isoform switching in cancer:**
- Epithelial-to-mesenchymal transition (EMT) includes IIIb→IIIc switch
- Some cancers inappropriately express IIIc in epithelial contexts
- Mis-splicing correlates with metastatic potential

## GOA Annotation Status

- **250 annotations fetched, 229 seeded**
- **NO isoform-specific annotations** - all annotated to P21802 gene level

## Expected Annotation Issues

1. **"FGF receptor signaling pathway"** - applies to both isoforms but with different ligands
2. **"fibroblast growth factor binding"** - TRUE for both, but DIFFERENT FGFs
3. Epithelial morphogenesis terms may be IIIb-specific
4. Mesenchymal development terms may be IIIc-specific
5. Any FGF7 (KGF) signaling annotations should be IIIb-specific
6. Any FGF2 signaling annotations should be preferentially IIIc

## Key References

- UniProt P21802 function annotation distinguishes IIIb and IIIc ligand binding
- PMID:1309608 - FGFR2 cloning and splice variants
- PMID:7987400 - FGF receptor ligand specificities
