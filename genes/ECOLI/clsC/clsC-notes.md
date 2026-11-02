# clsC curation notes

`just fetch-gene ECOLI clsC` succeeded in this worktree on 2026-10-02 and
seeded 11 GOA rows. PMID caching also succeeded for the two experimental
references. The Falcon deep-research provider and `perplexity-lite` fallback
were unavailable because no provider API keys were configured, and
`just fetch-fitness ECOLI clsC` could not reach FEBA or find a local FEBA
database, so this review uses the cached publications, UniProt, the existing
cardiolipin module, and PAINT files.

Tan et al. established that `ymdC`, renamed `clsC`, encodes the third E. coli
cardiolipin synthase. The `clsABC` triple deletion lacked detectable
cardiolipin, plasmid expression of `clsC` alone produced little cardiolipin,
and coexpression of `ymdB-clsC` restored a high cardiolipin level
[PMID:22988102, "fully complemented BKT22 with a high level of CL"].

ClsC is not the ordinary ClsA/ClsB phosphatidylglycerol-plus-phosphatidylglycerol
synthase. The YmdB-ClsC membrane fraction formed cardiolipin with
phosphatidylglycerol plus phosphatidylethanolamine and not with the other
tested substrate combinations [PMID:22988102, "The absence of signal with other
combinations of exogenous phospholipids indicates that CL synthesis was
dependent on ClsC with PG and PE as cosubstrates."]. His130Ala or His369Ala
substitutions in the two PLD HKD motifs eliminated cardiolipin production
[PMID:22988102, "Mutation of the putative catalytic motif of ClsC prevents CL
formation."].

The PTHR21248 PAINT node `PTN000478698` currently transfers both
`GO:0032049 cardiolipin biosynthetic process` and `GO:0008808 cardiolipin
synthase activity` to ClsC. The process transfer is correct, but
`GO:0008808` is the two-phosphatidylglycerol reaction and should be replaced by
`GO:0090483 phosphatidylglycerol-phosphatidylethanolamine phosphatidyltransferase
activity` for ClsC.

PMID:39842605 is abstract-only locally. Its abstract reports that ClsC
stimulates RNase III-dependent cleavage in vivo and in vitro and interacts with
RNase III, supporting EcoCyc's `GO:0050685 positive regulation of mRNA
processing` annotation as a non-core regulatory role, but the full text is
needed before making finer claims about direct RNA targets or the relationship
between RNase III activation and cardiolipin synthesis.
