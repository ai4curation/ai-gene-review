# lon-8 (C. elegans) - Research Notes

## Gene Overview

lon-8 (Y59A8B.20, WBGene00013352) encodes a small (162 aa) secreted protein expressed in hypodermal syncytia (hyp4 and hyp7) from embryonic comma stage through adulthood. Loss-of-function mutations cause a Long (Lon) body size phenotype. The protein contains an N-terminal signal peptide (aa 1-23) and a BPTI-like nematode-specific domain (IPR057449, Pfam PF25315, BPTI_nem).

## Key Publication

PMID:17374156 (Soete et al., 2007, BMC Dev Biol) is the sole characterization paper.

### Body Size Phenotype
- lon-8 loss-of-function (hu187, hu188) causes increased body length [PMID:17374156 "Both alleles gave a clear Lon phenotype"]
- RNAi knockdown also increases body length: "1.3 +/- 0.08 mm in animals treated with control vector versus 1.4 +/- 0.08 mm in animals treated with lon-8 RNAi" [PMID:17374156]
- lon-8 mutants grow faster during larval development, comparable to lon-1(e185) [PMID:17374156 "throughout larval development, they outgrew their wild-type counterparts at a rate comparable to that of lon-1(e185) animals"]
- Growth rate slows after ~96 hours post-hatching, unlike lon-1 which continues [PMID:17374156 "lon-8 is more important for body size determination during larval elongation and early adult growth than later in life"]
- No change in hypodermal or seam cell nuclei count - increased cell size, not cell number [PMID:17374156 "the increase in body length of lon-8 animals correlates with an increase in cell size rather than cell number"]
- No increase in hypodermal ploidy (unlike lon-1) [PMID:17374156 "lon-8 does not have an obvious effect on the nuclear content of the hypodermis"]

### Male Tail Phenotype
- lon-8 mutants show grossly thickened, abnormal male rays [PMID:17374156 "All rays appear morphologically abnormal, but rays 5 and 6 are most severely affected"]
- Phenotype resembles Ram (Ray Abnormal Morphology) mutants [PMID:17374156 "This phenotype is most reminiscent of the phenotype of mutants in a class of 8 genes that give a Ray Abnormal Morphology (Ram) phenotype"]
- Males can still mate despite abnormal morphology [PMID:17374156 "lon-8(hu187) and lon-8(hu188) males can mate"]
- No spicule defects (unlike Sma/Mab pathway mutants) [PMID:17374156]

### Relationship to Sma/Mab (TGF-beta/BMP) Pathway
- lon-8 does NOT suppress dbl-1 or sma-6 Sma phenotype [PMID:17374156 "lon-8 is unlikely to be an important effector of DBL-1 signaling"]
- lon-8 is NOT transcriptionally regulated by the Sma/Mab pathway [PMID:17374156 "lon-8 is not transcriptionally regulated by the Sma/Mab pathway"]
- lon-8 functions INDEPENDENTLY of the Sma/Mab pathway [PMID:17374156]

### Genetic Interactions with Cuticle Modifying Enzymes
- dpy-11(RNAi) and dpy-18(RNAi) completely suppress the lon-8 body size phenotype [PMID:17374156 "both dpy-11(RNAi) and dpy-18(RNAi) completely suppress the lon-8 body size phenotype"]
- dpy-11 and dpy-18 encode cuticle collagen modifying enzymes
- This places lon-8 function in the cuticle collagen processing pathway

### Expression
- Transcriptional reporter: hyp4 and hyp7 syncytia [PMID:17374156]
- Earliest expression: comma stage embryos [PMID:17374156]
- In males: also in ventral tail hypodermal cells (V6.pppaa, T.aa, R6.p, T.apapa, R7.p, R8.p, R9.p) [PMID:17374156]
- LON-8 is secreted and diffuses from the hypodermis [PMID:17374156]

### Secretion
- Signal peptide present (aa 1-23) [PMID:17374156]
- When signal peptide is included in reporter, GFP is secreted and diffuses [PMID:17374156]
- hu187 allele lacks signal peptide and is non-functional [PMID:17374156]

### Conservation
- Nematode-specific protein; homologs in C. briggsae, H. contortus, P. pacificus, P. trichosuri, M. incognita, B. malayi [PMID:17374156]
- All homologs have predicted signal peptides despite divergent N-terminal sequences [PMID:17374156]

## Domain Architecture

UniProt lists: IPR057449 (BPTI-like, C-terminal domain, nematode-specific), Pfam PF25315 (BPTI_nem). This is a nematode-specific variant of the BPTI/Kunitz superfamily fold. Note: this is NOT the classical Kunitz/BPTI domain (PF00014) but rather a nematode-specific clade (PF25315).

Other C. elegans Kunitz-domain cuticle proteins include:
- BLI-5: Kunitz domain protein involved in cuticle collagen biosynthesis; interacts with BLI-4 subtilisin-like protease; biochemically shown to ACTIVATE (not inhibit) serine proteases [PMID:19716386]
- MLT-11: Large Kunitz domain protein (10 Kunitz domains) required for cuticle patterning and molting; regulated by NHR-23 [PMID:38766248]

## Critical Assessment of BioReason Predictions

### BioReason Claimed GO:0005201 (extracellular matrix structural constituent)
This is speculative. There is no evidence that LON-8 is a structural component of the ECM. The paper says LON-8 is secreted and diffuses; there is no evidence of matrix integration. The genetic interaction with cuticle collagen modifying enzymes suggests it influences cuticle composition but not necessarily as a structural constituent.

### BioReason Claimed GO:0005604 (basement membrane)
This is WRONG. The paper never mentions basement membrane. LON-8 is secreted from the hypodermis into the extracellular space, likely interacting with the cuticle (apical ECM), not the basement membrane (basal ECM). The existing GOA annotation of cuticular extracellular matrix (GO:0060102) is more appropriate.

### BioReason Claimed "receptor engagement" and "cell proliferation"
The paper explicitly states: "the increase in body length of lon-8 animals correlates with an increase in cell size rather than cell number" and there is no evidence of receptor engagement or signaling activity. The UniProt summary mentions "modulating cell proliferation through interaction with one or more cell surface receptors" but this is stated as a hypothesis, not demonstrated.

### BioReason Claimed partners: "Col_cuticle_N domain-containing protein, ZP domain-containing protein, and cuticle collagen lon-3"
No interaction data for LON-8 with any of these proteins exists in the literature. The only genetic interactions demonstrated are with dpy-11 and dpy-18 (cuticle collagen modifying enzymes), not direct protein-protein interactions with collagens.
