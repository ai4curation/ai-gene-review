# CFAP61 Gene Review Notes

## Gene Overview

CFAP61 (Cilia- and flagella-associated protein 61; formerly C20orf26) encodes a 1237 amino acid protein (UniProt Q8NHU2) on chromosome 20. It is a conserved component of the calmodulin- and radial spoke-associated complex (CSC) in motile cilia and flagella.

## Key Literature Findings

### CSC complex composition and function

CFAP61 is the mammalian ortholog of Chlamydomonas FAP61 (also known as CaM-IP3). The CSC consists of three core proteins: FAP61, FAP91, and FAP251 (mammalian orthologs: CFAP61, CFAP91/MAATS1, CFAP251/WDR66) [PMID:21613541 "We previously identified a CaM and Spoke associated Complex (CSC) and provided evidence that this complex mediates regulatory signals between the radial spokes and dynein arms"; DOI:10.1091/mbc.E11-03-0271].

### Role in radial spoke 3 assembly (Tetrahymena)

In Tetrahymena, FAP61 and FAP251 are crucial for stable assembly of radial spoke 3 (RS3). Loss of FAP61 causes loss of an adjacent portion of the RS3 stem region, while FAP251 loss removes an arch-like density at the RS3 base [PMID:25694453 "loss of either FAP61 or FAP251 reduces cell swimming and affects the ciliary waveform and that RS3 is either missing or incomplete, whereas RS1 and RS2 are unaffected"; DOI:10.1091/mbc.E14-11-1545].

### CSC connects radial spokes, N-DRC, and dynein regulation

The CSC connects three major axonemal complexes: RS2, the nexin-dynein regulatory complex (N-DRC), and RS3 stand-in (RS3S). This provides a structural link for signal transduction from radial spokes to dynein motors [PMID:22740634 "the CSC connects three major axonemal complexes involved in dynein regulation: RS2, the nexin-dynein regulatory complex (N-DRC), and RS3S"; DOI:10.1091/mbc.E12-05-0357].

### CFAP61 in human sperm flagellum formation (Liu et al. 2021)

Liu et al. demonstrated CFAP61 is a conserved CSC component required for sperm flagellum formation. A splice variant (c.143+5G>A) causes MMAF phenotype. Cfap61 knockout mice recapitulate the infertility phenotype without other PCD symptoms. CFAP61 interacts with the CSC, radial spoke stalk and head. During early spermatid development, loss of CFAP61 impairs radial spoke component assembly [PMID:34792097 "CFAP61 is a conserved component of the calmodulin- and radial spoke-associated complex (CSC) of cilia... the assembly of radial spoke components is impaired. As spermiogenesis progresses, the axoneme in Cfap61-/- cells becomes unstable and scatters"; DOI:10.1242/dev.199805].

### CFAP61 mutations cause MMAF and male infertility (Ma et al. 2022)

Three Pakistani families with 11 infertile males carrying biallelic CFAP61 variants showed MMAF. TEM revealed severely disorganized axonemal ultrastructures with missing central pair, radial spokes, and inner dynein arms. Both CFAP61 and CFAP251 signals were absent from patient sperm tails [PMID:35174165 "CFAP61 and CFAP251 signals were absent from sperm tails of the patients, which suggested the loss of functional CSC in sperm flagella"; DOI:10.3389/fcell.2021.803818].

### Mouse Cfap61 knockout (Huang et al. 2020)

Cfap61 knockout mice show MMAF phenotype including short, coiled, and irregular flagella. Cfap61 initially localizes at the neck of sperm, functioning in flagellum formation, and later localizes to the midpiece [PMID:36659204 "Cfap61 is initially localized at the neck of sperm, where it potentially functions in flagellum formation, and is later localized to the midpiece of the sperm"; DOI:10.1016/j.scib.2020.01.023].

### OAT phenotype and additional variants (Hu et al. 2023)

Biallelic CFAP61 variants (p.R552C, p.D971N, splice site, p.G556R) were found in infertile men with severe oligoasthenoteratozoospermia. H&E and electron microscopy showed MMAF, absence of central pair microtubules, and mitochondrial sheath malformation [PMID:35387802 "CFAP61 is essential for spermatogenesis and that biallelic variants lead to male infertility in humans and mice with OAT"; DOI:10.1136/jmedgenet-2021-108249].

### Cfap91-dependent stability (Bicka et al. 2022)

In Tetrahymena, loss of Cfap91 causes significant reduction of RS3-specific proteins Cfap61 and Cfap251 at the axoneme level. This demonstrates interdependency among CSC components for radial spoke stability [PMID:36552811 "the level of RS3-specific proteins, Cfap61 and Cfap251, as well as RS2-associated Cfap206, are significantly diminished in CFAP91-KO cells"; DOI:10.3390/cells11244048].

