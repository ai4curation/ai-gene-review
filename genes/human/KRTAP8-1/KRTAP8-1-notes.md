# KRTAP8-1 notes

Family-batched review of keratin-associated proteins (2026-10-24). KRTAP8-1 is a high glycine-tyrosine (HGT) KAP8 family keratin-associated protein. An OpenScientist deep-research report (KRTAP8-1-deep-research-openscientist.md) arrived after the initial review and was integrated on 2026-10-24 (see below).

## Literature (verified, quotes verbatim from cached abstracts/full text)

- Defines the chromosome 21q22.1 domain containing KRTAP8-1. [PMID:12359730 "Based on amino acid sequence comparisons of the encoded proteins, the KAP genes could be divided into seven high glycine-tyrosine gene families (KAP6-KAP8, and KAP19-KAP22) and four high sulfur gene families (KAP11, KAP13, KAP15, and KAP23)."]
- In vitro binding of KAP8.1 to the K85 head domain; abstract does not state the species of the recombinant proteins (human nomenclature is used). [PMID:23791804 "Western blot analysis and isothermal titration calorimetry (ITC) indicate that KAP8.1 binds to the head domain of K85, which is helically aligned around the axis of the intermediate filament (IF)."]
- Monoclonal antibody localization of KAP8.1 in human hair cortex. [PMID:30125694 "KAP8.1 was predominantly expressed in discrete regions of the keratinizing zone of the hair shaft cortex."]
- Structural modelling and spectroscopy of synthetic KAP8.1. [PMID:28289743 "The model for KAP8.1 is characterized by four strands of poly-proline II (or PPII) type helical secondary structures, held together by two cysteine disulphide bridges."]
- Ovine KRTAP7-1 and KRTAP8-1 variation. [PMID:22044071 "The genes encoding the high glycine-tyrosine (HGT) KAPs are the first sub-group of KAP genes expressed in the wool follicle and just after expression of the keratin genes."]
- Ovine KRTAP8-1 variant association with staple length and opacity. [PMID:34666626 "Variation in KRTAP8-1 was found to have strong association with MSL, OpSD and CVOp"]
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

## OpenScientist report integration (2026-10-24)

Checked every quoted claim against cached publications (fetched PMID:25279319, PMID:23135675 for this).

Verified (quotes match the cached sources):
- K85 head-domain binding and the proposed orthocortex helical IF arrangement [PMID:23791804 "we propose that the helical arrangement of IFs found in the orthocortex, which is uniquely distributed on the convex fiber side of the hair, is regulated by KAP8.1"]
- Linear epitope conserved across species [PMID:30125694 "the monoclonal antibody recognized a linear epitope shared among human, mouse, and sheep KAP8.1"]
- HGT class and single human KAP8 gene [PMID:25279319 "KAP8 is a HGT-KAP family and was believed to be coded for by a single gene in both humans and sheep."]
- HGT KAP genes expressed first [PMID:22044071 "The genes encoding the high glycine-tyrosine (HGT) KAPs are the first sub-group of KAP genes expressed in the wool follicle and just after expression of the keratin genes."]
- Orthocortical expression of Gly/Tyr-rich proteins [PMID:17697142 "proteins high in glycine and tyrosine tend to be expressed initially on the orthocortical side of the follicle"]

Rejected or flagged as over-stated:
- Desmoplakin ("bidirectional") binding is shown for "some HGT KAPs" in PMID:23791804, not specifically KAP8.1 [PMID:23791804 "Moreover, DPCT-C also binds to some HGT KAPs."]. The existing suggested question was reworded to match.
- Mouse Krtap16 is not an ortholog of KRTAP8-1; only the gene domain is orthologous [PMID:15385554 "a larger KAP gene domain on mouse chromosome 16 (MMU16) that is orthologous to a recently described HGT- and high sulfur (HS)-type KAP gene complex on human chromosome 21q22.11"]. HOXC13 control is shown by EMSA for Krtap16 only, so it is not asserted for KRTAP8-1.
- AlphaFold "fully disordered" claim conflicts with experimental spectroscopy and modelling [PMID:28289743 "The model for KAP8.1 is characterized by four strands of poly-proline II (or PPII) type helical secondary structures, held together by two cysteine disulphide bridges."]. Recorded as a suggested question; the description is unchanged.
- Ortholog alignment percentages and the aromatic-stacking adhesion model are the report's own analyses, not reproduced here; not used.

Species of the recombinant proteins in PMID:23791804: not stated in the abstract or the report; full text was not reachable (publisher returned 403). The GO:1990254 keratin filament binding NEW (IDA) row is kept with an explicit caveat in its reason: human origin is likely (human keratin nomenclature; the same group raised its antibody against human KAP8.1 [PMID:30125694 "we generated a monoclonal antibody against human KAP8.1"]) but unconfirmed. The mouse and sheep KRTAP8-1 reviews do not carry this term, which is consistent because they are different species.

No annotation actions changed as a result of the report; it was added as a reference and cited on the GO:1990254 row and the core function.
