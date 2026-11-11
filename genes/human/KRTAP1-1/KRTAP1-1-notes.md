# KRTAP1-1 notes

Family-batched review of keratin-associated proteins (2026-10-24). KRTAP1-1 is a high-sulfur (HS) KAP1 family keratin-associated protein. No OpenScientist report was available; no deep research was run.

## Literature (verified, quotes verbatim from cached abstracts/full text)

- Defines the chromosome 17q12-21 KAP cluster that contains KAP1-KAP4 and KAP9 genes, with cortex expression by in situ hybridization. [PMID:11279113 "Hair follicle in situ hybridization data for single members of five different KAP multigene families all showed localization of the respective mRNAs to the upper cortex of the hair shaft."]
- Shows KAP1 family (including the KAP1.1 alleles) expression in the differentiated hair cortex. [PMID:11841537 "demonstrated the expression of this group in the differentiated portions of the hair cortex."]
- Establishes that KAP1.1A/1.6/1.7 are alleles of KRTAP1-1 and confirms cortex localization with a pan-KAP1 antibody. [PMID:12228244 "we have analyzed these eight hKAP1 genes in unrelated Japanese and Caucasian individuals and discovered that hKAP1.1A, hKAP1.6, and hKAP1.7 represent size polymorphisms of the hKAP1.1B gene."]
- Review of human KAP1 family domain structure. [PMID:12895003 "Keratin-associated proteins are involved in the formation of the cross-linked network of the keratin-intermediate filament proteins that support hair fibers."]
- Ovine KRTAP1-1 used as a candidate wool gene in population-diversity analysis. [PMID:21176141 "KRTAP1-1 (chromosome 11; a keratin-associated protein gene that encodes a protein KAP1-1 commonly found in wool)"]
- Single pharmacogenetic WGS association with SSRI remission in Korean MDD patients; not a hair phenotype and mechanism unexplained. [PMID:33633223 "A novel loss-of-function variant (rs3213755) in keratin-associated protein 1-1 (KRTAP1-1) was identified in this study."]
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
- Human disease/phenotype associations: none verified for hair disease. KRTAP1-1 rs3213755 was associated with SSRI remission in Korean MDD patients [PMID:33633223 "A novel loss-of-function variant (rs3213755) in keratin-associated protein 1-1 (KRTAP1-1) was identified in this study."].
## OpenScientist report (added during review)

- `KRTAP1-1-deep-research-openscientist.md` appeared during the review and was used as leads. Its identity mapping (KAP1.1/1.6/1.7) and cortex localization match PMID:11841537 and PMID:12228244. Its cysteine count (45/177, 25.4 mol%, 14 CC dipeptides) was recomputed from the UniProt sequence and agrees. Its HOXC13/DLX3 regulatory placement and livestock genetics are context only and were not turned into annotations. [file:human/KRTAP1-1/KRTAP1-1-deep-research-openscientist.md "it is a matrix protein of the hair-shaft cortex that becomes extensively disulfide (cystine) cross-linked to hard keratin intermediate filaments (IFs) and to neighbouring KAPs"]
