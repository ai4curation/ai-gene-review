# SAC1 (P32368, YKL212W) notes

Evidence journal (YeastPathways phosphoinositide_biosynthesis batch, 2026-10-06).

## Activity
- Phosphoinositide phosphatase; PtdIns3P and PtdIns4P hydrolysis, low activity on PtdIns(3,5)P2 [UniProt:P32368 "Has low activity towards phosphatidylinositol-3,5-"].
- [PMID:10625610 "SAC1 encodes a novel lipid phosphoinositide phosphatase"]; sac1 mutants alter PtdIns4P and PI(4,5)P2 levels.
- Principal in vivo substrate PtdIns4P [PMID:11514624 "inactivation of Sac1p leads to a specific increase in the cellular levels of phosphatidylinositol 4-phosphate (PtdIns(4)P)"]; mainly the Stt4 pool [PMID:11514624 "Sac1p primarily turns over Stt4p-generated PtdIns(4)P"].
- [PMID:11792713 "Sac1p is an important 4-phosphatase in the ER"]; Osh-stimulated activity [PMID:21295699 "We reconstitute Osh protein-stimulated Sac1 PI phosphatase activity in vitro."].

## YeastPathways assignments
- PI4P -> PI (EC 3.1.3.-): correct, core.
- PI3P -> PI (EC 3.1.3.64): supported in vitro; ER PI3P pool [PMID:11792713 "Sac1p controls a pool of phosphatidylinositol 3-phosphate and phosphatidylinositol 4-phosphate in the ER"]. Physiological PI3P phosphatases are mainly Ymr1/Sjl2/Sjl3.
- PI(3,5)P2 dephosphorylation mapped to GO:0043813 (5-phosphatase): questionable - Sac1 activity on PI(3,5)P2 is low and SGD curated it as 3-phosphatase (GO:0052629); Fig4 is the physiological 5-phosphatase. Marked over-annotated; the derived IEA 'PI3P biosynthetic process' removed.
- RCA 'phosphatidylinositol phosphate biosynthetic process' is the wrong direction for a phosphatase -> MODIFY to PI dephosphorylation.

## Location
- ER membrane, type II TM [PMID:11792713 "Sac1p is a type II transmembrane protein with a large N-terminal cytosolic domain"]; Golgi on growth arrest [PMID:15657391 "causing translocation of Sac1p to Golgi membranes"]; cortical ER [PMID:30785834 "while Sac1p is mainly found in the PM-associated part of the cortical ER"]; medial Golgi via Vps74 [PMID:22553352 "Vps74 binds directly to the catalytic domain of Sac1"].
- Mitochondrial proteome hits treated as contamination.

## Other
- SPOTS complex member [PMID:20182505 "These findings together suggest that Sac1 modulates serine palmitoyltransferase activity directly, but in a mode distinct from Orm1/2."].
- Autophagosome-vacuole fusion [PMID:32693712 "critical for autophagosome-lysosome fusion through its PtdIns4P phosphatase activity"].
- Co-opted by TBSV (PMID:32269127).
