# BT_3328 bioinformatics

## Purpose

Check that the KBase Dark Protein Atlas query `CAKXSP010000006.1_105` (an
environmental *Bacteroides thetaiotaomicron* assembly, annotated by eggNOG and
InterPro only as "Domain of unknown function (DUF4955)") is the same gene as
UniProt Q8A2H7 (BT_3328, BtCDH, the founding member of polysaccharide lyase
family PL29), and record the sequence features used in the review.

## Method

`align.py` makes a global BLOSUM62 alignment (Biopython PairwiseAligner, gap
open -10, extend -0.5) of the UniProt sequence in `../BT_3328-uniprot.txt`
against the query sequence `CAKXSP010000006.1_105.fasta`, taken from the
dashboard's review page. Output is in `align_output.txt`.

```
uv run python align.py ../BT_3328-uniprot.txt CAKXSP010000006.1_105.fasta
```

## Results

- Both sequences are 868 aa. The alignment has no gaps; 858 of 868 positions
  are identical (98.8% identity). The 10 differences are conservative or
  surface substitutions scattered along the chain:
  T170A L233F P321L I397V A541V S567A D675N A705T G779S V823M.
- The N-terminus `MKKVISIICITLLVALYSCDERDDL` carries a lipoprotein signal peptide
  with lipobox `LYSC` and Cys19 as the predicted lipidated residue, as in the
  UniProt LIPID feature at position 19 (PROSITE PS51257). The residues after
  Cys19 are acidic (`DERDD`), the pattern of the *Bacteroides* lipoprotein
  export signal that sends lipoproteins to the cell surface.
- InterProScan on the query (KBase run) finds Pfam PF16378 (DUF4988) at
  25-199 and PF16315 (DUF4955) at 716-867 (E = 2.8e-69). These are the only
  domain annotations; neither Pfam entry is linked to a function.

## Conclusion

The query is an allele of BT_3328 from another *B. thetaiotaomicron* strain,
so the experimental characterisation of BT_3328 applies directly to it.
DeepTMHMM in the KBase run classified the protein as soluble and secreted
(signal peptide 1-18). That conflicts with the lipobox and with the measured
cell-surface location (PMID:30262663), so it is probably a mis-call of a
lipoprotein signal peptide.
