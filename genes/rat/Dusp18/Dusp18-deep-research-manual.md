# Dusp18 (rat, Q6AXW7) - manual literature research

No deep-research provider was available; this summary was compiled manually from cached
publications (publications/PMID_*.md) and PubMed searches (query: DUSP18/DSP18/"dual
specificity phosphatase 18" in title, plus targeted searches), October 2026.

## Identity and family

- Rat Dusp18 (RGD:1306929, GeneID 305477), 204 aa, Swiss-Prot reviewed but PE 2 (transcript
  level). Single DSPc (tyrosine-protein phosphatase) domain 19-160 with phosphocysteine active
  site Cys104; region 95-141 "sufficient for mitochondrial localization" (by similarity).
  PANTHER PTHR46495:SF2 (DUAL SPECIFICITY PROTEIN PHOSPHATASE 18), CDD cd14573 DUSP18_21,
  InterPro IPR020420 atypical DUSP subfamily B. [file:rat/Dusp18/Dusp18-uniprot.txt]
- Atypical (low-molecular-weight) DSP: no CH2 domain and no kinase-interaction motif
  [PMID:18385140 "DSP18 and DSP21 lack these binding motifs, suggesting a unique substrate
  recognition motif for these phosphatases"].
- Closest paralog DUSP21 (testis-specific, mitochondrial matrix face of IM).

## Catalytic activity (orthologs)

- Human DUSP18 (GST fusion) hydrolyses pNPP and pThr/pTyr oligopeptides; Asp73, Cys104,
  Arg110, Ser111 required [PMID:12591617 "GST-DUSP18 fusion protein showed distinctive
  phosphatase activity toward p-nitrophenyl phosphate (pNPP), as well as oligopeptides
  containing pThr and pTyr, indicating that DUSP18 is a protein phosphatase with dual
  substrate specificity"] (abstract only).
- Human LMW-DSPs dephosphorylate MAPK peptides in vitro, prefer pTyr; no activity against
  MAPKs in cells [PMID:12408986 "However, when co-transfected with MAPKs into COS cells, the
  novel DSPs exhibited no detectable in vivo activity against MAPKs under our conditions."]
  (abstract only).
- Murine DSP18-His6: pNPP Km 0.46 mM, kcat/Km 848 s-1 M-1; C-to-S abolishes activity
  [PMID:18385140 "Mutation of the catalytic active site cysteine to serine abolished
  phosphatase activity of both DSP18 and DSP21"] (full text read).
- Human DUSP18 crystal structure (2.0 A): DSP fold plus C-terminal beta-hairpin; thermostable
  [PMID:16699184] (abstract only).
- Protein substrates (human protein, in vitro + cells): Src pTyr416
  [PMID:38346942 "Purified WT-DUSP18 potently reduced the phosphorylation of Src (Y416)
  purified from Sf9 insect cells in vitro, but the enzymatically dead DUSP18 (C104S) mutant
  had no activity"]; USF1 pThr100 [PMID:38992029 "In vitro dephosphorylation experiments
  showed that Lumacaftor inhibited the ability of purified DUSP18 to dephosphorylate WT USF1
  but had no effect on USF1T100A"]. Both full text cached.
- SAPK/JNK as substrate (overexpression, HEK293) [PMID:16720344] is disputed by Rardin et al.,
  who find no SAPK/JNK in mitochondria [PMID:18385140 "Collectively these data demonstrate the
  MAPK SAPK/JNK is not localized to the same subcellular compartment as DSP18 and, therefore,
  is highly unlikely to be its in vivo substrate under physiological conditions."].
- Other cell-line reports: MAPK14 dephosphorylation in HCC cells [PMID:35841693]; ataxin-1
  SUMOylation [PMID:29852174]. Not used for annotation.

## Localization (rat experimental)

- PMID:18385140 (full text): endogenous DSP18 in gradient-purified rat kidney mitochondria
  (ER marker calreticulin removed), immunogold EM inside mitochondria; subfractionation puts
  it in mitoplast/SMP fractions; trypsin-sensitive in mitoplasts but protected in SMPs; removed
  by alkaline (not salt) wash. Conclusion ["these results suggest that DSP18 is a mitochondrial
  IMS protein, which is peripherally associated with the IM predominantly along the cristae"].
- Internal targeting signal (aa 95-141 of the human/mouse numbering used there); N-terminal
  tags block import, explaining earlier nuclear/cytoplasmic reports from N-tagged constructs
  [PMID:18385140 "However, these were overexpression experiments utilizing N-terminal tags which
  have been shown to commonly disrupt the localization of mitochondrial proteins"].
- Released to the cytosol on staurosporine-induced apoptosis (COS-7 cells, endogenous and
  EGFP-tagged) [PMID:18385140 "These results indicate that DSP18 translocates from the IMS
  compartment to the cytosol upon mitochondrial OM permeabilization during apoptosis."].

## Physiology (mouse)

- Mouse Dusp18-/- mice show bone loss and osteoclast hyperactivation; Kp-10/GPR54 recruits
  Dusp18 and Src to the GPR54 C-terminus, Dusp18 dephosphorylates Src Y416
  [PMID:38346942 "Kiss1, Gpr54 and Dusp18 knockout mice all exhibit osteoclast hyperactivation
  and bone loss"]. This is the basis of the "negative regulation of bone resorption" rows.
  How a mitochondrial IMS protein reaches a plasma-membrane GPCR is not addressed.
- Colorectal cancer: DUSP18 dephosphorylates/stabilizes USF1 -> SREBF2 -> lanosterol release
  and immune evasion [PMID:38992029]. Cancer-context; not used for process annotation.

## Gaps

- Physiological substrate(s) in the mitochondrial IMS unknown; no rat functional data.
- Discrepancy between mitochondrial IMS localization and cytoplasmic/membrane signalling roles
  (GPR54/Src, USF1) unresolved.
