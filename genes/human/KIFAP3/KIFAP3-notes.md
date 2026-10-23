# KIFAP3 (KAP3/SMAP) notes

## Summary
- Non-motor cargo-linking subunit: [PMID:24338362 "The kinesin-2 motor is a heterotrimeric complex composed of KIF3A, KIF3B motor subunits and KAP3, the non-motor subunit, which binds the cargo."]
- Tail binding (UniProt): "Binds to the tail domain of the KIF3A/KIF3B heterodimer to form a heterotrimeric KIF3 complex and may regulate the membrane binding of this complex"
- SMAP = human KAP3; ER-area localization and SmgGDS binding [PMID:8900189 "SMAP was ubiquitously expressed and highly concentrated at the endoplasmic reticulum area"]
- Chromosome link proposal [PMID:9506951 "The results suggest that SMAP/KAP3 serves as a linker between HCAP and KIF3A/B in the nucleus, and that SMAP/KAP3 plays a role in the interaction of chromosomes with an ATPase motor protein."]
- POPX2 phosphatase binds KAP3 [PMID:24338362 "we have identified POPX2, a serine-threonine phosphatase, as an interacting partner of the KAP3 subunit of the kinesin-2 motor"]

## Curation decisions
- 15 protein binding rows with KIF3A/KIF3B: MODIFY to kinesin binding (GO:0019894), which is KAP3's defining MF and is already supported by IPI from PMID:16298999.
- 17 other protein binding rows (HTP Y2H partners NCF2, NAA10, HOXB5, KANK2 etc.; SMC3): REMOVE.
- signal transduction and protein-containing complex assembly TAS (8900189): MARK_AS_OVER_ANNOTATED.
- Photoreceptor, ER/Golgi, dendritic/synaptic, chromosome and spindle terms: KEEP_AS_NON_CORE.

## HPA cilium atlas vs module role
- HPA v25: Basal body (Approved); main locations Basal body; Microtubules.
- Module: lists KIFAP3 as a kinesin-2 subunit of an annoton whose function is plus-end-directed microtubule motor activity.
- Assessment: partial disagreement. KIFAP3 has no motor domain and does not possess motor activity. At the gene level the correct MF is kinesin binding / cargo adaptor. In GO terms KAP3 could at most *contribute_to* the complex's motor activity. core_functions therefore use kinesin binding (GO:0019894) plus participation in cilium organization and vesicle transport within kinesin II, and do not use GO:0008574. The basal-body localization in HPA fits kinesin-2 loading at the ciliary base. No change to modules/ made (outside scope); raised as a suggested question in the review.

## Deep research
See below.
Falcon deep research succeeded (genes/human/KIFAP3/KIFAP3-deep-research-falcon.md). Key points (not independently re-verified against primary papers unless cached):
- [file:human/KIFAP3/KIFAP3-deep-research-falcon.md "KAP3 couples kinesin-2 to cargo-associated proteins and helps organize interactions between the motor’s C-terminal tails and transport machinery."]
- No catalytic activity: [file:human/KIFAP3/KIFAP3-deep-research-falcon.md "no catalytic reaction or small-molecule transport substrate should be assigned to KAP3 itself"] — this supports the decision not to give KIFAP3 motor activity.
- Chlamydomonas FLA3/KAP ortholog: [file:human/KIFAP3/KIFAP3-deep-research-falcon.md "its mutation dispersed KAP and the FLA10 motor from the basal-body/flagellar region"]; anterograde IFT frequency was reduced. This is ortholog evidence for a ciliary role.
- APC-mediated mRNA cargo and KAP3-dependent activation of KIF3A/B by APC (Webb et al. 2025, reported in the deep research; not cached) would be a candidate non-ciliary cargo-adaptor role. Not used for annotations.
