# MLA10 (barley, Q6WWJ4) research notes

## Identity
- UniProt Q6WWJ4 (TrEMBL, unreviewed), EMBL AY266445 / AAQ55541, 951 aa, CC (Rx_N) - NB-ARC - WHD - LRR.
- Bai et al. 2012 used AY266445 as Mla10 [PMID:22685408 "AY266445 (Mla10)"], so this accession is the MLA10 studied there.
- Saur et al. 2019 used Mla10 GU245946, listed as "Different from NCBI:AY266445.1" [PMID:30777147]; allele-level identity with Q6WWJ4 is therefore not exact for the AVRA10 recognition data, but both are MLA10.

## Effector recognition
- AVRa10 (CSEP0141 allele) isolated; recognised by MLA10 [PMID:30777147 "We report here the isolation of Bgh AVRa7, AVRa9, AVRa10, and AVRa22, which encode small secreted proteins recognized by allelic MLA7, MLA9, MLA10, and MLA22 receptors, respectively."]
- Association: [PMID:30777147 "Co-expression of AVRa10-nLUC with Mla10-cLUC resulted in the detection of a 3.5-fold higher LUC activity when compared to expression of its virulent variants AVRa10-V/AVRa22-V-nLUC and AVRa22-nLUC (Figure 5C)."]; yeast: [PMID:30777147 "co-expression of BD-Mla10 with AD-AVRa10 in yeast resulted in leucine reporter gene activation"]. No purified-protein binding or MLA10-AVRA10 structure.
- LRR determines specificity [PMID:33534797 "the 58 amino acid differences between the LRRs of Mla10 and Mla22 are major determinants of respective recognition specificities for the allelic AVRA10 and AVRA22 effectors."]

## Localisation and signalling
- Nucleocytoplasmic; nuclear pool needed and sufficient for resistance [PMID:22685408 "We have previously shown that MLA10 locates to both the cytoplasm and the nucleus, and importantly, the nuclear pool is required for its disease resistance [44]."]
- Cytoplasmic pool drives cell death; resistance separable from death [PMID:22685408 "the cytoplasmic pool of MLA10 alone is sufficient to induce cell-death, whereas nuclear-localized MLA10 is unable to induce cell-death, but is capable of conferring disease resistance."]
- Contrast: wheat homologues Sr33/Sr50 act in the cytosol for both death and resistance [PMID:27555587 "full-length Sr33 proteins targeted to the cytosol provided rust resistance, whereas nuclear-targeted Sr33 was not functional"]. Open question.
- WRKY/MYB6: [PMID:17185563 "Recognition of the fungal avirulence A10 effector by MLA10 induces nuclear associations between receptor and WRKY transcription factors."]; [PMID:23532068 "The activated form of full-length MLA10 receptor is needed to release MYB6 activator from WRKY1 repression and to stimulate MYB6-dependent gene expression."]
- CC homodimer = minimal cell-death module [PMID:21402358 "MLA CC mutants that fail to self-interact impair in planta cell death activity triggered by the CC domain alone"]
- NB-ARC switch: P-loop K207R inactive; MHD D502V autoactive [PMID:22685408 "the F83E and the P-loop K207R mutation rendering MLA10 inactive"]. SGT1 required for cell death in N. benthamiana.
- miR9863 targets MLA1 but not MLA10 [PMID:25502438] (background).

## Curation decisions (6 GOA rows, all IEA)
- GO:0002758 innate immune response-activating signaling pathway: ACCEPT (receptor initiates pathway).
- GO:0006952 defense response: MODIFY -> GO:0050832 defense response to fungus.
- GO:0098542 defense response to other organism (TreeGrafter): MODIFY -> GO:0050832.
- GO:0009626 plant-type HR: KEEP_AS_NON_CORE (real output but separable from resistance).
- GO:0042742 defense response to bacterium (ARBA): REMOVE (no bacterial recognition for any MLA).
- GO:0043531 ADP binding: KEEP_AS_NON_CORE (NB-ARC switch; not directly measured).
- NEW: GO:0140376 innate immune receptor activity (comparators I2, RGA5, RPP1, RPP4, RPP13 carry it with EXP); GO:0005634 nucleus; GO:0005737 cytoplasm.
- Necessity vs participation: MLA10 is the receptor that performs the recognition step and its CC directly engages WRKY1/MYB6, so process terms reflect participation, not just mutant phenotype.
- Deep research (falcon) consulted: file:HORVU/MLA10/MLA10-deep-research-falcon.md.
