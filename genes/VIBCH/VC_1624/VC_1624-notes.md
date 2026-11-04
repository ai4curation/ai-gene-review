# VC_1624 (Q9KRL3) curation notes

## 2026-11-02 (module curation: bacterial_carboxyspermidine_biosynthesis)

Fetched with `just fetch-gene VIBCH Q9KRL3 --alias VC_1624`. UniProt gives no
gene name, so the ordered locus name is used as the symbol, following other
VIBCH folders (e.g. VC_1087).

Deep research: no gene-level provider deep-research file was generated in this
session. The module-level OpenScientist report
(`modules/bacterial_carboxyspermidine_biosynthesis-deep-research-openscientist.md`)
was used for retrieval; all claims below were checked against the cached
primary paper.

Evidence (full text of PMID:19196710 cached and read):

- Identity of the enzyme: [PMID:19196710 "Both the carboxynorspermidine and sym
  -norspermidine peaks were absent in the ΔVC1624 mutant (result not shown),
  confirming VC1624 as the functional CANSDH"]; complementation restored
  norspermidine.
- Both products depend on it: [PMID:19196710 "Deletion of either VC1624
  (putative CANSDH) or VC1623 (CANSDC) abolished sym -norspermidine and
  spermidine accumulation"].
- Putrescine use in vivo: [PMID:19196710 "when the CANSDH enzyme is in excess,
  it increasingly uses putrescine as a substrate and forms carboxyspermidine,
  which is then converted to spermidine by CANSDC"].
- Phenotype: growth reduced 50-60% and biofilm severely reduced, rescued by
  norspermidine. Biofilm is a downstream effect of the norspermidine signal, so
  no biofilm process annotation is proposed for the enzyme.

Decisions:

- GO:0102143 IEA: ACCEPT (core). The GO definition explicitly includes the
  carboxyspermidine reaction ("Also converts carboxyspermidine to putrescine").
- NEW IMP: GO:0045312 nor-spermidine biosynthetic process and GO:0008295
  spermidine biosynthetic process. The enzyme catalyses the committed
  condensation step, so it does work in both processes.
- No in vitro kinetics exist for VC_1624 itself; recorded as a knowledge gap.
