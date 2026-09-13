# purM curation notes

- UniProt identifies Q88MA9 as Phosphoribosylformylglycinamidine cyclo-ligase [file:PSEPK/purM/purM-uniprot.txt "RecName: Full=Phosphoribosylformylglycinamidine cyclo-ligase"].
- Remove the transferred PurD ligase activity because the exact protein is PurM/AIR
  synthetase. Retain both electronic cytoplasm and cytosol localizations as
  non-core, and replace broad purine biosynthesis with `GO:0006189`; adenine
  synthesis branches downstream from IMP and is therefore outside PurM's de
  novo IMP pathway role.
- PTHR10520:SF12 contains both standalone bacterial PurM and eukaryotic
  trifunctional GART proteins; the exact PurM molecular function is therefore
  required to constrain the family selector.
