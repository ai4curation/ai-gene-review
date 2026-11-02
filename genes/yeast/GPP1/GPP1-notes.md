# GPP1 / RHR2 (YIL053W, UniProt P41277) notes

## Activity
- Specific DL-G3Pase, EC 3.1.3.21 [PMID:8662716 "Both isoforms have a high specificity for dl-glycerol-3-phosphate, pH optima at 6.5, and KmG3P in the range of 3-4 mM."]
- Not stereospecific in vitro; acts on sn-glycerol 1-P and sn-glycerol 3-P [UniProt:P41277]. In vivo substrate = sn-G3P from Gpd1/Gpd2.

## Role
- Required for glycerol biosynthesis (redundant with GPP2) [PMID:11058591 "Mutants lacking both GPP1 and GPP2 are devoid of glycerol 3-phosphatase activity and produce only a small amount of glycerol, confirming the essential role for this enzyme in glycerol biosynthesis."]
- [PMID:11058591 "The gpp1Delta/gpp2Delta double mutant is hypersensitive to high osmolarity, whereas the single mutants remain unaffected, indicating GPP1 and GPP2 substitute well for each other."]
- Anaerobic: [PMID:11058591 "mutants lacking GPP1 show poor anaerobic growth"]
- Not rate limiting [PMID:11676566 "In contrast, overexpression of GPP1, encoding glycerol 3-phosphatase (Gpp1p), did not enhance glycerol production."]
- Cytosolic [PMID:27385335 "exhibited a very prominent cytosolic distribution"]

## Curation observations
- YeastPathways writes the reaction as 'glycerol 1-phosphate' (EC name); RCA mapped to sn-glycerol 1-phosphatase (GO:0000121). Wrong stereoisomer for the pathway -> MODIFY RCA to GO:0043136. Other GO:0000121 rows kept non-core (true in vitro).
- TAS response to osmotic stress cites PMID:11676566, which does not address osmotic stress; kept non-core.
