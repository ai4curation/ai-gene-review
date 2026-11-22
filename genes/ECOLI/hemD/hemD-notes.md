# hemD (P09126) notes, Escherichia coli K-12

## Sources and deep research

- Deep research was not available: the one attempted provider run for this batch
  (`just deep-research ECOLI hemA --provider perplexity`, 2026-11-10) failed with a missing
  template error ("All providers failed"). No deep-research file exists; this review uses
  the UniProt record and the cached abstract of PMID:2557837 (abstract-only).

## Function

- Uroporphyrinogen III synthase (co-synthase) purified from an overproducing strain; monomer
  of Mr 28,000 with Km 5 microM for pre-uroporphyrinogen (hydroxymethylbilane)
  [PMID:2557837 "the Km for the substrate, pre-uroporphyrinogen, is 5 microM"].
- hemD is adjacent to hemC (b3804/b3805).
- Mutant evidence in PMID:387909 groups uroporphyrinogen III cosynthase with decarboxylase
  defects, so it does not specifically implicate hemD; no NEW heme biosynthetic process row
  was added.

## Verdict summary

- GO:0004852 (IBA, IDA, IEA): ACCEPT, core.
- GO:0006780 uroporphyrinogen III biosynthetic process (InterPro2GO): ACCEPT, core process.
- GO:0033014 (InterPro2GO): TOO_GENERAL; GO:0006780 is_a GO:0033014. The P. putida review
  used KEEP_AS_NON_CORE while arguing the term is less precise; TOO_GENERAL matches that
  reasoning.
