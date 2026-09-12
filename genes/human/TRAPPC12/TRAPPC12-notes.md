# TRAPPC12 review notes

TRAPPC12, also called TRAMM/TTC-15, has two directly supported functional tracks: TRAPP-mediated membrane traffic and a moonlighting mitotic kinetochore role. Scrivens et al. identify TTC-15 as TRAPPC12 and state that C11/C12 are bona fide TRAPP components involved in early ER-to-Golgi trafficking [PMID:21525244 "TTC-15 (now designated TRAPPC12)" and "ER-to-Golgi trafficking at a very early stage"].

TRAPP membership is directly supported by TRAPP purifications and coimmunoprecipitation. TRAPPC11 and TRAPPC12 interact with each other and known TRAPP subunits, and newly identified proteins are stable TRAPP interactors [PMID:21525244 "C4orf41 and TTC-15 interact both with each other and with previously characterized TRAPP subunits" and "These results firmly establish the newly identified proteins as stable TRAPP interactors"].

TRAPPC12 localizes in TRAPP/early secretory contexts. Endogenous C12 elutes in a high-molecular-weight TRAPP pool and a second smaller pool, consistent with the dual biology later described for TRAMM [PMID:21525244 "endogenous C12 was observed to elute in the same high-molecular-weight pool as TRAPP" and PMID:25918224 "TRAMM cycles between its role in TRAPP in interphase cells, and its newly identified roles during mitosis"].

TRAPPC12 supports ER-to-ERGIC/Golgi traffic rather than COPII coat assembly per se. C12 knockdown causes fragmented Golgi, C11/C12 knockdown arrests cargo in a BFA-resistant ERGIC-associated compartment, and the authors model TRAPP function at ER exit or peripheral ERGIC elements [PMID:21525244 "RNAi against C8, C11, or C12 resulted in Golgi fragmentation", "knockdowns of either C11 or C12 arrest a cargo protein in a BFA-resistant compartment", and "TRAPP functions either at ER exit sites or at peripheral ERGIC (BFA-resistant) elements"].

The PN TRAPP leaf is autophagy-contextual but maps to TRAPP complex membership. For TRAPPC12, I am not adding a direct autophagy annotation: the direct seeded records support TRAPP/TRAPPIII membership and early secretory trafficking, while autophagy is represented by TRAPPIII/RAB1 context only [PMID:27066478 "TRAPP III, which contains core TRAPP plus TrappC8, 11-13"; Reactome:R-HSA-8877475 "RAB1 nucleotide exchange is stimulated in these pathways by the GEF activity of the multisubunit TRAPPC complexes II and III"].

The mitosis paper provides direct, full-text support for TRAPPC12/TRAMM nuclear/kinetochore and chromosome-congression annotations. TRAMM depletion causes noncongressed chromosomes and mitotic arrest, TRAMM weakly associates with chromosomes/kinetochores, and TRAMM regulates CENP-E recruitment to kinetochores [PMID:25918224 "Depletion of TRAMM resulted in noncongressed chromosomes", "Small amounts of TRAMM associated with chromosomes", and "prevented the recruitment of CENP-E to the kinetochore"].

The CENP-E interaction is real but the generic GO term `protein binding` is not an informative representation of TRAPPC12 function. The better GO representation is positive regulation of protein localization to kinetochore, regulation of kinetochore assembly, and metaphase chromosome alignment [PMID:25918224 "TRAMM affects the localization of some components of the outer layer of the kinetochore" and "TRAMM was able to recruit more CENP-E to kinetochores"].

The TRAPPC12 disease paper is cached as abstract-only. It supports Golgi dysfunction and delayed ER-to-Golgi/Golgi transport, but I am using it only as secondary support [PMID:28777934 "Fibroblasts derived from all three individuals showed a fragmented Golgi" and "Protein transport from the endoplasmic reticulum to and through the Golgi was delayed"].

The fetched PANTHER family metadata for PTHR21581 is labeled "D-alanyl-D-alanine Carboxypeptidase", which does not match TRAPPC12/TRAMM biology. I am not using that artifact as functional evidence for this review.

Falcon deep research was requested with `just deep-research-falcon human TRAPPC12`, but the provider timed out after 600 seconds and no `TRAPPC12-deep-research-falcon.md` file was produced. I am completing the review using the cached primary literature, UniProt record, GOA seed, and Reactome context described above.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording framed TRAPPC12 in the Proteostasis Network TRAPP bucket, where its shared gene-level semantics are TRAPP/TRAPPII/TRAPPIII complex membership and TRAPP/RAB1 trafficking, not a direct TRAPPC12-specific autophagy annotation.
