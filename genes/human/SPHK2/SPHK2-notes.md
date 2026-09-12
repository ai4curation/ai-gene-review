# SPHK2 (human) — gene review notes

UniProt: Q9NRA0 (SPHK2_HUMAN), HGNC:18859, gene 56848, chromosome 19. 654 aa (isoform 1).
EC 2.7.1.91. All quotes below from local files: `file:human/SPHK2/SPHK2-uniprot.txt`, the
GOA TSV, and cached `publications/PMID_*.md`.

## Core molecular function

SPHK2 is **sphingosine kinase 2**, a diacylglycerol-kinase-like lipid kinase (DAGKc domain,
FT DOMAIN 178..325; Pfam DAGK_cat). It phosphorylates sphingoid bases (sphingosine,
dihydrosphingosine/sphinganine, phytosphingosine) using ATP to give the corresponding
sphingoid-1-phosphate — chiefly sphingosine-1-phosphate (S1P).

- UniProt FUNCTION: "Catalyzes the phosphorylation of sphingosine to form
  sphingosine-1-phosphate (SPP), a lipid mediator with both intra- and extracellular
  functions. Also acts on D-erythro-dihydrosphingosine, D-erythro-sphingosine and
  L-threo-dihydrosphingosine." [file:human/SPHK2/SPHK2-uniprot.txt]
- Cloning/characterization: "Expression of SPHK2 in HEK 293 cells resulted in elevated SPP
  levels. d-erythro-dihydrosphingosine was a better substrate than d-erythro-sphingosine for
  SPHK2." [PMID:10751414 "Expression of SPHK2 in HEK 293 cells resulted in elevated SPP levels"]
- Catalytic activity (UniProt): "a sphingoid base + ATP = a sphingoid 1-phosphate + ADP + H(+)";
  EC=2.7.1.91. ATP-binding sites and DAGKc catalytic residues are annotated (ACT_SITE 247;
  multiple ATP BINDING sites). Cofactor Mg(2+). [file:human/SPHK2/SPHK2-uniprot.txt]

Core MF terms (author-supplied, validated): **GO:0008481 sphingosine kinase activity**,
**GO:0005524 ATP binding**.

## Localization

SPHK2 is a multi-compartment enzyme: nucleus, cytoplasm/cytosol, ER, mitochondrion inner
membrane. It carries a nuclear localization signal (MOTIF 122..130) and a PKD-regulated
nuclear export signal (MOTIF 416..425).

- Nuclear localization + G1/S arrest of DNA synthesis: "When SPHK2 was transiently expressed
  in various cell lines, it was localized in the nuclei as well as in the cytosol, whereas
  SPHK1 was distributed in the cytosol but not in the nucleus." [PMID:12954646]
