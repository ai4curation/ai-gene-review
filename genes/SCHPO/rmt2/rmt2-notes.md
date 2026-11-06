# rmt2 curation notes

Automated deep research was attempted with
`just deep-research-falcon SCHPO rmt2 --fallback perplexity-lite`, but Falcon was
not available in this runner and the Perplexity fallback was unavailable as well.
This review therefore uses the cached PomBase GOA paper, the local UniProt
record, the local PTHR32379 PAINT slice, and manual web searches for
`SPAC26A3.17c`/`rmt2` literature.

rmt2 is the fission-yeast member of `PTHR32379`. The official PANTHER family
name is GUANIDINOACETATE N-METHYLTRANSFERASE, but the PAINT table splits the
family into a fungal Rmt2 branch and a vertebrate GAMT branch. The fungal
`PANTHER:PTN001285370` node carries `GO:0019702` protein arginine
N5-methyltransferase activity from the experimentally characterized
S. cerevisiae seed. Chern et al. 2002 directly purified budding-yeast Rmt2,
used SAM to methylate ribosomal protein L12, and mapped the methyl-acceptor site
to Arg67, grounding that seed. The vertebrate `PANTHER:PTN001285367` node
carries guanidinoacetate N-methyltransferase activity and creatine
biosynthesis; those terms should not propagate to fungal rmt2.

PomBase and UniProt give rmt2 nuclear/cytoplasmic localization from the 2006
fission-yeast ORFeome YFP localization screen, and the 2026-05-29 PAINT
cytoplasm IBA at `PTN001282244` is even seeded by PomBase:SPAC26A3.17c itself.
Per the IBA project guidance, this is legitimate descendant experimental
support for the node rather than circular support.

The only fission-yeast Rpl12 methylation paper I found in targeted web searches
was PMID:18195021, which directly studies the Set11 methyltransferase and maps a
Set11-dependent Rpl12 lysine mark. Full-text search snippets mention
SPAC26A3.17c as the likely Rmt2 homolog for the arginine mark, but the cached
abstract does not assay rmt2 directly. I therefore used PMID:18195021 only as
background and did not add a direct Rpl12 process or substrate assertion.

UniProt cross-references Q10170 to Reactome `R-SPO-71288` for creatine
metabolism, inferred from human GAMT. I did not use that here: the local PAINT
snapshot already marks guanidinoacetate methyltransferase activity and creatine
biosynthesis as vertebrate PTN001285367 functions separate from the fungal Rmt2
GO:0019702 branch.
