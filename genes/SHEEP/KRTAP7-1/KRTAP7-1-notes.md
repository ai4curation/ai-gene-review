# KRTAP7-1 (SHEEP) review notes

Family-batched review of mammalian keratin-associated proteins (KRTAPs). Evidence comes from UniProt, cached PubMed records and family reviews. An OpenScientist deep-research report (KRTAP7-1-deep-research-openscientist.md) arrived after the initial review and was integrated on 2026-10-24 (see below).

## Family-level evidence

- KAPs form the matrix cross-linking hair keratin IFs [PMID:16382671 "Hair keratin-associated proteins (KAP) are a major component of the hair fiber, and play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF), which are produced from hair keratins."]
- [PMID:22298953 "These filaments have a matrix surrounding them, that contains the keratin-associated proteins (KAPs), which cross-link with the IFs through extensive disulfide bonding"]
- Mammal-specific family [PMID:18721477 "These results indicate that the KRTAP gene clusters are unique to mammals and have been inserted into in the ancestral mammalian genome."]
- HGT function less clear [PMID:23791804 "While HS and UHS KAPs are known to function in disulfide bond crosslinking, the function of HGT KAPs remains unknown."]

## Gene-specific notes

- KRTAP7-1 has no GOA annotations at all; NEW rows were added for MF, CC and BP. Trait association evidence (PMID:31863114) is from Pakistani breeds, modest (P=0.017/0.024).

- [PMID:2439340 "We report the isolation and complete nucleotide sequence of genes encoding the two major high-(glycine + tyrosine) (HGT) keratins of sheep wool in separate genomic clones."]
- [PMID:27240405 "This KAP family contains only one family member designated KAP7-1"]
- [PMID:22044071 "The genes encoding the high glycine-tyrosine (HGT) KAPs are the first sub-group of KAP genes expressed in the wool follicle and just after expression of the keratin genes."]
- [PMID:31863114 "Variation in KRTAP7-1 was found to be associated with yield (P = 0.017)."]

## Curation decisions

- MF: GO:0030281 structural constituent of cutaneous appendage (OLS-verified; child of GO:0005198). ND root and IEA structural molecule activity rows refined to it.
- CC: GO:0045095 keratin filament (ACCEPT/NEW/MODIFY of ND root).
- BP: GO:0031424 keratinization; hair cycle/follicle development not used (KAPs are downstream structural products).
- No cytosol row in this gene's GOA (family convention where present: KEEP_AS_NON_CORE, synthesized in the cytoplasm but acting in the keratin matrix).
- ISO identical protein binding (HuRI Y2H donors): MARK_AS_OVER_ANNOTATED.
- No bare GO:0005515 rows in this gene's GOA.

## OpenScientist report integration (2026-10-24)

All quoted claims were checked against cached publications (PMID:25279319 and PMID:29797268 were fetched for this).

Verified:
- HGT class and orthocortex [PMID:25782086 "High glycine-tyrosine keratin-associated proteins (HGT-KAPs) are predominantly present in the orthocortex of wool fibres."]
- Ovine chromosome 1 cluster [PMID:25279319 "KRTAP11-1, KRTAP7-1, KRTAP8-1,KRTAP8-2, KRTAP6-2, KRTAP6-1, KRTAP13-3 and KRTAP24-1(in order from the centromere)"]
- KAP7 family reduced in straight wool [PMID:34859500 "specifically the KAP6, KAP7, and KAP8 families"]
- Staple-length association [PMID:31863114 "There was also an association between variation in KRTAP7-1 and MSL (P = 0.024)"]; single modest cohort of 222 Pakistani sheep, nominal P values.
- Nomenclature [PMID:22298953 "GenBank sequence JN091630 would"] (sentence continues on the next line in the cache).

Rejected or flagged:
- "Late" expression of KRTAP7-1 is extrapolated from KAP6 [PMID:7680040 "KAP6 expression starts relatively late in hair follicle differentiation"] and contradicts the KRTAP7-1-specific statement [PMID:22044071 "The genes encoding the high glycine-tyrosine (HGT) KAPs are the first sub-group of KAP genes expressed in the wool follicle and just after expression of the keratin genes."]. The review keeps the early-expression wording. Note the companion human KRTAP8-1 OpenScientist report says "early", so the two reports contradict each other on this point.
- Isodityrosine/di-tyrosine cross-linking and the flexibility-versus-rigidity table are speculation with no cited support; not used.
- The report concedes there is no KRTAP7-1-specific functional or immunolocalization data; the existing NEW MF/CC/BP rows already rest on UniProt and family-level evidence, so no actions changed.

Changes: report and PMID:25279319, PMID:25782086 added to references; report quotes added to the keratin filament row and the core function to record that localization and mechanism are class-level inferences.
