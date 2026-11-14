# Krtap15-1 (mouse) review notes

Family-batched review of mammalian keratin-associated proteins (KRTAPs). No deep-research report was generated for this gene; evidence comes from UniProt, cached PubMed records and family reviews.

## Family-level evidence

- KAPs form the matrix cross-linking hair keratin IFs [PMID:16382671 "Hair keratin-associated proteins (KAP) are a major component of the hair fiber, and play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF), which are produced from hair keratins."]
- [PMID:22298953 "These filaments have a matrix surrounding them, that contains the keratin-associated proteins (KAPs), which cross-link with the IFs through extensive disulfide bonding"]
- Mammal-specific family [PMID:18721477 "These results indicate that the KRTAP gene clusters are unique to mammals and have been inserted into in the ancestral mammalian genome."]
- HGT function less clear [PMID:23791804 "While HS and UHS KAPs are known to function in disulfide bond crosslinking, the function of HGT KAPs remains unknown."]

## Gene-specific notes

- Krtap15-1 = pmg-2 (PMID:10446281). Expression was shown at RNA level only.

- [PMID:10446281 "Both genes are expressed in growing hair follicles in skin as well as in sebaceous and eccrine sweat glands."]

## Curation decisions

- MF: GO:0030281 structural constituent of cutaneous appendage (OLS-verified; child of GO:0005198). IEA structural molecule activity rows refined to it. ND rows: see the ND re-check below.
- CC: GO:0045095 keratin filament.
- BP: GO:0031424 keratinization; hair cycle/follicle development not used (KAPs are downstream structural products).
- ARBA cytosol: KEEP_AS_NON_CORE, harmonized with the human KRTAP reviews (KAPs are synthesized in the cytoplasm of the keratinizing cell but act in the keratin matrix; true but not the site of function).
- ISO identical protein binding (HuRI Y2H donors): MARK_AS_OVER_ANNOTATED.
- No bare GO:0005515 rows in this gene's GOA.

## ND re-check (2026-11-14)

- PubMed searched 2026-11-14 through E-utilities, "Krtap15-1", "pmg-2" in All Fields: 4 hits for Krtap15-1, all on goat or sheep KAP15-1 (PMID:41164236, PMID:39409811, PMID:36212123, PMID:31807622); of 8 hits for pmg-2 the only relevant one is PMID:10446281 (RNA expression of pmg-1 and pmg-2).
- No paper on mouse Krtap15-1 identifies a molecular function, biological process or cellular component of the protein. The ND rows therefore follow the evidence-code guideline and are ACCEPT with nd_case INFERABLE (projects/NO_DATA.md); the family-level terms they were earlier MODIFYed to are kept as NEW ISS rows. This replaces the MODIFY decisions of the first pass.
