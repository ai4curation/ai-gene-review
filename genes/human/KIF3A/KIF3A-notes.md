# KIF3A notes

## Summary
- Kinesin-2 motor subunit; heterotrimer with KIF3B and KAP3: [PMID:16298999 "Kinesin-2 is composed of two microtubule-based motor subunits, KIF3A/3B, and a kinesin-associated protein known as KAP3, which links KIF3A/3B to cargo that is carried to cellular organelles along microtubules in interphase cells."]
- Motor activity: [PMID:7559760 "The recombinant KIF3A/B complex (approximately 50-nm rod with two globular heads and a single globular tail) demonstrated plus end-directed microtubule sliding activity in vitro."]
- Anterograde IFT motor / ciliogenesis: [PMID:23386061 "Formation of cilia, microtubule-based structures that function in propulsion and sensation, requires Kif3a, a subunit of Kinesin II essential for intraflagellar transport (IFT)."]; [PMID:32386558 "Kinesin-2 enables ciliary assembly and maintenance as an anterograde intraflagellar transport (IFT) motor."]
- Non-ciliary, IFT-independent centriole role: [PMID:23386061 "Comparison to cells lacking Ift88 reveals that the centriolar functions of Kif3a are independent of IFT."]; motor-independent [PMID:23386061 "The transport functions of Kif3a are dispensable for subdistal appendage organization as mutant forms of Kif3a lacking motor activity or the motor domain can restore p150(Glued) localization."]
- Non-ciliary cargo transport: [PMID:24338362 "the phosphatase POPX2 is a negative regulator of the trafficking of N-cadherin and other cargoes; consequently, it markedly influences cell-cell adhesion"]

## Ciliary vs other roles (classification used in the review)
- Ciliary (core): motor activity, kinesin II complex, anterograde IFT (NEW), cilium assembly, protein localization to non-motile cilium, cilium/tip locations.
- Non-ciliary transport (accepted as core motor use, or non-core when cargo/tissue-specific): plus-end vesicle transport (ACCEPT); anterograde axonal transport, N-cadherin/cell-junction protein transport (KEEP_AS_NON_CORE).
- Centriolar, IFT-independent (KEEP_AS_NON_CORE): centriole-centriole cohesion, microtubule anchoring at centrosome.
- Mitotic (KEEP_AS_NON_CORE): spindle microtubule colocalization.
- Removed: 15 generic protein binding rows (KAP3, DISC1, AP3B1, PIFO, CLN3, RAB11FIP5); organelle organization TAS changed (MODIFY) to plus-end-directed vesicle transport.
- NEW: intraciliary anterograde transport (GO:0035720). Participation: kinesin-2 itself performs the transport step. Comparator: C. elegans KLP-11 carries GO:0035720 (NAS); human/mouse KIF3B carry the parent intraciliary transport (IMP/ISS); QuickGO shows no GO:0035720 annotation for human or mouse KIF3A.

## HPA cilium atlas vs module role
- HPA v25: Primary cilium (Approved), Basal body (Approved); main locations Basal body; Cytosol; Nucleoplasm; Primary cilium.
- Module: kinesin-2 subunit; plus-end-directed microtubule motor activity; intraciliary anterograde transport; axoneme.
- Assessment: consistent. core_functions use the same MF (GO:0008574) and process (GO:0035720). They also list a separate non-ciliary transport core function, because the module covers only the ciliary context. HPA's Approved grade is low-confidence, but it fits. The nucleoplasm call is unexplained.

## Deep research
See below.
Falcon deep research succeeded (KIF3A-deep-research-falcon.md). Points used:
- [file:human/KIF3A/KIF3A-deep-research-falcon.md "it moves IFT assemblies along ciliary axonemal microtubules from the basal body/ciliary base toward the tip."]
- The deep research reports acute inhibition of engineered kinesin-II (Engelke 2019, not cached), which stops IFT and causes cilium loss. It also reports that KIF3A-KIF3B-KAP3 co-immunoprecipitates with the IFT-B connecting tetramer. Both support the core anterograde IFT role.
