# SMIM45 ORF check

Script: `orf_check.py` (run `python3 -I orf_check.py`; raw output in `run_output.txt`).
It fetches UniProt A0A590UK83 sequence versions from UniSave (entry v11 = sequence v1;
entry v12 = sequence v2) and every Ensembl transcript of ENSG00000205704, locates both
proteins by three-frame translation, and maps the forward primers reported in
PMID:36593289 Methods.

Results (from `run_output.txt`):

- Sequence v1 (entries 1-11, up to 2023_01) is 107 aa (MSMAACPEAP...); sequence v2
  (from 2023_03, current) is 68 aa (MPHFLDWFVP...). The two share no sequence.
- In all 12 Ensembl transcripts both ORFs are present on the same mRNA, non-overlapping;
  e.g. in MANE ENST00000381348 the 68-aa ORF is at cDNA nt 286-493 and the 107-aa ORF
  at nt 817-1141 (0 nt overlap). The 107-aa ORF is therefore a downstream ORF.
- The KO genotyping primer KO-GT-F (ATGTCTATGGCTGCCTGTCCTG) begins at nt 817, the
  start codon of the 107-aa ORF; the qPCR primer ORF-RT-F lies at nt 845, also inside the
  107-aa ORF. Neither primer touches the 68-aa ORF.

Interpretation: the knockout, over-expression and localization experiments of
PMID:36593289 address the 107-aa product, which no longer has a UniProt accession; the
GO rows from that paper now sit on the unrelated 68-aa protein.
