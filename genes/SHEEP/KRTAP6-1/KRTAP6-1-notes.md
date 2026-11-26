# KRTAP6-1 (SHEEP) review notes

Family-batched review of mammalian keratin-associated proteins (KRTAPs). No deep-research report was generated for this gene; evidence comes from UniProt, cached PubMed records and family reviews.

## Family-level evidence

- KAPs form the matrix cross-linking hair keratin IFs [PMID:16382671 "Hair keratin-associated proteins (KAP) are a major component of the hair fiber, and play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF), which are produced from hair keratins."]
- [PMID:22298953 "These filaments have a matrix surrounding them, that contains the keratin-associated proteins (KAPs), which cross-link with the IFs through extensive disulfide bonding"]
- Mammal-specific family [PMID:18721477 "These results indicate that the KRTAP gene clusters are unique to mammals and have been inserted into in the ancestral mammalian genome."]
- HGT function less clear [PMID:23791804 "While HS and UHS KAPs are known to function in disulfide bond crosslinking, the function of HGT KAPs remains unknown."]

## Gene-specific notes

- Fratini et al. 1993 (PMID:7680040) cloned ovine KAP6.1 [PMID:7680040 "The KAP6.1 gene encodes a basic protein of 82 amino acids"]; UniProt Q02958 is 83 aa (initiator Met count). Trait associations: PMID:25782086 (57-bp deletion, Merino-cross), PMID:31807662 (NZ Romney).

- [PMID:7680040 "Localization of KAP6 mRNAs in sheep wool and rabbit hair follicles by in situ hybridization suggests that the genes are expressed in the cells of the hair shaft cortex in varying expression patterns."]
- [PMID:25782086 "High glycine-tyrosine keratin-associated proteins (HGT-KAPs) are predominantly present in the orthocortex of wool fibres."]
- [PMID:25782086 "The results suggest that variation in ovine KRTAP6-1 affects wool fibre diameter-associated traits"]
- [PMID:31807662 "These results suggest that variation in KRTAP6-1 affects wool fibre diameter in NZ Romney ewes"]

## Curation decisions

- MF: GO:0030281 structural constituent of cutaneous appendage (OLS-verified; child of GO:0005198). ND root and IEA structural molecule activity rows refined to it.
- CC: GO:0045095 keratin filament (ACCEPT/NEW/MODIFY of ND root).
- BP: GO:0031424 keratinization; hair cycle/follicle development not used (KAPs are downstream structural products).
- No cytosol row in this gene's GOA (family convention where present: KEEP_AS_NON_CORE, synthesized in the cytoplasm but acting in the keratin matrix).
- ISO identical protein binding (HuRI Y2H donors): MARK_AS_OVER_ANNOTATED.
- No bare GO:0005515 rows in this gene's GOA.

## OpenScientist report (integrated)

`KRTAP6-1-deep-research-openscientist.md` was used as leads. Verified against cached abstracts:
- KRTAP6-1 is transcribed late in the keratogenous zone and in brush-end cortical cells [PMID:19272529 "Some genes (KRT27, KRT31, KRT85 and KRTAP6-1), but not others, were expressed in cortical cells forming the brush-end"].
- Recombinant KAP6.1 expressed and purified; KAPs aggregate in isolation [PMID:29391282 "they tend to be insoluble in isolation and are prone to forming aggregates in solution"] (species of KAP6.1 not stated in the abstract).
- KAP6/7/8 reduced in straight crimp-mutant wool (PMID:34859500).
- 57-bp deletion and fibre diameter (PMID:25782086).
Not independently re-run: the report's composition analysis and AlphaFold pLDDT (mean 37.4, fully disordered); consistent with a non-globular matrix protein but no annotation depends on it.
