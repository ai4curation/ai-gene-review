# putA curation notes

- Q88D80 is the exact KT2440 full-length PutA exemplar. PMID:10613867 supports
  the fused two-step proline-to-glutamate assignment, while PMID:11097893
  supports repression of the divergent put promoters independent of catalysis.
- PANTHER:PTN001709052 occurs in the Q88D80 GOA provenance for GO:0003842 and
  GO:0009898. It is not used as the reusable module selector because the local
  PTHR42862:SF1 sample contains both approximately 1,300-aa fused PutA proteins
  and many approximately 515-aa stand-alone P5C dehydrogenases.
- The completed OpenScientist report was used for literature retrieval. Its
  family-level mechanistic claims were retained only where corroborated by the
  cached publications or exact UniProt record.
- 2026-08-31 clarification: PMID:10613867 directly links PutA to growth on
  proline and supports a fused two-step product, but assignment of the PRODH
  and GSALDH regions in that abstract is based on sequence homology rather than
  direct catalytic-domain assays.
- 2026-08-31 evidence update: PMID:18767154 directly tested the P. putida PutA
  N-terminal RHH domain and operator DNA by gel mobility-shift assays and NMR,
  supporting sequence-specific put control-region binding.


## 2026-11-06 comparative PutA-module audit

All original annotation payloads/order and historical NEW actions retained. All rows and core functions were re-read; only evidence/role inconsistencies were changed. Refined true anion/heterocyclic binding to supported FAD/proline/NAD interactions after official GO ancestor checks; no new annotation rows. Binding need not be a separate autonomous activity. Retained both catalytic reactions without assigning a universal quinone species or channeling mechanism.

Official full-text source and sequence checks are in `genes/PSEPK/putA/putA-source-analysis/primary-scope.md` and provenance.yaml. KT2442 derivative genetics, KT2440 reference identity, and the PpPutA45 fragment are distinguished explicitly. A full-length KT2440 membrane-switch/channeling assay remains unavailable; no catalytic membrane location was added to the core synthesis. Genuine existing OpenScientist report/artifacts were reused unchanged. PAINT reports the target accession absent from its cached tree, so lineage losses are not resolved rather than inferred absent.


## 2026-11-06 PR #6150 review follow-up

GO:0009898 changes from ACCEPT to UNDECIDED. The frozen UniProt cross-reference traces it to TreeGrafter; no independent target subcellular-location statement is present, and the available tree did not resolve target placement. Family membrane-coupled chemistry establishes plausibility, but the PpPutA45 construct and KT2440/KT2442 promoter results do not locate full-length target catalysis. This differs from GsPutA's quinone-site geometry and BjPutA's retained PAINT inference plus characterized catalytic architecture. [PMID:18767154 "PpPutA45 was shown to bind a 14 base-pair DNA oligomer"] The before/after ledger retains the other three action refinements: sequence-specific regulatory DNA binding and specific catalytic ligand binding. Live QuickGO ancestry confirms NAD binding is not below anion binding, so its omission from that replacement list is intentional.

The scoped action ledger and ontology checks are in `analysis/module_audits/bacterial_fused_puta_proline_catabolism/round1-action-reversal-ledger.yaml` and `round1-review-response.md`. Original annotation rows and source fields are retained in order.


## 2026-11-07 PR #6150 round3 follow-up

GO:0098562 changes from MODIFY to UNDECIDED, coherently with GO:0009898. The previous replacement asserted a membrane face that the companion row declines to settle. The ARBA broad location and TreeGrafter specific location do not provide independent target localization experiments. PMID:28712849 explains comparative membrane coupling and E. coli switching; its generic flavin-switch sentence does not locate full-length KT2440 PutA. The PpPutA45 assay measures fragment DNA binding [PMID:18767154 "PpPutA45 was shown to bind a 14 base-pair DNA oligomer"]. Family coupling remains biologically plausible; unresolved target placement is not evidence of loss. No replacement location or core location is asserted. The additive round3 action ledger records row 12 and preserves the earlier 16-entry ledger unchanged.
