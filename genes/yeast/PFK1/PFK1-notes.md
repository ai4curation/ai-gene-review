# PFK1 notes (P16861, YGR240C) — PFK alpha subunit

- alpha4beta4 PFK, EC 2.7.1.11 [UniProt:P16861 "SUBUNIT: Heterooctamer of 4 alpha and 4 beta chains."]; activity needs both subunits [PMID:3007939 "Transformation with one of the plasmids did not lead to an increase in phosphofructokinase activity."].
- Double mutant glucose-negative [PMID:2965996 "A haploid yeast strain containing both disrupted copies of the PFK-genes is not capable of growing on rich medium containing 2% glucose."]; activators AMP/F2,6BP [PMID:6219673].
- V-ATPase link: co-IP and pH defects [PMID:24860096 "Both phosphofructokinase-1 subunits co-immunoprecipitated with V-ATPase in wild-type cells"]; proton transport normal in pfk1 [PMID:24860096 "they were normal in pfk1Δ"].
- RNA binding shared with Pfk2 [PMID:41816908 "Both Pfk1p and Pkf2p directly bind to short GA-, UC-, AU-, and U-rich motifs"], but NOT ribosome-bound [PMID:41816908 "Pfk1p is not directly associated with translating ribosomes in the absence of Pfk2p"].

Decisions: REMOVE ribosome binding IDA+IEA (contradicted in full text of the cited paper), protein binding x6, bifid n/a; contributes_to proton-transporting ATPase and proton transport MARK_AS_OVER_ANNOTATED; RNA-binding rows KEEP_AS_NON_CORE.
