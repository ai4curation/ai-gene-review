# IFT122 notes

## Summary
IFT122 is a core-subcomplex subunit of IFT-A (IFT122/IFT140/IFT144 core; IFT43/IFT121/IFT139 periphery).
- Subcomplex architecture: [PMID:27932497 "the IFT-A complex is divided into a core subcomplex, composed of IFT122/IFT140/IFT144, which is associated with TULP3, and a peripheral subcomplex, composed of IFT43/IFT121/IFT139"]
- Linchpin role: [PMID:29220510 "As the IFT122 subunit connects the core and peripheral subcomplexes of the IFT-A complex, it is expected to play a pivotal role in the complex."]
- Ciliogenesis: IFT122 KO is unusual among IFT-A subunits [PMID:29220510 "knockout (KO) of the IFT122 gene in hTERT-RPE1 cells using the CRISPR/Cas9 system led to a severe ciliogenesis defect, whereas KO of other IFT-A genes had minor effects on ciliogenesis but impaired ciliary protein trafficking"]
- Membrane cargo import with TULP3: [PMID:20889716 "IFT-A is linked to retrograde ciliary transport, but, surprisingly, we find that the IFT-A complex has a second role directing ciliary entry of TULP3."]; structure [PMID:36775821 "TULP3, the cargo adapter, interacts with IFT-A through its N-terminal region, and interface mutations disrupt cargo transport."]
- Hedgehog: [PMID:20889716 "TULP3 and IFT-A proteins both negatively regulate Hedgehog signaling in the mouse embryo"]
- Disease: cranioectodermal dysplasia 1 (UniProt).

## Curation decisions
- protein binding (IPI, IFT-A partners / HIV AP-MS / IFTAP): REMOVE as uninformative; IFT-A membership captured by GO:0030991.
- Mouse ISS developmental terms (neural tube closure, limb, heart tube, eye, D/V patterning): KEEP_AS_NON_CORE; embryonic body morphogenesis and intracellular signal transduction MARK_AS_OVER_ANNOTATED.
- NK-cell membrane HDA: MARK_AS_OVER_ANNOTATED.
- Intraciliary anterograde transport IDA (20889716, 40472089): ACCEPT; IFT-A mediates ciliary entry of membrane cargo. The 40472089 full text only shows TULP3-dependent GPR45 entry and cites IFT-A as the TULP3 partner [PMID:40472089 "TUB and TULP3 function as adapters of the highly conserved intraflagellar complex-A (IFT-A) complex in ciliary trafficking"]; deferred to curator.
- protein carrier activity (contributes_to): ACCEPT, core (GO now labels GO:0140597 "protein carrier chaperone").

## HPA cilium atlas vs module role
- HPA v25 (Hansen et al. 2025, PMID:41005307): Primary cilium transition zone (Supported); main locations Cytosol; Mid piece; Primary cilium transition zone.
- Module (primary_cilium_life_cycle, stage 4 axoneme_extension_ift): IFT-A subunit, process intraciliary retrograde transport, function "IFT cargo adaptor", location non-motile cilium.
- Assessment: consistent. Transition-zone/base staining fits IFT-A docking and train assembly at the ciliary base; the antibody does not resolve the axonemal pool. core_functions match the module (retrograde IFT, cargo import with TULP3) and add cilium assembly, because IFT122 KO abolishes ciliogenesis. One point to note: the module lists only retrograde transport for IFT-A, but IFT122/IFT-A also mediates membrane-protein entry ([PMID:27932497 "the IFT-A complex mediates not only retrograde trafficking but also entry into cilia of GPCRs"]). The role_description covers this.

## Deep research
See below.
Falcon deep research succeeded (IFT122-deep-research-falcon.md). It is consistent with the review:
- [file:human/IFT122/IFT122-deep-research-falcon.md "It joins IFT-A subassemblies, helps incorporate IFT-A into intraflagellar transport trains and provides part of the binding surface for the membrane-cargo adaptor TULP3."]
- It also reports IFT-A/IFT-B coupling via IFT122-IFT144 and IFT88-IFT52 (Kobayashi 2021, not cached), and that IFT122 CED mutants mislocalize ARL13B and INPP5E (not used for annotations).
