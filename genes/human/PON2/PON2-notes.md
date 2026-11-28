# PON2 manual review notes

Automated deep research was not available in this lane without starting an extra
`claude_code` worker, so this review uses the seeded GOA references, UniProt, and
the PTHR11799 PAINT export directly.

## Evidence notes

- PON2 is an intracellular membrane-associated paraoxonase paralog with
  arylesterase and lactonase chemistry. Draganov 2005 expressed and purified all
  three human PONs and found that PON2 was especially active toward pathogenic
  bacterial N-acyl-homoserine lactones (PMID:15772423).
- The 1996 PON-family genomic paper established that PON2 is a PON1-like human
  gene on chromosome 7; it supports family identity but did not assay a
  PON2-specific activity or localization in the abstract (PMID:8661009).
- PON2 is not an HDL particle enzyme like PON1 and PON3. UniProt summarizes
  experimental work placing PON2 on membranes as a peripheral membrane protein,
  and the family-level extracellular-region PAINT row appears to transfer the
  secreted PON1/PON3 state onto PON2.
- The PON2 `GO:0042803 protein homodimerization activity` row comes from the
  Draganov recombinant-protein work and is a quaternary-structure observation,
  not a catalytic function.
- The HYAL2 interaction row is from the BioPlex proteome-scale AP-MS map
  (PMID:33961781). It is a bare protein-binding row and is not needed as a PON2
  molecular-function annotation.
