# LPXC1-5 paralog check

Reproducible comparison of the five Arabidopsis LpxC loci (LPXC1 At1g24793, LPXC2
At1g24880, LPXC3 At1g25054, LPXC4 At1g25145, LPXC5 At1g25210) with each other and with
E. coli LpxC (UniProt P0A725).

Run:

```bash
cd genes/ARATH/LPXC1/LPXC1-bioinformatics
uv run python lpxc_paralog_check.py
```

- Arabidopsis sequences and VAR_SEQ isoform features are parsed from the cached
  `genes/ARATH/LPXC*/LPXC*-uniprot.txt` files.
- E. coli LpxC is downloaded from `https://rest.uniprot.org/uniprotkb/P0A725.fasta`
  and cached as `ecoli_P0A725.fasta`.
- Pairwise identity: Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5;
  global for paralog pairs, local for E. coli comparisons. Identity = identical
  aligned columns / gapless aligned columns.
- Residues inspected (E. coli numbering): Zn(2+) ligands H79, H238, D242 and proton
  donor H265 (UniProt P0A725 BINDING/ACT_SITE features), plus D246, which Li et al.
  2011 (PMID:21709257) list with H238 and H265 as critical for activity.
- Output: `results.json` (all numbers are computed at run time).
