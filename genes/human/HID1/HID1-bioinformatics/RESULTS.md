# HID1 (Q8IV36) ortholog grounding

Script: `hid1_orthologs.py` (run with `uv run hid1_orthologs.py > RESULTS-orthologs.tsv`).
It fetches each UniProt record live, reports the PANTHER cross-reference, and computes a
global BLOSUM62 alignment to human HID1. Identity is identical residues divided by aligned
(non-gap) columns.

| accession | organism | length | PANTHER subfamily | identity to Q8IV36 |
|---|---|---|---|---|
| Q8IV36 | human HID1 | 788 | PTHR21575:SF12 | 1.000 |
| Q8R1F6 | mouse Hid1 | 788 | PTHR21575:SF12 | 0.957 |
| D4A0C3 | rat Hid1 | 788 | PTHR21575:SF12 | 0.953 |
| Q0E9B5 | Drosophila CG8841 | 837 | PTHR21575:SF12 | 0.687 |
| G5EG65 | C. elegans hid-1 | 729 | PTHR21575:SF12 | 0.612 |
| O13776 | S. pombe SPAC17A5.16 | 925 | PTHR21575:SF13 | 0.320 |

## Interpretation

- Human, mouse and rat HID1 share PANTHER subfamily SF12, are the same length, and are
  about 95-96% identical. Experimental findings made with mouse or rat HID1 (secretory
  granule maturation in mouse beta cells; LDCV biogenesis in rat PC12 and INS-1 cells)
  therefore transfer to human HID1 as orthologous findings.
- The metazoan members C. elegans hid-1 and Drosophila CG8841 also fall in SF12.
- The fission yeast Golgi protein SPAC17A5.16, the only seed of the eukaryote-level
  GO:0007030 Golgi organization IBD at PTN000491103, is in a different subfamily (SF13)
  and is only about 32% identical over the aligned columns. The Golgi organization IBA on
  human HID1 is therefore an inference that reaches across subfamilies, made by the PAINT
  curator at the eukaryote node, and none of the SF12 papers reviewed for HID1 (PMID:21337012, PMID:29074564,
  PMID:27751232, PMID:37751424, PMID:33999436) reports a Golgi stack organization defect.
