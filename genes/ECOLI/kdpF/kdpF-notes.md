# kdpF (P36937, E. coli K-12) curation notes

## 2026-11-01 review pass

- Provider deep research was not run in this pass; review based on cached publications and UniProt.
- KdpF is a single TM helix of KdpFABC [PMID:28636601 "KdpF is a single transmembrane helix with a position that is distinct from transmembrane helices or accessory elements in other P-type ATPases"],
  dispensable in vivo, stabilising in vitro [PMID:10608856 "Although KdpF is not essential for the function of the Kdp complex in vivo, it is part of the complex and functions as a stabilizing element in vitro."].
- No MF assigned in core_functions (no catalytic/transport activity); GO:0008556 rows marked
  over-annotated; complex membership GO:0031004 is the core annotation.
- GO:0005198 structural molecule activity was considered (definition: contributes to structural
  integrity of a complex) but not proposed as NEW, since the stabilisation is only demonstrated
  for the detergent-solubilised complex and is replaceable by lipids.
- GO:1903103 (antiporter complex, ComplexPortal IPI) MODIFY to GO:0031004 with a source defect.
