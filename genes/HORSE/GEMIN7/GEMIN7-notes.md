# GEMIN7 (horse, A0A9L0T0I7) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review (no prior review file existed for this folder). ProtNLM2 predictions were not
consulted.

### Identity

- A0A9L0T0I7 (TrEMBL, PE 3) is 131 aa, the same length as human GEMIN7 Q9H840, and aligns end
  to end without gaps at 88.5% identity (file:HORSE/GEMIN7/GEMIN7-bioinformatics/RESULTS.md).
  It is the canonical full-length product of horse GEMIN7, not a fragment, isoform or
  alternative gene model. Sm domain (65-131) and the N-terminal Arg/Gly-containing
  SMN-binding segment are present.
- PANTHER PTHR14679 has a single subfamily, SF1, containing human, mouse, bovine GEMIN7 and
  S. pombe gem7, so the horse protein is in the same subfamily as all characterised members.
  No family review exists under interpro/panther/PTHR14679 (only entries/metadata), so there
  is no placement disagreement to report.

### Deep research

`just deep-research-falcon HORSE GEMIN7 --fallback perplexity-lite` failed twice: falcon
returned "Failed to authenticate" (HTTP 403) and the perplexity-lite fallback timed out at
600 s. Review proceeds from cached literature (PubMed search gemin7[tiab], 20 hits; the
relevant papers were cached with `just fetch-pmid`).

### Literature (human unless noted)

- [PMID:12065586 "Gemin7 interacts directly with SMN and Gemin6 and mediates the association of
  Gemin6 with the SMN complex"]; also binds Sm proteins, especially SmE; cytoplasm and gems.
- [PMID:15939020 "Gemin6 and Gemin7 exist as a heterodimer"] with Sm folds; the heterodimer binds
  Sm proteins.
- [PMID:17178713 "SMN, Gemin8, and Gemin7 in its center"] of the SMN complex.
- [PMID:17023415 "Gemin6, Gemin7, and Unrip form a stable cytoplasmic complex"]; loss of this
  module from SMN impairs Sm protein, but not snRNA, association.
- [PMID:19321448 "Gemin7 knockdown revealed a decrease in snRNP assembly activity"]; Gemin6-Gemin7
  likely exchanged for SmD3-SmB with UNRIP's help.

### Decisions

- spliceosomal snRNP assembly (IBA): ACCEPT, core.
- RNA binding (IEA, Sm-domain mapping): MARK_AS_OVER_ANNOTATED; Sm fold used for protein
  contacts, GEMIN5 is the RNA-binding subunit.
- cytoplasm: ACCEPT; nucleoplasm and gems: KEEP_AS_NON_CORE.
- SMN-Sm protein complex (IEA): ACCEPT.
- Sm-like protein family complex (IBA): MODIFY to SMN complex / SMN-Sm protein complex
  (grouping term too general; node placement fine).
- NEW: SMN complex GO:0032797 (part_of), ISS from human GEMIN7.
- No new process terms added.

### Relative

Closest characterised relative: human GEMIN7 Q9H840 (PTHR14679:SF1, PAINT node PTN001027441
donor). No genes/human/GEMIN7 review exists. The donkey ortholog (genes/EQUAS/GEMIN7) is the
campaign partner and was not used. Module: modules/dmel_smn_complex.yaml (Drosophila SMN
complex) is the only related module.