### Proteomic identification in airway cilia (Blackburn et al. 2017)

CFAP61 was identified in quantitative proteomic analysis of human airway cilia, establishing its presence in respiratory motile cilia (not just sperm flagella) [PMID:28282151 "Quantitative Proteomic Analysis of Human Airway Cilia Identifies Previously Uncharacterized Proteins of High Abundance"; DOI:10.1021/acs.jproteome.6b00972].

### Testosterone/Leydig cell study (Zhu et al. 2023)

CFAP61 knockdown in Leydig cells reduced testosterone secretion via MAPK/COX-2 pathway. This study suggests broader roles beyond structural functions, though the physiological relevance and specificity of these in vitro findings remain uncertain [PMID:37982895 "CFAP61 knockdown reduced the Leydig cell viability and testosterone secretion and enhanced apoptosis"; DOI:10.1007/s10142-023-01271-1].

## Domain Architecture and Pseudoenzyme Status

### InterPro domain annotations for Q8NHU2:
- N-terminal domain (IPR032151/PF16092): residues 16-266 - CFAP61-specific N-terminal domain
- FAD/NAD(P)-binding domain superfamily (IPR036188): residues 665-998 - Rossmann-like fold
- CFAP61 dimerisation domain (IPR056299/PF23150): residues 1033-1151
- PANTHER family PTHR21178 spans nearly the entire protein (13-1235)

### BioReason-Pro analysis of pseudoenzyme status

The BioReason-Pro preprint (bioRxiv DOI:10.64898/2026.03.19.712954) highlights CFAP61 as an example of a protein with a domain architecture that superficially suggests enzymatic function. The Rossmann-like FAD/NAD(P)-binding superfamily fold (residues 665-998) could mislead domain-lookup pipelines into predicting oxidoreductase activity. However, BioReason-Pro correctly resolves this: the Rossmann-like domain is situated between an N-terminal axonemal targeting module and a C-terminal dimerization domain, all within a cilia-specific protein family. The model infers the Rossmann-like domain contributes a stable structural core for scaffolding interactions rather than catalysis.

### Assessment of pseudoenzyme claim

The term "pseudoenzyme" is used somewhat loosely here. CFAP61 has a Rossmann-like fold classified under the FAD/NAD(P)-binding superfamily (SUPFAM SSF51905), but this is a structural classification -- many proteins have Rossmann folds without being enzymes. There is NO evidence that CFAP61 has any catalytic activity, nor does UniProt annotate any enzymatic function. The protein has no metallopeptidase domain annotated in InterPro/Pfam. The HEXXH motif claim from the task description may be confused with another protein or may refer to a degenerate sequence motif within the Rossmann fold region that is not annotated as a metallopeptidase domain in current databases.

Key point: CFAP61 functions as a **structural scaffold** within the CSC complex, essential for radial spoke assembly and axoneme integrity. It has no known enzymatic function. The Rossmann-like fold likely provides a stable protein-protein interaction surface rather than catalytic activity.

## Interaction Partners (from UniProt, by similarity to mouse ortholog Q8CEL2)

- CFAP91/MAATS1 (CSC component)
- CFAP251/WDR66 (CSC component)
- ODAD2/ARMC4
- RSPH3A (radial spoke head)
- ROPN1, ROPN1L
- RSPH9 (radial spoke head)
- DYNLT1, DYNC1I2, TUBB3
- WDR35, IFT22, IFT81 (IFT proteins)
- CFAP70

## Disease Association

Spermatogenic failure 84 (SPGF84; MIM 620409): autosomal recessive male infertility with MMAF phenotype. Multiple pathogenic variants reported across different populations.

## Tissue Expression

According to HPA: tissue-enhanced expression in fallopian tube, heart muscle, skeletal muscle, testis. Consistent with presence in all motile cilia, not just sperm.

## Structural Data

PDB 8J07: cryo-EM structure at 4.10 A resolution. This shows the entire CFAP61 protein in context of the axonemal repeat.

## Missing Annotations / Gaps

1. No MF annotation in GOA - CFAP61 has no molecular function GO annotation
2. The UniProt GO section lists GO:0120317 (sperm mitochondrial sheath assembly) via IMP:MGI, but this is NOT in the GOA file for this protein
3. No annotation to radial spoke assembly (GO:0062177) despite this being a core function
4. No annotation to calmodulin-spoke associated complex (no GO term exists for CSC)
5. The ISS annotations transfer from Chlamydomonas/Tetrahymena orthologs but some are quite appropriate given the high conservation of CSC function
