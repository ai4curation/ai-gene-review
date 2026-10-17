# NADK2: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/NADK2/NADK2-bioinformatics/align.py genes/EQUAS/NADK2/NADK2-uniprot.txt Q4G0N4 genes/EQUAS/NADK2/NADK2-bioinformatics`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human canonical sequence (Q4G0N4) is fetched from UniProt REST and saved as Q4G0N4.fasta; the donkey sequence is parsed from the local UniProt flat file.

## Output

```
donkey A0A9L0K2P4 length 506; human Q4G0N4 length 442
aligned pairs 410; identical 396; identity over aligned pairs 96.59%
coverage of human 92.76%; coverage of donkey 81.03%
aligned blocks (donkey start-end : human start-end, 1-based):
  97-383 : 1-287
  384-506 : 320-442
donkey C-terminus: DELRTVLLDQ human C-terminus: DELRTVLLEQ
```

## Interpretation

The donkey model A0A9L0K2P4 has a 96-residue N-terminal extension with no counterpart in human NADK2; donkey residues 97-383 align to human 1-287, so the region corresponding to the human mitochondrial transit peptide (human 1-62) is internal in the donkey model rather than at its N-terminus. The donkey model lacks the segment corresponding to human residues 288-319 (human sequence ASYYEISVDDGPWEKQKSSGLNLCTGTGSKAW), the same segment that is missing from human isoform 2 (VSP_027193). The GGDG motif of the NAD kinase family is retained (donkey GGDG at 255, aligned to human GGDG at 159). Whether a protein lacking the 288-319 segment is catalytically active has not been tested, and the N-terminal extension may reflect a gene-model start-site error; both are properties of this predicted sequence, not observations of donkey NADK2 protein.
