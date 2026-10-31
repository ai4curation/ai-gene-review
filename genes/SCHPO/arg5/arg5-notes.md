# arg5 (SPBC56F2.09c, cpa1, UniProt O60060) notes

## Naming trap
- S. pombe arg5 = CPSase A small (glutaminase) subunit = S. cerevisiae CPA1. S. cerevisiae ARG5,6 = S. pombe arg11.

## Evidence
- [UniProt:O60060 "FUNCTION: Small subunit of the arginine-specific carbamoyl phosphate"]; transit peptide 1..17.
- Location conflict in UniProt: [UniProt:O60060 "SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:200419}."] vs [UniProt:O60060 "Cytoplasm {ECO:0000269|PubMed:16823372}."]. Partner arg4 is mitochondrial in the same HTP screen.
- Separate pyrimidine CPSase: [UniProt:O60060 "one, CPSase P, is part of a multifunctional protein (ura1) encoding 3"]; [UniProt:O60060 "synthase is channeled to its respective pathway, in contrast to"].

## Decisions
- HDA cytoplasm UNDECIDED; IBA/IEA cytoplasm MODIFY -> matrix.
- de novo pyrimidine nucleobase biosynthesis (InterPro2GO) REMOVE: compartmentalised, channelled CPSase A; pyrimidine CPSase is ura1. (S. cerevisiae CPA1 review only marked it over-annotated because the budding-yeast pools are shared.)
- Core: MF GO:0004359, contributes_to GO:0004088, complex GO:0005951, matrix.


## 2026-10-26 systematic fungal annotation audit

Reviewed all 18 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

ISS source P22572 is Neurospora crassa arg-2, not budding-yeast CPA1 (P07258); the source identity is corrected in the review only. This is the mitochondrial glutaminase subunit of arginine-specific CPSase. Curated UniProt explicitly distinguishes mitochondrial CPSase A from cytosolic ura1 CPSase P and channeling to their respective pathways, supporting rejection of generic CarA pyrimidine-pathway propagation. Broad glutamine metabolism is refined to the hydrolysis step actually performed by this subunit.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-SCHPO-arg5-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 11, MODIFY 6, REMOVE 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.

## PR #5563 follow-up, 2026-10-26

Restored supported GO:0005739 mitochondrion rows to ACCEPT under the explicit root-organelle policy; existing matrix rows remain separate. Reasons distinguish organelle screens, direct targeting, publication-linked curated evidence and unavailable full text. No original annotation payload changed. Cytosol decisions use target-specific fractionation/processing evidence rather than relationship qualifiers or generic precursor transit. For Aga1, matrix inference does not imply universal post-import autoproteolysis.
