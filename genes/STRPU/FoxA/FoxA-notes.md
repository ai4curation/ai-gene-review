# FoxA (Sp-FoxA, Q1PA44) — curation notes

## Identity
- UniProt Q1PA44 (unreviewed), 440 aa, "Forkhead transcription factor A", gene name FoxA
  (EMBL ABE68834.1). The RX citation is the sea urchin Forkhead family survey
  [PMID:17081512 "This genome includes 22 fox genes, only three of which"].
  Domains (UniProt DR): Fork_head domain IPR001766 (Pfam PF00250), Forkhead N-terminal
  IPR013638 (PF08430), HNF_C IPR018533 (PF09354) — the FoxA/HNF3-type C-terminal region.
  PANTHER PTHR11829 (FORKHEAD BOX PROTEIN), subfamily SF380. The literature gene is
  Sp-foxa of the Davidson endomesoderm GRN; the same forkhead-A orthologue is the one
  studied by Oliveri et al. 2006 and de-Leon & Davidson 2010. No identity doubt: the
  GRN literature refers to a single foxa gene in S. purpuratus.
- No GO-CAM contains this gene (`gocams/index.tsv` has no STRPU rows).

## Place in the GRN
- Endoderm regulatory gene of the veg2 lineage
  [PMID:17038513 "The foxa gene is an integral component of the endoderm specification subcircuit"].
