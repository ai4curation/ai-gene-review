# xcpX (PA3097, Q00518) review notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE xcpX`; accession Q00518 matches the worklist (rank 15,
PA3097). No deep-research provider was used; these are manual notes from the cached
publications and the UniProt record.

### What XcpX is

- XcpX is the GspK-family minor pseudopilin of the Xcp type II secretion system (T2SS).
  UniProt: "Belongs to the GSP K family"; Pfam PF03934 (T2SSK), NCBIfam NF037980 (T2SS_GspK),
  PANTHER PTHR38831.
- It is a bitopic inner-membrane protein processed by the prepilin peptidase PilD/XcpA
  [PMID:9466253 "we characterized the xcpX gene product, a bitopic cytoplasmic membrane protein";
  "We show that XcpX could be processed by the prepilin peptidase, PilD/XcpA, and that the highly
  conserved glycine residue preceding the hydrophobic segment could not be mutated without loss of
  the XcpX function"]. UniProt: TRANSMEM 8..29, periplasmic domain 30..333.
- XcpX controls the length of the XcpT pseudopilus and binds XcpT directly
  [PMID:16012171 "when the number of XcpX subunits increases, the length of the pseudopilus
  decreases. Conversely, in the absence of XcpX, the pseudopilus length is abnormally long";
  "Our results indicate that XcpT and XcpX directly interact with each other"].
- XcpX forms the tip complex with XcpU, XcpV and XcpW [PMID:19828448 "We found an XcpV(I)-W(J)-X(K)
  complex, which demonstrates that the crystallized trimeric complex also exists in the P.
  aeruginosa T2SS"]. Crystal structure of XcpVWX (Zhang et al. 2018) places XcpX on top of the
  tip complex [PMID:30346996 "XcpX is on the top (Fig 2B, in yellow) of the tip complex"] and shows
  a third Ca2+ site confirmed by ITC [PMID:30346996 "The calcium binding of XcpX was also confirmed
  by isothermal titration calorimetry"].

### Conflict on secretion requirement

Bleves et al. 1998 (abstract) report loss of XcpX function on mutating the conserved glycine.
Zhang et al. 2018, using PAO1 transposon mutants from the Manoil library, found the xcpX mutant
still secreted protease [PMID:30346996 "The WT, xcpU and xcpX mutant strains generated clear rim by
secreting protease while the xcpV and -W mutants did not because of the lack of the functional
T2SS"]. The insertion site was not given; a late insertion could leave a functional protein, and
in Klebsiella PulK deletion affects PulA secretion (cited in the same paper). The weight of
evidence (classic Xcp genetics, the GspK family role in tip assembly) still supports involvement in
T2SS secretion, but the necessity of XcpX for every substrate is open. Recorded as a question.

### PseudoCAP row details

- GO:0015627 IDA PMID:9466253: the abstract shows membrane location, PilD processing and
  pseudopilin classification; the full text (Mol Microbiol 1998) is not in PMC. Membership in the
  T2SS complex is independently shown by the tip-complex biochemistry (PMID:19828448) and the
  XcpVWX structure (PMID:30346996). The term is correct.
- GO:0015628 IDA PMID:9818381: this paper is a review (Filloux, Michel & Bally 1998, FEMS
  Microbiol Rev; PubMed type Review). The IDA is not supported: the full text has no original secretion data. The term is correct, and the
  primary evidence is Bleves et al. 1998 (mutational loss of function, i.e. IMP). Source defect
  recorded as WRONG_EVIDENCE_CODE / CHECK.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000475915 | GO:0015627 type II protein secretion system complex | 1 (sole seed) | 35 (28 taxa) | GO:0015627, IDA, PMID:9466253 | SOUND | XcpX is a GspK pseudopilin and is part of the pseudopilus tip complex (PMID:19828448, PMID:30346996). The cited abstract alone only shows membrane location and PilD processing, but the claim is correct and GspK is a conserved T2SS component, so the node term suits the GspK clade. |
| PTN000475915 | GO:0015628 protein secretion by the type II secretion system | 1 (sole seed) | 35 (28 taxa) | GO:0015628, IDA, PMID:9818381 | SOUND (term); evidence code WRONG (cited paper is a review with no original secretion data; full text checked) | Term is correct for GspK proteins. PMID:9818381 is a review, so IDA is not valid; the primary support is PMID:9466253 (IMP, glycine mutant loses function). A 2018 transposon mutant still secreted protease (PMID:30346996), a caveat but not a refutation. The IBD conclusion is sound; the seed should be re-keyed to PMID:9466253 IMP (or TAS for the review). |
