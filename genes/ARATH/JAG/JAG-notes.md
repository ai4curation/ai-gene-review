# JAG (ARATH) review notes

## 2026-10-28 initial review

- `just fetch-gene ARATH JAG` resolved Q6S591 (JAG_ARATH, At1g68480, GeneID 843177);
  18 GOA rows. PANTHER family fetch (PTHR45730) failed with an InterPro 500 error.
- Cached PMID:23133401 (full text), 22902754 (full text), 23653565 (full text),
  18156293 (full text), 26390296 (full text); 14973281, 14973282, 16192305,
  16554365, 24497510, 39260627 are abstract-only.
- No deep-research API available; manual synthesis in JAG-deep-research-manual.md.

Key points:
- JAG is a direct transcriptional repressor: ChIP on BP and BEL1 with
  cycloheximide-independent repression [PMID:22902754 "In both cases, reproducible
  binding was seen to specific regions upstream of the starting codon"]; ChIP-seq
  targets KRP2/KRP4, HAN, CLV1, BOP2 [PMID:24497510]; PTL [PMID:23653565].
- Hence GO:0003700 rows refined to GO:0001217 DNA-binding transcription repressor
  activity (is_a GO:0003700, checked with OAK), and GO:0006355 to GO:0045892.
- GO:0010093 specification of floral organ identity (IBA + IMP) judged an
  over-annotation: jag organs are mis-shaped, not mis-specified. Source defect
  recorded for the TAIR IMP row (CHECK); IBA follows the same node.
- GO:0010158 abaxial cell fate specification (IMP, PMID:16192305, abstract-only):
  undecided; abstract concerns valve margin gene activation, and the NUB/JAG paper
  reports adaxial cell type differentiation in carpel walls.
- Bare protein binding (HAN, IPI) removed per policy; interaction recorded in prose.
- Fruit patterning [PMID:23133401]: JAG/FIL lateral factors repress BP in medial
  domain; not added as NEW (genetic/expression evidence; covered by repressor MF).
- No NEW process terms proposed (CLAUDE.md NEW bar).
