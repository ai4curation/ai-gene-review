# MDJ1 notes

## 2026-09-28 IBA rereview

- Checked the current PTHR43096 PAINT cache. The only current assertions at
  PTN002454318 are `GO:0005737` cytoplasm and `GO:0042026` protein refolding;
  the GOA `GO:0051082` IBA no longer appears in the current family snapshot.
- Kept the PTN002454318 protein-refolding IBA as a core transfer. MDJ1 is itself
  one of the yeast experimental descendants for the node, and the exact target
  in the source list is expected for IBA rather than circular.
- Modified the broad PTN002454318 cytoplasm IBA to `GO:0005759` mitochondrial
  matrix. The cytoplasm node is seeded partly by MDJ1's own matrix evidence and
  is a parent-location granularity issue rather than a wrong-compartment transfer.
- Treated `GO:0051082` unfolded protein binding as stale/obsolete terming and
  proposed `GO:0044183` protein folding chaperone for the IBA, IEA and IMP rows.
- Kept generic `GO:0005515` protein-binding IPI rows from Krogan 2006, Gong
  2009 and Zhong 2016 as `MARK_AS_OVER_ANNOTATED`: the interactions may be real,
  but they do not provide a specific molecular-function term for Mdj1.
- Searched 2024-2026 literature for `MDJ1`, `Mdj1`, and `YFL016C` with
  `Saccharomyces cerevisiae`. No newer direct functional paper was found; the
  recent hits use Mdj1 precursor/mature forms as an import or precursor-stress
  reporter rather than revising its core Ssc1 cochaperone role.

Key cached publications:

- Rowley et al. 1994 (PMID:8168133) first characterized Mdj1 as a mitochondrial
  DnaJ-family heat-shock protein; `mdj1` disruption caused petite formation,
  mtDNA loss, temperature-sensitive inviability, impaired folding of newly
  imported proteins, and reduced refolding of a thermolabile tester.
- Wagner et al. 1994 (PMID:7957078) placed Mdj1 and mt-Hsp70 upstream of PIM1 in
  mitochondrial misfolded-protein degradation by keeping substrates soluble and
  competent for proteolysis.
- Prip-Buus et al. 1996 (PMID:8603724) showed that absence of Mdj1 enhances
  heat-induced luciferase aggregation in isolated mitochondria.
- Westermann et al. 1996 (PMID:8943361) used `mdj1` mutants to show client
  chaperoning for newly synthesized mitochondrial proteins and for imported
  precursors after they enter the matrix.
- Kubo et al. 1999 (PMID:9973563) reconstituted protection and refolding of
  firefly luciferase with purified mature Ssc1p, Mdj1p and Yge1p.
