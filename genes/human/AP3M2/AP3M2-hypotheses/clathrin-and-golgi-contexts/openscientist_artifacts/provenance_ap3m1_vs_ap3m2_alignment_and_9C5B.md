# Computed provenance: 9C5B subunit identity + AP3M1/AP3M2 alignment

## 1. RCSB PDB 9C5B polymer entities (data.rcsb.org REST API)
Executed this run. Result:

| Entity | Description | UniProt |
|--------|-------------|---------|
| 1 | ADP-ribosylation factor 1 | P84077 |
| 2 | AP-3 complex subunit delta-1 | O14617 (AP3D1) |
| 3 | AP-3 complex subunit **mu-1** | **Q9Y2T2 (AP3M1)** |
| 4 | AP-3 complex subunit sigma-1 | Q92572 (AP3S1) |
| 5 | Lysosome-associated membrane glycoprotein 1 (cargo) | P11279 (LAMP1) |
| 6 | AP-3 complex subunit beta-1 | O00203 (AP3B1) |

Conclusion: the medium subunit in 9C5B is **AP3M1 (mu3A)**, NOT AP3M2 (P53677/mu3B).
The structure captures an Arf1-bound AP-3 engaging a YXXphi cargo (LAMP1); **no clathrin** is present.

## 2. Pairwise Needleman-Wunsch alignment: P53677 (AP3M2/mu3B) vs Q9Y2T2 (AP3M1/mu3A)
Sequences fetched from UniProt; simple NW (match=2, mismatch=-1, gap=-2). Result:

```
AP3M2 len 418 | AP3M1 len 418
Alignment cols=418, aligned(no-gap) cols=418
Identical residues=352  => %identity = 84.2%
AP3M2 pos405 = I   aligned AP3M1 = V   (seed claims conservative V405I)
context m2: KPFKGIKYMTK
context m1: KPFKGVKYVTK
```

Conclusion: mu3A and mu3B are **84.2% identical** over full length with no gaps; residue 405 is a
conservative Val(mu3A)->Ile(mu3B) substitution. This supports transferring cargo-contact (YXXphi pocket)
inferences from the mu3A 9C5B structure to mu3B **by paralogy**, but transfers nothing about clathrin.

## 3. PANTHER family provenance (pantherdb.org geneinfo)
P53677 -> family **PTHR10529**, subfamily SF341. Family-level GO annotations include
GO:0035615 (clathrin-cargo adaptor activity), GO:0035651 (AP-3 adaptor complex binding),
GO:0006896 (Golgi to vacuole transport), GO:0006897 (endocytosis), GO:0008089 (anterograde axonal transport).
The family PTHR10529 spans AP-1/AP-2/AP-3/AP-4 mu subunits, so GO:0035615 (a genuine AP-1/AP-2 clathrin-adaptor
activity) is propagated by IBA onto clathrin-independent AP-3 mu subunits.
