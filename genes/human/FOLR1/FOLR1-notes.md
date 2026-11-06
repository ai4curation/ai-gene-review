# FOLR1 (P15328) — curation notes

Deep-research providers are unavailable in this environment; research is from the cached
publications, the UniProt record and PubMed.

## Protein and localization

Folate receptor alpha is **GPI-anchored on the outer leaflet of the plasma membrane**, so
the whole folate-binding domain is extracellular and accessible on intact cells.
[PMID:2527252 "Complementary DNA for the folate binding protein correctly predicts anchoring to the membrane by glycosyl-phosphatidylinositol."]
[file:human/FOLR1/FOLR1-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:2527252, ECO:0000269|PubMed:8033114, ECO:0000269|PubMed:8567728}; Lipid-anchor, GPI-anchor"]
It recycles through clathrin-coated vesicles and endosomes.
[PMID:8567728 "Using immunoelectron microscopy, we found MFR-alpha along the entire endocytic pathway: in clathrin-coated buds and vesicles, and in small and large endosomal vacuoles."]
Polarised sorting is tissue-dependent: basolateral in retinal pigment epithelium, apical
elsewhere.
[PMID:10787414 "which contrasts with the basolateral distribution of FRalpha in these cells"]

Localization conclusion: **plasma membrane, GPI-anchored with the ligand-binding domain
extracellular**, plus the endocytic recycling compartments. The 21 Reactome rows for ER
membrane, ERGIC, ER-to-Golgi vesicles, Golgi membrane and transport vesicles describe the
GPI-anchoring and secretory route and are kept as non-core; the extracellular-region row
reflects the shed soluble form; the single nucleus row is a surprising claim and is kept
as non-core.

## Function

[file:human/FOLR1/FOLR1-uniprot.txt "Binds to folate and reduced folic acid derivatives and mediates delivery of 5-methyltetrahydrofolate and folate analogs into the interior of cells"]
[file:human/FOLR1/FOLR1-uniprot.txt "Exposure to slightly acidic pH after receptor endocytosis triggers a conformation change that strongly reduces its affinity for folates and mediates their release"]
[PMID:23851396 "To understand how folate binds its receptors, we determined the crystal structure of human FRα in complex with folic acid at 2.8 Å resolution."]

## Review decisions of note

- Both `signaling receptor activity` rows (IBA and TAS) were MODIFYed to
  `GO:0061714 folic acid receptor activity`. GO places that term under cargo receptor
  activity, and its definition — combining selectively with extracellular folic acid and
  delivering it into the cell via endocytosis — is precisely what FOLR1 does. The TAS row
  rests on co-residence with Lyn and G alpha i-3 in detergent-resistant membranes, which
  is typical of GPI-anchored proteins and does not show signal transduction by FOLR1.
- `tetrahydrofolate biosynthetic process` was marked as over-annotation: FOLR1 imports
  folates, while DHFR performs the reduction.
- Rodent-derived developmental rows (heart looping, neural crest migration, pharyngeal
  arch artery morphogenesis, anterior neural tube closure, axon regeneration, Wnt and
  TGF-beta regulation) are kept as non-core, since the receptor's contribution is folate
  supply.
