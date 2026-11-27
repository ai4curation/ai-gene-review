# IRF6 notes

## Deep research

`just deep-research-falcon human IRF6 --fallback perplexity-lite` could not run in this workspace: the research client exposed only `claude_code`, while both `falcon` and the `perplexity` provider used by the fallback were unavailable. I did not run a Claude Code deep-research job because this lane is limited to the current Codex writer and no extra sub-workers.

## Manual synthesis

IRF6 is the epithelial-development IRF-family member. The UniProt-reviewed summary describes it as a probable DNA-binding transcriptional activator involved in the keratinocyte proliferation-differentiation switch and mammary epithelial proliferation; unlike IRF1, IRF5, IRF7, or IRF9, it is not an interferon-response factor.

The main human experimental papers show that IRF6 binds SERPINB5/maspin in mammary epithelial cells [PMID:16049006, "Mammary serine protease inhibitor (Maspin) binds directly to interferon regulatory factor 6"], that IRF6 re-expression promotes breast-cancer cell-cycle arrest and cooperates with maspin in a mammary epithelial differentiation model [PMID:18212048, "the reexpression of IRF6 in breast cancer cells results in cell cycle arrest"], and that ChIP-seq with expression profiling after siRNA-mediated IRF6 depletion in primary human keratinocytes identified direct IRF6 targets among cell-cycle, differentiation, adhesion and cell-cell-contact genes [PMID:21807998, "we performed a genome-wide analysis by combining ChIP sequencing for IRF6 binding sites and gene expression profiling in primary human keratinocytes after siRNA-mediated IRF6 depletion"]. High-throughput SELEX also supports a direct sequence-specific double-stranded-DNA binding capacity for human IRF6 [PMID:28473536, "we performed a HT-SELEX"].

I therefore kept the IRF-family DNA-binding and RNAPII transcription rows, kept mammary epithelial differentiation and proliferation outputs as non-core consequences of the epithelial transcriptional program, and marked the family-wide immune-system IBA as over-propagated for this divergent subfamily.
