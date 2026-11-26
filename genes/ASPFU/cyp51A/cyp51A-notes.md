# cyp51A notes

## 2026-11-21

- Reviewed the fetched GOA rows against the local PTHR24304 PAINT cache. The
  fungal `GO:0006696` IBA on `PANTHER:PTN001209323` is appropriate for this
  intact *Aspergillus fumigatus* CYP51 paralog; the deep P450
  `GO:0016491` oxidoreductase IBA is biologically true but less informative
  than `GO:0008398`.
- Read the cached PMID:15215142 text supporting the original cyp51A/cyp51B
  assignments and the Cyp51A M220 azole-resistance substitutions. Later azole
  papers mainly refine resistance alleles and regulation, so they do not change
  the core sterol 14-demethylase and ergosterol-biosynthesis call.
- Synchronized UniProt's experimentally supported cyp51A catalytic and pathway
  comments while addressing PR review: the lanosterol and eburicol reaction
  lines name PMID:18191972, PMID:26459890, and PMID:29439966, and the pathway
  and disruption-phenotype lines name PMID:18191972. The GOA snapshot still has
  no direct IDA row for `GO:0008398` or `GO:0006696` on cyp51A despite those
  experimentally traced UniProt assertions.
