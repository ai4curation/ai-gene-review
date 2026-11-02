# PTHR13158 (NAD kinase 2, mitochondrial): tree, membership and catalytic-motif survey

Script: `family_survey.py` (this folder). Raw output: `family_survey.out`; tables:
`reference_tree.tsv`, `member_summary.tsv`, `nadk_paralogs.tsv`. Data were fetched live
from the PANTHER treeinfo API (PANTHER 19) and UniProtKB REST on 2026-11-02.

## 1. PANTHER reference tree

The reference tree has 40 leaves. The family root PTN004406956 is a HORIZ_TRANSFER
node and is also the SF5 subfamily node. It has two children: the eukaryotic node
PTN000994636 (39 leaves) and a single bacterial leaf, Leptospira interrogans LB_063
(UniProtKB Q8EXZ4).

- PTN004406956 carries the PAINT IBDs for NAD+ kinase activity (GO:0003951) and
  NAD+ metabolic process (GO:0019674); every leaf descends from it, including the
  Leptospira leaf.
- PTN000994636 (Eukaryota) carries the PAINT IBD for mitochondrion (GO:0005739). It
  contains bilaterians, a choanoflagellate (Monosiga brevicollis, two leaves), and an
  alveolate/stramenopile pair (Plasmodium falciparum PF3D7_0913300, Phytophthora ramorum).
- SF4 ("NAD(+) KINASE") is a nematode-only clade (C. elegans and C. briggsae nadk-1,
  Pristionchus WBGene00276985) that arose by a duplication within nematodes
  (PTN000463660); its sister clade holds the nematode nadk-2 genes in SF5.
- The seeds of all three PAINT IBDs are mammalian (human Q4G0N4 and mouse MGI:1915896).

## 2. UniProtKB membership by lineage and motif

3234 UniProtKB proteins carry a PTHR13158 cross-reference (4 reviewed: human, mouse,
rat and Xenopus tropicalis NADK2). About a third are bacterial.

| lineage | subfamily | GGDGT | GQDGL | other G-x-D-G | none |
|---|---|---|---|---|---|
| Metazoa | SF5 | 1575 | 0 | 16 | 284 |
| Metazoa | SF4 | 78 | 0 | 1 | 19 |
| Other eukaryotes | SF5 | 91 | 0 | 1 | 18 |
| Viridiplantae | SF5 | 8 | 0 | 0 | 0 |
| Bacteria | SF5 | 8 | 936 | 95 | 73 |
| Bacteria | SF4 | 0 | 17 | 14 | 0 |

The canonical NAD kinase motif reads GGDGT in human NADK2 (residues 159-163,
catalytic Asp161). Almost every eukaryotic member with a detectable motif carries it,
including the nematode SF4 nadk-1 proteins. In bacterial members the common form is
GQDGL, where Gln replaces the second Gly. Only 8 of 1112 bacterial SF5 members have the
Pfam NAD_kinase domain PF01513; eukaryotic members mostly have it (see
`member_summary.tsv`). The PANTHER reference leaf Leptospira LB_063 (Q8EXZ4) has
GGDN at 123-126, where Asn replaces the last Gly, and UniProt names it "Sugar kinase".
"none" means the regex found no G-x-D-G anywhere; these are mostly fragments or divergent
gene models and were not examined further.

Spot positions used as residue-site controls (from the live UniProt sequences):

- Q4G0N4 (human NADK2, SV 2): GGDGT at 159; D161.
- Q8C5H8 (mouse Nadk2, SV 2): GGDGT at 147; D149.
- Q9N4A9 (C. elegans nadk-1, SF4, SV 2): GGDGT at 121; D123.
- Q8I319 (P. falciparum PF3D7_0913300, SV 1): GGDGT at 199; D201.
- A0A086PAA9 (Sphingobium herbicidovorans, bacterial SF5, SV 1): GQDGL at 91; Q92.
- Q8EXZ4 (Leptospira interrogans LB_063, SV 2): GGDN at 123; N126.

## 3. NAD kinase paralogs per genome (Pfam PF01513)

| organism | PTHR13158 | PTHR20275 (cytosolic NADK / Pos5 family) |
|---|---|---|
| Homo sapiens | 3 | 12 |
| Mus musculus | 5 | 5 |
| Drosophila melanogaster | 0 | 16 |
| Caenorhabditis elegans | 3 | 0 |

Counts are UniProtKB entries, so isoform entries and TrEMBL duplicates inflate them.
Drosophila Nadk2 is in PTHR13158 but its UniProt entries carry no PF01513
cross-reference, so it does not appear in this column. The C. elegans result is the
notable one: all of its PF01513 proteins (nadk-1 Q9N4A9 and the nadk-2 entries) are in
PTHR13158, and none is in PTHR20275. C. elegans therefore has no member of the family that
contains cytosolic NADK, and the nematode-specific SF4 paralog nadk-1 is a candidate for
the cytosolic role. Its localisation has not been tested.

## Interpretation and limits

- The eukaryotic clade under PTN000994636 is uniformly NADK2-like at the catalytic motif,
  and the only experimental data (human, mouse) are from it.
- The bacterial members join the tree at a horizontal-transfer root and carry a variant
  motif without a PF01513 match. Whether they phosphorylate NAD+ has not been tested; the
  motif result shows divergence, not loss of activity.
- Motif calls come from a regex, not a multiple alignment. The control positions listed
  above were read from the sequence context of each hit, which aligns unambiguously to the
  human GGDGT block.
