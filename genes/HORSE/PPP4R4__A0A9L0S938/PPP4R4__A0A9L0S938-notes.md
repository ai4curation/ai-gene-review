# PPP4R4 (horse, A0A9L0S938) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

- Folder created with `just fetch-gene HORSE A0A9L0S938 --alias PPP4R4__A0A9L0S938`. A0A9L0S938 is the UniProt
  reference-proteome canonical product of horse gene ENSECAG00000019485; `genes/HORSE/PPP4R4` holds the
  A0A9L0S961 isoform. No ProtNLM2 files or prediction-evidence folders were consulted.
- Deep research: `just deep-research-falcon HORSE A0A9L0S938 --alias PPP4R4__A0A9L0S938 --fallback perplexity-lite`
  FAILED. Falcon returned "Failed to authenticate", and the perplexity-lite fallback returned HTTP 401
  insufficient_quota. No deep-research file exists. The review uses the cached literature directly.
- Literature: there are no horse studies. The only functional study is on the human protein
  [PMID:18715871 "Our data demonstrate that PP4R4 forms a novel cytosolic complex with PP4c, independent from
  the complexes containing PP4R1, PP4R2.PP4R3, and alpha4"]. Human PP4R4 binds PP4c specifically
  [PMID:18715871 "specifically associates with PP4c (and not with the related PP2Ac or PP6c phosphatases)"]
  and the complex is less active than free PP4c in vitro.
- Evolutionary grounding: A0A9L0S938 is in PANTHER PTHR21467:SF0, the family's only subfamily and the same one as
  human Q6NUP7. Its IBAs come from PTN001087371, the same node as human. My global alignment
  (`PPP4R4__A0A9L0S938-bioinformatics/RESULTS.md`) gives 95.4% identity over 99.5% of human, with the same
  C-terminus. A0A9L0S961 differs only in its last ~8 residues (99.5% identity), which looks like alternative
  3' splicing.
- PAINT propagated regulator activity, cytosol and the phosphatase complex, but not the human inhibitor IDA terms.
  I take that omission as deliberate, and the human review also modifies the inhibitor terms to the regulator term.
  No NEW terms are proposed.
- Actions: cytoplasm IEA MODIFY to cytosol; cytosol IBA ACCEPT; protein serine/threonine phosphatase complex IBA
  MODIFY to protein phosphatase 4 complex (GO:0030289), as in the human review; protein phosphatase regulator
  activity IBA ACCEPT (core). Every function here is inferred by orthology. None has been shown experimentally
  in horse.
