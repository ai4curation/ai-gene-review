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
- Replaced the obsolete/generic chaperone terms GO:0044183 and GO:0051082 with
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
