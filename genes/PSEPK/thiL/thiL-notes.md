# thiL (PP_0519, Q88QH4) curation notes

## Sources

Deep-research providers were not available in this session; no
`-deep-research-<provider>.md` file was generated. No KT2440-specific thiL
publication in the cache. Evidence: UniProt (HAMAP MF_02128), E. coli genetics
[PMID:6284709], ortholog structures [PMID:18311927, PMID:30867460].

## Evidence

- HAMAP function: "Catalyzes the ATP-dependent phosphorylation of thiamine-
  monophosphate (TMP) to form thiamine-pyrophosphate (TPP)"
  [file:PSEPK/thiL/thiL-uniprot.txt]. Record carries CAUTION "Lacks conserved
  residue(s) required for the propagation of feature annotation." -- concerns feature
  transfer; binding residues are still largely assigned; not treated as loss of function.
- PANTHER PTHR30270:SF0 (same subfamily as E. coli ThiL P0AGG0, the only PAINT seed).
- E. coli thiL mutants "lack thiamine monophosphate kinase activity" [PMID:6284709].
- In-line phosphoryl transfer [PMID:18311927]; metal environment [PMID:30867460].
- KT2440 has no IBA rows at all in its GOA (no PSEPK gene in the repo has one), so
  the absence of a PTHR30270 IBA here reflects proteome coverage, not a PAINT decision.

## Decisions (2026-11-12)

- GO:0000287 Mg binding, GO:0005524 ATP binding: KEEP_AS_NON_CORE (cofactor/substrate
  binding entailed by the kinase activity; consistent with THI6/THI80; METJA thiL had
  ACCEPT).
- GO:0009030 TMP kinase: ACCEPT, core.
- GO:0009228: KEEP_AS_NON_CORE (ThiL acts after thiamine-P formation; consistent with
  METJA thiL); GO:0009229: ACCEPT.
- No NEW cytoplasm row added (no GOA location row; kept conservative).
