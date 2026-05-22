# Manual Deep Research: nosZ

Automated Falcon and OpenScientist runs did not complete for nosZ, so this is a manual synthesis from the fetched UniProt record and the completed PTHR42838 family research.

## Evidence synthesis

nosZ is annotated as nitrous-oxide reductase with EC 1.7.2.4 [file:RHOPA/nosZ/nosZ-uniprot.txt "RecName: Full=Nitrous-oxide reductase; EC=1.7.2.4"]. UniProt maps the protein to nitrate reduction by denitrification, step 4 of 4, which is the N2O-to-N2 terminal reaction [file:RHOPA/nosZ/nosZ-uniprot.txt "PATHWAY: Nitrogen metabolism; nitrate reduction (denitrification); dinitrogen from nitrate: step 4/4"].

The interesting finding is the family-boundary problem. PTHR42838 contains true NosZ/N2OR proteins and cytochrome c oxidase subunit II-like CuA proteins, so cytochrome-c oxidase activity can spill over from shared CuA-domain ancestry [file:interpro/panther/PTHR42838/PTHR42838-deep-research-falcon.md "separates true NosZ/N2OR proteins from cytochrome c oxidase subunit II homologs"]. nosZ has NosZ-specific EC and pathway evidence, so nitrous-oxide reductase is the correct molecular function.

## Curation consequence

Accept nitrous-oxide reductase activity and denitrification pathway. Remove cytochrome-c oxidase activity as a family-domain over-annotation.
