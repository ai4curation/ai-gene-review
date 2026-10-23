# Dsor1 review notes

## 2026-09-30 annotation review

Provider deep research was unavailable: Falcon requires `agentapi` on `PATH`,
and the configured API-key fallbacks were not available. This pass therefore
used the seeded UniProt/GOA review, `Dsor1-uniprot.txt`, cached publications,
cached Reactome entries, and the local Drosophila Spi/Egfr and Torso GO-CAM
models.

Reviewed all 62 seeded GOA rows. The core biology is Dsor1/MEK MAP kinase
kinase activity between Raf and rolled/ERK in the conserved Ras/Raf/MEK/ERK
cascade. Receptor-specific EGFR, Torso, Sevenless, Breathless/FGFR, Pvr, and
insulin outputs were kept as non-core where the cached evidence supported the
Dsor1 or MAPK cascade role. Generic kinase and Raf/KSR binding rows were
modified to MAP kinase kinase activity, MAPKKK binding, or scaffold protein
binding. Four Reactome TAS cytosol rows were removed because the cited events
are PKA or CK2 phosphorylation reactions in Hedgehog/circadian pathways rather
than Dsor1 events.
