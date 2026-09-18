# yfiH curation notes

## 2026-08-13 purine-salvage boundary review

The current Q88Q72 record is internally contradictory. RuleBase names it a
purine nucleoside phosphorylase and ARBA supplies purine reactions, but NCBIfam
assigns TIGR00726 PgeF and PTHR30616:SF2 consists of reviewed peptidoglycan
editing factors. The experimentally characterized E. coli ortholog is a
cytoplasmic amidase that hydrolyzes incorrect UDP-MurNAc-L-serine precursor
[PMID:35164571, "YfiH hydrolyzes UDP-MurNAc-monopeptide into UDP-MurNAc"].

Recombinant bacterial family members do show PNP activity in vitro
[PMID:31978345, "recombinantly expressed DUF152 bacterial proteins YlmD and
YfiH metabolized adenosine to inosine and adenine"]. However, a direct 2025
comparison found that PNP activity required over 500-fold more protein than
precursor editing and that PgeF did not rescue PNP loss in E. coli
[PMID:40632566, "PgeF fails to compensate for the absence of PNP activity in E.
coli"]. The purine assignment is therefore excluded from pathway
satisfiability but retained as a non-core biochemical uncertainty.

The copper-binding GOA row is removed as a historical family/domain overcall.
The review transfers the broad amidase and peptidoglycan-biosynthesis roles by
ISS and proposes a substrate-specific GO molecular-function term. Direct assay
of Q88Q72 is still needed.
