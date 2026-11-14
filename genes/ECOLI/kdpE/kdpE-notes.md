# kdpE (P21866) curation notes

## 2026-11-01 review pass

- Provider deep research was not run in this pass; no `kdpE-deep-research-*.md` file exists.
  Evidence came from cached publications (PMID:22291906, PMID:16322582, PMID:18631241 full
  text; others abstract-only).
- Two separate core functions retained: GO:0000156 receiver/phosphorelay activity and
  GO:0000987 cis-regulatory sequence-specific DNA binding driving GO:0045893
  [PMID:1630316, "This upstream sequence was demonstrated to be the target site for the
  trans-acting activator, KdpE"].
- General terms (GO:0000976, GO:0003677, GO:0003700, GO:0006355, GO:0005737, GO:0042802)
  MODIFY to their specific supported descendants. Bare GO:0005515 rows removed per policy.


## 2026-11-07 E. coli Kdp module consultation

Reviewed all existing annotation claims against the cached primary literature, UniProt record, and current GO definitions. Original ordered annotation payloads and source files were frozen before editing; no new annotation rows were added. The two inherited KdpD NEW proposals remain present. Detailed decisions and source scope are recorded in `analysis/module_audits/bacterial_kdp_potassium_homeostasis/ecoli-consultation/`.

A genuine configured Falcon research request was attempted for this gene and failed with HTTP 403 authentication; no provider report was fabricated. The exact attempt log is `.cache/module-audit-logs/kdp-20261107/ecoli-consultation/falcon-kdpE.log`. PAINT-loss checking found no IRD/IKR loss on the recorded lineage.

The core now uses the existing specific DNA-binding transcription activator activity, rather than stopping at DNA binding. PMID:22291906 directly separates isolated DNA recognition from the full-length receiver-dependent transcriptional response. The functional DNA complex and receiver-domain dimerization are central to this activity and now ACCEPT. Receiver-domain dimerization (PMID:16322582) is not contradicted by a monomeric isolated DNA-binding domain.
