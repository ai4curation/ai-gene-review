# Which *Capsaspora* T-box protein is Brachyury (CoBra)?

This is our own analysis (2026-10-01), not published data. Reproduce it with:

```
uv run python projects/ORIGINS_OF_MULTICELLULARITY/capsaspora-tbox/tbox_assign.py
```

The raw output is in `tbox_assign_output.txt`. All sequences and domain
coordinates are fetched live from UniProt.

**Problem.** PMID:24043797 characterised *Capsaspora* Brachyury (CoBra) but
gives no locus ID. UniProt has three *Capsaspora* T-box proteins, all with
automatic names:

| Accession | Locus | UniProt name |
|---|---|---|
| A0A0D2VZV8 | CAOG_007284 | T-box domain-containing protein |
| A0A0D2WSA5 | CAOG_005526 | T-box transcription factor TBX4 |
| A0A0D2VUC6 | CAOG_005512 | TBX19 protein |

**Two tests.**
1. **Best match.** We scored each T-box domain against 12 human T-box
   domains by global alignment (BLOSUM62).
2. **Residue marker.** We found the residue aligned to Lys149 of Xenopus
   Brachyury (P24781). The paper uses this position as a marker: Lys in
   metazoan Brachyury, Asn in other T-box classes, and Arg in CoBra.

**Results.**

| Accession | Best human matches | Residue at XBra149 |
|---|---|---|
| A0A0D2VUC6 | TBX19, then TBXT (the T subfamily) | **R** (LKLTN**R**PNTKG) |
| A0A0D2WSA5 | TBX2, then TBX19 and TBX5 | T |
| A0A0D2VZV8 | TBX19, TBR1, EOMES (weaker) | N |

**Assignment.**
- **A0A0D2VUC6 (CAOG_005512) is CoBra.** It is the best T-subfamily match,
  and it has the arginine the paper reports for CoBra at the Lys149
  position.
- **A0A0D2WSA5** fits the Tbx2/3 class, consistent with the paper's CoTbx3.
- **Caveats.** The assignment rests on similarity plus one marker residue, not
  a phylogeny. The paper also mentions a *Capsaspora* T-box gene with two
  T-box domains; none of the three UniProt entries has two annotated T-box
  domains, so the gene models may differ from the paper's.
