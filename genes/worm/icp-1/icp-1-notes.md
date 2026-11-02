# icp-1 review notes

## 2026-10-28 initial review

- Fetched with `just fetch-gene worm icp-1`; UniProt G5EE37 confirmed (unreviewed TrEMBL,
  622 aa, INCENP_ARK-bind domain at 530-587). 23 GOA rows.
- Also cached PMID:11050385 (Kaitna et al. 2000, the paper that identified ICP-1); only the
  abstract is available, but it is not cited by any GOA row.
- Full text read: PMID:12707312 (Romano 2003, CSC-1), PMID:11402065 (Oegema 2001),
  PMID:15548597 (Bishop 2005, BMK-1). Abstract-only: PMID:15331665, PMID:15916946,
  PMID:11050385; PMID:14704431 (Y2H interactome) has the abstract only.
- See `icp-1-deep-research-manual.md` for the sourced literature summary.

Key decisions:

- Core: CPC scaffold subunit (GO:0032133) that binds and activates AIR-2
  (GO:0043539) [PMID:12707312 "ICP-1 dramatically stimulates AIR-2 kinase activity."].
- GO:0090307 mitotic spindle assembly (IMP, PMID:11402065) -> MODIFY to
  GO:0051256 mitotic spindle midzone assembly: the same paper says spindle assembly is normal
  until mid-anaphase and the midzone is what is missing.
- GO:0007079 mitotic chromosome movement towards spindle pole -> MODIFY to GO:0000070
  mitotic sister chromatid segregation. Anaphase A is minor in the C. elegans zygote
  [PMID:11402065 "chromosomes do not move significantly polewards during anaphase"], and the
  RNAi phenotype is a segregation (lagging chromatin) defect, not a poleward-movement defect.
- ComplexPortal NAS rows for positive regulation of the SAC and of sister chromatid
  separation: no worm evidence in the cited paper; depleted embryos still separate paternal
  sister chromatids. MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding (AIR-2) -> REMOVE under the protein-binding policy; the
  informative content is captured by the kinase activator rows.
- Kinetochore IDA (PMID:15331665) UNDECIDED: abstract-only, and the full-text data from
  PMID:11402065 place ICP-1 between the kinetochore plates (inner-centromere-like) rather than
  on them.
- No NEW rows: all processes with solid evidence are already in GOA or covered by MODIFY
  replacements.
