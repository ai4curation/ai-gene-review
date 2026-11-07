# Isc family reconciliation — 2026-11-07

PTHR10093 now has UNRESOLVED universal GO0140132 scope. Established IscU/NifU/ISU cluster-delivery positives remain; B. subtilis SufU O32163 is a verified family member with substantial sulfur-transfer evidence. Its early positive cluster-reconstitution/Leu1-transfer report is retained beside the later contrary biochemical and complementation evidence. No whole-subfamily loss or fabricated member exception is asserted.

The PTHR10093 PTN000009661 GO0008198 assessment changes TOO_DEEP→UNRESOLVED. Direct bacterial iron-binding results remove the old bacterial/eukaryotic split, while full ancestral node extent remains uncertain. The GO0006879 node stays UNRESOLVED with its eukaryotic-only rationale replaced by the specific E. coli Fur-maturation evidence and its assay limits. Seed taxonomy or counts are not treated as a phylogenetic argument. Node IDs, asserted terms, dates, evidence and seed lists are immutable.

PTHR19375 universal GO0140662 changes FAMILY_WIDE→UNRESOLVED. Canonical Hsp70 folding positives are retained. HscA ATPase, IscU state selection, holdase and cluster-transfer evidence does not automatically establish a folding endpoint, but also does not establish a universal absence or loss. No new HscA negative exception or family-wide ATPase grant is introduced. All34 existing PAINT objects, unrelated localization assessments, member identities and residue site data are unchanged.

The old HSPH1/Q92598 negative judgment is preserved. Its exact former member exception is in `hsp110-exception-baseline.json`; its rationale appears verbatim in the family notes and its quoted support remains in the term assessment. The live `member_exceptions` field was removed solely because the schema/cross-check permits exceptions only on FAMILY_WIDE or SUBFAMILY_ONLY grants, not UNRESOLVED. Parent explicitly approved this representation correction; the biological judgment did not change.

## Verification

Focused family schema and term/label validation pass. Reference validation passes with no issues. The two-family gene cross-check has no conflicts after the schema-legal Hsp110 representation correction. Residue/PAINT/member validation reports131 pass,0 fail,1 unresolved: E. coli HscA P0A6Z1→SF176 cannot be verified by the absent worktree PANTHER member index. Its family-level presence is independently visible in the unchanged entries.csv; that does not by itself verify SF176. No member identifier was changed to hide this warning.

Both generated `other` histories validate. Strict preservation and Ruff pass. The verifier permits only the scoped prose/evidence changes, the three documented verdict changes, and the approved Hsp110 representation adjustment. Twenty-three protected raw family and publication files retain exact hashes. All other PAINT, localization, member and residue judgments compare exactly to the frozen baseline.

Reproduce preservation with `uv run python analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/family-consultation/verify.py`. Logs and frozen file hashes are under `.cache/module-audit-logs/isc-20261107/family-consultation/`. No gene, module, shared project, raw source or validator files were edited. No commit, push or full-corpus run was performed. Ownership released after handoff.
