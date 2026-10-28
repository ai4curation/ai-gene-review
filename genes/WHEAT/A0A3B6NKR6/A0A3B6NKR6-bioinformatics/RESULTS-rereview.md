# A0A3B6NKR6 re-review bioinformatics (2026-10-21)

Analyses written for the full re-review; they are independent of any ProtNLM2 output.

## 1. PANTHER placement

- The UniProt record places A0A3B6NKR6 in PANTHER PTHR38710 / PTHR38710:SF1 (the only subfamily).
- `interpro/panther/PTHR38710/PTHR38710-entries.csv` places both Arabidopsis glucuronokinases,
  Q93ZC9 (GLCAK1, At3g01640) and Q9LY82 (GLCAK2, At5g14470), in the same subfamily PTHR38710:SF1.
- PANTHER 19 tree (`panther_tree_PTHR38710.json`, from the pantherdb.org treeinfo service; parsed by
  `trace_panther_tree.py`, output `trace_panther_tree.out`): the tree served contains 17 reference-genome
  leaves (no Arabidopsis or wheat leaf in this download). Root PTN008673760 (Eukaryota) splits into a
  Metazoa-Choanoflagellida clade (PTN001475528) and a Viridiplantae clade (PTN008673762) containing
  Chlamydomonas, Klebsormidium, Marchantia, Selaginella, a Liliopsida node (PTN009162939: Zostera marina,
  Zea mays) and a Pentapetalae node (PTN009162941). Of the 16 internal events, 15 are speciation and
  1 is a duplication (PTN008103557, two Selaginella paralogs). So there is no duplication separating
  the grass and eudicot glucuronokinases: the wheat protein (a grass, like Zea mays) and the
  Arabidopsis enzymes are orthologous members of one seed-plant clade.

## 2. PAINT nodes

`interpro/panther/PTHR38710/PTHR38710-paint.tsv`:

| node | term | seeds |
|---|---|---|
| PTN000048555 | GO:0005829 cytosol; GO:0004496 mevalonate kinase activity; GO:0019287 IPP biosynthesis, mevalonate pathway | mouse Mvk (MGI:107624), rat Mvk, yeast ERG12 (Q03426 / S000004821) |
| PTN001475528 | GO:0047940 glucuronokinase activity | zebrafish si:dkey-105h12.4 (ZDB-GENE-080204-36) |
| PTN008680403 | GO:0047940 glucuronokinase activity | Arabidopsis AT3G01640 (GLCAK1), dated 2026-06-17 |

PTN000048555 does not occur in the PTHR38710 tree (`trace_panther_tree.out`). It is a node seeded by
mevalonate kinases, which belong to a different GHMP family. The cytosol IBA that A0A3B6NKR6 (and both Arabidopsis
GLCAKs) carries therefore comes from a mevalonate-kinase node, not from a glucuronokinase node. The
glucuronokinase-activity IBD at PTN008680403 is too recent to appear in the PANTHER 19 tree download,
and the wheat GOA file (snapshot used for this review) carries no IBA for GO:0047940, so this analysis
cannot confirm that the wheat leaf descends from PTN008680403.

## 3. Sequence comparison (`pairwise_identity_rereview.py`, output `pairwise_identity_rereview.out`)

Global alignment (BLOSUM62) of the full-length sequences:

- A0A3B6NKR6 (360 aa) vs GLCAK1 Q93ZC9 (362 aa): 65.2% identity over aligned columns.
- A0A3B6NKR6 vs GLCAK2 Q9LY82 (366 aa): 66.0% identity.
- GLCAK1 vs GLCAK2: 81.5% identity. This is a lineage-specific (eudicot/Brassicaceae) paralog pair,
  so the wheat protein is equally related to both.
- The GHMP phosphate-binding glycine-rich loop motif GLSGSSA is conserved in all three
  (wheat position 124; Arabidopsis position 130).

The wheat protein is full length relative to the characterised Arabidopsis enzymes (360 vs 362/366 aa),
and contains both Pfam GHMP domains (N 97-181, C 257-327). It is not a fragment.
