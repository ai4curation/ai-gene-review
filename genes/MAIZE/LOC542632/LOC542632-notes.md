# LOC542632 review notes

- 2026-10-28: fetched with `just fetch-gene MAIZE LOC542632`; UniProt id A0A804QUX9 as
  expected (GeneID 542632; EnsemblPlants Zm00001eb356600). GOA has 4 IEA rows
  (glutathione transferase activity, cytoplasm, cytosol, glutathione metabolic process).
  The older TrEMBL entry Q9FQB2 (same GeneID and RefSeq) carries the same terms plus IBA
  rows for GO:0004364, GO:0006749 and GO:0005737 (QuickGO check), consistent with this
  review.
- Key naming caveat: LOC542632 = McGonigle "GST 27" (tau, GSTU6, AF244692), NOT the
  classic phi GST-27 subunit of GST II/IV (P46420, GeneID 542311)
  [PMID:7858222 "GST IV a homodimer of 27 kDa subunits"]. Do not use P46420 biochemistry.
- Pang et al. papers [PMID:22792398 "were designed from the ORF region of ZmGST27
  (accession number AF244692)"] measure expression of this gene: induced by atrazine,
  2,4-D, primisulfuron, metolachlor and dichlormid; authors call this "a general response
  of this gene to chemical stress". Expression only -> no NEW process term (CLAUDE.md
  NEW bar).
- Actions: GO:0004364 ACCEPT (core; family signatures + conserved catalytic Ser19 in
  the tau G-site motif). GO:0005829 cytosol ACCEPT (non-core location). GO:0005737
  cytoplasm MODIFY -> cytosol (correct but general, gene already carries cytosol).
  GO:0006749 glutathione metabolic process KEEP_AS_NON_CORE.
- No upstream GO annotation error found, so no source_defects.
