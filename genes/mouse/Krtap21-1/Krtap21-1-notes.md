# Krtap21-1 (mouse) review notes

Family-batched review of mammalian keratin-associated proteins (KRTAPs). No deep-research report was generated for this gene; evidence comes from UniProt, cached PubMed records and family reviews.

## Family-level evidence

- KAPs form the matrix cross-linking hair keratin IFs [PMID:16382671 "Hair keratin-associated proteins (KAP) are a major component of the hair fiber, and play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF), which are produced from hair keratins."]
- [PMID:22298953 "These filaments have a matrix surrounding them, that contains the keratin-associated proteins (KAPs), which cross-link with the IFs through extensive disulfide bonding"]
- Mammal-specific family [PMID:18721477 "These results indicate that the KRTAP gene clusters are unique to mammals and have been inserted into in the ancestral mammalian genome."]
- HGT function less clear [PMID:23791804 "While HS and UHS KAPs are known to function in disulfide bond crosslinking, the function of HGT KAPs remains unknown."]

## Gene-specific notes

- All ten GOA rows citing PMID:17151017 (Kurek et al. 2007, Gata3 conditional knockout) are attached to Krtap21-1, with WITH/FROM MGI:3696958. MGI resolves MGI:3696958 to a Gata3 targeted allele (Gata3<tm3Gsv>, page title 'Gata3 Targeted Allele Detail MGI Mouse (MGI:3696958)'), checked 2026-10-24. QuickGO lists no Gata3 (MGI:95663) annotations from this paper. The phenotypes (delayed hair growth, abnormal follicle organization, pigmentation, postnatal growth) are those of the Gata3 mutant; Krtap21-1 appears in the paper only as a Gata3-dependent transcript (UniProt INDUCTION). Recorded as a WRONG_GENE_PRODUCT source defect for MGI. The IBA hair follicle development row (PTN002526071) lists only Krtap21-1 (MGI:2157767) as experimental donor, i.e. it was seeded by the mis-attached IMP.

- [PMID:15385554 "All Krtap16 genes exhibit strong expression in a narrowly defined pattern restricted to the lower and middle cortical region of the hair shaft in both developing and cycling hair."]

## Curation decisions

- MF: GO:0030281 structural constituent of cutaneous appendage (OLS-verified; child of GO:0005198). ND root and IEA structural molecule activity rows refined to it.
- CC: GO:0045095 keratin filament (ACCEPT/NEW/MODIFY of ND root).
- BP: GO:0031424 keratinization; hair cycle/follicle development not used (KAPs are downstream structural products).
- No cytosol row in this gene's GOA (family convention where present: KEEP_AS_NON_CORE, synthesized in the cytoplasm but acting in the keratin matrix).
- ISO identical protein binding (HuRI Y2H donors): MARK_AS_OVER_ANNOTATED.
- No bare GO:0005515 rows in this gene's GOA.
