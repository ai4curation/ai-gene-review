# PMM1 notes

## 2026-11-24

Seed/family context:

- PMM1 is the only human reviewed PTHR10466 member on `origin/main` without a
  gene review. PMM2 is already reviewed, and
  `interpro/panther/PTHR10466/PTHR10466-review.yaml` already covers the
  eukaryotic PMM family and the PMM1/PMM2 vertebrate split.
- `just paint-losses human PMM1` reports no IRD or IKR loss on the Q92871
  lineage. PMM1 therefore inherits the PTN000049281 phosphomannomutase,
  mannose-metabolism, cytosol, and N-linked-glycosylation IBD rows without a
  PAINT loss exception.
- A Falcon deep-research run was attempted with `just deep-research human PMM1
  --provider falcon`, but this checkout's provider registry exposed only
  `claude_code`. No `PMM1-deep-research-*` provider file was written; this notes
  file records the manual source review instead.

Core sources:

- `PMM1-uniprot.txt` has direct UniProt curation for the EC 5.4.2.8 reaction,
  the Mg(2+) cofactor, the GDP-alpha-D-mannose pathway step, homodimerization,
  RAB6A/RAB6B IntAct interactions, and a mouse-orthology cytoplasm statement.
- PMID:9070917 cloned human PMM1 from liver cDNA, showed that expression in
  `Escherichia coli` yields active phosphomannomutase, and noted expression in
  liver, heart, brain, pancreas, and skeletal muscle.
- PMID:16540464 solved PMM1 structures with magnesium and
  alpha-D-mannose 1-phosphate, mapped the conserved active site, and reported
  similar kinetic properties for alpha-PMM1 and alpha-PMM2.
- Reactome R-HSA-446201 directly states that cytosolic PMM1 and PMM2 catalyse
  Man6P to Man1P, and R-HSA-446205 places that reaction in synthesis of
  GDP-mannose.

Annotation decisions:

- `GO:0004615` phosphomannomutase activity: ACCEPT across EXP, IDA, IBA, IEA,
  and TAS. The experimental PMID:16540464 and PMID:9070917 rows establish the
  activity, while the PAINT and IEA rows agree with the curated EC/Rhea mapping.
- `GO:0009298` GDP-mannose biosynthetic process: ACCEPT. PMM1 catalyses the
  Man6P to Man1P mutase step, which feeds GDP-mannose biosynthesis in Reactome
  and UniPathway.
- `GO:0006013` mannose metabolic process: ACCEPT. It is the parent process for
  the mannose-phosphate mutase reaction and is kept consistently with PMM2 and
  the existing PTHR10466 review.
- `GO:0006487` protein N-linked glycosylation: KEEP_AS_NON_CORE. PMM1 acts
  upstream by supplying mannose 1-phosphate for GDP-mannose and
  dolichol-phosphate-mannose; it does not catalyse a glycan transfer to protein.
- `GO:0005829` cytosol: ACCEPT. PAINT, HPA, and Reactome all converge on a
  soluble cytosolic PMM reaction.
- `GO:0005737` cytoplasm: TOO_GENERAL. Cytoplasm is true, but the review
  already keeps cytosol as the precise compartment.
- `GO:0043025` neuronal cell body: MARK_AS_OVER_ANNOTATED. The row is a
  cell-region-specific Ensembl orthology transfer from mouse PMM1 and adds no
  functional information beyond soluble cytosol for human PMM1.
- All four `GO:0005515` protein-binding rows are REMOVE under the generic
  protein-binding policy. The action does not dispute the reported RAB6A/RAB6B
  high-throughput interactions; it removes only the bare, uninformative GO
  molecular-function annotation.
