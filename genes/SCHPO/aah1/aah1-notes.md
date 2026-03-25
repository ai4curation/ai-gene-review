# aah1 (O74922) - S. pombe 4-alpha-glucanotransferase - Review Notes

## Gene Identity
- **UniProt:** O74922 (AGLT1_SCHPO)
- **Gene:** aah1 (SPCC757.12)
- **EC:** 2.4.1.25 (4-alpha-glucanotransferase)
- **Family:** GH13 (glycoside hydrolase family 13, alpha-amylase superfamily)

## Key Literature

### PMID:40668835 - Jacob et al. 2025, PNAS
"α-glucan remodeling by GH13-domain enzymes shapes fungal cell wall architecture."

This is the primary experimental paper for aah1 function. Key findings:
- Aah1 and Aah3 are GPI-anchored GH13-family enzymes that act redundantly [PMID:40668835 "two conserved glycosylphosphatidylinositol-anchored α-amylase-like enzymes, Aah1 and Aah3, which act redundantly as key contributors to α-glucan network formation"]
- Double mutant (aah1Δ aah3Δ) shows severe phenotype: rounded cells, delayed division, clumping [PMID:40668835 "Cells lacking both enzymes exhibit severe growth and morphological defects, including rounded shape, delayed division, and cell clumping"]
- Solid-state NMR: α-1,3-glucan drops from 44% to 11% in rigid phase of double mutant [PMID:40668835 "the double mutant cell walls have dramatically reduced α-1,3-glucan and galactomannan content"]
- Cell wall thickens ~4x (100 nm to 400 nm) with compensatory β-glucan increase
- Proposed function: GH13-family transglycosylases that remodel α-glucan downstream of Ags1 synthase

### PMID:16751704 - Morita et al. 2006
"An alpha-amylase homologue, aah3, encodes a GPI-anchored membrane protein required for cell wall integrity and morphogenesis in S. pombe."

- Identified four alpha-amylase homologs (aah1-aah4) with GPI anchor signals [PMID:16751704 "four alpha-amylase homologs (Aah1p-Aah4p) have putative signal sequences and C-terminal GPI anchor addition signals"]
- aah1 single deletion: no obvious phenotype at 30°C or 37°C
- aah3 single deletion: morphological defects, hypersensitivity to cell wall-degrading enzymes
- No starch-degrading activity detected in S. pombe - supports transglycosylase not hydrolase function
- Catalytic residue mutations in Aah3 abolished function, confirming enzymatic activity is required

## Annotation Review Summary

### Accepted (core)
- **GO:0004134** 4-alpha-glucanotransferase activity (IEA/ISS/ISO) - core MF
- **GO:0009897** external side of plasma membrane (IEA) - core CC
- **GO:0051278** fungal-type cell wall polysaccharide biosynthetic process (ISS)
- **GO:0071940** fungal-type cell wall assembly (ISS)
- **GO:0070600** fungal-type cell wall (1->3)-alpha-glucan biosynthetic process (IMP) - most specific BP
- **GO:0009277** fungal-type cell wall (ISS)

### Kept as non-core
- **GO:0005509** calcium ion binding - structural cofactor, not primary function
- **GO:0005886** plasma membrane - correct but less informative than external side

### Removed
- **GO:0016052** carbohydrate catabolic process - incorrect; Aah1 is a transglycosylase/biosynthetic enzyme, not catabolic

### Over-annotated
- **GO:0005975** carbohydrate metabolic process - too broad, redundant with specific BP terms

## Key Gaps
- No direct enzymology on purified Aah1 (substrate specificity inferred from A. niger orthologs AgtA/AgtB)
- Individual contribution of aah1 vs aah3 unclear (strong phenotype only in double mutant)
- The "nonredundant" collaboration mentioned in PMID:40668835 suggests they may have distinct but overlapping substrate preferences
