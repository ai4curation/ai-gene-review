# Krtap6-5 (mouse) review notes

Family-batched review of mammalian keratin-associated proteins (KRTAPs). No deep-research report was generated for this gene; evidence comes from UniProt, cached PubMed records and family reviews.

## Family-level evidence

- KAPs form the matrix cross-linking hair keratin IFs [PMID:16382671 "Hair keratin-associated proteins (KAP) are a major component of the hair fiber, and play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF), which are produced from hair keratins."]
- [PMID:22298953 "These filaments have a matrix surrounding them, that contains the keratin-associated proteins (KAPs), which cross-link with the IFs through extensive disulfide bonding"]
- Mammal-specific family [PMID:18721477 "These results indicate that the KRTAP gene clusters are unique to mammals and have been inserted into in the ancestral mammalian genome."]
- HGT function less clear [PMID:23791804 "While HS and UHS KAPs are known to function in disulfide bond crosslinking, the function of HGT KAPs remains unknown."]

## Gene-specific notes

- Krtap6-5 was described as Krtap16-8 in the Krtap16 complex (PMID:15385554, PMID:11290294). Expression is Hoxc13- and Gata3-regulated (UniProt INDUCTION).

- [PMID:15385554 "All Krtap16 genes exhibit strong expression in a narrowly defined pattern restricted to the lower and middle cortical region of the hair shaft in both developing and cycling hair."]

## Curation decisions

- MF: GO:0030281 structural constituent of cutaneous appendage (OLS-verified; child of GO:0005198). IEA structural molecule activity rows refined to it. ND rows: see the ND re-check below.
- CC: GO:0045095 keratin filament.
- BP: GO:0031424 keratinization; hair cycle/follicle development not used (KAPs are downstream structural products).
- No cytosol row in this gene's GOA (family convention where present: KEEP_AS_NON_CORE, synthesized in the cytoplasm but acting in the keratin matrix).
- ISO identical protein binding (HuRI Y2H donors): MARK_AS_OVER_ANNOTATED.
- No bare GO:0005515 rows in this gene's GOA.

## ND re-check (2026-11-14)

- PubMed searched 2026-11-14 through E-utilities, "Krtap6-5", "Krtap16-8" (its earlier name), "Krtap16" in All Fields: 4 hits for Krtap6-5: PMID:42081981 (Krtap6-5 among six proteins detected in mouse plasma only after blood-brain barrier opening, a biomarker list), PMID:38254984, PMID:34370022 and PMID:27045687 (sheep and goat KAP6 genes); 0 for Krtap16-8; for Krtap16 the 4 hits listed for the Krtap16 complex.
- No paper on mouse Krtap6-5 identifies a molecular function, biological process or cellular component of the protein. The ND rows therefore follow the evidence-code guideline and are ACCEPT with nd_case INFERABLE (projects/NO_DATA.md); the family-level terms they were earlier MODIFYed to are kept as NEW ISS rows. This replaces the MODIFY decisions of the first pass.
