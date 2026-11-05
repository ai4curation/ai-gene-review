# Map2k4 (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Map2k4` resolved A0ABK0L269 (TrEMBL, RGD:1307040, GeneID 287398); GOA file
  keyed to the same accession, 35 rows. No accession switch.
- No deep-research provider available; manual synthesis in `Map2k4-deep-research-manual.md`.
- Papers read in full: PMID:20550965, PMID:12514131, PMID:9487126, PMID:10521398. Abstract only:
  PMID:7768885, PMID:17064355, PMID:9714150, PMID:12029621, PMID:9769323, PMID:25100604,
  PMID:10493750, PMID:24705900, PMID:8702681.
- Kept consistent with the human MAP2K4 review (`genes/human/MAP2K4`): core MF = JUN kinase kinase
  activity (JNK cascade) plus MAP kinase kinase activity toward p38.

### Key decisions

- Generic kinase rows (kinase, transferase, protein kinase, protein Ser/Thr kinase) -> MODIFY to
  GO:0004708 MAP kinase kinase activity (MKK4 is dual-specificity, so Ser/Thr-only is also not
  quite right).
- MAPK cascade ISO rows -> MODIFY to JNK cascade + p38MAPK cascade. Note that
  [PMID:20550965 "MKK4 is not a physiologically relevant activator of p38"] in the ischaemic heart;
  the p38 role is stimulus-dependent and minor.
- positive regulation of JNK cascade (IDA, PMID:17064355): MKK4 is a component of the cascade,
  not a regulator of it -> MARK_AS_OVER_ANNOTATED.
- NMJ development ISO: mouse source PMID:10521398 is about ErbB2 and the with/from allele
  MGI:1929071 is Erbb2 -> REMOVE + source_defects (MGI wrong gene; RGD ISO propagation).
- negative regulation of motor neuron apoptotic process ISO: mouse source PMID:25100604 shows
  MKK4 loss makes motoneurons resistant to death -> sign inversion; MODIFY to GO:2000673 + source
  defect. Abstract only, but the abstract states the direction explicitly.
- cellular response to mechanical stimulus ISO from human P45985: human row already judged
  UNDECIDED (source paper does not mention MKK4) -> UNDECIDED.
- positive regulation of DNA replication (IMP 9487126): readout is S-phase entry downstream of
  c-Jun; MARK_AS_OVER_ANNOTATED.
- ERBB signaling ISO (mouse IDA PMID:8702681): abstract discusses MEK, not MKK4; but PMID:10493750
  supports MKK4 in neuregulin-JNK signaling, so KEEP_AS_NON_CORE and raise the 8702681 attribution
  as a question.

No NEW rows proposed (nucleus localization is ortholog-only and not shown for rat).
