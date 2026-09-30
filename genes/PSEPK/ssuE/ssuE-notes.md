# ssuE curation notes

## Identity and evidence

- Q88R97 is the reviewed PP_0236 SsuE-family NADPH-dependent FMN reductase at
  the start of the KT2440 `ssuEADCB` locus
  [file:PSEPK/ssuE/ssuE-uniprot.txt, "Belongs to the SsuE family"].
- Purified E. coli SsuE P80644 is the explicit ISS comparator and directly
  supplies reduced FMN to SsuD [PMID:10480865, "SsuE is the FMN reducing enzyme
  providing SsuD with FMNH(2)"].
- P. putida S-313 genetics provides both positive pathway evidence and an
  essentiality caveat: SsuE was needed for arylsulfonate growth but was
  dispensable for tested aliphatic sulfonates, implying an alternative
  reductase [PMID:10781557, "was needed for growth with arylsulfonates";
  "suggesting that an alternative isozyme exists"]. This is why the reusable
  module makes canonical SsuE-mediated FMNH2 supply optional while retaining
  the SsuD requirement for reduced FMN.

## Research coverage

The completed OpenScientist process for `ssuE` did not materialize a report in
this worktree. No provider output was reconstructed or invented. Curation uses
the exact reviewed UniProt record, the purified E. coli ortholog, and direct
Pseudomonas locus genetics.

## Localization

The reaction is expected in the cytoplasm, but the exact Q88R97 record has no
subcellular-location assertion and no target-specific localization experiment
was found. No GO cellular-component annotation was added.
