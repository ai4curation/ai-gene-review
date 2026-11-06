# ant-1 curation notes

Automated deep research was attempted with
`just deep-research-falcon NEUCR ant-1 --fallback perplexity-lite`, but Falcon
was not available in this runner and the Perplexity fallback was unavailable as
well. The review therefore uses the local UniProt record, the local PTHR32379
PAINT slice, cached Neurospora PRMT literature, and manual web searches for
`ant-1`, `NCU08111`, `Q7SCW9`, and RMT2/arginine methyltransferase papers.

The GOA seed is entirely homology-based: PTHR32379 PAINT rows for nucleus,
cytoplasm, and protein arginine N5-methyltransferase activity; UniProt SubCell
mappings for inferred nucleus/cytoplasm; manual ISS transfers from budding-yeast
Q03305; and the InterPro2GO mapping from RMT2-family `IPR017408` to broad
`GO:0016274`.

The official PANTHER family name for `PTHR32379` is GUANIDINOACETATE
N-METHYLTRANSFERASE, but the local PAINT table separates the vertebrate GAMT
branch from the fungal Rmt2 branch. `PANTHER:PTN001285370`, not the vertebrate
`PANTHER:PTN001285367` node, is the relevant ant-1 node for
`GO:0019702` protein arginine N5-methyltransferase activity.

Manual web searches on 2026-11-06 did not find a direct ant-1/NCU08111
biochemical or deletion paper. The relevant Neurospora PRMT genetics paper is
PMID:24260473; it experimentally studied the type I/II PRMTs amt-1, amt-3 and
skb-1, while mentioning NCU08111 only as a putative type IV PRMT whose enzymatic
properties had not been determined. The paper also notes that inactivating the
F. graminearum homolog had no observable phenotype; that cautions against
transferring cellular phenotypes to ant-1, although it does not argue against
the fungal-node protein arginine N5-methyltransferase activity because
NCU08111/Q7SCW9 carries the RMT2/SAM_RMT2 domain signatures rather than the
classical type I/II PRMT domains studied in that paper. NCBI Gene and commercial
ORF/protein pages repeat the Rmt2 assignment but do not provide experimental
ant-1 evidence.

I therefore did not add Neurospora-specific biological-process rows. Direct
tests of Rpl12 arginine methylation, ribosome biogenesis, or translational
fidelity in an ant-1 deletion strain are still needed.
