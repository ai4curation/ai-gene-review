# CFAP61 Review Notes

## Gene Identity
- **UniProt:** Q8NHU2 (CFA61_HUMAN)
- **HGNC:** CFAP61 (formerly C20orf26)
- **Organism:** Homo sapiens
- **Size:** 1237 AA, 141 kDa
- **Isoforms:** 5 named isoforms (1, 3, 4, 5, 6)

## Key Findings from Literature Review

### Core Function: Structural component of axonemal radial spoke 3 (RS3) base
CFAP61 is a structural protein of motile cilia/flagella axonemes. It is NOT an enzyme despite having an FAD/NAD(P)-binding domain fold (Gene3D: 3.50.50.60, SUPFAM: SSF51905). This makes it a **pseudoenzyme** — the ancestral Rossmann-like fold has been exapted for structural/protein-protein interaction roles in the radial spoke complex rather than catalysis [PMID:37258679, "RS3...is built on a base of CFAP61, CFAP91 and CFAP251"].

### Pseudoenzyme / Exapted Active Site Aspect
- Contains two copies of the FAD/NAD(P)-binding domain fold per Gene3D classification
- No known enzymatic activity — no cofactor binding, no catalytic residues conserved
- The Rossmann-like fold is repurposed as a structural scaffold within the RS3 base
- This is a classic example of a pseudoenzyme with an exapted active site: the fold provides structural stability and protein-protein interaction surfaces rather than catalytic function
- InterPro domains: CFAP61 (IPR038884), CFAP61_dimer (IPR056299), CFAP61_N (IPR032151), FAD/NAD-bd_sf (IPR036188)

### Molecular Complex and Interactions
- Component of the **calmodulin- and spoke-associated complex (CSC)** together with CFAP91 (MAATS1) and CFAP251 [PMID:34792097, "CFAP61 is a conserved component of the calmodulin- and radial spoke-associated complex (CSC) of cilia"]
- Forms the **base of radial spoke 3 (RS3)** in human respiratory cilia [PMID:37258679, "a full-length RS3, which we show is built on a base of CFAP61, CFAP91 and CFAP251"]
- In Chlamydomonas, the CSC orthologs form the "RS3 stand-in" (RS3S), a stubby headless structure [PMID:37258679]
- Interacts with: CFAP91/MAATS1, ODAD2/ARMC4, RSPH3A, ROPN1, ROPN1L, RSPH9, DYNLT1, DYNC1I2, TUBB3, WDR35, IFT22, IFT81, CFAP70 [UniProt by similarity from mouse Q8CEL2]

### Cryo-EM Structure
- PDB 8J07: 96-nm repeat of human respiratory doublet microtubule at 4.10 Å by cryo-EM [PMID:37258679 Walton et al., Nature 2023]
- CFAP61 is resolved as part of the RS3 base in this structure
- A 2024 Nature Communications study further places CFAP61/CFAP91/CFAP251 in the RS3 stalk/base [doi:10.1038/s41467-023-44577-1, Meng et al.]

### Subcellular Localization
- **Axoneme** of both respiratory cilia and sperm flagella
- Identified in human airway cilia proteomics at moderate abundance [PMID:28282151]
- Localizes to sperm flagellum [PMID:36659204, PMID:34792097]
- Also localizes to manchette during spermatid elongation [PMID:34792097 by similarity]
- Part of the radial spoke stalk structure [ISS annotation]

### Disease: Spermatogenic Failure 84 (SPGF84) / MMAF
- Biallelic loss-of-function variants cause Multiple Morphological Abnormalities of the Flagella (MMAF) [PMID:34792097, PMID:35174165, PMID:35387802, PMID:38775994]
- MMAF phenotype: absent, short, bent, coiled flagella with severely reduced motility
- Mouse Cfap61 KO recapitulates the MMAF/infertility phenotype [PMID:34792097, PMID:36659204]
- Notably, NO primary ciliary dyskinesia (PCD) symptoms — respiratory cilia appear unaffected [PMID:34792097, "without other symptoms usually observed in PCD"]
- This organ-specific requirement suggests CFAP61 may be more critical for sperm flagellum RS3 assembly than for respiratory cilia RS3

### Tissue Specificity
- Highly expressed in testis [HPA: tissue enhanced in fallopian tube, heart muscle, skeletal muscle, testis]
- Present in airway cilia (proteomics, PMID:28282151) but KO does not cause respiratory phenotype
- The sperm-specific phenotype may relate to the longer flagellum requiring more robust RS stabilization

### Key Evidence Types for Annotations
- **IDA (direct assay):** Axoneme localization in human cilia [PMID:28282151], sperm flagellum localization [PMID:36659204]
- **IMP (mutant phenotype):** Sperm flagellum assembly defects [PMID:34792097, PMID:35174165], flagellated sperm motility [PMID:34792097]
- **IBA (phylogenetic):** Sperm flagellum, sperm flagellum assembly [GO_REF:0000033]
- **ISS (sequence similarity):** Cilium movement, motile cilium, cilium organization, radial spoke stalk, axoneme [GO_REF:0000024, from mouse]
- **IEA (electronic):** Cytoskeleton, cilium, axoneme [GO_REF:0000044]

### Missing Annotations to Consider
- **Radial spoke (GO:0001539)** or **radial spoke stalk (GO:0001536)** — strong evidence from cryo-EM structure
- **Sperm mitochondrial sheath assembly (GO:0120317)** — listed in UniProt GO but not in current GOA annotations; from mouse KO showing mitochondrial sheath defects
- **Molecular function:** No catalytic activity; could consider structural molecule activity or a binding term. The pseudoenzyme aspect means we should NOT annotate with any oxidoreductase or NAD-binding activity terms.
