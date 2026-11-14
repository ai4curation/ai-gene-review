# DDR clade of PTHR24416: kinase and collagen-pocket residues on the PANTHER tree

## Question

PAINT node PTN002400507 (taxon Eumetazoa) carries two IBDs that every DDR in the
tree inherits: GO:0038062 protein tyrosine kinase collagen receptor activity and
GO:0005518 collagen binding, both seeded only by vertebrate DDR1/DDR2. The
Drosophila Ddr gene review predicted from sequence that dipteran Ddr is a
pseudokinase and that the DDR2 collagen pocket is not conserved in invertebrates.
This analysis asks where on the PANTHER tree each change happened, so that the node
placement can be judged.

## Method

`ddr_catalytic_residues.py` loads the PTHR24416 tree from the PANTHER treeinfo API
(through `ai_gene_review.etl.panther_trees`), takes every leaf below PTN002400507
(71 leaves), fetches each leaf's UniProt sequence, aligns it globally (BLOSUM62) to
human DDR2 (UniProtKB:Q16832) and reports the residue aligned to:

- three canonical protein-kinase catalytic positions, located on DDR2 by motif
  search: the beta3 lysine (VAVK, Lys608), the catalytic-loop asparagine (HRDLATRN,
  Asn715) and the DFG aspartate (ADFG, Asp728); the HRD aspartate (Asp710) is shown
  for reference;
- the central residues of the DDR2 collagen-binding pocket from the DDR2
  DS domain-collagen structure (PMID:20004161): Trp52, Thr56, Asp69, the
  Cys73-Cys177 disulfide, Arg105 and Glu113.

Each leaf is classed, separately for the kinase triad and the pocket, as `kept`
(all positions have the DDR2 residue), `substituted` (at least one position has
another residue) or `not_covered` (no substitution, but a position falls in an
alignment gap, typically a fragmentary gene model). Every internal node of the DDR
subtree is then summarised. Run from the repository root:

```
uv run python interpro/panther/PTHR24416/PTHR24416-bioinformatics/ddr_catalytic_residues.py
```

Raw output is in `output.txt`. Four leaves have no current UniProt sequence (retired
accessions) and are counted as unavailable.

## Results

### Kinase catalytic residues

- The dipteran node PTN002400510 (Drosophila melanogaster Ddr Q59DZ7 and
  Anopheles gambiae A0A1S4GZW5) is the only internal node in the DDR subtree whose
  leaves all carry substitutions at all three catalytic positions: fly Ddr has
  A789/S897/S910, Anopheles S634/S741/T754 (output rows for PTN001230948 and
  PTN008618230). Both keep the HRD aspartate.
- Its sister clade PTN008618231 is three Tribolium castaneum paralogs. One
  (A0A139WLZ5) keeps all three residues (K648/N755/D768); one (A0A139WLW9) has
  His at the beta3 lysine but keeps the Asn and Asp; the third (A0A139WM16) is not
  covered at the beta3 position. The full triad loss is therefore placed at
  PTN002400510, not deeper.
- Elsewhere the triad is kept across the clade: vertebrate DDR1 and DDR2, Ciona,
  amphioxus, sea urchin, Tribolium D6WFT6, Daphnia E9HQT9, and the nematode DDR-2
  clade (C. elegans Q95ZV7 K554/N650/D663, C. briggsae, Pristionchus). Isolated
  single-leaf substitutions (gar W5M346, Daphnia E9HPD9, Trichoplax B3RNH4, leech
  T1G770) do not define a clade and several come from fragmentary or unusual gene
  models.

### Collagen-binding pocket

- Within the vertebrate DDR node PTN007801558 (49 leaves, DDR1 and DDR2 from gar,
  teleosts, Xenopus and amniotes) the pocket is kept in 42 of the 46 leaves with
  a sequence. Three have one substitution each, all in unreviewed models: platypus
  A0A6I8PFB1 (Lys at Thr56, with Trp52 not covered), Anolis H9GE80 (Pro at Asp69)
  and Anolis H9GJ02 (the conservative Ser at Thr56). One Anolis model does not cover
  Trp52.
- Outside vertebrates, every DDR with a covered pocket has substitutions at Trp52
  and/or Asp69, including the deuterostomes: Ciona F6RMP9 (H47), amphioxus
  A0A9J7LMZ0 (H51, V55), sea urchin A0A7M7RDB0 (Y54, A74); arthropods (Phe, Tyr or
  His at Trp52 and Gly at Asp69 in Tribolium, Daphnia, Drosophila and Anopheles);
  and nematodes (C. elegans DDR-2 F47, S65). Not every lineage has lost both: Ciona
  keeps Asp69 (D64) and C. briggsae A8XJG8 keeps Trp52 (W97, with F150 at Asp69). The
  Arg105-Glu113 salt bridge is conserved in every covered leaf, and the Cys73-Cys177
  disulfide in every covered leaf except C. briggsae A8XJG8 (S154 at Cys73). The
  cnidarian, placozoan and leech sequences do not cover the pocket.
- Alignment register check: in distant leaves the calls keep DDR2's spacings, for
  example fly Ddr C150/C254 (104 apart, as Cys73/Cys177) and R181/E189 (8 apart, as
  Arg105/Glu113), so the DS domain, not only the kinase domain, is aligned in frame.

## Interpretation

1. The catalytic triad is ancestral in the DDR clade and was lost on the dipteran
   branch at PTN002400510, after the split from the Tribolium paralogs. This is a
   key-residue loss of protein tyrosine kinase activity confined to that node.
2. The pocket that recognises the GVMGFO motif of fibrillar collagens is conserved
   only in the vertebrate DDR node PTN007801558. Sequence gives no support for
   transferring the vertebrate collagen-binding mode to invertebrate DDRs. It does
   not exclude collagen binding through another surface, which would need
   experimental evidence.
3. Both conclusions rest on sequence. No kinase or collagen-binding assay has been
   reported for any invertebrate DDR in the literature this repository has cached.
