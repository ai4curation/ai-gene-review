# PTHR13158 (NAD kinase 2, mitochondrial): tree, membership and catalytic-motif survey

Script: `family_survey.py` (this folder; re-run 2026-11-02 after adding the PANTHER-based paralog query). Raw output: `family_survey.out`; tables:
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

Pfam NAD_kinase domain (PF01513) coverage is the sharpest contrast between the
eukaryotic and bacterial members:

| lineage | subfamily | with PF01513 |
|---|---|---|
| Metazoa | SF5 | 1350/1875 (72%) |
| Metazoa | SF4 | 77/98 (79%) |
| Other eukaryotes | SF5 | 34/110 (31%) |
| Viridiplantae | SF5 | 8/8 (100%) |
| Bacteria | SF5 | 8/1112 (1%) |
| Bacteria | SF4 | 0/31 (0%) |

The motif result corroborates this. The canonical NAD kinase block reads GGDGT in human
NADK2 (residues 159-163, catalytic Asp161), and almost every eukaryotic member with a
detectable block carries it, including the nematode SF4 nadk-1 proteins. In bacterial
members the common form is GQDGL: Gln replaces the second glycine, while the catalytic
Asp is retained. The PANTHER reference leaf Leptospira LB_063 (Q8EXZ4) has GGDN at
123-126, where Asn replaces the last glycine and the Asp is again retained; UniProt names
it "Sugar kinase". UniProt names many other bacterial members "Inorganic
polyphosphate/ATP-NAD kinase" or "NAD kinase" (for example A0A086PAA9); these names are
automatic and untested. "none" means the regex found no G-x-D-G anywhere; these are
mostly fragments or divergent gene models and were not examined further.

Spot positions used as residue-site controls (from the live UniProt sequences):

- Q4G0N4 (human NADK2, SV 2): GGDGT at 159; D161.
- Q8C5H8 (mouse Nadk2, SV 2): GGDGT at 147; D149.
- Q9N4A9 (C. elegans nadk-1, SF4, SV 2): GGDGT at 121; D123.
- Q8I319 (P. falciparum PF3D7_0913300, SV 1): GGDGT at 199; D201.
- A0A086PAA9 (Sphingobium herbicidovorans, bacterial SF5, SV 1): GQDGL at 91; Q92.
- Q8EXZ4 (Leptospira interrogans LB_063, SV 2): GGDN at 123; N126.

## 3. NAD kinase paralogs per genome (by PANTHER cross-reference)

Each organism was queried for UniProtKB entries cross-referenced to PTHR13158 and to
PTHR20275 (the family holding cytosolic NADK and fungal Pos5). This query does not depend
on Pfam, so it also finds entries whose Pfam cross-reference is missing (Drosophila
Nadk2, for example, has no PF01513 cross-reference). Counts are UniProtKB entries, so
isoform entries and TrEMBL duplicates inflate them; the gene names are what matter.

| organism (taxid) | PTHR13158 genes | PTHR20275 genes |
|---|---|---|
| Homo sapiens (9606) | NADK2 (SF5) | NADK (SF0) |
| Mus musculus (10090) | Nadk2 (SF5) | Nadk (SF0) |
| Drosophila melanogaster (7227) | Nadk2 (SF5) | Nadk1a, Nadk1b (SF0) |
| Caenorhabditis elegans (6239) | nadk-2 (SF5: Q9XXI5, Q9XXI6), nadk-1 (SF4: Q9N4A9) | none |
| Plasmodium falciparum 3D7 (36329) | PF3D7_0913300 (SF5) | none |

The species-level taxid for P. falciparum (5833) returns no entry for either family,
because UniProt files the reference proteome under the strain taxid; the strain taxid
36329 was used instead. No queried organism was dropped.

C. elegans has two NAD kinase genes, both in PTHR13158 and none in PTHR20275. nadk-2 is
in SF5 with the vertebrate NADK2 orthologs; nadk-1 is the nematode-specific SF4 paralog.
Because nematodes have no member of the cytosolic NADK family, one of these two must
supply cytosolic NADP+ if C. elegans has a cytosolic NAD kinase at all, and nadk-1, the
paralog outside the NADK2 orthogroup, is the more likely candidate. Neither gene's
localisation has been tested. P. falciparum likewise has a single NAD kinase, in this
family, with no PTHR20275 member.

## Interpretation and limits

- The eukaryotic clade under PTN000994636 is uniformly NADK2-like at the catalytic motif,
  and the only experimental data (human, mouse) are from it.
- The bacterial members join the tree at a horizontal-transfer root. Only 1% match Pfam
  PF01513 (against 72% of metazoan SF5 members), and most substitute the second glycine
  of the GGDG block while keeping the catalytic Asp. Whether they phosphorylate NAD+ has
  not been tested; these results show divergence, not loss of activity.
- Motif calls come from a regex, not a multiple alignment. The control positions listed
  above were read from the sequence context of each hit, which aligns unambiguously to the
  human GGDGT block.
