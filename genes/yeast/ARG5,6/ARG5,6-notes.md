# ARG5,6 (YER069W, Q01217) notes

- Single 863-aa precursor processed in mitochondria into acetylglutamate kinase (EC 2.7.2.8, N-terminal) and N-acetyl-gamma-glutamyl-phosphate reductase (EC 1.2.1.38, NADP-dependent) [UniProt:Q01217; PMID:1851947 "the ARG5,6 gene encodes acetylglutamyl-P reductase and acetylglutamate kinase, two arginine anabolic enzymes which are localized in the mitochondria"].
- "ARG5,6 encodes a precursor that is maturated in the mitochondria into acetylglutamate kinase and acetylglutamyl-phosphate reductase" [PMID:11553611].
- NAGS/NAGK metabolon with Arg2; the ascomycete-specific C-terminal domain of NAGK "is required to maintain synthase activity and protein level"; mutual feedback-regulation coupling [PMID:12603335].
- Moonlighting DNA binding/transcription: "Chromatin immunoprecipitation experiments revealed that Arg5,6 is associated with specific nuclear and mitochondrial loci in vivo" and "Deletion of Arg5,6 causes altered transcript levels of both nuclear and mitochondrial target genes." [PMID:15486299] -> KEEP_AS_NON_CORE.
- Mitochondrial proteomics HDA [PMID:16823961, PMID:24769239].

## Curation decisions
- Two core MFs: GO:0003991 (in GO:0106098 complex) and GO:0003942; BP GO:0006526/GO:0006592; CC GO:0005759.
- NEW: part_of GO:0106098 NAGS/NAGK complex (IPI, PMID:11553611) - GOA has it only on ARG2.
- RCA cytosol REMOVE; IEA cytoplasm MODIFY -> mitochondrial matrix; NAD binding over-annotated (NADP enzyme); generic grouping terms MODIFY.


## 2026-10-26 systematic fungal annotation audit

Reviewed all 28 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

PMID:1649049 supports import-dependent precursor processing, unlike Arg7 pre-import maturation. PMID:11553611/12603335 support the kinase contribution to the NAGS complex and dispensability of the reductase for that support. The one pre-existing NEW complex annotation is preserved, not newly added. Mitochondrial DNA binding/transcription claims remain non-core on their own experimental evidence (PMID:15486299). NAD-binding inference is refined to the supported NADP specificity without asserting exclusion of every other nucleotide.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-yeast-ARG5,6-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 17, KEEP_AS_NON_CORE 1, MODIFY 8, NEW 1, REMOVE 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.

Ontology-cache advisory: live QuickGO confirms GO:0003942 has the NADP+-specific label; the local ontology cache retains the older shorter label. The machine payload and current chemically specific label are preserved rather than rewritten to silence a stale-label warning.

## PR #5563 follow-up, 2026-10-26

Restored supported GO:0005739 mitochondrion rows to ACCEPT under the explicit root-organelle policy; existing matrix rows remain separate. Reasons distinguish organelle screens, direct targeting, publication-linked curated evidence and unavailable full text. No original annotation payload changed. Cytosol decisions use target-specific fractionation/processing evidence rather than relationship qualifiers or generic precursor transit. For Aga1, matrix inference does not imply universal post-import autoproteolysis.

The authored GO:0003942 label follows the repository ontology version; NADPH specificity remains explicit in the biological rationale. Original GOA term labels are preserved.
