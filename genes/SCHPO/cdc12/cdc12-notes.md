# cdc12 (S. pombe) review notes

UniProt: Q10059 (CDC12_SCHPO). ORF SPAC1F5.04c. 1841 aa. Formin homology family, BNI1 subfamily.
Domains: GBD/FH3 (232-620), FH1 (740-972, proline-rich, profilin-binding), FH2 (980-1391, actin nucleation/capping). PDB 8RTT/8RTY cover FH2 region (~972-1390).

## Core function
Cdc12 is the single essential cytokinetic formin of fission yeast. It nucleates and processively elongates unbranched actin filaments for the cytokinetic actomyosin contractile ring (CR/CAR).

- Required for actin ring assembly and septum formation; essential gene. cdc12-112 ts mutant has specific defect in actin ring formation and cell division [PMID:9105045 "Schizosaccharomyces pombe cdc12 is an essential gene necessary for actin ring assembly and septum formation"].
- Member of formin family (diaphanous, BNI1, fus1) [PMID:9105045 "cdc12p is a member of a family of proteins including Drosophila diaphanous, Saccharomyces cerevisiae BNI1, and S. pombe fus1"].
- Localizes to the cell division ring, not other actin structures; medial spot in interphase when overexpressed [PMID:9105045 "cdc12p is located in the cell division ring and not in other actin structures. When overexpressed, cdc12p is located at a medial spot in interphase that anticipates the future ring site."].
- FH1 binds profilin (Cdc3); proline-rich domain binds directly to profilin cdc3p in vitro [PMID:9105045 "a proline-rich domain of cdc12p binds directly to profilin cdc3p in vitro, suggesting that one function of cdc12p in ring assembly is to bind profilin"].

## Biochemistry (Kovar/Pollard)
- FH1 binds profilin, FH2 binds actin [PMID:12796476 "The proline-rich formin homology (FH) 1 domain binds profilin, and the FH2 domain binds actin."].
- Caps barbed ends; profilin-gated barbed-end capping protein [PMID:12796476 "Like capping protein, purified Cdc12(FH1FH2)p caps the barbed end of actin filaments, preventing subunit addition and dissociation, inhibits end to end annealing of filaments, and nucleates filaments that grow exclusively from their pointed ends."].
- With profilin: nucleates filaments that grow rapidly from barbed ends [PMID:12796476 "profilin changes the mechanism so that Cdc12(FH1FH2)p nucleates filaments that grow rapidly from their barbed ends"].
- Conclusion: "formins are profilin-gated barbed end capping proteins with the ability to initiate actin filaments from actin monomers bound to profilin" [PMID:12796476].

## Mechanism of elongation (cryo-EM)
- Formins processively elongate F-actin at barbed ends; common asymmetric formin conformation imposed by the filament [PMID:38603491 "we present high-resolution cryo-electron microscopy structures of F-actin barbed ends bound by three distinct formins, revealing a common asymmetric formin conformation imposed by the filament"]. (PDB 8RTT/8RTY are Cdc12 FH2 on F-actin barbed end.)

## Localization / CC
- Localized to cell division site; cdc12p spot moves to future division site at mitotic onset [PMID:10469572 "cdc12p was found, during interphase, in a discrete, motile cytoplasmic spot that moved to the future site of cell division at the onset of mitosis"].
- Joins cytokinetic nodes (Mid1 band) with myosin-II, Rng2, Cdc15 [PMID:16864655 "These nodes mature by the addition of conventional myosin II (Myo2p, Cdc4p, and Rlc1p), IQGAP (Rng2p), pombe Cdc15 homology protein (Cdc15p), and formin (Cdc12p). The nodes coalesce laterally into a compact ring when Cdc12p and profilin Cdc3p stimulate actin polymerization."].
- Recruited to cytokinetic precursor nodes by both modules [PMID:21422229 "Both modules recruit the formin Cdc12 to nucleate actin filaments."].
- In Δmid1, Cdc12 in scattered cytokinetic nodes producing actin filaments [PMID:22918943 "Cdc12p accumulates in cytokinetic nodes scattered in the cortex and produces actin filaments that associate with myosin-II, Rng2p, and Cdc15p to form strands"].
- Spatiotemporal ring assembly: formin Cdc12p joins broad band independent of actin filaments [PMID:14602073 "conventional myosin-II (Myo2p), IQGAP (Rng2p), PCH protein (Cdc15p), and formin (Cdc12p) join the broad band independent of actin filaments"].
- Nanoscale architecture: formin in membrane-proximal layer (0-80 nm) of the CR [PMID:28914606 "The most membrane-proximal layer (0-80 nm) is composed of membrane-binding scaffolds, formin, and the tail of the essential myosin-II."].
- Global localization screen (HDA), division site / cytoplasm [PMID:16823372 ORFeome localization study].
- Blt1p roles in cytokinesis — Cdc12 in ring [PMID:24790095].

