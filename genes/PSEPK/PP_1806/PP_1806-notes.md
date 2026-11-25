# PP_1806 curation notes

- Q88LX1 carries the exact EC 5.3.1.13/Rhea 23104 reaction and belongs to the
  GutQ/KpsF API subfamily [file:PSEPK/PP_1806/PP_1806-uniprot.txt,
  "Reaction=D-arabinose 5-phosphate = D-ribulose 5-phosphate"].
- PP_1806 is immediately followed by kdsA2/PP_1807, supporting a KDO-pathway
  interpretation, but there is no direct KT2440 assay or pathway-specific gene
  name for this copy.
- The molecular function is accepted while the physiological division of labor
  with kdsD remains an explicit question.
- The reviewed record places both PP_1806 and KdsD in `PTHR42745:SF1`; the
  second-API interpretation therefore comes from synteny and the comparative
  E. coli GutQ paradigm, not a discriminating PANTHER subfamily
  [PMID:16199563, "Recombinant GutQ was shown to indeed be a second copy of
  API"].

## 2026-11-10 completion pass

- Generic parent rows that the evidence refines were changed to MODIFY with the
  specific KDO-pathway term (rather than MARK_AS_OVER_ANNOTATED), matching the
  E. coli exemplar reviews; substrate-binding rows stay KEEP_AS_NON_CORE.
- Every row now carries a vetted quote (UniProt curated rule/family lines,
  PANTHER PAINT rows, or E. coli ortholog papers clearly marked as such).
- No provider deep research was generated (no provider access in this session).
- Generic process rows are KEEP_AS_NON_CORE, not refined to GO:0019294,
  because the pathway receiving PP_1806's arabinose 5-phosphate is untested.
