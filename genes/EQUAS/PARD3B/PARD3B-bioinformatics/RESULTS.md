# PARD3B: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/PARD3B/PARD3B-bioinformatics/align.py genes/EQUAS/PARD3B/PARD3B-uniprot.txt Q8TEW8 genes/EQUAS/PARD3B/PARD3B-bioinformatics 1-82 201-289 383-468 498-585`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human canonical sequence (Q8TEW8) is fetched from UniProt REST and saved as Q8TEW8.fasta; the donkey sequence is parsed from the local UniProt flat file.

## Output

```
donkey A0A9L0JEY6 length 1204; human Q8TEW8 length 1205
aligned pairs 1202; identical 1061; identity over aligned pairs 88.27%
coverage of human 99.75%; coverage of donkey 99.83%
aligned blocks (donkey start-end : human start-end, 1-based):
  1-180 : 1-180
  181-890 : 184-893
  893-1204 : 894-1205
donkey C-terminus: RQKDPMTAAV human C-terminus: RQKNPMTAAV
human region 1-82: 82 of 82 residues aligned, 77 identical
human region 201-289: 89 of 89 residues aligned, 88 identical
human region 383-468: 86 of 86 residues aligned, 85 identical
human region 498-585: 88 of 88 residues aligned, 84 identical
```

## Interpretation

The donkey PARD3B model spans the full length of human PARD3B (Q8TEW8) at 88.3% identity. Divergence is concentrated outside the folded domains: the N-terminal region containing the Par3/HAL N-terminal domain (human 1-82) is 77/82 identical, and the three PDZ domains (human 201-289, 383-468, 498-585) are 88/89, 85/86 and 84/88 identical. The donkey model corresponds to the full-length human isoform 1 (no isoform-specific deletions).

## Ortholog experimental GO annotations

`fetch_experimental_goa.py` retrieves experimental-evidence GO annotations for human Q8TEW8 and mouse Q9CSB4 from QuickGO (raw TSV: ortholog_experimental_goa.tsv; one line per annotation: ortholog_experimental_goa.txt). Apart from protein binding and generic complex/cell-junction rows, no experimental GO annotation exists for either PARD3B ortholog.

Reproduce: `uv run python genes/EQUAS/PARD3B/PARD3B-bioinformatics/fetch_experimental_goa.py genes/EQUAS/PARD3B/PARD3B-bioinformatics/ortholog_experimental_goa.tsv Q8TEW8,Q9CSB4`
