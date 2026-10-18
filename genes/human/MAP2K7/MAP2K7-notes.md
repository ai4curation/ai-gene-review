# MAP2K7 (MKK7, JNKK2, MEK7, SKK4) - curation notes

UniProt O14733; human; 419 aa (isoform 1); STE Ser/Thr kinase group, MAP kinase kinase subfamily.

## Identity and domain architecture

- MAP2K7 is the second JNK-activating MAP2K, cloned in 1997 by several groups
  [PMID:9207092 "Here we report the molecular cloning of a new member of the mammalian MAP kinase kinase group (MKK7) that functions as an activator of JNK"]
  [PMID:9372971 "We show that JNKK2 is a highly specific JNK kinase."]
  [PMID:9312068 "Unlike JNKK1 that activates both JNK and p38 MAP kinases, JNKK2 stimulated only JNK."]
- Closest relatives are Drosophila hemipterous (hep) and C. elegans JKK-1, not MKK4
  [PMID:9535930 "The kinase domain of MKK7 is closely related to a Drosophila JNK kinase dHep (69% identity)"].
- N-terminal disordered regulatory region carries three JNK-docking D-sites (unique among MAP2Ks)
  [PMID:16533805 "We conclude that MKK7 contains three JNK-docking sites that interact to selectively bind JNK and contribute to JNK signal transmission and specificity."]
  [PMID:25737554 "MKK7 activates the c-Jun N-terminal kinase (JNK) pathway and is the only MKK containing three motifs within its regulatory domain."]
- C-terminal DVD docking site binds upstream MAP3Ks
  [PMID:15866172 "The DVD sites bind to their specific upstream MAP kinase kinase kinases (MAPKKKs), including MTK1 (MEKK4), ASK1, TAK1, TAO2, MEKK1, and Raf-1."].

## Molecular function

- Dual-specificity MAP2K; phosphorylates the JNK Thr-Pro-Tyr activation motif, with a strong preference for the Thr
  [PMID:11390361 "JNK is phosphorylated preferentially on Tyr by MKK4 and on Thr by MKK7."]
  [Reactome:R-HSA-168162 "MKK7 a striking preference for the threonine residue (Thr-183)"].
- Thr monophosphorylation by MKK7 is sufficient to raise JNK activity; MKK4 adds the Tyr
  [PMID:11390361 "MKK7 was able to activate both wild-type JNK and a mutated JNK protein (Tyr 182 replaced with Phe)"].
- JNK-selective: does not activate p38 or ERK in vitro
  [PMID:9207092 "In vitro protein kinase assays demonstrate that MKK7 phosphorylates and activates JNK, but not the p38 or extracellular signal-regulated kinase groups of MAP kinase."]
  [PMID:9535930 "MKK7 phosphorylated and activated JNK1 but failed to activate p38 MAPK in co-expression studies."].
- Exception: in human neurons, a DLK -> MKK7 -> ERK1/2 route downstream of ApoE; immunoprecipitated MKK7 phosphorylated recombinant ERK2
  [PMID:28111074 "We observed that MKK7 directly phosphorylated ERK2"]. Single study; non-canonical.
- GO: GO:0008545 JUN kinase kinase activity (is_a GO:0004708 MAP kinase kinase activity) is the precise MF, matching the MAP2K4 review.

## Activation

- Activated by MAP3K phosphorylation of Ser271/Thr275 (MEKK1, TAK1, ASK1, MLKs, DLK)
  [Reactome:R-HSA-450337 "Residues involved in activation of these protein kinases correspond to human Ser271, Thr275 in MKK7"]
  [PMID:9312068 "JNKK2, a novel member of the MAP kinase kinase family, was phosphorylated and activated by MEKK1"].
- Endogenous MKK7 activated by IL-3, CD40, BCR, Fc receptor, heat, UV, anisomycin, hyperosmolarity and TNF
  [PMID:9535930 "MKK7 was also activated when cells were exposed to heat, UV irradiation, anisomycin, hyperosmolarity or the pro-inflammatory cytokine tumor necrosis factor-alpha."].
