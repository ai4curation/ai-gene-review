# ssb curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 5 current GOA rows and reviewed UniProt Q88QK5. Accepted single-stranded DNA binding, DNA replication, and nucleoid localization. Kept DNA repair and recombination as genuine non-core uses of the same SSB activity outside this module boundary. No GOA row remains pending.



## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target Q88QK5 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003697 single-stranded DNA binding: ACCEPT. The SSB family OB-fold architecture and HAMAP MF_00984 support direct ssDNA binding. Pseudomonas replicase reconstitution independently uses purified SSB; no species-specific affinity is transferred.
- GO:0006260 DNA replication: ACCEPT. SSB physically protects exposed replication templates and recruits partners, a structural contribution to replication rather than an indirect necessity-only phenotype.
- GO:0006281 DNA repair: ACCEPT. SSB template protection and partner recruitment are conserved genome-maintenance functions also used in repair. Repair is a central SSB function, not peripheral merely because this module emphasizes replication.
- GO:0006310 DNA recombination: ACCEPT. The target HAMAP functional statement includes recombination. ssDNA stabilization and recruitment of recombination factors are part of the same conserved SSB activity; no recombinase catalysis is assigned.
- GO:0009295 nucleoid: ACCEPT. SSB associates with exposed chromosome ssDNA in the nucleoid. This synthesis localization is consistent with its conserved chromosome-maintenance role; no membrane or nuclear localization is inferred.

Primary sources used: . Independent frozen support: file:PSEPK/ssb/ssb-uniprot.txt.
