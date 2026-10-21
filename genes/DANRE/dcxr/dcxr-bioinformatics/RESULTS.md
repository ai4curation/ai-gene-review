# dcxr: exact selected product and human ortholog reference

Selected Q567K5 has 244 residues; reference Q7Z4W1 has 244 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–244 | 1–244 | 169 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Active site: Nucleophile | 136–136 | 1 / 1 | 1 |
| Active site: Proton acceptor | 149–149 | 1 / 1 | 1 |
| Active site: Proton donor | 153–153 | 1 / 1 | 1 |
| Binding site:  | 17–17 | 1 / 1 | 1 |
| Binding site:  | 19–19 | 1 / 1 | 1 |
| Binding site:  | 38–38 | 1 / 1 | 0 |
| Binding site:  | 39–39 | 1 / 1 | 1 |
| Binding site:  | 40–40 | 1 / 1 | 1 |
| Binding site:  | 60–60 | 1 / 1 | 1 |
| Binding site:  | 61–61 | 1 / 1 | 1 |
| Binding site:  | 83–83 | 1 / 1 | 1 |
| Binding site:  | 134–134 | 1 / 1 | 1 |
| Binding site:  | 149–149 | 1 / 1 | 1 |
| Binding site:  | 153–153 | 1 / 1 | 1 |
| Binding site:  | 182–182 | 1 / 1 | 1 |
| Binding site:  | 184–184 | 1 / 1 | 1 |
| Binding site:  | 185–185 | 1 / 1 | 0 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and human ortholog reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Target sequence is read from `dcxr-uniprot.txt` (UniProt Q567K5, 244 aa).

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5; NJ on 1 - pairwise identity.

### Alignment to human DCXR (Q7Z4W1)

Q567K5 (244 aa) vs Q7Z4W1 (244 aa): 169 identical residues.

| Human feature | Human pos | Human res | Zebrafish pos | Zebrafish res |
|---|---|---|---|---|
| ACT_SITE Nucleophile | 136 | S | 136 | S |
| ACT_SITE Proton acceptor | 149 | Y | 149 | Y |
| ACT_SITE Proton donor | 153 | K | 153 | K |
| BINDING NADP(+) | 17 | K | 17 | K |
| BINDING NADP(+) | 19 | I | 19 | I |
| BINDING NADP(+) | 38 | S | 38 | T |
| BINDING NADP(+) | 39 | R | 39 | R |
| BINDING NADP(+) | 40 | T | 40 | T |
| BINDING NADP(+) | 60 | D | 60 | D |
| BINDING NADP(+) | 61 | L | 61 | L |
| BINDING NADP(+) | 83 | N | 83 | N |
| BINDING NADP(+) | 134 | V | 134 | V |
| BINDING NADP(+) | 149 | Y | 149 | Y |
| BINDING NADP(+) | 153 | K | 153 | K |
| BINDING NADP(+) | 182 | V | 182 | V |
| BINDING NADP(+) | 184 | T | 184 | T |
| BINDING NADP(+) | 185 | S | 185 | E |

### Pairwise identity of Q567K5 to PTHR44252 members

| Accession | Gene | PANTHER subfamily | Identity to Q567K5 |
|---|---|---|---|
| Q7Z4W1 | DCXR | PTHR44252:SF2 | 0.693 |
| Q91X52 | Dcxr | PTHR44252:SF2 | 0.689 |
| Q8JIS3 | DER | PTHR44252:SF3 | 0.701 |
| Q21929 | dhs-21 | PTHR44252:SF3 | 0.510 |
| P08074 | Cbr2 | PTHR44252:SF1 | 0.615 |
| Q29529 | CBR2 | PTHR44252:SF1 | 0.635 |

### Neighbour-joining tree (rooted on the CBR2 subfamily SF1)

```
((((Q567K5_dcxr:0.14388,Q21929_dhs-21:0.34574)Inner5:0.01390,Q8JIS3_DER:0.14191)Inner4:0.01997,(Q91X52_Dcxr:0.08043,Q7Z4W1_DCXR:0.07531)Inner2:0.04508)Inner3:0.13115,Q29529_CBR2:0.06680,P08074_Cbr2:0.08074)Inner1:0.00000;
```

A distance tree from seven sequences is a coarse check on placement, not a substitute for the PANTHER/PAINT tree.
