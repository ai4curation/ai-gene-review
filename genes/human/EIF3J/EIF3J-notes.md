# EIF3J research notes

UniProt O75822 (EIF3J_HUMAN), eukaryotic translation initiation factor 3 subunit J. Cytoplasm.

## Core role
EIF3J is a subunit of the 13-subunit eukaryotic translation initiation factor 3 (eIF-3) complex.
- UniProt FUNCTION: "Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis [PMID:25849773, PMID:27462815]. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC)." 
- The eIF-3 complex "is also required for disassembly and recycling of post-termination ribosomal complexes and subsequently prevents premature joining of the 40S and 60S ribosomal subunits prior to initiation." (UniProt) — this is the ribosome-recycling / 40S-availability role.

## EIF3J is a labile / loosely-associated subunit
- UniProt SUBUNIT: "EIF3J is a labile subunit that binds to the eIF-3 complex via EIF3B." (sub-stoichiometric, loosely associated).
- In cryo-EM/structural and biochemical work eIF3j occupies the 40S mRNA entry channel and the decoding region, modulating mRNA loading and is implicated in 40S availability / recycling.
- IC annotations for "translation initiation factor activity" (GO:0003743) are inferred from being part of the eIF-3 complex (GO:0005852) [PMID:17322308, PMID:18599441]. EIF3J itself contributes_to this activity (contributes_to qualifier), consistent with it being a non-catalytic accessory subunit rather than the catalytic core.

## Annotations
- part_of GO:0005852 eukaryotic translation initiation factor 3 complex — CORE (IBA, IDA, IPI all agree). ACCEPT.
- GO:0003743 translation initiation factor activity (contributes_to, IC; also IEA) — ACCEPT as core MF (with contributes_to qualifier retained — it is an accessory subunit).
- BP translational initiation / cytoplasmic translational initiation / formation of cytoplasmic translation initiation complex — ACCEPT (core process).
- 43S/48S preinitiation complex (GO:0016282, GO:0033290) — ACCEPT as non-core CC (genuine but transient assembly intermediates; IEA UniRule).
- cytoplasm / cytosol — ACCEPT.
- protein binding IPI (many: EIF3B P55884, EIF4G1 Q04637, CSNK2A1 P68400, ABCE1 P61221, NFE2L2 Q16236) — uninformative term; KEEP_AS_NON_CORE. The biologically meaningful ones (EIF3B = how it joins eIF-3; ABCE1 = recycling factor) are captured by complex membership.
- identical protein binding GO:0042802 (self, O75822) — EIF3J self-interaction (IntAct), KEEP_AS_NON_CORE.

## Notable interactions
- EIF3B (P55884): the subunit through which EIF3J docks onto eIF-3 (PMID:14688252, 18628297, 35271311). Meaningful.
- ABCE1 (P61221): the ribosome-recycling ATPase; consistent with EIF3J/eIF-3 role in post-termination recycling and 40S availability (PMID:32296183, 35271311).
- CSNK2A1 (P68400): casein kinase 2 (phosphorylates EIF3J; phosphorylation enhanced on serum stimulation) — regulatory.

## Curation conclusions
- CORE MF: translation initiation factor activity (GO:0003743), as an accessory eIF-3 subunit (contributes_to).
- CORE CC: eukaryotic translation initiation factor 3 complex (GO:0005852).
- CORE BP: cytoplasmic translational initiation (GO:0002183) / translational initiation (GO:0006413).
- protein binding IPI = KEEP_AS_NON_CORE (uninformative).
