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

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK cheA --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/cheA/cheA-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Literature added: PMID:30761113 (Lopez-Farfan 2019, full text; was cited by DOI only) [PMID:30761113 "mutation of cheA2 abolished chemotaxis, which is consistent with the notion the CheA2 forms part of the che chemotaxis pathway"]; PMID:40197389 (He 2025, full text) [PMID:40197389 "The results showed that CheA exhibited a strong autophosphorylation signal after incubation with [32P]ATP[γP] for 45 min"] [PMID:40197389 "The addition of CheY to phosphorylated CheA led to a labeling of CheY and a reduction in the phospholabeling of CheA"]. PMIDs found via Europe PMC search (DOI and title queries). The He 2025 text does not give the CheA locus tag; its chemotaxis-null cheA deletion matches PP_4338.
- The UniProt CC FUNCTION/CATALYTIC ACTIVITY lines are ARBA-only; replaced as support by the papers above and by PROSITE FT DOMAIN / MOD_RES lines.
- GO:0000155 phosphorelay sensor kinase activity is an is_a CHILD of GO:0004673 (earlier note had this backwards). Its definition puts signal detection on the kinase; CheA is receptor-controlled [PMID:40197389 "methylated MCPs and the coupling protein CheW activate CheA autophosphorylation"]. MODIFY -> GO:0004673 (same as E. coli CheA).
- GO:0016772 MODIFY -> GO:0004673; GO:0007165 TOO_GENERAL (ancestor of accepted GO:0000160); GO:0005737 ACCEPT (no KT2440 localization data for a more specific term).
- Removed six non-verbatim falcon quotes (baseline-listed) and the DE-name quote. Status COMPLETE.