- Timing/space: [PMID:20479235 "Transcriptional expression of the foxa gene starts at about 11 h
  postfertilization (hpf). At 15 hpf foxa is expressed in all of the descendants of the veg2 ring
  of cells and is absent from the skeletogenic mesoderm lineage (SM), from veg1 and from the
  ectoderm"]; cleared from NSM at 18–20 hpf; later also in the oral ectoderm patch where the
  mouth forms.
- At the endoderm/mesoderm split, the outer veg2 ring keeps foxa and loses gcm
  [PMID:21623371 "whereas the peripheral cells of the veg2 lineage (the presumptive endoderm)
  express foxa alone (Fig. 2a)"]. Notch perturbation prevents clearance from the mesoderm domain
  [PMID:21623371 "In embryos with perturbed expression of either Delta or Notch, the endodermal
  regulatory genes foxa, blimp1b and dachshund (dac) continue to be expressed in the presumptive
  mesodermal domain at 24 h"].

## Inputs (cis-regulatory analysis, de-Leon & Davidson 2010)
- Four CRMs (F, I, J, K) [PMID:20479235 "Four separate cis -regulatory modules (CRMs) cooperate
  to control foxa expression in different spatial domains of the endomesoderm, and at different
  times."].
- Spatial control is a Tcf toggle switch in module F: [PMID:20479235 "Taken together, these
  results indicate that Tcf is the input responsible for keeping the foxa gene off outside of the
  endoderm, at least in embryos <22 hpf, and that this regulatory transaction is mediated by the
  genomic Tcf site in module F."]; see also [PMID:19895806 "Mutation of Tcf binding sites in the
  cis-regulatory regions of hox11/13b, foxA and brachyury, and eve results in dramatic ectopic
  expression of reporter constructs in all or most domains of the embryo."].
- Activating inputs: Su(H) (early boost, module J), Hox11/13b (module K), Otx (modules K and J),
  Brachyury (module I) [PMID:19895806 "The regulation of foxA and brachyury is fairly similar at
  these early stages. Both genes appear to be expressed under the control of Tcf, Hox11/13b and
  Otx, as mentioned above, and are also ultimately affected by GataE."].
- Autorepression through a single FoxA site in module I: [PMID:20479235 "A mutation of a single
  putative FoxA site in module I increased the level of the FIJ:GFP reporter transcript at 20–24
  hpf ( Fig. 3 I ). This result verifies that FoxA is an autorepressor that reduces, but does not
  eliminate, its gene product level."]; [PMID:20479235 "At 24 hpf the injection of Foxa MO
  increased the level of the construct FIJ:GFP by 2-fold, similar to the increase of the level of
  the endogenous foxa gene in the same injections."]. Abstract-level statement in
  [PMID:17038513 "pregastrular regulatory system of foxa, and Foxa represses its own"].

## Outputs / functions (Oliveri et al. 2006; de-Leon 2011 review)
- Three functions: repression of mesodermal fate in veg2 endomesoderm, gut gene expression after
  gastrulation, stomodaeum formation [PMID:17038513 "mesodermal fate in the veg2 endomesoderm; it
  is required in postgastrular"]. MASO phenotype: [PMID:17038513 "endomesoderm cells become
  pigment and other mesenchymal cell types, less gut is"] ... no mouth.
- Direct-ish repressive step on gcm: [PMID:17038513 "the normal endoderm, a crucial role of Foxa is
  to repress gcm expression in response"] [PMID:17038513 "to a Notch signal, and hence to repress
  mesodermal fate."]; summarized as [PMID:21130759 "The suppression of mesodermal fate in the
  endoderm is mediated, at least in part, by Foxa repression of the gene that encodes the
  transcription factor GCM (Oliveri et al., 2006), a key regulator of mesodermal fate in the sea
  urchin embryo (Ransick and Davidson, 2006)."].
- Other known targets: [PMID:21130759 "Foxa has two other known targets, it activates the
  transcription of the gene that encodes the ligand, Hedgehog, and it represses its own gene
  expression (Oliveri et al., 2006)."].
- Foregut endoderm specification: [PMID:20479235 "For these endoderm cells, foxa later provides
  canonical regulatory functions that are essential to specification of the foregut endoderm ( 7 )."].
- Gut morphogenesis: [PMID:21130759 "When foxa is downregulated by the injection of morpholino
  antisense oligonucleotides these processes do not occur, and there is a failure of gut formation
  (Oliveri et al., 2006)."]. Boundary maintenance: [PMID:20479235 "In Xenopus ( 6 ) and the sea
  urchin ( 1 ) a major function of the foxa gene during embryonic development is maintenance of the
  endoderm–mesoderm boundary, by repression of mesoderm fate in the endoderm."].

## Curation decisions
- IBA rows (GO:0000978, GO:0000981, GO:0005634, GO:0006357): ACCEPT — Fox forkhead DNA binding is
  family-wide and the sea urchin gene is a documented sequence-specific regulator (autorepression
  via a FoxA site).
- IBA GO:0030154 cell differentiation -> MODIFY to GO:0001714 endodermal cell fate specification.
- IBA GO:0009653 anatomical structure morphogenesis -> MODIFY to GO:0048546 digestive tract
  morphogenesis (gut/mouth failure on knockdown).
- IEA GO:0003677 -> MODIFY to GO:0000978; IEA GO:0003700 -> MODIFY to GO:0000981; IEA GO:0006355
  -> MODIFY to GO:0000122 (documented direction is repression); IEA GO:0043565 ACCEPT;
  IEA GO:0019904 protein domain specific binding (InterPro Fork-head_N) MARK_AS_OVER_ANNOTATED.
- NEW: GO:0001227 (IDA, site mutagenesis), GO:0000122 (IMP/IDA), GO:0001714 (IMP),
  GO:0042662 negative regulation of mesodermal cell fate specification (IMP).
  Comparator check via QuickGO: GO:0001714 is carried by endoderm-specifying TFs (worm end-1,
  med-1/2, zebrafish foxh1, Eomes); GO:0042662 by TFs such as Mesp1 and klf2a/b — so both are
  conventional for a TF that itself performs the regulatory step.
- Not proposed: activator activity (hh activation is reported only second-hand in a review, and the
  post-gastrular gut-gene requirement is necessity evidence), stomodeum/mouth terms (pleiotropic,
  ectodermal role), Hedgehog signalling terms.
