# Prkcz (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Prkcz` resolved P09217 (KPCZ_RAT; RGD:3399; GeneID 25522); 108 GOA rows.
- No deep-research provider available; manual synthesis in `Prkcz-deep-research-manual.md`.
- Full text cached for PMID:15707389, 15728837, 16525020, 19885391, 9177193, 19254952;
  all other GOA references are abstract-only.

### Key curation decisions

- GO:0004697 (DAG-dependent, IEA from EC 2.7.11.13 mapping) and GO:0004698 (calcium,DAG-
  dependent, ISO from human Q05513) are REMOVED: aPKCs are not regulated by DAG or Ca2+
  [UniProt P09217 ACTIVITY REGULATION; C1 domain does not bind DAG, PMID:9177193].
  Recorded as source defects (EC-to-GO mapping is too specific for EC 2.7.11.13, which covers
  all PKC isoforms; donor human annotation should be checked).
- Stress fiber IDA (PMID:16525020): the full text states PKCzeta staining was diffuse where
  actin remained in stress fibres ["Away from the dorsal surface, most actin filaments remained
  in the form of stress fibers, and the staining pattern of PKCzeta was diffuse."]; PKCzeta
  colocalised with insulin-induced cortical actin structures. MODIFY to cortical actin
  cytoskeleton (GO:0030864) and source defect.
- IMP-coded CC rows (Schaffer collateral-CA1 synapse, glutamatergic synapse, PMID:18667614):
  a perturbation phenotype cannot establish a location; REMOVE the IMP rows, keep the IDA rows,
  and record WRONG_EVIDENCE_CODE source defects.
- Bare protein binding (A6rp/twinfilin-2, PMID:10406962) removed per policy; the paper shows a
  substrate relationship (phosphorylation), not an informative binding function.
- Potassium channel regulator activity (IMP, PMID:15062979): PKCzeta acts as a kinase within a
  p62-Kv complex; the regulator MF overstates a kinase-mediated, indirect effect -> over-annotated.
- protein kinase activity rows -> MODIFY to protein serine/threonine kinase activity.
- 19254952 (Kim et al. 2009, rat VSMC siRNA): supports positive regulation of ERK1/ERK2 cascade
  downstream of AT1R/Gq; added as additional support to existing ERK rows (no NEW row needed).
- No NEW annotations proposed. PAR polarity complex membership (GO:0120157) is captured in
  core_functions.in_complex only (supported by PMID:11525734 and UniProt SUBUNIT).
