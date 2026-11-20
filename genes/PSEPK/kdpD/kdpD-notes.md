# kdpD curation notes

## Evidence assessment

KdpD is a membrane sensor kinase with large cytosolic input and transmitter
domains. E. coli experiments establish that membrane-bound KdpD controls
KdpE-dependent kdpFABC expression and describe four transmembrane segments plus
cytoplasmic domains [PMID:14534307, "The membrane-bound sensor kinase KdpD
consists of an N-terminal input domain"]. UniProt predicts the corresponding
multi-pass topology for PSEPK Q88FD9 [file:PSEPK/kdpD/kdpD-uniprot.txt].

## Curation decision

The full-length protein is assigned to the plasma membrane. The ARBA cytoplasm
annotation likely reflects its extensive cytosolic domains, but `located_in
cytoplasm` misstates the location of the integral membrane gene product and is
therefore removed.

## 2026-11-01 re-review

- Provider deep research was not run in this pass; no deep-research file exists.
- Thin rows upgraded with reasons and support. Correct-but-general terms (GO:0004673,
  GO:0016301, GO:0016740, GO:0016772, GO:0007165, GO:0016020) changed from
  KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED to MODIFY with the specific term already on the gene.
- E. coli KdpD papers (PMID:9099740, PMID:8223625, PMID:7499326, PMID:14534307) cited as
  orthology-based support; Q88FD9 shares PANTHER PTHR45569:SF1 and KdpD N-terminal/TM signatures.
- Open question: whether the E. coli N-terminal atypical serine kinase activity (KdpB S162
  phosphorylation, PMID:38622146) is conserved in KT2440; not annotated.


## Scoped Kdp module consultation — 2026-11-07

Current GO0005737 explicitly excludes the plasma membrane. The four-TM target architecture plus homolog topology support retaining REMOVE for the whole-protein cytoplasm assignment, without denying its cytoplasmic domains. The supported core remains histidine phosphorelay kinase. Full PMID38622146 establishes an additional serine-kinase mechanism in tested proteins; full-length KT2440 architecture alone does not establish its conservation, K+ dependence, or second-messenger control, so no NEW serine-kinase assertion is added.

Every original annotation row and its source payload/order was reviewed and preserved. No additional annotation rows were proposed. Full provenance and assay boundaries: `analysis/module_audits/bacterial_kdp_potassium_homeostasis/psepk-consultation/primary-scope.md`; sequence checks are adjacent. No IBA rows occur in these six reviews, so no IBA loss judgment is being made. Family membership and original historical ISO donors are retained independently of donor counts.

A genuine `just deep-research PSEPK kdpD --provider falcon` request failed HTTP403 authentication. Logs remain in `.cache/module-audit-logs/kdp-20261107/psepk-consultation/`; no provider report was manufactured.

Native KT2440 context is supplied by PMID38927284 full text: salt stress increases kdpA/B/D transcripts, but individual overexpression does not improve growth in the tested high-salt medium. This is not a purified activity assay or proof that the complete pump is unimportant. PMID26913973 publisher text corrects the historical kdpB pseudogene annotation; its local abstract cache remains unchanged. No salt-tolerance process assertion is added.
