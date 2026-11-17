# xcpZ (Pseudomonas aeruginosa PAO1, P25061) curation notes

## 2026-11-13 initial review

- Reviewed as the characterized GspM assembly-platform exemplar for
  `modules/bacterial_type_ii_secretion.yaml`, alongside the KT2440 member `genes/PSEPK/xcpZ`.
- Deep research was not run (no provider credentials in this environment); no
  `-deep-research-<provider>.md` file was created. Sources are the GOA-cited cached publications and the
  curated UniProt record.
- XcpZ is the bait protein of the co-purification study that isolated the XcpYZ and XcpRSYZ subcomplexes
  [PMID:16168578 "by a co-purification approach using a His-tagged XcpZ as a bait, XcpY and XcpZ were
  found associated together to constitute the most stable functional unit so far isolated from the
  P. aeruginosa secreton"], so its GO:0015627 IDA row is well keyed, unlike the pseudopilin rows.
- Function rests on linker-insertion variants that separate XcpY stabilisation from secreton function
  [PMID:11872731 "We identified three distinct regions of XcpZ required for both the stabilization of
  XcpY and the functionality of the secreton"] and on mutual stabilisation with XcpY [PMID:9884230].
- Unlike XcpY, this entry has no GO:0009276 row: the InterPro2GO mapping of IPR007690 (T2SS GspM) does
  not include that term. The defect recorded on the xcpY review is therefore specific to IPR007812.
- The GO:0015628 IDA keyed to the review PMID:9818381 carries the same evidence-code defect as the other
  Xcp proteins.
