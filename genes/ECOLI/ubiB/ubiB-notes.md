# ubiB (P0A6A0, E. coli K-12) review notes

## Sources
- No deep-research provider output (provider API keys unavailable); built from UniProt, cached abstracts
  (PMID:9422602, PMID:10960098, PMID:15919996) and full texts on the UbiB/COQ8 family (PMID:27499294,
  PMID:29198567).

## Findings
- yigR/ubiB required for UQ [PMID:9422602 "An E. coli yigR::Kan mutant was also deficient in ubiquinone content."]
  and [PMID:10960098 "Both the P. stuartii aarF and E. coli ubiB (yigR) disruption mutant strains lack CoQ and
  accumulate octaprenylphenol."]
- E. coli UbiB assayed directly: copurifies with OPP/OHB and has phenol-stimulated ATPase [PMID:29198567 "We found
  that ATPase activity is an evolutionarily conserved feature of COQ8 orthologs from E. coli to humans that is
  enhanced by phenolic compounds resembling CoQ biosynthetic precursors."]
- No trans kinase activity in the family [PMID:27499294 "Screening potential protein substrates for COQ8A and
  Coq8p further demonstrated their lack of trans protein kinase activity."]

## Decisions
- protein kinase activity IEA MODIFY to GO:0016887 ATP hydrolysis activity; NEW GO:0016887 IDA (PMID:29198567).
  Core MF = ATP hydrolysis activity, matching the P. putida ubiB review.
- regulation of UQ biosynthesis MARK_AS_OVER_ANNOTATED (as in P. putida).
