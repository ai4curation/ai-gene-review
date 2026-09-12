# NBR1 (Next to BRCA1 gene 1 protein) — review notes

UniProt: Q14596 (NBR1_HUMAN), 966 aa. HGNC:6746. Located head-to-head with BRCA1 at 17q21.

## Domain architecture (UniProt features)
- **PB1 domain** (4–85): mediates self-oligomerization and heterodimerization with SQSTM1/p62 [PMID:12813044; PMID:19250911]. Asp-50 is required for p62 interaction.
- **ZZ-type zinc finger** (212–264): binds two Zn2+ ions (8 coordinating residues). Basis of GO:0008270 zinc ion binding.
- **ATG8/LIR regions** (542–636 and 727–738): LC3-interacting regions; Tyr-732 mutation abolishes ATG8-family binding [PMID:19250911].
- **UBA domain** (913–957): binds K48- and K63-linked polyubiquitin; F929A abolishes ubiquitin binding [PMID:24692539, PMID:19427866].
- An Ig-like / FW region (Nbr1_FW, ~365–485; PDB 4OLE).

## Core function: ubiquitin-binding selective autophagy receptor
NBR1 is a ubiquitin-binding autophagy cargo receptor that, like its functional partner SQSTM1/p62, bridges ubiquitinated cargo to ATG8/LC3 on the forming autophagosome.
- [PMID:19250911 "NBR1 (neighbor of BRCA1 gene 1)... is an autophagy receptor"] — NBR1 contains PB1, ZZ, two LIR/ATG8-binding regions, and a UBA domain; interacts with SQSTM1, MAP1LC3A/B/C, GABARAP, GABARAPL1, GABARAPL2; required for autophagosomal degradation of ubiquitinated substrates; Asp-50 (p62 binding) and Tyr-732 (ATG8 binding) mutants characterized.
- [PMID:19427866 "the nbr1 UBA domain binds to lysine-48 and -63 linked polyubiquitin-B chains. Nbr1 also binds to the autophagic effector protein LC3-A... Ubiquitin-binding... is required to target nbr1 to LC3 and polyubiquitin-positive bodies"]. Also binds USP8 and p14/Robld3 (endosomal trafficking).
- [PMID:24692539 "Solution structure of the UBA domain... and its interaction with ubiquitin and polyubiquitin"] — F929A complete loss of ubiquitin binding; structural basis of UBA-Ub binding. (Not cached; verified via PubMed and UniProt features.)
- [PMID:34471133 "define the roles of the human cargo receptors p62, NBR1 and TAX1BP1 in ubiquitin condensate formation and autophagy initiation"] — in vitro reconstitution; NBR1 (with p62/TAX1BP1) drives ubiquitin condensate formation and autophagy initiation. Interacts with TAX1BP1. full_text_available: true.
- [PMID:33226137] — receptor-mediated clustering of FIP200; NBR1 flux used as a selective-autophagy readout; NBR1 interacts with TAX1BP1.

## Aggrephagy / protein aggregation
- [PMID:24879152 "NBR1... binds UB/ubiquitin and the autophagosome-conjugated MAP1LC3/LC3 proteins, thereby ensuring ubiquitinated protein degradation... NBR1 phosphorylation by GSK3 at Thr586 prevents the aggregation of ubiquitinated proteins"] — NBR1 promotes formation of ubiquitinated protein aggregates; GSK3A phosphorylation at Thr-586 inhibits this; relevant to inclusion body myositis. Supports aggrephagy (GO:0035973) and the dual aggregate-formation function noted in UniProt.
- [PMID:20417604] — Alfy/WDFY3 scaffolds selective macroautophagy of aggregated proteins with p62/NBR1-positive proteins (NBR1 contextually a cargo partner). Background/context, NBR1 named in network.

## Pexophagy (peroxisome turnover)
- Reactome R-HSA-9664873 "Pexophagy"; reactions R-HSA-9664867/9664880/9664881 (NBR1 binds MAP1LC3B; MAP1LC3B binds ATM:Ub-p-PEX5:SQSTM1:NBR1; NBR1 binds ATM:Ub-p-PEX5:SQSTM1). NBR1 (with p62) is the receptor for ubiquitinated PEX5 / peroxisomal membrane proteins → peroxisomal membrane localization (GO:0005778) is functionally grounded.

