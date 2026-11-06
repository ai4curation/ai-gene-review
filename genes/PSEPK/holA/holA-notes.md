# holA review notes


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target Q88DM9 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003677 DNA binding: ACCEPT. The conserved delta subunit contacts DNA as part of the clamp-opening/loading assembly. The target-specific support is its HolA domain architecture; purified Pseudomonas tau3-delta-delta-prime provides comparative functional evidence.
- GO:0003887 DNA-directed DNA polymerase activity: REMOVE. HolA is the delta clamp-opening subunit, not the alpha polymerase. The target ARBA reaction is a complex-to-subunit over-propagation contradicted by HolA architecture and the separation of catalytic alpha-epsilon from tau3-delta-delta-prime in Pseudomonas reconstitution.
- GO:0006260 DNA replication: MODIFY. The supported context is DNA-templated chromosome replication, a descendant already present.
- GO:0006261 DNA-templated DNA replication: ACCEPT. HolA performs structural work opening and positioning the sliding clamp during template-dependent DNA replication; this is machinery participation rather than polymerase catalysis.
- GO:0009360 DNA polymerase III complex: ACCEPT. HolA is the delta component of the polymerase III clamp-loader subassembly, supported by target HolA domains and Pseudomonas minimal-loader reconstitution.
- GO:0071897 DNA biosynthetic process: ACCEPT. The upstream inferred polymerase MF is wrong, but the BP claim is independently supported by direct clamp-loading assistance to processive DNA synthesis. A true process claim is not removed merely because its original inference route was defective.

Primary sources used: PMID:15611049. Independent frozen support: file:PSEPK/holA/holA-uniprot.txt.
