# APP: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/APP/APP-bioinformatics/align.py genes/EQUAS/APP/APP-uniprot.txt P05067 genes/EQUAS/APP/APP-bioinformatics 28-189 291-341 374-565 672-713 700-723 724-770`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human canonical sequence (P05067) is fetched from UniProt REST and saved as P05067.fasta; the donkey sequence is parsed from the local UniProt flat file.

## Output

```
donkey A0A9L0JJJ9 length 770; human P05067 length 770
aligned pairs 770; identical 754; identity over aligned pairs 97.92%
coverage of human 100.00%; coverage of donkey 100.00%
aligned blocks (donkey start-end : human start-end, 1-based):
  1-770 : 1-770
donkey C-terminus: TYKFFEQMQN human C-terminus: TYKFFEQMQN
human region 28-189: 162 of 162 residues aligned, 156 identical
human region 291-341: 51 of 51 residues aligned, 51 identical
human region 374-565: 192 of 192 residues aligned, 192 identical
human region 672-713: 42 of 42 residues aligned, 42 identical
human region 700-723: 24 of 24 residues aligned, 24 identical
human region 724-770: 47 of 47 residues aligned, 47 identical
```

## Interpretation

The donkey APP model is the 770-residue isoform and aligns end-to-end with human APP770 (P05067) at 97.9% identity. Human regions checked: E1 domain (28-189) 156/162 identical; BPTI/Kunitz protease-inhibitor domain (291-341) 51/51 identical; E2 domain (374-565) 192/192 identical; amyloid-beta 1-42 (672-713) 42/42 identical, so the donkey peptide has the human-type sequence (DAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVVIA) rather than the rodent variant; transmembrane region and intracellular domain (700-770) identical, including the YENPTY motif.

## Ortholog experimental GO annotations

`fetch_experimental_goa.py` retrieves experimental-evidence GO annotations for human P05067, mouse P12023 and rat P08592 from QuickGO (raw TSV: ortholog_experimental_goa.tsv; one line per annotation: ortholog_experimental_goa.txt). These include the experimental sources behind the donkey Ensembl Compara (GO_REF:0000107) transfers.

Reproduce: `uv run python genes/EQUAS/APP/APP-bioinformatics/fetch_experimental_goa.py genes/EQUAS/APP/APP-bioinformatics/ortholog_experimental_goa.tsv P05067,P12023,P08592`
