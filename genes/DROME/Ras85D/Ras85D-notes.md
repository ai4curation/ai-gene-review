# Ras85D Notes

## 2026-09-30 Annotation Review

Provider deep research was unavailable for this pass: Falcon required `agentapi` on
`PATH`, and the Perplexity/OpenAI fallbacks did not have API keys in the
environment. This review used the UniProt record, the GOA-seeded review, cached
PMIDs, the local Spi/Egfr and Torso GO-CAMs, and the two local Reactome events
cited by the seeded GOA rows.

Key curation decisions:

- Accepted the core Ras85D small-GTPase, GTP-binding, G-protein switch, plasma
  membrane, Ras/MAPK signaling, Raf-activation, and direct RTK pathway rows.
- Kept the many eye, wing, tracheal, mesodermal, ovarian, hemocyte, lifespan,
  autophagy, growth, and survival annotations as non-core outputs of Ras85D
  signaling.
- Removed uninformative `GO:0005515 protein binding` rows and two stale
  Reactome plasma-membrane rows whose cited events describe CK2 phosphorylation
  of Timeless or Period rather than Ras85D.
- Marked a narrow set of downstream gene-expression and oncogenic
  Malpighian-tubule stem-cell readouts as over-annotated.
