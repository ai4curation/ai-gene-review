# fib-1 review notes

## 2026-10-28 session

- fetch-gene resolved Q22053 (FBRL_CAEEL, WBGene00001423, GeneID 179999) as requested;
  22 GOA rows.
- Cached publications read: PMID:18804378 (full), PMID:22768349 (full), PMID:26492166
  (full), PMID:36329008 (full), PMID:23705068 (full; FIB-1 used as TORC1 readout in the
  intestine), PMID:28853436 (full), PMID:30190478 (full). PMID:14872060 (RBD-1 paper) is
  abstract-only; the abstract does not mention FIB-1, so the nucleolus IDA is accepted on
  trust (FIB-1 is the standard nucleolar marker and the claim is confirmed by three other
  papers). PMID:18312858 is abstract-only.
- Literature summary with provenance: see `fib-1-deep-research-manual.md`.

### Decisions

- Core: rRNA methyltransferase activity (GO:0008649), rRNA methylation, rRNA processing,
  box C/D snoRNP complex, small-subunit processome, nucleolus / fibrillar center.
  No worm enzymology exists; catalytic assertion rests on fibrillarin family conservation
  (all SAM-binding residues present, PS00566 signature).
- methyltransferase activity (IEA) -> MODIFY to rRNA methyltransferase activity and
  histone H2AQ104 methyltransferase activity (both carried by the gene).
- protein-glutamine N-methyltransferase activity (RHEA IEA) -> MODIFY to histone H2AQ104
  methyltransferase activity; that histone activity is kept as non-core (by similarity only).
- chromatin remodeling (IEA from GO:1990259 via GO_REF:0000108) -> over-annotation: no worm
  evidence; H2AQ105me is a histone mark, not a remodeling activity.
- Cajal body (IBA, metazoan node PTN000818345): UNDECIDED - no Cajal body localization
  has been shown for FIB-1, and C. elegans Cajal bodies are poorly defined; nucleoplasmic
  FIB-1 foci in early embryos were interpreted as prenucleolar-body-like structures
  [PMID:22768349].
- positive regulation of translation (IMP): 20% drop in 35S incorporation after fib-1 RNAi
  is an indirect consequence of reduced ribosome biogenesis -> MARK_AS_OVER_ANNOTATED.
- nucleologenesis (IMP): fib-1 loss gives small nucleoli; fibrillarin GAR domain
  contributes to nucleolar phase separation in other organisms -> KEEP_AS_NON_CORE.
- No NEW terms proposed (phenotypes on lifespan, immunity, neuron size do not meet the bar).
