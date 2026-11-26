# ERG4 notes (P25340, YGL012W)

- Function: sterol C-24(28) reductase, final step of ergosterol synthesis [PMID:10722850 "The yeast ERG4 gene encodes sterol C-24(28) reductase which catalyzes the final step in the biosynthesis of ergosterol."]; reaction ergosta-5,7,22,24(28)-tetraenol + NADPH -> ergosterol, EC 1.3.1.71, RHEA:18501 [UniProt:P25340].
- Null phenotype: [PMID:10722850 "Deletion of ERG4 resulted in a complete lack of ergosterol and accumulation of the precursor ergosta-5,7,22,24(28)-tetraen-3beta-ol."]; drug and cation hypersensitivity, brefeldin A sensitivity (same abstract).
- Early enzymology: [PMID:14922 "Optimal conditions for the 24(28)methylene reductase were obtained."] (abstract only).
- Gene identity: YGL022 is the old ORF name of ERG4 [UniProt:P25340 ORFNames=YGL022]; [PMID:8125337 "strains carrying disruptions of sts1+ or YGL022 have ergosterol biosynthesis defects in the enzyme, sterol C-24(28) reductase (Erg4p; encoded by ERG4)"].
- Location: ER, by fractionation + Erg4-EGFP [PMID:10722850 "Enzyme activity measurements with isolated subcellular fractions revealed that Erg4p is localized to the endoplasmic reticulum."]. Polytopic, ERG4/ERG24 family [UniProt:P25340].
- GO issue: GO:0050614 "Delta24-sterol reductase activity" (EC 1.3.1.72, DHCR24-type C24=C25 reduction) is annotated IDA from PMID:10722850 but Erg4 reduces the 24(28) methylene bond (EC 1.3.1.71 = GO:0000246). MODIFY -> GO:0000246.
- YeastPathways cytosol RCA rows -> MODIFY to ER membrane.
- Decisions: 17 ACCEPT, 7 MODIFY.
