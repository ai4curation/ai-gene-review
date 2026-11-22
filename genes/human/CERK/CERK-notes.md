# CERK notes

PTHR12358 is a heterogeneous lipid-kinase family. The reviewed human branch
contains CERK, AGK, CERKL, SPHK1 and SPHK2; CERK is the only human member in
the vertebrate CERK subfamily and the only one with a CERK-focused unreviewed
Swiss-Prot entry when this pass started.

CERK core reaction and specificity:

- PMID:11956206 cloned human CERK and showed that HEK293 membrane fractions
  expressing hCERK phosphorylated ceramide but not sphingosine, other sphingoid
  bases, diacylglycerol or phosphatidylinositol.
- PMID:16269826 characterized recombinant HsCERK, showing Mg2+ dependence and
  activity against several ceramide substrates, including C2, C6 and long-chain
  ceramides.
- PMID:19168031 is an SPHK2 lipid-binding paper, but it directly assays Cerk
  activity with C6-NBD ceramide and C18:0 ceramide while using sulfatide as an
  inhibitory probe; it supports ceramide kinase activity but not CERK
  localization.

CERK localization:

- PMID:11956206 resolved the activity to HEK293 membranes rather than cytosol.
- PMID:16269826 supports a plasma-membrane pool in CHO cells mediated by the
  N-terminal PH domain.
- PMID:17392267 directly localized CERK to the TGN and showed that CERT
  knockdown dramatically reduces newly synthesized C1P, connecting ER-to-Golgi
  ceramide transfer to CERK activity.
- PMID:23863933 identified CPTP as a selective C1P transfer protein and
  presents the current CERT/CERK/CPTP model: CERK makes C1P at the cytoplasmic
  surface of the TGN, then CPTP transports it to other membranes.

Review decisions:

- Keep all ceramide kinase and ceramide metabolic process rows; the PAINT CERK
  node PTN002644025 is sound.
- Keep the plasma-membrane rows as non-core: a real CERK pool, but not the TGN
  pool in the production GO-CAM.
- Keep Golgi and cytoplasmic side of TGN membrane as core. The UOS_MCB TGN row
  cites a review and should be re-pointed to a primary TGN localization paper.
- Mark the Reactome glycosphingolipid biosynthesis parent as
  over-annotated for CERK because C1P synthesis is not sugar addition to make a
  glycosphingolipid.
- Remove the bare HuRI GO:0005515 rows under the protein-binding policy.

Family cross-check:

- SPHK1 already corrected PAINT/ARBA "sphingosine biosynthetic process" to
  sphingosine metabolic process. SPHK2 inherited the same wrong-direction
  process from PAINT and ARBA; this pass makes the SPHK2 IBA/IEA calls
  consistent with SPHK1 while leaving the weak PMID:23106337 perturbation rows
  as over-annotations.
