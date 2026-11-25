# lolD (Escherichia coli K-12) review notes

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
- PMID:10783239 states that LolCDE is not involved in transmembrane transport.
  The IBA rows for transmembrane transport (removed) and transmembrane
  transporter activity (refined to GO:0140306) come from the deep PTHR24220
  node PTN000655654; see interpro/panther/PTHR24220/PTHR24220-review.yaml.


## 2026-11-07: Lol comparative consultation

All existing annotations and core functions were reassessed against their cited cached literature, curated UniProt text, and relevant full primary texts. Ordered annotation payloads and immutable sources are preserved. The evidence/action ledger and access limits are in `analysis/module_audits/bacterial_lol_lipoprotein_trafficking/ecoli-consultation/evidence.md`.

An actual configured Falcon attempt for this gene failed with HTTP 403 authentication; no provider report was fabricated. The log is retained under `.cache/module-audit-logs/lol-20261107/ecoli-consultation/falcon-lolD.log`. Manual primary-source review supplies the evidence.

LolD is the cytoplasmic ATP-binding and ATP-hydrolyzing subunit of the Escherichia coli LolCDE lipoprotein-release complex. Two LolD copies associate with the inner-membrane subunits LolC and LolE, coupling the nucleotide cycle to extraction of mature lipoproteins from the periplasmic leaflet and transfer to LolA. ATP binding drives conformational rearrangements in the cargo-binding assembly; ATP hydrolysis is required for sustained membrane release and resets the cycle in structural models. LolD powers extracytoplasmic cargo extraction rather than transport of cargo through the inner-membrane bilayer.
