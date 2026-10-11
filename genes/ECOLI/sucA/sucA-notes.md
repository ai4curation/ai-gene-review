# sucA notes

## 2026-09-30 re-review

Deep research was attempted with `just deep-research-falcon ECOLI sucA --fallback perplexity-lite`; the wrapper reported that no Falcon/Edison, OpenAI, Asta, or Perplexity credentials were configured. FEBA/RB-TnSeq fetching was also unavailable because neither the local `/srv/home/cmungall/repos/feba` cache nor the remote fit.genomics.lbl.gov source could be reached.

Manual evidence check:

- PMID:17367808 solved SucA/E1o structures and assayed wild-type and active-site mutant E1o within reconstituted OGDH assemblies containing E1o, E2o/SucB, E3/LpdA, ThDP, MgCl2, NAD+, 2-oxoglutarate, and CoA.
- The AMP pocket observed in SucA should not be promoted to a core nucleotide-binding function because UniProt explicitly notes that its physiological relevance is unclear.
- High-throughput protein-binding rows to SucB/YheS do not add functional information beyond SucA OGDH complex membership and core E1 catalysis.
