# fabZ1 / FabN (Enterococcus faecalis V583, Q820V3) curation notes

## 2026-11-13

- FabZ1 is the E. faecalis FabZ homolog that replaces E. coli FabA
  [PMID:15194690 "Therefore E. faecalis FabZ1 is a bifunctional dehydratase/isomerase"].
  Lu et al. call it EfFabN
  [PMID:15980063 "One of these, termed EfFabN, carries out the isomerization reaction in vivo, whereas the other, EfFabZ, does not"],
  and its isomerase activity maps to the beta3/beta4 tunnel strands.
- **Accession mapping caveat.** Wang and Cronan identify the protein only as
  the one "annotated as FabZ1" in the E. faecalis genome. UniProt has two
  FabZ homologs from the V583 genome annotation (PMID:12663927): Q820V3
  (fabZ1, EF_0284) and Q820T5 (fabZ2, EF_2878), both in PTHR30272:SF1.
  FabN is mapped to Q820V3 because its UniProt gene name is fabZ1, taken
  from the same genome annotation the paper uses. The paywalled full text
  could not be retrieved to confirm the locus tag, so this mapping is the
  main uncertainty for this review and for the FabN route of the module.
  UniProt's Q820V3 function text is by similarity to FabZ and does not yet
  mention the isomerase.
- The lipid A biosynthetic process row (UniRule) is removed as a taxon
  mismatch, since E. faecalis makes no lipopolysaccharide; this is recorded as
  a source defect.
- GO:0034017 and GO:0006636 are added as NEW rows. They are member-level
  properties within SF1, which the PTHR30272 family review does not license
  for the subfamily as a whole.
