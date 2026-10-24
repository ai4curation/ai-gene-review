# KRTAP11-1 notes

Family-batched review of keratin-associated proteins (2026-10-24). KRTAP11-1 is a high-sulfur (HS) KAP11 family keratin-associated protein. No OpenScientist report was available; no deep research was run.

## Literature (verified, quotes verbatim from cached abstracts/full text)

- Defines the chromosome 21q22.1 domain containing KRTAP11-1. [PMID:12359730 "Based on amino acid sequence comparisons of the encoded proteins, the KAP genes could be divided into seven high glycine-tyrosine gene families (KAP6-KAP8, and KAP19-KAP22) and four high sulfur gene families (KAP11, KAP13, KAP15, and KAP23)."]
- Recombinant production of KAP11.1 for biophysics. [PMID:29391282 "we have expressed and purified a HS KAP (KAP11.1) and a HGT KAP (KAP6.1)."]
- Ovine KRTAP11-1 identification and variation. [PMID:21400094 "Keratin-associated proteins (KAPs) are a structural component of the wool fibre and form the matrix between the keratin intermediate filaments (KIFs)."]
- Rabbit Krtap11-1 overexpression in a cell line; mitochondrial localization prediction is inconsistent with the hair matrix role and not adopted. [PMID:32955717 "Krtap11-1 was confirmed to be a hydrophilic protein localized mostly in mitochondria."]
- Rogers et al. 2006 review of human KAP families (abstract only cached). [PMID:16939781 "This review describes the currently known human KAP families, their genomic organization, and their characteristics of expression."]
- Wu et al. 2008, molecular evolution of the KRTAP family in mammals (full text). [PMID:18721477 "In the hair cortex, hair keratins IFs are embedded in an in interfilamentous matrix, which consists of hair keratin-associated proteins (KATAP, usually abbreviated as KAP) [26]."]
- States the matrix and disulfide-stabilising role of KAPs. [PMID:29391282 "KAPs are the major constituent of the matrix between the hair keratin intermediate filaments (IFs), and stabilise hair structure by extensive disulfide bonding."]
- Review of human KAP1 family, with general statement of KAP role. [PMID:12895003 "Keratin-associated proteins are involved in the formation of the cross-linked network of the keratin-intermediate filament proteins that support hair fibers."]
- Sequence-repeat analysis of human KAPs and how they interact with IFs. [PMID:16713301 "This may give additional conformational flexibility to the chain and hence allow the A pentapeptides greater opportunity to interact appropriately with the IF via disulphide bonds, ionic interactions and/or hydrogen bonding."]
- Review of KRTAP evolution and use in wool breeding. [PMID:29797267 "KRTAP gene variants thus should provide information for improved wool by sheep and goat breeding."]

## Curation decisions

- All bare GO:0005515 protein binding rows (HuRI and related Y2H screens) REMOVED under the protein-binding policy; cysteine-rich KAPs are promiscuous Y2H preys.
- keratin filament (GO:0045095) accepted as the closest GO location for the keratin-associated interfilamentous matrix (added as NEW where the InterPro signature is absent).
- cytosol (ARBA IEA / Reactome TAS) kept as non-core: cytoplasmic but not the functional location.
- Core MF: structural constituent of cutaneous appendage (GO:0030281), verified in OLS (child of structural molecule activity). Generic GO:0005198 IEA rows MODIFIED to it; NEW elsewhere. QuickGO showed no current KRTAP carries GO:0030281.
- keratinization (GO:0031424) accepted/added: KAPs supply structure to the keratinizing hair cell (comparator: KRT81/KRT85/KRT86 carry it by IBA; KRTAP6-1/6-2/6-3 by IEA).
- hair cycle (GO:0042633) not proposed: KRTAP4 paralogues carry it by IBA/IDA (PMID:21916889, hair greying study), but KAPs are anagen-expressed products rather than participants in the cycle.
- Human disease/phenotype associations: none verified for hair disease. Ovine/caprine orthologue variants are associated with wool or cashmere traits where cited above.
