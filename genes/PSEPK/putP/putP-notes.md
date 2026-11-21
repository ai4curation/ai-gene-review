# putP curation notes

- Q88D81 is the exact KT2440 PutP exemplar. PMID:10613867 identifies the gene
  product as an integral inner-membrane proline-uptake protein; the sodium
  coupling assignment is electronic in the exact UniProt record rather than a
  direct KT2440 transport-kinetics measurement.
- The first QuickGO fetch produced a header-only TSV. A forced refresh on
  2026-08-13 returned 11 rows, including GO:0015193 and GO:0031402; the review
  was rebuilt against all 11 rows with no NEW substitutions.
- The current GOA provenance includes PANTHER:PTN005155986. UniProt assigns
  Q88D81 to PTHR48086:SF3, which is used as the reusable PutP family selector.
- OpenScientist exited naturally without producing a putP report. No provider
  report was fabricated or restarted.


## 2026-11-06 comparative PutA-module audit

All original annotation payloads/order and historical NEW actions retained. All rows and core functions were re-read; only evidence/role inconsistencies were changed. Retained sodium binding as a central transport interaction, with direct E. coli evidence distinguished from the KT2440 family/RuleBase inference. Existing transport/CC refinements remain supported; no extra process or coupling assertions added.

Official full-text source and sequence checks are in `genes/PSEPK/putA/putA-source-analysis/primary-scope.md` and provenance.yaml. KT2442 derivative genetics, KT2440 reference identity, and the PpPutA45 fragment are distinguished explicitly. A full-length KT2440 membrane-switch/channeling assay remains unavailable; no catalytic membrane location was added to the core synthesis. Genuine existing OpenScientist report/artifacts were reused unchanged. PAINT reports the target accession absent from its cached tree, so lineage losses are not resolved rather than inferred absent.


## 2026-11-06 PR #6150 review follow-up

Sodium binding remains ACCEPT as a specific-family/RuleBase mechanistic inference (TIGR02121; RuleBase:RU366012). It is not a KT2440 direct binding assay, affinity measurement, sodium-only protection result, or stoichiometry measurement. The E. coli evidence is stronger [PMID:1567896 "Na+ alone, even in the absence of proline, partially protected it from the NEM-inactivation"]; sharing a curation action does not erase this distinction. The UniProt quotation now includes the complete L-proline substrate name across the flat-file wrap.

The scoped action ledger and ontology checks are in `analysis/module_audits/bacterial_fused_puta_proline_catabolism/round1-action-reversal-ledger.yaml` and `round1-review-response.md`. Original annotation rows and source fields are retained in order.
