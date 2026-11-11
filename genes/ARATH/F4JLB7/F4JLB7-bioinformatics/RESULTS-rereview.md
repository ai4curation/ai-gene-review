# F4JLB7 re-review analyses (2026-10-20)

Independent of any ProtNLM2 output. Reproduce with
`uv run --no-project python c_terminus_and_crib_scan.py` (stdlib only; sequences
fetched live from UniProt). Raw output: `results-rereview.tsv`.

## 1. Phylogenetic placement (PANTHER 19.0 tree, Arabidopsis-pruned)

Retrieved from the PANTHER API (`treeinfo?family=PTHR48004&taxonFltr=3702`) and
`geneinfo` on 2026-10-20. F4JLB7 (AT4G28560) is the only member of subfamily
PTHR48004:SF38 in Arabidopsis; the frozen UniProt record instead lists PTHR48004:SF58.
In the PANTHER 19.0 tree F4JLB7 is sister to the clade containing TMM (TOO MANY MOUTHS,
Q9SSD1) and RLP29 (Q9SJH6), both in subfamily SF42 (node PTN008481374). That clade is in
turn sister to the PII-2 clade (SF55, Q5PP26). CLV2 (O80809, SF9) is in the other major
clade of the family.

```
PTN008727258 (family root, duplication)
  PTN008727295
    PTN002404959  PII-2 (Q5PP26), At3g25670           [SF55]
    PTN008481374
      F4JLB7 (AT4G28560)                              [SF38]
      PTN009222082  TMM (Q9SSD1), RLP29 (Q9SJH6)      [SF42]
  PTN008727306
    CLV2 (O80809), At1g13910, RLP16                   [SF9/SF34/SF73]
```

The nearest experimentally characterised relative is therefore TMM, a paralog in a different
subfamily. TMM-specific functions (EPF-peptide recognition with ERECTA-family receptors in
stomatal patterning) are not transferable to F4JLB7 on this basis.

## 2. C-terminal hydrophobic segment

The most C-terminal 19-residue Kyte-Doolittle window with mean >= 1.6:

| accession | protein | length | window | residues after window |
|---|---|---|---|---|
| F4JLB7 | AT4G28560 | 450 | 431-449 (1.85) | 1 |
| Q9SSD1 | TMM | 496 | 478-496 (1.76) | 0 |
| O80809 | CLV2 | 720 | 691-709 (1.78) | 11 |

F4JLB7, like TMM, ends in a hydrophobic segment with essentially no cytoplasmic tail. This is
compatible with either a single-pass type I anchor or a GPI-attachment signal; the analysis
cannot distinguish the two.

## 3. CRIB motif scan

A plant RIC CRIB pattern that detects the positive control Q1G3K8 (AT4G28556, UniProt CRIB
domain 36-49, `IGNPTDVKHVAHIG`) finds no CRIB motif in F4JLB7 or in any PTHR48004 member
tested. F4JLB7 therefore lacks the motif required for binding GTP-bound ROPs.
