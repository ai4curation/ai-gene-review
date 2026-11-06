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
- GO:0008692 3-hydroxybutyryl-CoA epimerase is KEEP_AS_NON_CORE: through
  dehydration/rehydration at the crotonase site (PMID:8454629) FadB lets
  D-3-hydroxyacyl-CoA enter the spiral, and UniProt records from experiment
  that FadB uses D-3-hydroxyacyl-CoA as a substrate. It is non-core because
  the main spiral runs through the L isomer. (PR #5935 review: the earlier
  "by-product" argument was replaced, as sharing an active site does not
  decide whether an activity is kept.)
- The GO:0004300 IEA row is sourced from Rhea 20724, the (3E) hydration, and
  now quotes that reaction; GO:0018812 (Rhea 16105, (2E) only) is an is_a child
  of GO:0004300, which stays the core term because it covers both reactions.
- Generic parents (catalytic, oxidoreductase, lyase, lipid and fatty acid
  metabolic/catabolic process) are TOO_GENERAL.
