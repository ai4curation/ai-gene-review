# cheA Notes

- Q88EW4 is the KT2440 chemotaxis histidine kinase locus `PP_4338`; the KT2440
  literature calls this paralog `cheA2` [UniProt:Q88EW4 "OrderedLocusNames=PP_4338"]
  [DOI:10.3389/fmicb.2019.00078 "PP_4338 (cheA2)"].
- UniProt gives the canonical CheA mechanism: transmission of receptor input to
  the flagellar pathway through autophosphorylation and phosphotransfer to CheB
  or CheY [UniProt:Q88EW4 "CheA is autophosphorylated; it can transfer its phosphate group to either CheB or CheY."].
- The conserved phosphohistidine is His49 in the HPt domain, consistent with a
  phosphorelay histidine kinase [UniProt:Q88EW4 "MOD_RES         49 /note=\"Phosphohistidine\""]
  [UniProt:Q88EW4 "DOMAIN          2..106 /note=\"HPt\""].
- The strongest KT2440 phenotype is in chemotaxis rather than generic signaling:
  Lopez-Farfan et al. report that `a cheA2 mutant was entirely deficient in MRE
  chemotaxis` [DOI:10.3389/fmicb.2019.00078 "a cheA2 mutant was entirely deficient in MRE chemotaxis"].
- The same paper separates paralog function: `cheA1` affected c-di-GMP and
  biofilm formation, whereas `cheA2` mapped to the classical chemotaxis pathway
  [DOI:10.3389/fmicb.2019.00078 "a mutant in cheA1 showed reduced c-di-GMP levels and impaired biofilm formation"]
  [DOI:10.3389/fmicb.2019.00078 "indicating the existence of homologs of the P. aeruginosa wsp and che (chemotaxis) pathways"].
- Annotation consequences:
  keep `protein histidine kinase activity`, `phosphorelay signal transduction
  system`, and `chemotaxis`; demote or remove broader parent terms like
  `phosphorelay sensor kinase activity`, `transferase activity, transferring
  phosphorus-containing groups`, and `signal transduction`.
