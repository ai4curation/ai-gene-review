# Akap5 (rat) review notes

## Session 2026-10-28

- fetch-gene resolved P24587 (AKAP5_RAT, Swiss-Prot, RGD:620829); GOA keyed to P24587. 108 rows.
- No deep-research API keys; literature synthesis written by hand in
  `Akap5-deep-research-manual.md`.
- Full text available and read for PMID:20410303 (AC8), 12177200, 15141163, 19169250,
  19535604, 22343722. Others are abstract-only.

### Decisions worth flagging

- Core MF: PKA-anchoring scaffold. Modelled as `signaling adaptor activity` (GO:0035591),
  with PKA-RII binding, PP2B binding and adenylate cyclase binding as supporting MF rows.
  The three `molecular adaptor activity` rows are MODIFIED to GO:0035591.
- AC8 (PMID:20410303): direct binding (GST pull-down) and endogenous co-IP; AKAP150 dampens
  Ca2+-stimulated AC8 activity in MIN6 and rat hippocampal neurons [PMID:20410303
  "AKAP79/150 dampens Ca2+-dependent AC8 activity as a consequence of its interaction with
  the enzyme"]. The UniProt DR GO line also lists `positive regulation of adenylate cyclase
  activity` (IDA:RGD), which is not in the GOA file under review; the HEK293 overexpression
  result that might underlie it is described by the authors as a non-native artefact.
  Recorded as a suggested question.
- GO:0043271 negative regulation of monoatomic ion transport (IMP, PMID:18701070): the
  abstract says AKAP-TRPV1 binding is required for sensitization, i.e. positive regulation.
  Abstract-only, so UNDECIDED with a SUSPECTED sign-inversion source defect.
- GO:0032984 protein-containing complex disassembly (IDA, PMID:12177200, full text read):
  AKAP150 is the object of NMDA/latrunculin-induced complex dissociation, not an agent of
  disassembly. REMOVE with WRONG_TERM source defect.
- SynGO glutamatergic synapse / PSD intracellular component rows with IEP/IMP codes: a
  phenotype or expression assay cannot establish location; kept with the same action as
  the IDA rows and a WRONG_EVIDENCE_CODE CHECK source defect.
- GO:1905751: GOA labels it obsolete; OLS (checked 2026-10-28) and the local GO build still
  show it live. Kept as non-core; claim also covered by GO:1903078.
- Protein kinase binding rows (GO:0019901) MODIFIED to GO:0034237 (PKA R-subunit binding).
  Note GO:0034237 is_a GO:0051018 protein kinase A binding, not a descendant of GO:0019901
  (checked with runoak ancestors), so this is a lateral correction.
