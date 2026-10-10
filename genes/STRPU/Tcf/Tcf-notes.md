# Tcf (SpTcf/Lef, Q9Y0B2) — curation notes

## Identity

- UniProt Q9Y0B2, "HMG protein Tcf/Lef" (EMBL AAD45010.1), cloned by Huang et al. 2000 from
  Strongylocentrotus purpuratus as SpTcf/Lef. The record's single RX reference is PMID:10664150.
  Domains: N-terminal beta-catenin-binding region (InterPro IPR013558, Pfam PF08347), HMG box
  (IPR009071, residues 316-384), TCF/LEF family signature (IPR024940). PANTHER PTHR10373:SF38.
- The community GRN name is simply `Tcf` (also `Tcf1` in Minokawa et al. 2005). It is the only
  Tcf/Lef-family gene in the sea urchin, so the accession and the GRN node are the same gene.

## What the gene does

SpTcf/Lef is the HMG-box transcription factor that transduces the maternal beta-catenin signal
into transcription in the vegetal half of the embryo. Its expression peaks when beta-catenin
nuclearizes in vegetal blastomeres, and a dominant-negative form phenocopies the loss of
nuclear beta-catenin [PMID:10664150 "Expression of SpTcf/Lef was maximal when beta-catenin
became localized to nuclei of vegetal blastomeres, consistent with its acting in combination
with beta-catenin to specify vegetal cell fates. Expression of a dominant-negative SpTcf/Lef
inhibited primary and secondary mesenchyma, endoderm, and aboral ectoderm formation in a manner
similar to that observed when nuclear accumulation of beta-catenin was prevented."].

Nuclear beta-catenin itself is required for all vegetal fates [PMID:9847248 "the accumulation
of beta-catenin in nuclei of vegetal cells is regulated cell autonomously and that this
localization is required for the establishment of all vegetal cell fates and the production of
micromere-derived signals"], and Tcf is its nuclear effector: dominant-negative TCF animalizes,
activated TCF vegetalizes, and all of beta-catenin's axial activity runs through TCF
[PMID:10625549 "We show that expression of a dominant negative TCF results in a classic
"animalized" embryo. In contrast, microinjected RNA encoding an activated TCF produces a highly
"vegetalized" embryo."; "We also provide evidence indicating that all of beta-catenin's activity
in patterning the sea urchin AV axis is mediated by TCF."]. The Vonica et al. abstract does not
state which sea urchin species was used; treat as corroborating, not S. purpuratus-specific.

### The activator/repressor switch

In the animal half, where beta-catenin is not nuclear, Tcf bound by the co-repressor Groucho
silences the endomesoderm regulatory genes; nuclear beta-catenin competes Groucho off Tcf and
converts it to an activator. This was shown in Lytechinus variegatus [PMID:15708573 "Interaction
assays demonstrate that LvGroucho interacts with Tcf via both the Q and the WD domains of the
protein. LvGroucho interacts with Tcf to antagonize the expression of key endomesoderm regulatory
genes."; "LvGroucho functionally competes with beta-catenin for Tcf binding, and this competitive
mechanism regulates one of the earliest steps in the initiation of the sea urchin endomesoderm
GRN"]. In S. purpuratus the same dual behaviour is written into the wnt8 cis-regulatory system:
Tcf sites are needed for endomesodermal activation, and in a second module they repress ectopic
expression in the prospective ectoderm [PMID:16289024 "The Tcf1/beta-catenin and Blimp1/Krox
inputs are both necessary for normal endomesodermal expression mediated by this cis-regulatory
module"; "In a second regulatory region, which initiates expression in micromere and macromere
descendant cells early in cleavage, Tcf1 sites act to repress ectopic transcription in
prospective ectoderm cells."]. Peter & Davidson formalize this as the Tcf 'X, 1-X' processor and
show the same Tcf sites later extinguish the endoderm GRN in mesoderm precursors
[PMID:21623371 "the same Tcf sites that are used to initiate the endoderm GRN in the veg2
lineage are used again to extinguish it in mesoderm precursors"; "A possible explanation is that
in cells receiving Notch signalling, the availability of nuclear β-catenin is reduced, leading to
Tcf/Groucho-mediated repression."].

### Place in the endomesoderm GRN

- Micromere / skeletogenic lineage: beta-catenin/Tcf plus Otx activate pmar1, the top of the
  double-negative gate [PMID:18413610 "The pmar1 genes are activated by the β-catenin/Tcf
  transcription complex plus Otx, i.e., by two of the micromere-specific inputs just enumerated
  ( 25 , 30 )."; "Dsh regionally prevents the degradation of cytoplasmic β-catenin ( 27 ), which
  transits to the nucleus, forming an active complex with the Tcf transcription factor."].
- Wnt8 community-effect loop: wnt8 needs beta-catenin/Tcf and Blimp1 inputs, so Tcf both
  receives and drives the Wnt8 signal [PMID:18413610 "the inputs required for its expression in
  the micromere lineage are Blimp1 and β-catenin/Tcf"; PMID:19104065 "the wnt8 gene requires
  inputs from both β-catenin/Tcf (i.e., from the same signal transduction system that it
  activates) and from Blimp1 factor for expression"].
- veg2 endoderm: most of the eight early endoderm regulatory genes are under cis-regulatory Tcf
  control [PMID:21623371 "the cis-regulatory Tcf responsiveness of early endodermal genes results
  first in the activation of an endodermal GRN and then, together with cleavage geometry, in the
  spatial separation of endodermal and mesodermal regulatory states and hence of biological
  fates"].
- Timing / shutdown in mesoderm: Tcf activity is required early but must be turned off in the
  mesodermal lineage by Notch-induced NLK (shown in Paracentrotus lividus) [PMID:17038519
  "activating the expression of a TCF-VP16 construct at blastula stages strongly inhibits
  endoderm and mesoderm formation, indicating that while TCF activity is required early for
  launching the endomesoderm gene regulatory network, it has to be downregulated at blastula
  stage in the mesodermal lineage"].

## Curation decisions

- GOA has three electronic rows (DNA binding, nucleus, Wnt signaling pathway). All are
  consistent with the literature. DNA binding and nucleus are accepted; the generic Wnt term is
  narrowed to canonical (beta-catenin-dependent) Wnt signaling, since Tcf is the transcriptional
  endpoint of that branch.
- NEW: activator activity (GO:0001228, IMP, Huang 2000) and repressor activity (GO:0001227,
  IDA, Minokawa 2005) - both signs are demonstrated and both are the biology of the switch.
  Canonical Wnt signaling pathway (GO:0060070, IMP). Endodermal (GO:0001714) and mesodermal
  (GO:0007501) cell fate specification (IMP): Tcf itself performs the transcriptional step that
  turns on pmar1, wnt8, blimp1 and the veg2 endoderm genes, so it passes the participation test;
  its vertebrate orthologues carry the equivalent germ-layer terms.
- Not proposed: beta-catenin binding and Groucho binding. Direct binding has been assayed only
  for the Lytechinus protein (Groucho) or inferred from LiCl/dominant-negative behaviour; no
  S. purpuratus binding assay is cached. Recorded as a knowledge gap.
- gocams/index.tsv has no S. purpuratus Tcf model.
