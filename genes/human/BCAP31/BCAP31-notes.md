# BCAP31 Review Notes

## Gene Identity

- Human BCAP31 encodes B-cell receptor-associated protein 31, also known as BAP31, UniProt P51572.
- The UniProt record describes BCAP31 as a 246 aa, reviewed Swiss-Prot ER membrane protein with three transmembrane segments and a cytosolic C-terminal domain. UniProt summarizes it as a chaperone protein involved in ER export, recognition of abnormally folded proteins, ERAD targeting, and TOMM40-dependent mitochondrial complex I assembly [UniProt:P51572 "Functions as a chaperone protein"].

## Core Functional Picture

BCAP31 is best curated as an ER-resident membrane protein-sorting factor with three linked roles:

1. ER cargo selection and export of selected membrane proteins.
2. ER quality control and ER-associated degradation of misfolded membrane proteins.
3. ER-mitochondria contact site function that supports mitochondrial complex I component import.

The ERAD role is directly supported by the Cell paper showing that BAP31 binds Sec61beta and TRAM, associates with CFTRDeltaF508, and promotes retrotranslocation and proteasomal degradation [PMID:18555783 "BAP31 is an endoplasmic reticulum protein-sorting factor"; PMID:18555783 "promotes its retrotranslocation from the ER and degradation by the cytoplasmic 26S proteasome system"]. This supports keeping the positive regulation annotations and adding the direct ERAD pathway annotation (GO:0036503).

The ER-mitochondria contact role is supported by the Tom40 study: BAP31 forms an ER-mitochondria bridging complex and stimulates NDUFS4 translocation to mitochondria for complex I assembly [PMID:31206022 "BAP31 acts as a key factor in mitochondrial homeostasis"; PMID:31206022 "interacts with mitochondria-localized proteins, including Tom40"]. This supports the MAM localization and protein localization to mitochondrion annotations as core/non-incidental.

## Localization Calls

The primary localization is ER membrane. The early BAP31 paper identifies p28 Bap31 as a polytopic ER protein [PMID:9334338 "polytopic integral protein of the endoplasmic reticulum"], and UniProt also states ER membrane plus ERGIC/cis-Golgi shuttling [UniProt:P51572 "May shuttle between the ER and the intermediate compartment/cis-Golgi complex"].

ERGIC/Golgi membrane annotations are acceptable as trafficking-related localizations, but ER membrane is the core site. Lipid droplet annotation is treated as non-core because the cited study is a lipid droplet fraction proteomics experiment in HuH7 cells, not a mechanistic BCAP31 localization paper [PMID:14741744 "a fraction enriched with lipid droplets was isolated"]. Plasma membrane remains undecided because the original surface-antigen study supports antibody-accessible surface expression [PMID:8706661 "expression of a 28-kDa surface protein"], but later work establishes ER/ERGIC residency as the primary biology.

## Apoptosis Annotations

BCAP31 is a caspase substrate and ER-mitochondria apoptosis platform component, but broad apoptosis annotations overstate the intact protein's core function. The original Bap31 apoptosis paper shows caspase cleavage and the p20 fragment, not a constitutive apoptotic regulator function for intact BCAP31 [PMID:9334338 "cleavage of p28 at the two caspase recognition sites"; PMID:9334338 "p20 fragment induces apoptosis"]. The Fis1 paper similarly frames the event as Fis1 facilitating Bap31 cleavage into p20Bap31 [PMID:21183955 "facilitating its cleavage into the pro-apoptotic p20Bap31"].

Therefore:

- Broad apoptotic process and positive regulation of intrinsic apoptotic signaling pathway are marked over-annotated.
- ER-mitochondria contact and stress sensor annotations from PMID:31206022 remain supported.

## Protein Binding Annotations

Generic protein binding rows should be removed. BCAP31 has many real interactors, including Sec61beta, TRAM, Derlin-1, CFTR, BCL2, CASP8, Fis1, TOMM40, and viral SH protein, but GO:0005515 does not capture the function. The biologically informative terms are ERAD pathway/regulation, retrograde ER-to-cytosol transport, ER-to-Golgi transport, MHC class I protein binding, MAM localization, and mitochondrial protein localization.

## New Term Rationale

GO:0036503 ERAD pathway is justified because the strongest mechanistic evidence places BCAP31 directly in the ERAD substrate-handling pathway rather than only upstream regulation. PMID:18555783 shows BCAP31 associating with the misfolded CFTRDeltaF508 substrate, Sec61 translocon components, and Derlin-1, and reducing BAP31 reduces proteasomal degradation [PMID:18555783 "Depletion of BAP31 reduces the proteasomal degradation of DeltaF508"; PMID:18555783 "associates physically and functionally with the Derlin-1 protein disclocation complex"].

## Open Questions

- Which BCAP31 client proteins are physiologically most important in neurons and oligodendrocyte lineage cells affected in DDCH syndrome?
- Can separation-of-function variants distinguish the ERAD/cargo-export role from the TOMM40/MAM mitochondrial homeostasis role?
- Are the apoptosis annotations better represented by annotations to the p20 cleavage product context, or should they remain pathway-context-only references rather than BCAP31 core function terms?

## Resolution Notes

- The plasma membrane (`GO:0005886`) call referenced under "Localization Calls" was resolved as `MARK_AS_OVER_ANNOTATED` in PR #317. The PMID:8706661 surface-antigen detection is real but represents a trafficking intermediate / overexpression artifact in transfected cells; later work establishes ER/ERGIC residency as the primary biology, consistent with the cytoplasmic KKXX retrieval motif.
- The clathrin-coated vesicle (`GO:0030136`) IEA was resolved as `MARK_AS_OVER_ANNOTATED` in the same PR — Ensembl rat transfer with no human-specific support, and BCAP31 traffics via COPI/COPII machinery rather than the clathrin pathway.
