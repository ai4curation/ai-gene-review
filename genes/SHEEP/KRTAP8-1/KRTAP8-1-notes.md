# KRTAP8-1 (SHEEP) review notes

Family-batched review of mammalian keratin-associated proteins (KRTAPs). No deep-research report was generated for this gene; evidence comes from UniProt, cached PubMed records and family reviews.

## Family-level evidence

- KAPs form the matrix cross-linking hair keratin IFs [PMID:16382671 "Hair keratin-associated proteins (KAP) are a major component of the hair fiber, and play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF), which are produced from hair keratins."]
- [PMID:22298953 "These filaments have a matrix surrounding them, that contains the keratin-associated proteins (KAPs), which cross-link with the IFs through extensive disulfide bonding"]
- Mammal-specific family [PMID:18721477 "These results indicate that the KRTAP gene clusters are unique to mammals and have been inserted into in the ancestral mammalian genome."]
- HGT function less clear [PMID:23791804 "While HS and UHS KAPs are known to function in disulfide bond crosslinking, the function of HGT KAPs remains unknown."]

## Gene-specific notes

- Protein sequence from wool (PMID:4735656, Dopheide 1973; no abstract cached). Matsunaga et al. 2013 (PMID:23791804) in-vitro KAP8.1-K85 head binding; species of the recombinant KAP8.1 not stated in the abstract, so no NEW keratin filament binding annotation was made.

- [PMID:2439340 "We report the isolation and complete nucleotide sequence of genes encoding the two major high-(glycine + tyrosine) (HGT) keratins of sheep wool in separate genomic clones."]
- [PMID:22044071 "The genes encoding the high glycine-tyrosine (HGT) KAPs are the first sub-group of KAP genes expressed in the wool follicle and just after expression of the keratin genes."]
- [PMID:34666626 "Variation in KRTAP8-1 was found to have strong association with MSL, OpSD and CVOp (p ≤ 0.027)."]

## Curation decisions

- MF: GO:0030281 structural constituent of cutaneous appendage (OLS-verified; child of GO:0005198). ND root and IEA structural molecule activity rows refined to it.
- CC: GO:0045095 keratin filament (ACCEPT/NEW/MODIFY of ND root).
- BP: GO:0031424 keratinization; hair cycle/follicle development not used (KAPs are downstream structural products).
- ARBA cytosol: KEEP_AS_NON_CORE, harmonized with the human KRTAP reviews (KAPs are synthesized in the cytoplasm of the keratinizing cell but act in the keratin matrix; true but not the site of function).
- ISO identical protein binding (HuRI Y2H donors): MARK_AS_OVER_ANNOTATED.
- No bare GO:0005515 rows in this gene's GOA.

## OpenScientist report (integrated)

`KRTAP8-1-deep-research-openscientist.md` appeared after the first draft and was used as leads. Verified items:
- KAP8.1 binds the K85 head domain in vitro [PMID:23791804 "KAP8.1 binds to the head domain of K85, which is helically aligned around the axis of the intermediate filament (IF)."]
- HGT proteins start on the orthocortical side [PMID:17697142 "proteins high in glycine and tyrosine tend to be expressed initially on the orthocortical side of the follicle"]
- Straight crimp-mutant wool has less KAP6/7/8 [PMID:34859500 "specifically the KAP6, KAP7, and KAP8 families"]
- KAP8.1 immunolocalization was done in human hair (PMID:30125694 title: "Structural behavior of keratin-associated protein 8.1 in human hair as revealed by a monoclonal antibody"), so it is not sheep evidence.
- Ovine KRTAP8-1 coding variant p.Tyr34Asn (PMID:22044071).
- Report's own sequence-composition analysis (4 Cys, Gly+Tyr ~40 mol%) was not independently re-run; consistent with the UniProt sequence.
Not adopted: the report's argument that aromatic stacking dominates over disulfides is a hypothesis (extrapolated from cysteine-free KAP36-1); no annotation depends on it.
