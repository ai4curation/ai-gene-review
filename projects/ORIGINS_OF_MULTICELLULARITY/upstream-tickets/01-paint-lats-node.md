# PAINT, PTHR24356: tissue-level IBDs on the LATS node reach choanoflagellates

**Destination:** PAINT curators (GO annotation tracker, `geneontology/go-annotation`, label PAINT).

**Summary.** Node PTN002390470 in PTHR24356 carries four IBDs (from the
cached PAINT slice `interpro/panther/PTHR24356/PTHR24356-paint.tsv`):

| IBD term | Seeds |
|---|---|
| GO:0035329 hippo signaling | fly wts, mouse Lats1/Lats2, human LATS1/LATS2 |
| GO:0046620 regulation of organ growth | mouse Lats2 only |
| GO:0043065 positive regulation of apoptotic process | fly wts only |
| GO:0000082 G1/S transition of mitotic cell cycle | mouse Lats2, human LATS2 |

The node's descendants include the choanoflagellate Warts kinases:
- *Monosiga brevicollis* A9UVF9 receives all four by IBA.
- *Salpingoeca rosetta* F2U943 receives all four by TreeGrafter IEA, from leaf
  PTN001220369.

Choanoflagellates are unicellular and have no organs. GO's taxon constraints
on GO:0046620 do not exclude them, so nothing downstream blocks the row.

**Evidence.**
- QuickGO, 2026-10-01: GO:0046620 occurs on exactly two proteins in
  Choanoflagellata (A9UVF9 IBA, F2U943 IEA) and on none in Filasterea or
  Ichthyosporea.
- In *S. rosetta*, warts knockout doubles rosette cell number but slows growth
  (DOI:10.1101/2024.07.13.603360). This is not an organ phenotype.
- *Capsaspora* Warts loss has no effect on proliferation (PMID:38517944).
- No apoptosis data exist for choanoflagellate Warts.

**Requested change.**
- Move the GO:0046620 IBD from PTN002390470 to the metazoan descendant node,
  or add NOT/exceptions for the choanoflagellate leaves.
- Consider the same for GO:0043065, which rests on one seed.
- Keep hippo signaling on PTN002390470: it is supported by the *Capsaspora*
  data.

**Repo references.** `genes/SALRS/warts/warts-ai-review.yaml` (REMOVE organ
growth; apoptosis and G1/S over-annotated); `genes/human/LATS1/` (human rows
kept).
