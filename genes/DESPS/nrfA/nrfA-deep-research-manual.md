# Manual Deep Research: nrfA

Automated Falcon and OpenScientist runs did not complete for nrfA, so this is a manual synthesis from the fetched UniProt record and the completed PTHR30633 family research.

## Evidence synthesis

nrfA is annotated as cytochrome c-552, specifically an ammonia-forming cytochrome c nitrite reductase with EC 1.7.2.2 [file:DESPS/nrfA/nrfA-uniprot.txt "AltName: Full=Ammonia-forming cytochrome c nitrite reductase"; "EC=1.7.2.2"]. UniProt states that it reduces nitrite to ammonia while consuming six electrons [file:DESPS/nrfA/nrfA-uniprot.txt "Catalyzes the reduction of nitrite to ammonia, consuming six electrons in the process"].

The family research is important because the cytochrome c-552 display label is not equivalent to catalytic NrfA activity in every member. PANTHER should be used through its tree, subfamily, and propagation evidence rather than by treating the root label as a GO assertion. PTHR30633 can include periplasmic electron-transfer cytochromes as well as catalytic nitrite reductases, so the c552 family name alone should not be used to propagate either nitrate-assimilation or catalytic claims [file:interpro/panther/PTHR30633/PTHR30633-deep-research-falcon.md "conflate catalytic nitrite reductases with electron-transfer cytochromes"]. For this gene, HAMAP MF_01182, InterPro IPR017570, and the EC/reaction text support ammonia-forming nitrite reductase.

## Curation consequence

Accept ammonia-forming cytochrome c nitrite reductase activity and anaerobic electron-transport context. Remove nitrate assimilation because the reaction is dissimilatory nitrite reduction to ammonium, not assimilatory nitrate incorporation.
