# Gsta1 review notes

## Evidence summary
- [UniProtKB:P00502] UniProt describes Gsta1 as catalyzing glutathione attack on electrophilic exogenous and endogenous compounds.
- [PMID:11119643] The UniProt entry cites this publication for the EC 2.5.1.18 glutathione transferase reaction.

## Curation decisions
- Core function: glutathione S-transferase alpha-1 (glutathione transferase activity, GO:0004364).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## Review follow-up (PR #2374)
- GO:0005739 mitochondrion (ISO, GO_REF:0000121) changed from KEEP_AS_NON_CORE to
  MARK_AS_OVER_ANNOTATED. It enters only by symbol-matched ISO transfer from mouse
  MGI:MGI:95863 (`Gsta1-goa.tsv:13`); no rat observation supports it, and UniProt records
  only [UniProtKB:P00502 "SUBCELLULAR LOCATION: Cytoplasm."]. The previous `reason`
  ("records where Gsta1 has been observed") also contradicted `suggested_experiments[2]`
  in the same file.
- The same donor MGI:MGI:95863 is still trusted for GO:0004364 and GO:0005829 because both
  are independently confirmed in rat by direct assay — GO:0004364 IDA PMID:15152091 and
  GO:0005829 IDA PMID:17112229 (`Gsta1-goa.tsv:23`) — so those transfers are not
  load-bearing. Mitochondrion has no such independent rat evidence.
- Removed the claim that mouse Gsta2 (MGI:MGI:95863) is a "Yc2-type subunit, not a Ya-type
  one" from the GO:0009617 and GO:0035634 propagation comments, the donor `source_label`s,
  and `suggested_questions[2]`. It rested only on the parenthetical in MGI's legacy gene
  name string, with no citable source, and rodent Yc subunits are conventionally the
  GSTA3/GSTA5-type products. The auditable half of the argument — rodent alpha-class GST
  symbols are not 1:1 orthologous between mouse and rat, so symbol-matched ISO transfer is
  unwarranted — is retained and carries the conclusion on its own. Rat P00502 is still
  described as Ya-1, which is UniProt-documented [UniProtKB:P00502 "AltName: Full=Glutathione
  S-transferase Ya-1;"].
- GO:0035634 response to stilbenoid: replaced failure mode ROLE_CONFLATION with
  SOURCE_EVIDENCE_WEAK (keeping WRONG_ORTHOLOG_OR_PARALOG). GO "response to X" terms do
  cover transcriptional induction by X, so a gene being a downstream target of the response
  is not role conflation; the real objection is that the induction was shown for a mouse
  paralog and never for rat Gsta1. ROLE_CONFLATION is retained on GO:0030855 epithelial
  cell differentiation, where `involved_in` genuinely does claim participation.
