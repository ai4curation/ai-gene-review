# Curation notes: *Pseudomonas putida* KT2440 fadE (Q88LN6, PP_1893)

## Sources

- `fadE-deep-research-openscientist.md` (provider report, already present).
- The UniProt entry is unreviewed; its reaction, EC and pathway lines carry
  ARBA evidence and are not cited. Family cross-references (PANTHER
  PTHR48083:SF18, InterPro FadE_C, Pfam ACDH_C) are cited instead.
- Experimental support is transferred from the E. coli orthologue FadE
  (Q47146; `genes/ECOLI/fadE/`), which is in the same PANTHER subfamily SF18
  and whose mutant cannot grow on C8-C18:1 fatty acids (PMID:12057976).

## Decisions (2026-11 completion pass)

- The earlier draft's UNDECIDED on GO:0005737 cytoplasm is resolved to ACCEPT.
  The Phobius helix at residues 43-64 is a single sequence-analysis line; the
  E. coli orthologue has the same hydrophobic N-terminal stretch, UniProt
  curates no transmembrane segment for it, and E. coli acyl-CoA dehydrogenase
  activity fractionates with the soluble fraction (PMID:334745). Membrane
  association remains a suggested question.
- GO:0003995 changed from MARK_AS_OVER_ANNOTATED to ACCEPT: it is the
  reaction-class term and the module's term for this step.
- GO:0016627 changed from MARK_AS_OVER_ANNOTATED to TOO_GENERAL (true but
  entailed by the accepted chain-length-specific activities).

## 2026-11-04 PR #5935 review round

- The cytoplasm reason now states what outweighs the Phobius helix (the E. coli
  orthologue's identical hydrophobic stretch without a curated TM segment, and
  soluble-fraction activity), and that the catalytic domains face the cytoplasm
  on either topology.
