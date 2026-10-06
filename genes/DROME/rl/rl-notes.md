# rl notes

## 2026-09-30 annotation review

Provider deep research was unavailable for this pass: Falcon required `agentapi` on
`PATH`, and the Perplexity/OpenAI fallbacks were unavailable because API keys were not
configured. I reviewed the GOA-seeded `rl-ai-review.yaml` against the UniProt record,
cached PMID text, and the local spi/Egfr and Torso GO-CAMs:

- `gocams/60ad85f700001873/60ad85f700001873-src.yaml`
- `gocams/60d5209a00000521/60d5209a00000521-src.yaml`

No `rl-deep-research-*.md` file was created.

The review treats Rolled/ERK-A as the core Drosophila MAP kinase in the
Ras/Raf/Dsor1/ERK cassette. Receptor-specific EGFR, Sevenless, Torso, FGFR,
insulin, and Pvr rows were retained as context-specific non-core pathway uses
unless the cached evidence failed to expose Rolled-specific support. Generic
`protein binding` IPI rows were changed to specific binding terms where the
partners identify the activity: RSK/LK6 protein kinase binding, Capicua
DNA-binding transcription factor binding, and beta-arrestin/Kurtz
arrestin-family protein binding.
