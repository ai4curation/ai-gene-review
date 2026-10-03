# KIF3B notes

## Summary
- Motor subunit with intrinsic motor activity: [PMID:7559760 "we showed that KIF3B itself has motor activity in vitro"]; heterodimer [PMID:7559760 "KIF3A and KIF3B directly bind with each other in the absence of KAP3."]
- Nodal cilia / L-R: [PMID:9865700 "the node lacked monocilia while the basal bodies were present"]; [PMID:9865700 "the left-right asymmetry was randomized in the heart loop and the direction of embryonic turning"]
- Human dominant ciliopathy: [PMID:32386558 "We observed a significant increase in primary cilia length in vitro in the context of either of the two mutations"]; [PMID:32386558 "rhodopsin was sequestered to the photoreceptor rod inner segment layer with a concomitant increase in photoreceptor cilia length"]
- Mitosis: [PMID:16298999 "expression of a mutant KIF3B, which is able to associate with KIF3A but not KAP3 in NIH3T3 cells, caused chromosomal aneuploidy and abnormal spindle formation"]
- Neuronal: GRIN2A vesicle transport into dendrites (UniProt, by similarity to mouse).

## Ciliary vs other roles
- Ciliary (core): motor activity, kinesin II, intraciliary transport (IMP), cilium assembly, IFT-B binding (IFT20), cilium/tip locations; NEW intraciliary anterograde transport (refines the existing intraciliary transport IMP).
- Ciliary but cell-type specific (non-core): opsin transport, left/right determination.
- Non-ciliary transport: plus-end vesicle transport, cytoskeleton-dependent transport (ACCEPT); axonal, dendritic and synaptic terms (KEEP_AS_NON_CORE).
- Mitotic: spindle organization/assembly KEEP_AS_NON_CORE; mitotic centrosome separation UNDECIDED (not in the cached abstract).
- small GTPase binding (IPI, 19635168): REMOVE — the partner recorded in GOA is ARHGEF10, a RhoA GEF and not a small GTPase [PMID:19635168 "Here we show that RhoA is a substrate for ARHGEF10."]
- 10 generic protein binding rows REMOVE; urinary exosome HDA MARK_AS_OVER_ANNOTATED.

## HPA cilium atlas vs module role
- HPA v25: Primary cilium tip (Approved); main locations Flagellar centriole; Nucleoplasm; Primary cilium tip.
- Module: kinesin-2 subunit; plus-end-directed microtubule motor activity; anterograde IFT; axoneme.
- Assessment: consistent. Tip enrichment fits an anterograde motor that delivers trains to the tip, where kinesin-2 is released or diffuses back. The core-function location is ciliary tip rather than the module's axoneme; both are correct, and the tip is what HPA observes.

## Deep research
See below.
