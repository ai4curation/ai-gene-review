# Curation notes: *Escherichia coli* K-12 fadB (P21177, b3846)

Reviewed as the E. coli exemplar of the hydratase and dehydrogenase steps in
`modules/bacterial_fatty_acid_beta_oxidation.yaml`.

## Sources

- No provider deep-research report was generated for this gene in this session;
  the review rests on the reviewed UniProt entry and the cached GOA-cited
  publications (all abstract-only: PMID:368024, PMID:3286611, PMID:6402028,
  PMID:8454629, PMID:8755745), plus PMID:334745 for the soluble localization.
  No `-deep-research-*.md` file exists for it.

## Decisions

- Core functions: GO:0004300 enoyl-CoA hydratase (G116F abolishes it),
  GO:0003857 (3S)-3-hydroxyacyl-CoA dehydrogenase (His450 catalytic; fadB64
  mutant), and GO:0004165 delta3-delta2-enoyl-CoA isomerase (auxiliary step for
  unsaturated substrates, but a genuine FadB activity).
- GO:0016509 (long-chain, IBA) and GO:0018812 (the (2E)-specific child of
  GO:0004300, Rhea) are accepted as specific forms of the core activities.
- GO:0008692 3-hydroxybutyryl-CoA epimerase is KEEP_AS_NON_CORE: PMID:8454629
  shows it is a dehydration/rehydration by-product of the crotonase site.
- Generic parents (catalytic, oxidoreductase, lyase, lipid and fatty acid
  metabolic/catabolic process) are TOO_GENERAL.
