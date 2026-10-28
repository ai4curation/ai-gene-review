# Vegfa (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Vegfa` resolved UniProt P16612 (VEGFA_RAT, RGD:619991, GeneID 83785);
  GOA file keyed to P16612, 265 rows. 31 PMIDs cached by `fetch-gene-pmids`; PMID:20097747
  cached and read (full text).
- No deep-research provider available; literature synthesis is in
  `Vegfa-deep-research-manual.md`. Most cached rat papers are abstract-only; full text was
  available for PMID:12181492, PMID:19012730, PMID:23887904 and PMID:20097747.
- The human VEGFA review (`genes/human/VEGFA/`) was used for comparison of ISO-donor rows.

## Key judgements

- Core: extracellular VEGFR1/VEGFR2/NRP1 ligand with growth-factor, chemoattractant and
  heparin/ECM-binding activities; drives angiogenesis, endothelial proliferation and
  migration and vascular permeability [PMID:7929439 "binds to two structurally related
  tyrosine kinase receptors denoted Flt1 and KDR"; PMID:16230500; PMID:16793871].
- GO:0007200 (PLC-activating GPCR signalling) is a wrong term: the human source
  (PMID:18059339) describes VEGFR2/PKC signalling; VEGF receptors are RTKs. Removed and
  recorded as a source defect.
- GO:1905604 (negative regulation of BBB permeability) contradicts the human source
  (PMID:19148554 "VEGF ... increased endothelial cell permeability in vitro"); removed with
  a source defect (likely belongs to ANGPT1 or should be the positive term GO:1905605).
- GO:0051402 neuron apoptotic process (IMP, PMID:17591953) should be negative regulation
  (GO:0043524): "VEGF-A exposure resulted in a dose-dependent reduction in retinal neuron
  apoptosis".
- GO:0070482 response to oxygen levels (IEP, PMID:15885787): the cached abstract describes
  human pterygium tissue only; UNDECIDED with a CHECK source defect.
- NOT rows (RGC axon guidance, commissural axon guidance, axon extension) come from the
  mouse short isoform (PR:Q00731-3) and coexist with positive rows from PR:Q00731-2; kept
  with a consistency_exception. The rat rows lost the isoform context.
- Transcription/gene-expression/mRNA-stabilisation rows: distal signalling outputs of a
  secreted ligand; marked over-annotated.
- Human L-VEGF/N-VEGF (CUG-initiated) explains nucleus/cytoplasm/ER/Golgi ISO rows; whether
  rat uses the same upstream CUG start is not represented in P16612 (suggested question).

## Curation gaps (not knowledge gaps)

- No GO term for VEGF's role as VEGFR2 ligand beyond binding/growth factor activity; the
  existing GO:0030297 (transmembrane receptor protein tyrosine kinase activator activity)
  is used as the most specific activity term.
