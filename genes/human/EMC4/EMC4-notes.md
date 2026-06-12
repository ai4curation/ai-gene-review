# EMC4 (TMEM85) review notes

UniProt: Q5J8M3 (EMC4_HUMAN). 183 aa. Synonyms TMEM85, PIG17, HSPC184. Gene on chr15.

## Identity / overview
- EMC4 is a small (~20 kDa) accessory transmembrane subunit of the ER membrane protein complex (EMC), the conserved 9-10 subunit ER insertase. It is NOT the catalytic insertase core (that is EMC3 + EMC6).
- Topology (from structures): cytoplasmic N-terminus (2-66), three TMs (67-87, 99-120, 128-148) and a lumenal C-terminus, or possibly single-pass. [file:human/EMC4/EMC4-uniprot.txt "TRANSMEM        67..87"]
- 8 cryo-EM structures (PDB 6Z3W, 7ADO, 7ADP, 8EOI, 8J0N, 8J0O, 8S9S, 9C7V) all resolve EMC4 (chain D) as part of the EMC. Membership is structurally unambiguous.

## Function (EMC complex membership)
- EMC mediates energy-independent insertion of newly synthesized membrane proteins into the ER membrane. [file:human/EMC4/EMC4-uniprot.txt "Part of the endoplasmic reticulum membrane protein complex"]
- EMC = TA (tail-anchored) protein post-translational insertase. [PMID:29242231 "Thus, EMC is a transmembrane domain insertase"]; preferentially accommodates weakly hydrophobic TMDs.
- EMC engages multipass membrane proteins co-translationally, enriched for transporters. [PMID:29809151 "the ER membrane protein complex (EMC) binds to and promotes the biogenesis of a range of multipass transmembrane proteins, with a particular enrichment for transporters"]
- EMC sets topology of multipass proteins (e.g. GPCRs) via co-translational N-exo insertion of the first TMD. [PMID:30415835 "efficient biogenesis of ... G protein-coupled receptors (GPCRs) requires the conserved ER membrane protein complex (EMC)"]
- The catalytic vestibule is formed by EMC3 and EMC6 — NOT EMC4. [PMID:32439656 "substrate insertion ... occurs via an enclosed hydrophilic vestibule within the membrane formed by the subunits EMC3 and EMC6"]
- EMC4 is therefore a structural/scaffold subunit; its catalytic-activity annotations are correctly given with the `contributes_to` qualifier (it contributes to complex insertase activity, not standalone).

