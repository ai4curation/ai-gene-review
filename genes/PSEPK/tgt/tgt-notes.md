# tgt review notes

- Q88PL7 is a reviewed bacterial Tgt homodimer assigned to PTHR46499:SF1.
  [file:PSEPK/tgt/tgt-uniprot.txt
  "RecName: Full=Queuine tRNA-ribosyltransferase"]
  [file:interpro/panther/PTHR46499/PTHR46499-entries.csv
  "Q88PL7,Queuine tRNA-ribosyltransferase"]
- The bacterial reaction exchanges guanine 34 for preQ1. It is not the
  eukaryotic reaction that inserts free queuine. [file:PSEPK/tgt/tgt-uniprot.txt
  "queuine precursor 7-aminomethyl-7-deazaguanine (PreQ1) at position 34"]
  [PMID:40703034 "the mutant does not insert preQ1 in tRNA"]
- GO:0008479 currently defines the free-queuine reaction, so it was modified to
  the chemically correct parent GO:0050147 while GO:0002099 records the exact
  wobble-guanine process. A dedicated bacterial preQ1 transglycosylase MF term
  would be preferable.
- Upstream preQ0 production is outside scope; Tgt receives preQ1 from QueF and
  supplies preQ1-tRNA to QueA.
