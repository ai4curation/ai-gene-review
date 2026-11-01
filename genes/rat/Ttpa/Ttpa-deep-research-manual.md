# Ttpa (rat alpha-tocopherol transfer protein, P41034) - manual literature research

No deep-research API was available; this summary was compiled by hand from cached
publications (`publications/PMID_*.md`), PubMed searches and the UniProt record.

## Identity and family
- Rat Ttpa (UniProt P41034, RGD:3915, GeneID 25571), 278 aa, a Sec14/CRAL-TRIO lipid-binding
  protein (Pfam PF00650 CRAL_TRIO, PF03765 CRAL_TRIO_N; PANTHER PTHR10174:SF225).
- Cloned from rat liver: "alpha TTP present in rat liver cytosol specifically binds this vitamin
  and enhances its transfer between separate membranes" and "exhibit a structural homology with
  the cellular retinaldehyde-binding protein" [PMID:8349655].

## Molecular function
- Tocopherol binding: a 32-kDa alpha-tocopherol-binding protein purified from rat liver cytosol;
  "D-alpha-[3H]tocopherol was displaced from homogeneous TBP in the presence of 500-fold excess of
  nonlabeled alpha-tocopherol, indicating the specificity of the binding" [PMID:1569384].
- Ligand selectivity measured by intermembrane transfer competition: "RRR-alpha-tocopherol = 100%
  ... gamma-tocopherol, 9% ... alpha-tocotrienol, 12%" [PMID:9199513]. Binding and transfer are
  stereo- and form-selective for RRR-alpha-tocopherol.
- Phosphoinositide-gated release (human alpha-TTP): "wild-type α-TTP bound phosphatidylinositol
  phosphates (PIPs), whereas the arginine mutants did not" and "PIPs in the target membrane promoted
  the intermembrane transfer of α-tocopherol by α-TTP" with PIP binding causing "the lid of the
  α-tocopherol-binding pocket to open" [PMID:23599266]. UniProt transfers PI(3,4)P2 and PI(4,5)P2
  binding residues to rat by similarity to mouse Q8BWP5.
- Review: "In hepatocytes, α-TTP catalyzes the vectorial transport of α-Toc from the endocytotic
  compartment to the plasma membrane (PM) by targeting phosphatidylinositol phosphates (PIPs) such
  as PI(4,5)P2" [PMID:34563650].

## Location
- Cytosolic in hepatocytes [PMID:1569384, PMID:8349655]. Under chloroquine, "alpha-TTP accumulates
  transiently on the cytoplasmic surface of late endosomal membranes", an activity requiring
  residues 21-50 [PMID:14531858].

## Expression
- Liver-restricted in rat by Western/Northern [PMID:8349655]; also reported in brain, pregnant
  uterus and retina (cited in PMID:22147702). Hepatic protein (not mRNA) falls with dietary vitamin
  E deficiency; both fall with low protein diet [PMID:9868180].

## Chloroquine protection (PMID:22147702, full text read)
- alpha-TTP expression in McARH7777 hepatoma cells prevented CQ-induced vacuolation, caspase-3
  activation and death; Ttpa KO mice had greater CQ hepatotoxicity and retinopathy, not rescued by
  vitamin E.
- Mechanism: "α-TTP prevents CQ accumulation in acidic organelles, thus preserving their low pH";
  required NPC1 and the N-terminal translocation segment. alpha-TTP did not acidify organelles
  itself: "the expression of α-TTP did not affect the pH in the acidic organelles".
- Hence the RGD IDA "intracellular pH reduction" reads the result in the wrong direction; the
  apoptosis row is a downstream protective effect.

## Physiology (from orthologs)
- Human TTPA mutations cause ataxia with vitamin E deficiency; mouse KO has very low plasma
  alpha-tocopherol and vitamin E-dependent reproductive (placental) failure (summarised in
  PMID:22147702 and PMID:34563650). These are consequences of systemic vitamin E deficiency.
