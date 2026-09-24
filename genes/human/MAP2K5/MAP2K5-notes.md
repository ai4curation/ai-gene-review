# MAP2K5 (MEK5) curation notes

UniProt Q13163 (MP2K5_HUMAN), 448 aa, HGNC:6845, 15q23. STE7-group dual-specificity MAP2K with an
N-terminal PB1 domain (~res 18-109) and C-terminal kinase domain.

## Identity and family

- STE family MAP kinase kinase subfamily [file:human/MAP2K5/MAP2K5-uniprot.txt "Belongs to the protein kinase superfamily. STE Ser/Thr"].
- Cloned in human by Zhou et al. 1995 together with ERK5, which was found as a specific two-hybrid partner of MEK5 [PMID:7759517 "ERK5 was identified by a specific interaction with the MEK5 mutants S311A/T315A and K195M in the yeast two-hybrid system"; "ERK5 did not interact with MEK1 or MEK2"].
- Rat MEK5 cloned in parallel; does not phosphorylate ERK1/2/3, JNK or p38 [PMID:7499418 "MEK5 does not phosphorylate the ERK/MAP kinase family members ERK1, ERK2, ERK3, JNK/SAPK, or p38/HOG1"]. Rat MEK5beta is "primarily cytosolic", MEK5alpha "particulate" [PMID:7499418].

## Molecular function: MAP2K for ERK5 only

- MEK5 is the dedicated and only known MAP2K for ERK5/MAPK7 [PMID:23382384 "MKK5 is the specific activator of extracellular regulated kinase 5 (ERK5)"; PMID:16260599 "In contrast to the other MAPK cascades, only one activator of ERK5, MEK5, has been cloned"].
- Phosphorylates Thr and Tyr of the ERK5 TEY motif [PMID:14583600 "MEKs activate their downstream MAPK by phosphorylation of threonine and tyrosine in the T- X-Y motif. MEK5 is the upstream BMK1 kinase"].
- In vitro reconstitution of MEKK3-MKK5-ERK5 module [PMID:23382384 "We also reconstituted the three-tiered ERK5 MAPK module (MEKK3-MKK5-ERK5) in vitro"].
- Constitutively active MEK5(D) selectively activates ERK5 in cells [PMID:9384584 "a constitutively active form of the MAP kinase kinase, MEK5(D), which selectively activates BMK1 but not other MAP kinases in vivo"].
- Deep research: ERK5 only established physiological substrate [file:human/MAP2K5/MAP2K5-deep-research-falcon.md "ERK5 remains the only firmly established direct physiological substrate of MEK5"].
- UniProt lists EC 2.7.12.2 and Ser, Thr and Tyr Rhea reactions; the Tyr and Ser reactions are generic parts of the dual-specificity MAP2K reaction, not separate functions. Better captured by GO:0004708.

## Activation and scaffolding (PB1)

- Activated by MEKK2/MEKK3 through PB1-PB1 heterodimerisation [PMID:12912994 "The PB1 domains of MEKK2 and MEKK3 bind the PB1 domain of MEK5"; "the PB1 domain mediates the association of MEKK2 and MEKK3 with MEK5"].
- Activation-loop sites Ser311/Thr315 (S311D/T315D phosphomimetic activates ERK5) [PMID:14583600 "Dual phosphorylation site mutation of MEK5alpha (Ser-311 --> Asp and Thr- 315 --> Asp; MEK5alpha(S311D/T315D)) activated BMK1"].
- MEK5alpha N-terminus contains a unique ERK5 docking site (acidic cluster 61, 63-66) [PMID:16260599 "It consists of a cluster of acidic residues at position 61 and positions 63 to 66"].
- PB1 domain co-recruits activator and substrate: bivalent adaptor [PMID:23382384 "it also enables co-recruitment of the upstream activating enzyme and the downstream substrate into one signaling competent complex"].
- UniProt: "Acts as a scaffold for the formation of a ternary" MAP3K2/MAP3K3-MAP2K5-MAPK7 complex.
- Isoform note: MEK5beta (lacks 89 N-terminal residues incl. PB1) behaves as dominant negative in some studies [PMID:14583600 "the presence of MEK5beta prevented association of MEK5alpha with BMK1"], though Seyfried et al. find both catalytically active [PMID:16260599 "Our data demonstrate that both MEK5α and MEK5β are catalytically active enzymes"].

