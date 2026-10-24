# dpm-1 re-review: isoform mapping and ortholog comparison

Sequences fetched live from UniProt REST by `compare_sequences_rereview.py`.

| Accession | Description | Length | Reviewed | PANTHER |
|---|---|---|---|---|
| U4PF58 | worm dpm-1 isoform b (benchmark) | 51 | UniProtKB unreviewed (TrEMBL) | PTHR43398;PTHR43398:SF1 |
| Q9TYJ7 | worm dpm-1 isoform a (canonical) | 239 | UniProtKB unreviewed (TrEMBL) | PTHR43398;PTHR43398:SF1 |
| O60762 | human DPM1 | 260 | UniProtKB reviewed (Swiss-Prot) | PTHR43398;PTHR43398:SF1 |
| P14020 | yeast DPM1 | 267 | UniProtKB reviewed (Swiss-Prot) | PTHR43398;PTHR43398:SF1 |

## U4PF58 vs canonical Q9TYJ7

U4PF58 is an exact substring of Q9TYJ7: canonical residues 189-239 of 239 (51 residues, 100% identity).

Q9TYJ7 sequence features (from UniProt):

| Type | Description | Start | End | Present in U4PF58 |
|---|---|---|---|---|
| Domain | Glycosyltransferase 2-like | 8 | 176 | no |

## Global alignments of canonical Q9TYJ7 with characterised orthologs

BLOSUM62, gap open -10, extend -0.5. Identity over aligned (ungapped) columns.

| Pair | Aligned columns | Identical | % identity |
|---|---|---|---|
| Q9TYJ7 vs O60762 | 238 | 154 | 64.7 |
| Q9TYJ7 vs P14020 | 230 | 81 | 35.2 |

Human DPM1 carries 13 annotated binding-site residues in total.

## Where the U4PF58 segment falls in human DPM1

Canonical residues 189-239 align to human DPM1 residues 211-260 (50 aligned columns).

Human DPM1 (O60762) features overlapping that interval:

| Type | Description / ligand | Start | End | By similarity to |
|---|---|---|---|---|
| Binding site | GDP-alpha-D-mannose | 234 | 234 | Q8U4M3 |
| Binding site | GDP-alpha-D-mannose | 240 | 240 | Q8U4M3 |
| Natural variant | in CDG1E; dbSNP:rs587777114 | 248 | 248 |  |
| Sequence conflict | in Ref. 5; AAH08466 | 220 | 220 |  |
