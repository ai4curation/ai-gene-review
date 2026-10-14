# sos-1 notes

## 2026-09-30 annotation review

Provider deep research was unavailable: Falcon requires `agentapi` on `PATH`,
and the Perplexity/OpenAI fallbacks were unavailable without API keys. This
focused pass reviewed the GOA-seeded `sos-1-ai-review.yaml` against the local
UniProt record, cached PMIDs, and local GO-CAM/Reactome caches when present; no
`sos-1-deep-research-*.md` file was created.

SOS-1 is the C. elegans Son of sevenless RasGEF encoded by `let-341`. The core
rows are its guanyl-nucleotide exchange factor activity, activity in Ras/small
GTPase signal transduction, regulated plasma-membrane activity, and
participation in LET-23/EGFR signaling upstream of LET-60/Ras. Female gamete
generation, sex myoblast migration, and vulval development were kept as
supported nematode developmental outputs rather than the reusable RasGEF
function itself. The abstract-only LGV embryonic-development row remains
`UNDECIDED`, and the InterPro histone-fold protein-heterodimerization transfer
was removed as unsupported for SOS-1.
