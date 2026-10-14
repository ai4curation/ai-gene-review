## 2026-09-30 seeded annotation review

Provider deep research was unavailable in the parent environment because Falcon
needed `agentapi` on `PATH`, and the Perplexity/OpenAI fallbacks lacked API
keys. This pass therefore relied on the seeded UniProt and GOA records, cached
PMIDs under `publications/`, and the cached Drosophila Spi/Egfr GO-CAM
(`gocams/60ad85f700001873/60ad85f700001873-src.yaml`).
