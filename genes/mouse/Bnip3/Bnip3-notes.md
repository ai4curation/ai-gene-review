# Bnip3 (mouse, UniProt O55003) review notes

## Identity and structure

- 187 aa, NIP3 family (PANTHER PTHR15186, subfamily SF4; InterPro IPR010548; Pfam PF06553).
  Helical TM segment at 157-177 and BH3 motif at 93-118 (UniProt O55003 feature table).
  UniProt location: "Mitochondrion outer membrane {ECO:0000250}; Single-pass membrane protein"
  (by similarity to human Q12983). UniProt also notes that "Coexpression with the EIB 19-kDa
  protein results in a shift in NIP3 localization pattern to the nuclear envelope", which is
  where the nuclear envelope annotations come from. This is an artefact of co-expression with a
  viral protein, not a native location.
- The LIR motif is N-terminal. Phosphorylation of Ser17/Ser24, which flank the LIR, promotes
  binding to LC3B and GATE-16 [PMID:23209295 "phosphorylation of serine residues 17 and 24
  flanking the Bnip3 LIR promotes binding to specific Atg8 members LC3B and GATE-16"]. The
  experiments used human cell lines and the mouse HL-1 cardiac line.
- Homodimerisation through the TM helix is required for both the pro-death activity and
  autophagy induction [PMID:22505714 "Bnip3 contains a C-terminal transmembrane domain that is
  essential for homodimerization and proapoptotic function. In this study, we show that
  homodimerization of Bnip3 is also a requirement for induction of autophagy."].

## Core function: mitophagy / ER-phagy receptor

- [PMID:23209295 "The BH3-only protein Bnip3 is an autophagy receptor that signals autophagic
  degradation of mitochondria (mitophagy) via interaction of its LC3-interacting region (LIR)
  with Atg8 proteins."]
- [PMID:22505714 "The clearance of these organelles was mediated in part via binding of Bnip3 to
  LC3 on the autophagosome."; "Although ablation of the Bnip3-LC3 interaction by mutating the LC3
  binding site did not impair the prodeath activity of Bnip3, it significantly reduced both
  mitophagy and ERphagy."; "In addition, we discovered that endogenous Bnip3 is localized to both
  mitochondria and the endoplasmic reticulum (ER)."]
- Mouse in vivo: the Bnip3-null liver has increased mitochondrial mass and dysfunctional
  mitochondria [PMID:22547685 "BNip3 localizes to the outer mitochondrial membrane, where it
  functions in mitophagy and mitochondrial dynamics."; "These results identify a role for BNip3
  in limiting mitochondrial mass and maintaining mitochondrial integrity in the liver"].
- Mouse genetics of turnover: SCF-FBXL4 ubiquitinates BNIP3 and NIX. Fbxl4-/- mice have
  hyperactive mitophagy, and losing Bnip3 or Nix rescues them [PMID:36896912 "Fbxl4-/- mice exhibit
  elevated BNIP3 and NIX proteins, hyperactive mitophagy, and perinatal lethality. Importantly,
  knockout of either Bnip3 or Nix rescues metabolic derangements and viability of the Fbxl4-/-
  mice."]. PPTC7 scaffolds the substrate-PPTC7-SCF(FBXL4) holocomplex [PMID:38151018 "Mitophagy
  mediated by BNIP3 and NIX critically regulates mitochondrial mass."].
- In mouse ischaemic heart, ROS activate Bnip3 to initiate mitophagy [PMID:22044588 "ROS
  production was elevated and followed by Bnip3 activation which is an initiator of mitophagy"].

## Hypoxia / HIF-1

- HIF-1 induces BNIP3, and BNIP3 with BNIP3L is required for hypoxia-induced autophagy
  [PMID:19273585 "the combined silencing of these two HIF targets suppresses hypoxia-mediated
  autophagy"].
- In mouse macrophages, NO-induced Bnip3 expression depends on the HRE in the Bnip3 promoter
  [PMID:16954213 "Mutation of the HIF-1-binding site (hypoxia-response element) in the Bnip3
  promoter abolished BNIP3 induction"].
- PMID:18281291 (Zhang et al. 2008, J Biol Chem; HIF-1-dependent BNIP3 mitophagy in MEFs) was
  **retracted** in 2023 (the cached record says "Retraction in J Biol Chem. 2023 Aug;299(8):105125").
  It is not used as support in this review.

## Cell death (context-dependent, non-core)

- Originally identified as Nip3, an E1B-19K/BCL2 interactor [PMID:7954800 "We have isolated cDNAs
  for three different proteins, designated Nip1, Nip2, and Nip3, that interact with the 19 kDa
  protein."].
- Pro-death activity when overexpressed: mitochondrial, PT-pore-dependent, necrosis-like
  [PMID:10891486 "We propose that BNIP3 is a gene that mediates a necrosis-like cell death through PT
  pore opening and mitochondrial dysfunction."]. That paper also reports death independent of
  caspases and cytochrome c release.
- Mouse knockout: Bnip3-/- hearts show less peri-infarct apoptosis and remodelling after I/R, and
  forced cardiac expression causes apoptosis [PMID:17909626 "at 2 days after IR, apoptosis was
  diminished in Bnip3(-/-) periinfarct and remote myocardium"].
- OPA1 binding, fission and apoptosis [PMID:20436456 "We show that Bnip3 interacts with Opa1,
  leading to mitochondrial fragmentation and apoptosis."].
- Mouse macrophage NO-induced death [PMID:16954213 "These results suggest that NO-induced death of
  macrophages is mediated, at least in part, by BNIP3 induction."]. This is the source of the
  IMP/IGI intrinsic apoptotic signaling annotations.
- Mieap/SPATA18-mediated MALM [PMID:22292033 "These results suggest that two mitochondrial outer
  membrane proteins, BNIP3 and NIX, mediate MALM in order to maintain mitochondrial integrity."].

## Mouse-specific GOA references checked

- PMID:14651853 (HDA, mitochondrion): mouse mitochondrial proteome. Consistent.
- PMID:17114649 (IDA, postsynaptic density): synaptosomal phosphoproteomics. Synaptosome
  preparations contain mitochondria, so this does not establish a PSD location.
- PMID:18492766 (IDA, brown fat cell differentiation): I checked the full text at PMC2493586. Bnip3
  appears only in Table 1, among genes upregulated during in vitro brown adipogenesis (24-fold by
  PCR validation of the microarray). This is expression evidence, not a role in differentiation.
- PMID:23012479 (IEP, response to bacterium): an intestinal transcriptomics study of Listeria
  infection with lactobacilli. Bnip3 is not named in the abstract. Expression change only.
- PMID:22044588 (IPI, identical protein binding, with PR:O55003): probably detection of the Bnip3
  dimer as its "activated" form. The abstract only.

## PAINT (PTHR15186) observations

- PTN001032684 (Bilateria): MOM, mitophagy and positive regulation of apoptotic process are
  reasonable; fly BNIP3 and worm DCT-1 seed MOM and mitophagy. The nucleus IBD is seeded only by
  vertebrate BNIP3/BNIP3L/rat Bnip3, and nuclear BNIP3 is cell-type-restricted, so a Bilateria
  placement is generous. GO:0043653 (mitochondrial fragmentation involved in apoptotic process) is
  seeded by human BNIP3 alone yet placed at Bilateria. The underlying OPA1 data are from mammalian
  cells.
- PTN002689498 (Euteleostomi): ER membrane, GO:0140580 and reticulophagy are seeded by human BNIP3
  only. Placing GO:0140580 at Euteleostomi while mitophagy sits at Bilateria is conservative.
  Invertebrate DCT-1 and fly BNIP3 also act as LIR-bearing mitophagy receptors, so the MF node
  could arguably be deeper.
- PTN000795991 (root): nuclear envelope (2017) and ER (2024) are seeded by human BNIP3/BNIP3L. The
  nuclear envelope evidence traces largely to E1B-19K co-expression or cell-type-specific
  observations. ER at the root is broader and deeper than the ER membrane node at Euteleostomi.
</content>
</invoke>