- TNF and IL-1 activate MKK7 but not MKK4; Mkk7-/- MEFs lose cytokine-induced JNK activation; stress-induced JNK activation needs loss of both MKK4 and MKK7
  [PMID:11390361 "disruption of the Mkk7 gene alone was sufficient to prevent JNK activation caused by proinflammatory cytokines."]
  [PMID:11390361 "Simultaneous disruption of the Mkk4 and Mkk7 genes was required to block JNK activation caused by exposure of cells to environmental stress."].

## Scaffolds and interactors (for protein-binding rows)

- JIP1/JIP2 scaffolds assemble MLK-MKK7-JNK modules
  [PMID:10490659 "Both JIP1 and JIP2 strongly potentiate JNK activation by the MLK/MKK7 signaling pathway."].
- TAK1 (MAP3K7) is an upstream MAP3K that phosphorylates MKK7
  [Reactome:R-HSA-450321] [PMID:17709393 "This signalosome is formed by TAK1 as the upstream MAPKKK, MKK7 as the MAPKK, and JNK as the last kinase in the cascade"].
- Negative regulators that bind MKK7: GADD45beta (blocks catalytic pocket) [PMID:25314077], c-FLIPL [PMID:17110930], TRIB3 [PMID:15299019, abstract only], RASSF7.
  These are functions of the partner (inhibitor), not an informative MF of MKK7; generic protein-binding rows REMOVEd (interaction not disputed).
- DUSP19/SKRP1 binds MKK7 selectively (not MKK4) and scaffolds ASK1-MKK7 (mouse)
  [PMID:11959862 "SKRP1 selectively formed the stable complexes with MKK7 but not with MKK4"]. Basis of the ISS protein phosphatase binding row.
- LRRK2 binds and can phosphorylate MKK3/6/7 [PMID:20067578]; HSP90AB1 client (kinase-wide screen) [PMID:22939624]; YWHAE (14-3-3 interactome) [PMID:36931259].

## Localization

- Cytoplasm and nucleus (UniProt, ISS from mouse); Reactome places the JNK-activating reactions in the cytosol;
  anthrax lethal factor cleaves MKK7 in the cytosol [Reactome:R-HSA-5211387].

## Physiology

- Mouse Mkk7 knockout is embryonic lethal (Mkk4 too), showing non-redundancy
  [PMID:11390361 "Studies of mice demonstrate that both the Mkk4 ( Yang et al. 1997 ; Ganiatsas et al. 1998 ; Nishina et al. 1999 ) and Mkk7 genes ( Dong et al. 2000 ) are required for embryonic viability."].

## Annotation judgement calls

- protein kinase activity / protein serine kinase / protein tyrosine kinase IEA -> MODIFY to GO:0004708 (as in MAP2K3/MAP2K4).
- IDA MAP kinase kinase activity (PMID:9535930) ACCEPT; JNKK activity (IBA/ISS/TAS) ACCEPT as core.
- Response-to-stimulus IDA rows (heat, UV, osmotic, TNF) from PMID:9535930: MKK7 activity measured after stimuli; keep as non-core.
- GO:0032206 positive regulation of telomere maintenance (IMP, PMID:21531765): RNAi screen; abstract does not mention MKK7 -> UNDECIDED.
- GO:0019901 protein kinase binding IPI (PMID:14697235): partner DLK/MAP3K12, abstract is a ZPK promoter paper; DLK-MKK7 is a known
  activator relationship (UniProt ACTIVITY REGULATION; PMID:28111074 "MKK7, a MAP-kinase kinase that is a major DLK target in neurons")
  -> kept as non-core, deferring to curator.
- ERK1/2 cascade and transcription IMP (PMID:28111074): non-canonical neuronal ApoE pathway; ERK kept as non-core, transcription marked over-annotated (indirect, AP-1 driven).
- No PMID:19593445 mechanical-stimulus row exists for MAP2K7.
