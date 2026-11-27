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


## 2026-11-07 E. coli Kdp module consultation

Reviewed all existing annotation claims against the cached primary literature, UniProt record, and current GO definitions. Original ordered annotation payloads and source files were frozen before editing; no new annotation rows were added. The two inherited KdpD NEW proposals remain present. Detailed decisions and source scope are recorded in `analysis/module_audits/bacterial_kdp_potassium_homeostasis/ecoli-consultation/`.

A genuine configured Falcon research request was attempted for this gene and failed with HTTP 403 authentication; no provider report was fabricated. The exact attempt log is `.cache/module-audit-logs/kdp-20261107/ecoli-consultation/falcon-kdpD.log`. PAINT-loss checking found no IRD/IKR loss on the recorded lineage.

The generic phosphotransferase refinement now includes both established sensor-histidine-kinase and serine-kinase activities. PMID:38622146 establishes the E. coli KdpD-to-KdpB inhibitory output; short Deinococcus KdpD/c-di-AMP regulation is not transferred to this protein. GO:0005737 currently explicitly excludes plasma membrane; the electronic cytoplasm row therefore remains REMOVE, with whole-protein topology distinguished from cytoplasm-facing domains. Homodimerization is core support for trans-autophosphorylation (PMID:9858704). Both inherited NEW rows are unchanged in presence and source payload.
