# ALD2 (YMR170C, UniProt P47771) notes

## Identity
- Cytosolic, stress-inducible ALDH; tandem paralog of ALD3 [PMID:10407263 "We characterize here the tandem-repeated ORFs YMR170c and YMR169c as the cytoplasmic stress-inducible isoforms, with gene names ALD2 and ALD3, respectively."]
- UniProt: NAD+-dependent EC 1.2.1.3, 3-aminopropanal + NAD+ -> beta-alanine (RHEA:30695) [UniProt:P47771]

## Function
- Core: 3-aminopropanal -> beta-alanine for pantothenate/CoA [PMID:12586697 "This study presents evidence that the closely related aldehyde dehydrogenase genes ALD2 and ALD3 are required for pantothenic acid biosynthesis via conversion of 3-aminopropanal to beta-alanine in vivo."]
- 3-aminopropanal comes from polyamine oxidation by Fms1 [PMID:12586697 "yeast derive the beta-alanine required for pantothenic acid production via polyamine metabolism, mediated by the four SPE genes and by the FAD-dependent amine oxidase encoded by FMS1"]
- Ethanol: only weak phenotype [PMID:10407263 "The only phenotype detected in this mutant was a reduced growth rate in ethanol medium as compared to the wild type."]
- Not involved in fermentative acetate formation [PMID:15256563 "In contrast, the deletion of ALD2 or ALD3 had no effect on acetate production."]

## Curation observations
- YeastPathways RCA rows attach ALD2 to glucose fermentation / ethanol degradation; the fermentation link is contradicted by PMID:15256563.
- RCA GO:0008774 (acetylating, CoA-dependent ALDH) is a wrong reaction mapping: removed.
- RCA GO:0019658 bifid shunt (bifidobacterial pathway) is a superpathway artefact: removed.
