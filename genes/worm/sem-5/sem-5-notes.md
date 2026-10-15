# sem-5 notes

## 2026-09-30 annotation review

Provider deep research was unavailable for this pass: Falcon could not run without
`agentapi` on `PATH`, and the Perplexity/OpenAI fallback providers were unavailable
because API keys were not configured.

This review used the UniProt P29355 record, the GOA-seeded
`sem-5-ai-review.yaml` file, the cached PMID records for all six GOA-cited
papers, and local pathway caches. No local GO-CAM entry for `WBGene00004774`
and no sem-5-specific C. elegans Reactome summary were present, so the pathway
interpretation rests on the direct WormBase literature rows and the PAINT
GRB2/Sem-5/Drk family annotations.

All 23 seeded rows were reviewed. The core picture is SEM-5 as a conserved
SH2/SH3 adaptor that binds activated RTKs through the SH2 domain, binds
proline-rich partners through SH3 domains, and couples LET-23/EGFR-like and
other RTK inputs to downstream Ras/MAPK signaling. Vulval induction, sex
myoblast migration, male spicule fate specification, and EGL-15/FGFR-dependent
body-wall-muscle membrane regulation were kept as real but context-specific
developmental outputs.
