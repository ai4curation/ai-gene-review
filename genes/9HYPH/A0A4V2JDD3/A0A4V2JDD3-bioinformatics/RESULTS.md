# Hans-LanM (A0A4V2JDD3) versus Mex-LanM (C5B164): EF-hand loops and identity

Script: `compare_lanm.py` (Biopython PairwiseAligner, global, BLOSUM62, gap open -10,
extend -0.5). Input sequences are read from the cached UniProt flat files
`genes/9HYPH/A0A4V2JDD3/A0A4V2JDD3-uniprot.txt` and `genes/METEA/lanM/lanM-uniprot.txt`.
Raw output: `compare_lanm_output.txt`.

## EF-hand loops (12-residue windows, numbering on the displayed UniProt sequences)

| EF hand | Hans-LanM loop (start) | Hans position 2 | Mex-LanM loop (start) | Mex position 2 |
|---|---|---|---|---|
| EF1 | NKDNDDSLEIAE (34) | K | DPDKDGTIDLKE (35) | P |
| EF2 | NPDGDTTLESGE (58) | P | DPDKDGTLDAKE (59) | P |
| EF3 | NKDGDQTLEMDE (83) | K | DPDNDGTLDKKE (84) | P |
| EF4 | DANKDGKLTAAE (107) | A | NPDNDGTIDARE (108) | P |

Hans-LanM carries Pro at loop position 2 only in EF2 (Pro59); Mex-LanM has Pro2 in all four
EF hands. Hans-LanM EF1-EF3 begin with Asn (N1) and have Glu at positions 9 and 12; EF4 lacks
an acidic residue at position 9 (Thr). Adjacent Hans-LanM loops are spaced 12-13 residues
apart (34->58->83->107 starts give 12-13 residue linkers after each 12-residue loop), the
LanM-specific spacing. EF3 in this numbering contains Asp85 (position 3) and Glu91 (position 9),
and Arg100 lies in the following helix, matching the residue numbers used for the crystal
structures in PMID:37259003 (the paper numbers residues on the full-length precursor that
UniProt displays).

## Global pairwise identity

- Full length (133 vs 133): 45 identical residues, 33.8% of Hans-LanM length (33.1% of
  alignment columns).
- Mature chains, each from its own UniProt `FT CHAIN` feature (Hans-LanM 24-133, SignalP;
  Mex-LanM 22-133, experimentally evidenced): 38 identical residues, 34.5% of the Hans-LanM
  mature chain (33.6% of alignment columns).

This agrees with the 33% identity reported in PMID:37259003.

## Interpretation

The sequence satisfies the LanM hallmarks used in PMID:37259003 (four EF hands, short
inter-loop spacing, at least one Pro2). Low identity to Mex-LanM and the different Pro2
pattern are consistent with the divergent metal selectivity reported experimentally; the
analysis itself does not demonstrate lanthanide binding, which rests on the published
biochemistry and crystal structures.
