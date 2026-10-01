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
  tightened to `GO:0004197`, while `GO:0097194 execution phase of apoptosis` and
  `GO:1900119 positive regulation of execution phase of apoptosis` were replaced
  by `GO:0051604 protein maturation` because Casp8 is an initiator that matures
  effector substrates rather than an executioner-caspase participant.
- Generic `GO:0005515 protein binding` rows were removed unless the local cache
  could not expose the exact interactor. `PMID:11684016`, `PMID:21382479`,
  `PMID:24113711`, `PMID:24557836`, and `PMID:26649818` are still
  `UNDECIDED` pending full-text checks.
