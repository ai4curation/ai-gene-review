# HOXA2: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/HOXA2/HOXA2-bioinformatics/align.py genes/EQUAS/HOXA2/HOXA2-uniprot.txt O43364 genes/EQUAS/HOXA2/HOXA2-bioinformatics 143-202 94-99`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human canonical sequence (O43364) is fetched from UniProt REST and saved as O43364.fasta; the donkey sequence is parsed from the local UniProt flat file.

## Output

```
donkey A0A9L0JBM7 length 373; human O43364 length 376
aligned pairs 373; identical 364; identity over aligned pairs 97.59%
coverage of human 99.20%; coverage of donkey 100.00%
aligned blocks (donkey start-end : human start-end, 1-based):
  1-115 : 1-115
  116-373 : 119-376
donkey C-terminus: TTIDLQHLNY human C-terminus: TTIDLQHLNY
human region 143-202: 60 of 60 residues aligned, 60 identical
human region 94-99: 6 of 6 residues aligned, 6 identical
```

## Interpretation

The donkey HOXA2 model is 97.6% identical to human HOXA2 over 373 aligned residues, with a 3-residue deletion relative to human 116-118 outside the functional motifs. The homeodomain (human DNA-binding region 143-202) is 100% identical (60/60) and the Antp-type hexapeptide (human 94-99), which mediates PBX cofactor interaction in HOX proteins, is identical.

## Ortholog experimental GO annotations

`fetch_experimental_goa.py` retrieves experimental-evidence GO annotations for human O43364 and mouse P31245 from QuickGO (raw TSV: ortholog_experimental_goa.tsv; one line per annotation: ortholog_experimental_goa.txt). These are the experimental sources behind the donkey Ensembl Compara (GO_REF:0000107) transfers.

Reproduce: `uv run python genes/EQUAS/HOXA2/HOXA2-bioinformatics/fetch_experimental_goa.py genes/EQUAS/HOXA2/HOXA2-bioinformatics/ortholog_experimental_goa.tsv O43364,P31245`
