# Pairwise identity: S. pombe HMP/HMP-P kinase paralogs vs S. cerevisiae THI20/THI21/THI22

Method: Biopython PairwiseAligner, local alignment, BLOSUM62, gap open -10, extend -0.5,
sequences taken from the cached UniProt records. Identity = identical aligned positions /
aligned (ungapped) positions. Run from the repo root:

```
uv run python -I genes/SCHPO/thi201/thi201-bioinformatics/pairwise_identity.py \
  thi20=genes/SCHPO/thi20/thi20-uniprot.txt thi201=genes/SCHPO/thi201/thi201-uniprot.txt \
  SPCC18B5.05c=genes/SCHPO/SPCC18B5.05c/SPCC18B5.05c-uniprot.txt \
  THI20=genes/yeast/THI20/THI20-uniprot.txt THI21=genes/yeast/THI21/THI21-uniprot.txt \
  THI22=genes/yeast/THI22/THI22-uniprot.txt
```

## Output

```
thi20	thi201	len506/551	aligned 454	id 0.36
thi20	SPCC18B5.05c	len506/327	aligned 303	id 0.32
thi20	THI20	len506/551	aligned 451	id 0.29
thi20	THI21	len506/551	aligned 473	id 0.29
thi20	THI22	len506/572	aligned 461	id 0.31
thi201	SPCC18B5.05c	len551/327	aligned 255	id 0.36
thi201	THI20	len551/551	aligned 476	id 0.41
thi201	THI21	len551/551	aligned 473	id 0.40
thi201	THI22	len551/572	aligned 470	id 0.38
SPCC18B5.05c	THI20	len327/551	aligned 243	id 0.29
SPCC18B5.05c	THI21	len327/551	aligned 272	id 0.31
SPCC18B5.05c	THI22	len327/572	aligned 288	id 0.31
THI20	THI21	len551/551	aligned 551	id 0.86
THI20	THI22	len551/572	aligned 550	id 0.76
THI21	THI22	len551/572	aligned 550	id 0.78
```

## Interpretation

- thi201 (O94266, SPBP8B7.18c) is the S. pombe protein most similar to the budding-yeast
  THI20/THI21/THI22 trio (about 0.40 identity), consistent with its PANTHER placement in
  PTHR20858:SF17 together with them.
- thi20 (O94265, SPBP8B7.17c) is more distant (about 0.29-0.31) and sits in a different
  PANTHER subfamily (SF22). The PomBase name "thi20" therefore does not mark it as the closer
  ortholog of S. cerevisiae THI20.
- SPCC18B5.05c (Q9USL6) aligns only over the N-terminal ThiD-like kinase region (it lacks the
  C-terminal TenA/thiaminase-II domain) and is about 0.29-0.36 identical to the others.
- All identities are modest; this analysis only orders similarity and does not establish
  one-to-one orthology or activity.
