# EMC10 (Q5UCC4) review notes

## Identity / domain architecture
- Human EMC10 = "ER membrane protein complex subunit 10" (C19orf63, INM02). 262 aa precursor; N-terminal signal peptide (1..25), large lumenal domain (26..221), single TM helix (222..242), short cytoplasmic tail (243..262). Single-pass type I ER membrane protein, N-glycosylated at Asn-182 [file:human/EMC10/EMC10-uniprot.txt "Single-pass type I membrane protein"], [file: "N-linked (GlcNAc...) asparagine"].
- It is the LUMENAL/peripheral subunit of the EMC; structural cryo-EM studies (PMID:32439656, PMID:32459176) place EMC10's bulk in the ER lumen. It is NOT a catalytic insertase subunit (the membrane insertase core is EMC3/EMC6).
- Belongs to the EMC10 family; Pfam PF21203, TCDB 3.A.27.1.1 (EMC family) [file: "the endoplasmic reticulum membrane protein insertion complex (emc) family"].

## Core function = EMC complex membership + ER membrane
- EMC is a transmembrane-domain insertase/chaperone enabling energy-independent insertion of newly synthesized membrane proteins into the ER membrane; inserts tail-anchored (TA) proteins post-translationally and multipass membrane proteins co-translationally, and sets N-exo topology of multipass proteins (e.g. GPCRs) [file: "enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins"].
- EMC10 is a bona fide EMC subunit: identified in the EMC by AP-MS in the ERAD-network study [PMID:22119785], and present in the cryo-EM EMC structure [PMID:32439656]. UniProt SUBUNIT: "Component of the ER membrane protein complex (EMC)." [file: "Component of the ER membrane protein complex (EMC)."]
- The insertase activity is a property of the holo-complex; EMC10 "contributes_to" membrane insertase activity (GO:0032977) in IMP screens [PMID:29809151, PMID:30415835]. For a non-catalytic lumenal subunit, the core MF is complex membership, not standalone insertase catalysis. The `contributes_to` qualifier is appropriate and is kept as non-core.

## Secreted form / HSS1 / angiogenesis (peripheral, isoform 2)
- Isoform 2 (Q5UCC4-2) = "Hematopoietic Signal peptide-containing Secreted 1" (HSS1); isoform 1 = HSM1 (membrane). Junes-Gill et al. described HSS1/HSM1 from hematopoietic stem cells; HSS1 is secreted and suppresses glioma growth [PMID:20680400 "the discovery of HSS1 (Hematopoietic Signal peptide-containing Secreted 1) and its splice variant HSM1"].
- INM02 (= EMC10) is detectable in human serum and glucose-regulated in islets [PMID:19570817 "INM02 could be detectable in human serum by ELISA"].
- Reboll et al.: secreted EMC10 is a bone marrow-derived angiogenic growth factor; stimulates endothelial cell migration/outgrowth via p38 MAPK/MK2/PAK after MI [PMID:28931551 "discovered a poorly characterized secreted protein, EMC10 ... showing activity in an angiogenic screen"], [file: "Stimulates cardiac endothelial cell migration and outgrowth via the activation of p38 MAPK, PAK and MAPK2 signaling pathways"].
- These secreted/angiogenesis roles are real (EXP/IDA/IMP supported) but are peripheral to EMC's core ER membrane-insertion function and pertain largely to the secreted isoform → KEEP_AS_NON_CORE.

## Disease
- Biallelic loss-of-function variants cause NEDDFAS (neurodevelopmental disorder with dysmorphic facies and variable seizures; MIM:619264) [PMID:32869858, PMID:33531666]. Consistent with EMC being broadly required for membrane proteostasis.

## Annotation review decisions
- EMC complex (GO:0072546) IBA/IPI/IDA, ER membrane (GO:0005789) IDA/IEA/NAS → ACCEPT, CORE.
- membrane insertase activity (GO:0032977) contributes_to, IMP → KEEP_AS_NON_CORE (complex-level catalysis; EMC10 lumenal subunit contributes but is not catalytic).
- protein insertion into ER membrane by stop-transfer (GO:0045050) and tail-anchored insertion (GO:0071816), IDA/IMP → KEEP_AS_NON_CORE (correct EMC processes but EMC10 is a structural subunit; complex-level BP).
- membrane (GO:0016020) IDA → ACCEPT (correct but generic vs ER membrane).
- extracellular region (GO:0005576) EXP×3 + IEA → KEEP_AS_NON_CORE (real secreted isoform 2 / serum, peripheral to EMC).
- angiogenesis terms GO:0045766, GO:0010595, GO:0001938 → KEEP_AS_NON_CORE (real but secreted-form moonlighting, peripheral).
- No clearly wrong IEA to REMOVE; no unverifiable experimental annotations requiring UNDECIDED (all cited PMIDs cached, organism human).

## Cached publication status
- full_text_available: 29242231 true, 22119785 true, 20680400 true, 30415835 (check), 29809151 (check); 32439656 false, 28931551 false, 19570817 false (abstract only). For abstract-only papers, supporting_text drawn from UniProt file or abstract.
</content>
