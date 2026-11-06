# holB review notes


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target Q88LG7 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003677 DNA binding: UNDECIDED. The delta-prime structural subunit belongs to a DNA-engaging clamp-loader complex, but the retrieved Pseudomonas reconstitution does not establish direct DNA binding by isolated HolB. Complex DNA engagement alone cannot resolve this individual MF; preserve uncertainty.
- GO:0003887 DNA-directed DNA polymerase activity: REMOVE. HolB is delta-prime, a structural clamp-loader subunit. Polymerization is supplied by DnaE/alpha, and the complex-wide ARBA/EC mapping is not valid for isolated HolB.
- GO:0006260 DNA replication: MODIFY. The direct machinery role lies in DNA-templated replication, a descendant already present.
- GO:0006261 DNA-templated DNA replication: ACCEPT. HolB organizes the multisubunit clamp loader that enables processive copying of the chromosome; it performs structural work rather than merely being required indirectly.
- GO:0008408 3'-5' exonuclease activity: REMOVE. The proofreading exonuclease belongs to DnaQ/epsilon, not the delta-prime loader scaffold. HolB domain architecture and the separate catalytic alpha-epsilon assembly contradict this individual nuclease assignment.
- GO:0009360 DNA polymerase III complex: ACCEPT. The delta-prime subunit is part of the polymerase III clamp loader, supported by target HolB domains and the Pseudomonas tau3-delta-delta-prime reconstitution.
- GO:0034061 DNA polymerase activity: REMOVE. HolB supplies structural loader function, not polymerase chemistry; the catalytic alpha subunit performs nucleotide addition.
- GO:0071897 DNA biosynthetic process: ACCEPT. HolB contributes the clamp-loading scaffold that enables processive DNA production. This supports biosynthetic machinery participation despite the erroneous accompanying polymerase MF; no claim of isolated HolB catalysis is made.

Primary sources used: PMID:15611049. Independent frozen support: file:PSEPK/holB/holB-uniprot.txt.


## PR #6117 round-1 follow-up (2026-11-06)

- Record UNIPROT WRONG_TERM for GO:0003887 (InterPro:IPR004622|InterPro:IPR015199|EC:2.7.7.7); original action remains REMOVE.
- Record INTERPRO WRONG_TERM for GO:0008408 (InterPro:IPR004622); original action remains REMOVE.

All historical annotation payloads, inherited NEW proposals, and frozen raw/provider files are preserved. Source confidence distinguishes direct target assays from comparative Pseudomonas evidence. No publication cache was refreshed.
