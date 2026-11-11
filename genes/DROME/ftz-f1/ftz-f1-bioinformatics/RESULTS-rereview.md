# ftz-f1 (M9NFK2) re-review sequence and family placement results (2026-10-20)

## Sequence identity (compare_isoforms_rereview.py)

Output of `python3 compare_isoforms_rereview.py`, run on the FASTA files in `../ftz-f1-isoform-records/`:

```
M9NFK2 length: 803
P33244-2 length: 803; identical to M9NFK2: True
P33244-1 (canonical) length: 1027; identical to M9NFK2: False
Shared C-terminal suffix with P33244-1: 629 aa (M9NFK2 175-803 = P33244-1 399-1027)
Isoform-specific N-terminus: M9NFK2 1-174 vs P33244-1 1-398
```

Interpretation: M9NFK2 (unreviewed, PE 3) is a duplicate UniProtKB/TrEMBL entry for the
shorter FTZ-F1 product, identical to reviewed isoform P33244-2. It is not a fragment. It
differs from the canonical P33244-1 (1027 aa) only in the isoform-specific N-terminal
region. The nuclear-receptor DNA-binding domain (M9NFK2 281-356), the ligand-binding-type
domain (568-800) and the AF-2 motif (789-800) all lie inside the shared 629-aa C-terminal
segment, so no domain or functional motif is missing relative to the canonical product.

## Family placement

UniProt places M9NFK2 in PANTHER PTHR24086:SF15 (NUCLEAR HORMONE RECEPTOR FTZ-F1). The
repo family table `interpro/panther/PTHR24086/PTHR24086-entries.csv` places canonical
P33244, Bombyx FTZ-F1 (P49867) and C. elegans nhr-25 (Q19345) in the same subfamily SF15.
Mammalian NR5A1/SF-1 (SF24) and NR5A2/LRH-1 (SF18) are in different subfamilies, and the
Drosophila paralog Hr39 (Q05192, UniProt name "Nuclear hormone receptor FTZ-F1 beta") is in
SF25. Hr39 is a separate gene and must not be confused with the betaFTZ-F1 isoform.
No disagreement was found between UniProt's subfamily assignment and the repo family review.
