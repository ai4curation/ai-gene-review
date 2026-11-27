# lolC (Escherichia coli K-12) review notes

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


## 2026-11-07: Lol comparative consultation

All existing annotations and core functions were reassessed against their cited cached literature, curated UniProt text, and relevant full primary texts. Ordered annotation payloads and immutable sources are preserved. The evidence/action ledger and access limits are in `analysis/module_audits/bacterial_lol_lipoprotein_trafficking/ecoli-consultation/evidence.md`.

An actual configured Falcon attempt for this gene failed with HTTP 403 authentication; no provider report was fabricated. The log is retained under `.cache/module-audit-logs/lol-20261107/ecoli-consultation/falcon-lolC.log`. Manual primary-source review supplies the evidence.

LolC is a four-pass inner-membrane subunit of the Escherichia coli LolCDE lipoprotein-release complex. Together with LolE, it forms the pockets that bind the lipid anchor of mature outer-membrane-destined lipoproteins. The Hook and Pad surfaces in its large periplasmic domain recruit LolA and prepare the carrier to receive cargo. Two cytoplasmic LolD ATPase subunits drive the conformational cycle that extracts lipoproteins from the periplasmic leaflet of the inner membrane. This releases already translocated cargo into the periplasm rather than moving it through the inner-membrane bilayer.
