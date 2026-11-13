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
positions 170 and 414 (244 residues apart). That spacing is comparable to E. coli ClsC
(130 and 369, 239 apart), whose His130 and His369 are required for cardiolipin
formation, and differs from the ClsA/ClsB proteins in the same output (about 180 apart). The motifs are consistent with
an active phospholipase D-type phosphatidyltransferase. They do not show which
phosphatidyl donor (PG or PE) the enzyme uses, or whether it needs a YmdB-like partner.
