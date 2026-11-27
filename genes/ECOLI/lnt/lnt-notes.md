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


## 2026-11-07 source and ontology audit

Reviewed all original rows, references and core activity. Original annotation payloads/order and historical NEW actions are preserved; no row was added or retired. See `analysis/module_audits/bacterial_lipoprotein_maturation/ecoli-bacsu-consultation/evidence.md` for the complete source/construct and ontology rationale. All genuine Falcon attempts returned authentication HTTP403; manual synthesis is recorded here without creating provider output. Final PAINT lineage inspection reported no IRD/IKR loss; initial cold-cache download races were retried sequentially and logged. Protected publication/provider/raw files remain unchanged.

Replaced protein-name/EC-label support with measured phospholipid-dependent N-acylation. GO:0140186 is lysine-N6/acyl-CoA chemistry and is not a replacement. Retained actual periplasmic catalytic-domain location alongside membrane insertion, without asserting a soluble enzyme.
