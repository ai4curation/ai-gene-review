# A0A1S3BTE3 phylogenetic placement and catalytic-motif check

Script: `phylo_placement.py` (run with `uv run phylo_placement.py`); raw output in
`phylo_placement_output.txt`; alignment `mpk_aln.fasta` (MAFFT L-INS-i); NJ tree `mpk_nj.nwk`.

## Method

The melon target A0A1S3BTE3 (492 aa) was aligned with all 20 Arabidopsis thaliana MPKs
(UniProt sequences). Pairwise identity was computed over aligned non-gap columns, and a
neighbour-joining tree (BLOSUM62 distances, Biopython) was rooted on group C MPK1.
Arabidopsis PANTHER 19.0 subfamily ids come from the PANTHER classification file
PTHR19.0_arabidopsis. The target's own PANTHER subfamily could not be retrieved: the InterPro
API and the UniProt record give only the family PTHR24055, and melon is not a PANTHER
reference genome.

## Results

- Catalytic motifs are intact: glycine-rich loop GRGSYGVV (32-39), VAIK lysine K54, catalytic
  loop HRDLKP (D151), DFG (D169), and activation-loop phosphorylation motif TDY at 187-189.
- TDY places the protein in plant MAPK group D (groups A-C carry TEY). All eight Arabidopsis
  group D MPKs (MPK8, 9, 15-20) share 63-74% identity with the target; group A-C MPKs share
  43-47%.
- Highest identities: MPK19 (Q9LUC3, SF200) 0.735; MPK18 (Q9C5C0, SF420) 0.724; MPK20
  (Q9SJG9, SF392) 0.702.
- In the NJ tree the target groups with MPK18, MPK19 and MPK20. Within that clade it is sister
  to the MPK18 + MPK19 pair, with MPK20 outside them. The tree therefore makes it a co-ortholog
  of the MPK18/MPK19 pair. Its order relative to MPK18 and MPK19 is not resolved: the two
  identities differ by about 1%, and no bootstrap support was computed.
- In PANTHER, MPK18, MPK19 and MPK20 sit in three different subfamilies (SF420, SF200, SF392).
  Because the target's subfamily is unknown, this analysis cannot assign it to one of them.
- Length: 492 aa, versus 598-615 aa for MPK18/19/20. The kinase domain (25-316) is complete,
  so the difference lies in the C-terminal extension that is typical of group D MPKs. The
  492-aa size matches the CmMAPK19 gene model (MELO3C016139) in the melon genome-wide survey
  (PMID:32407323). It is the longest of the four RefSeq/UniProt products of LOC103492960
  (other entries are 410-423 aa).

## Interpretation

Family-wide features can be transferred: protein kinase chemistry, ATP binding, MAP kinase
activity and dual-phosphorylation activation. These rest on the PTHR24055 membership, the
MAPK PROSITE/InterPro signatures and the intact catalytic residues. Clade-specific functions
reported for Arabidopsis MPK18 (cortical microtubule function, PHS1 interaction, MKKK20
activation) should not be transferred, because the subfamily assignment is not resolved.
