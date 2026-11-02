# lnt notes

## 2026-10-02

`just deep-research-falcon ECOLI lnt` could not run in this Orca environment
because `agentapi` was not available on `PATH` and no provider API keys were
configured, so this review uses the cached primary literature from
`just fetch-gene` plus the fetched UniProtKB record.

Manual synthesis:

- Lnt is the E. coli inner-membrane apolipoprotein N-acyltransferase. Gupta and
  Wu identified an activity converting apolipoprotein to mature lipoprotein and
  found that it was "enriched in the inner membrane and in the inner
  membrane/outer membrane mixed fractions of the E. coli cell envelope"
  [PMID:2032623].
- Its terminal lipoprotein-maturation reaction transfers a phospholipid acyl
  chain to the N-terminal diacylglyceryl-modified cysteine of apolipoprotein.
  Hillmann et al. report that purified E. coli Lnt "was fully active, as judged
  by its ability to form a stable thioester acyl-enzyme intermediate and
  N-acylate the apo-form of the murein lipoprotein Lpp in vitro"
  [PMID:21676878].
- GO lacks a specific valid molecular-function term for EC 2.3.1.269
  apolipoprotein N-acyltransferase, so `GO:0016747 acyltransferase activity,
  transferring groups other than amino-acyl groups` is retained as the best
  current parent and a term request is proposed.
- The two `GO:0005515 protein binding` rows trace to high-throughput physical
  interaction studies [PMID:15690043; PMID:24561554]. Those rows should not be
  read as false interactions, but they also do not describe Lnt's catalytic
  N-acyltransferase activity.