## Complex membership / localization
- Identified in mEMC (mammalian EMC) as TMEM85 by Christianson 2011. [PMID:22119785 "we identified 5 additional HCIPs (TTC35, TMEM32/MMGT1, TMEM85, C15orf24 and COX4NB)"]
- SUBCELLULAR LOCATION: ER membrane, multi-pass membrane protein. [file:human/EMC4/EMC4-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"]

## Protein interactions (IPI / bare protein binding)
- SLC2A9 / GLUT9 (Q9NRM0-1, Q9NRM0-2): TMEM85 was tested as a GLUT9 interactor; in the functional assay TMEM85 did NOT affect urate transport (ITM2B did). [PMID:31695625 "wherein ITM2B but not TMEM85 inhibited GLUT9-mediated urate uptake"]. This is likely EMC4 acting as the EMC subunit engaging the multipass transporter client GLUT9 (consistent with EMC's transporter-client preference), but recorded only as bare protein binding.
- SARS-CoV-2 rep/nsp interactions (P0DTD1 PRO_0000449624): from three large viral-host interactome screens (PMID:33845483, PMID:34232536, PMID:36217030), all abstract-only in cache. IntAct INTERACTION block of UniProt lists "Q5J8M3; PRO_0000449624 [P0DTD1]: rep". These are high-throughput viral-host PPIs; bare protein binding, non-core.

## Curation decisions summary
- CORE: EMC complex membership (GO:0072546 part_of), ER membrane (GO:0005789), TA insertion (GO:0071816 involved_in), stop-transfer multipass insertion (GO:0045050 involved_in).
- membrane insertase activity (GO:0032977) with `contributes_to`: ACCEPT (complex-level catalytic contribution, scaffold framing), not standalone core MF for EMC4.
- All bare protein binding (GO:0005515 IPI): KEEP_AS_NON_CORE.
- GO:0016020 membrane: redundant/generic vs ER membrane -> KEEP_AS_NON_CORE.
- apoptotic process (GO:0006915, IEA KW): from old yeast/human TMEM85 H2O2-cell-death observation [PMID:18586032]; this is an indirect/pleiotropic downstream effect, MARK_AS_OVER_ANNOTATED (note: this term is a UniProtKB-KW IEA and appears in the DR GO block but is not in goa.tsv, so not in existing_annotations list).
</content>

## Verification pass (2026-06-11)
- All 18 PENDING annotations reviewed and filled; status COMPLETE.
- Verbatim substrings confirmed in cache/uniprot: uniprot "Component of the ER membrane protein complex (EMC).", "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane", "Q5J8M3; Q9NRM0-1: SLC2A9", "Q5J8M3; PRO_0000449624 [P0DTD1]: rep", "enables the energy-independent insertion into endoplasmic", "post-translational insertion of tail-anchored/TA proteins in", "stop-transfer membrane-anchor sequences become ER membrane spanning"; PMID:29242231 "transmembrane domain insertase" / "tail-anchored membrane proteins with moderately hydrophobic transmembrane"; PMID:30415835 "G protein-coupled receptors".
- IPI partners: PMID:31695625 -> GLUT9/SLC2A9 (multipass transporter client; KEEP_AS_NON_CORE); PMID:33845483/34232536/36217030 -> SARS-CoV-2 replicase rep (P0DTD1, viral; KEEP_AS_NON_CORE).
- EMC4 is a non-catalytic accessory membrane subunit; GO:0032977 insertase activity carries contributes_to and is ACCEPTed at complex level. CORE = EMC complex membership + ER membrane + TA/stop-transfer insertion processes. No REMOVE/MODIFY/UNDECIDED.

## Falcon deep-research findings (incorporated 2026-06)

New EMC4-relevant references verified against PubMed and added to the review (all additive; no action changes):

- Improved 2023 human EMC cryo-EM resolves **three TMDs in EMC4**; EMC4/EMC7/EMC10 TMDs partially enclose the EMC3/EMC6 hydrophilic insertase vestibule, and substrate photocrosslinking/disulfide crosslinking detects contacts with EMC4 (not only EMC3). EMC4 loss also impairs EMC7/EMC10 incorporation. [PMID:37199759 "the hydrophilic vestibule ... partially enclosed by dynamic TMDs from EMC4/7/10"]
- The EMC acts as a **holdase/chaperone** during assembly of the multipass voltage-gated Ca channel CaV1.2; EMC4 is part of the client-engaging cytoplasmic chaperone module and of a lumenal EMC1/EMC4/EMC7/EMC10 subassembly. [PMID:37196677 "the EMC functions as a channel holdase that facilitates channel assembly"]
- Independent 2024 human EMC cryo-EM (apo + VDAC-bound) describes EMC4 as an **ordered three-TMH bundle adjacent to EMC3/EMC6** forming a sidewall of the vestibule; EMC engages VDAC at mitochondria-ER contact sites. [PMID:38517390 "identified a gating plug located inside the EMC hydrophilic vestibule"]
- Reconstitution + MD propose **lipid scrambling as a general insertase feature, localized to EMC3 and EMC4**, in the same hydrophilic channel used for protein insertion (hypothesis-generating; not yet shown for human EMC4 in cells). [PMID:38621120 "lipid scrambling is a general feature of protein insertases"]
- EMC4 is a **proviral host factor for flaviviruses** (dengue, yellow fever, Zika), acting at an early entry/uncoating step and in viral multipass protein biogenesis. [PMID:31273220 "Dual roles for the ER membrane protein complex in flavivirus infection"]; the EMC also supports flavivirus NS4B/non-structural multipass protein biogenesis [PMID:31067454 "Promotes Biogenesis of Dengue and Zika Virus Non-structural Multi-pass Transmembrane Proteins"].
- EMC4 (with EMC7) acts as a **molecular tether** of late endosome-ER contacts during SV40 entry, engaging Rab7 and syntaxin18 — a role partly distinct from the bulk EMC insertase. [PMID:32111841 "Selective EMC subunits act as molecular tethers of intracellular organelles exploited during viral entry"]
- Note: these antiviral/tether roles are informative but recorded as non-core context; the core EMC4 identity remains EMC complex membership + ER-membrane localization + contribution to the insertase/TA + multipass insertion processes.
