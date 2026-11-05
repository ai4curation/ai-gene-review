# Curation notes: *Escherichia coli* K-12 fadE (Q47146, b0221, formerly yafH)

Reviewed as the E. coli exemplar of the acyl-CoA dehydrogenase step in
`modules/bacterial_fatty_acid_beta_oxidation.yaml`.

## Sources

- No provider deep-research report was generated for this gene in this session;
  the review rests on the reviewed UniProt entry and the cached GOA-cited
  publications. No `-deep-research-*.md` file exists for it.
- PMID:12057976 (Campbell & Cronan 2002) and PMID:334745 are abstract-only in
  the cache; PMID:4928881 is title-only.

## Decisions

- Core functions: GO:0004466 long-chain and GO:0070991 medium-chain fatty
  acyl-CoA dehydrogenase activity (UniProt reactions curated from
  PMID:12057976; the mutant fails on C8, C10, C12 and C18:1 fatty acids).
- GO:0003995 acyl-CoA dehydrogenase activity is kept (ACCEPT) on every row:
  it names the reaction class and is the module's term for this step.
- GO:0005737 cytoplasm is accepted. FadE (like Pseudomonas putida FadE) has a
  hydrophobic N-terminal stretch, but UniProt curates no transmembrane segment
  and the activity was recovered in the soluble fraction (PMID:334745).
  Membrane association is left as an open question.
- GO:0016627 and GO:0009062 are TOO_GENERAL.
