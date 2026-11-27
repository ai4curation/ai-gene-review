# B8BAB0 re-review bioinformatics (2026-10-20)

Independent of any ProtNLM2 output. Scripts in this folder, run with
`uv run --with biopython python <script>`; raw outputs are kept next to them
(`RESULTS-rereview-raw.tsv`, `panther_tree_placement_rereview.out`,
`motif_scan_rereview.out`, `align_vs_osburp12_rereview.out`).

## 1. Identity: B8BAB0 is the indica gene model of OsBURP12 (Os08g0380100)

`compare_sequences_rereview.py` (global alignment, BLOSUM62, gap -10/-0.5):

| comparator | identity over aligned pairs | identity over B8BAB0 length |
|---|---|---|
| Q6ZA27 OsBURP12 (japonica Os08g0380100, SF2) | 0.956 (568/594) | 0.912 |
| Q6K2M1 OsBURP14 (SF4) | 0.636 | 0.604 |
| Q40161 tomato PG1 beta subunit GP1 (SF2) | 0.530 | 0.496 |
| Q7XES5 OsBURP16 (SF2, 344 aa) | 0.521 | 0.283 |
| O80760 Arabidopsis PGL2 (SF2) | 0.504 | 0.465 |
| P92990 Arabidopsis PGL3 (SF10) | 0.528 | 0.493 |
| P92982 Arabidopsis PGL1 (SF10) | 0.509 | 0.474 |

B8BAB0 (OsI_29064, indica chromosome 8, 623 aa) and Q6ZA27 (japonica chromosome 8,
627 aa) are near-identical outside two blocks, so B8BAB0 is the indica allele / gene
model of OsBURP12.

`align_vs_osburp12_rereview.py` locates the differences:

- N-terminal propeptide region: B8BAB0 lacks about 31 residues present in Q6ZA27
  (Q6ZA27 residues ~92-134), a segment that contains one of the FTNYG repeat units
  of Q6ZA27; the sequences around it are divergent over a short stretch.
- C-terminus: after the shared sequence ending "FIALGGKPGEVEV" (B8BAB0 residue 581),
  B8BAB0 has a 42-residue tail (TGFGHNAGLLIPKPCMLMLMRVLLEKRACALKYNGSLSELMR) that does
  not align with the Q6ZA27 C-terminus (CHWIFEGDMTWTVAD). The Q6ZA27 tail carries the
  fourth CH motif of the BURP domain.

`motif_scan_rereview.py`: B8BAB0 has 3 CH dipeptides in its BURP region (positions
514, 526, 555), whereas Q6ZA27, tomato GP1 and Arabidopsis PGL2 each have 4 (for
Q6ZA27: 545, 557, 586, 613). The fourth CH, conserved in all three comparators, is
missing from B8BAB0 because of the divergent C-terminal tail. The divergent tail is
most likely a gene-model difference (for example a different splice acceptor or
read-through in the indica BGI annotation BGIOSGA028580) rather than conserved
biology, but this was not tested against indica transcript evidence here. Either
way, B8BAB0 as recorded is an alternative gene model with an incomplete BURP domain
relative to its japonica allele and to characterised SF2 members.

The variable region of B8BAB0 contains the PG1 beta repeat: 19 FxxY units and 3
strict F[TS]xYG units (starts 215, 229, 243), as in tomato GP1 (21 FxxY, 6 F[TS]xYG)
and Arabidopsis PGL2 (21 FxxY, 5 F[TS]xYG). OsBURP16 (Q7XES5, 344 aa) has none of
these repeats in its UniProt sequence, which consists of a BURP-domain-centred
protein lacking the repeat-rich region.

## 2. Phylogenetic placement (PANTHER 19 tree, `panther_tree_placement_rereview.py`)

B8BAB0 itself (indica TrEMBL) is not a PANTHER reference leaf; its japonica allele
Q6ZA27 was used as its proxy.

- Q6ZA27 OsBURP12 path: Tracheophyta PTN007882607 > Magnoliophyta PTN000779096 >
  Mesangiosperma PTN004827825 > Liliopsida PTN004827826 > commelinids PTN004827828 >
  duplication PTN002050022 > Poaceae PTN002050027 > BEP clade PTN002050028 >
  duplication PTN000779097 > leaf.
- Closest paralog: OsBURP16 (Q7XES5), last common ancestor at the grass
  duplication PTN000779097.
- Next: OsBURP14 (Q6K2M1, SF4), last common ancestor at the commelinid duplication
  PTN002050022.
- Tomato GP1, Arabidopsis PGL1/PGL2/PGL3: last common ancestor with OsBURP12 at the
  Mesangiosperma speciation node PTN004827825 (i.e. the monocot-eudicot split). No
  one-to-one eudicot ortholog of OsBURP12 can be read off the tree; the grass and
  eudicot PG1beta-like copies diversified independently.
- The only PAINT IBD in this family (PTN004827911; GO:0009505 plant-type cell wall,
  GO:0009827 plant-type cell wall modification, GO:0042547 cell wall modification
  involved in multidimensional cell growth; seed AT1G70370 = PGL3) is the Brassicaceae
  node above PGL1 and PGL3 (SF10). OsBURP12 / B8BAB0 do not descend from it
  (under_PTN004827911=False), nor do Arabidopsis PGL2 or tomato GP1. PAINT curators
  therefore did not propagate cell wall terms to the grass PG1beta-like clade.

## 3. Interpretation

- B8BAB0 belongs to the PG1beta-like (PTHR31458) BURP family by HMM membership, the
  repeat-rich variable region and the BURP domain; this supports secretion and,
  by family-level evidence (tomato GP1 purified from cell walls; AtPGL3-GFP in the
  cell wall), a cell-wall location.
- Molecular activity is not established for any grass member: OsBURP16 overexpression
  raises PG activity and lowers pectin, but this is an in planta overexpression
  phenotype of a paralog, and the tomato beta subunit "apparently regulates" PG2.
  No transfer of an enzyme-regulator activity is warranted.
- The B8BAB0 gene model lacks the fourth BURP CH motif present in its japonica allele.
