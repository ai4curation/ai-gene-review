# rmt2 curation notes

Automated deep research was attempted with
`just deep-research EMENI rmt2 --provider falcon --fallback perplexity-lite`,
but Falcon was not available in this runner and the Perplexity fallback was
unavailable as well. This review therefore uses the local UniProt record, the
local PTHR32379 PAINT slice, the S. cerevisiae RMT2 biochemical seed paper,
PubMed searches, and manual web searches for `AN6072`, `Q5B058`, and
A. nidulans `rmt2`.

Q5B058 is the A. nidulans member of `PTHR32379`. The official PANTHER family
name is GUANIDINOACETATE N-METHYLTRANSFERASE, but PAINT separates the fungal
Rmt2 node from the vertebrate GAMT node. `PANTHER:PTN001285370` carries
`GO:0019702` protein arginine N5-methyltransferase activity from the
experimentally characterized S. cerevisiae RMT2 seed; the vertebrate
`PANTHER:PTN001285367` node carries guanidinoacetate N-methyltransferase
activity and creatine biosynthesis.

No direct A. nidulans rmt2 biochemical or genetics paper turned up in PubMed for
`AN6072`, `Q5B058`, or Aspergillus `rmt2`. Web search on 2026-11-06 likewise
found product/catalog records and broader PRMT literature rather than direct
functional evidence for Q5B058. The review therefore treats protein arginine
N5-methyltransferase activity as the inherited fungal core activity and leaves
the precise Aspergillus Rpl12 substrate and ribosome phenotypes as questions.
