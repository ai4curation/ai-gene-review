# rps-11 (F40F11.1; UniProt Q20206) - manual literature review

No deep-research API was available; this summary was compiled manually from the
UniProt record, cached publications and PubMed searches (October 2026).

## Identity and family

- C. elegans rps-11 (ORF F40F11.1, WBGene00004480, GeneID 178083) encodes the
  155-aa small ribosomal subunit protein uS17 (40S ribosomal protein S11), an
  unreviewed TrEMBL entry with protein-level existence from cryo-EM structures
  [file:worm/rps-11/rps-11-uniprot.txt "Belongs to the universal ribosomal protein uS17 family."].
- Family signatures: Pfam PF00366 (Ribosomal_S17) and PF16205
  (Ribosomal_S17_N), the archaeal/eukaryotic uS17 signature (InterPro
  IPR028333; NCBIfam TIGR03630), PROSITE PS00056 (RIBOSOMAL_S17), the
  OB-fold nucleic-acid-binding superfamily and PANTHER PTHR10744
  [file:worm/rps-11/rps-11-uniprot.txt "DR   InterPro; IPR028333; Ribosomal_uS17_arc/euk."].
- uS17 is a universal small-subunit protein. In bacteria S17 is an early
  assembly protein binding the 5' domain (body) of 16S rRNA; in the eukaryotic
  40S subunit uS17 (S11) sits on the body/platform region contacting 18S rRNA.
  (General background; no C. elegans biochemistry exists.)

## Experimental structural evidence in C. elegans

- Sehgal et al. 2024 (PMID:39209556; full text read) solved a cryo-EM structure
  of the C. elegans 80S ribosome from ribosomes purified by sucrose gradient
  fractionation [PMID:39209556 "We purified ribosomes from C. elegans via sucrose
  gradient fractionation."]. All ribosomal proteins were modelled except stalk
  proteins, eL28 and RACK-1 [PMID:39209556 "We also modeled the ribosomal
  proteins, with the exceptions of those bound to the P- and L-stalks (uL10/P0,
  P1, P2, uL1, uL11), eL28, and RACK-1"]. The UniProt entry cross-references PDB
  9BH5 and 9CAI chain AL covering residues 1-155
  [file:worm/rps-11/rps-11-uniprot.txt "DR   PDB; 9CAI; EM; 2.59 A; AL=1-155."],
  so uS17 is a modelled component of the worm 40S subunit.

## Functional / phenotypic data

- Dalton and Curran 2018 (PMID:30020921; full text read) used rps-11 RNAi as a
  tool to inhibit protein synthesis [PMID:30020921 "We inhibited protein synthesis
  by reducing ribosome biogenesis (rps-11/RPS11 RNAi)"]. rps-11 RNAi impaired
  induced reporter synthesis [PMID:30020921 "protein synthesis inhibition by
  egl-45 (red) or rps-11 (green) RNAi impairs GFP biosynthesis in response to
  heat shock in animals expressing hsp-16."], caused a reversible L2 arrest with
  stress resistance, and an rps-11 promoter reporter was expressed in multiple
  tissues [PMID:30020921 "An rps-11p::gfp (R,S) and egl-45p::mCherry (T,U)
  reporter is detectable in multiple tissues at 24 hours (R,T) and 48 hours (S,U)
  of development."]. These are consequences of loss of general translation, not
  specific functions of uS17.
- Hansen et al. 2007 (PMID:17266679; abstract only) found that RNAi of
  ribosomal proteins extends lifespan [PMID:17266679 "reducing the levels of
  ribosomal proteins, ribosomal-protein S6 kinase or translation-initiation
  factors increases the lifespan of Caenorhabditis elegans"]; WormBase
  annotated rps-11 to determination of adult lifespan (IMP) from this paper. The
  abstract does not name rps-11, so the specific data could not be checked.
- Audhya et al. 2005 (PMID:16247027; full text read) used RNAi of six
  small-subunit proteins including RPS-11 as a general translation-inhibition
  control [PMID:16247027 "Depletions of six different ribosomal subunits (RPS-1,
  -3, -5, -11, -18, and -23) each resulted in penetrant sterility (unpublished
  data)."]; partial depletion gave osmotically sensitive embryos without
  cytokinesis defects. Necessity phenotypes only.

## Interpretation

- Core: structural constituent of ribosome (MF); part of cytosolic small
  ribosomal subunit (CC); cytoplasmic translation (BP).
- Lifespan, larval arrest, sterility and stress resistance are organismal
  consequences of reduced translation and do not warrant process annotations
  beyond non-core retention of the existing lifespan IMP row.

## Searches

- PubMed "rps-11 elegans" returned only PMID:30020921.
- PubMed "(F40F11.1 OR \"ribosomal protein S11\") AND elegans" returned nothing.
