# MAGI1 review notes

## 2026-07-18

- Initialized human MAGI1 (UniProt Q96QZ7) with `just fetch-gene human MAGI1`.
  QuickGO returned 406 rows, collapsed by the seeding workflow into 43 review
  groups. No NOT-qualified or isoform-qualified GOA rows were present.
- Cached all 21 PMIDs cited by the seeded review. Added and cached primary
  functional papers PMID:12042308, PMID:21123374, and PMID:21666716 to support
  alpha-actinin binding, junction integrity, and junction/adhesion function.
- `just deep-research-falcon human MAGI1 --fallback perplexity-lite` failed:
  Falcon/Edison returned HTTP 402 Payment Required and Perplexity returned HTTP
  401 insufficient quota. Per repository policy, no `-deep-research-{provider}`
  file was fabricated; manual research is recorded in
  `MAGI1-deep-research-manual.md`.
- Curation decision: MAGI1 is primarily a multivalent junctional molecular
  adaptor/scaffold. Generic `protein binding` entries are not treated as its
  defining molecular function. Direct, gene-specific junctional localization
  and adhesion annotations are retained; older S-SCAM/MAGI or supplementary-only
  interactions remain conservative where exact evidence cannot be verified.
- Functional replacement/new annotations proposed from direct evidence:
  GO:0060090 molecular adaptor activity (replacement for generic protein binding),
  GO:0070830 bicellular tight junction assembly, and GO:0005634 nucleus (the latter
  as a non-core experimentally observed location).
