# GUCY2C notes

Deep research (`just deep-research-falcon human GUCY2C --fallback perplexity-lite`) failed in
this environment (falcon/perplexity providers unavailable). Research below is from the
UniProt record (P25092), cached publications, and PubMed searches.

## Identity and topology
- Receptor guanylyl cyclase C (GC-C, STaR), type I single-pass membrane protein: signal peptide
  1-23, extracellular ligand-binding domain 24-430, TM 431-454, cytoplasmic kinase-homology
  domain (KHD, 489-749) and guanylyl cyclase catalytic domain (824-954) (UniProt features).
- [PMID:1680854 "The receptor contains both an extracellular ligand binding site and a cytoplasmic guanylyl cyclase catalytic domain"]
- Stable cell lines "specifically bind 125I-STa (Kd approximately 1.0 nM) and respond to STa by dramatically increasing (approximately 50-fold) cellular cGMP levels" [PMID:1680854].

## Localization (cell-surface benchmark)
- Plasma membrane, extracellular domain exposed; apical/brush-border membrane of intestinal
  epithelium. STa acts "by binding to the brush border membrane of the small intestine" [PMID:1680854].
- [PMID:11950846 "The GCC-IKEPP interaction is not required for the efficient targeting of GCC to the apical cell surface."]
- Two glycoforms: 130 kDa high-mannose ER-resident precursor and 145 kDa plasma-membrane form;
  [PMID:23269669 "differentially glycosylated forms that are resident in the endoplasmic reticulum (130 kDa) and the plasma membrane (145 kDa) bind the ST peptide with equal affinity"]. ER pool is a biosynthetic precursor; the functional site is the PM.
- Glycosylation needed for surface localization and ST binding; interacts with lectin chaperone VIP36 (LMAN2) [PMID:23269669].

## Function
- Ligands: guanylin (GUCA2A), uroguanylin (GUCA2B), E. coli STa (Reactome R-HSA-8936214, R-HSA-8936356).
- cGMP produced activates PKGII/CFTR, driving Cl-/water secretion [PMID:11950846; PMID:22521417 "the encoded protein activates the CFTR protein through local generation of cGMP"].
- KHD is a pseudokinase: binds ATP (Lys516) which modulates cyclase activity, no kinase activity
  [PMID:16460035 "The KHD lacks many of the amino acids required for phosphotransfer activity and, therefore, is not expected to possess kinase activity."; "we demonstrate that the intracellular domain of GC-C and the KHD bind ATP"]; [PMID:11478887].
- PDZ protein NHERF4/IKEPP binds the C-terminus and inhibits ST-activated cyclase [PMID:11950846].

## Disease
- Activating mutation -> dominant familial diarrhea (DIAR6) [PMID:22436048].
- Loss-of-function homozygous mutations -> meconium ileus [PMID:22521417].
