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
- The OpenScientist report recovered the same PP_2371/Q88KB9 sulfite-reductase
  hemoprotein identity but followed KEGG in mapping a NADPH-dependent CysJ
  partner to PP_0860/PP_1703. I treated that donor model as disputed rather than
  as independent support because the KO-based transfer does not distinguish
  E. coli CysJ from the Fpr-class reductases implicated by PMID:23794620.

## Open issue

Reconstitute CysI with Fpr-I and candidate KT2440 ferredoxins or flavodoxins to
resolve the immediate electron donor.


## Comparative sulfate-assimilation audit — 2026-10-26

Re-reviewed all five rows. Supersedes the first-pass donor choice: the prior NEW ferredoxin-specific GO0050311 is retired and UNDECIDED, because full [PMID:23794620] leaves direct FprA transfer or carrier-mediated transfer unresolved. Positive sulfite-reduction chemistry is retained, and the general oxidoreductase term is refined to current GO0016667 sulfur-group redox activity. Live QuickGO confirmed GO0016002 is obsolete. PTHR32439 contains multiple reductase substrates and is not used as a donor assay. The old P9WJ02 comparator is CDC1551, whereas direct H37Rv experiments concern P9WJ03. OpenScientist’s CysJ assignment remains disputed; Fpr is an FAD-containing FNR, not a CysJ diflavin subunit.

Research provenance: parent already attempted Falcon (403) and Perplexity-lite (401 quota) for this batch; no generated report was fabricated. Existing PSEPK OpenScientist reports were used only as discovery. Source caches were fetched normally and never hand-edited. All original annotation payloads were preserved, with a retirement marker only for the existing CysI donor-specific NEW proposal.