## Interactions / recruitment / regulation
- Cdc15 (F-BAR) binds directly to Cdc12; mutual dependence for CR localization [PMID:12939254 "Cdc15p also binds directly to Cdc12p. Cdc15p and Cdc12p not only display mutual dependence for CAR localization, but also exist together in a ring-nucleating structure before CAR formation."].
- Cdc12 N-terminal motif binds directly to F-BAR domain of Cdc15 [PMID:25688133 "we define a short motif within the N terminus of Cdc12 that binds directly to the F-BAR domain of the scaffolding protein Cdc15"]. -> F-bar domain binding (GO:1990808).
- Cdk1 phosphorylates Cdc12 to inhibit the Cdc12-Cdc15 (formin-F-BAR) interaction; opposes CR formation [PMID:29343550 "A single essential formin, Cdc12, localizes to the cell middle upon mitotic onset and nucleates the F-actin of the CR. Cdc12 medial recruitment is mediated in part by its direct binding to the F-BAR scaffold Cdc15."]. -> F-bar domain binding (GO:1990808).
- SIN kinase Sid2 phosphorylates Cdc12; phosphoregulation of formin multimerization / F-actin bundling activity [PMID:24115772 "we identify the essential cytokinetic formin Cdc12 as a key CR substrate of SIN kinase Sid2 ... Sid2 phosphorylation of Cdc12 abrogates multimerization of a previously unrecognized Cdc12 domain that confers F-actin bundling activity."]. -> supports actin filament bundle assembly (GO:0051017) and CR localization.
- Cdc12 and For3 cooperate during CR assembly; For3 essential when Cdc12 N-truncated [PMID:24127216 "the formins Cdc12 and For3 cooperate during contractile ring assembly in cytokinesis ... For3 became essential in cells expressing N-terminal truncations of Cdc12"].
- Formins dictate which tropomyosin associates with filament; Cdc12 vs For3 [PMID:24954052 "Exchanging the localization of the fission yeast formins For3 and Cdc12 results in an exchange in localizations of Tm forms on actin polymers."].
- Sop2p modulates profilin function; interacts with Arp3 — IPI link to Cdc12 via shared assay (cdc12 binds sop2/Arp-complex pathway) [PMID:8978670 abstract only; full text assays not in cache]. Defer (PomBase curated IPI).
- Oligomerization of Cdc15 F-BAR underlies cytokinesis function [PMID:26702831 abstract only].
- cdc12-112 genetic screen for ring assembly mutants [PMID:8834798 "cdc12 and cdc15 mutants display disorganized actin patches during mitosis, but normal interphase actin patterns"].

## Annotation assessment summary
CORE MF: actin filament binding (GO:0051015), actin filament polymerization (GO:0030041), barbed-end actin filament capping (GO:0051016), profilin/F-BAR binding (GO:1990808).
CORE BP: mitotic actomyosin contractile ring assembly (GO:1903475).
CORE CC: mitotic actomyosin contractile ring (GO:0110085), cell division site (GO:0032153).

Concerns:
- nucleus (GO:0005634, IEA from UniProt SubCell): the SubCell note (PubMed:10759889) is a large-scale GFP-fusion-fragment localization screen of fragment 517-689 only, not full-length. Cdc12 is a cytoplasmic/ring/division-site protein; "nucleus" is not supported by the functional literature. The deep-research full text PMID:10759889 was a screen using genomic fragments and may not reflect true full-length localization. Mark as over-annotated / non-core (do not assert it's wrong gene). Use KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED with caution -> choose UNDECIDED is too weak; this is an IEA SubCell mapping that conflicts with strong experimental CC. Use MARK_AS_OVER_ANNOTATED.
- small GTPase binding (GO:0031267, IEA InterPro from GBD domain IPR010473): Cdc12 GBD/FH3 present, but no experimental evidence Cdc12 binds a Rho GTPase in S. pombe (For3 is Rho-regulated; Cdc12 regulation is via Cdc15/Mid1/SIN/Cdk1, not a Rho GTPase). InterPro domain-based prediction; weak. MARK_AS_OVER_ANNOTATED.
- protein binding (GO:0005515, bare): uninformative; for Cdc15 IPIs propose F-bar domain binding / leave as KEEP_AS_NON_CORE per guidance avoid bare protein binding. MODIFY where specific partner known.
- actin filament bundle assembly (GO:0051017, IBA + ... ): supported by Sid2/Cdc12 F-actin bundling domain [PMID:24115772]. Keep as non-core (bundling is a regulated secondary activity).
- mating projection tip (GO:0043332, IBA): based on phylogeny (fus1 paralog is the mating formin). Cdc12 itself is the cytokinesis formin; mating projection localization is for fus1. Likely IBA over-propagation. MARK_AS_OVER_ANNOTATED.
- actin cytoskeleton organization (GO:0030036, IEA ARBA/InterPro): correct but general; keep non-core.
- protein localization to mitotic actomyosin contractile ring (GO:1904498, IEA ARBA): Cdc15 recruits Cdc12, and Cdc12 generates actin that captures other components into ring; plausible but IEA. Keep non-core.
