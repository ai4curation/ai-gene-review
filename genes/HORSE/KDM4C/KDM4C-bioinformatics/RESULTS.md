# KDM4C: horse-human sequence comparison

## Method

The horse sequence (A0A3Q2HAR2, from `../KDM4C-uniprot.txt`) was aligned globally to the
reviewed human KDM4C (Q9H3R0, `human-KDM4C-Q9H3R0.fasta`, downloaded from the UniProt
REST API on 2026-10-21 together with the flat file `human-KDM4C-Q9H3R0-uniprot.txt`) using
Biopython PairwiseAligner (BLOSUM62, gap open -10, gap extend -0.5). The script is a
PEP 723 copy of the donkey KDM4C alignment script (`genes/EQUAS/KDM4C/KDM4C-bioinformatics/align_to_human.py`).

Reproduce from this folder:

```
uv run --script align_horse_to_human.py ../KDM4C-uniprot.txt human-KDM4C-Q9H3R0.fasta 134 190 192 200 208 236 242 243 278 308 310
```

Human residue positions queried: 2-oxoglutarate-binding Y134, N200, K208, K243; catalytic
Fe-binding H190, E192, H278; Zn-binding C236, H242, C308, C310 (human UniProt FT lines).

## Output (alignment_output.txt)

```
Query A0A3Q2HAR2: 1053 aa; human Q9H3R0: 1056 aa
Paired residues: 1053; identical: 960; identity over paired: 91.17%
Coverage of human: 99.72%; coverage of query: 100.00%
Human ranges with no aligned query residue: 472..472, 488..489
Query ranges with no aligned human residue: none
Human Y134 -> query Y134
Human H190 -> query H190
Human E192 -> query E192
Human N200 -> query N200
Human K208 -> query K208
Human C236 -> query C236
Human H242 -> query H242
Human K243 -> query K243
Human H278 -> query H278
Human C308 -> query C308
Human C310 -> query C310
```

## Interpretation

The horse KDM4C protein is a full-length gene product: it aligns over 99.72% of human KDM4C at 91.17% identity, with only three single-residue gaps in the disordered linker (human 472, 488-489) between the catalytic module and the PHD/Tudor readers. All human 2-oxoglutarate-binding, catalytic Fe-binding and Zn-binding residues of the JmjC domain are conserved at the same positions in the horse protein. Together with its PANTHER subfamily placement (PTHR10694:SF104, LYSINE-SPECIFIC DEMETHYLASE 4C, the same subfamily as human Q9H3R0 and mouse Q8VCD7), this supports transfer of the experimentally established KDM4C demethylase activity.
