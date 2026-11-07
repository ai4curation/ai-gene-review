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


## 2026-11-07 E. coli Kdp module consultation

Reviewed all existing annotation claims against the cached primary literature, UniProt record, and current GO definitions. Original ordered annotation payloads and source files were frozen before editing; no new annotation rows were added. The two inherited KdpD NEW proposals remain present. Detailed decisions and source scope are recorded in `analysis/module_audits/bacterial_kdp_potassium_homeostasis/ecoli-consultation/`.

A genuine configured Falcon research request was attempted for this gene and failed with HTTP 403 authentication; no provider report was fabricated. The exact attempt log is `.cache/module-audit-logs/kdp-20261107/ecoli-consultation/falcon-kdpF.log`. PAINT-loss checking found no PANTHER family in the source record, so lineage losses could not be checked.

PMID:10608856 directly distinguishes structural contribution from indispensability. The protected abstract explicitly reports nearly unchanged membrane ATPase activity and growth at 0.1 mM K+ without KdpF, but activity loss after detergent purification and restoration with purified KdpF or lipids. Together with intact-complex structures, these observations support a core contribution to GO:0008556 and transport participation, now ACCEPT. No autonomous ATPase, universal native requirement, or new annotation row is asserted. Publisher full-text retrieval was attempted by the collaborating reviewer and returned HTTP 403; the explicit abstract observations are sufficient for these bounded claims.


## 2026-11-07 PR6179 round-one adjudication

Reviewed the source relation, core role and source-specific limits relevant to this gene. See `analysis/module_audits/bacterial_kdp_potassium_homeostasis/round1/evidence.md` for the full evidence and disagreement record. Original ordered annotation payloads, qualifiers and historical NEW/retired flags are preserved. GO0008556 now has a relation-specific overannotation judgment and probable source correction from enables to contributes_to; structural contribution remains core. KdpF requirement is conditional on the tested detergent-solubilized preparation, not universal native essentiality. [PMID:10608856; PMID:34272288].
