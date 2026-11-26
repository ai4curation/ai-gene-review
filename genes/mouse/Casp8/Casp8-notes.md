# Casp8 notes

## 2026-10-01

Falcon deep research could not run because no deep-research provider was
configured in the local environment. I reviewed the new GOA seed manually using
the cached literature, UniProt, the existing human CASP8 review, and the
annotation-reviewer sidecar for a systematic pass over mouse-specific GO rows.

### Manual evidence trail

- `PMID:9837723` supports the basic mouse cysteine-aspartyl protease activity:
  recombinant murine caspase-8 processes murine procaspases, including
  procaspases-3, -6, -7, and -8.
- `PMID:9654089`, `PMID:9729047`, `PMID:12404118`, and `PMID:15322156`
  establish that mouse Casp8 is essential for death-receptor-induced apoptosis
  and for several in vivo endothelial, yolk-sac, hematopoietic, macrophage,
  neural-tube, and heart contexts.
- `PMID:21368763`, `PMID:22037414`, `PMID:22089168`, `PMID:22675671`,
  `PMID:31511692`, `PMID:31748744`, and `PMID:31827281` collectively support the
  anti-necroptotic checkpoint: catalytically active FADD/Casp8/cFLIP complexes
  restrain RIPK1/RIPK3/MLKL signaling, with CYLD and RIPK1 as important
  Casp8-cleaved substrates.
- `PMID:21737330` supports the human ripoptosome comparator used for inherited
  mouse `GO:0097342 ripoptosome` rows: the complex contains RIP1, FADD,
  caspase-8, caspase-10, and cFLIP isoforms.
- `PMID:30361383` supports direct gasdermin D cleavage by mouse and human
  caspase-8 downstream of TAK1 blockade, and `PMID:32971525` supports N4BP1
  cleavage as a direct innate-immune / cytokine-production branch.

### Curation notes

- The inherited and automated exact `GO:0006915 apoptotic process` rows were
  narrowed to `GO:0008625 extrinsic apoptotic signaling pathway via death domain
  receptors`.
- The direct `PMID:16183742` PIDD rows were marked over-annotated rather than
  narrowed to death-receptor apoptosis: the paper explicitly reports that
  PIDD-expressing MEFs did not show detectable procaspase-8 or procaspase-9
  processing.
- Cysteine endopeptidase, DISC/CD95-DISC, cytosol, death-receptor, ripoptosome,
  and negative-necroptosis rows were retained. Generic peptidase rows were
  tightened to `GO:0004197`, `GO:0097194 execution phase of apoptosis` rows were
  narrowed to `GO:1900119 positive regulation of execution phase of apoptosis`,
  and existing `GO:1900119` rows were retained because Casp8 directly activates
  effector caspases but is not itself an executioner-caspase participant.
- Generic `GO:0005515 protein binding` rows were removed unless the local cache
  could not expose the exact interactor. `PMID:11684016`, `PMID:21382479`,
  `PMID:24113711`, `PMID:24557836`, and `PMID:26649818` are still
  `UNDECIDED` pending full-text checks.

## 2026-10-12 Ortholog/family consistency audit

- GOA refresh (`just fetch-gene mouse Casp8`): no new annotations; all 182
  unique GOA term/reference rows are covered and no stale rows remain.
- PANTHER: Casp8 is in PTHR48169 (DED domain-containing protein; subfamily
  SF7) [file:mouse/Casp8/Casp8-uniprot.txt "PTHR48169; DED DOMAIN-CONTAINING PROTEIN"],
  shared with human CASP8; Casp9 and Casp3 are in PTHR47901 / PTHR10454 respectively,
  so only the caspase-wide IBA rows (cysteine-type endopeptidase activity,
  cytoplasm, apoptotic process, positive regulation of neuron apoptotic process)
  are directly comparable across the family.
- Compared against `genes/human/CASP8` (DRAFT), `genes/mouse/Casp3`,
  `genes/mouse/Casp9`, `genes/human/CASP9`, `genes/DROME/Dronc`, `genes/worm/ced-3`.
- Resolved mouse/human disagreements by aligning mouse to the human CASP8
  treatment (48 rows changed, each `review.reason` prefixed "Ortholog audit 2026-10-12"):
  - `GO:0097191` extrinsic apoptotic signaling (all rows), `GO:0036462` TRAIL
    pathway, `GO:0016485` protein processing, `GO:0097110` scaffold protein
    binding -> ACCEPT. The previous MODIFY (narrowing to GO:0008625) was dropped
    because it would exclude the non-receptor activation platforms, matching
    human CASP8.
  - `GO:0006915` apoptotic process, `GO:0097190` apoptotic signaling pathway and
    `GO:0006508` proteolysis: not narrowed to GO:0008625 (which would lose the
    non-receptor platforms) but, after PR #5079 review, kept as KEEP_AS_NON_CORE
    rather than ACCEPT. These are true but broad parents strictly entailed by the
    accepted GO:0097191/GO:0008625/GO:0016485 rows, so they are correct-but-not-core.
    (Casp9/CASP9 MODIFY their apoptotic rows to intrinsic signaling; Casp9 is
    essentially restricted to the apoptosome pathway, so the difference is
    biological, not inconsistent.)
  - `GO:0097194` execution phase (MODIFY -> KEEP_AS_NON_CORE; experimental rows no
    longer recast), `GO:0043065`, `GO:0042981`, `GO:0045862`, plasma membrane IEA,
    `GO:0042802` identical protein binding (ACCEPT -> non-core, binding term),
    `GO:0044877` (REMOVE -> non-core), and the ARBA developmental/immune parents
    (`GO:0048513`, `GO:0043009`, `GO:0030154`, `GO:0009967`, `GO:0002682`;
    over-annotated -> non-core, given Casp8-null midgestation lethality through
    unrestrained necroptosis) -> KEEP_AS_NON_CORE.
  - `GO:0030690` Noc1p-Noc2p complex IMP (PMID:14657025) REMOVE -> UNDECIDED: an
    experimental MGI row whose full text was not inspected (project rule), matching
    the human UNDECIDED verdict on its electronic transfer.
  - `GO:0005123` death receptor binding and `GO:0044297` cell body (rat-donor ISO)
    REMOVE -> UNDECIDED, matching human CASP8; donor assays not traced.
  - `GO:0005164` tumor necrosis factor receptor binding (rat-donor ISO, same
    RGD:620945) REMOVE -> UNDECIDED (PR #5079 review suggestion 10). TNFR1 is a
    death receptor, so this row stands or falls with GO:0005123; the audit did
    not reach it in the first pass because it has no human CASP8 counterpart to
    align against (human CASP8 carries only the GO:0005123 IEA).
- No human CASP8 edits: no donor-side row was clearly wrong.
- PR #5079 review follow-up: after demoting GO:0006915 apoptotic process,
  GO:0097190 apoptotic signaling pathway and GO:0006508 proteolysis to
  KEEP_AS_NON_CORE (strictly-entailed broad parents of accepted descendants),
  these three parents now *intentionally* differ from human CASP8, which still
  has them ACCEPT. This is a new, deliberate mouse/human divergence: human CASP8
  is DRAFT and should be demoted the same way when it leaves DRAFT.
