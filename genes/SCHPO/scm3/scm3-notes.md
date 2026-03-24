# scm3 (SPAPB1A10.02) - Gene Review Notes

## Gene Overview
- **Full name**: CENP-A histone chaperone scm3
- **UniProt ID**: Q9HDY7
- **Organism**: Schizosaccharomyces pombe (fission yeast)
- **Domains**: Scm3/HJURP (IPR018465), Histone-fold (IPR009072), Scm3 Pfam (PF10384)
- **Human ortholog**: HJURP (Holliday junction recognition protein)

## Core Function Summary
Scm3 is the dedicated CENP-A/Cnp1 histone chaperone in S. pombe. Its primary function is to
mediate the stable deposition of the histone H3 variant CENP-A (Cnp1) into centromeric chromatin,
which is essential for kinetochore assembly and proper chromosome segregation.

### Key structural domains:
1. **N-terminal CENP-A binding domain** - Interacts specifically with Cnp1/CENP-A [PMID:19217403, PMID:19217404]
2. **Mis16-binding domain (Mis16-BD)** (~aa 270-305) - Interacts with Mis16 for centromere targeting [PMID:38084929]
3. **C-terminal cysteine-rich domain (CYS)** - Binds zinc, essential for centromere localization [PMID:38084929]

## Key Literature Findings

### PMID:19217403 (Williams et al. 2009)
- Scm3 is required for centromeric localization of Cnp1
- Scm3 localizes at centromeres independently of Cnp1
- Mis16-Mis18 complex required for Scm3 centromere localization
- Scm3 dissociates from centromeres during mitosis (like Mis16/Mis18)
- Inactivation of Scm3 leads to H3 and H2A/H2B invading centromeres
- In S. pombe, Scm3 acts as a Cnp1 assembly/maintenance factor (not a nucleosome component as proposed in budding yeast)

### PMID:19217404 (Pidoux et al. 2009)
- Scm3 co-affinity purifies with Cnp1/CENP-A
- Scm3 associates with CENP-A in vitro
- Scm3 localizes independently of intact CENP-A chromatin
- Differentially released from chromatin compared to CENP-A
- Required for integrity of subkinetochore chromatin
- Model: Scm3 acts as a CENP-A receptor, cooperating with Mis16 and Mis18

### PMID:26275423 (Thakur et al. 2015)
- ChIP-seq mapping of inner kinetochore proteins
- Scm3 is highly enriched throughout the centromeric central domain
- Enriched except at tRNA genes
- Weakly enriched in H3-rich heterochromatin (outer repeats)
- No evidence for preferred kinetochore assembly sites

### PMID:38084929 (Folco et al. 2024)
- CYS domain binds zinc in vitro
- CYS is essential for Scm3 centromere localization and function
- Disrupting CYS prevents centromere localization and compromises kinetochore integrity
- CYS alone can localize to centromere (weakly), enhanced with Mis16-BD
- CYS likely binds centromeric DNA (independent of Mis16 interaction)
- Overexpression of truncated Scm3 (with CYS but lacking CENP-A binding) causes toxicity and kinetochore loss

### PMID:16823372 (Matsuyama et al. 2006)
- Large-scale protein localization study
- Scm3 detected in both nucleus and cytoplasm/cytosol (HDA evidence)

## Protein-Protein Interactions
- **Cnp1/CENP-A (SPBC1105.17)**: Direct binding via N-terminal domain [PMID:19217403, PMID:19217404]
- **Mis16 (SPCC970.12)**: Interaction via Mis16-BD for centromere targeting [PMID:19217404]
- **Mis18 (SPCC1672.10)**: Part of the Mis18 holocomplex pathway [PMID:19217403]
- **Self-interaction (SPAPB1A10.02)**: Reported IPI with itself [PMID:19217403]

## Annotation Review Considerations
- "protein binding" (GO:0005515) annotations should be replaced with more specific terms
- Histone chaperone activity is well-supported experimentally
- Zinc ion binding is supported by the CYS domain characterization
- The protein heterodimerization IEA may relate to histone fold but needs evaluation
- Scm3 is NOT a stable nucleosome component in S. pombe (unlike what was proposed for budding yeast)
