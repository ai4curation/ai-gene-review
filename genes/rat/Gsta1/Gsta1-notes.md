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

## Re-review 2026-10-04

**GOA changes.** Two new seeded rows, both donor splits: cytosol (GO:0005829, ISO, GO_REF:0000121) from human GSTA2 (UniProtKB:P09210) alongside the existing mouse Gsta2 (MGI:MGI:95863) row; and phospholipid-hydroperoxide glutathione peroxidase activity (GO:0047066, ISS, GO_REF:0000024) from human GSTA1 (UniProtKB:P08263) alongside the existing IEA row. No retired rows. Total 31 rows.

**Actions.**
- Cytosol ISO (human GSTA2 donor): PENDING -> KEEP_AS_NON_CORE, consistent with its sibling; location independently shown for rat GSTA1 [PMID:17112229 "was isolated from liver cytosol of rats treated with 14C-BB"]. Sibling reason now names the mouse Gsta2 donor.
- GO:0047066 ISS (human GSTA1 donor): PENDING -> KEEP_AS_NON_CORE. Matches the UniProt by-similarity reaction [UniProtKB:P00502 "Through its glutathione-dependent peroxidase activity toward the fatty acid hydroperoxide (13S)-hydroperoxy-(9Z,11E)-octadecadienoate/13-HPODE it is also involved in the metabolism of oxidized linoleic acid (By similarity)."]; not measured on purified rat enzyme.
- No existing action changed. Supporting quotes on experimental rows that cited only background sentences were replaced with assay-specific ones: PMID:17112229 (liver-cytosol GST purification on GSH-agarose), PMID:15152091 (specific activities of A1-1 homo/heterodimers), PMID:10751412 (Y9F effects on glutathione-conjugate binding in rat GST A1-1), PMID:11119643 (title: rat GST A1-1), PMID:17197701 (dinitrosyl-diglutathionyl-iron complex "binds tightly to Alpha class GSTs in rat hepatocytes").

**Open questions.** The existing questions on rodent alpha-class orthology (which mouse gene is the true Gsta1 counterpart) and on whether the secondary activities have been measured on rat A1-1 remain open.
