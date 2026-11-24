# cyp51B notes

## 2026-11-21

- Reviewed the fetched GOA rows against the local PTHR24304 PAINT cache. cyp51B
  inherits the same fungal `GO:0006696` IBA on `PANTHER:PTN001209323` as cyp51A,
  with UniProt/Rhea support for sterol 14-demethylase activity.
- Read the cached PMID:15215142 text, which supports the existence of the two
  A. fumigatus 14-alpha sterol demethylase genes and establishes Cyp51A-focused
  triazole resistance. No cached or newer literature found in this tranche
  supported splitting cyp51B away from the conserved fungal CYP51 activity.
- Synchronized UniProt's experimentally supported cyp51B catalytic and pathway
  comments while addressing PR review: the lanosterol reaction names
  PMID:18191972, PMID:26269599, PMID:26459890, and PMID:29439966; the eburicol
  and kinetic lines name PMID:26269599; and the disruption-phenotype line names
  PMID:18191972. The GOA snapshot still has no direct experimental row for
  `GO:0008398` or `GO:0006696` on cyp51B despite those experimentally traced
  UniProt assertions.
