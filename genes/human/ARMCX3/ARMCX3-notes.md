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
