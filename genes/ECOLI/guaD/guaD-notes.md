# ECOLI guaD notes

## 2026-10-02

`just fetch-gene ECOLI guaD` seeded 12 GOA annotations for reviewed UniProt
accession P76641 and fetched PMID:10913105 as full text. PMID:20023034 was
available only as an abstract in the local publication cache even though it has
a PMCID; the abstract directly reports that an E. coli guanine deaminase
deletion mutant is deficient in ammeline deaminase activity, and also frames
ammeline deamination as a promiscuous activity of widespread GuaD orthologs.

`just deep-research-falcon ECOLI guaD --fallback perplexity-lite` failed because
no deep-research providers were configured (`OPENAI_API_KEY`,
`EDISON_API_KEY`, `ASTA_API_KEY`, `PERPLEXITY_API_KEY`, and `agentapi` were
unavailable), so this review relies on the cached papers, UniProt, PANTHER
PTHR11271, and the existing PSEPK guaD review.

`just fetch-fitness ECOLI guaD` failed because no local FEBA database was
present at `/srv/home/cmungall/repos/feba/cgi_data/feba.db` and the remote bulk
source was unreachable.

Decision sketch:

- Accept the exact guanine deaminase activity and guanine catabolic process
  annotations. Maynes et al. purified recombinant E. coli GuaD and showed
  guanine-to-xanthine turnover with `Km = 15.4 +/- 1.8 uM` and
  `kcat = 3.18 +/- 0.12 s^-1`.
- Keep zinc ion binding as non-core. The zinc measurement and chelator
  inhibition in PMID:10913105 verify it as a catalytic cofactor property rather
  than the defining activity.
- Keep the cytosol IBA as non-core.
- Mark broad hydrolase parent terms as over-annotated because GO:0008892 carries
  the experimentally established substrate specificity.
- Keep ammeline aminohydrolase activity as a non-core promiscuous activity:
  PMID:20023034 reports an E. coli guaD knockout phenotype for ammeline
  deamination, and PMID:31283204 later directly showed secondary ammeline
  deaminase activity for purified EcGuaD, but the physiological purine substrate
  remains guanine.
