# KRTAP12-1 notes

Family-batched review of keratin-associated proteins (2026-10-24). KRTAP12-1 is a high-sulfur (HS) KAP12 family keratin-associated protein. No OpenScientist report was available; no deep research was run.

## Literature (verified, quotes verbatim from cached abstracts/full text)

- Characterises the KAP10/KAP12 domain and cuticle expression. [PMID:14962103 "revealed mRNA expression of nearly all KAP10 and KAP12 members exclusively in a narrow region of the middle portion of the hair fiber cuticle."]
- Independent description of the KRTAP12 cluster with hair-root-restricted expression. [PMID:15028290 "their expression was restricted to hair root cells (radix pili cells) and not found in 28 other tissues, including skin."]
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
