# DUT1 (P33317) notes

Module: `dntp_de_novo_synthesis`, role = dUTP diphosphatase (dUMP source variant).

## Evidence journal
- Essential; death by uracil incorporation [PMID:8223452 "in the absence of dUTPase, cell death results from the incorporation of uracil into DNA"]
- Biochemistry and structure [PMID:21548881 "The hydrolysis of dUTP by DUT1 was strictly dependent on a bivalent metal cation"; "Mg2+ supported the highest rate of dUTP hydrolysis by DUT1"]
- dITP side activity, physiological relevance unknown [PMID:21548881 "In addition, DUT1 showed a significant activity against another potentially mutagenic nucleotide: dITP."; "This suggests that S. cerevisiae might potentially use two enzymes to detoxify dITP, DUT1 and HAM1."]

## Annotation decisions
- dITP diphosphatase IDA: KEEP_AS_NON_CORE; dITP catabolic process IDA: MARK_AS_OVER_ANNOTATED (in vitro only).
- GO:0006207 'de novo' pyrimidine nucleobase biosynthesis (RCA): REMOVE.

## YeastCyc
- DUTP-PYROP-RXN carries EC 3.6.1.23 and the broad EC 3.6.1.9; the latter is not a separate Dut1 activity.
