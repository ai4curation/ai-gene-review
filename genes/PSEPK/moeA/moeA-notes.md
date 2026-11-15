# moeA (Q88L14, PP_2123) curation notes

## 2026-11-10 completion for the MoCo biosynthesis module

No notes file existed for the earlier DRAFT. The review rests on the curated RuleBase/UniRule
statements in the UniProt record, the MoeA domain architecture, and the characterised E. coli
ortholog (genes/ECOLI/moeA; PMID:15632135
"MoeA is responsible for mediating molybdenum ligation to molybdopterin"). The OpenScientist
report is retained as provider output and assessed LOW_QUALITY (misassigned KT2440 locus tags);
none of its organism-specific claims are used. No KT2440 assay exists.

Changes from the draft, aligned with ECOLI/moeA:

- GO:0005737 cytoplasm: KEEP_AS_NON_CORE -> MODIFY to GO:0005829 cytosol (correct but general,
  and cytosol is supported). Recorded as superseded_by in
  projects/TREEGRAFTER/rereview-2026-09-24/batch-05.yaml.
- GO:0032324: MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0006777 (the draft argued the term was
  merely general, which is a MODIFY).
- GO:0046872 metal ion binding: KEEP_AS_NON_CORE -> MODIFY to GO:0000287 magnesium ion binding
  (RuleBase Mg2+ cofactor; one Mg2+ per subunit in the E. coli structure).
- Added supported_by to every row. GO:0061599 and GO:0006777 stay ACCEPT.
