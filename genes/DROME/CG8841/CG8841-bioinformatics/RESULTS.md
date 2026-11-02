# CG8841 (Q0E9B5) comparison with PTHR21575:SF12 HID1 proteins

Script: `compare_hid1_orthologs.py` (run with
`uv run --no-project --with biopython --with requests python compare_hid1_orthologs.py`).
Raw output: `compare_hid1_orthologs.out`.

Method: sequences fetched from the UniProt REST API; global pairwise alignment
(BLOSUM62, gap open -10, extend -0.5); identity is reported over aligned (non-gap)
columns, over the full CG8841 length, and over the last 150 residues of each pair.
All compared proteins are PANTHER PTHR21575:SF12 members (per
`interpro/panther/PTHR21575/PTHR21575-entries.csv`).

## Results (copied from compare_hid1_orthologs.out)

Q0E9B5 length 837; N-terminus MGNTDSKL; Gly2=True

| Accession | Protein | Length | N-terminus | Gly2 | Identity (aligned) | Identity (query) | C-terminal 150 aa identity |
|---|---|---|---|---|---|---|---|
| Q8IV36 | H. sapiens HID1 | 788 | MGSTDSKL | yes | 68.7% | 63.3% | 72.5% |
| Q8R1F6 | M. musculus Hid1 | 788 | MGSADSKL | yes | 69.7% | 63.7% | 78.0% |
| D4A0C3 | R. norvegicus Hid1 | 788 | MGSADSKL | yes | 68.8% | 63.1% | 76.6% |
| Q9P7M6 | S. pombe hid3 (SPAC17A5.16) | 797 | MGSQQSKL | yes | 29.9% | 26.3% | 24.6% |
| Q06673 | S. cerevisiae ECM30 | 1274 | MGNTDSKS | yes | 27.5% | 24.6% | 28.0% |

## Interpretation

- CG8841 is a full-length HID1 protein, about 69% identical to the mammalian HID1
  proteins over aligned positions. Its extra length (837 vs 788 aa) is accounted for by
  the UniProt MobiDB-lite disordered acidic segment (residues 570-705) and is not a
  truncation or a missing domain.
- The N-terminal Gly2 myristoylation motif (MGxxxSKL), which is required for Golgi
  membrane binding of mammalian and nematode HID-1 (PMID:21337012, PMID:21115972), is
  conserved.
- The C-terminal region is conserved (72-78% identity to the mammalian C-terminal 150
  residues).
- Fungal members of the same subfamily are much more distant (25-30%), consistent with
  dense-core-vesicle functions being a metazoan specialization layered on the ancestral
  Golgi role.
- Pairwise identity does not by itself establish orthology; the orthology claim rests on
  shared PANTHER subfamily membership (SF12) and on the PAINT nodes from which the
  GO_Central IBA annotations descend.
