# DCAF11 (Q8TEB1) review notes

## Identity
- DCAF11 = DDB1- and CUL4-associated factor 11; AltName WD repeat-containing protein 23 (WDR23). HGNC:20258. 546 aa, 7 WD40 repeats (UniProt Q8TEB1).
- Member of the DCAF family that serve as substrate-recognition receptors for the CRL4 (DDB1-CUL4-RBX1) cullin-RING E3 ubiquitin ligase.

## Core function: CRL4(DCAF11) substrate receptor
- Identified as a Ddb1- and Cul4-associated factor (DCAF). "we identify 18 Ddb1- and Cul4-associated factors (DCAFs), including 14 containing WD40 repeats. DCAFs interact with multiple surfaces on Ddb1, and the interaction of WD40-containing DCAFs with Ddb1 requires a conserved 'WDXR' motif." [PMID:16949367 "we identify 18 Ddb1- and Cul4-associated factors (DCAFs), including 14 containing WD40 repeats"]. DCAF11 co-purified with DDB1 and CUL4A by mass spectrometry; UniProt: "May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex" and "Interacts with DDB1 and CUL4A" (ECO:0000269|PubMed:16949367).
- Molecular architecture of DDB1-CUL4A E3 machinery, in which WD40 DCAFs dock on DDB1 as substrate receptors [PMID:16964240 "Molecular architecture and assembly of the DDB1-CUL4A ubiquitin ligase machinery"].
- ComplexPortal: CRL4-DCAF11 E3 ubiquitin ligase complex, CUL4A variant (CPX-2403) and CUL4B variant (CPX-2404) (UniProt DR lines).

## Substrates / biological roles
- NRF2/NFE2L2 degradation: "DCAF11 and DDB1-Cul4/Roc1 bind to the DIDLID sequence of the Neh2 domain of Nrf2 to mediate its degradation." DCAF11-specific siRNA increases Nrf2 protein, "indicating that DCAF11 is a functional E3-ubiquitin ligase for Nrf2." TFEB transcriptionally represses DCAF11 (CLEAR element in 5'-UTR), stabilizing Nrf2 [PMID:31586112]. (ComplexPortal annotates this paper to GO:0080135 regulation of cellular response to stress.)
- CENP-A degradation: "DCAF11 ... is the E3 ligase that specifically mediates the observed polyubiquitination" of phospho-Ser68 CENP-A; "Deletion of DCAF11 hampers CENP-A degradation and causes its mislocalization" during the cell cycle [PMID:34758320]. ComplexPortal links this to GO:1902412 regulation of mitotic cytokinesis (indirect; the paper is about CENP-A centromere homeostasis, not cytokinesis per se).
- p21/CDKN1A is reported in the broader literature as a CRL4(DCAF11) substrate (biological hint); not directly in the cached publications here.
- In C. elegans, the ortholog WDR-23 is the substrate receptor controlling the Nrf ortholog SKN-1 (background; the IBA transfer derives from WB:WBGene00008419 = wdr-23).

## Localization
- Nucleoplasm: IDA by HPA immunofluorescence (GO_REF:0000052) and Reactome TAS annotations placing the CRL4 complex (neddylation/CAND1/CSN cycle reactions) in nucleoplasm. Consistent with nuclear substrates (NRF2, CENP-A).

## Protein-binding (IPI) annotations — mostly generic GO:0005515
- PMID:16949367 IPI WITH DDB1/CUL4A/CUL4B (Q16531/Q13619/Q13620): the meaningful, specific interaction (CRL4 assembly). Captures DDB1/cullin binding (substrate-receptor docking).
- PMID:19109893, PMID:28514442, PMID:33961781, PMID:35271311 IPI WITH DDB1 (Q16531): large-scale interactome / structural studies; reduce to DDB1 binding, generic GO:0005515 over-annotated.
- PMID:22190034 WITH HIV vif (P12504, Xeno): viral hijack interactome screen, not endogenous function.
- PMID:27018634 WITH E. coli T3SS effector (Q8XB62): pathogen effector screen, not endogenous function.
- PMID:32296183 binary interactome: WITH AGR2, TNNI1, TNNI2, RCN1, GPSM1 — high-throughput Y2H partners, no functional follow-up; over-annotated.

## Annotation assessment summary
- ACCEPT: Cul4-RING E3 ubiquitin ligase complex (GO:0080008, IDA PMID:16949367 and IBA); proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161, IBA) as core ubiquitin-dependent degradation role; protein ubiquitination (GO:0016567).
- KEEP_AS_NON_CORE / accept: nucleoplasm localization (IDA HPA, Reactome TAS).
- MODIFY: bare protein binding for the DDB1/CUL4 interaction (PMID:16949367) -> ubiquitin-like ligase-substrate adaptor activity (GO:1990756), the informative MF capturing DCAF substrate-receptor role.
- MARK_AS_OVER_ANNOTATED: generic GO:0005515 from large-scale/viral/pathogen interactome screens.
- Cul4A-RING (GO:0031464) and Cul4B-RING (GO:0031465): ComplexPortal NAS, both supported (CPX-2403/2404); ACCEPT/KEEP as the complex exists in both CUL4A and CUL4B variants. Use the parent GO:0080008 as core.
- GO:0080135 regulation of cellular response to stress (NAS PMID:31586112): supported via NRF2/oxidative-stress axis; keep as non-core (downstream/indirect).
- GO:1902412 regulation of mitotic cytokinesis (NAS PMID:34758320): the paper concerns CENP-A centromere homeostasis, not cytokinesis directly; this is an imprecise/over-reaching label -> MARK_AS_OVER_ANNOTATED.
