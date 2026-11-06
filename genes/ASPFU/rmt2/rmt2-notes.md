# rmt2 curation notes

Automated deep research was attempted with
`just deep-research-falcon ASPFU rmt2 --fallback perplexity-lite`, but Falcon was
not available in this runner and the Perplexity fallback was unavailable as well.
This review therefore uses the local UniProt record, the local PTHR32379 PAINT
slice, the S. cerevisiae RMT2 biochemical seed paper, PubMed searches, and
manual web searches for `AFUA_2G09080`, `Q4X1R1`, and A. fumigatus `rmt2`.

AFUA_2G09080/Q4X1R1 is the A. fumigatus member of `PTHR32379`. The official
PANTHER family name is GUANIDINOACETATE N-METHYLTRANSFERASE, but PAINT separates
the fungal Rmt2 node from the vertebrate GAMT node. `PANTHER:PTN001285370`
carries `GO:0019702` protein arginine N5-methyltransferase activity from the
experimentally characterized S. cerevisiae RMT2 seed; the vertebrate
`PANTHER:PTN001285367` node carries guanidinoacetate N-methyltransferase
activity and creatine biosynthesis.

No direct A. fumigatus rmt2 biochemical or genetics paper turned up in PubMed
for `Afu2g09080`, `Q4X1R1`, `AFUA_2G09080`, or Aspergillus `rmt2`. Web search
on 2026-11-06 likewise found product and genome-catalog records for
AFUA_2G09080 rather than direct functional literature. The review therefore
treats protein arginine N5-methyltransferase activity as the inherited fungal
core activity and leaves the precise Aspergillus Rpl12 substrate and ribosome
phenotypes as questions.
