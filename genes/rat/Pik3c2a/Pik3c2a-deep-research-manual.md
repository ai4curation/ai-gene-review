# Pik3c2a (rat, D3ZTF6) - manual literature synthesis

No deep-research API was available for this review. This file records a manual
literature survey done with PubMed searches and the cached publications in
`publications/`. Quotes are verbatim from the cached files.

## Identity

- Rat Pik3c2a, UniProtKB D3ZTF6 (TrEMBL, unreviewed, 1687 aa), RGD:1310389,
  GeneID 361632. PE level 3 (inferred from homology). Ortholog of human
  PIK3C2A (O00443) and mouse Pik3c2a (Q61194, MGI:1203729).
- Domain architecture (InterPro/Pfam in the UniProt record): Ras-binding domain
  (PF00794), C2 (PI3K-type, PF00792), PI3K helical/accessory (PF00613),
  PI3/PI4 kinase catalytic domain (PF00454), PX domain (PF00787) and C-terminal
  C2 domain (PF00168); InterPro IPR037705 "PI3-kinase_C2-alpha_cat" and
  IPR042133 "PX_PI3K_C2_alpha". The catalytic loop (DRHNDN, residue 1251) and
  DFG motif (residue 1269) are present in the rat sequence; the C2-domain
  nuclear localisation stretch KRKTKISRKTR mapped in the human protein
  (PMID:11606566) is conserved at residue 1610.

## Catalytic activity and lipid products

- Human PI3K-C2alpha cloning: [PMID:9337861 "the enzyme only phosphorylates
  PtdIns and PtdIns4P when the lipids are presented alone. However, when lipids
  were presented together with phosphatidylserine acting as a carrier,
  phosphorylation of PtdIns(4,5)P2 was also observed."] and it is refractory
  to wortmannin/LY294002.
- In vivo product during insulin signalling is PI3P: [PMID:17644513 "we here
  identify phosphatidylinositol 3-phosphate as the sole in vivo product of the
  insulin-dependent activation of PI3K-C2alpha"].
- At clathrin-coated pits it generates PI(3,4)P2: [PMID:23823722 "formation of
  phosphatidylinositol-3,4-bisphosphate (PI(3,4)P2) by class II
  phosphatidylinositol-3-kinase C2α (PI(3)K C2α) spatiotemporally controls
  clathrin-mediated endocytosis"].
- Clathrin binds the N-terminus and activates the kinase: [PMID:11239472
  "clathrin functions as an adaptor for the class II PI 3-kinase C2alpha
  (PI3K-C2alpha), binding to its N-terminal region and stimulating its
  catalytic activity, especially toward phosphorylated inositide substrates"].
  The clathrin-binding domain alone drives lattice assembly [PMID:16215232].
- The PX domain binds PI(4,5)P2 and mediates membrane recruitment
  [PMID:17038310 "This PX domain contains a signature PI-binding site that is
  optimized for PtdIns(4,5)P(2) binding."].

## Localisation

- Rat brain clathrin-coated vesicles [PMID:10766823 "Centrifugation of rat
  brain homogenates and Western blotting revealed that in contrast to the class
  IA PI3K enzymes, PI3K-C2alpha could be co-purified with a population of
  clathrin-coated vesicles (CCVs)."]; perinuclear TGN staining with
  gamma-adaptin and TGN-46 in the same paper.
- Coated pits at the plasma membrane [PMID:11239472 "endogenous PI3K-C2alpha is
  localized in coated pits"].
- Nucleus/nuclear speckles in HeLa cells [PMID:11606566].
- Pericentriolar recycling endosome at the cilium base [PMID:24697898
  "PI3K-C2α is enriched in the pericentriolar recycling endocytic compartment
  (PRE) at the base of the primary cilium, where it regulates production of a
  specific pool of PtdIns3P."].
- Mature secretory granules in PC12 (rat) cells [PMID:16055506 "In
  neuroendocrine cells, PI3K-C2alpha is present on a subpopulation of mature
  secretory granules."].

## Rat-specific experimental evidence

- PC12 (rat pheochromocytoma) cells: [PMID:16055506 "Overexpression of
  wild-type PI3K-C2alpha enhanced secretion, whereas transfection of PC12 cells
  with a catalytically inactive PI3K-C2alpha mutant or a 2xFYVE domain
  sequestering PtdIns3P abolished secretion."] (abstract only in cache).
- INS1 rat insulinoma cells (key paper, full text read): [PMID:21127054 "Here
  we report that selective down-regulation of this PI3K isoform in INS1 rat
  insulinoma cells specifically impairs insulin secretion irrespective of the
  metabolic effect, without affecting insulin content or the number of insulin
  granules associated with the plasma membrane in resting cells."]. Calcium
  influx was unaffected, KCl-evoked secretion did not need insulin receptor or
  Akt, and SNAP25 proteolysis was reduced, placing the defect at granule
  fusion. Both stable shRNA and transient siRNA lines were used. This is
  knockdown (phenotype) evidence; the mechanistic inference is that
  PI3K-C2alpha-derived PtdIns3P is needed for fusion competence, as in PC12
  cells.
- Rat brain CCV fractionation (PMID:10766823, above).

## Endocytosis and trafficking

- Clathrin-mediated endocytosis: depletion impairs late-stage coated-pit
  maturation and SNX9 recruitment [PMID:23823722].
- Dynamin-independent uptake [PMID:21081650 "downregulation of PI3KC2α
  impaired internalization of CD59 as well as fluid-phase endocytosis"].
- Endothelial endosomal trafficking and VE-cadherin delivery; the global and
  endothelial knockout is embryonic lethal with angiogenesis defects
  [PMID:22983395].
- Rab11 activation and ciliogenesis [PMID:24697898]; human loss-of-function
  causes a syndromic ciliopathy-like disorder [PMID:31034465].

## Autophagy

- Mouse MEFs, combined class II alpha+beta siRNA: [PMID:24098492 "Our studies
  indicate that while Vps34 is the main PI3P source during autophagy, class II
  PI3Ks also significantly contribute to PI3P generation and regulate AP
  biogenesis."]
- Human U2OS cells: [PMID:28910396 "This defective autophagy is rescued by
  exogenous PI3K-C2α, but not kinase-dead PI3K-C2α."]
- Kidney epithelia, shear stress: [PMID:32102612 "We showed that PtdIns3P is
  generated by PIK3C2A, but not by PIK3C3/VPS34, during flow-associated primary
  cilium-dependent autophagy, in a ULK1-independent manner."]

## Signalling

- Insulin: recruitment to the plasma membrane via TC10, contributes to GLUT4
  translocation (PMID:17644513). In beta cells, knockdown reroutes IR-B
  signalling from PKB to ERK (PMID:26387957). In INS1 cells KCl-evoked
  secretion is Akt-independent (PMID:21127054).
- Class II PI3K-C2alpha makes PI3P and PI(3,4)P2 rather than PIP3, so the
  class I PI3K/PKB axis is not its core output.

## Other

- Podocyte/glomerular maintenance in knockout mice (PMID:20974805).
- Mitotic spindle scaffolding function independent of kinase activity
  (PMID:29017056, abstract only, not used for annotation).
- miR-206 targets PIK3C2A in endothelial progenitor cells (PMID:26175229).
