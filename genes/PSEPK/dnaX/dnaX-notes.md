# dnaX curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 8 current GOA rows, UniProt Q88F30, and its AAA+ clamp-loader and polymerase-III coupling domains. Accepted ATP binding, DNA replication, DNA-templated replication, and polymerase III complex membership; retained generic DNA binding as non-core. Removed DNA polymerase activities because catalysis belongs to DnaE, and marked broad DNA biosynthesis as over-annotated. Added a contributes_to assertion for DNA clamp loader activity because DnaX supplies the ATPase component but the complete activity requires the multisubunit loader. This is grounded in the target UniProt SUBUNIT statement that the gamma complex contains gamma, delta, delta-prime, psi, and chi, rather than in the InterPro family-name cross-reference. No seeded GOA row remains pending.
