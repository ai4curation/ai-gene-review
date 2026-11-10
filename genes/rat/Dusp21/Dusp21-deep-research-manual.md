# Dusp21 (rat, UniProt D3ZAQ8) - manual literature research

No deep-research API was available; this summary was compiled by hand from PubMed
searches ("DUSP21 OR dual specificity phosphatase 21", 9 hits, 2026-10-28) and the
cached publications in `publications/`.

## Identity

- Rat Dusp21, RGD:1560427, GeneID 302867, UniProtKB D3ZAQ8 (TrEMBL, 189 aa).
- Atypical (low-molecular-weight) dual specificity phosphatase; Pfam PF00782 DSPc;
  InterPro IPR020420 (atypical DUSP subfamily B); PANTHER PTHR46495:SF1
  (DUAL SPECIFICITY PHOSPHATASE 21). Active-site Cys105 (phosphocysteine
  intermediate, PROSITE-ProRule PRU00160) in the CX5R P-loop.
- Closest paralog DUSP18 (69% identity) [PMID:18385140 "Based on high sequence identity or similarity (69.3 and 80.4%, respectively), we identified a 21.5-kDa protein, DSP21"].

## Catalytic activity

- Human DUSP21 cloned as a testis-specific LMW-DSP; dephosphorylates pNPP and
  synthetic MAPK phosphopeptides with a preference for pTyr and doubly phosphorylated
  forms over pThr; no detectable activity on MAPKs in cells
  [PMID:12408986 "Both proteins are able to dephosphorylate the phosphotyrosine analog pNPP in vitro and can be inhibited by sodium orthovanadate"].
- Recombinant murine DSP21 hydrolyses pNPP (Km 0.92 mM, kcat/Km 91.5 s-1 M-1);
  Cys-to-Ser mutation abolishes activity
  [PMID:18385140 "Mutation of the catalytic active site cysteine to serine abolished phosphatase activity of both DSP18 and DSP21"].
- Recombinant human DUSP21 dephosphorylates STAT3 in vitro (overexpression study in HeLa)
  [PMID:39961235 "Recombinant DUSP21 directly dephosphorylated STAT3 in vitro."].

## Localization

- Rat testis: endogenous DSP21 is in mitochondria, peripherally bound to the matrix
  face of the inner membrane (subfractionation, trypsin protection, alkaline wash;
  ER marker calreticulin removed) [PMID:18385140 "subfractionation of rat testis mitochondria revealed DSP21 is localized to the matrix as a peripheral membrane protein of the inner membrane"].
- Earlier nucleus/cytoplasm localization (Hood et al. 2002) used N-terminal tags,
  which the 2008 paper shows block mitochondrial import
  [PMID:18385140 "these were overexpression experiments utilizing N-terminal tags which have been shown to commonly disrupt the localization of mitochondrial proteins"].
- Mouse sperm: cryo-EM of sperm doublet microtubules places DUSP21 as a
  microtubule inner protein (MIP) in the A-tubule lumen, anchored to tektin filaments;
  it is absent from the human sperm DMT
  [PMID:41764189 "DUSP21, a dual specificity phosphatase anchored to the TEKT3 filament, is present in mouse sperm DMT but absent in human sperm DMT"];
  [PMID:37989994 "the remaining five MIPs were sperm-specific MIPs that highly expressed in testis tissue31, including Tektin5, CCDC105, DUSP21, CFAP77 and TEX43"].

## Physiology

- Expression: testis-restricted (human, rat)
  [PMID:18385140 "DSP21 protein appeared highly expressed only in testis tissue"].
- Mouse Dusp21 knockout (X-linked, -/y): normal sperm morphology, motility and
  fertility; phosphoproteomics shows increased phosphorylation of many axonemal proteins
  [PMID:41764189 "In contrast, Dusp21-/y spermatozoa exhibited normal morphology, motility, and fertility, mirroring WT phenotypes"];
  [PMID:41764189 "In Dusp21-/y spermatozoa, an increased proportion of up-phosphorylated sites was observed, consistent with its function as a phosphatase."].
- Cancer/testis antigen in hepatocellular carcinoma; knockdown activates p38 and
  suppresses proliferation (PMID:23929653, abstract only); expression changes in other
  disease datasets (PMID:40966956, 27609023, 37476896) are not informative for function.

## Open questions

- Physiological substrates in the mitochondrial matrix and in the sperm axoneme are
  unknown.
- Whether rat sperm DMT contains Dusp21 (as in mouse) has not been tested directly.
- How the mitochondrial and axonemal localizations relate (different germ-cell stages?)
  is unresolved.
