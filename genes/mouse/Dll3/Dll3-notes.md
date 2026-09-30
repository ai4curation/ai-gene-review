# Dll3 (mouse) review notes

UniProt O88516 (DLL3_MOUSE), Delta-like protein 3, 592 aa, type I membrane protein.
PANTHER PTHR24044 (NOTCH LIGAND FAMILY MEMBER), subfamily PTHR24044:SF420. MGI:1096877.
Notch-module role: **divergent DSL ligand acting as a cell-autonomous (cis) inhibitor of Notch**;
does not activate Notch in trans.

## Divergent structure
- Most divergent Delta homologue [PMID:9272948 "Dll3 is the most divergent Delta homologue identified to date."]
  UniProt/InterPro: Notch_ligand_N (MNNL) domain and EGF repeats; its DSL domain is degenerate
  (InterPro lists no DSL domain IPR001774 for Dll3, unlike Dll1). Lacks the intracellular
  PDZ-binding/ubiquitination motif architecture of Dll1 (not independently verified here).

## Does not activate Notch; cis-inhibitor
- [PMID:16144902 "In contrast to other DSL ligands, we show that Dll3 does not activate N signaling in multiple assays."]
- [PMID:16144902 "Dll3 does not bind to cells expressing any of the four N receptors, and N1 does not bind Dll3-expressing cells."]
- [PMID:16144902 "Although Dll3 did not bind or activate N when presented in trans, it cell autonomously inhibited N signaling that was induced by other DSL ligands in CSL gene reporter, Xenopus laevis primary neurogenesis, and mouse embryonic neural progenitor differentiation assays."]
- As a Notch antagonist, Dll3 promoted Xenopus neurogenesis and inhibited glial differentiation of mouse
  neural progenitors [PMID:16144902]. This contradicts the earlier interpretation that ectopic Dll3
  inhibits primary neurogenesis as an activating ligand [PMID:9272948 "We confirm that Dll3 can inhibit primary neurogenesis when ectopically expressed in Xenopus, suggesting that it can activate the Notch receptor"].
- Knock-in replacing Dll1 by Dll3 does not rescue; DLL3 does not activate Notch in Drosophila wing
  [PMID:17664336 "Dll3 does not compensate for Dll1; DLL1 activates Notch in Drosophila wing discs, but DLL3 does not."]
  Geffers et al. did not detect DLL3 antagonism of DLL1 in mouse PSM (point of disagreement with Ladi/Chapman).

## Subcellular localisation
- Endogenous DLL3 predominantly in the Golgi, not at the PSM cell surface
  [PMID:17664336 "In contrast to endogenous DLL1 located on the surface of presomitic mesoderm cells, we find endogenous DLL3 predominantly in the Golgi apparatus."]
- Interacts with Notch1 in late endocytic compartment, targeting Notch1 for lysosomal degradation
  [PMID:21147753 "Dll3 is not presented on the surface of presomitic mesoderm (PSM) cells in vivo, but instead interacts with Notch1 in the late endocytic compartment."]
- In oocytes, DLL3 is detected at the membrane close to MIB2; co-IP with Notch2 and Gm364; Gm364 KO reduces
  DLL3 ubiquitination [PMID:34635817 "P Co-IP and blot showed that Notch2 interacts with DLL3."]
- Mib1 interacts with all Notch ligands including Dll3 [PMID:16000382 "Mib1 interacts with and regulates all of the Notch ligands, jagged 1 and jagged 2, as well as Dll1, Dll3 and Dll4."]

## Somitogenesis / disease
- pudgy (Dll3 pu) and targeted null (Dll3 neo) cause vertebral/rib malformations; disrupted segmentation clock
  [PMID:11923214 "the developmental origins of the skeletal defects lie in delayed and irregular somite formation, which results in the perturbation of anteroposterior somite polarity."]
- [PMID:9662403 "the pu mutation disrupts the proper formation of morphological borders in early somite formation and of rostral-caudal compartment boundaries within somites."]
- Human DLL3 mutation causes spondylocostal dysostosis type 1 (SCDO1) [PMID:21147753].
- No overt neural phenotype is reported for Dll3 mutants in the cached literature; neural annotations rest on
  expression and overexpression assays.

## Pathway-variant relevance
- Vertebrate-specific divergent DSL ligand; functions in cis (cis-inhibition), intracellular (Golgi /
  late endosome) rather than as a trans signal-sending ligand. Contrast with Dll1 (canonical activating
  ligand, cell surface, Mib1-dependent endocytosis).

## Deep research
Falcon deep research launched; see review for whether it was used.
