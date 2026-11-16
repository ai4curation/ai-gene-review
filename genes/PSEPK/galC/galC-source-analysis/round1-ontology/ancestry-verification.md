# Gallate process ancestry and activity definitions, 2026-11-07

Official QuickGO term and ancestor endpoints were queried independently. `GO_0019396-ancestors.json` requests only `is_a,part_of` relationships and includes all three of GO:0019336, GO:0042537 and GO:0072329. Separate term and ancestor snapshots for these candidate parents are retained with URL, retrieval time and SHA256 provenance.

Verified findings:

- GO:0019396 gallate catabolic process is an is_a/part_of descendant of GO:0019336 phenol-containing compound catabolic process.
- GO:0019396 gallate catabolic process is an is_a/part_of descendant of GO:0042537 benzene-containing compound metabolic process.
- GO:0019396 gallate catabolic process is an is_a/part_of descendant of GO:0072329 monocarboxylic acid catabolic process.
- GO:0047443 defines both HMG cleavage and the exact CHA-to-oxaloacetate-plus-pyruvate reaction; its short HMG label does not exhaust its definition.

Thus all three GalC process changes are hierarchical refinements, not lateral corrections. GalC performs a downstream reaction in the gallate pathway; its immediate substrate need not retain gallate's aromatic ring or single carboxyl group. Independent definitions for the keto-enol, C=C-transposition and hydro-lyase genera are also preserved here for the related GalD/LigU/LigJ core review.
