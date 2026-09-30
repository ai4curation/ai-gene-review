# LepB research notes

LepB is the E. coli type I signal peptidase, an inner-membrane serine-lysine
protease that cleaves N-terminal signal peptides from non-lipoprotein precursor
proteins. Purified leader peptidase from uninfected E. coli membranes catalyzes
leader-peptide cleavage [PMID:6995457 "We now describe a 6,000-fold purification
of a leader peptidase from the membranes of uninfected Escherichia coli"], and
repression of the lepB gene causes precursor accumulation
[PMID:2999144 "When the synthesis of leader peptidase is repressed, protein
precursors accumulate"].

GO:0009003 `signal peptidase activity` is the exact molecular-function endpoint
for LepB. The endopeptidase, serine-type endopeptidase, peptidase, and
serine-type peptidase rows describe true enzyme classes, but are broader than
signal peptidase activity.

LepB participates in protein processing by cleaving signal peptides. Generic
`proteolysis` is broader than this maturation step, and `protein maturation`
should be replaced with the more appropriate GO:0016485 `protein processing`
term already used by curated experimental rows.

The generic LepB `membrane` row should be narrowed to plasma membrane. The
enzyme is membrane-anchored at the bacterial cytoplasmic membrane with its
catalytic domain exposed to the periplasmic side, where exported precursors
emerge for signal-peptide removal.
