# PANTHER Family Review: PTHR11773

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR11773 |
| **Family Name** | GLYCINE DEHYDROGENASE, DECARBOXYLATING |
| **InterPro Entry** | IPR020581 (GDC_P) |
| **Total Proteins** | 28,819 |
| **Taxonomic Breadth** | 32,151 taxa |
| **Subfamilies** | 3 |
| **Representative Structure** | 6i35 (Human GLDC with pyridoxyl-glycine-5'-monophosphate) |

## Executive Summary

PTHR11773 is a highly conserved protein family encoding **glycine dehydrogenase (decarboxylating)**, also known as the **P-protein** of the **glycine cleavage system (GCS)**. This family catalyzes the pyridoxal 5'-phosphate (PLP)-dependent decarboxylation of glycine, transferring the aminomethyl moiety to the lipoylated H-protein. The reaction is:

**EC 1.4.4.2**: glycine + lipoyl-H-protein + H+ → aminomethyl-lipoyl-H-protein + CO2

The family is present across all domains of life, from bacteria to eukaryotes, with a well-conserved core function. The family shows minimal neo-functionalization - all members catalyze the same fundamental reaction.

## Subfamily Analysis

### PTHR11773:SF1 - GLYCINE DEHYDROGENASE (DECARBOXYLATING), MITOCHONDRIAL
**Members**: ~246 proteins (largest subfamily)

**Taxonomy**: Contains both eukaryotic proteins (with mitochondrial targeting signals) and bacterial full-length gcvP proteins.

**Key Members**:
- Human GLDC (P23378)
- Mouse Gldc (Q91W43)
- Chicken GLDC (P15505)
- Yeast GCV2 (P49095)
- Arabidopsis GLDP1 (Q94B78), GLDP2 (O80988)
- Bacterial full-length gcvP

**Function**: EC 1.4.4.2 - glycine dehydrogenase (decarboxylating) activity

**Notes**: The "MITOCHONDRIAL" suffix is somewhat misleading as this subfamily also contains bacterial proteins. In bacteria, the GCS is located in the cytoplasm. The naming reflects the eukaryotic proteins' mitochondrial localization.

### PTHR11773:SF13 - GLYCINE DEHYDROGENASE (DECARBOXYLATING)
**Members**: ~109 proteins

**Taxonomy**: Primarily Gammaproteobacteria, particularly Enterobacteriaceae (E. coli, Shewanella, Yersinia, Salmonella, Klebsiella)

**Key Members**:
- E. coli gcvP
- Shewanella spp. gcvP
- Yersinia spp. gcvP
- Vibrio spp. gcvP

**Function**: EC 1.4.4.2 - identical enzymatic function to SF1

**Notes**: This subfamily appears to represent a Gammaproteobacteria-specific clade with the same enzymatic function. The separation from SF1 likely reflects phylogenetic divergence rather than functional change.

### PTHR11773:SF12 - GLYCINE CLEAVAGE SYSTEM P PROTEIN
**Members**: ~4 proteins

**Taxonomy**: Plant-specific (Flaveria genus)

**Key Members**:
- Flaveria anomala GDCSP (O49850)
- Flaveria trinervia GDCSPA (O49852)
- Flaveria pringlei GDCSPA (P49361), GDCSPB (P49362)

**Function**: EC 1.4.4.2 - glycine dehydrogenase (decarboxylating) activity

**Notes**: This small subfamily contains C4 plant isozymes. Some Flaveria species have duplicated P-protein genes. These may have tissue-specific expression patterns related to C4 photosynthesis, but the core enzymatic function is unchanged.

## Functional Diversity Assessment

### Neo-functionalization: NONE DETECTED

All three subfamilies catalyze the same fundamental reaction (EC 1.4.4.2). There is no evidence of:
- Different EC numbers within the family
- Opposite reactions (e.g., synthesis vs. degradation)
- Non-catalytic functions
- Different substrate specificities

### Subfunctionalization: MINIMAL

The main variation observed is:
1. **Protein architecture**: Full-length (~950-1050 aa) vs. split (gcvPA + gcvPB subunits, ~480-500 aa each) in some bacteria
2. **Subcellular localization**: Mitochondrial (eukaryotes) vs. cytoplasmic (bacteria)
3. **Gene duplication**: Some plants (Flaveria, Arabidopsis) have multiple P-protein genes

## GO Annotation Assessment

### Core Annotations (Appropriate for ALL Family Members)

The following annotations are appropriate for the entire PTHR11773 family:

| GO Term | GO ID | Aspect | Notes |
|---------|-------|--------|-------|
| glycine dehydrogenase (decarboxylating) activity | GO:0004375 | MF | Core function, EC 1.4.4.2 |
| glycine binding | GO:0016594 | MF | Required for catalysis |
| pyridoxal phosphate binding | GO:0030170 | MF | Essential cofactor |
| glycine cleavage complex | GO:0005960 | CC | All P-proteins are GCS components |
| glycine decarboxylation via glycine cleavage system | GO:0019464 | BP | Core biological process |
| glycine catabolic process | GO:0006546 | BP | Part of glycine degradation |

### Annotations Requiring Taxon Restrictions

| GO Term | GO ID | Aspect | Taxon Restriction | Notes |
|---------|-------|--------|-------------------|-------|
| mitochondrion | GO:0005739 | CC | Eukaryota only | Bacteria lack mitochondria |

### Annotations to AVOID

| GO Term | GO ID | Reason |
|---------|-------|--------|
| glycine dehydrogenase activity | GO:0047960 | **WRONG** - This is a DIFFERENT enzyme (EC 1.4.1.10) that produces glyoxylate, NOT the GCS P-protein |

## CRITICAL ANNOTATION ERROR

**GO:0047960 (glycine dehydrogenase activity)** should NEVER be assigned to GLDC/GCV2/gcvP proteins:

- GO:0047960 catalyzes: `glycine + H2O + NAD+ → glyoxylate + NH3 + NADH` (EC 1.4.1.10)
- GO:0004375 catalyzes: `glycine + lipoyl-H-protein + H+ → aminomethyl-lipoyl-H-protein + CO2` (EC 1.4.4.2)

These are completely different reactions with different products. The current annotations in GOA for chicken GLDC (P15505) include erroneous GO:0047960 annotations that should be corrected to GO:0004375.

## Structural Biology

**Representative Structure**: PDB 6i35
- Human glycine decarboxylase (P-protein) bound with pyridoxyl-glycine-5'-monophosphate
- Shows PLP-binding pocket and active site architecture

**Key Structural Features**:
- PLP-binding lysine (Lys-738 in chicken)
- His-Lys(PLP)-X motif characteristic of PLP-dependent decarboxylases
- Homodimeric architecture (~200 kDa native)
- N-terminal and C-terminal domains (GDC_P_N and GDC_P_C)

## Key Literature

| PMID | Title | Key Finding |
|------|-------|-------------|
| PMID:7440562 | The mitochondrial glycine cleavage system. Purification and properties of glycine decarboxylase from chicken liver mitochondria | Seminal characterization of chicken P-protein |
| PMID:7440563 | Functional association of glycine decarboxylase and aminomethyl carrier protein | P-H protein interaction |
| PMID:1993704 | Molecular cloning of the chicken and human glycine decarboxylase cDNAs | Sequence conservation |
| PMID:3426593 | Amino acid sequence of the phosphopyridoxyl peptide from P-protein | PLP binding site identification |
| doi:10.1038/ncomms7388 | Glycine decarboxylase deficiency causes neural tube defects | Human disease mechanism |

## Recommendations

### For IBA Annotation Propagation

1. **ACCEPT** propagation of GO:0004375 (glycine dehydrogenase (decarboxylating) activity) to all family members
2. **ACCEPT** propagation of GO:0005960 (glycine cleavage complex) to all family members
3. **ACCEPT** propagation of GO:0016594 (glycine binding) to all family members
4. **ACCEPT** propagation of GO:0030170 (pyridoxal phosphate binding) to all family members
5. **ACCEPT** propagation of GO:0019464 (glycine decarboxylation via glycine cleavage system) to all family members
6. **RESTRICT** propagation of GO:0005739 (mitochondrion) to Eukaryota only
7. **NEVER** propagate GO:0047960 (glycine dehydrogenase activity) - this is a different enzyme

### For Database Curators

1. **Correct** existing GO:0047960 annotations on GLDC/GCV2/gcvP proteins to GO:0004375
2. **Review** propagated annotations to ensure taxon-appropriate localization terms
3. **Consider** renaming SF1 from "MITOCHONDRIAL" to something more inclusive of bacterial members

## Review Status

- **Date**: 2026-01-10
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: UniProt, PANTHER, published literature, GOA annotations
