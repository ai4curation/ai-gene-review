# sucB notes

## 2026-09-30 re-review

Deep research was attempted with `just deep-research-falcon ECOLI sucB --fallback perplexity-lite`; the wrapper reported that no Falcon/Edison, OpenAI, Asta, or Perplexity credentials were configured. FEBA/RB-TnSeq fetching was also unavailable because neither the local `/srv/home/cmungall/repos/feba` cache nor the remote fit.genomics.lbl.gov source could be reached.

Manual evidence check:

- PMID:17367808 defines SucB as the lipoylated E2o enzyme in the E. coli 2-oxoglutarate dehydrogenase complex and documents SucA-SucB interaction.
- PMID:1854331 supports lipoylation of the E. coli 2-oxoglutarate dehydrogenase E2 domain.
- The GO:0033512 L-lysine catabolic process annotation is a UniPathway family-level transfer and does not match E. coli SucB, whose characterized physiological role is OGDH E2 succinyltransferase activity.
- Generic protein-binding rows from IntAct were removed rather than mapped onto a second molecular function; the functional assembly is represented by GO:0045252 oxoglutarate dehydrogenase complex.
