# SSK2 (YNR031C, UniProt P53599) curation notes

## Identity
- MAP kinase kinase kinase SSK2, 1579 aa, STE Ser/Thr kinase family, MAPKKK subfamily; C-terminal kinase domain (aa 1266-1558) and a long N-terminal regulatory region [file:yeast/SSK2/SSK2-uniprot.txt "Belongs to the protein kinase superfamily. STE Ser/Thr"].
- Paralog of SSK22 (P25390); both in PANTHER PTHR48016 / InterPro IPR017240 (MAPKKK_Ssk2/Ssk22). Human homolog MTK1/MEKK4 (MAP3K4).

## Core function: MAP3K of the Sln1 branch of the HOG pathway
- Pbs2 is activated by Ssk2 and Ssk22 under control of Sln1-Ssk1 [PMID:7624781 "Pbs2p was activated by MAP kinase kinase kinases (MAPKKKs) Ssk2p and Ssk22p that are under the control of the SLN1-SSK1 two-component osmosensor."].
- Activation mechanism: Ssk1 receiver domain binds Ssk2 N-terminus; osmostress-induced intramolecular autophosphorylation; Thr1460 activation-loop residue [PMID:9482735 "The SSK1 C-terminal receiver domain interacts with an N-terminal segment of SSK2."; "Upon hyperosmotic treatment, SSK2 is autophosphorylated rapidly, and this reaction requires the interaction of SSK1 with SSK2."; "A conserved threonine residue (Thr1460) in the activation loop of SSK2 is important for kinase activity."]. Abstract-only in cache; deep research (from full text) reports in vitro phosphorylation of kinase-dead Pbs2 by purified Ssk2 and inactivity of K1295N.
- Only the doubly unphosphorylated Ssk1 dimer activates Ssk2/Ssk22 [PMID:18573873 "Ssk1 binds to an N-terminal regulatory domain of the Ssk2/Ssk22 MAPKKKs, as demonstrated by both two-hybrid analyses and coprecipitation assays"].
- Substrate specificity via Pbs2 docking site RSD-I that binds Ssk2/Ssk22 kinase domain [PMID:12853477 "The Ssk2/Ssk22 MAPKKKs in the SLN1 branch, when activated, exclusively phosphorylate the Pbs2 MAPKK."; "The Pbs2 docking site constitutively bound the Ssk2/Ssk22 kinase domain."].
- Redundancy with Ssk22 and Ste11 [PMID:9742096 "Either SSK2, SSK22, or STE11 MAPKKK can activate PBS2 by phosphorylation."].
- Ssk1-independent activation of Ssk2 (aa 177-240) not shared by Ssk22 [PMID:23457455 "We observed that Ssk2 can be activated independent of Ssk1 upon osmotic shock by an unidentified mechanism."].
- Review: [PMID:23028184 "Ssk1 activates a pair of homologous, and functionally redundant, MAPKKKs termed Ssk2 and Ssk22"].

## Secondary, Ssk2-specific: actin cytoskeleton recovery after osmotic stress
- Ssk2 identified as actin two-hybrid interactor; forms ~1:1 complex with actin after stress; concentrates at bud neck; kinase activity and Thr1460 required for actin recovery; Ssk1 and Ssk22 not required [PMID:12181352 "Within minutes of cells' experiencing osmotic stress or catastrophic disassembly of the actin cytoskeleton through latrunculin A treatment, Ssk2p concentrates in the neck of budding yeast cells and concurrently forms a 1:1 complex with actin."; "The role of Ssk2p in actin cytoskeleton recovery does require Ssk2p localization to the neck, its interaction with actin, and the kinase activity of Ssk2p."].
- Unstressed: uniformly cytoplasmic [PMID:12181352 "on low-osmotic medium, GFP-Ssk2p was uniformly distributed throughout the cytoplasm"].
- Neck localization needs Shs1; bud cortex localization needs Spa2 [PMID:12857882 abstract]. Substrate(s) for actin recovery unknown.
- Two papers from one lab (Amberg); corroborated only by the Saito & Posas review summary. Treated as a genuine but non-core function.

## Localization summary
- Cytosol/cytoplasm (unstressed); transient bud neck, bud cortex/tip, incipient bud site after osmotic stress.

## Annotation decisions
- MAP3K activity (IDA, IEA), kinase/ATP binding IEA: ACCEPT.
- GO:0038066 p38MAPK cascade (IBA/IEA/IGI/IMP): ACCEPT; GO definition explicitly includes Hog1.
- GO:0007234 osmosensory signaling via phosphorelay: ACCEPT (Ssk2 is the direct output of Ssk1).
- GO:0071474: ACCEPT.
- Actin binding, regulation of actin cytoskeleton organization, polarized CCs: KEEP_AS_NON_CORE.
- GO:0005515 protein binding (Ssk1 x5, Slt2 x1; HTP AP-MS/PCA): REMOVE; Ssk1-Ssk2 interaction is real but no informative MF term exists for binding the activator; Slt2 AP-MS contact unexplained.

## Caveat on deep research
- Falcon report attributes localization/actin statements to "walia2008thessk2mapkkk", a Candida albicans paper; not used.
