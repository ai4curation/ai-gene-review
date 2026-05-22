# Manual Deep Research: algE

Automated Falcon and OpenScientist runs did not complete for algE, so this is a manual synthesis from the fetched reviewed UniProt record.

## Evidence synthesis

algE encodes AlgE, an outer-membrane alginate production protein [file:PSEPK/algE/algE-uniprot.txt "RecName: Full=Alginate production protein AlgE"]. UniProt states that it has non-porin-like channel-forming properties and probably functions as an alginate permeability pore, and maps it to alginate biosynthesis [file:PSEPK/algE/algE-uniprot.txt "Has non-porin-like, channel-forming properties and probably functions as an alginate permeability pore"; "PATHWAY: Glycan biosynthesis; alginate biosynthesis"].

Domain support is consistent with the channel/export role: InterPro includes Alginate_export_dom and Alginate_Permeability_Chnl, and the record places the protein at the cell outer membrane with a signal peptide [file:PSEPK/algE/algE-uniprot.txt "InterPro; IPR025388; Alginate_export_dom"; "InterPro; IPR053728; Alginate_Permeability_Chnl"; "SUBCELLULAR LOCATION: Cell outer membrane"; "SIGNAL          1..25"]. The main gap is ontology expressivity: the current GOA captures outer-membrane location and alginic acid biosynthesis process, but not a specific alginate pore/channel molecular function.

## Curation consequence

Accept outer membrane and alginic acid biosynthetic process for algE. Keep the proposed new term for alginate channel activity because the core role is polymer export/channel function, not a catalytic biosynthetic step.