## Biological roles

- Mouse Mek5 knockout: embryonic lethal ~E10.5 with cardiac defects, reduced proliferation/increased apoptosis; MEK5 required for ERK5 activation and MEF2 activity [PMID:15601854 "mek5(-/-) embryos die at approximately embryonic day 10.5 (E10.5)"; "MEK5 is required for mediating extracellular signal-regulated kinase 5 (ERK5) activation"].
- Endothelial shear stress: laminar flow induces KLF2 via MEK5/ERK5/MEF2; MEK5 activation "both required and sufficient" [PMID:16341264 "this flow-mediated increase in expression occurs via a MEK5/ERK5/MEF2 signaling pathway"].
- Constitutively active MEK5 in human endothelial cells: apoptosis resistance, decreased angiogenic/migratory/inflammatory potential via KLF4 [PMID:20551324 "constitutive Erk5 activation elicits an overall protective phenotype characterized by increased apoptosis resistance and a decreased angiogenic, migratory, and inflammatory potential"]. This is the source (via rat RGD IMP, then ISS/IEA to human) of many BP annotations (IL-8, CXCL2, NF-kB, cytokine response, heterotypic adhesion, sprouting angiogenesis, apoptosis). These are downstream outputs of ERK5/KLF4 transcription, so non-core for MEK5.
- Cardiomyocyte hypertrophy (CT-1) needs MEK5-ERK5 [PMID:15623435 "CT-1-induced cell hypertrophy was suppressed by overexpression of a dominant-negative MEK5 mutant"] -> source of rat positive regulation of cell growth.
- Cardiac anti-apoptosis via ERK5-CHIP-ICER [PMID:20724525] -> source of rat "negative regulation of smooth muscle cell apoptotic process"; the abstract is about cardiomyocytes, so the cardiac muscle term (GO:0010667) fits better.
- Biliary epithelial proliferation in PCK rats, MEK5 siRNA inhibits [PMID:15631999 "The increased proliferative activity was significantly inhibited by the transfection of short interfering RNA against MEK5 mRNA"].
- IGF-2 pro-myogenic signalling in mouse C2 myoblasts [PMID:19654213 "transfection of myoblasts with dominant-negative MEK5 blocked the pro-myogenic action of IGF-2"] -> source of IGF receptor signaling pathway.
- Mouse spindle IDA (PMID:15509711) is a broad phospho-antibody immunostaining survey of many kinases in M phase; weak for a specific MEK5 spindle location.
- TGF-beta increases MEK5 association with phospho-ERK5 and MEF2C in renal PTEC [PMID:18588859 "TGF-beta increased the association of MEK5 with phospho-ERK5 and MEF2C"]; MEF2C is an ERK5 substrate, so MEF2C co-IP is likely indirect.

## Interactions (GO:0005515 IPI rows)

- Informative: MAPK7 (substrate; NbExp=8), MAP3K2 (NbExp=7), MAP3K3 (NbExp=5) -> GO:0051019 / GO:0031435.
- HSP90AB1 (NbExp=4): kinase client of HSP90 (Taipale 2012) -> GO:0051879, consistent with BRAF review.
- SQSTM1 (PB1-PB1, by similarity in UniProt) - function unclear; LNX2, GRB2, ZNF620, ZNF426, GUCD1, PFDN5, DUSP21 - binary screens only; REMOVE generic binding.

## Localization

- No human CC annotations other than an IEA spindle. Deep research: predominantly cytosolic; ERK5 (not MEK5) translocates to the nucleus. Rat MEK5beta cytosolic (PMID:7499418). Mouse has IEA cytoplasm (UniProt SL). Not added as NEW; cytoplasm used as core-function location context.

## Decisions summary

- Core: GO:0004708 MAP kinase kinase activity; GO:0070375 ERK5 cascade; GO:0071499 cellular response to laminar fluid shear stress.
- Generic kinase MF terms (protein kinase / tyrosine kinase / serine kinase activity) -> MODIFY to GO:0004708 (consistent with MAP2K3).
- Signal transduction -> MODIFY to GO:0070375 ERK5 cascade.
- Did not propose NEW heart development / angiogenesis (necessity evidence from knockouts, not participation) nor MAP kinase scaffold activity (raised as question).
