# Manual Deep Research: Ferp_0128

Automated Falcon and OpenScientist runs did not complete for Ferp_0128, so this is a manual synthesis from the fetched UniProt record and the completed PTHR42838 family research.

## Evidence synthesis

Ferp_0128 is annotated as nitrous-oxide reductase with EC 1.7.2.4 [file:FERPA/Ferp_0128/Ferp_0128-uniprot.txt "RecName: Full=Nitrous-oxide reductase; EC=1.7.2.4"]. UniProt maps it to denitrification step 4 of 4 and says it belongs to the NosZ family [file:FERPA/Ferp_0128/Ferp_0128-uniprot.txt "PATHWAY: Nitrogen metabolism; nitrate reduction (denitrification); dinitrogen from nitrate: step 4/4"; "Belongs to the NosZ family"].

The family-level finding mirrors nosZ: PTHR42838 includes both true NosZ/N2OR proteins and cytochrome c oxidase subunit II-like CuA proteins. That explains why cytochrome-c oxidase activity can be attached incorrectly to NosZ-like sequences [file:interpro/panther/PTHR42838/PTHR42838-deep-research-falcon.md "separates true NosZ/N2OR proteins from cytochrome c oxidase subunit II homologs"]. For Ferp_0128, the EC, pathway text, and NosZ subfamily support nitrous-oxide reductase.

## Curation consequence

Accept nitrous-oxide reductase activity and denitrification pathway. Remove cytochrome-c oxidase activity and leave proton transport unresolved because Ferp_0128 is the terminal reductase, not itself a proton pump.
