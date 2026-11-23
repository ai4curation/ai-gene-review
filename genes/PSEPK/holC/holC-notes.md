# holC review notes


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target Q88P74 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003677 DNA binding: MARK_AS_OVER_ANNOTATED. The KT2440 chi-psi complex binds ssDNA, but that does not establish DNA binding by chi itself. Chimeric P. aeruginosa/E. coli complexes and N-terminal psi truncation attribute the DNA-binding activity to psi (PMID21955458). The present individual-HolC electronic annotation exceeds that evidence.
- GO:0003887 DNA-directed DNA polymerase activity: REMOVE. HolC is an accessory chi subunit coupling SSB to the loader; it does not catalyze DNA synthesis. The alpha subunit supplies polymerization, so this individual catalytic mapping is incorrect.
- GO:0006260 DNA replication: ACCEPT. The chi subunit links SSB-coated templates to the clamp-loader machinery, a direct physical contribution to replication. The KT2440 chi-psi complex was purified in PMID21955458, while detailed SSB-interface mechanism comes from the homologous P. aeruginosa/E. coli systems.
- GO:0032298 positive regulation of DNA-templated DNA replication initiation: MARK_AS_OVER_ANNOTATED. The retrieved evidence concerns SSB coupling and clamp loading during synthesis, not a demonstrated increase in chromosomal origin-firing frequency or positive regulation of initiation in KT2440. Primer-to-polymerase exchange must not be equated with regulation of chromosome replication initiation.
- GO:0071897 DNA biosynthetic process: ACCEPT. The chi accessory subunit physically couples template protection to the replicase, supplying structural support for DNA production. This participation does not require assigning polymerase catalysis to HolC or making it universally essential.

Primary sources used: PMID:21955458. Independent frozen support: file:PSEPK/holC/holC-uniprot.txt.

The paper explicitly clones KT2440 chi–psi. Primer-to-locus/sequence mapping is being documented separately. Complex ssDNA binding must not be propagated to standalone chi. Current GO0030674 protein-macromolecule adaptor activity covers the non-receptor SSB–loader bridge; no new ontology term is required. GO0030159 is receptor-specific and is not used. The module may treat HolC as an accessory architecture, while the gene itself has a core accessory function.


## PR #6117 round-1 follow-up (2026-11-06)

- Record UNIPROT WRONG_TERM for GO:0003887 (InterPro:IPR007459|EC:2.7.7.7); original action remains REMOVE.
- Refine machine GO:0006260 to GO:0006261 and align the core process.

All historical annotation payloads, inherited NEW proposals, and frozen raw/provider files are preserved. Source confidence distinguishes direct target assays from comparative Pseudomonas evidence. No publication cache was refreshed.
