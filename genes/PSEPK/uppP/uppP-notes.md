# uppP notes

- UniProt assigns Q88IY7 hydrolysis of undecaprenyl diphosphate to
  undecaprenyl phosphate
  [file:PSEPK/uppP/uppP-uniprot.txt "Catalyzes the dephosphorylation of undecaprenyl diphosphate"].
- The protein is a multi-pass inner-membrane enzyme
  [file:PSEPK/uppP/uppP-uniprot.txt "SUBCELLULAR LOCATION: Cell inner membrane"].
- Bacitracin resistance is a supported consequence of maintaining the carrier
  pool, but it is not substituted for the conserved phosphatase reaction
  [file:PSEPK/uppP/uppP-uniprot.txt "Confers resistance to bacitracin"].
- OpenScientist found conservation of the ortholog-defined catalytic residues
  but no direct biochemical or genetic experiment on Q88IY7
  [file:PSEPK/uppP/uppP-deep-research-openscientist.md "No direct experimental data on the *P. putida* KT2440 protein"].
- PAP2-family phosphatases may provide overlapping C55-PP phosphatase activity,
  but no such annotation is transferred to a KT2440 candidate without
  paralog-specific evidence
  [file:PSEPK/uppP/uppP-deep-research-openscientist.md "two unrelated families of integral membrane proteins exhibit undecaprenyl-diphosphate phosphatase activity"].
- Periplasm-facing catalysis and a possible C55-P flippase role are
  ortholog-derived or speculative and are not asserted as Q88IY7 core
  functions.

## 2026-11-02 completion pass

- Membrane (GO:0016020) changed from MARK_AS_OVER_ANNOTATED to TOO_GENERAL: plasma
  membrane is accepted and entails it.
- Truncated UniProt and deep-research quotes completed; the NEW GO:0016094 row now also
  cites the E. coli ortholog study [PMID:15778224 "The enzyme function is to synthesize the carrier lipid"].
  Status set to COMPLETE.
- Review round (PR #5923): proposed new term "undecaprenyl phosphate biosynthetic process" added and cross-referenced from the NEW GO:0016094 row; no GO:0016311 row exists on this gene.
