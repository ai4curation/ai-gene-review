# lolE (Escherichia coli K-12) review notes

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

An actual configured Falcon attempt for this gene failed with HTTP 403 authentication; no provider report was fabricated. The log is retained under `.cache/module-audit-logs/lol-20261107/ecoli-consultation/falcon-lolE.log`. Manual primary-source review supplies the evidence.

LolE is a four-pass inner-membrane subunit of the Escherichia coli LolCDE lipoprotein-release complex. LolE and LolC jointly form lipid-anchor-binding pockets, while a cleft on the LolE periplasmic domain contacts a short segment of the cargo polypeptide and promotes efficient release. Two LolD ATPase subunits drive the conformational cycle, and LolC recruits the LolA carrier. LolD and LolE can support release in a particular in vitro reconstitution, whereas the canonical cellular machinery requires both LolC and LolE. Cargo is extracted from the periplasmic leaflet, not translocated through the inner-membrane bilayer.
