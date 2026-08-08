# PTHR13723 annotation census for ADAMTSL1

Regenerate with:

```
uv run genes/human/ADAMTSL1/ADAMTSL1-bioinformatics/check_family_propagation.py
```

Retrieval timestamp is recorded in `results.json` so this file stays byte-reproducible.

## 1. `GO:0031012` coverage across human PTHR13723

PAINT holds `GO:0031012` as an IBD annotation at node `PTN000347317`. Of the 26 human members of the family, 24 receive it by IBA from that node.

| gene | accession | subfamily | GO:0031012 IBA | other rows | evidence codes | GO:0030198 IBA | GO:0030198 other |
|---|---|---|---|---|---|---|---|
| ADAMTS1 | Q9UHI8 | PTHR13723:SF40 | 1 | 2 | HDA, IBA, IEA | 1 | IBA, IEA |
| ADAMTS10 | Q9H324 | PTHR13723:SF26 | 1 | 1 | IBA, IDA | 1 | IBA, IEA |
| ADAMTS12 | P58397 | PTHR13723:SF189 | 1 | 0 | IBA | 1 | IBA, IEA |
| ADAMTS13 | Q76LX8 | PTHR13723:SF20 | 1 | 1 | IBA, TAS | 1 | IBA, IEA |
| ADAMTS14 | Q8WXS8 | PTHR13723:SF24 | 1 | 0 | IBA | 1 | IBA, IEA, TAS |
| ADAMTS15 | Q8TE58 | PTHR13723:SF39 | 1 | 1 | IBA, IEA | 1 | IBA, IEA, ISS |
| ADAMTS16 | Q8TE57 | PTHR13723:SF140 | 1 | 0 | IBA | 1 | IBA, IEA |
| ADAMTS17 | Q8TE56 | PTHR13723:SF151 | 1 | 1 | IBA, IDA | 1 | IBA, IEA |
| ADAMTS18 | Q8TE60 | PTHR13723:SF167 | 1 | 0 | IBA | 1 | IBA, IEA |
| ADAMTS19 | Q8TE59 | PTHR13723:SF197 | 1 | 0 | IBA | 1 | IBA, IEA, ISS |
| ADAMTS2 | O95450 | PTHR13723:SF141 | 1 | 1 | IBA, IEA | 1 | IBA, IEA, TAS |
| ADAMTS20 | P59510 | PTHR13723:SF165 | 1 | 1 | IBA, TAS | 1 | IBA, IEA |
| ADAMTS3 | O15072 | PTHR13723:SF158 | 1 | 2 | IBA, NAS, TAS | 1 | IBA, IC, IEA, NAS, TAS |
| ADAMTS4 | O75173 | PTHR13723:SF38 | 1 | 1 | HDA, IBA | 1 | IBA, IEA, TAS |
| ADAMTS5 | Q9UNA0 | PTHR13723:SF37 | 1 | 2 | IBA, IEA, TAS | 1 | IBA, IEA, ISS, TAS |
| ADAMTS6 | Q9UKP5 | PTHR13723:SF27 | 1 | 0 | IBA | 1 | IBA, IEA |
| ADAMTS7 | Q9UKP4 | PTHR13723:SF142 | 1 | 1 | IBA, IEA | 1 | IBA, IEA |
| ADAMTS8 | Q9UP79 | PTHR13723:SF41 | 1 | 2 | IBA, IEA, ISS | 1 | IBA, IEA |
| ADAMTS9 | Q9P2N4 | PTHR13723:SF33 | 1 | 2 | IBA, IDA, ISS | 1 | IBA, IEA, ISS |
| ADAMTSL1 | Q8N6G6 | PTHR13723:SF157 | 0 | 0 | - | 0 | IEA |
| ADAMTSL2 | Q86TH1 | PTHR13723:SF147 | 1 | 0 | IBA | 1 | IBA, IEA |
| ADAMTSL3 | P82987 | PTHR13723:SF169 | 1 | 1 | IBA, TAS | 0 | IEA |
| ADAMTSL4 | Q6UY14 | PTHR13723:SF144 | 1 | 3 | HDA, IBA, TAS | 1 | IBA |
| ADAMTSL5 | Q6ZMM2 | PTHR13723:SF173 | 1 | 3 | IBA, IDA, TAS | 0 | IEA |
| PAPLN | O95428 | PTHR13723:SF281 | 0 | 2 | IEA, TAS | 0 | IEA |
| THSD4 | Q6ZMP0 | PTHR13723:SF16 | 1 | 10 | HDA, IBA, IEA, RCA, TAS | 1 | IBA |
| *Adamtsl1* (mouse) | Q8BLI0 | PTHR13723:SF157 | 1 | 3 | HDA, IBA | 0 | IEA |

**Members with no `GO:0031012` annotation of any kind: ADAMTSL1.**

PAPLN holds `GO:0031012` without the IBA, but **none of its rows is experimental** (evidence codes: IEA, TAS), so redundancy suppression does not account for the missing IBA. Its absent IBA is a second coverage gap at this node, not an explained omission.

ADAMTSL1 has neither an IBA nor any other row, and its mouse orthologue - the same PANTHER subfamily, the same IBD node - does receive the IBA.

