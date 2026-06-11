# EMC2 (TTC35, KIAA0103) — gene review notes

UniProt: Q15006 (EMC2_HUMAN), 297 aa, ~34.8 kDa. HGNC:28963. Chromosome 8.

## Identity / domain architecture
- ER membrane protein complex subunit 2; AltName Tetratricopeptide repeat protein 35 (TTC35) [file:human/EMC2/EMC2-uniprot.txt "AltName: Full=Tetratricopeptide repeat protein 35"].
- TPR-repeat protein: three annotated TPR repeats (87-120, 155-188, 192-225) forming an all-alpha-helical solenoid; PDB structures (6Y4L X-ray, 6WW7 cryo-EM, etc.) show a near-continuous array of helices [file:human/EMC2/EMC2-uniprot.txt "REPEAT          87..120 ... TPR 1"].
- Belongs to the EMC2 family [file:human/EMC2/EMC2-uniprot.txt "Belongs to the EMC2 family"].

## Core biology: cytosolic scaffold of the EMC insertase
- EMC2 is one of two soluble cytosolic subunits of the EMC (the other being the mutually-exclusive paralogues EMC8/EMC9); the EMC has seven membrane-spanning subunits (EMC1, 3-7, 10) and two soluble cytosolic subunits [PMID:33964204 "the EMC is composed of seven integral membrane subunits (EMC1, 3-7, and 10) and two soluble cytosolic subunits (EMC2 and the closely related paralogues EMC8/9)"].
- EMC2 is the architectural scaffold of the EMC cytosolic domain — it anchors and stabilizes the entire complex: [PMID:33964204 "EMC2 is a superhelical architectural scaffold, responsible for anchoring both the cytosolic and membrane spanning subunits of the complex"].
- The cytosolic domain is organized around the soluble EMC2-8/9 heterodimer [PMID:33964204 "The cytosolic domain is organized around the soluble EMC2-8/9 heterodimer"].
- EMC2 makes an extensive hydrophobic interface with EMC8 and contacts cytosolic extensions of membrane subunits EMC3 and EMC5 [PMID:33964204 "EMC2 forms an extensive, predominantly hydrophobic interface with EMC8 and makes interactions with the cytosolic extensions of the membrane-spanning subunits EMC3 and 5"].
- Structure-guided mutagenesis of EMC2 surface residues (R28, E156, E160, Y171, E180, Y200, R227, W259) disrupts interactions with EMC5/EMC3/EMC8 — confirming the scaffold/interface role [file:human/EMC2/EMC2-uniprot.txt "R->A: Loss of interaction with EMC5"].

## The complex (not EMC2 alone) is the insertase
- EMC is a transmembrane-domain insertase: purified EMC in liposomes catalyzes insertion of TA substrates [PMID:29242231 "Purified EMC in synthetic liposomes catalyzed the insertion of its substrates in a reconstituted system. Thus, EMC is a transmembrane domain insertase"].
- The catalytic membrane vestibule is formed by EMC3 and EMC6 (NOT EMC2): [PMID:32439656 "substrate insertion requires a methionine-rich cytosolic loop and occurs via an enclosed hydrophilic vestibule within the membrane formed by the subunits EMC3 and EMC6"]. => EMC2 contributes as scaffold but is not the catalytic core. GO:0032977 (membrane insertase activity) on EMC2 is correctly qualified `contributes_to`.
- EMC inserts the first TMD of GPCRs co-translationally, in N-exo topology, cooperating with Sec61 (topogenesis) [PMID:30415835 "EMC inserts TMDs co-translationally and cooperates with the Sec61 translocon to ensure accurate topogenesis of many membrane proteins"].
- EMC also enables biogenesis of multipass transmembrane proteins, engaging clients cotranslationally [PMID:29809151 "the EMC broadly enables the biogenesis of multipass transmembrane proteins containing destabilizing features"].
- EMC is necessary AND sufficient for post-translational insertion of moderately-hydrophobic tail-anchored (TA) proteins such as squalene synthase (SQS) [PMID:29242231 "the EMC was shown to be essential for efficient insertion in vitro and in cells"].

## Localization
- UniProt SUBCELLULAR LOCATION: ER membrane, peripheral membrane protein, cytoplasmic side [file:human/EMC2/EMC2-uniprot.txt "Endoplasmic reticulum membrane ... Peripheral membrane protein ... Cytoplasmic side"]. EMC2 itself has no TMD — it associates with the ER membrane peripherally via the membrane subunits, on the cytosolic face. Also detectable as free cytosolic protein (orphan, rapidly degraded).
- Christianson et al. 2012 (ERAD mapping) identified EMC2 in the EMC and localized it to ER membrane / cytoplasm [PMID:22119785]. Original EMC-complex identification + subcellular location.
- Hoja et al. 2000 (PROLOC GFP screen): EMC2/TTC35 (KIAA0103) localized to the ER [PMID:10942595 "novel proteins associated with the nucleolus, mitochondria, the ER"]. Abstract-only; an early GFP-fusion localization screen.
- GO:0042406 extrinsic component of ER membrane (IDA, PMID:32439656) — accurate: EMC2 is a peripheral membrane protein on the cytosolic side, consistent with the structural data.

