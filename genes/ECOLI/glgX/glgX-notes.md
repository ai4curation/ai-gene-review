# glgX notes

## 2026-09-30 re-review

Deep research was attempted with `just deep-research-falcon ECOLI glgX --fallback perplexity-lite`; the wrapper reported that no Falcon/Edison, OpenAI, Asta, or Perplexity credentials were configured. FEBA/RB-TnSeq fetching was also unavailable because neither the local `/srv/home/cmungall/repos/feba` cache nor the remote fit.genomics.lbl.gov source could be reached.

Manual evidence check:

- PMID:15687211 shows that E. coli GlgX is an isoamylase-type glycogen debranching enzyme with specificity for three- and four-glucose alpha-1,6 branches and that glgX deletion overproduces glycogen with short external chains.
- `modules/glycogen_synthesis_and_mobilization.yaml` models GlgX after GlgP, removing the alpha-1,6 branch stubs exposed by phosphorolysis. That module uses GO:0120549 rather than the legacy amylo-alpha-1,6-glucosidase activity term.
- PMID:11967071 is a transcriptomics response-to-DNA-damage paper. The cached abstract supports expression changes after mitomycin C, not a direct DNA-damage-response role for GlgX.
