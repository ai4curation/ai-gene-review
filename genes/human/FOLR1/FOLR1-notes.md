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

## 2026-11-23 ORGANELLES endosome batch 1

- Two GO:0005768 rows (EXP PMID:8567728; IEA SL-0101 tagged ECO:0000269 to the same paper). Both ACCEPT, core (endocytic receptor; folate release in the acidic endosome and receptor recycling are part of the activity).
- Read the full text of PMID:8567728 outside the cache: PMCID PMC2120708, DOI 10.1083/jcb.132.1.35 (Rijnboutt et al. 1996). Endogenous receptor in human KB cells grown in low folate; immunogold on ultrathin cryosections; Table I: about 88% of gold at the plasma membrane (including coated pits and caveolae), 9.3% in the endocytic compartment (tubulo-vesicular structures, endosomes, multivesicular endosomes, identified with internalised BSA-gold), about 2% biosynthetic (ER, Golgi, TGN). No stage marker (EEA1, Rab5, Rab7, Rab11, transferrin) was used. Not quoted beyond the cached abstract.
- Folate release in the acidic endosome is stated in [PMID:23851396 "Inside of the cell, the acidic environment of the endosome promotes the release of folate from receptors"] (author statement in the introduction).
- NEW GO:0010008 endosome membrane (IC) added beside the root: own GPI anchor [PMID:2527252] plus endogenous immunogold in endosomes [PMID:8567728]. No stage row. The two GO:0016020 rows stay MODIFY to plasma membrane only, because their evidence is about the cell-surface receptor.
