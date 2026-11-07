# lolB (Escherichia coli K-12) review notes

## 2026-10-23

- Review created as an experimental exemplar for the reusable module
  `modules/bacterial_lol_lipoprotein_trafficking.yaml`; E. coli K-12 is the
  organism in which the LolCDE-LolA-LolB pathway was defined biochemically and
  genetically (Tokuda laboratory).
- Provider deep research was not generated: no deep-research provider API key
  is configured in this session. The review is based on the UniProt record,
  the GOA rows and the cached publications in `publications/`, most of which
  are abstract-only (`full_text_available: false`).
- GO has specific molecular-function terms for two Lol stages:
  GO:0140306 lipoprotein releasing activity (LolCDE; already annotated to
  E. coli LolC, LolD and LolE by IDA/IMP) and GO:0140598 lipoprotein carrier
  activity (LolA). No MF term exists for the LolB acceptance/insertion step.
- The GOA IMP row to GO:0044874 cites PMID:1052496, which resolves to a 1975
  clinical paper ("Ketotic hypoglycaemia"); recorded as a WRONG_REFERENCE
  source defect against EcoCyc. The claim itself is supported by PMID:9384574.


## 2026-11-07: Lol comparative consultation

All existing annotations and core functions were reassessed against their cited cached literature, curated UniProt text, and relevant full primary texts. Ordered annotation payloads and immutable sources are preserved. The evidence/action ledger and access limits are in `analysis/module_audits/bacterial_lol_lipoprotein_trafficking/ecoli-consultation/evidence.md`.

An actual configured Falcon attempt for this gene failed with HTTP 403 authentication; no provider report was fabricated. The log is retained under `.cache/module-audit-logs/lol-20261107/ecoli-consultation/falcon-lolB.log`. Manual primary-source review supplies the evidence.

LolB is a lipid-anchored outer-membrane lipoprotein of Escherichia coli whose periplasm-facing domain accepts mature lipoproteins from LolA and promotes insertion of their lipid anchors into the outer membrane. It is the terminal acceptor and insertion component of the canonical Lol trafficking pathway. LolB is essential in ordinary E. coli backgrounds; this requirement can be bypassed under altered lipoprotein-toxicity and envelope-stress conditions. Its historical HemM name does not reflect its established lipoprotein-trafficking function.
