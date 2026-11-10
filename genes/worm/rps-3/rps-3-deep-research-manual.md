# rps-3 (C23G10.3; UniProt P48152) - manual literature review

No deep-research API was available; this summary was compiled manually from the
UniProt record, cached publications and PubMed searches (October 2026).

## Identity and family

- C. elegans rps-3 (ORF C23G10.3, WBGene00004472) encodes the 247-aa small
  ribosomal subunit protein uS3 (40S ribosomal protein S3)
  [file:worm/rps-3/rps-3-uniprot.txt "Belongs to the universal ribosomal protein uS3 family."].
- Domain/family signatures: an N-terminal KH type-2 domain (residues 23-94,
  PROSITE PS50823; Pfam PF07650 KH_2), the Ribosomal_S3_C domain (Pfam PF00189),
  the eukaryote/archaea-specific uS3 signature (InterPro IPR005703; NCBIfam
  TIGR01008 uS3_euk_arch), PROSITE PS00548 (RIBOSOMAL_S3) and PANTHER
  PTHR11760:SF32. A disordered, basic C-terminal tail (216-247) is predicted by
  MobiDB-lite.
- In all characterised ribosomes uS3 sits on the head of the small subunit at the
  mRNA entry channel, where its KH domain contacts rRNA and incoming mRNA.

## Experimental structural evidence in C. elegans

- Sehgal et al. 2024 (PMID:39209556) determined a cryo-EM structure of the
  C. elegans 80S ribosome purified by sucrose gradient fractionation
  [PMID:39209556 "We purified ribosomes from C. elegans via sucrose gradient
  fractionation."]. All ribosomal proteins were modelled except stalk proteins,
  eL28 and RACK-1 [PMID:39209556 "We also modeled the ribosomal proteins, with
  the exceptions of those bound to the P- and L-stalks (uL10/P0, P1, P2, uL1,
  uL11), eL28, and RACK-1"]. uS3 is therefore part of the modelled 40S head; the
  UniProt record carries secondary-structure features derived from PDB 9CAI
  (e.g. [file:worm/rps-3/rps-3-uniprot.txt "HELIX           9..30"]).

## Phenotypic data

- Audhya et al. 2005 (PMID:16247027; full text read) used RNAi of six small-subunit
  ribosomal proteins, including RPS-3, as a general translation-inhibition control
  in a study of CAR-1/CGH-1 [PMID:16247027 "Depletions of six different ribosomal
  subunits (RPS-1, -3, -5, -11, -18, and -23) each resulted in penetrant sterility
  (unpublished data)."]. Partial depletion produced osmotically sensitive embryos
  with pleiotropic defects but no cytokinesis defect [PMID:16247027 "Defects in
  cytokinesis were not observed after partial depletion of ribosomal subunits,
  although embryos were osmotically sensitive and exhibited other pleiotropic
  phenotypes, consistent with those previously reported for general inhibition of
  translation"]. These are necessity phenotypes expected of any core ribosomal
  protein and do not identify a specific process in which RPS-3 does the work.

## Possible extra-ribosomal role in DNA repair

- Elsakrmy et al. 2022 (PMID:35809390; abstract only) identified CeRPS-3 in the
  interactome of uracil DNA glycosylase UNG-1 and confirmed the interaction by
  yeast two-hybrid [PMID:35809390 "Our analysis identified that CeUNG-1 is
  associated with the 40 S ribosomal protein S3 (CeRPS-3)"]. rps-3 knockdown
  sensitised worms, particularly apn-1 mutants, to H2O2, and CeRPS-3 expression
  rescued H2O2 sensitivity and mutator phenotype of yeast apn1 apn2 mutants
  [PMID:35809390 "A cross-species complementation experiment reveals that the
  expression of CeRPS-3 rescued the hydrogen peroxide sensitivity, and suppressed
  the high mutation frequency of the yeast AP endonuclease-deficient strain lacking
  Apn1 and Apn2."]. The authors only propose a repair role [PMID:35809390 "We
  propose that CeRPS-3 may function as an auxiliary DNA repair enzyme in C. elegans
  to process oxidative DNA lesions."]. No in vitro AP-lyase or 8-oxoG activity of
  the worm protein, and no nuclear localisation in worms, is reported in the
  abstract. Knockdown hypersensitivity is confounded by the general translation
  requirement.

## Apoptosis

- No C. elegans data link rps-3 to apoptosis. The pro-apoptotic signalling roles of
  human RPS3 (JNK activation, TRAIL/death-receptor contexts) involve pathways that
  are not conserved in the nematode core apoptosis machinery (CED-9/CED-4/CED-3).

## Conclusions for GO

- Core: structural constituent of ribosome (MF); part of cytosolic small
  ribosomal subunit (CC); cytoplasmic translation (BP).
- Non-core: RNA binding (KH domain; rRNA/mRNA contacts); nucleus (pre-40S
  assembly transit, inherited by IBA).
- Over-annotated in worm: positive regulation of apoptotic signaling pathway (IBA
  from human RPS3 only).
- DNA repair: suggestive but not sufficient for an annotation; raise as a question.
