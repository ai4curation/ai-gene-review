# ubiG review notes (E. coli K-12, P17993)

Reviewed for the ubiquinone_biosynthesis module (bacterial ring-modification
route, both O-methylation annotons).

## Provenance

- No deep-research provider was available (no API keys), so there is no
  `-deep-research-<provider>.md` file and none was fabricated. The review is
  built from the reviewed UniProt record, the cached publications and the
  PTHR43464 PAINT table.
- Cached publications are abstract-only (PMID:10419476 full text is
  subscription-only; Europe PMC lists no PMC copy).

## Function

- UbiG catalyses both O-methylations. [PMID:10419476 "E. coli UbiGp was
  purified and found to catalyze both O-methylation steps."]
- The first bacterial substrate is 2-polyprenyl-6-hydroxyphenol; in vitro UbiG
  also methylates the eukaryotic (carboxylated) analogue. [PMID:8703953 "UbiG
  methylates both the derivative of the eukaryotic intermediate,
  3,4-dihydroxy-5-farnesylbenzoate, as well as that of the E. coli
  intermediate, 2-farnesyl-6-hydroxyphenol."]
- UbiG is part of the soluble Ubi metabolon. [PMID:30686758 "We purify the Ubi
  complex from cytoplasmic extracts and demonstrate that UQ biosynthesis occurs
  in this fraction"]
- UbiG binds PG/CL membranes via a conserved insertion needed in vivo.
  [PMID:26251450 "Mutation of the key residues renders UbiG unable to
  efficiently bind liposome in vitro and the mutant fails to rescue the
  phenotype of ΔubiG strain in vivo."]

## Decisions worth flagging

- GO:0008425 (IDA, PMID:10419476, EcoCyc) is the UbiE C-methylation term; the
  paper reports O-methylation only. MODIFY to GO:0061542 with a source defect
  for EcoCyc.
- GO:0010420 (InterPro2GO) is the eukaryotic first O-methylation substrate:
  MARK_AS_OVER_ANNOTATED, same as P. putida UbiG and in line with the
  PTHR43464 family review. The family review lists only the P. putida member
  as an exception; E. coli UbiG could be added there.
- GO:0042538 hyperosmotic salinity response is an end-product (Q8) effect:
  MARK_AS_OVER_ANNOTATED.
