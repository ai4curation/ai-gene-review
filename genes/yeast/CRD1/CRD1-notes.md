# CRD1 (YDL142C, Q07560) notes

## Activity
- CMP-forming CL synthase: CDP-DAG + PG -> CL + CMP [PMID:2171667 "Cardiolipin (CL) synthase activity was characterized in mitochondrial extracts of the yeast Saccharomyces cerevisiae and was shown for the first time to utilize CDP-diacylglycerol as a substrate."]
- Gene identification; null lacks CL, PG elevated [PMID:9614098 "Disruption of the CLS1 gene in a haploid yeast strain resulted in the loss of CL synthase activity, no detectable CL, a 5-fold elevation in phosphatidylglycerol levels"]

## Location
- Mitochondrial inner membrane [PMID:9614098 "CL and its synthesis are localized predominantly to the mitochondrial inner membrane"]

## Downstream phenotypes (non-core)
- Membrane potential/import defects [PMID:10777514 "We propose that CL is required for maintaining the mitochondrial membrane potential and that reduced membrane potential in the absence of CL leads to defects in protein import and other mitochondrial functions."]
- Vacuolar acidification defects [PMID:18799619 "we present evidence that the crd1Delta mutant exhibits severe vacuolar defects, including swollen vacuole morphology and loss of vacuolar acidification, at 37 degrees C."]
- Ups1 IM association depends on CL [PMID:26235513 "Ups1 was recovered exclusively in the IM vesicles in WT mitochondria, while it was evenly distributed to the OM and IM vesicles in crd1Δ mitochondria lacking cardiolipin"]

## Curation observations
- YeastPathways writes the CL synthase reaction as 2 PG -> CL + glycerol (bacterial PLD-type ClsA). Wrong for Crd1 (CMP-forming, EC 2.7.8.41). GO RCA term GO:0043337 is nonetheless correct.
- Cytosol RCA -> MODIFY to mitochondrial inner membrane. Lipid biosynthetic process rows -> MODIFY to cardiolipin biosynthetic process.
