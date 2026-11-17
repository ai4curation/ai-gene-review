# Krtap29-1 (mouse) review notes

Family-batched review of mammalian keratin-associated proteins (KRTAPs). No deep-research report was generated for this gene; evidence comes from UniProt, cached PubMed records and family reviews.

## Family-level evidence

- KAPs form the matrix cross-linking hair keratin IFs [PMID:16382671 "Hair keratin-associated proteins (KAP) are a major component of the hair fiber, and play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF), which are produced from hair keratins."]
- [PMID:22298953 "These filaments have a matrix surrounding them, that contains the keratin-associated proteins (KAPs), which cross-link with the IFs through extensive disulfide bonding"]
- Mammal-specific family [PMID:18721477 "These results indicate that the KRTAP gene clusters are unique to mammals and have been inserted into in the ancestral mammalian genome."]
- HGT function less clear [PMID:23791804 "While HS and UHS KAPs are known to function in disulfide bond crosslinking, the function of HGT KAPs remains unknown."]

## Gene-specific notes

- Krtap29-1 is PE 3 (inferred from homology), with no FUNCTION text in UniProt and only a genome-assembly reference (PMID:19468303). All annotations in this review are family-level inferences; the family-level terms on its NEW ISS rows are therefore lower-confidence than for the transcript-supported KAPs.


## Curation decisions

- MF: GO:0030281 structural constituent of cutaneous appendage (OLS-verified; child of GO:0005198). IEA structural molecule activity rows refined to it. ND rows: see the ND re-check below.
- CC: GO:0045095 keratin filament.
- BP: GO:0031424 keratinization; hair cycle/follicle development not used (KAPs are downstream structural products).
- No cytosol row in this gene's GOA (family convention where present: KEEP_AS_NON_CORE, synthesized in the cytoplasm but acting in the keratin matrix).
- ISO identical protein binding (HuRI Y2H donors): MARK_AS_OVER_ANNOTATED.
- No bare GO:0005515 rows in this gene's GOA.

## ND re-check (2026-11-14)

- PubMed searched 2026-11-14 through E-utilities, "Krtap29-1", "keratin associated protein 29-1" in All Fields: 0 hits for either.
- No paper on mouse Krtap29-1 identifies a molecular function, biological process or cellular component of the protein. The ND rows therefore follow the evidence-code guideline and are ACCEPT with nd_case INFERABLE (projects/NO_DATA.md); the family-level terms they were earlier MODIFYed to are kept as NEW ISS rows. This replaces the MODIFY decisions of the first pass.
