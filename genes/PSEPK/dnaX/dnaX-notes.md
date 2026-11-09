# dnaX curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 8 current GOA rows, UniProt Q88F30, and its AAA+ clamp-loader and polymerase-III coupling domains. Accepted ATP binding, DNA replication, DNA-templated replication, and polymerase III complex membership; retained generic DNA binding as non-core. Removed DNA polymerase activities because catalysis belongs to DnaE, and marked broad DNA biosynthesis as over-annotated. Added a contributes_to assertion for DNA clamp loader activity because DnaX supplies the ATPase component but the complete activity requires the multisubunit loader. This is grounded in the target UniProt SUBUNIT statement that the gamma complex contains gamma, delta, delta-prime, psi, and chi, rather than in the InterPro family-name cross-reference. No seeded GOA row remains pending.


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target Q88F30 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003677 DNA binding: ACCEPT. DnaX engages primed DNA within the ATP-dependent loader. DNA recognition is part of its core mechanism, not peripheral because the loader activity is more informative; the claim is based on conserved loader architecture.
- GO:0003887 DNA-directed DNA polymerase activity: REMOVE. DnaX supplies the ATPase/organizing component of the loader. In Pseudomonas reconstitution the alpha-epsilon complex supplies DNA synthesis and tau3-delta-delta-prime supplies clamp-loading support; assigning the polymerase catalytic reaction to DnaX is erroneous.
- GO:0005524 ATP binding: ACCEPT. The conserved DnaX AAA+ domain binds ATP to support clamp-loader conformational cycling.
- GO:0006260 DNA replication: MODIFY. DnaX supports DNA-templated chromosome replication; refine to the specific descendant GO0006261 already present.
- GO:0006261 DNA-templated DNA replication: ACCEPT. DnaX directly contributes ATP-dependent clamp loading and couples polymerase cores during chromosome copying. It is a working component of replication, not merely a required upstream regulator.
- GO:0009360 DNA polymerase III complex: ACCEPT. DnaX is a component of the polymerase III clamp-loader assembly. Pseudomonas reconstitution corroborates the conserved subassembly, without proving the exact KT2440 holoenzyme stoichiometry.
- GO:0034061 DNA polymerase activity: REMOVE. DnaX has no DNA-polymerizing catalytic role; the polymerase III alpha subunit supplies this chemistry.
- GO:0071897 DNA biosynthetic process: ACCEPT. DnaX contributes the ATP-driven clamp-loading step on which processive DNA synthesis depends. This is direct machinery participation, not polymerase catalysis. Current ontology does not make DNA replication a descendant of GO0071897, so no unsupported refinement is made.
- GO:0003689 DNA clamp loader activity: NEW. Retain the inherited proposal and its original payload. Pseudomonas reconstitution demonstrates the tau3-delta-delta-prime loader as a required unit for efficient elongation. DnaX contributes ATP-dependent conformational work, while the other loader subunits are also required; the inherited contributes_to qualifier is appropriate. No isolated-DnaX loading or universal gamma isoform is asserted.

Primary sources used: PMID:15611049. Independent frozen support: file:PSEPK/dnaX/dnaX-uniprot.txt.


## PR #6117 round-1 follow-up (2026-11-06)

- Record UNIPROT WRONG_TERM for GO:0003887 (InterPro:IPR012763|InterPro:IPR021029|InterPro:IPR022754|EC:2.7.7.7); original action remains REMOVE.

All historical annotation payloads, inherited NEW proposals, and frozen raw/provider files are preserved. Source confidence distinguishes direct target assays from comparative Pseudomonas evidence. No publication cache was refreshed.
