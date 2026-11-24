# YWHAE manual literature synthesis

No deep-research provider was available for this review. This synthesis was compiled manually
from the cached UniProt record, GO-CAM 65692e7e00001822, and cached publications in
`publications/`.

## Core molecular role

- YWHAE encodes 14-3-3 epsilon, one of the human 14-3-3 paralogs. UniProt describes it as
  an adaptor for many signaling pathways that usually binds client phosphoserine or
  phosphothreonine motifs
  [file:human/YWHAE/YWHAE-uniprot.txt "Binds to a large number of partners, usually by recognition of a phosphoserine or phosphothreonine motif"].
- The 14-3-3 fold acts as a dimer. UniProt records 14-3-3 epsilon homodimerization and
  heterodimerization with 14-3-3 zeta/YWHAZ
  [file:human/YWHAE/YWHAE-uniprot.txt "Homodimer (PubMed:17085597). Heterodimerizes with YWHAZ"].
- HSF1 is a clear phospho-client. ERK/GSK3-dependent phosphorylation of HSF1 at Ser303 and
  Ser307 enables YWHAE binding, which represses HSF1 transcriptional activity and sequesters
  it in the cytoplasm
  [PMID:12917326 "Furthermore, the serine phosphorylation-dependent binding of HSF1 to 14-3-3 epsilon results in the transcriptional repression of HSF1 and its sequestration in the cytoplasm."].
- TAZ/WWTR1 is a second canonical sequestered client. Its phosphorylation-dependent 14-3-3
  binding inhibits TAZ transcriptional coactivation by driving nuclear export
  [PMID:11118213 "14-3-3 binding requires TAZ phosphorylation on a single serine residue, resulting in the inhibition of TAZ transcriptional co-activation through 14-3-3-mediated nuclear export."].
- A 2023 study adds hnRNP C as a nuclear client exported by 14-3-3 epsilon to the cytoplasm,
  where it is degraded by the ubiquitin-proteasome system
  [PMID:37599448 "Taken together, these data demonstrated that hnRNP C protein is exported from the nucleus by 14-3-3ε and was ubiquitinated and degraded by proteasomes in the cytoplasm."].
- 14-3-3 epsilon also has a neurodevelopmental NDEL1/LIS1 arm. The Miller-Dieker
  syndrome paper showed Ywhae-dependent neuronal-migration defects in mice and connected
  them to binding of CDK5/p35-phosphorylated NUDEL/NDEL1, maintenance of NUDEL
  phosphorylation and proper NUDEL/LIS1 localization
  [PMID:12796778 "14-3-3epsilon binds to CDK5/p35-phosphorylated NUDEL and this binding maintains NUDEL phosphorylation. Similar to LIS1, deficiency of 14-3-3epsilon results in mislocalization of NUDEL and LIS1, consistent with reduction of cytoplasmic dynein function."].

## Innate immune client pathways

- In RIG-I signaling, 14-3-3 epsilon is not merely an interactor. It is part of the RIG-I
  translocon and is needed for RIG-I/TRIM25 membrane redistribution during acute RNA virus
  infection
  [PMID:22607805 "Our results define 14-3-3ε as a key component of a RIG-I translocon required for innate antiviral immunity."].
- In the RNF115/TLR-trafficking model, AKT1 phosphorylation lets RNF115 associate with
  multiple 14-3-3 proteins, including 14-3-3 epsilon, which facilitates RNF115 association
  with Toll-like receptors and localization to the ER and Golgi
  [PMID:35343654 "RNF115 is phosphorylated by AKT1 and subsequently associates with the 14‐3‐3 chaperones that facilitate RNF115 associating with TLRs and localizing on the ER and the Golgi apparatus."].
- The RNF115 paper supports the GO-CAM activity qualitatively, but it does not single out
  YWHAE as the only acting paralog: the paper recovered theta, eta, zeta, epsilon, gamma
  and beta 14-3-3 proteins as RNF115 interactors. The model would be more precise as a
  14-3-3 entity set or a family-scoped activity.

## Ion-channel, pump, and other client-specific outputs

- YWHAE/HERG binding prolongs cAMP/PKA effects on the HERG/KCNH2 potassium channel
  [PMID:11953308 "We show that HERG associates with 14-3-3epsilon to potentiate cAMP/PKA effects upon HERG."]. This supports potassium-channel regulation and membrane-repolarization rows,
  but not organism-scale heart-rate regulation rows.
- PMCA1/ATP2B1 and PMCA3/ATP2B3 are plasma-membrane Ca2+-transporting ATPases, not
  calcium channels. 14-3-3 epsilon binds and inhibits both pumps
  [PMID:18029012 "The effect of the interaction on the activity of the two pumps, and thus on the homeostasis of Ca(2+), was investigated by co-expressing the 14-3-3epsilon protein and PMCA3 or PMCA1 in CHO cells"].
  The existing `calcium channel` molecular-function rows should therefore be replaced by
  `ATPase inhibitor activity`.
- 14-3-3 epsilon binds HDAC4 and HDAC5 at phosphorylation sites and holds these class II
  histone deacetylases in the cytoplasm
  [PMID:10869435 "Both HDACs were found to interact with14-3-3 proteins at three phosphorylation sites."].
- KSR, CDC25 phosphatases, ZNRF1/ZNRF2, Parkin, and many other proteins are reported as
  client or candidate client interactors. The specific, mechanistic subset fit
  non-core binding or regulatory rows; high-throughput protein-binding rows remain too
  generic to carry as GO:0005515.

## Screen-only rows

- Several rows were seeded from broad proteomic screens: mRNA-interactome capture
  [PMID:22658674 "Employing two complementary protocols for covalent UV crosslinking of RBPs to RNA, we describe a systematic, unbiased, and comprehensive approach, termed \"interactome capture,\" to define the mRNA interactome of proliferating human HeLa cells."],
  focal adhesion proteomics, E-cadherin proximity proteomics, exosome proteomes, and a
  disease substantia nigra proteome
  [PMID:22926577 "Using a quantitative proteomic approach, we investigated protein expressions in the substantia nigra of Alzheimer's disease, Huntington's disease, and Multiple sclerosis."].
- These screens establish candidate physical recovery or localization in a fraction, not
  YWHAE-specific execution of RNA binding, cadherin binding, MHC-II binding, focal
  adhesion function, extracellular exosome function, or substantia nigra development.
