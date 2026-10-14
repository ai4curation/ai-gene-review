# Manual deep research: E. coli lspA

Falcon deep research was unavailable in this Orca environment because `agentapi`
was not on `PATH` and provider API keys were not configured. This manual
research note summarizes the cached evidence used for the E. coli `lspA`
review.

`lspA` encodes lipoprotein signal peptidase II, the inner-membrane enzyme that
cleaves the signal peptide from diacylglyceryl-modified prolipoproteins.
Tokunaga et al. characterized E. coli prolipoprotein signal peptidase activity
in vitro, showed that it recognizes glycyl-glyceride cysteine as a cleavage
site, and localized the enzyme activity to the inner cytoplasmic membrane
[PMID:6368552]. Inukai et al. identified apolipoprotein as the intermediate
formed after signal peptide cleavage and before terminal N-acylation
[PMID:6363408].

Topology and sequence studies are consistent with the same inner-membrane
signal peptidase II assignment. The `lsp` sequence encodes a 164-residue
prolipoprotein signal peptidase [PMID:6374664], and Munoa et al. showed with
`lsp-phoA` and `lsp-lacZ` fusions that signal peptidase II spans the cytoplasmic
membrane four times [PMID:1894646].

GO currently has no specific molecular-function term for bacterial lipoprotein
signal peptidase activity. The review therefore accepts or modifies rows to
`GO:0004190 aspartic-type endopeptidase activity`, marks the ancestor process
`GO:0006508 proteolysis` as over-annotated, and proposes both a new lipoprotein
signal peptidase activity term and a missing `GO:0042158 lipoprotein
biosynthetic process` annotation.
