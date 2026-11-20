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


## 2026-11-07 ISC whole-gene re-review

PMID25688831 directly reconstitutes E. coli NADPH→FNR(P28861)→Fdx→IscS/IscU electron delivery. FNR was codon-optimized and expressed from a His6/TEV construct. GO0022900 does not require respiration or energy conservation, so the old rejection is corrected. This does not establish unique native donor use or every-condition necessity. PMID33712431 was acquired to check cold/iron-loading behavior; no new temperature-response or iron-binding annotation was manufactured from the additional biochemical context.

All original ordered annotation payloads and historical NEW actions were preserved. Existing raw/provider/publication files were not refreshed. A genuine new default Falcon attempt returned HTTP 403; no provider report was fabricated. Manual source review is recorded here and in `analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/ecoli-consultation/`. The normal PAINT lineage-loss check found no IRD or IKR; donor-list length and target self-inclusion were not used as evidence against the ancestral assertion. Focused validation, render, and append-only helper-history results are recorded in the final handoff.
