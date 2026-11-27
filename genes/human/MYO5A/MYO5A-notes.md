# MYO5A curation notes

## Deep research status
- `just deep-research-falcon human MYO5A` was run (first with the unavailable perplexity-lite fallback, then `--timeout 2400`). See the end of this file for the outcome. The review was written from cached primary literature.

## Key findings (with provenance)
- Processive actin-based motor [PMID:10448864 "Here we provide direct evidence that myosin-V is indeed a processive actin-based motor that can move in large steps approximating the 36-nm pseudo-repeat of the actin filament."]
- Melanosome transport via RAB27A-melanophilin [PMID:11980908 "melanophilin can associate simultaneously with activated Rab27a and myosin Va via distinct regions, and serve as a linker between these proteins"]
- Binds many Rabs directly; RAB10/RAB11 dominate membrane recruitment [PMID:24006491 "Although the total pool of myosin Va is shared by several Rabs, Rab10 and Rab11 appear to be the major determinants of its recruitment to intracellular membranes."]
- Depletion clusters recycling-pathway membranes perinuclearly; no effect on Golgi morphology (basis of the NOT annotation) [PMID:24006491 "RNAi-mediated knockdown of myosin Va resulted in the accumulation of TfR-positive membranes in the perinuclear region of the cell"]; [PMID:24006491 "Myosin Va knockdown had no obvious effect on Golgi distribution or morphology"]
- Ciliary role: preciliary vesicle transport to distal appendages [PMID:29335527 "Here, we demonstrate that myosin-Va mediates the transportation of preciliary vesicles to the mother centriole and reveal the underlying mechanism."]; [PMID:29335527 "Depletion of myosin-Va significantly inhibits the attachment of preciliary vesicles to the distal appendages of the mother centriole and decreases cilia assembly."]; [PMID:29335527 "Myosin-Va functions upstream of EHD1- and Rab11-mediated ciliary vesicle formation."]

## Pleiotropy: ciliary vs other roles
- Non-ciliary (major, well-established): melanosome capture/transport (Griscelli syndrome type 1), Rab-dependent recycling/secretory vesicle transport, neuronal vesicle/ER transport, insulin-stimulated GLUT4 delivery (ISS, kept non-core).
- Ciliary: one discrete step (preciliary vesicle delivery). GOA had no ciliary annotation; I proposed NEW cilium assembly (GO:0060271, IMP, PMID:29335527). Participation: MYO5A is the motor that performs the delivery step. Comparator: EHD1 and EHD3 (next step) carry cilium assembly.

## Curation decisions (summary)
- Motor activity, ATP hydrolysis, actin filament-based movement, vesicle transport along actin filament, melanosome transport/location, small GTPase binding (Rab binding): ACCEPT.
- Small GTPase binding IPI from the RAB27B paper: MARK_AS_OVER_ANNOTATED (indirect via melanophilin) - leaves one validator consistency warning, deliberately.
- Weak colocalizations (lysosome, late endosome, peroxisome; "limited overlap"), RNA binding HDA, exosome HDA: MARK_AS_OVER_ANNOTATED.
- Endocytosis and actin filament organization IBAs: KEEP_AS_NON_CORE (no MYO5A-specific evidence; not challenging PAINT node placement).

## HPA cilium atlas vs module role
- Module: stage 2_ciliary_vesicle, "preciliary vesicle transport to distal appendages"; process ciliary vesicle assembly (GO:1905556); module notes MF not asserted pending review.
- HPA v25: Primary cilium (A), Basal body (A), Centriolar satellite (A); main locations centriolar satellite and focal adhesion sites. No HPA-sourced GOA rows for MYO5A.
- Assessment: HPA basal-body/centriolar-satellite signal is consistent with a pericentrosomal pool that delivers vesicles to the mother centriole. I partially disagree with the module's process term: Wu et al. place myosin-Va upstream of ciliary vesicle formation (delivery, not fusion/tubulation), so core_functions use vesicle transport along actin filament + cilium assembly rather than ciliary vesicle assembly. The MF the module left open is microfilament motor activity (GO:0000146).

## Deep research outcome
- Falcon succeeded on retry (`--timeout 2400`): `MYO5A-deep-research-falcon.md`. It agrees on the core motor/cargo functions (RAB27A-MLPH-exon F melanosome transport, Rab10/Rab11/Rab14 endosome positioning, smooth-ER delivery into Purkinje spines, NMJ nAChR recycling) and the exon-F deletion causing pigmentation-only disease vs GS1 with neurological impairment. Notably it does not mention the ciliary role at all; the ciliary NEW annotation rests on PMID:29335527 (Wu et al. 2018), which is cached abstract-only.
