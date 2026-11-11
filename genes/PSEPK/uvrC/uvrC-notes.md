# uvrC (Pseudomonas putida KT2440, Q88FJ7, PP_4098) notes

Reviewer: Claude (AI-assisted).

## Sources

- `uvrC-deep-research-falcon.md` (provider report, read in full). It found no KT2440-specific
  UvrC biochemistry or mutant; KT2440 context it reports (predicted pp4100-gacA-uvrC-pgsA
  operon; uvrB mutant hypersensitive to formaldehyde) is pathway context, not UvrC data.
- UniProt Q88FJ7 is a reviewed entry annotated by HAMAP rule MF_00203: "UvrC both incises the 5'
  and 3' sides of the lesion" and "Interacts with UvrB in an incision complex."
- E. coli ortholog evidence (see `genes/ECOLI/uvrC/uvrC-notes.md`): R42 is the 3' incision
  catalytic residue [PMID:10671556 "substitution R42A abolishes 3' incision"]; D399, D438, D466
  and H538 are required for 5' incision [PMID:1387639 "Enzyme reconstituted with these mutant
  proteins carried out normal 3' incision but was completely defective in 5' incision activity"].

## Bioinformatics

`uvrC-bioinformatics/RESULTS.md`: global alignment to E. coli UvrC (53.3% identity over the
E. coli length). R42 aligns to R42; D399, D438, D466, H538 align to D398, D437, D466, H534.
Both incision active sites are predicted intact.

## Decisions (revised from the earlier DRAFT)

- GO:0009381 excinuclease ABC activity: ACCEPT (was MARK_AS_OVER_ANNOTATED). Both
  incision chemistries reside in UvrC, so it enables the activity as catalytic subunit;
  consistent with the E. coli review. Core MF is GO:0009381 (is_a GO:0004520).
- GO:0004520 NEW (ISS from P0A8G0) removed on PR review (2026-11-10): it is an ancestor of the accepted core
  GO:0009381, so adding it is redundancy, not new coverage. Propagation gap noted for follow-up: KT2440 UvrC
  receives no IBA row from the PTHR30562 PAINT node PTN000778007 (GO:0004520), although its E. coli ortholog
  does; this is a PAINT/GOA propagation gap, not missing biology.
- DNA repair and DNA damage response: MODIFY to nucleotide-excision repair (were
  KEEP_AS_NON_CORE while arguing they were too general).
- SOS response: MARK_AS_OVER_ANNOTATED (was KEEP_AS_NON_CORE). E. coli uvrC is not
  UV-inducible [PMID:3295776 "transcription from both promoters on the chromosome is not
  inducible by UV damage"]; no KT2440 LexA evidence was found.
