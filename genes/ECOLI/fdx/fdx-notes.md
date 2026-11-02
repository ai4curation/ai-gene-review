# fdx (P0A9R4, E. coli K-12) notes

Provider deep research could not run: `just deep-research-falcon` failed with Edison API 403 (auth), 2026-10-23. These notes are from the cached publications and the UniProt record.

## Function
- Adrenodoxin-type [2Fe-2S] ferredoxin [PMID:4375562 "Escherichia coli ferredoxin, an iron-sulfur protein of the adrenodoxin type."]
- Donates an electron to IscS [PMID:23682711 "These results (1) show that reduced Fdx supplies one electron to the IscS complex as S(0) is produced by the enzymatic conversion of Cys to Ala and (2) explain the role of Fdx as a member of the isc operon."]; [PMID:23682711 "These results indicate that donation of an electron from reduced Fdx is essential to cluster assembly on IscU."]
- Competes with IscU and CyaY for binding to IscS [PMID:23682711 "We found that Fdx, IscU, and CyaY (the bacterial frataxin) compete for overlapping binding sites on IscS."]
- Genetics [PMID:11432781 "Strains with mutations in the iscU, hscB, hscA, and fdx genes also exhibited conspicuous phenotypical consequences almost identical to one another."]
- Fdx is the acceptor of an IscA-derived cluster [PMID:11319236 "The metal form but not the apoform of IscA binds ferredoxin, another member of the isc operon, selectively, allowing transfer of iron and sulfide from IscA to ferredoxin and formation of the [2Fe-2S] holoferredoxin."]

## Curation decisions
- Core MF is GO:0009055, in GO:0016226. This matches the module.
- GO:0140647 (P450 electron transport chain) is removed because E. coli K-12 has no P450. GO:0022900 is marked as over-annotated. GO:0051536 is changed to GO:0051537.
