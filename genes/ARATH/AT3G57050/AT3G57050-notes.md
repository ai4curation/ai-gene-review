# AT3G57050 / CBL (P53780) curation notes

## Sources checked (2026-11-13)
- UniProt P53780 (Swiss-Prot); GOA has 26 rows (the stub merges the duplicate chloroplast IDA rows from PMID:31002461),
  matching a live QuickGO query.
- Cached publications: PMID:8541513, 11402193 and 31002461 (abstract only; PMC111155 is a scanned PDF with no text),
  plus proteomics PMID:18431481, 20061580 and 25293756. Also fetched PMID:35472754 (CBL and H2S), which is cited in the UniProt FUNCTION.
- No deep-research provider file; this is a manual literature pass.

## Decisions
- gene_symbol set to CBL, the TAIR symbol in the UniProt DR TAIR line ("TAIR; AT3G57050; CBL."). UniProt gives no GN Name.
  CBL must not be confused with the CALCINEURIN B-LIKE family (CBL1-CBL10, e.g. genes/ARATH/CBL10).
- Chloroplast rows (HDA, IDA, IEA, ISM, ISS) and the cytoplasm rows (IBA is_active_in, ISM) were changed by MODIFY to
  chloroplast stroma GO:0009570, which the gene already carries (AT_CHLORO HDA, PMID:20061580). This follows the
  correct-but-general rule, since plastids are outside the root-organelle exception, and matches the AKHSDH1 precedent.
- Molecular adaptor activity (EXP, DisProt, PMID:11402193) was marked over-annotated, with a SUSPECTED source defect
  for DisProt. Nothing in the structure paper indicates bridging.
- L-methionine biosynthetic process (IDA) was changed by MODIFY to 'de novo' L-methionine biosynthetic process (GO:0071266, carried via TAS).
- Cysteine desulfhydrase / H2S production [PMID:35472754 "The recombinant CBL activity in vitro revealed that CBL produced
  H2S using L-cysteine as a substrate."]: not proposed as NEW, because dedicated DES1 exists and in vivo weighting is unclear.
- Developmental phenotypes [PMID:31002461] are downstream of methionine/SAM supply, which is rescued by Met, so no development BP was added.
- Family: PTHR11808:SF50 (eukaryotic CBL subfamily, shared with S. pombe cbl1); not PTHR43500 (E. coli MetC).
