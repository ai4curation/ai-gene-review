# glc-4 curation notes

## 2026-11-22

- Ran `just fetch-gene worm glc-4`, which resolved UniProtKB:Q95QT7
  (`WBGene00001594`) and seeded 12 GOA rows. The PTHR18945 family data already
  existed locally and was not refreshed.
- Ran `just mod-description-deep-research worm glc-4` to cache the WormBase
  brief gene description, and `just paint-losses worm glc-4`, which found no
  IRD or IKR loss on the Q95QT7 lineage.
- Ran `just fetch-gene-pmids worm glc-4`; the seeded review only cited
  GO_REFs, so no PMIDs were fetched and no existing publication files were
  refreshed.
- Attempted `just deep-research-falcon worm glc-4 --fallback perplexity-lite`,
  but both configured providers were unavailable in this environment
  (`agentapi` was missing and the wrapper reported only `claude_code` as
  available). No provider deep-research file was written.
- PMID:37811674 is full text in the local cache and is the key direct native
  source. Li et al. showed that `glc-2` and `glc-4` reporters are expressed in
  enteric and anal depressor muscles, that loss of either `glc-2` or `glc-4`
  suppresses the `ubr-1` elevated-glutamate expulsion and enteric-muscle
  calcium defects, and that exogenous glutamate fails to inhibit enteric-muscle
  calcium activity in the `glc-2; glc-4` double mutant.
- No cached source directly assays GLC-4 homomers or a purified GLC-2/GLC-4
  complex. This review therefore adds GLC-4 as contributing to a native
  extracellularly glutamate-gated chloride channel, not as independently
  enabling homomeric GluCl activity.
- The WormBase brief description is useful recall support for a predicted GluCl
  and for older ivermectin, reversal-behavior and `avr-14` genetic-interaction
  leads. It is uncited and does not mention the Li et al. enteric-muscle
  result, so the review marks it UNVERIFIED and grounds the core function in
  Li et al., UniProt domain architecture and the local PTHR18945 review.
