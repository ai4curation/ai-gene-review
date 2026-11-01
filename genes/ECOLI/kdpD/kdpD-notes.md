# kdpD (P21865) curation notes

## 2026-11-01 review pass

- Provider deep research was not run in this pass; no `kdpD-deep-research-*.md` file exists.
  Evidence came from cached publications (most abstract-only; PMID:38622146 full text).
- Core functions: (1) phosphorelay sensor kinase toward KdpE [PMID:9099740, "Purified and
  reconstituted KdpD-His6 exhibited autokinase activity, and the phosphoryl group could be
  transferred to KdpE"]; (2) phospho-KdpE phosphatase, K+-modulated dual sensing
  [PMID:27320909, "is a dual sensor, which modulates its autokinase and phosphatase activities"];
  (3) N-terminal atypical serine kinase phosphorylating KdpB S162 [PMID:38622146, "the Walker
  A/B motif of the N-terminal KdpD domain functions as an ASK that phosphorylates KdpBS162"].
- Cytosol (IDA PMID:7499326, ISM PMID:1532388) and periplasmic space (IDA PMID:7499326) rows
  reflect topology of a multipass inner-membrane protein; MODIFY to plasma membrane. ARBA
  cytoplasm removed.
- All bare GO:0005515 rows removed per protein-binding policy (UspC, IIA(Ntr), KdpE, PhoR/PhoU).
- NEW: GO:0004721 phosphoprotein phosphatase activity (PMID:9099740) and GO:1901017 negative
  regulation of K+ transmembrane transporter activity (PMID:38622146).
