# Manual Deep Research: nirK2

Automated Falcon and OpenScientist runs did not complete for nirK2, so this is a manual synthesis from the fetched UniProt record and the completed multicopper-oxidase family research.

## Evidence synthesis

nirK2 is annotated as a copper-containing nitrite reductase with EC 1.7.2.1 [file:RHOPA/nirK2/nirK2-uniprot.txt "RecName: Full=Copper-containing nitrite reductase; EC=1.7.2.1"]. UniProt maps the protein to denitrification, step 2 of 4, matching NO-forming nitrite reduction [file:RHOPA/nirK2/nirK2-uniprot.txt "PATHWAY: Nitrogen metabolism; nitrate reduction (denitrification); dinitrogen from nitrate: step 2/4"].

The sequence carries NO2-reductase_Cu/cupredoxin features and the TIGR02376 copper nitrite reductase model [file:RHOPA/nirK2/nirK2-uniprot.txt "InterPro; IPR001287; NO2-reductase_Cu"; "NCBIfam; TIGR02376; Cu_nitrite_red; 1"]. The PTHR11709 deep-research report shows why the broad multicopper-oxidase family is not by itself enough for substrate-specific annotation; here, the EC and nitrite-reductase-specific signatures justify the more precise function [file:interpro/panther/PTHR11709/PTHR11709-deep-research-falcon.md "multicopper oxidases are functionally diverse"].

## Curation consequence

Accept nitrite reductase (NO-forming) activity and denitrification pathway for nirK2. Keep broad oxidoreductase activity as non-core because it adds little beyond the specific nitrite reductase term.
