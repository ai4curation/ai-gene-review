# KCR1 (At1g67730; Q8L9C4) review notes

## Identity and function
- Beta-ketoacyl-CoA reductase of the ER FAE; only functional KCR isoform [PMID:19439572 "these results indicate that only AtKCR1 is a functional KCR isoform involved in microsomal fatty acid elongation"].
- Complements yeast ybr159 KCR mutant [PMID:11792704 "Both Ybr159p and an Arabidopsis homologue were shown to restore heterologous elongase activities when expressed in ybr159Delta mutants."]; ybr159 microsomes defective in beta-ketoacyl reduction.
- ER localization of functional YFP-KCR1 [PMID:19439572 "YFP fluorescence labeled a reticulate network typical of the ER"]; dilysine ER retention motif.
- Null kcr1 embryo lethal (globular arrest); RNAi reduces wax and VLCFAs of sphingolipids, seed TAG, root glycerolipids [PMID:19439572 "suppressed KCR activity results in a reduction of cuticular wax load and affects VLCFA composition of sphingolipids, seed triacylglycerols, and root glycerolipids"].
- KCR2 (At1g24470) is inactive in yeast and cannot rescue kcr1.
- Cofactor: paper notes putative NADH-binding site; deep research (file:ARATH/KCR1/KCR1-deep-research-falcon.md) flags NADH vs NADPH preference as unmeasured. GO:0141040 is written with NADP+.

## Decisions
- MODIFY: acetoacetyl-CoA reductase activity (GO:0018454, IMP) -> GO:0141040 very-long-chain 3-oxoacyl-CoA reductase activity.
- ACCEPT: GO:0141040 (EXP, IEA), ketoreductase (IBA, IDA; general but correct - kept consistent across evidence codes), ER/ER membrane, VLCFA biosynthesis (IMP), IEA parents.
- KEEP_AS_NON_CORE: embryo development (IMP).
- MARK_AS_OVER_ANNOTATED: mitochondrion (HDA, co-fractionation).
- REMOVE: chloroplast (ISM), protein binding (IPI, PMID:30604175; uninformative).
- No NEW terms. Considered NEW wax biosynthetic process (RNAi reduces wax) but not added - evidence is supportive but KCR1 is a generic elongase subunit and VLCFA biosynthesis already captures it.
