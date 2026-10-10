# PBS2 (YJL128C, UniProt P08018) curation notes

## Identity

- MAP kinase kinase of the HOG (high-osmolarity glycerol) pathway; aliases HOG4, SFS4, SSK4.
  UniProt: "Belongs to the protein kinase superfamily. STE Ser/Thr" (MAP kinase kinase subfamily);
  668 aa, C-terminal kinase domain (360-623), long disordered N-terminal region (PBS2_N, PF31257).
- PANTHER PTHR48013:SF25 "MAP KINASE KINASE PBS2".

## Core catalytic function: MAPKK for Hog1

- [PMID:7681220 "Two of these genes, HOG1 and PBS2, encode members of the mitogen-activated protein
  kinase (MAP kinase) and MAP kinase kinase gene families, respectively."]
- [PMID:7681220 "A rapid, PBS2-dependent tyrosine phosphorylation of HOG1 protein occurred in response
  to increases in extracellular osmolarity."]
- UniProt FUNCTION: activates HOG1 by concomitant phosphorylation of Thr-174 and Tyr-176
  (PubMed:38270553, 7681220); Rhea Thr and Tyr reactions carry experimental evidence
  (PubMed:38270553); the Ser reaction (RHEA:17989) carries no experimental evidence tag.
- [PMID:38270553 "The activity of Hog1p was specifically enhanced at these proline-adjacent sites on
  Dot1p upon Hog1p activation by the osmostress-responsive MAP kinase kinase PBS2 (Pbs2p)."]
  -> Pbs2 used as in vitro activator of Hog1 (basis for EXP tyrosine kinase activity row).

## Upstream activation - convergence of two branches

- [PMID:7624781 "Pbs2p was activated by two independent signals that emanated from distinct
  cell-surface osmosensors."]
- SLN1 branch: [PMID:7624781 "Pbs2p was activated by MAP kinase kinase kinases (MAPKKKs) Ssk2p and
  Ssk22p that are under the control of the SLN1-SSK1 two-component osmosensor."]
- SHO1 branch: [PMID:7624781 "Alternatively, Pbs2p was activated by a mechanism that involves the
  binding of its amino terminal proline-rich motif to the Src homology 3 (SH3) domain of a putative
  transmembrane osmosensor Sho1p."]
- [PMID:9180081 "A second osmosensor, Sho1p, also activated Pbs2p and Hog1p, but did so through the
  Ste11p MAPKKK."]
- Deep research (falcon; Tatebayashi 2020/2023, not cached): Ste11 phosphorylates Pbs2 mainly at
  Thr518, Ssk2/Ssk22 at Ser514+Thr518; Hog1 feeds back on Pbs2 Ser248 (Mosbacher 2023).
  PP2Cs Ptc1-4 dephosphorylate Pbs2; [file deep-research "Nbp2 recruits Ptc1 to Pbs2, providing
  interaction specificity for dephosphorylation."]

## Scaffold function

- [PMID:9180081 "The MAPKK Pbs2p bound to the Sho1p osmosensor, the MAPKKK Ste11p, and the MAPK
  Hog1p. Thus, Pbs2p may serve as a scaffold protein."]
- [PMID:15200959 "In the yeast high osmolarity response pathway, the MAP kinase kinase Pbs2 is thought
  to function as a scaffold, since it binds the osmosensor Sho1, the upstream MAP kinase kinase kinase
  Ste11, and the downstream MAP kinase Hog1."] and Sho1 and Pbs2 are co-scaffolds:
  [PMID:15200959 "Thus, a network of interactions provided by both Sho1 and Pbs2 appears to direct
  pathway information flow."]
- Pbs2 Pro-rich motif (PLPPLP, res 94-99) is the high-specificity ligand of the Sho1 SH3 domain:
  [PMID:14668868 "Here we show that an isolated peptide ligand from the yeast protein Pbs2 recognizes
  its biological partner, the SH3 domain from Sho1, with near-absolute specificity"]
- Affinity of Sho1 SH3 for Pbs2 tunes HOG output [PMID:15200958 "We demonstrate a strong linear
  correlation between the binding energy of these mutants and quantitative in vivo outputs from the
  HOG high-osmolarity response pathway controlled by Sho1p."]
- Pbs2 also binds the SH3 of the negative regulator Nbp2 via a distinct Pro-rich motif:
  [PMID:14685261 "In addition, the Pbs2 scaffold bound the Nbp2 SH3 via a Pro-rich motif distinct
  from that which binds the SH3 domain of the positive regulator Sho1."]
- Conclusion: GO:0005078 MAP kinase scaffold activity is supported by cached evidence (SGD IPI
  annotations with Sho1, Ste11, Hog1). Partner-specific MF for the IntAct/SGD protein-binding rows:
  GO:0017124 SH3 domain binding (Sho1 SH3, Nbp2 SH3).

## Localization

- [PMID:9755161 "we found that HOG1, PBS2 and STE11 localize to the cytoplasm of unstressed cells.
  Following osmotic stress, HOG1, but neither PBS2 nor STE11, translocates into the nucleus."]
- [PMID:10980703 "Pbs2 tagged with green fluorescent protein (Pbs2-GFP) is evenly distributed in the
  cytoplasm but excluded from the nucleus before and after exposure to stress."]
- Transient polarized (bud tip/bud neck) pool only resolved with a kinase-dead trap:
  [PMID:10980703 "Here we show that a catalytically inactive form of Pbs2 attains a highly polarised
  localization during osmostress."]

## Peripheral / downstream phenotypes

- Actin repolarization after osmotic shock needs the HOG pathway [PMID:7941729 "Thus, the HOG pathway
  is required for repositioning of the actin cytoskeleton and the normal spatial patterns of cell
  growth after recovery from osmotic stress."] -> downstream, non-core.
- Hog1 nuclear import: Hog1 phosphorylation is sufficient [PMID:9755161 "HOG1 phosphorylation is
  necessary and sufficient for nuclear translocation"]; Pbs2 C-terminal chimera study (PMID:15707964)
  therefore reflects Hog1 activation, Pbs2 is not part of the import machinery -> over-annotation.
- Macroautophagy (2025): [PMID:40524543 "Furthermore, the influence of Pbs2 on macroautophagy was shown
  to be independent of Hog1, a well-known downstream factor of Pbs2."] Late-stage defect; mechanism
  unknown -> non-core, acts upstream.
- Stress granule core proteomics (PMID:26777405, HDA): single HT dataset, no follow-up.

## Problematic annotations: NatB (PMID:12783868)

- UniProt-assigned (2006/2013) rows on P08018: GO:0004596 N-terminal acetyltransferase (IMP),
  GO:0031416 NatB complex (IDA), protein binding with MDM20 (IPI).
- The abstract explicitly defines the complex: [PMID:12783868 "NatB is composed of the interacting
  Nat3p and Mdm20p subunits, both of which are required for acetyltransferase activity."]
- Pbs2 has no GNAT/acetyltransferase domain (InterPro: kinase domain only). UniProt's own P08018
  SUBUNIT line ("Interacts with NBP2, PTC1, SHO1 and STE11.") does not mention NatB, and SGD's live
  curated PBS2 GO set (checked via SGD API 2026-09-24) does not contain any of these rows, whereas SGD
  annotates NAT3 (Q06504) to NatB from this same paper. Strongly suggests the rows were entered on
  the wrong accession (NAT3 intended). Removed; flagged as a question for UniProt.

## GO-CAM / module context

- modules/scer_hog1_cascade.yaml uses GO:0004708 MAP kinase kinase activity for Pbs2.
