# arg4 (SPBC215.08c, UniProt O94313) notes

## Naming trap
- S. pombe arg4 = CPSase A large subunit (= S. cerevisiae CPA2). S. cerevisiae ARG4 = argininosuccinate lyase (= S. pombe arg41/arg7).

## Evidence
- [UniProt:O94313 "linked to the arginine pathway and is designated CPSase A (arg5-arg4),"]; [UniProt:O94313 "it is localized to mitochondria and repressed by arginine."]; location from Urrestarazu et al. 1977 (PMID:200419, title only cached) and ORFeome HDA.
- Classical mutant (Kohli et al. 1977, PMID:17248775) and deletion screen (PMID:32896087).
- Not in the PomBase arginine GO-CAM (gomodel:6690711d00000916 omits CPSase).

## Decisions
- IBA cytoplasm MODIFY -> mitochondrial matrix (ancestral cytosolic location; pombe enzyme relocated), propagation_review added.
- Core: MF GO:0004087, contributes_to GO:0004088, in complex GO:0005951, matrix (CPA2 core but mitochondrial).


## 2026-10-26 systematic fungal annotation audit

Reviewed all 18 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

The mitochondrial large CPSase subunit contributes ATP-dependent carbamoyl-phosphate synthesis, with the small arg5 subunit supplying glutamine-derived ammonia. Curated compartment/pathway separation is retained. Magnesium/manganese binding refinement reflects curated cofactor inference; broad cytoplasm is compatible with a mitochondrial subcompartment.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-SCHPO-arg4-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 13, MODIFY 5. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.

## PR #5563 follow-up, 2026-10-26

Restored supported GO:0005739 mitochondrion rows to ACCEPT under the explicit root-organelle policy; existing matrix rows remain separate. Reasons distinguish organelle screens, direct targeting, publication-linked curated evidence and unavailable full text. No original annotation payload changed. Cytosol decisions use target-specific fractionation/processing evidence rather than relationship qualifiers or generic precursor transit. For Aga1, matrix inference does not imply universal post-import autoproteolysis.
