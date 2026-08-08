# Manual literature synthesis for human ARSI

## Why this file exists

Automated deep research was attempted on 2026-07-18. Falcon failed with HTTP 402 and the Perplexity-lite fallback failed with HTTP 401. This manually curated synthesis records the literature conclusions used for the review.

## Evidence synthesis

### Catalytic identity

ARSI is a SUMF1-activated class I sulfatase. The 2009 human ARPE-19 study showed neutral-pH activity against artificial 4-methylumbelliferyl sulfate only when ARSI and SUMF1 were coexpressed, and the C93S mutant lacked activity [PMID:19262745 "When ARSI-FLAG and SUMF1-FLAG were coexpressed, the conditioned medium of the transfected cells showed arylsulfatase activity at a range of neutral pH"] [PMID:19262745 "The conditioned media of ARSI-C93S-FLAG-expressed cells coexpressed with SUMF1-FLAG showed no ARS activity"].

The 2026 Matrix Biology paper supplies the decisive natural-substrate result: human ARSI overexpression lowered cellular C4S, Arsi knockout increased C4S, and purified SUMF1-activated human ARSI desulfated GalNAc4S but not GalNAc6S. The cached abstract states that [PMID:41916471 "Biochemical analyses of ARSI gain and loss of function cell lines and isolated cell-free systems revealed that ARSI is a novel chondroitin endosulfatase, specifically desulfating chondroitin-4-sulfate at pH 4.5"]. This supports the specific GO term GO:0003943 rather than relying only on broad arylsulfatase or sulfuric-ester-hydrolase terms.

### Functional compartment

The 2009 study observed FLAG-tagged ARSI in ER and medium [PMID:19262745 "Transiently produced ARSI-FLAG was localized to the endoplasmic reticulum and was detected in the cellular fraction and the medium"]. The study used transient overexpression and itself discussed instability, degradation, and ER retention, so these observations do not establish that extracellular space is the principal native compartment.

The later study localized human ARSI with lysosomal/endosomal markers and found altered lysosome abundance and size after Arsi loss in chondrocytes. Its abstract reports [PMID:41916471 "Colocalization studies suggested that ARSI is lysosomal, and lysosome homeostasis was altered in ARSI loss of function chondrocytes"]. Acidic pH preference for GalNAc4S further coheres with lysosomal function. Lysosome is thus the core functional location, while ER lumen is a biosynthetic/formylglycine-maturation location and extracellular region remains non-core overexpression evidence.

### Cartilage role

ARSI abundance rises during chondrocyte maturation in multiple vertebrate models. Rat chondrocyte Arsi knockout increased maturation-marker expression, including after FGF18 induction [PMID:41916471 "Finally, Arsi knockout in RCS chondrocytes caused increased expression of maturation genes, such as Col10a1 and Mmp13"]. This supports negative regulation of chondrocyte differentiation, but because the perturbation evidence is from rat cells the human annotation should use ISS.

### Interaction and disease boundaries

The KRT40 interaction comes from a systematic binary interactome map [PMID:25416956 "we describe a systematic map of ?14,000 high-quality human binary protein-protein interactions"]. It has no ARSI-specific physiological validation and does not justify generic protein binding as an informative core function.

The 2014 exome study included ARSI among putative HSP candidates but its abstract frames the output as candidate discovery [PMID:24482476 "identified 18 previously unknown putative HSP genes and validated nearly all of these genes functionally or genetically"]. Without accessible ARSI-specific segregation and functional details, the SPG66 association is noted as unresolved and is not converted to GO biology.

## Curation conclusion

ARSI is best modeled as a lysosomal, SUMF1-dependent N-acetylgalactosamine-4-sulfatase that removes terminal 4-sulfate from chondroitin/dermatan sulfate chains and restrains chondrocyte maturation in experimental vertebrate cartilage systems. The older extracellular neutral-pH model was informative but is no longer the strongest account of its core physiological compartment and substrate.

The physiological human proteoglycan substrates and the significance of a possible extracellular pool remain unresolved.
