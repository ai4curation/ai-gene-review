# Choanoflagellate cadherins with propagated classical-cadherin terms

Script: `cadherin_nodes.py` (run 2026-10-02; raw output in
`cadherin_nodes_output.txt`). It queries the public PANTHER tree API for
PTHR24027, the InterPro REST API for Pfam matches, and the UniProt REST API for
sequences and features. Nothing is hardcoded.

Proteins: *Monosiga brevicollis* A9V8Y4 (MBCDH12, MONBRDRAFT_11339) and
*Salpingoeca rosetta* F2UD23 (PTSG_05882), F2UFV3 (PTSG_06458) and F2USU1
(PTSG_11235).

## 1. PANTHER nodes behind the propagated rows

| Node | PANTHER species label | Leaves | Unicellular leaves |
|---|---|---:|---|
| PTN008601603 (family root) | Metazoa-Choanoflagellida | 580 | 1, *M. brevicollis* A9V8Y4 |
| PTN000616280 | Bilateria | 524 | none; all leaves are bilaterians |

- PTN008601603 is the root of the PTHR24027 reference tree. A9V8Y4 is a leaf
  attached directly to it. That is why the IBDs placed at the root (beta-catenin
  binding, catenin complex, cadherin binding, cell migration, cell-cell adhesion)
  reach A9V8Y4 as IBA rows.
- PTN000616280 sits four levels below the root (root > PTN009075361 >
  PTN001167681 [Eumetazoa] > PTN002771681 > PTN000616280). The PANTHER
  species label and the PAINT file (`taxon:33213`) agree that it is a Bilateria
  node. Its leaves are vertebrates plus a few insects, a tick, a leech, a sea
  urchin, amphioxus and *Ciona*.
- The three *S. rosetta* proteins are not in the reference tree (*S. rosetta*
  is not a PANTHER reference genome). TreeGrafter grafts them onto
  PTN000616280, outside the clade the node represents. They therefore inherit
  the six IBDs on PTN000616280 and the four MF/CC/BP IBDs from the root.

## 2. Pfam domains and the beta-catenin-binding domain

| Protein | Pfam domains | PF01049 (Cadherin_C) |
|---|---|---|
| A9V8Y4 | Cadherin, VWD, Vwde, EGF_2, IPT/TIG, SH2 | absent |
| F2UD23 | Cadherin, Vwde, EGF_Teneurin, SH2 | absent |
| F2UFV3 | Cadherin, fibronectin type II | absent |
| F2USU1 | Cadherin, protein-tyrosine phosphatase | absent |

F2UFV3 has a fibronectin type II domain, not a laminin G domain. None of the
four has the classical-cadherin cytoplasmic domain through which classical
cadherins bind beta-catenin. (See also `genes/human/CDH1/CDH1-bioinformatics/`:
0 PF01049 proteins in Choanoflagellata, Filasterea and Ichthyosporea.)

## 3. Topology and motif checks

| Protein | Length | TM | Cytoplasmic tail | Cadherin repeats | DXN[DE][NHD] | [LIVM]D[RYK]E |
|---|---:|---|---:|---:|---:|---:|
| A9V8Y4 | 1794 | 1559-1581 | 213 aa (SH2) | 6 | 0 | 0 |
| F2UD23 | 1856 | 1623-1645 | 211 aa (SH2) | 8 | 0 | 2 |
| F2UFV3 | 3697 | 3613-3635 | 62 aa | 23 | 13 | 10 |
| F2USU1 | 8158 | 7478-7502 | 656 aa (PTP) | 56 | 41 | 37 |

- **SH2 (A9V8Y4, F2UD23).** Both SH2 domains keep the arginine of the FLVR
  motif that binds the phosphate of phosphotyrosine: FVVRDS in A9V8Y4 and FIIRDY
  in F2UD23. In both proteins the SH2 domain is in the cytoplasmic tail, after
  the single TM helix.
- **PTP (F2USU1).** The phosphatase domain is cytoplasmic. It has the
  pTyr-recognition KNRY loop, a WPD loop and the catalytic VHCSAGVGRS signature
  (C8029 is the UniProt active-site cysteine). These features fit a classical,
  tyrosine-specific receptor PTP domain with an intact active site.
- **Calcium-binding motifs.** The cadherin repeats of F2UFV3 and F2USU1 carry
  many canonical DXNDN-type and LDRE-type calcium-binding motifs, and UniProt
  matches the PROSITE CADHERIN_1 signature in both. The repeats of A9V8Y4 and
  F2UD23 have no DXNDN-type motif and at most two LDRE-type motifs, and neither
  protein matches CADHERIN_1. Their cadherin-like repeats are divergent, so
  canonical calcium binding cannot be assumed for them.

## Limitations

- The motif counts are simple regular-expression scans. They do not use an
  alignment, so they can miss non-canonical calcium ligands.
- TreeGrafter was not re-run. The graft node comes from the GOA
  `supporting_entities` of each row.
