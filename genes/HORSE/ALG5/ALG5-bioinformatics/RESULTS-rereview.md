# ALG5 re-review: isoform identity of A0A5F5PM72 and conservation of the missing segment

Script: `compare_isoforms_rereview.py` (Biopython global alignment, match 2, mismatch -1, gap open -10, extend -0.5). Raw values: `results-rereview.json`.

## Which product is A0A5F5PM72?

- Human isoform 2 (Q9Y673-2) is isoform 1 minus residues 95-124: True
- Horse vs human isoform 1: {'len_a': 324, 'len_b': 294, 'paired': 294, 'identical': 278, 'identity': 0.9456, 'a_residues_unpaired': 30}
- Horse vs human isoform 2: {'len_a': 294, 'len_b': 294, 'paired': 294, 'identical': 278, 'identity': 0.9456, 'a_residues_unpaired': 0}
- Human segment 95-124 absent from the horse model: `QKRDPAFTYEVIVVDDGSKDQTSKVAFKYC`

## The missing segment across PTHR10859:SF91 orthologs

| Ortholog | Residues aligned to human 95-124 |
|---|---|
| Q9DB25 ALG5_MOUSE | `QKHDCTFTYEVIVVDDGSEDQTSKVALKYC` |
| Q9VLQ1 ALG5_DROME | `SAGTPNFTYEVIVVSDGSQDATVSVALGYS` |
| Q54J42 ALG5_DICDI | `SKKDLKFSYEIIIIDDGSKDSTAKLVTSYI` |
| O60061 ALG5_SCHPO | `SSSAGQRRWEILIVDDESKDTTvNAVLEFSN` |
| P40350 ALG5_YEAST | `-KEKYGSRWEIVIVDDGSTDNTTQYCLKIC` |

## The missing segment in all horse ALG5 UniProt entries

| Horse entry | Length | Residues aligned to human 95-124 |
|---|---|---|
| A0A9L0R8Q1 | 312 | `QKQDPTFTYEVIVVDDGSKDQTSEVAFKYC` |
| A0A9L0R8Q6 | 300 | `QKQDPTFTYEVIVVDDGSKDQTSEVAFKYC` |
| A0A9L0SJT3 | 293 | `QKQDPTFTYEVIVVDDGSKDQTS-------` |
| A0A9L0TRZ9 | 309 | `QKQDPTFTYEVIVVDDGSKDQTSEVAFKYC` |
| F6RYM5 | 304 | `QKQDPTFTYEVIVVDDGSKDQTSEVAFKYC` |
| A0A9L0SJD5 | 266 | `QKQDPTFTYEVIVVDDGSKDQTSEVAFKYC` |
| A0A9L0SQ24 | 286 | `QKQDPTFTYEVIVVDDGSKDQTSEVAFKYC` |
| A0A9L0TPE9 | 259 | `QKQDPTFTYEVIVVDDGSKDQTSEVAFKYC` |
| A0A5F5PM72 | 294 | `------------------------------` |
| A0A9L0SN10 | 251 | `-KQDPTFTYEVIVVDDGSKDQTSEVAFKYC` |

DXD motif ADADG present in A0A5F5PM72: True (position 132).

Gap characters ('-') mark residues absent from the compared sequence; lowercase marks insertions relative to human. This is sequence evidence only: it does not measure enzyme activity of either isoform.
