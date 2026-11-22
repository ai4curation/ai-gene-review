# CNOT8 notes

## 2026-11-22

CNOT8 is the human POP2/CAF1B paralog in PTHR10797:SF1, paired with CNOT7 (CAF1) in
PTHR10797:SF79. The current GOA fetch had 46 annotation rows plus the header, so it was
not a failed header-only fetch.

`just paint-losses human CNOT8` reported no IRD or IKR losses on the CNOT8 lineage. The
four PTHR10797 PAINT rows all sit at `PTN000084083` and cover the conserved CAF1/POP2
core: `GO:0004535` poly(A)-specific ribonuclease activity, `GO:0030015` CCR4-NOT core
complex, `GO:0000288` deadenylation-dependent decay, and the contextual `GO:0000932`
P-body row.

The direct nuclease anchor is PMID:15769875, which assayed both human CAF1/CNOT7 and
POP2/CNOT8 on poly(A) substrate and supports refining the generic RNA exonuclease row to
`GO:0004535`. PMID:20065043 and PMID:22977175 ground CNOT8 in miRNA-target and
NOT1-recruited deadenylation. The CNOT1/CNOT2/CNOT3/CNOT6/CNOT6L/BTG/TOB/PATL1
interaction rows are kept only as evidence for complex or recruitment contexts; the
bare `GO:0005515` rows are removed under the protein-binding policy.
