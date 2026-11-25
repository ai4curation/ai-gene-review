# Tardbp (rat) review notes

## 2026-10-28 session

- Fetched with `just fetch-gene rat Tardbp`; UniProt A0A8I6GLU8 confirmed (RGD:1310906,
  GeneID 298648); GOA file has 65 rows, all keyed to A0A8I6GLU8.
- No deep-research provider; literature work is in `Tardbp-deep-research-manual.md`.
- Rat experimental rows:
  - RNA binding IDA [PMID:21051541] - RIP-seq in rat cortical neurons; binding in introns and
    3'-UTRs. Refined to pre-mRNA intronic binding + mRNA 3'-UTR binding.
  - Perichromatin fibrils / nuclear speck / interchromatin granule IDA [PMID:19539030] -
    abstract only; perichromatin fibrils is the strong site, speckle labelling is "weak".
  - Positive regulation of insulin secretion IMP [PMID:21127054] - full text is about
    PI3K-C2alpha only, TDP-43 never mentioned. Removed; source defect (wrong gene product) for RGD.
  - Response to ER stress IEP [PMID:21608013] - misfolding by amino-acid analogues raises TDP-43
    levels; ER not examined. Modified to response to misfolded protein; WRONG_TERM defect.
- Mouse UniProt IDA (PMID:28585542) for positive regulation of protein import into nucleus: the
  paper shows CHCHD10 retains TDP-43 in the nucleus, so TDP-43 is the cargo. Rat ISO/IEA rows
  removed; defect recorded for UniProt.
  - Correction on re-review: the mouse row has `has_input` Chchd10, and the same paper reports that
    "TDP-43 promoted the nuclear localization of CHCHD10 in a retrograde signalling manner"
    (three-fold more nuclear CHCHD10 on TDP-43 overexpression). TDP-43 is the regulator in that
    experiment, so the source row is sound. Defect withdrawn; rat ISO/IEA rows now KEEP_AS_NON_CORE.
- Mouse MGI IDA (PMID:18836447) for RNA pol II cis-regulatory sequence-specific DNA binding: the
  cached full text does not name TDP-43 (likely in a supplementary SBE2 pull-down list). Kept as
  non-core because human TDP-43 binding of promoter TAR DNA is independently documented.
- Core functions: intronic pre-mRNA binding driving regulation of alternative splicing (incl.
  cryptic exon repression); 3'-UTR binding driving mRNA destabilisation (autoregulation);
  condensate scaffolding by the CTD.

## Source-defect re-review (2026-11-10)

An independent re-review of this gene's wrong-gene / wrong-reference source defects changed the following; where earlier notes above say otherwise, this section supersedes them.

- GO:0042307 / GO_REF:0000107: defect withdrawn (evidence depth: FULL_TEXT). The mouse source row (Q921F2 IDA, PMID:28585542) carries has_input Chchd10, and the cached full text states "TDP-43 promoted the nuclear localization of CHCHD10" (three-fold more nuclear CHCHD10 on TDP-43 overexpression). TDP-43 is the regulator and CHCHD10 the cargo, exactly as annotated; the claimed cargo/regulator conflation was wrong. Defect deleted, action/summary/reason rewritten, and the contradicting reference_review note, notes.md line and deep-research-manual line corrected.
- GO:0042307 / GO_REF:0000121: defect withdrawn (evidence depth: FULL_TEXT). Same source row as the IEA entry; defect alias removed, action changed to KEEP_AS_NON_CORE and propagation_review changed from SOURCE_BAD/ROLE_CONFLATION to NO_FAILURE_NON_CORE/SUPPORTS_TRANSFER.
