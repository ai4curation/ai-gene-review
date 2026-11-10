# Lam (P08928) review notes

## Session 1 (2026-10-28)

- `just fetch-gene DROME Lam` timed out twice against rest.uniprot.org, then succeeded;
  UniProt P08928 (LMNB_DROME) confirmed, 89 GOA rows. The PANTHER family fetch (PTHR45721)
  returned an InterPro 500 error; no family file was written.
- No deep-research API keys; literature synthesis written by hand in
  `Lam-deep-research-manual.md` from the 35 cached papers (10 with full text, the rest
  abstract-only).
- PMID:19273613 (Megator spindle matrix) was read: it is not cited in GOA for Lam, and its
  only Lam content is that lamin B persists around the S2-cell spindle ["In this study, we
  used immunofluorescence to show that lamin B is not fully disintegrated at this stage"].
  It corroborates the spindle-envelope localization (spindle pole row), nothing more.

### Decisions

- MF `GO:0005200 structural constituent of cytoskeleton` (IBA, IEA, IMP) -> MODIFY to
  `GO:0160123 structural constituent of nuclear lamina`, the dedicated term for a lamin.
- `nucleus` and `nuclear envelope` rows -> MODIFY to `nuclear lamina` (correct but general;
  nuclear lamina is part_of both, and the gene already carries it many times over).
- `nuclear envelope lumen` (IDA PMID:2517292, abstract only): lamins line the nucleoplasmic
  face of the inner nuclear membrane, so lumen looks like a term-selection error; I cannot
  see the immuno-EM in the full text, so UNDECIDED with a PROBABLE WRONG_TERM source defect.
- `heterochromatin formation` IDA PMID:20702563: the abstract is about Lamin C tethering,
  full text not retrievable (PMC record returned no body) -> ACCEPT, deferring to the FlyBase
  curator, because the claim is independently supported (PMID:19218438, PMID:25754639, PMID:25417159)
  and keeps the term's rows consistent.
- `signaling receptor binding` (IPI with LBR) -> REMOVE: LBR is an inner nuclear membrane
  protein, not a signaling receptor; the binding itself is real. Bare protein-binding rows
  (Wash, Otefin, YA) -> REMOVE under the protein-binding policy.
- Developmental phenotype rows (eye, gonad, CNS, gut, cuticle, trachea, D/V, spermatogenesis)
  -> KEEP_AS_NON_CORE; ARBA broad morphogenesis terms -> TOO_GENERAL.
- `negative regulation of cell population proliferation` (acts upstream, fat body lamin loss
  -> gut hyperplasia via secreted PGRPs) -> MARK_AS_OVER_ANNOTATED (non-cell-autonomous,
  several steps removed).
- No NEW rows. Histone H2A/H2B binding (PMID:10077600) was considered and rejected: the
  evidence is competition of tail-chromosome binding, which chromatin binding already covers.

### Process note

- The review stub was regenerated offline with `ai-gene-review seed-goa` from `Lam-goa.tsv`
  after a scratch copy was clobbered (shared scratch directory); a re-run of fetch-gene timed
  out against UniProt. Row order was checked against the original seed before reviews were
  applied. `just validate DROME Lam` passes with no content warnings.
