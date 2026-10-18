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

## Full-gene metabolic-scope re-review, 2026-09-20

The standalone AIRS/AIRS_C architecture supports the exact PurM reaction and rejects transfer of the distinct PurD/GARS activity from the fused GART-family context (PTN002237315). Cytoplasm/cytosol and broad purine-nucleotide biosynthesis are core compatible inferences, not weak annotations because they are electronic or broad. GO:0046084 adenine biosynthesis was checked against current GO usage: exact experimental annotations include Candida ADE5:7 (A0A1D8PE67), yeast ADE8 and fission-yeast ade7. The official UniProt comparator record confirms AIRS activity and RHEA:23032 in ADE5:7; PMID:17600079 reports "resulting mutants were adenine deficient". These upstream de novo-enzyme comparators contradict a categorical restriction to free-base-release enzymes. PurM contributes the same AIR-synthesis work, so the adenine annotation is accepted; the project module boundary is not a biological exclusion. All five pre-existing cached purine reports were read: three inventory/context hits and two pathway-mechanism reports, none a focused GO:0046084 adjudication. Their generated contents were exported with ResearchProcessor and hashes, not rewritten. The live comparator evidence settles the scope without another OpenScientist request.
