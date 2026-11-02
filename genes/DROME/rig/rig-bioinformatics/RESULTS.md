# rig (Q86BY9) bioinformatics: retention of human GEMIN5 snRNA-contact residues

## Question

Human GEMIN5 recognises the Sm site of pre-snRNAs through aromatic and basic residues
of its N-terminal WD40 propellers (Xu et al. 2016, PMID:27881600): Trp14 and Tyr15 stack
Sm-site bases, Arg335, Met357, Arg359, Phe381, Met403 and Trp422 contact the 5' end
nucleotides, and Tyr474 stacks the m7G cap. Does Drosophila rig retain these residues,
which would be needed to transfer "snRNA binding" from the human protein?

## Evolutionary relationship

rig and human GEMIN5 both belong to PANTHER PTHR46362:SF1 (GEM-ASSOCIATED PROTEIN 5,
the family's only subfamily; UniProt DR PANTHER lines in both cached flat files), and rig
is an experimental donor (FB:FBgn0250850) to the PAINT node PANTHER:PTN005299808 that
supplies the Gemin5 IBAs. They are therefore orthologs; the question is whether a
particular molecular function was retained in the fast-evolving fly lineage.

## Method

`snrna_site_conservation.py` parses both sequences from the cached UniProt files and
runs a global Needleman-Wunsch alignment (Biopython PairwiseAligner, BLOSUM62, gap open
-10, extend -0.5), then reports the fly residue aligned to each human contact position.
A regex scan of the fly sequence for any Trp-Tyr dipeptide was also done.

Run: `uv run genes/DROME/rig/rig-bioinformatics/snrna_site_conservation.py`
Output: `snrna_site_conservation.json`.

## Results

- human 1508 aa, fly 1235 aa; 926 aligned residue pairs with 31.1% identity.
- Of 16 human contact residues checked, only Tyr474 (aligned to fly Tyr660) and Asn605
  (aligned to fly Asn762) are identical at the aligned position.
- The Sm-site stacking pair Trp14-Tyr15 aligns to fly Gly15-Asn16, and the fly sequence
  contains no Trp-Tyr dipeptide anywhere.
- Arg335, Met357 and Arg359 align to fly Lys473, Lys517 and Lys519; Trp422 and Leu580
  fall in alignment gaps.
- The region between human ~280 and ~460 aligns poorly, with long gaps on both sides,
  so individual position assignments there are low confidence.

## Interpretation

The canonical human Sm-site recognition residues of the first WD40 propeller are not
retained at aligned positions in rig, while the m7G-stacking tyrosine of the second
propeller may be. This is a pairwise comparison, not a family alignment, and it cannot
show whether rig binds snRNA by a different mode. It is consistent with the
biochemical finding that the fly SMN complex binds U snRNAs in S2 cells without stably
associated Rig (Kroiss et al. 2008, PMID:18621711). It does not support transferring
"snRNA binding" from human GEMIN5 to rig without fly-specific binding data.
