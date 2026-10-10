# SSA2 review notes

## Identity and core function

- SSA2 is P10592/YLL024C, a constitutively expressed cytosolic Ssa-family Hsp70.
- The best molecular-function summary is GO:0140662, ATP-dependent protein folding
  chaperone. Ssa-class Hsp70s cooperate with Ydj1 to suppress aggregation and use ATP,
  and Ssa1/2 depletion strongly impairs luciferase refolding
  [PMID:7867784; PMID:8947547].
- In-vivo reporter and nascent-enzyme experiments support protein folding/refolding as
  the central biological role [PMID:9448096; PMID:9789005].

## Annotation decisions

- All 57 logical review records reconcile against the 278 pinned GOA provenance rows;
  no PENDING or UNDECIDED actions remain. The review is therefore marked COMPLETE.
- Replaced the generic GO:0044183 and obsolete GO:0051082 chaperone terms with
  GO:0140662 where the evidence supports ATP-dependent folding chaperone activity.
- Replaced GO:0006616 with GO:0031204. The experimental evidence concerns an Ssa/Ydj1
  contribution to post-translational translocation of a subset of ER precursors, not
  SRP-dependent cotranslational targeting [PMID:8754838; PMID:8947547]. GO:0031204 is
  retained instead of its broader parent GO:0006620 because PMID:8754838 reports an
  in-vivo translocation block; the negative PMID:8947547 cell-free result is recorded
  as assay-context counterevidence and keeps this role non-core.
- Retained nucleus, vacuolar membrane, cell wall, mitochondrion, and the experimental
  plasma-membrane HDA as non-core localizations. The cell-wall and vacuolar-membrane
  evidence is directly supported [PMID:8755907; PMID:10745074]; the plasma-membrane
  cache is abstract-only and does not name SSA2 [PMID:16622836]. The separate pinned
  plasma-membrane IBA is removed because current PTHR19375 data contain no GO:0005886
  assertion at its cited PTN002500132 node
  [file:interpro/panther/PTHR19375/PTHR19375-paint.tsv].
- Marked generic nucleotide binding as over-annotated because ATP binding/hydrolysis and
  ATP-dependent chaperone activity are already represented more informatively.
- Removed the remaining bare `GO:0005515 protein binding` rows from generic
  high-throughput or prediction-backed interaction records, and retained the two
  Hsp70/Hsp90 co-chaperone rows as `MODIFY` to `GO:0031072 heat shock protein
  binding`.
- Kept broad nuclear import as non-core because its direct support is the specialized
  tRNA-import pathway rather than the central folding/refolding mechanism.

## Citation adjudication

- PMID:12761219 begins from *Candida albicans* Ssa1/2 but directly assays isogenic
  *S. cerevisiae* SSA1/SSA2 mutants. Reduced histatin-5 killing of the delta-ssa2
  single mutant and the stronger double-mutant phenotype support a specialized
  Ssa2 cell-envelope receptor role [PMID:12761219].

## Project relevance

- SSA2 is directly relevant to `UNFOLDED_PROTEIN_BINDING`; its row now points to
  GO:0140662 and describes its constitutive cytosolic Hsp70 role.
- No curated module membership was found for SSA2/YLL024C/P10592.

## 2026-09-29 IBA follow-up

- Rechecked all eight GO_REF:0000033 IBA rows against
  `interpro/panther/PTHR19375/PTHR19375-paint.tsv`. The nucleus, cytoplasm,
  cytosol, ATPase, heat-shock-protein-binding, and protein-folding chaperone
  transfers all still trace to current PAINT rows. The pinned plasma-membrane
  IBA remains stale because current PTN002500132 carries only `GO:0005634
  nucleus` and `GO:0005829 cytosol`.
- Retained `GO:0042026 protein refolding` as a core Ssa2 activity because
  Ssa1/2 refolding is directly supported by PMID:8947547, but marked the 2022
  IBA row itself as stale: current PAINT carries a 2026 fungal PTN001065099
  NOT/IRD for `GO:0042026` with `GO:0006457 protein folding` retained at the
  same node.
- Recorded the probable GOA lag in the other direction: PTN001065100 now
  carries a Saccharomycetaceae `GO:0006616 SRP-dependent cotranslational
  protein targeting to membrane` IBD seeded by SSA2 itself, but the pinned SSA2
  GOA snapshot has no matching `GO:0006616` IBA row.
- Added `propagation_review.source_entities` to the accepted IBA rows that were
  missing source traces, and expanded the PTN-only Hsp70-family molecular
  function blocks with representative current donors.
- Searched PubMed for exact `SSA2`/`Ssa2`/`YLL024C` mentions in 2025-2026. The
  only exact 2026 hit was PMID:41699988, an adaptive-evolution study of
  trehalose accumulation and freeze-thaw tolerance that does not alter the
  cytosolic Hsp70 curation decisions.

## Focused hypothesis research

- OpenScientist independently supported `KEEP_AS_NON_CORE` for GO:0005886, emphasizing
  that PMID:16622836 used a stripped plasma-membrane fraction and does not establish a
  primary membrane-resident function.
- Its live QuickGO query reported only the HDA row and asserted that no IBA exists. This
  conflicts with the pinned `SSA2-goa.tsv`, which contains both an IBA/GO_REF:0000033 row
  (dated 2025-09-03) and an HDA/PMID:16622836 row. Its use of the histatin paper is
  valid because the paper directly assays *S. cerevisiae* SSA mutants. The provider
  report remains `DISPUTED` only for the incorrect live-database claim; its conservative
  localization judgment is retained.

## 2026-10-01 current-GOA reconciliation

- Force-refreshed SSA2 from the current GOA feed and reconciled the review to 61 live
  source rows. The refresh added 17 rows: 15 newly split current IntAct
  `GO:0005515 protein binding` assertions from PMID:16429126, PMID:17892321, and
  PMID:37968396; a live InterPro `GO:0005524 ATP binding` row; and the
  ComplexPortal `GO:0017053 transcription repressor complex` row from PMID:15102838.
- Preserved the 12 older source assertions that are absent from current GOA as
  `retired: true` rows. These cover the stale plasma-membrane IBA, older
  GO_REF:0000043/GO_REF:0000117/GO_REF:0000120 automatic rows, five no-longer-live
  unsourced IntAct `protein binding` rows, and two retired GO:0051082 experimental/ISS
  rows.
- Rechecked the eight baseline PTHR19375 IBA rows against the current PAINT table.
  The accepted/non-core nucleus, cytoplasm, cytosol, ATPase, heat-shock-protein-binding,
  and protein-folding-chaperone rows still trace to current PTHR19375 assertions; the
  old plasma-membrane IBA remains stale at PTN002500132; and the GO:0042026
  `protein refolding` row remains a stale 2022 inheritance beside the 2026 fungal
  PTN001065099 NOT/IRD override.
- Read the newer cached primary paper PMID:40202836. It shows that the constitutive
  Ssa1/Ssa2 pair limits aggregation of the endogenous Pab1 stress-granule protein, but
  it does not require a new GO assertion beyond the existing Ssa2 folding/refolding and
  proteostasis curation.
