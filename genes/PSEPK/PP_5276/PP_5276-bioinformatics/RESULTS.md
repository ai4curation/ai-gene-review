# PP_5276 (Q88CA5) HKD motif check

Command (run from the repository root):

```
python3 genes/PSEPK/PP_5276/PP_5276-bioinformatics/hkd_motifs.py genes/PSEPK/PP_5276/PP_5276-uniprot.txt genes/ECOLI/clsC/clsC-uniprot.txt genes/ECOLI/clsA/clsA-uniprot.txt genes/ECOLI/clsB/clsB-uniprot.txt
```

Output:

```
genes/PSEPK/PP_5276/PP_5276-uniprot.txt	length=517	170:HNKLFLVD; 414:HTKAIVFD
genes/ECOLI/clsC/clsC-uniprot.txt	length=473	130:HNKSFTVD; 369:HAKTFSID
genes/ECOLI/clsA/clsA-uniprot.txt	length=486	224:HRKMIMID; 404:HTKSVLVD
genes/ECOLI/clsB/clsB-uniprot.txt	length=413	113:HRKIVVID; 290:HGKVALMD
```

Interpretation: PP_5276 retains both PLD-superfamily HxK(x4)D catalytic motifs, at
positions 170 and 414, with the same spacing as E. coli ClsC (130 and 369), whose
His130 and His369 are required for cardiolipin formation. The motifs are consistent with
an active phospholipase D-type phosphatidyltransferase. They do not show which
phosphatidyl donor (PG or PE) the enzyme uses, or whether it needs a YmdB-like partner.
