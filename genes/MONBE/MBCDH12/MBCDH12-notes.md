# MBCDH12 (Monosiga brevicollis, A9V8Y4) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment), so no `-deep-research-*.md` file exists. These notes were written on
2026-10-02 from the cached publications, the UniProt record and the analysis in
`MBCDH12-bioinformatics/` (`cadherin_nodes.py`; see RESULTS.md). This protein was reviewed
together with the S. rosetta cadherins PTSG_05882, PTSG_06458 and PTSG_11235.

## Identity and architecture

- A9V8Y4, TrEMBL, 1794 aa. Gene name MBCDH12 (EMBL EDQ85956.1), ORF MONBRDRAFT_11339.
- Signal peptide 1-20. VWFD 140-326. Six cadherin repeats 691-1319. IPT/TIG and EGF domains.
  TM 1559-1581. Cytoplasmic SH2 1627-1727, with an FLVR arginine (FVVRDS).
- No canonical calcium motifs and no CADHERIN_1 match. UniProt carries a "lacks conserved
  residue(s)" caution.
- No PF01049 (Cadherin_C).
- *M. brevicollis* is strictly unicellular
  [PMID:18273011 "Although M. brevicollis is strictly unicellular, other choanoflagellates facultatively form colonies"].
  It has at least 23 cadherin genes
  [PMID:18273011 "At least 23 M. brevicollis genes encode one or more cadherin domains"].
- The MBCDH names come from Abedin & King 2008 (PMID:18276888). Only the abstract is cached,
  so the paper's description of MBCDH12 could not be read.

## PANTHER and Track C

- *M. brevicollis* is a PANTHER reference genome. A9V8Y4 is the only choanoflagellate leaf
  in the PTHR24027 tree, and it attaches directly to the root PTN008601603
  ("Metazoa-Choanoflagellida", 580 leaves).
- The five IBA rows come from IBDs placed at that root:
  - beta-catenin binding, seeded by classical cadherins;
  - catenin complex;
  - cadherin binding;
  - cell migration, seeded by classical cadherins plus DCHS1;
  - cell-cell adhesion.
- Unlike the S. rosetta grafts, the target is inside the IBD clade. The argument is therefore
  against node placement, backed by target-specific evidence: there is no Cadherin_C domain
  (so no beta-catenin binding), and M. brevicollis is strictly unicellular.
- Actions:
  - REMOVE: beta-catenin binding, catenin complex.
  - MARK_AS_OVER_ANNOTATED: cadherin binding, cell migration, cell-cell adhesion (IBA and
    IEA), homophilic cell-cell adhesion.
  - UNDECIDED: calcium ion binding.
  - ACCEPT: membrane.
- Recommendation for PAINT: move the PTN008601603 catenin IBDs onto the classical-cadherin
  subtree.