## Assembly / regulation (WNK1)
- WNK1 is an EMC assembly factor: a conserved amphipathic helix of WNK1 binds the EMC2-8 interface, stabilizing orphan EMC2 and preventing its ubiquitination/degradation, thereby permitting assembly [PMID:33964204 "WNK1 uses a conserved amphipathic helix to stabilize the soluble subunit, EMC2, by binding to the EMC2-8 interface. Shielding this hydrophobic surface prevents promiscuous interactions of unassembled EMC2 and directly competes for binding of E3 ubiquitin ligases, permitting assembly"].
- Orphan/unassembled cytosolic EMC2 is ubiquitinated and proteasomally degraded [file:human/EMC2/EMC2-uniprot.txt "Ubiquitinated when soluble in the cytoplasm, leading to its degradation by the proteasome"]. WNK1 binding (Q9H4A3) protects it.
- The GO:0005515 protein-binding IPI annotation original_reference_id PMID:33964204 with WITH/FROM UniProtKB:Q9H4A3 = WNK1 — this is the biologically meaningful WNK1 interaction.

## Interactome / protein-binding IPI annotations (mostly non-core)
GOA has many GO:0005515 (protein binding) IPI annotations from large-scale interactome / IntAct studies. WITH/FROM partners are predominantly genuine EMC subunits and assembly machinery:
- O43402 = EMC8; Q9Y3B6 = EMC9; Q9P0I2 = EMC3; Q8N4V1 = MMGT1/EMC5 — bona fide EMC subunits, recovered by AP-MS in ERAD/interactome maps.
- Q9H4A3 = WNK1 (assembly factor, PMID:33964204).
- Other partners (Q53Y03 COX4NB/EMC7-region, Q9UKT9 IKZF3, Q7L8J4 SH3BP5L, Q96GW1 HSP90B1, Q9UHA2 SS18L2, Q9Y5F1 PCDHB12) are from binary/HT interactome screens — some are clients/incidental.
- Interactome sources: PMID:16189514 (HT-Y2H proteome map), PMID:25416956 (HuRI/interactome), PMID:26496610 (3D interactome by stoichiometry), PMID:28514442 (interactome communities), PMID:30021884 (histone crosslinking-MS — likely incidental), PMID:32296183 (HuRI binary interactome), PMID:33961781 (BioPlex dual proteome), PMID:35271311 (OpenCell), PMID:40205054 (multimodal cell maps).
- These all map to bare `protein binding` (GO:0005515) — uninformative term; per curation guidelines, KEEP_AS_NON_CORE (real interactions but uninformative MF). The WNK1 one is biologically the most meaningful but still bare protein binding -> KEEP_AS_NON_CORE.
- PMID:30021884 (histone interaction landscapes by crosslinking-MS in nuclei): EMC2 capture here is likely incidental/nuclear-envelope contamination; relevance LOW.

## Curation summary
- CORE: EMC complex membership (GO:0072546, part_of); ER membrane localization (GO:0005789, located_in, via peripheral association on cytosolic side); scaffold role in TA / multipass / stop-transfer membrane protein insertion (GO:0071816, GO:0045050 involved_in); contributes_to membrane insertase activity (GO:0032977, contributes_to) — complex has the activity, EMC2 contributes as scaffold (NOT catalytic; vestibule is EMC3/EMC6).
- NON-CORE: all bare protein-binding IPI; cytoplasm/ER (broad) localizations.

## Verification pass (2026-06-11)
- Verbatim substrings confirmed present in cached sources: PMID:33964204 "superhelical architectural scaffold", "amphipathic helix to stabilize the soluble", "organized around the soluble EMC2"; PMID:29242231 "transmembrane domain insertase", "tail-anchored membrane proteins with moderately hydrophobic transmembrane"; PMID:30415835 "G protein-coupled receptors"; uniprot "Component of the ER membrane protein complex (EMC)", "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane", "Peripheral membrane protein", "Cytoplasmic side", "stop-transfer membrane-anchor sequences become ER membrane spanning", "enables the energy-independent insertion into endoplasmic", "post-translational insertion of tail-anchored/TA proteins in", interaction lines "Q15006; O43402: EMC8" / "Q15006; Q9P0I2: EMC3" / "Q15006; Q9Y3B6: EMC9".
- All 31 PENDING annotations reviewed; no REMOVE/MODIFY/UNDECIDED needed (all experimental/electronic annotations verifiable and consistent with EMC2 as the cytosolic TPR scaffold). GO:0042406 (extrinsic component of ER membrane) is an informative, accurate localization for the non-TM peripheral subunit and was ACCEPTed.
