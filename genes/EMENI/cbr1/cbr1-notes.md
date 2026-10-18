# cbr1 notes

## 2026-10-11

- Seeded `EMENI/cbr1` with 16 current GOA rows for Q5AZB4/AN6366.
  `just fetch-gene-pmids` found no GOA PMIDs because the current rows are
  GO_REF-based IBA, ISS, and IEA annotations.
- `just deep-research-falcon EMENI cbr1 --fallback perplexity-lite` failed
  because no deep-research provider credentials or `agentapi` are configured,
  so this review was done manually from the GOA seed, the Swiss-Prot record,
  the PTHR19370 PAINT rows, the cached S. cerevisiae Cbr1/Dph3 publications,
  and the completed CBR1-like reviews for Candida, Neurospora, and
  Schizosaccharomyces.
- Web searches for `Q5AZB4`, `AN6366`, and *Aspergillus nidulans* Cbr1 found
  no newer direct A. nidulans cbr1 functional paper. A 2025 A. nidulans paper
  instead characterizes a separate CBBR cytochrome b5/cytochrome b5 reductase
  fusion electron-transfer system with CYP540A2, not cbr1.

### CBR1-like activity

Q5AZB4 is in `PTHR19370:SF184`, the CBR1-like
NADH-cytochrome-b5-reductase branch. It retains the single predicted N-terminal
membrane anchor and the FAD/NADH-binding domain architecture found in the
characterized S. cerevisiae Cbr1 protein.

The current PAINT cache does not place `GO:0090524` or the broader
`GO:0004128` on the fungal SF184 branch that contains Aspergillus and
Neurospora CBR1 proteins. The only IBA on EMENI cbr1 is the family-root
`PTN001833551` `GO:0016491 oxidoreductase activity` row, which is correct but
intentionally broad across fungal CBR1/MCR1/PGA3, plant nitrate reductase, and
animal CYB5R branches.

### Dph3 transfer

S. cerevisiae Cbr1 directly reduces the iron protein Dph3 from NADH. Reduced
Dph3 is an electron carrier for the Elp3 radical-SAM tRNA wobble-modification
enzyme and for Dph1-Dph2 in the first step of diphthamide biosynthesis. Because
A. nidulans cbr1 is in the conserved fungal CBR1-like subfamily, the tRNA and
diphthamide process transfers are plausible outputs of the inferred Dph3
reductase activity.

`GO:0090560 2-(3-amino-3-carboxypropyl)histidine synthase activity` is too
specific for cbr1: that is the Dph1-Dph2 radical-SAM reaction that transfers
ACP to eEF2. Cbr1 provides reducing equivalents to Dph3; it does not perform the
ACP transfer itself. As in the other fungal CBR1 reviews, this should be
replaced by a GO term for NADH-dependent Dph3 reductase activity once GO has
one for RHEA:71231.
