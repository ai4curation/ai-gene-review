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
  its actual pentosyltransferase parent GO:0016763 while GO:0002099 records the
  exact wobble-guanine process. AmiGO confirms that GO:0008479 is restricted to
  the RHEA:16633 free-queuine reaction and that GO:0016763 is one of its direct
  `is_a` parents. GO:0050147 was rejected because it describes free-nucleoside
  ribosyltransferase chemistry rather than a tRNA substrate. A dedicated
  bacterial preQ1 transglycosylase MF term would be preferable.
- The reviewed record assigns one zinc ion per subunit, so GO:0008270 zinc ion
  binding is added as a missing annotation. [file:PSEPK/tgt/tgt-uniprot.txt
  "Note=Binds 1 zinc ion per subunit."]
- Upstream preQ0 production is outside scope; Tgt receives preQ1 from QueF and
  supplies preQ1-tRNA to QueA.

## OpenScientist reconciliation

Source: `file:PSEPK/tgt/tgt-deep-research-openscientist.md`.

- The report independently identifies Q88PL7 as bacterial Tgt and supports
  preQ1 insertion at guanine 34 rather than the eukaryotic free-queuine
  reaction.
- Its sequence, AlphaFold, operon, and pathway-completeness analyses are
  computational corroboration, not organism-specific experimental evidence.
- The report explicitly found no biochemical, structural, kinetic, or genetic
  study of Q88PL7 itself. The curated review therefore retains the existing
  orthology-based confidence level and records this as a knowledge gap.
