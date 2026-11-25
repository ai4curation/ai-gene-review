# rps-23 (F28D1.7; UniProt Q19877) - manual literature review

No deep-research API was available; this summary was compiled manually from the
UniProt record, cached publications and PubMed searches (October 2026).

## Identity and family

- C. elegans rps-23 (ORF F28D1.7, WBGene00004492, GeneID 178188) encodes the
  143-aa small ribosomal subunit protein uS12 (40S ribosomal protein S23)
  [file:worm/rps-23/rps-23-uniprot.txt "Belongs to the universal ribosomal protein uS12 family."].
- Family signatures: Pfam PF00164 (Ribosom_S12_S23), the eukaryote/archaea uS12
  signature (InterPro IPR005680; NCBIfam TIGR00982 uS12_E_A), PROSITE PS00055,
  PIRSF002133 and PANTHER PTHR11652
  [file:worm/rps-23/rps-23-uniprot.txt "DR   InterPro; IPR005680; Ribosomal_uS12_euk_arc."].
- uS12 is a universal small-subunit protein. In the assembled small subunit it
  lies at the decoding centre on the subunit-interface side, near the A site
  (general background from bacterial S12 and eukaryotic uS12 structural work;
  not tested in C. elegans).
- UniProt annotates a hydroxyproline at Pro62 by similarity
  [file:worm/rps-23/rps-23-uniprot.txt "/note=\"Hydroxyproline\""]; in other
  eukaryotes this residue of uS12 is hydroxylated by the OGFOD1/Tpa1 family
  prolyl hydroxylase. Not examined in the worm.

## Experimental structural evidence in C. elegans

- Sehgal et al. 2024 (PMID:39209556) solved a cryo-EM structure of the
  C. elegans 80S ribosome purified by sucrose gradient fractionation
  [PMID:39209556 "We purified ribosomes from C. elegans via sucrose gradient
  fractionation."]. All ribosomal proteins were modelled except stalk proteins,
  eL28 and RACK-1 [PMID:39209556 "We also modeled the ribosomal proteins, with
  the exceptions of those bound to the P- and L-stalks (uL10/P0, P1, P2, uL1,
  uL11), eL28, and RACK-1"], so uS12 is part of the modelled 40S subunit. The
  UniProt entry lists PDB 9BH5/9CAI chains covering the full-length protein
  [file:worm/rps-23/rps-23-uniprot.txt "DR   PDB; 9CAI; EM; 2.59 A; AX=1-143."].

## Location

- UniProt transfers cytosol, cytoplasm and rough ER locations by similarity
  (human P62266, dog Q6SA96)
  [file:worm/rps-23/rps-23-uniprot.txt "Detected in ribosomes that are associated with the
  rough endoplasmic reticulum (By similarity)."]. The rough ER location is a
  consequence of 80S ribosomes docking at the ER translocon during
  co-translational targeting; no C. elegans data.

## Genetics and phenotypes

- Cenik et al. 2019 (PMID:30799226; full text) made an rps-23 null (early stop)
  allele and named the product uS12 [PMID:30799226 "To study the effects of
  ribosomal machinery dysfunction we introduced early stop codons to generate
  loss of function mutation strains for the ribosomal protein (RP) genes: rpl-5,
  rps-30, rps-23, rps-10 and rpl-33"]. Homozygous nulls complete embryogenesis
  on maternal ribosomes [PMID:30799226 "We observed that among all homozygous RP
  mutants [rpl-5(0), rps-23(0), rps-30(0), rps-10(0) and rpl-33(0)], early and
  late embryonic development proceeded similar to wild-type embryonic
  development"] and arrest as L1 larvae [PMID:30799226 "Despite being
  phenotypically similar to wild-type first-stage (L1) larvae, the homozygous
  larvae arrest at L1 stage without any detectable growth"].
- Surya et al. 2025 (PMID:41047111; full text) showed rps-23(0) larvae arrest
  with partial M-cell divisions, less severe than large-subunit nulls, and that
  inx-14 or sinh-1 knockdown partially rescues the rps-23(0) arrest
  [PMID:41047111 "Small subunit RP mutants rps-23(0) and rps-10(0) exhibited a
  less extreme phenotype"]. These describe a ribosome-insufficiency checkpoint,
  not an activity of RPS-23 itself.
- Surya et al. 2025 J Cell Biol (PMID:39786340; full text) studied rps-23(0)/+
  heterozygotes: RPS-23 protein reduced by about half
  [PMID:39786340 "revealing reductions of ∼50% for RPL-33 and RPS-23"], with
  altered mitochondrial morphology and a modest lifespan extension without FuDR
  [PMID:39786340 "The only exception was rps-23(0)/+ mutants that displayed a
  modest but significant extension of lifespan only in the absence of FuDR"].
  Indirect consequences of reduced ribosome dosage.
- Audhya et al. 2005 (PMID:16247027; full text read) used RNAi of RPS-23 among
  six RPS proteins as a translation-inhibition control
  [PMID:16247027 "Depletions of six different ribosomal subunits (RPS-1, -3, -5,
  -11, -18, and -23) each resulted in penetrant sterility (unpublished data)."];
  partial depletion produced osmotically sensitive embryos without cytokinesis
  defects. Necessity phenotypes only.

## Assessment

- Core: structural constituent of ribosome (MF); part of cytosolic small
  ribosomal subunit (CC); cytoplasmic translation (BP).
- Phenotypes (L1 arrest, sterility, mitochondrial changes, lifespan) are
  indirect consequences of reduced translation and do not justify process
  annotations.