## Innate immunity / antiviral selective autophagy
- [PMID:35914352 "NBR1 mediates autophagic degradation of IRF3 to negatively regulate type I interferon production"] — NBR1 binds IRF3 (both unphosphorylated and phosphorylated) and targets it for autophagic degradation; negatively regulates type I IFN. Interacts with IRF3; induced upon viral infection.
- [PMID:33577621 "PB1 protein of influenza A virus inhibits the innate immune response by targeting MAVS for NBR1-mediated selective autophagic degradation"] — NBR1 recognizes ubiquitinated MAVS (K27-linked) and delivers it to autophagosomes; influenza PB1 hijacks this; NBR1 deficiency impairs MAVS degradation. Verified via PubMed (not cached). Supports antiviral innate immune response / selective autophagy roles.

## SRBD1 clearance / cellular senescence
- [PMID:38169523 "Selective Autophagy Receptor NBR1... Directing the Clearance of SRBD1"] — NBR1 interacts with SRBD1 and clears it via the autophagic-lysosomal pathway, retarding nucleus pulposus cell senescence. full_text_available: true.

## FGFR / endosomal signaling
- [PMID:19822672 "Neighbor of BRCA1 (NBR1)... interacts and colocalizes with Spred2... Attenuation of FGF signaling by Spred2 is dependent on the interaction with NBR1... redirecting the trafficking of activated receptors to the lysosomal degradation pathway"] — NBR1 as late endosomal protein in FGFR down-regulation. Supports late endosome (GO:0005770) localization.

## Bone / osteoblast / MAPK (mouse-derived, ISS/IEA from Ensembl Compara to mouse ortholog P97432/Q501R9)
The negative regulation of osteoblast differentiation (GO:0045668), regulation of bone mineralization (GO:0030500), regulation of stress-activated MAPK cascade (GO:0032872) and MAPK binding (GO:0051019) annotations originate from BHF-UCL ISS and Ensembl Compara IEA, ultimately tracing to mouse Nbr1 work (Whitehouse et al.; p38 MAPK scaffold / osteoblast studies). NBR1 functions as a p38/MAPK scaffold and a truncated-NBR1 transgenic mouse shows increased bone mass via osteoblast effects. These are real but secondary/pleiotropic roles, supported only by ISS/IEA in human → KEEP_AS_NON_CORE.

## Th2 / PB1 signalling adapter
- [PMID:20808283 "NBR1 is a new PB1 signalling adapter in Th2 differentiation and allergic airway inflammation in vivo"] — T-cell-specific NBR1-deficient mice; impaired Th2 differentiation. PB1-domain adapter role; pleiotropic/immune developmental role (no GO term currently annotated from it; it is one of the IPI protein-binding sources).

## Sarcomere / M band / titin
- UniProt: Cytoplasm, myofibril, sarcomere, M line (by similarity to mouse Q501R9). Interacts with titin/TTN and TRIM55 [PMID:15802564]. Basis of M band (GO:0031430) IEA-SubCell. Real but tissue-specific (cardiac/skeletal muscle) → KEEP_AS_NON_CORE.

## Localization summary
Cytoplasm/cytosol (core), autophagosome/phagophore assembly site, lysosome (degraded there), late endosome, peroxisomal membrane (pexophagy), M band (muscle). Mitochondrion colocalization (GO:0005739, PMID:21296869) reflects Parkin-mitophagy context. Mitochondrial intermembrane space (GO:0005758, Ensembl IEA) and membrane (GO:0016020, HDA from NK-cell membrane proteome PMID:19946888) are low-confidence/generic.

## Protein binding (IPI) sources
Many GO:0005515 protein binding annotations from interactome/specific studies: PMID:19250911 (SQSTM1, ATG8s), 19427866 (USP8, ubiquitin), 20010802 (Nix mitophagy context), 20368287 (PI3K-mTOR interactome), 20417604 (Alfy), 20562859 (autophagy network), 20808283 (Th2 PB1 adapter), 24879152 (GSK3), 25416956/33961781 (HuRI/BioPlex interactomes), 29568061 (MAC-tag), 30824926 (GSK3A/sperm), 34524948 (macroautophagy proximity interactome), 19822672 (Spred2/FGFR). All KEEP_AS_NON_CORE per "avoid bare protein binding" guideline; informative partners noted in reasons.

## Key GO terms verified via QuickGO API
- GO:0035973 aggrephagy = "selective degradation of protein aggregates by macroautophagy"
- GO:0000425 pexophagy
- GO:0160247 autophagy cargo adaptor activity = "binding activity of a molecule that brings together a cargo, targeted for degradation via autophagy, to a phagophore" (the precise MF for an autophagy receptor)
- GO:0061753 substrate localization to autophagosome
- GO:0032480 negative regulation of type I interferon production
- GO:0140374 antiviral innate immune response