### `GO:0030198` coverage, same node

22 of the 26 human members receive `GO:0030198` by IBA from `PTN000347317`: ADAMTS1, ADAMTS10, ADAMTS12, ADAMTS13, ADAMTS14, ADAMTS15, ADAMTS16, ADAMTS17, ADAMTS18, ADAMTS19, ADAMTS2, ADAMTS20, ADAMTS3, ADAMTS4, ADAMTS5, ADAMTS6, ADAMTS7, ADAMTS8, ADAMTS9, ADAMTSL2, ADAMTSL4, THSD4. Members with no `GO:0030198` annotation at all: none.

Within the ADAMTS-like branch the IBA reaches only ADAMTSL2, ADAMTSL4, THSD4. ADAMTSL1 and ADAMTSL5 are therefore in the same position for this term - the InterPro IEA and nothing else - which matters when comparing verdicts between their reviews.

## 2. `Hydrolase` keyword across the ADAMTS-like branch

UniProt's `KW-0378 Hydrolase` is what generates the `GO:0016787 hydrolase activity` cross-reference in an entry's own GO list (`IEA:UniProtKB-KW`).

| gene | accession | length | MF keywords | CATALYTIC ACTIVITY comments | CAUTION: no metalloprotease domain |
|---|---|---|---|---|---|
| ADAMTSL1 | Q8N6G6 | 1762 | Hydrolase | 0 | yes |
| ADAMTSL2 | Q86TH1 | 951 | - | 0 | yes |
| ADAMTSL3 | P82987 | 1691 | - | 0 | yes |
| ADAMTSL4 | Q6UY14 | 1074 | - | 0 | yes |
| ADAMTSL5 | Q6ZMM2 | 481 | Heparin-binding | 0 | yes |
| THSD4 | Q6ZMP0 | 1018 | Hydrolase | 0 | no |

Hydrolase keyword present on: ADAMTSL1, THSD4. CAUTION stating the metalloprotease and disintegrin-like domains are absent: ADAMTSL1, ADAMTSL2, ADAMTSL3, ADAMTSL4, ADAMTSL5 (absent on THSD4).

Entries with a CATALYTIC ACTIVITY comment: none. So on ADAMTSL1 the keyword sits alongside that entry's own statement that the catalytic domain is missing, with no reaction recorded anywhere in the entry.

## 3. PAINT's own loss calls in this family

The cached PAINT table records explicitly negated annotations, i.e. terms PAINT blocks from propagating below a node:

| node | term | aspect | evidence | seed |
|---|---|---|---|---|
| PTN002673039 | GO:0004222 | F | IKR | PANTHER:PTN000347317 |
| PTN002673039 | GO:0006508 | P | IRD | PANTHER:PTN000347317 |

`IKR` is inferred-from-key-residues and `IRD` inferred-from-rapid-divergence: PAINT has judged that catalysis was lost on this branch. Where those calls land in GOA:

| gene | GO:0004222 rows | GO:0006508 rows |
|---|---|---|
| ADAMTSL1 | none | none |
| ADAMTSL2 | `NOT\|enables` IBA GO_REF:0000033 | none |
| ADAMTSL3 | none | none |
| ADAMTSL4 | none | none |
| ADAMTSL5 | none | none |
| THSD4 | none | none |

Negated rows in GOA: ADAMTSL2 GO:0004222. Positive rows in GOA: none. So the loss call is recorded for part of the branch and simply absent for the rest - ADAMTSL1 inherits neither the catalytic terms nor the statement that they do not apply.

## 4. IBD seed composition at the family node

Counting WITH/FROM tokens on the derived IBA rows overstates the number of experimental sources by one, because GOA appends the PANTHER node itself to the list. The seed lists in the PAINT table give the gene sources directly:

| node | term | aspect | evidence | seed tokens | gene sources | by database |
|---|---|---|---|---|---|---|
| PTN000347317 | GO:0031012 | C | IBD | 16 | 16 | FB 2, MGI 8, RGD 1, UniProtKB 4, WB 1 |
| PTN000347317 | GO:0004222 | F | IBD | 9 | 9 | MGI 3, UniProtKB 6 |
| PTN000347317 | GO:0006508 | P | IBD | 13 | 13 | MGI 7, UniProtKB 4, ZFIN 2 |
| PTN000347317 | GO:0030198 | P | IBD | 14 | 14 | FB 2, MGI 11, WB 1 |

## Guards

The script aborts rather than emitting a stale sentence if any of these stop holding: a QuickGO response is paginated (page total read as the whole set); human ADAMTSL1 acquires any `GO:0031012` row; mouse Adamtsl1 loses its IBA from `PTN000347317`; ADAMTSL1 loses `KW-0378`, gains a CATALYTIC ACTIVITY comment, or loses the CAUTION about the missing metalloprotease domain; the IKR loss call disappears from the cached PAINT table; or ADAMTSL1 gains a GO:0004222/GO:0006508 row. A missing cached input is a hard error naming the command that regenerates it. The zero-row count for ADAMTSL1 is produced by the same code path that returns non-zero for the other 25 human members on every run, so the census is its own positive control.
