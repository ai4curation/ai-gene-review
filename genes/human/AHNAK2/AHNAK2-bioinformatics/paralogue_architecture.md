## Architecture of the three donors vs AHNAK2

| protein | accession | status | length | PDZ (UniProt FT) | PDZ as % of chain |
|---|---|---|---|---|---|
| AHNAK2 | Q8IVF2 | Swiss-Prot | 5795 | 112-193 | 1.4% |
| AHNAK2_MOUSE | A0A7N9VR94 | TrEMBL | 3501 | 108-175 | 1.9% |
| AHNAK | Q09666 | Swiss-Prot | 5890 | 9-90 | 1.4% |
| AHNAK_MOUSE | E9Q616 | TrEMBL | 5656 | 1-57 | 1.0% |
| PRX | Q9BXM0 | Swiss-Prot | 1461 | 16-99 | 5.7% |
| PRX_MOUSE | O55103 | Swiss-Prot | 1391 | 16-99 | 6.0% |
| PRX_RAT | Q63425 | Swiss-Prot | 1383 | 16-99 | 6.1% |

Each giant AHNAK has a large central repeat. Discover each one's own anchor
rather than assuming they share a unit, then cross-test.

| protein | own most frequent 10-mer | occurrences |
|---|---|---|
| AHNAK2 | `KDSKFKMPKF` | 22 |
| AHNAK2_MOUSE | `FKMPSFGVSA` | 12 |
| AHNAK | `KLKGPKFKMP` | 29 |
| AHNAK_MOUSE | `KLKGPKFKMP` | 27 |
| PRX | `LPKVPEMAVP` | 7 |
| PRX_MOUSE | `RLPEVQLPKV` | 4 |
| PRX_RAT | `PEMAVPDVHL` | 3 |

Cross-test of the AHNAK2 anchor `KDSKFKMPKF` (22 occurrences in AHNAK2) against every other protein:

| protein | AHNAK2-anchor occurrences | first | last | span | span as % of chain |
|---|---|---|---|---|---|
| AHNAK2 | 22 | 671 | 4459 | 671-4468 | 65.5% |
| AHNAK2_MOUSE | 11 | 490 | 2392 | 490-2401 | 54.6% |
| AHNAK | 0 | - | - | - | 0.0% |
| AHNAK_MOUSE | 0 | - | - | - | 0.0% |
| PRX | 0 | - | - | - | 0.0% |
| PRX_MOUSE | 0 | - | - | - | 0.0% |
| PRX_RAT | 0 | - | - | - | 0.0% |

The only structured domain either AHNAK has is the PDZ. Score it separately
from the full-length alignment, and calibrate against ortholog controls.

| pair | PDZ-vs-PDZ identity | aligned aa | full-length local identity | aligned aa |
|---|---|---|---|---|
| AHNAK2 vs AHNAK | 28.4% | 81 | 36.9% | 4838 |
| AHNAK2 vs PRX | 56.8% | 81 | 31.3% | 1342 |
| AHNAK2 vs PRX_MOUSE | 58.0% | 81 | 36.2% | 1263 |
| AHNAK2 vs PRX_RAT | 58.0% | 81 | 33.5% | 1277 |
| AHNAK2 vs AHNAK2_MOUSE | 89.7% | 68 | 66.2% | 2853 |
| AHNAK vs AHNAK_MOUSE | 97.9% | 48 | 84.0% | 5569 |
| PRX vs PRX_MOUSE | 97.6% | 84 | 81.8% | 1389 |

Partition of the AHNAK2 full-length local alignment by the AHNAK2 repeat span 671-4468:

| pair | aligned aa inside repeat | identity inside | aligned aa outside | identity outside | % of aligned length inside |
|---|---|---|---|---|---|
| AHNAK2 vs AHNAK | 3478 | 39.9% | 1360 | 29.3% | 71.9% |
| AHNAK2 vs PRX | 885 | 31.4% | 457 | 31.1% | 65.9% |
| AHNAK2 vs AHNAK2_MOUSE | 1796 | 74.4% | 1057 | 52.2% | 63.0% |

