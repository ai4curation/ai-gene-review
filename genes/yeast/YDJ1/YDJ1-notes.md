# YDJ1 review notes

## 2026-08-28 completion audit

- YDJ1 encodes a type-I DnaJ/Hsp40 co-chaperone whose defining molecular
  function is stimulation of the Ssa1 Hsp70 ATPase cycle [PMID:1400408, “We
  report that a purified cytoplasmic Hsp70 homolog from Saccharomyces cerevisiae,
  Hsp70SSA1, exhibits a weak ATPase activity, which is stimulated by a purified
  eukaryotic dnaJp homolog (YDJ1p).”]. The InterPro-derived ATP
  binding annotation is therefore removed: Ydj1 activates its Hsp70 partner but
  has no ATP-binding/ATPase domain of its own.

- All 49 unique nonredundant GOA signatures were reconciled exactly by GO term,
  evidence, reference, and relation qualifier. The 62 physical GOA rows collapse
  to 49 signatures because high-throughput `protein binding` annotations repeat
  the same assertions for multiple WITH/FROM partners. All eight generic protein
  binding signatures remain marked over-annotated; specific Hsp70/heat-shock
  protein binding terms capture the informative partner biology.

- All six IBA annotations were reviewed from their exact GOA WITH/FROM
  provenance. Cytosol, cellular response to heat, protein refolding, and
  obsolete unfolded protein binding use PTN001531327; ATPase activator activity
  uses PTN002376157; nucleus uses PTN001180221. YDJ1 is an experimental
  descendant source at PTN001531327 and PTN002376157, which is valid PAINT
  grounding rather than circular evidence. The SGD:S000005021 source on the
  unfolded-protein-binding and nucleus rows is APJ1, a class-A/type-I Ydj1
  paralog, not SIS1. YDJ1 belongs to PTHR43888, not PTHR44298. After fetching
  the correct family through the repository wrappers, the current PAINT table
  retains PTN001531327, PTN001180221, and PTN002376157. Their current node-level
  terms and seeds support five IBA transfers; PTN001531327 no longer carries
  obsolete GO:0051082. Direct YDJ1 evidence independently supports the core
  biological decisions.

