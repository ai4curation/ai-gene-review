# SIX6 notes

Automated deep research was unavailable for this session (falcon 402, OpenAI 401); no
`-deep-research-<provider>.md` file was generated. Notes from cached publications and UniProt.

## Molecular function
- Strong tissue-specific repressor with Dach corepressors (mouse):
  [PMID:12130660 "Six6, in association with Dach corepressors, regulates proliferation by directly repressing cyclin-dependent kinase inhibitors, including the p27Kip1 promoter."]
- Binds Groucho/TLE1 and AES (SIX6 was the two-hybrid bait): [PMID:12441302 "identification of TLE1 (a transcriptional repressor of the groucho family) and AES ... as cofactors for both SIX6 and SIX3"].
- Binds the Shh SBE2 enhancer directly in EMSA [PMID:18836447 "indicating that the binding of Six3 and Six6 to SBE2 was direct"].
- HT-SELEX profiled [PMID:28473536].

## Biological roles / disease
- Retinal and pituitary progenitor proliferation [PMID:12130660].
- Eye field specification with Six3 [PMID:12441302 "Six3 and Six6 are two genes required for the specification and proliferation of the eye field"].
- 14q22-q23 deletions with SIX6 hemizygosity: anophthalmia + pituitary anomalies [PMID:10512683]; but no SIX6
  point mutations found in 173 MAC patients [PMID:15505031]. Homozygous truncation -> complex microphthalmia (ODRMD) [PMID:23167593; abstract unavailable].
- POAG / cup-disc ratio association; zebrafish six6a knockdown reduces optic nerve volume; Asn141His and Leu205Arg hypomorphic [PMID:24875647].

## Review decisions
- NEW: GO:0001227 (ISS from mouse PMID:12130660), GO:0001222 (IPI PMID:12441302).
- Visual perception REMOVE (IEA) / over-annotated (TAS). Animal organ morphogenesis -> retina development in camera-type eye.
- Module annoton GO:0000981 in eye development is consistent; SIX6 is better described as a repressor.
