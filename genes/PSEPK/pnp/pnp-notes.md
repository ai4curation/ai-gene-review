# pnp curation notes

## 2026-08-31

PNPase is curated as a processive 3'-to-5' phosphorolytic exoribonuclease. Its
GO:0000175 annotation describes direction and exonucleolytic mode, while
GO:0004654 captures the defining phosphate-dependent chemistry; the former is
therefore retained as non-core and the latter as core. Full-text
biochemical work establishes an active RhlB-PNPase complex
[PMID:16275923 "PNPase-alpha and RhlB form a ribonucleolytically active
complex"]. This is homologous mechanistic support; direct KT2440 complex
composition remains to be tested.

The species-aware OpenScientist report identifies RNase R as a possible
alternative or additional pseudomonad degradosome exonuclease. PNPase remains
well supported as a KT2440 phosphorolytic exoribonuclease, but the review does
not treat presence as proof of obligate complex membership.

The nested localization annotations are normalized by accepting the more
specific cytosol term and retaining cytoplasm as non-core.

The direct KT2440 study does not establish the catalytic mechanism, but it does
show that a `pnp` deletion is viable without the E. coli-like cold-sensitive
phenotype and that cold-shock transcription differs between the species
[PMID:12923102 "We identified the PNPase-encoding gene (pnp) of Pseudomonas
putida and constructed deletion mutants that did not exhibit cold sensitivity."].

## 2026-09-01 wave134 annotation-reviewer pass

All ten seeded GOA rows were rechecked. The specific phosphorolytic
exoribonuclease activity, RNA binding, Mg2+ binding, RNA/mRNA catabolism, and
cytosolic localization remain accepted; broader parent terms remain non-core.
The review retains direct KT2440 evidence for `pnp` physiology and homologous
evidence for RhlB coupling without asserting a purified KT2440 complex.
Same-genus PMID:40096066 directly maps PNPase binding to the P. aeruginosa
RNase E scaffold and sharpens, but does not remove, that KT2440-specific hedge.
