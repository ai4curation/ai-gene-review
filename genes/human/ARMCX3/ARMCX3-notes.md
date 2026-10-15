# ARMCX3 (ALEX3) review notes

## Sources
- Affinage: trust gates clear. Checked against:
  - PMID:22569362: Armcx3 trafficking via Kinesin/Miro/Trak2.
  - PMID:19304657: integral outer-membrane protein; binds Sox10.
  - PMID:38320000: Alex3/Galpha-q complex; CNS knockout.
  - PMID:23844091: Wnt/PKC degrades Alex3; full text.
- Human ARMCX3 rows are mostly transferred from mouse Armcx3 (Q8BHS6), whose donor rows include IDA nucleus, cytosol and mitochondrion, EXP cytoplasm and outer membrane, and IDA axonal transport (QuickGO).
- The axonal-transport IBA node (PTN001038987) is seeded by mouse Armcx3 itself.

## Decisions
- ACCEPT:
  - Mitochondrion (IBA, IEA, HTP) and mitochondrial outer membrane (IEA, ISS).
  - Axonal transport of mitochondrion (IBA).
- KEEP_AS_NON_CORE: nucleus, cytoplasm, cytosol and axon cytoplasm.
- REMOVE: MAF1, EHHADH and FAM25A protein binding (policy).
- No NEW adaptor MF. The Galpha-q paper is abstract-only and says only that Galpha-q "interacted with" Alex3 and Miro1/Trak2, so this is raised as a question.

## Review round 1 (PR #4195)
- The non-core nucleus, cytoplasm and cytosol rows are now supported by UniProt's by-similarity location line, with the mouse donor source named. The Wnt/PKC quote was removed from them, since that paper shows mitochondrial localization.
- Sox10 coactivation decision: ARMCX3 has no intrinsic transcriptional activity and sits on the mitochondrial outer membrane. It enhances Sox10 transactivation, plausibly by controlling Sox10's mitochondrial association, rather than acting as a promoter-bound coactivator. No transcription coregulator MF is assigned; the point is raised as a suggested question. The PMID:19304657 finding is recorded.
- No core MF is assigned, because no direct activity is established. The redundant mitochondrion location was dropped from core_functions, and the truncated Wnt/PKC quote was completed.
