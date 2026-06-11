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
