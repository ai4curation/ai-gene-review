# AOPEP exopeptidase-motif check

Script: `gxmen_motif.py` (sequences fetched from UniProt REST, run 2026-10-04).

Question: does AOPEP carry the M1-family GXMEN (GAMEN) motif that binds the substrate's free
alpha-amino group and confers aminopeptidase (exopeptidase) specificity?

Output:

```
Q8N6M6	AOPEP (human aminopeptidase O)	length=819
  GXMEN: none
  relaxed G.M.N: none
  HEXXH: [(479, 'HEIAH')]
P15144	ANPEP (aminopeptidase N; UniProt's similarity source for AOPEP)	length=967
  GXMEN: [(352, 'GAMEN')]
  relaxed G.M.N: [(352, 'GAMEN'), (716, 'GPMKN')]
  HEXXH: [(388, 'HELAH')]
P09960	LTA4H (leukotriene A4 hydrolase / aminopeptidase)	length=611
  GXMEN: [(269, 'GGMEN')]
  relaxed G.M.N: [(269, 'GGMEN')]
  HEXXH: [(296, 'HEISH')]
Q9H4A4	RNPEP (aminopeptidase B)	length=650
  GXMEN: [(298, 'GGMEN')]
  relaxed G.M.N: [(298, 'GGMEN')]
  HEXXH: [(325, 'HEISH')]
```

Conclusion: AOPEP keeps the HEXXH zinc motif (HEIAH at 479) but has no GXMEN motif, even under a relaxed G.M.N pattern, whereas the three characterised M1 aminopeptidases each have GXMEN 27 to 36 residues upstream of their HEXXH motif. Metallopeptidase chemistry is supported by sequence; aminopeptidase specificity is not.
