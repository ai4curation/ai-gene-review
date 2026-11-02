# lpd notes

## 2026-09-30 re-review

Deep research was attempted with `just deep-research-falcon ECOLI lpd --fallback perplexity-lite`; the wrapper reported that no Falcon/Edison, OpenAI, Asta, or Perplexity credentials were configured. FEBA/RB-TnSeq fetching was also unavailable because neither the local `/srv/home/cmungall/repos/feba` cache nor the remote fit.genomics.lbl.gov source could be reached.

Manual evidence check:

- PMID:3066354 directly overexpressed and mutagenized the E. coli lpd gene and measured lipoamide dehydrogenase activity, supporting GO:0004148.
- PMID:2211531 shows that lpdA encodes the L protein used by the E. coli glycine cleavage complex; the same protein is also common to pyruvate and 2-oxoglutarate dehydrogenases.
- PMID:17367808 defines the E. coli OGDH complex as SucA/E1o, SucB/E2o, and LpdA/E3. The lpd TCA-cycle row is therefore sound even though the paper structurally focuses on SucA.
- PMID:24580753 supports hydrogen-peroxide sensitivity from loss of LpdA but is phenotype-level evidence; it does not make oxidative stress response a core function.
- The zinc-binding annotation from PMID:11985624 is not verifiable from the cached abstract, which lists several identified zinc-binding proteins but not LpdA by name.
