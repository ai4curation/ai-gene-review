# NCGR_LOCUS29329 - Bifunctional Aspartate Kinase / Homoserine Dehydrogenase

## Gene Summary

- **UniProt ID**: A0A811PKG6 (TrEMBL, unreviewed)
- **Organism**: *Miscanthus lutarioriparius* (taxon 422564, Poaceae/grasses)
- **Protein**: Bifunctional aspartokinase/homoserine dehydrogenase (AK-HSD)
- **Size**: 920 amino acids
- **Domains**: N-terminal aspartate kinase (AA_kinase, Pfam PF00696), C-terminal homoserine dehydrogenase (Homoserine_dh, PF00742), NAD-binding domain (NAD_binding_3, PF03447), two ACT regulatory domains (positions 416-491 and 497-574)
- **EC numbers**: EC 2.7.2.4 (aspartate kinase), EC 1.1.1.3 (homoserine dehydrogenase)
- **Localization**: Chloroplast/plastid

## Functional Context

Bifunctional AK-HSD enzymes catalyze the first (AK) and third (HSD) steps in the aspartate-derived amino acid biosynthetic pathway, which produces lysine, threonine, and methionine from L-aspartate. This is a conserved pathway in plants and bacteria.

### Reactions catalyzed:
1. **Aspartate kinase (EC 2.7.2.4)**: L-aspartate + ATP -> 4-phospho-L-aspartate + ADP
2. **Homoserine dehydrogenase (EC 1.1.1.3)**: L-aspartate 4-semialdehyde + NAD(P)H + H+ -> L-homoserine + NAD(P)+

### Pathway involvement:
- L-lysine biosynthesis via DAP pathway (step 1)
- L-threonine biosynthesis (steps 1 and 3)
- L-methionine biosynthesis via de novo pathway (steps 1 and 3)
- L-homoserine biosynthesis (catalyzes the HSD step directly)

## Plant AK-HSD Biology

In plants like Arabidopsis, bifunctional AK-HSD enzymes (AK-HSDH I and II) are well-characterized [PMID:26175505 "Analysis of Loss-of-Function Mutants in Aspartate Kinase and Homoserine Dehydrogenase Genes Points to Complexity in the Regulation of Aspartate-Derived Amino Acid Contents"]. Key features:

- All aspartate pathway steps (except final methionine methylation) occur in the chloroplast
- AK-HSD enzymes are subject to feedback inhibition by threonine via ACT domains
- The ACT domains serve as allosteric regulatory sensors for threonine
- Plants typically have both monofunctional AK (lysine-sensitive) and bifunctional AK-HSD (threonine-sensitive) forms

## Genome Context

The *M. lutarioriparius* genome was assembled at chromosome scale (2.07 Gb, 57,710 genes) [PMID:33911077 "Chromosome-scale assembly and analysis of biomass crop Miscanthus lutarioriparius genome"]. This is a C4 grass used as a biomass energy crop. The NCGR_LOCUS29329 sequence is from WGS preliminary data.

## Notes on Annotation Quality

- All 11 existing GO annotations are IEA (electronic) - no experimental evidence
- The protein is unreviewed (TrEMBL) and from WGS preliminary data
- Domain architecture is highly consistent with bifunctional AK-HSD: the InterPro signatures (IPR001341, IPR018042, IPR011147, IPR001342, IPR005106) are all diagnostic
- PANTHER classification (PTHR43070:SF5) confirms homoserine dehydrogenase subfamily
- CDD domain cd04257 (AAK_AK-HSDH) is specific to the bifunctional enzyme
