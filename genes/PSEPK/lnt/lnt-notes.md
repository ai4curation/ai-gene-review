# lnt consultation notes

## 2026-11-07 — source-qualified KT2440 review

Reviewed all original annotations and the core function against frozen UniProt/HAMAP features, genuine existing OpenScientist research and the primary sources summarized in [the consultation evidence](../../../analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation/evidence.md). Provider files and source payloads remain unchanged. No direct KT2440 biochemical assay or essentiality result was located in the consulted sources; experimental statements from E. coli/P. aeruginosa retain their species scope.

[PMID:21676878, "strongly affected by the phospholipid headgroup and acyl chain composition."] Full E. coli kinetic Results support phospholipid donation, including non-PE donors; no exclusive PE requirement is imposed on KT2440. [PMID:28675161, "The active site resides above the membrane interface"] Full ortholog structures place catalysis on the periplasmic face of an integral membrane enzyme. Independent sequence mapping supports the E269/K329/C381 triad and four additional sites. GO0016410 obsolescence was verified; GO0140186 uses acyl-CoA and lysine-N6 and is not an appropriate replacement. Existing actions remain unchanged.

PAINT-loss tooling could not inspect a target lineage because the accession is absent from its cached family tree. No verified loss-free ancestry or invented PTN is claimed. Conserved enzyme work supports the biosynthetic process; necessity alone and pathway-neighbor annotations are not used as participation evidence.
