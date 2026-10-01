# PANTHER / TreeGrafter, PTHR24027: choanoflagellate cadherins grafted onto a Bilateria-restricted node

**Destination:** PANTHER team (pantherdb.org feedback), copied to PAINT curators.

**Summary.** The cached PAINT slice `interpro/panther/PTHR24027/PTHR24027-paint.tsv`
records node PTN000616280 at `taxon:33213` (Bilateria). Its IBDs, seeded by
classical cadherins from mouse, rat, human and zebrafish, are:
- GO:0005912 adherens junction
- GO:0000902 cell morphogenesis
- GO:0007043 cell-cell junction assembly
- GO:0016339 calcium-dependent cell-cell adhesion via plasma membrane cell
  adhesion molecules
- GO:0034332 adherens junction organization
- GO:0044331 cell-cell adhesion mediated by cadherin

TreeGrafter nonetheless grafts three *Salpingoeca rosetta* cadherins in
subfamily PTHR24027:SF422 onto this node. Each receives 10 IEA rows
(GO_REF:0000118), 30 in all:

| Protein | Pfam domains |
|---|---|
| F2UD23 | cadherin repeats, SH2 |
| F2UFV3 | cadherin repeats, laminin G |
| F2USU1 | cadherin repeats, tyrosine phosphatase |

Separately, node PTN008601603 gives *Monosiga brevicollis* A9V8Y4 five IBA rows
(beta-catenin binding, catenin complex, cadherin binding, cell migration,
cell-cell adhesion).

**Evidence.**
- None of the four proteins has PF01049, the cytoplasmic domain that binds
  beta-catenin. A UniProt census finds 0 PF01049 proteins in Choanoflagellata,
  Filasterea and Ichthyosporea, against 23,575 in Metazoa
  (`genes/human/CDH1/CDH1-bioinformatics/`).
- Choanoflagellates lack classical cadherins (PMID:22837400, PMID:27189570),
  and *S. rosetta* colonies have no adherens-junction-like structures
  (PMID:22837400).

**Requested change.**
- Explain why SF422 proteins graft onto a node labelled Bilateria, and graft
  them onto a pre-bilaterian cadherin node instead.
- Move the PTN008601603 catenin and junction IBDs below the choanoflagellate
  split.
