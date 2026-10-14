# ASTE1 notes

## 2026-10-05 review (PAINT, affinage)

- ASTE1 is a structure-specific ssDNA / 3' overhang endonuclease and a downstream effector of 53BP1-RIF1-shieldin [PMID:34354233 "Here, we identify a downstream effector of the shieldin complex, ASTE1, as a structure-specific DNA endonuclease that specifically cleaves single-stranded DNA and 3' overhang DNA."].
- It is recruited to breaks by shieldin [PMID:34354233 "ASTE1 localizes to DNA damage sites in a shieldin-dependent manner."]. I added NEW site of double-strand break (IDA) for this; SHLD1, SHLD2 and SHLD3 carry the same term by IDA in QuickGO.
- Loss impairs NHEJ and class switching [PMID:34354233 "Loss of ASTE1 impairs non-homologous end-joining, leads to hyper-resection and causes defective immunoglobulin class switch recombination."]. I added NEW positive regulation of isotype switching (GO:0045830); SHLD1, SHLD2 and SHLD3 carry it by IDA.
- The HR rows (IMP plus a mouse Ensembl projection) were changed to negative regulation of HR (GO:2000042), because ASTE1 loss *restores* HR in BRCA1-deficient cells [PMID:34354233 "ASTE1 deficiency also causes resistance to poly(ADP-ribose) polymerase inhibitors in BRCA1-deficient cells owing to restoration of homologous recombination."]. Shieldin subunits carry GO:2000042 by IDA.
- PMID:34354233 is abstract-only (not in PMC). The R252A catalytic-dead mutant and the SHLD2-binding region (351-400) come from UniProt's curation of that paper.
- All six GO:0005515 IPI rows were removed under the generic protein-binding policy: XRCC4 from HuRI, and RIF1, SHLD1, SHLD2, SHLD3 and REV7 from PMID:34354233.
- Other literature on ASTE1 (HT001) concerns the cancer coding-microsatellite frameshift target (PMID:15563124, PMID:23674496) and its antisense overlap with ATP2C1 (PMID:23344038). None of it addresses function.
