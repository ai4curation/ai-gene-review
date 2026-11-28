# PON3 manual review notes

Automated deep research was not available in this lane without starting an extra
`claude_code` worker, so this review uses the seeded GOA references, UniProt, and
the PTHR11799 PAINT export directly.

## Evidence notes

- PON3 shares the family lactonase fold and in Draganov 2005 hydrolyzed aromatic
  lactones and bulky drug lactones such as lovastatin and spironolactone
  (PMID:15772423). The same abstract says organophosphates were hydrolyzed
  almost exclusively by PON1, so EC-only aryldialkylphosphatase rows on PON3
  should be treated as, at most, weak promiscuous activity.
- PON3 is secreted and extracellular, in contrast to PON2. The HDL-associated
  Reactome events are plausible because PON3 behaves like an HDL-associated
  serum PON, but ER membrane rows represent transit of a secreted protein rather
  than a function at the ER membrane.
- The PON3 `GO:0042803 protein homodimerization activity` row comes from the
  Draganov recombinant-protein work and is a quaternary-structure observation,
  not a catalytic function.
- The PON3 extracellular-exosome HDA row is from parotid exosome proteomics
  (PMID:19199708). It supports detection in a human extracellular vesicle
  preparation but does not establish that exosomal PON3 has a core activity
  there.
- The mouse superoxide-regulation row reflects a downstream antioxidant
  phenotype rather than a direct molecular function of human PON3, so the
  Ensembl transfer should not be kept as a core human PON3 process.
