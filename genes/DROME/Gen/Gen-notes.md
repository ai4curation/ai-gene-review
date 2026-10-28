# Gen (DROME) review notes

- UniProt Q9VRJ0 (GEN_DROME, Swiss-Prot), FlyBase FBgn0263831, GeneID 38594. fetch-gene resolved the
  expected accession.
- Literature compiled by hand in `Gen-deep-research-manual.md` (no deep-research API keys).
- Cached full text: PMID:22022278, PMID:28369583, PMID:17660539, PMID:25205745. Abstract only:
  PMID:15576351, PMID:17614965 (FlyBase/UniProt IDA rows rest on these).

## Key decisions

- 3'-5' exonuclease rows (GO:0008310, GO:0008311; IDA PMID:15576351): REMOVE. UniProt CAUTION states the
  activity is probably artifactual (contaminating nucleases); the follow-up with an active-site mutant
  (PMID:17614965) reports only nick-dependent 5'-3' exonuclease, and Bellendir 2017 detected no cleavage of
  unbranched or nicked duplex [PMID:28369583 "We did not detect cleavage of unbranched dsDNA, nicked duplex DNA, or 3΄ flaps"].
  Flagged for expert check because the original full text is not cached.
- Nucleus (IDA, PMID:17614965) vs cytoplasm (IDA, PMID:28369583): both kept as non-core. The later study
  argues GEN is cytoplasmic in interphase like HsGEN1 [PMID:28369583 "DmGen, like Yen1 and HsGEN1, is primarily or exclusively cytoplasmic during interphase"].
  No location is put in core_functions.
- UniProt FUNCTION text ("Does not cleave bubble-like or Holliday junction substrates") is outdated with
  respect to HJs: PMID:28369583 shows robust symmetric HJ cleavage. Recorded as a suggested question
  (UniProt function text update).
- No NEW process terms. GO:0071140 (resolution of mitotic recombination intermediates) was considered;
  biochemistry shows GEN cleaves HJs and Blm synthetic lethality is partially Rad51-dependent, but in vivo
  HJ resolution by GEN in flies is not directly demonstrated and the authors themselves suggest simpler
  branched structures may be the main substrates. Left as a suggested question.
- PMID:17660539 (DSB repair IMP): the paper tests mus324 (later shown = Gen, PMID:22022278) and finds a mild
  SSA reduction only with 32 C induction; weak, but DSB repair is corroborated by IR hypersensitivity
  (PMID:28369583). Accepted.
