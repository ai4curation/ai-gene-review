# Krtap5-4 (mouse) review notes

Family-batched review of mammalian keratin-associated proteins (KRTAPs). No deep-research report was generated for this gene; evidence comes from UniProt, cached PubMed records and family reviews.

## Family-level evidence

- KAPs form the matrix cross-linking hair keratin IFs [PMID:16382671 "Hair keratin-associated proteins (KAP) are a major component of the hair fiber, and play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF), which are produced from hair keratins."]
- [PMID:22298953 "These filaments have a matrix surrounding them, that contains the keratin-associated proteins (KAPs), which cross-link with the IFs through extensive disulfide bonding"]
- Mammal-specific family [PMID:18721477 "These results indicate that the KRTAP gene clusters are unique to mammals and have been inserted into in the ancestral mammalian genome."]
- HGT function less clear [PMID:23791804 "While HS and UHS KAPs are known to function in disulfide bond crosslinking, the function of HGT KAPs remains unknown."]

## Gene-specific notes

- Wood et al. 1990 (PMID:2250030) describe two murine serine-rich UHS genes (gUHS-SER-1, 230 aa; gUHS-SER-2, 223 aa); the 223-aa product matches Krtap5-4 (Q62220, 223 aa) [PMID:2250030 "gUHS-SER-2, encodes 223 amino acids with 41% cysteine and 21% serine"]. In situ signal was reported in medulla, inner root sheath and upper epidermis, whereas human KAP5 proteins are cuticle proteins [PMID:21712910 "we can now provide direct evidence for the presence of KAP 5"]; the mouse compartment assignment should be treated with caution (3'UTR probe, 1990 resolution).

- [PMID:2250030 "mRNA for the ultra high sulfur protein gene is found during the active phases of the hair cycle not only in the medulla and the inner root sheath of the forming hair but also in upper layers of the epidermis of skin."]

## Curation decisions

- MF: GO:0030281 structural constituent of cutaneous appendage (OLS-verified; child of GO:0005198). ND root and IEA structural molecule activity rows refined to it.
- CC: GO:0045095 keratin filament (ACCEPT/NEW/MODIFY of ND root).
- BP: GO:0031424 keratinization; hair cycle/follicle development not used (KAPs are downstream structural products).
- No cytosol row in this gene's GOA (family convention where present: KEEP_AS_NON_CORE, synthesized in the cytoplasm but acting in the keratin matrix).
- ISO identical protein binding (HuRI Y2H donors): MARK_AS_OVER_ANNOTATED.
- No bare GO:0005515 rows in this gene's GOA.