- Nucleus/cytoplasm shuttling via PKD: PKD phosphorylates a serine in the NES driving nuclear
  export. [PMID:17635916 "phosphorylation of SPHK2 catalyzed by protein kinase D (PKD), which
  regulates its localization"]
- ER accumulation upon serum starvation; ER-targeting converts SPHK1 to pro-apoptotic.
  [PMID:16118219 "Serum starvation increased the proportion of SphK2 in the endoplasmic
  reticulum and targeting SphK1 to the endoplasmic reticulum converted it from anti-apoptotic
  to pro-apoptotic."]
- Mitochondrial S1P production. [PMID:20959514 "S1P, produced in the mitochondria mainly by
  sphingosine kinase 2 (SphK2)"]
- Lysosomal-membrane co-purification is from a placental lysosomal-membrane proteomics survey
  (isoform 2). [PMID:17897319]
- AD brains: SphK2 shifts from cytosol to nucleus; cytosolic expression decreases with amyloid
  density. [PMID:29615132 "SphK2 is preferentially localized in the nucleus in AD brain extracts"]

## Nuclear S1P / HDAC "moonlighting" (epigenetic role)

Landmark finding: nuclear S1P made by SPHK2 directly inhibits HDAC1/HDAC2, linking nuclear
sphingolipid metabolism to histone acetylation and gene transcription.

- "Sphingosine kinase 2 (SphK2)... was associated with histone H3 and produced S1P that
  regulated histone acetylation. S1P specifically bound to the histone deacetylases HDAC1 and
  HDAC2 and inhibited their enzymatic activity." [PMID:19729656]
- "Only H3, but not histones H4, H2B, or H2A, bound to SphK2." → histone binding (GO:0042393)
  is well supported (IDA). [PMID:19729656]
- Catalytically-dead SphK2G212E still binds H3 but does not increase acetylation → the effect
  is via S1P production, not the protein per se. [PMID:19729656 "catalytically inactive
  SphK2G212E ... did not affect its acetylation status"]

This is a **genuine second molecular function**: the ENZYME produces the inhibitory ligand
(S1P) in situ; the inhibition of HDAC is a consequence of the kinase reaction, and SPHK2
physically sits in HDAC1/2 co-repressor complexes at target promoters (p21, c-fos). I record
**GO:0046811 histone deacetylase inhibitor activity** as a justified secondary core MF (the
protein, via its product, inhibits HDAC in the same physical complex), and keep the associated
BP GO:0045815 (transcription initiation-coupled chromatin remodeling) as a non-core consequence.
Histone binding GO:0042393 (IDA) is accepted as a supporting MF.

## Apoptosis / opposing SPHK1

Unlike pro-survival SPHK1, SPHK2 is often pro-apoptotic (putative BH3-only protein) and raises
ceramide.
- "In contrast to pro-survival SphK1, the putative BH3-only protein SphK2 inhibits cell growth
  and enhances apoptosis." [PMID:16118219]
- "Overexpression of SphK2 increased incorporation of [(3)H]palmitate ... into C16-ceramide,
  whereas SphK1 decreased it." → positive regulation of ceramide biosynthesis. [PMID:16118219]
These BP consequences (positive regulation of apoptotic process GO:0043065, positive regulation
of ceramide biosynthesis GO:2000304) are real but downstream/context-dependent → KEEP_AS_NON_CORE.

## Mitochondrial respiration

Mitochondrial S1P binds prohibitin 2 (PHB2) to regulate complex IV (cytochrome-c oxidase)
assembly and respiration.
- "S1P, produced in the mitochondria mainly by sphingosine kinase 2 (SphK2), binds with high
  affinity and specificity to prohibitin 2 (PHB2)... depletion of SphK2 or PHB2 led to a
  dysfunction in mitochondrial respiration through cytochrome-c oxidase." [PMID:20959514]
Supports IMP GO:1904959 (regulation of cytochrome-c oxidase activity) → KEEP_AS_NON_CORE.

## Regulation / interactions

- ERK/MAPK phosphorylation (Ser387, Thr614) increases kinase activity (PMID:17311928, in
  UniProt PTM); PKD phosphorylation (Ser419/421) drives nuclear export (PMID:17635916).
- EEF1A1 (eEF1A) interacts with and directly enhances SPHK2 (and SPHK1) catalytic activity
  ~2.6-fold. [PMID:18263879 "GST-eEF1A1 was shown to increase SK2 activity by ~2.6-fold"]
  → the PMID:18263879 "protein binding" IPI (with UniProtKB:P68104 = EEF1A1) is a real
  interaction but bare "protein binding" is uninformative → MARK_AS_OVER_ANNOTATED.
- OPTN interaction listed in UniProt INTERACTION (Q96CV9); this is the PMID:32814053 IPI
  (neurodegeneration interactome Y2H). Bare protein binding → MARK_AS_OVER_ANNOTATED.

## Annotations needing scrutiny

- **GO:0038036 sphingosine-1-phosphate receptor activity** (IMP PMID:23106337; and IEA/ARBA):
  This MF means a GPCR that *binds S1P and signals through a G-protein* (OLS def). SPHK2 is the
  kinase that MAKES S1P; it is not the receptor. PMID:23106337 is about S1P acting on S1PR2 to
  drive ERM phosphorylation/filopodia, and states endogenous S1P is generated "predominantly by
  the action of SK1" — SK2 was knocked down as a control. So "receptor activity" for the kinase
  is a mis-typing of the MF. The IMP is experimental → MARK_AS_OVER_ANNOTATED (not REMOVE); the
  ARBA IEA duplicate → REMOVE. The paired IMP/IGI GO:0046512 "sphingosine biosynthetic process"
  from the same paper is odd (the paper is about S1P signaling, not sphingosine biosynthesis),
  but sphingosine biosynthesis is not SPHK2's reaction anyway (SPHK2 consumes sphingosine); IBA
  supports GO:0046512 phylogenetically, so keep the IBA and mark the paper-based IMP/IGI as
  over-annotation/undecided.
- **GO:0031267 small GTPase binding** (NAS PMID:12391145): abstract says "siRNA that targets
  SPK1, but not SPK2, blocks VEGF-induced accumulation of Ras-GTP" — i.e. the effect is SPHK1,
  not SPHK2, and this is only NAS (author statement) for a Ras/MAPK signaling paper, not a
  direct GTPase-binding assay. Over-annotation. [PMID:12391145 "siRNA ... that targets SPK1, but
  not SPK2, blocks VEGF-induced accumulation of Ras-GTP"]
- **GO:0005515 protein binding** IPI x3 (PMID:11777919 TRAF2/Q12933; PMID:18263879 EEF1A1;
  PMID:19729656 HDAC1/HDAC2/MBD2/SIN3A; PMID:32814053 OPTN): all bare protein binding →
  MARK_AS_OVER_ANNOTATED per policy (do not REMOVE IPI). The PMID:11777919 TRAF2 interaction is
  described for "sphingosine kinase (SphK)" generically (SPHK1 context); UNDECIDED-leaning but
  kept as over-annotation.

## Mouse-ortholog ISS/Ensembl block (Q9JIA7-projected)

A large block of ISS (GO_REF:0000024) and Ensembl-Compara IEA (GO_REF:0000107) annotations
project mouse Sphk2 (Q9JIA7) phenotypes onto human: mast-cell cytokine/IL-6/IL-13/TNF
production, NF-kB, mast-cell degranulation, ROS, ATP biosynthesis regulation, negative
regulation of cell growth, intracellular signal transduction, female pregnancy, S1P metabolism.
Most are duplicated (one ISS + one Ensembl IEA). These are legitimate ortholog transfers but are
downstream/tissue-specific consequences, not the core enzymatic function → KEEP_AS_NON_CORE
(the duplicated IEA copies REMOVE/MARK_AS_OVER_ANNOTATED as redundant electronic). "female
pregnancy" (GO:0007565, from rat ortholog A6JB73) is a weak, distal IEA → MARK_AS_OVER_ANNOTATED.

## Localization annotation handling

Nucleus, cytoplasm, cytosol, ER, mitochondrion, mitochondrial inner membrane, membrane are all
supported experimentally or by strong ISS and are ACCEPT/KEEP_AS_NON_CORE. Nucleoplasm (HPA IDA
GO:0005654) slightly conflicts with PMID:19729656 ("Endogenous SphK2 was mainly associated with
isolated chromatin and was not detected in the nucleoplasm") but is a valid HPA IF observation →
KEEP_AS_NON_CORE. Nucleosome (part_of GO:0000786, IDA PMID:19729656) reflects chromatin/histone
association → ACCEPT. Lysosomal membrane (HDA proteomics, isoform 2) → KEEP_AS_NON_CORE.

## Core function summary

1. Sphingosine kinase (GO:0008481) + ATP binding (GO:0005524): phosphorylate sphingoid bases →
   S1P/dihydro-S1P, producing GO:0006669 (sphinganine-1-phosphate biosynth) and the S1P/
   sphingolipid metabolic output.
2. Nuclear S1P-mediated HDAC inhibition (GO:0046811 histone deacetylase inhibitor activity +
   GO:0042393 histone binding): epigenetic regulation of transcription (moonlighting, but a
   direct, mechanistically-supported second function).
</content>
</invoke>
