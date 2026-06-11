# EMC8 (O43402) review notes

## Identity / overview
- EMC8 = ER membrane protein complex subunit 8 (human, 210 aa). Synonyms: C16orf2/C16orf4, COX4AL, COX4NB, FAM158B, NOC4, "Neighbor of COX4". HGNC:7864, GeneID 10328 [file:human/EMC8/EMC8-uniprot.txt "RecName: Full=ER membrane protein complex subunit 8"], [file:human/EMC8/EMC8-uniprot.txt "AltName: Full=Neighbor of COX4"].
- It is a **cytosolic, peripheral** subunit of the nine-subunit EMC, an ER membrane insertase/chaperone. EMC8 sits on the cytoplasmic side of the membrane and is non-catalytic [file:human/EMC8/EMC8-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"], [file:human/EMC8/EMC8-uniprot.txt "Peripheral membrane protein"], [file:human/EMC8/EMC8-uniprot.txt "Cytoplasmic side"].
- Belongs to the EMC8/EMC9 family; **EMC8 and EMC9 are mutually exclusive subunits** of EMC [file:human/EMC8/EMC8-uniprot.txt "Belongs to the EMC8/EMC9 family."], [file:human/EMC8/EMC8-uniprot.txt "EMC8 and EMC9 are mutually exclusive subunits of the EMC complex"].
- Contains a single MPN domain (residues 4-150), a (pseudo-?)JAMM/MPN fold; EMC8/9 are MPN-domain proteins related to the proteasome lid/COP9 deneddylase subunits but lack the catalytic metalloprotease residues (annotated CDD MPN_UPF0172, Pfam UPF0172) [file:human/EMC8/EMC8-uniprot.txt "DOMAIN          4..150"], [file:human/EMC8/EMC8-uniprot.txt "CDD; cd08060; MPN_UPF0172"].
- Note: the context-provided "PDE6D-like phosphodiesterase fold" framing is NOT what the UniProt record states; the record annotates an **MPN domain**. No catalytic activity is assigned in UniProt. No moonlighting NMNAT/neuromuscular-junction role is substantiated in any of the EMC8 input files, so none is asserted.

## Complex / structure
- Identified as a component of the mammalian EMC ("mEMC") in the foundational ERAD-network MS study; EMC8 appears there under the alias COX4NB [PMID:22119785 "we identified 5 additional HCIPs (TTC35, TMEM32/MMGT1, TMEM85, C15orf24 and COX4NB)"]. This is the IDA source for EMC-complex membership and cytoplasm localization.
- Cryo-EM structures of human EMC place EMC8 (chain H) in the cytosolic-facing region of the complex [file:human/EMC8/EMC8-uniprot.txt "STRUCTURE BY ELECTRON MICROSCOPY (3.40 ANGSTROMS) OF THE EMC COMPLEX"]; the catalytic insertase machinery is the EMC3/EMC6 transmembrane vestibule, not EMC8 [PMID:32439656 "substrate insertion requires a methionine-rich cytosolic loop and occurs via an enclosed hydrophilic vestibule within the membrane formed by the subunits EMC3 and EMC6"].

## Function (complex-level, not EMC8-intrinsic)
- The EMC is a co- and post-translational transmembrane-domain insertase/chaperone that inserts newly synthesized membrane proteins into the ER membrane, with preference for weakly hydrophobic / destabilizing TMDs; handles multipass (stop-transfer) and tail-anchored substrates and sets N-exo topology of multipass proteins [file:human/EMC8/EMC8-uniprot.txt "enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins"], [file:human/EMC8/EMC8-uniprot.txt "required for the post-translational insertion of tail-anchored/TA proteins in"].
- These functional studies (PMID:29242231 insertase; PMID:29809151 cotranslational multipass; PMID:30415835 topogenesis; PMID:32439656/32459176 structure) concern the **whole EMC**. EMC8-specific IMP "membrane insertase activity" (GO:0032977, contributes_to) is appropriate because the GO `contributes_to` qualifier is exactly for a subunit contributing to a complex MF; full text of the IMP papers (knockdown of EMC subunits) was read by curators.

## Interaction (IPI) annotations
- All nine `GO:0005515 protein binding` IPI annotations have WITH/FROM = UniProtKB:Q15006 (**EMC2**) and come from high-throughput interactome / structural mapping papers (PMID:16189514 Rual Y2H map; 22119785 ERAD network; 26496610 BioPlex stoichiometry; 28514442 interactome communities; 30021884 histone XL-MS; 32296183 HuRI binary; 32439656 EMC structure; 33961781 BioPlex 3; 35271311 OpenCell). EMC2 is the EMC scaffold that EMC8 docks onto, so the interaction is real and biologically meaningful (it is how EMC8 joins the complex), but bare "protein binding" is uninformative -> KEEP_AS_NON_CORE per guidelines. The UniProt INTERACTION block confirms the EMC2 partner [file:human/EMC8/EMC8-uniprot.txt "O43402; Q15006: EMC2; NbExp=17"].
- PMID:30021884 (histone crosslinking MS in nuclei) is an odd citation for an ER complex subunit, but it is a curator-entered IntAct EMC8-EMC2 evidence; cannot verify the specific datapoint from the abstract -> keep as non-core, do not REMOVE an experimental IPI.

## Localization
- ER membrane (peripheral, cytoplasmic side); also annotated cytoplasm (IDA, PMID:22119785) and ER (IDA/HPA). `GO:0016020 membrane` (HDA, PMID:19946888 NK-cell membrane proteome) is a generic parent, correct but low-information [file:human/EMC8/EMC8-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"].

## Core function determination
- For a non-catalytic cytosolic subunit, CORE = **EMC complex membership (GO:0072546)** + **ER membrane (GO:0005789)**, with `contributes_to membrane insertase activity (GO:0032977)` capturing its participation in the complex MF.
- The BP terms (GO:0045050 stop-transfer insertion; GO:0071816 TA insertion) are complex-level functions EMC8 contributes to; keep but they are complex-level, not EMC8-intrinsic.

## Action summary
- ACCEPT: EMC complex (all evidence forms), ER membrane, membrane insertase activity (contributes_to IMP/IBA), insertion BP terms (IDA/IMP/IBA), cytoplasm IDA, ER IDA.
- KEEP_AS_NON_CORE: all 9 `protein binding` GO:0005515 IPI (bare term, but real EMC2 interaction); `membrane` HDA (generic parent).
- No REMOVE/MODIFY/UNDECIDED warranted — annotations are consistent and well-supported.
