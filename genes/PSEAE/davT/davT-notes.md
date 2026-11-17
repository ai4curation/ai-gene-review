# davT (PA0266, Q9I6M4) curation notes

- Deep research: `just deep-research-falcon PSEAE davT` was attempted on
  2026-11-11 and failed with an authentication error (HTTP 403); no other
  provider key was available in the session. No provider file was written.
  A PubMed search for `(davD OR davT OR PA0265 OR PA0266) AND aeruginosa`
  returned only PMID:17388807.
- PA0266 was predicted and biochemically verified as the 5-aminovalerate
  aminotransferase of P. aeruginosa lysine degradation [PMID:17388807, "we
  identified PA0266 as a putative 5-aminovalerate aminotransferase (EC
  2.6.1.48)"]; the assay was a coupled reaction with PA0265 [PMID:17388807,
  "We observed that the predicted gene products catalyzed the expected
  reactions"]. Only the abstract is cached.
- PANTHER places Q9I6M4 in PTHR11986:SF58, the same subfamily as P. putida
  DavT (Q88RB9) and E. coli PuuE; IBA rows for GABA catabolism and PLP binding
  descend from PTN000944876 and cytosol from PTN000241468.
- GABA-related rows (GO:0034386, GO:0009450) are marked as over-annotation,
  consistently with P. putida DavT and both DavD orthologs: the C5 substrate
  is the only one tested.