- GO:0051082 is obsolete in live GO, whose official obsoletion comment gives
  GO:0044183 protein folding chaperone and GO:0140309 unfolded protein holdase
  activity as evidence-dependent consider terms
  [AmiGO GO:0051082, accessed 2026-08-28](https://amigo.geneontology.org/amigo/term/GO%3A0051082).
  Ydj1 directly supports both:
  it suppressed thermally induced luciferase aggregation and, paired with Ssa1,
  promoted productive refolding [PMID:9774392, “Ydj1:Ssa1 could promote up to
  four times more luciferase folding than Sis1:Ssa1.”]. All three GO:0051082
  assertions are therefore modified to both evidence-matched successor
  activities, and both activities are represented in the core-function model.

- The CAFA-assigned IDA `chaperone-mediated protein complex assembly` row has
  empty WITH/FROM and cites an abstract-only human p23 paper [PMID:10811660].
  The abstract demonstrates p23 chaperoning of progesterone receptor but no
  direct YDJ1 assay, so the row is marked over-annotated rather than treated as
  MOD-curated evidence or labelled a wrong-identifier citation.

- Ydj1's heat-stress quality-control role is directly supported in full text
  [PMID:25344756, “We found that ubiquitylation of heat-induced substrates
  requires the Hsp40 co-chaperone Ydj1 that is further associated with Rsp5 upon
  heat shock.”].
  ERAD and protein targeting to ER are retained as important cellular functions;
  HAP1 regulation, oxygen response, starvation-linked tRNA import, nuclear
  localization, and broad protein transport are retained as specialized non-core
  uses of the central Hsp70 co-chaperone machinery. TRC membership is marked
  over-annotated because upstream cascade participation does not establish stable
  incorporation into the Get4-Get5/Mdy2 complex.

- Most older supporting publications in the cache are abstract-only. Their
  experimental annotations were not overruled when the abstract lacked assay
  detail. Full text is locally available for PMID:19536198, PMID:23217712,
  PMID:25344756, PMID:25853343, PMID:26928762, and PMID:37968396.

## 2026-08-28 dedicated re-review addendum

- Recounted the current export directly: 62 physical GOA rows collapse to 49
  qualifier-aware signatures (21 IPI rows account for most of the collapse).
  Every signature is represented exactly once and has a manual action; there
  are no pending or undecided entries.
- Rechecked the obsolete-term successors against the current GO ontology and
  separated the two activities supported by PMID:9774392 instead of treating
  all unfolded-client evidence as folding alone.
- Rechecked all six IBA rows against current GOA and the correct PTHR43888
  PANTHER PAINT cache. PTN001531327, PTN001180221, and PTN002376157 are all
  present, so the biologically supported transfers retain no-failure provenance
  classifications. The obsolete GO:0051082 row remains a term-scoping issue.
- PMID:10811660 was manually classified as `MISCITED`/`NONE` for YDJ1: its
  abstract reports human p23 assays and supplies no YDJ1-specific experimental
  support for the CAFA-assigned IDA row.

## 2026-09-29 IBA project re-review

- Rechecked all six IBA rows against the PTHR43888 PAINT cache and the
  `projects/IBA_REVIEW.md` taxonomy. The review already records PTN ancestor
  nodes, not extant WITH/FROM donors, as the IBA `source_entities`; YDJ1
  self-evidence remains valid grounding of the ancestral PTN assertions rather
  than circular support. Current PAINT still supports the cytosol, ATPase
  activator, heat-response, refolding, and nucleus decisions; obsolete
  GO:0051082 remains correctly scoped to direct Ydj1 replacements rather than
  treated as a propagated active GO term.

- Migrated the eight `GO:0005515 protein binding` IPI annotations from the
  legacy `MARK_AS_OVER_ANNOTATED` action to `REMOVE`. This does not dispute the
  reported Rad3/Rad24/Ctr9, Hsp82, Sgt2/Mdy2, Sup35, Ssa1, Sse1, Tif2, and Eft2
  physical associations, but `protein binding` is a generic molecular-function
  label; the functionally established partnerships are already represented by
  Hsp70 protein binding, heat shock protein binding, ATPase activator activity,
  TRC-pathway review text, or client-folding activity as appropriate.

- Searched newer literature and cached PMID:39652584 and PMID:40383781. Omkar
  et al. (2024) directly shows that Ydj1 J-domain acetylation tunes Ssa1 and
  Hsp82 interaction, client refolding, Ssa1 ATPase stimulation, and translation
  fidelity, refining regulation of the existing Hsp40/Hsp70 co-chaperone model.
  Vestergaard et al. (2025) used YDJ1 and SSA1 overexpression to improve
  heterologous aspulvinone E production; that supports the breadth of Ydj1's
  client-folding utility but is a cell-factory application and not evidence for
  a new endogenous GO term.

## 2026-10-01 live-GOA refresh

- Refreshed YDJ1 against current GOA. The live export now has 41 physical rows
  rather than the old 62-row export, and the review keeps 12 exact stale rows as
  `retired: true`: the obsolete `GO:0051082 unfolded protein binding` IBA, IEA,
  and IDA assertions; the former UniProt keyword rows for `GO:0008270 zinc ion
  binding`, `GO:0015031 protein transport`, and `GO:0046872 metal ion binding`;
  and six no-longer-live IntAct `GO:0005515 protein binding` rows. The zinc
  function itself is still live through the SGD RCA row, and ER plus
  mitochondrial targeting are now represented more specifically than the old
  broad `protein transport` keyword transfer.
- Rechecked the PTHR43888 PAINT table. Current PAINT agrees with current GOA:
  YDJ1 has five live IBA rows, for cytosol, ATPase activator activity, cellular
  response to heat, protein refolding, and nucleus. The stale
  `GO:0051082`/PTN001531327 row is gone from both live GOA and the local PAINT
  export; its direct experimental support remains valid evidence for the
  `GO:0044183 protein folding chaperone` and `GO:0140309 unfolded protein
  holdase activity` core functions.
- Resolved four newly seeded current-GOA rows. The second Liou et al. 2007
  `GO:0005515 protein binding` IPI edge from PMID:17441508 was removed for the
  same reason as the existing Sgt2 row: the Mdy2/Sgt2/Ydj1 relationship is real,
  but generic protein binding is not an informative molecular function. The new
  `GO:0017053 transcription repressor complex` NAS row was kept as a non-core
  ComplexPortal HAP1/Ssa/Ydj1/Sro9 complex assertion. The ARBA and IMP
  `GO:0070585 protein localization to mitochondrion` rows were accepted because
  the original MAS5/YDJ1 paper directly reported mitochondrial protein import
  defects [PMID:1729605, "The deletion mutant also displayed a modest import
  defect at 23 degrees C and a substantial import defect at 37 degrees C."].
- Searched 2025-2026 literature and found no new primary yeast YDJ1 paper that
  changes the curated core Hsp40/Hsp70 co-chaperone model. The 2025 yeast hits
  were either the already cached heterologous small-molecule production study
  (PMID:40383781), a prion-client in vitro application, or a Cdc42 preprint.

The refreshed review has 53 total rows: 41 current GOA rows and 12 retired
historical rows. Final action counts are 27 ACCEPT, 10 KEEP_AS_NON_CORE, 10
REMOVE, 4 MODIFY, and 2 MARK_AS_OVER_ANNOTATED.
