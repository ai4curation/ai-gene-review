# cysI curation notes

## First-pass synthesis

- Q88KB9 has the siroheme/iron-sulfur domain architecture and deposited product
  name expected for the catalytic CysI sulfite reductase hemoprotein
  [UniProtKB:Q88KB9, "Sulphite reductase hemoprotein, beta subunit"].
- Q88KB9 belongs to PTHR32439, whose reviewed members include the
  ferredoxin-dependent sulfite reductase Sir P9WJ02
  [file:interpro/panther/PTHR32439/PTHR32439-entries.csv,
  "P9WJ02,Sulfite reductase [ferredoxin]"]. The classical E. coli CysI P17846
  instead belongs to PTHR11493:SF47
  [file:interpro/panther/PTHR11493/PTHR11493-entries.csv,
  "P17846,Sulfite reductase [NADPH] hemoprotein beta-component"].
- Q88KB9's `PTHR32439:SF9` label is not used as evidence because that subfamily
  includes misleading CobG/BLR3264 labeling. The ferredoxin-specific proposal
  rests on the broader family, the exact Sir exemplar, and pathway context.
- Pseudomonas genetics place FprA in effective sulfate assimilation and indicate
  a sulfite-reduction architecture distinct from enterobacterial CysJI
  [PMID:23794620, "fprA is necessary for effective sulfate assimilation by P.
  putida"]. These experiments used P. putida DSM 3601 rather than KT2440 and
  therefore corroborate the pathway model rather than directly assaying Q88KB9.
- The paper leaves open whether FprA transfers electrons through reduced
  ferredoxin or directly. GO:0050311 is therefore the best current functional
  model, not a claim that the exact carrier has been reconstituted.

## Open issue

Reconstitute CysI with Fpr-I and candidate KT2440 ferredoxins or flavodoxins to
resolve the immediate electron donor.
