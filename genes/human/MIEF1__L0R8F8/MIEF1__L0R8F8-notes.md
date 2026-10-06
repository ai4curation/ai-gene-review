# AltMIEF1 / AltMiD51 / MIEF1-MP (UniProt L0R8F8) - review notes

## Identity
- 70-aa product of an upstream ORF in exon 2 (5' leader) of the bicistronic MIEF1 gene, in a
  different frame from MiD51/MIEF1 (Q9NQG6), the outer-membrane DRP1 fission adaptor. Folder
  follows the `<HOST>__<ACC>` alt-ORF convention. The MIEF1 (MiD51) folder was not touched.
- Abundance: [PMID:30181344 "levels of the 70 amino acid altMiD51, a small protein encoded in an exon originally annotated as \"non-coding\" of MIEF1/SMCR7L/MiD51 are two to six times higher than the levels of the canonical MiD51 protein in cells and in a human tissue"]
- LYR-motif (Complex1_LYR, IPR008011 / PF05347) protein; three helices in the PDB structures.

## Localisation: mitochondrial matrix (solid)
- Proteinase K protection: [PMID:30215512 "MIEF1-MP-FLAG degradation in the proteinase K assay had an identical pattern to that of HSP60, indicating that MIEF1-MP is a mitochondrial matrix microprotein."]
- Quenching assay: [PMID:29083303 "The absence of quenching of the fluorescence compared to IMS-Venus indicates the matricial localization of altMiD51."]

## Core: MALSU1-L0R8F8-mt-ACP module on mt-LSU intermediates
- Discovery by cryo-EM: [PMID:28892042 "We conclude that L0R8F8 and mt-ACP are assembly factors for the human mitoribosome."]
- LYR contact with mt-ACP 4-PP: [PMID:28892042 "The 4-PP modification adopts a “flipped-out” conformation29 and inserts into a hydrophobic pocket of L0R8F8"]
- Anti-association: [PMID:28892042 "However, one functional consequence of the MALSU1–L0R8F8–mt-ACP module is that it would sterically obstruct the binding of the mt-SSU."]
- Reproduced in GTPBP5 (PMID:34135318), GTPBP7/GTPBP10 (PMID:38042949) and MRM2 (PMID:35177605) intermediates: [PMID:38042949 "Both, NSUN4—MTERF4 and MALSU1—L0R8F8—mtACP bind early in the mtLSU maturation process and persist over multiple maturation steps."]
- Loss of function: [PMID:31666358 "Subsequent knockout and interaction network studies in human cells revealed the LYRM member AltMiD51 to be important for optimal assembly of the large mitoribosome subunit, consistent with recent structural studies."] (abstract only; full text not retrievable)

## Translation rate (downstream)
- [PMID:30215512 "Quantitative analysis of the mtDNA-encoded protein band densities revealed a robust increase (54%) in protein levels upon MIEF1-MP overexpression, and significant decreases (32%) in cells lacking MIEF1-MP (Figure 5C)."] Rescue with siRNA-resistant MIEF1-MP controls for MiD51 co-knockdown.
- NDUFAB1 interaction is LYR-dependent but had no functional effect on complex I activity or lipid synthesis in that study.

## Fission (weak)
- Overexpression only: [PMID:29083303 "Remarkably, we found that altMiD51 also localizes at the mitochondria (Figure 12c; Figure 12—figure supplement 3) and that its overexpression results in mitochondrial fission (Figure 12d)."] This is DRP1-dependent and LYR-dependent, with no loss-of-function data. Marked as an over-annotation.

## Complex I assembly (unverified)
- The UniProt FUNCTION line cites PMID:31666358, but the abstract attributes the complex I N-module defect to LYRM2. The full text was unavailable, so this is UNDECIDED. Even if real, the defect is likely secondary to reduced ND-subunit translation.

## Decisions summary
- ACCEPT: 3x mtLSU assembly, 2x mtLSU binding, 3x mitochondrion, 4x matrix
- KEEP_AS_NON_CORE: positive regulation of mitochondrial translation
- MARK_AS_OVER_ANNOTATED: mitochondrial fission
- UNDECIDED: complex I assembly
- MODIFY: protein binding with MRPL4 -> GO:0140978
- REMOVE: protein binding with NDUFAB1 (x2), MALSU1, MRPS27
- No GO term exists for LYRM binding of the ACP phosphopantetheine arm; no NEW terms proposed.
