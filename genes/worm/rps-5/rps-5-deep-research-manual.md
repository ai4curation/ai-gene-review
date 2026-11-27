# rps-5 (T05E11.1; UniProt P49041) - manual literature review

No deep-research API was available; this summary was compiled manually from the
UniProt record, cached publications and PubMed searches (October 2026).

## Identity and family

- C. elegans rps-5 (ORF T05E11.1, WBGene00004474, GeneID 178012) encodes the
  210-aa small ribosomal subunit protein uS7 (40S ribosomal protein S5)
  [file:worm/rps-5/rps-5-uniprot.txt "Belongs to the universal ribosomal protein uS7 family."].
- Family signatures: Pfam PF00177 (Ribosomal_S7), the eukaryote/archaea uS7
  signature (InterPro IPR005716; NCBIfam TIGR01028 uS7_euk_arch), PROSITE
  PS00052 (RIBOSOMAL_S7), PIRSF002122 and PANTHER PTHR11205
  [file:worm/rps-5/rps-5-uniprot.txt "DR   InterPro; IPR005716; Ribosomal_uS7_euk/arc."].
- uS7 is a universal small-subunit protein. In bacteria it is a primary binder of
  the 3' major domain of 16S rRNA and organises the head; in the 40S subunit it
  sits on the head near the E site and mRNA exit path, contacting rRNA and the
  mRNA upstream of the codon in the P site. (General background; no C. elegans
  biochemistry exists.)

## Experimental structural evidence in C. elegans

- Sehgal et al. 2024 (PMID:39209556) solved a cryo-EM structure of the
  C. elegans 80S ribosome purified by sucrose gradient fractionation
  [PMID:39209556 "We purified ribosomes from C. elegans via sucrose gradient
  fractionation."]. All ribosomal proteins were modelled except stalk proteins,
  eL28 and RACK-1 [PMID:39209556 "We also modeled the ribosomal proteins, with
  the exceptions of those bound to the P- and L-stalks (uL10/P0, P1, P2, uL1,
  uL11), eL28, and RACK-1"], so uS7 is part of the modelled 40S subunit. The
  UniProt entry carries secondary-structure features from PDB 9CAI covering
  residues ~21-209 [file:worm/rps-5/rps-5-uniprot.txt "HELIX           194..209"].

## Ribosome biogenesis / nucleolus

- UniProt transfers (By similarity, from human P46782 and mouse P97461) a role as
  part of the small-subunit (SSU) processome and a nucleolar plus cytoplasmic
  location [file:worm/rps-5/rps-5-uniprot.txt "Part of the small subunit (SSU)
  processome, first precursor of the small eukaryotic ribosomal subunit."].
  There are no C. elegans data on nucleolar localisation or pre-rRNA processing
  for RPS-5; the claim rests on orthology to the human protein.

## Phenotypic data

- Audhya et al. 2005 (PMID:16247027; full text read) used RNAi of six
  small-subunit ribosomal proteins including RPS-5 as a general
  translation-inhibition control in a CAR-1/CGH-1 cytokinesis study
  [PMID:16247027 "Depletions of six different ribosomal subunits (RPS-1, -3, -5,
  -11, -18, and -23) each resulted in penetrant sterility (unpublished data)."].
  Partial depletion gave osmotically sensitive embryos without cytokinesis
  defects [PMID:16247027 "Defects in cytokinesis were not observed after partial
  depletion of ribosomal subunits, although embryos were osmotically sensitive
  and exhibited other pleiotropic phenotypes, consistent with those previously
  reported for general inhibition of translation"]. These are necessity
  phenotypes expected of any core ribosomal protein and do not justify a specific
  developmental process annotation.

## Literature not relevant

- PubMed query "(rps-5 OR ribosomal protein S5 OR T05E11.1) AND elegans" returned
  only PMID:23698443 (Houtkooper et al. 2013), which concerns the mitochondrial
  ribosomal protein mrps-5 (E02A10.1), a different gene [PMID:23698443 "We
  identified Y37A1C.1/nkcc-1, E02A10.1/mrps-5, and F25C8.5/ttll-9 as worm
  homologs of Slc12a1, Mrps5, and Ttl, respectively."]. Not used as evidence for
  rps-5.

## Summary for curation

- Core: structural constituent of ribosome (MF); part of cytosolic small
  ribosomal subunit (CC); cytoplasmic translation (BP).
- Non-core: rRNA binding and mRNA binding (contacts within the 40S subunit);
  nucleolus / SSU processome and ribosomal small subunit biogenesis (by
  orthology only).
