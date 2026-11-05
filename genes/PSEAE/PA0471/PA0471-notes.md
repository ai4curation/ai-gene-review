# PA0471 (PA0471, Q9I647) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I647 --alias PA0471`; accession matches the worklist.
Unreviewed entry. No deep-research provider was used; literature from the cached papers and
PubMed MCP. Read with the cognate sigma review (PA0472 / foxI) for consistency.

### Literature

- Seed paper PMID:16484199 (Llamas et al. 2006): cached file is abstract only; the full text was
  read on the PMC article page (PMC1426570) on 2026-11-05. A fiuR transposon mutant (UW library)
  produces its receptor independent of the inducing siderophore, and the fiuA promoter is
  constitutively active (higher under iron restriction). The authors: "consistent with a role
  for ... an anti-sigma factor"; FoxR and FiuR "are not required for maximal activities of FoxI
  and FiuI". [PMID:16484199 "The involvement of this putative regulatory locus in the specific
  induction of the ferrioxamine B and ferrichrome receptors has been demonstrated"].
- PMID:35138377 (review, full text): [PMID:35138377 "The regulatory proteins FoxR and FiuR act as
  anti-sigma factors in that they inhibit the sigma factors FoxI and FiuI"]; the cytoplasmic
  N-terminal fragments have pro-sigma activity.
- PMID:39138320: the receptor (fiuA) imports hydroxamate iron-siderophores.
- UniProt Q9I647: FecR_N, FecR, PIRSF018266, one Phobius TM helix (88-106). No gene name in UniProt, so the folder uses the locus tag.

### Annotation decisions

- GO:0016989 sigma factor antagonist activity (IMP): ACCEPT, core MF.
- GO:0045892 (IEA, GO_REF:0000108): MODIFY to GO:2000143 negative regulation of DNA-templated
  transcription initiation.
- GO:0034756 regulation of iron ion transport (IMP): MODIFY to GO:0034757 negative regulation of
  iron ion transport (mutant derepresses the receptor), non-core. Mirrors the MODIFY to
  GO:0034758 positive regulation on the cognate sigma review.
- NEW GO:0005886 plasma membrane (IC): TM helix plus published description.
- Action counts: ACCEPT 1, MODIFY 2, NEW 1.
- GOA has no IBA rows on PA0471, although the PAINT leaf file assigns it the PTN001250434 IBA.

## PseudoCAP IBA-seed assessment

Node-level assessment: see `genes/PSEAE/fpvR/fpvR-notes.md` (recorded once there); summary below.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001250434 | GO:0016989 sigma factor antagonist activity | 4 | 53 (7 taxa) | GO:0016989, IMP, PMID:16484199 | SOUND | Full text (PMC page): the fiuR mutant expresses its receptor constitutively, independent of siderophore; derepression is the genetic signature of an anti-sigma factor, later confirmed (PMID:35138377). | fpvR (IMP, plus direct binding PMID:25433393), VreR (G3XCU5 merged into O69006), and foxR | Yes |

No source defects: the PseudoCAP row is sound and the IBD is sound.
