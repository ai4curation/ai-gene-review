# lhfpl5a / lhfpl5b: identity, conserved synteny and public expression records

Scripts (run from the repo root; both query live APIs, nothing is hardcoded):

- `uv run python genes/DANRE/lhfpl5a/lhfpl5a-bioinformatics/pair_analysis.py lhfpl5a lhfpl5b LHFPL5` → `output.txt`
  (Ensembl REST: locations, Compara orthologues/paralogy node, canonical proteins, 15 protein-coding neighbours
  on each side of each copy with their gar and human orthologue positions).
- `uv run python genes/DANRE/lhfpl5a/lhfpl5a-bioinformatics/expression_compare.py lhfpl5a lhfpl5b` →
  `expression_output.txt` (ZFIN wild-type expression download and Bgee REST calls).

Run 2026-09-28. Results below are copied from those output files.

## Locations and Compara

- lhfpl5a chr11:2.83 Mb; lhfpl5b chr8:23.88 Mb (different chromosomes).
- Ensembl Compara paralogy node joining them: **Osteoglossocephalai**.
- One gar orthologue for both (ENSLOCG00000011154, LG3:32.28 Mb). One medaka one-to-one orthologue for each, on
  different medaka chromosomes (lhfpl5a → chr5, lhfpl5b → chr7).

## Protein identity (canonical Ensembl translations, global alignment, BLOSUM62)

| Pair | Identity | Similarity |
|---|---|---|
| lhfpl5a vs lhfpl5b | 74.6% | 84.6% |
| lhfpl5a vs gar | 77.2% | 84.4% |
| lhfpl5b vs gar | 73.7% | 82.6% |
| lhfpl5a vs human LHFPL5 | 66.8% | 83.2% |
| lhfpl5b vs human LHFPL5 | 65.2% | 81.9% |

(The UniProt-based figure in the pair's annotation-comparison.md is 76.5%; the Ensembl canonical lhfpl5a
translation is 226 aa against 219 aa for UniProt F1Q837.) lhfpl5b is slightly further from the gar sequence than
lhfpl5a: a small asymmetry in rate, with no functional implication by itself.

## Conserved synteny

Of 30 neighbours of each copy, those whose gar orthologue lies within 5 Mb of the gar lhfpl5 anchor: lhfpl5a 5,
lhfpl5b 9. Those whose human orthologue lies within 5 Mb of human LHFPL5 (chr6:35.8 Mb): lhfpl5a 3, lhfpl5b 5.
The key observation is that **the same gene families flank both copies**: mapk14b/mapk14a, srpk1b/srpk1a and
cpne5b/cpne5a sit next to lhfpl5a and lhfpl5b respectively, and their orthologues, where Compara reports one (gar LG3:32.2-32.4 Mb for
mapk14b, srpk1b, cpne5b and cpne5a; human 6p21, 35.8-36.7 Mb for all but srpk1a), are next to gar lhfpl5 and human
LHFPL5. Two zebrafish segments, each holding one copy of a
block that is single in gar and human, is the double-conserved-synteny signature of the teleost genome duplication.

## Public expression records

- ZFIN (curated; all records cite one publication, ZDB-PUB-200207-5, dated to early 2020 like Erickson et al., PMID:32009898 — the mapping was not checked): lhfpl5a anterior/posterior macula and their hair
  cells (Prim-5 to Day 5); lhfpl5b neuromast and neuromast hair cell. No shared terms.
- Bgee: lhfpl5a in maculae/hair cells (in situ) plus bulk testis and larva; lhfpl5b only bulk RNA-seq calls in many
  adult tissues and early embryos (score 36-82). The bulk calls are not hair-cell resolved and are not interpreted.

## Interpretation

Synteny and Compara support a TGD origin (two chromosomes, flanking paralog pairs, one gar gene). The public curated
expression records reproduce the published ear/lateral-line split; they are not independent of it.
