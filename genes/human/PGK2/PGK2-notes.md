# PGK2 notes

## 2026-11-24

- Seed/family: PGK2 is UniProtKB:P07205, HGNC:8898, in PANTHER `PTHR11406:SF10`.
  The two human members are `PGK1` (`P00558`, already reviewed) and `PGK2`.
- Core function: PGK2 retains the canonical phosphoglycerate kinase activity
  (`GO:0004618`, EC 2.7.2.3) and acts in glycolysis in late spermatogenic cells
  and sperm. UniProt's catalytic-activity block asserts the reversible
  `(2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP`
  reaction, while the PGK2-specific human paper reports that PGK2 is enriched in
  round spermatids and that sperm PGK2 abundance tracks motility
  [PMID:26677959].
- PAINT: the six family-root IBD rows at `PTN000150497` are sound for catalytic
  activity, ATP binding, ADP binding, glycolysis and cytosol, except for
  gluconeogenesis descending to PGK2. The `GO:0006094` row is appropriate for
  PGK1-like PGKs but over-propagates to the testis/sperm PGK2 clade; the
  existing PGK2-clade fibrous-sheath IBD at `PTN001685897` anchors the same
  eutherian PGK2 branch.
- GOA row calls: `GO:0004618`, `GO:0005524`, `GO:0043531`, `GO:0006096`,
  `GO:0005829` and `GO:0035686` are retained. `GO:0005929` is a generic
  Ensembl transfer from the same mouse PGK2 evidence and should be narrowed to
  sperm fibrous sheath. `GO:0005737` cytoplasm is true but too general.
  `GO:0006094` gluconeogenesis and `GO:0016310` phosphorylation are
  over-annotations of the sperm PGK2 role. The nine `GO:0005515` AP-MS/IPI rows
  are bare protein-binding rows from BioPlex/OpenCell-style high-throughput
  screens and are `REMOVE` by the bare protein-binding policy.
- Module/GO-CAM: `modules/glycolysis_payoff_phase.yaml` already models the PGK
  step with a PTHR11406 family selector and a "PGK1/PGK2" label, so the update
  only needs to add PGK2 as a second representative. `gocams/index.tsv` has no
  human PGK2 activity; human PGK1 is covered in `gomodel:684b6c8100001669`, and
  the PGK2 hits in `gocams/663d668500002302` are fission-yeast canonical
  glycolysis with PGK2 only in PAINT with/from lists.
