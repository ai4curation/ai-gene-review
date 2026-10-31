# GID1C (At5g27320, UniProt Q940G6) curation notes

## Identity
- UniProt Q940G6 GID1C_ARATH "Gibberellin receptor GID1C"; synonyms CXE19, GID1L3; At5g27320. PANTHER PTHR23024:SF492.

## Key findings (with provenance)
- GA binding / GA receptor activity of all three AtGID1s [PMID:16709201 "The GA-binding activities of the three recombinant proteins were confirmed by an in vitro assay"; "These results demonstrate that all three AtGID1s functioned as GA receptors in Arabidopsis"].
- gid1a gid1c is the only dwarf double mutant [PMID:17521411 "The double knockout mutant atgid1a atgid1c showed a dwarf phenotype"].
- Low affinity of GID1C for RGL2 explains failure in stamen development [PMID:19500306 "AtGID1c showed a quite lower affinity to RGL2, the major DELLA protein in floral buds, than AtGID1a or AtGID1b"].
- GID1C expressed in valves and style; gid1a gid1c defective in pod elongation [PMID:24961590 "In summary, GID1A and GID1C are expressed in valves, while GID1A and GID1B are expressed in ovules."].
- GID1ac clade required for germination [PMID:21778177 "GA signalling via the GID1ac receptors is required for Arabidopsis seed germination"].
- Proteolysis-independent DELLA inhibition by GID1 overexpression in sly1 [PMID:18827182 "GA-bound GID1 can block DELLA repressor activity by direct protein-protein interaction with the DELLA domain"].
- Falcon deep research for GID1C timed out (not available).

## Curation decisions
- Same scheme as GID1B: hydrolase REMOVE; NOT response to gibberellin REMOVE (redundancy, contradicted); IGI response to gibberellin with GID1A ACCEPT (validator warns about mixed actions on GO:0009739 because negated and positive rows differ - intentional).
- Core: gibberellin binding (GO:0010331), GA mediated signaling pathway (GO:0010476), nucleus.
